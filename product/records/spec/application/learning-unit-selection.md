# Concept: Learning-unit selection

- **id**: `spec:product.application.learning_unit_selection`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.application`

## What this is

Application contract for bounded learning-unit reference selection and availability-aware retrieval.
The contract keeps transient queue state in the PWA and selection execution behind semantic query ports.

## Non-goals

- Learner history, recommendation ranking, and progress-aware selection.
- Topic, discussion, source, or difficulty controls in the first MVP.
- Backend queue identity, queue persistence, reservation, and queue history.
- Total eligible count in application or PWA results.
- Exact randomization, sampling, and database query algorithms.
- HTTP routes, status-code mappings, and wire schemas.
- PWA queue position, retry timing, and learner progression.

## Concept model

```text
SelectionScope =
  All
  | Constrained(non_empty_constraints)
```

```text
CreateCompleteShuffleQueue
  application policy:
    selection_scope = All
    maximum_count = 100

  selection operation:
    input:
      selection_scope
      maximum_count

    output:
      ordered learning_unit_refs[]
```

```text
GetPublishedLearningUnit
  input:
    learning_unit_ref: LearningUnitRef

  result:
    Available(complete_learning_unit)
    | Unavailable
```

| layer | responsibility |
|---|---|
| Published-content contract | Define current availability and the available or unavailable runtime state. |
| Application domain | Define selection scope, queue cardinality, uniqueness, ordering semantics, and result validity. |
| Application use case | Apply first-MVP policy, coordinate outbound queries, and reject observable invalid results. |
| Outbound selection operation | Express bounded randomized learning-unit reference selection. |
| Outbound retrieval port | Retrieve one published learning unit by `LearningUnitRef` and return `Available(complete_learning_unit) \| Unavailable`. |
| Persistence adapter | Apply availability and scope, then perform bounded randomized reference selection and content loading. |
| PWA | Store the returned ordered reference array, keep queue position, and own learner progression. |

## Definitions

| term | definition |
|---|---|
| `LearningUnitRef` | A stable reference identifying one published learning unit within the published-content boundary. The exact format is an implementation detail. |
| `outbound retrieval port` | An application-owned semantic boundary that declares the capability required to retrieve one published learning unit by reference. The persistence adapter implements this port. |
| `Available` | A retrieval result indicating that the referenced learning unit exists and is currently available to a new learner flow. See `spec:product.application.published_content` for availability semantics. |
| `Unavailable` | A retrieval result indicating that no current state exists for the reference, or that the current unit is not available to a new learner flow. `Unavailable` is not a mapping failure or infrastructure failure. |

## Rules

### Application use cases

The first MVP application must provide these semantic behaviors:

- `CreateCompleteShuffleQueue`;
- `GetPublishedLearningUnit`.

`CreateCompleteShuffleQueue` must not load complete learning-unit content.
`GetPublishedLearningUnit` must return one complete unit or `Unavailable`.

The first-MVP PWA must not choose or submit a selection scope or maximum count.
`CreateCompleteShuffleQueue` must apply `All` and `100` as application policy.

The PWA must receive only the accepted ordered learning-unit reference array.
The result must not include a total eligible count, queue identity, reservation token, backend position, or queue history.

### Selection scope

`SelectionScope` defines content-based constraints for one selection operation.

A candidate is eligible only when both conditions hold:

- the candidate is currently available under `spec:product.application.published_content` during the selection operation;
- the candidate satisfies the requested `SelectionScope`.

`All` adds no content-based constraint.
The first MVP supports only `All`.

`All` includes every currently available unit in the eligible candidate set.
`All` does not require one queue to contain the complete eligible corpus.

Future non-history constraints may cover source, topic, discussion, and difficulty.
Future non-history constraints must combine by intersection.
A constrained scope must contain at least one constraint.
An empty constraint set must be represented as `All`.

Every non-history constraint must be evaluable from the published runtime boundary.
A scope must not contain queue position, prior queue references, learner answers, or learner progress.

Learner-history selection remains excluded.
A separate decision must establish durable learner identity, progress ownership, and history access before learner-history selection is added.

### Complete-shuffle cardinality

`maximum_count` is application policy.
The first-MVP value is `100`.

`eligible_count` is the number of unique candidates satisfying current availability and the requested scope during selection.
`eligible_count` is a semantic quantity used to define adapter cardinality.
The application and PWA must not receive `eligible_count`.

```text
queue_size = min(maximum_count, eligible_count)
```

| eligible count | required result size |
|---|---|
| `0` | `0`; an empty queue is valid. |
| `1..99` | Exactly `eligible_count`. |
| `100 or more` | Exactly `100`. |

The adapter must not intentionally underfill the result while additional eligible candidates exist during the operation.
The adapter contract does not require a separate total-count query or total-count result.

### Queue invariants

- One queue result must contain stable `LearningUnitRef` values only.
- One queue result must contain no duplicate reference.
- Uniqueness applies only within one result.
- A later queue may repeat references from an earlier queue.
- Returned order must be randomized by the selection implementation.
- The application must preserve the accepted returned order.
- Queue issuance must create no learner-specific reservation.
- The backend must retain no queue identity, position, history, or learner progress.
- Exact randomization algorithms and statistical distribution guarantees remain implementation details.

### Semantic selection operation

The application must depend on one bounded semantic selection operation.

```text
input:
  selection_scope
  maximum_count

output:
  ordered learning_unit_refs[]
```

The adapter must:

- select only references currently available during the operation;
- select only references satisfying `selection_scope`;
- return exactly `min(maximum_count, eligible_count)` references;
- return unique stable `LearningUnitRef` values;
- return references in randomized order;
- preserve the returned order;
- allow bounded selection inside the database;
- avoid loading the complete candidate set into application memory;
- retain no learner-specific queue state.

The exact sampling algorithm, query, index, query plan, transaction, isolation mechanism, and persistence technology remain implementation details.

### Validation boundary

The application must validate only properties observable from the returned array.

| invariant | application validation | adapter contract verification |
|---|---|---|
| Result length does not exceed `maximum_count` | Required. | Required. |
| References are unique within the array | Required. | Required. |
| Every element is a valid `LearningUnitRef` | Required. | Required at persistence-to-domain mapping. |
| References were available during selection | Not independently observable. | Required. |
| References satisfy the requested scope | Not independently observable from reference identity alone. | Required. |
| Result has exact cardinality | Not independently observable without candidate-total information. | Required. |
| Ordering was randomized | Not provable from one returned array. | Required. |

The application must not query or receive `eligible_count` only to revalidate adapter behavior.
The application must not infer underfill from an array containing fewer than `maximum_count` references.

Adapter contract tests must cover zero, below-limit, exact-limit, and above-limit eligible candidate sets.
Adapter contract tests must also cover unavailable candidates and every supported constrained scope.
Random-selection tests must verify randomized selection rather than fixed repository order.
The contract defines no statistical distribution threshold.

### Invalid returned arrays

Observable invalid results must be rejected as a complete result.
Observable invalid results must not be normalized into a queue.

| returned array | handling |
|---|---|
| More than `maximum_count` references | Reject the complete result. |
| Duplicate references | Reject the complete result. |
| Malformed or invalid reference | Fail domain mapping or reject the complete result. |
| Empty array | Accept as a valid result. |
| Fewer than `maximum_count` references | Accept because underfill is not observable from the array alone. |

The application must not:

- truncate an over-limit array;
- remove duplicate references;
- discard malformed references and return a partial queue;
- retry only because fewer than `maximum_count` references were returned.

The rejection must be a transport-independent application failure.
Concrete error types and transport mappings remain deferred.

### Retrieval and availability timing

Queue selection must use availability observed during queue creation.
A later withdrawal must not retroactively invalidate the accepted queue result.

Retrieval must independently recheck current availability.
Retrieval must return the complete current content only when the unit remains available.
A missing or unavailable reference must produce `Unavailable`.

`Unavailable` must remain distinct from infrastructure failure.
The PWA owns removal and skipping of an unavailable queued reference.
A learning unit already loaded into the PWA remains governed by the UI loaded-content contract.

### Outbound retrieval port

The application owns the `GetPublishedLearningUnit` outbound retrieval port.
The port accepts one `LearningUnitRef` and returns `Available(complete_learning_unit) | Unavailable`.
The persistence adapter implements the outbound retrieval port.

The persistence adapter must:

- read the committed current published state for the supplied reference;
- read the committed availability value;
- return `Available(complete_learning_unit)` when current content exists and is currently available;
- return `Unavailable` when no current state exists for the reference;
- return `Unavailable` when current content exists but is not currently available;
- map persisted complete content into the learning-unit contract;
- keep provenance inside the published-content boundary;
- propagate mapping and infrastructure failures as technical failures.

The persistence adapter must not decide whether a learning unit should be available.
The pipeline owns the availability decision and stores its result during publication or availability change.
The application use case coordinates the outbound port result.
The application use case does not receive a published projection containing separate content, availability, and provenance fields.

### Domain and adapter separation

- Application domain rules must not depend on SQL, database tables, HTTP, or framework types.
- Application results must remain transport-independent.
- Outbound operations must express selection and retrieval semantics rather than generic CRUD.
- Persistence adapters may perform filtering, bounded sampling, ordering, and loading inside persistence.
- Adapter implementation details must not redefine selection invariants.

## Boundary

| concern | owner |
|---|---|
| Selection scope, cardinality, result validity, and application orchestration | `spec:product.application.learning_unit_selection` |
| Current availability meaning and published runtime state | `spec:product.application.published_content` |
| Learning-unit semantic composition | `spec:product.learning.learning_unit` |
| PWA queue storage, position, exhaustion, retry, skipping, and progression | `spec:product.ui.learning_flow` |
| Database sampling, persistence, and transport mapping | Implementation adapters. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application` | Parent application overview. |
| `spec:product.application.published_content` | Defines current availability and the runtime records selected and retrieved. |
| `spec:product.learning.learning_unit` | Defines the complete content returned by retrieval. |
| `spec:product.ui.learning_flow` | Owns the returned queue state, queue progression, and stale-reference skipping. |
| PRODUCT-ADR-APPLICATION-003 | Establishes use cases, retrieval result names, and the current published-content boundary. |
| PRODUCT-ADR-APPLICATION-004 | Establishes the outbound retrieval-port result shape and persistence-adapter obligations. |
