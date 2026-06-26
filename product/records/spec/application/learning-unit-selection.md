# Concept: Learning-unit selection

- **id**: `spec:product.application.learning_unit_selection`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.application`

## What this is

Application model for creating bounded shuffle queues and retrieving one complete published learning unit.
The model keeps learner queue state in the PWA and selection execution behind semantic query ports.

## Non-goals

- Learner history, recommendation ranking, and progress-aware selection.
- Topic, discussion, source, or difficulty controls in the first MVP.
- Backend queue identity, queue persistence, and reservation.
- Exact randomization, sampling, and database query algorithms.
- HTTP routes, status-code mappings, and wire schemas.
- PWA retry timing and presentation behavior.

## Concept model

```text
CreateCompleteShuffleQueue
  input:
    scope = all

  policy:
    max_units = 100
    unique_within_queue = true

  result:
    ordered learning_unit_refs[]
```

```text
GetPublishedLearningUnit
  input:
    learning_unit_ref

  result:
    Found(complete_learning_unit)
    | Unavailable
```

| layer | responsibility |
|---|---|
| Application domain | Define selection scope, queue bounds, uniqueness, and availability rules. |
| Application use case | Coordinate domain policy and outbound queries. |
| Outbound query port | Express runtime selection and retrieval operations semantically. |
| Database adapter | Execute availability filtering, bounded sampling, ordering, and content loading. |
| PWA | Keep queue position, skip unavailable references, and own learner session progress. |

## Rules

### Application use cases

The first MVP application must provide these semantic behaviors:

- `CreateCompleteShuffleQueue`;
- `GetPublishedLearningUnit`.

`CreateCompleteShuffleQueue` must not load complete learning-unit content.
`GetPublishedLearningUnit` must return one complete unit or an unavailable result.

### Complete-shuffle queue

- The first MVP selection scope must be all available learning units.
- A queue must contain at most 100 learning-unit references.
- A queue must contain no duplicate reference.
- A queue may contain fewer than 100 references when fewer units are available.
- Queue ordering must be randomized by the selection implementation.
- The same learning unit may appear in a later queue.
- Queue exhaustion must allow the PWA to request another queue.
- Queue generation must use availability observed during that request.
- Queue generation must not create a learner-specific reservation.
- The application must not retain queue position or queue history.

The name `complete shuffle` identifies the unrestricted first-MVP selection scope.
The name does not require one queue to contain every available unit.

### Retrieval and availability

- Retrieval must recheck current availability.
- Retrieval must return the complete current content only when the unit remains available.
- A missing or unavailable reference must produce `Unavailable`.
- `Unavailable` must not be treated as a transient infrastructure failure.
- `Unavailable` must allow the PWA to bypass that reference and try another queued reference.
- Network and server failures must remain distinct from `Unavailable`.
- A queue containing only stale references may be exhausted and replaced.

### Domain and application separation

- Domain rules must define valid scope, maximum queue size, uniqueness, and availability requirements.
- Application use cases must coordinate ports and domain rules.
- Domain rules must not depend on SQL, database tables, HTTP, or framework types.
- Application results must remain transport-independent.
- Transport adapters may map `Unavailable` to a transport-specific not-found response.

### Query-port semantics

The application must depend on semantic outbound operations rather than generic CRUD.

Examples, not exhaustive:

```text
SelectAvailableLearningUnitReferences
  input:
    scope
    maximum_count

  result:
    randomized unique references
```

```text
LoadAvailablePublishedLearningUnit
  input:
    learning_unit_ref

  result:
    current complete publication
    | unavailable
```

- The selection port must allow the database adapter to perform bounded random selection.
- The selection port must not require loading every candidate reference into the domain layer.
- The adapter must satisfy the port contract for availability, scope, maximum count, uniqueness, and ordering.
- The exact sampling algorithm must remain adapter-owned.

### Extensibility

Future selection scopes may include source, topic, discussion, difficulty, or learner history.
Future scopes must extend the selection model without moving transient queue state into the application.
Learner-history selection may require a separate decision about durable learner identity and progress.

## Boundary

| concern | owner |
|---|---|
| Selection invariants and application orchestration | `spec:product.application.learning_unit_selection` |
| Current published content and availability | `spec:product.application.published_content` |
| Learning-unit semantic composition | `spec:product.learning.learning_unit` |
| PWA queue position, retry flow, and session state | `spec:product.ui.learning_flow` |
| Database sampling and transport mapping | Implementation adapters. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application` | Parent application overview. |
| `spec:product.application.published_content` | Defines the runtime records selected and retrieved. |
| `spec:product.learning.learning_unit` | Defines the complete content returned by retrieval. |
| `spec:product.ui.learning_flow` | Owns queue position and stale-reference skipping behavior. |
| PRODUCT-ADR-APPLICATION-001 | Establishes the use cases, layering, and bounded queue decision. |
