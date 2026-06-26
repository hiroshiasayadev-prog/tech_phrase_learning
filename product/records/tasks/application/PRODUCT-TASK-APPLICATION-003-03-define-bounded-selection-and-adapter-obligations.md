# PRODUCT-TASK-APPLICATION-003-03: Define bounded selection and adapter obligations

- **id**: PRODUCT-TASK-APPLICATION-003-03
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-003
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-003-02
- **outputs**:

## Goal

Define bounded random selection semantics, adapter obligations, observable result validation, and contract-verification boundaries.

## Work

1. Use the scope and queue invariants resolved by PRODUCT-TASK-APPLICATION-003-02.
2. Define one semantic bounded-selection operation without selecting a concrete port name or wire shape.
3. Define operation inputs for scope and maximum count.
4. Define the adapter obligation to select only units available during the selection operation.
5. Define adapter obligations for scope matching, maximum count, uniqueness, and randomized ordering.
6. Preserve database-side bounded selection without loading every candidate reference into the domain layer.
7. Define the ordered learning-unit reference array as the only selection result returned to the application.
8. Do not expose total eligible count to the application or PWA.
9. Define which invariants are observable and validatable from the returned array.
10. Define transport-independent handling for duplicate, over-limit, malformed, or otherwise invalid returned arrays.
11. Decide whether observable invalid results are rejected or normalized for each invariant.
12. Assign availability, scope matching, exact cardinality, and randomized selection verification to adapter tests when the returned array cannot prove them.
13. Clarify that the application cannot distinguish valid under-100 cardinality from underfill using the returned array alone.
14. Distinguish selection-time availability from later withdrawal before unit retrieval.
15. Keep exact randomization, SQL, indexes, query plans, and database-specific failure handling outside the contract.
16. Determine whether any adopted result requires a new ADR.
17. Record the operation, obligations, validation boundary, invalid-result policy, and ADR judgment in `## Evidence`.
18. Leave specification reflection to PRODUCT-TASK-APPLICATION-003-04.

## Done condition

- The bounded-selection operation has explicit semantic inputs and returns only an ordered learning-unit reference array.
- The maximum count remains application policy rather than adapter policy.
- The adapter selects from currently available units matching the requested scope.
- The adapter returns exactly the cardinality required by PRODUCT-TASK-APPLICATION-003-02.
- The adapter returns unique references in randomized order.
- The adapter may perform bounded selection inside the database.
- The contract does not require full candidate loading into application memory.
- The application and PWA do not receive total eligible count.
- Application or domain validation is limited to invariants observable from the returned array.
- Adapter tests cover availability, scope matching, exact cardinality, and randomized selection obligations that the array cannot prove independently.
- Observable invalid-result handling is explicit and transport-independent.
- An empty or under-100 array may be valid; the application does not infer underfill from array length alone.
- Later unavailability does not retroactively make a selection-time result invalid.
- The ADR requirement judgment is explicit.
- T04 has sufficient inputs to reflect the design in current specifications.

## Verification

- Trace each adapter obligation to a domain invariant from PRODUCT-TASK-APPLICATION-003-02.
- Confirm that the operation remains semantic rather than generic CRUD.
- Confirm that invalid-result handling does not depend on HTTP status codes or database exceptions.
- Confirm that the operation does not return total eligible count to the application or PWA.
- Confirm that application validation uses only the returned array.
- Confirm that adapter-contract verification does not require loading the full eligible candidate set into application memory.
- Confirm that later retrieval still rechecks availability independently.
- Confirm that no exact algorithm, SQL, index, or persistence technology enters the design.
- Confirm that any new architectural decision has an accepted ADR before task completion.

## Evidence

### Result

- **Verdict**: PASS.
- The semantic selection operation, adapter obligations, validation boundary, and invalid-result policy are explicit.
- The application and PWA receive only an ordered learning-unit reference array.
- No new ADR is required.

### Semantic bounded-selection operation

The application depends on one semantic operation that selects available learning-unit references.

```text
input:
  selection_scope
  maximum_count

output:
  ordered learning_unit_refs[]
```

The first-MVP use case supplies:

```text
selection_scope = All
maximum_count = 100
```

The PWA does not supply either value in the first MVP.
The PWA receives the returned reference array as its transient queue.

The operation does not return:

- total eligible count;
- queue identity;
- reservation token;
- backend queue position;
- queue history;
- complete learning-unit content.

`maximum_count` is application policy.
The adapter must honor the supplied value without replacing it with an adapter-owned default.

### Adapter obligations

The adapter must apply availability and scope within one semantic selection operation.

The adapter must:

- select only references currently available during the operation;
- select only references satisfying `selection_scope`;
- return exactly `min(maximum_count, eligible_count)` references;
- return each reference at most once;
- return the references in randomized order;
- return stable learning-unit references only;
- preserve the order in the returned array;
- perform bounded selection without requiring the full candidate set in application memory.

`eligible_count` is a semantic quantity used to define exact cardinality.
The contract does not require the adapter to materialize, count, or return the full candidate total.

The adapter may execute filtering, bounded sampling, and ordering inside the database.
The exact algorithm, query, index, and isolation mechanism remain implementation details.

The adapter must not retain learner-specific state after the operation.

### Validation boundary

The application validates only invariants observable from the returned array.

| invariant | application validation | adapter contract test |
|---|---|---|
| Result count does not exceed `maximum_count` | Required. | Required. |
| References are unique within the array | Required. | Required. |
| Every element is a valid `LearningUnitRef` domain value | Required through domain-value construction or result validation. | Required at persistence-to-domain mapping. |
| References were available during selection | Not independently observable. | Required. |
| References satisfy the requested scope | Not independently observable from reference identity alone. | Required. |
| Result has exact cardinality when additional candidates exist | Not independently observable without candidate-total information. | Required. |
| Ordering was randomized | Not provable from one returned array. | Required at the adapter behavior boundary. |

The application does not receive `eligible_count` only to revalidate adapter behavior.
The application does not query the full candidate set after bounded selection.

Adapter contract tests must cover known candidate sets for:

- zero eligible units;
- fewer than 100 eligible units;
- exactly 100 eligible units;
- more than 100 eligible units;
- unavailable candidates;
- future supported scope constraints.

Random-selection tests must verify use of randomized selection rather than fixed repository ordering.
The contract defines no statistical distribution threshold.

### Invalid returned-array policy

Observable invalid results are rejected.
They are not normalized into a queue.

| returned result | handling |
|---|---|
| More than `maximum_count` references | Reject the complete result. |
| Duplicate references | Reject the complete result. |
| Malformed or invalid reference | Fail domain mapping or reject the complete result. |
| Empty array | Accept as a valid queue result. |
| Array smaller than `maximum_count` | Accept because the application cannot infer underfill from array length alone. |

The application must not:

- truncate an over-limit array;
- remove duplicate references;
- discard malformed elements and return a partial queue;
- retry selection solely because the result contains fewer than 100 references.

Rejecting the complete result preserves adapter defects for diagnosis.
Normalization would hide a broken adapter contract.

The rejection is a transport-independent application failure.
The rejection is not an empty queue and not an unavailable learning-unit result.
Concrete error names and transport mappings remain outside this task.

### Availability timing

Availability is evaluated during queue selection.
A later withdrawal does not retroactively invalidate the returned queue.

Retrieval rechecks availability for each queued reference.
The PWA skips a reference that later produces `Unavailable`.

The selection adapter does not reserve availability.

### ADR judgment

No new ADR is required.

The operation shape, validation boundary, and reject-without-normalization policy refine the accepted application architecture.
They do not change ownership, dependency direction, database-side bounded selection, or PWA queue-state ownership.

### T04 inputs

T04 must reflect these contracts in `spec:product.application.learning_unit_selection`:

- `SelectionScope` and the first-MVP `All` policy;
- exact bounded cardinality as an adapter obligation;
- ordered `LearningUnitRef[]` as the only selection result;
- no total eligible count in the application or PWA result;
- database-side bounded selection compatibility;
- application validation for count, uniqueness, and valid reference values;
- adapter contract-test ownership for availability, scope, underfill, and randomized selection;
- rejection without normalization for observable invalid results;
- retrieval-time availability recheck after later withdrawal.

T04 must not add SQL, algorithms, indexes, transport schemas, or persistence technology.

### Verification

- Every adapter obligation traces to a T02 domain invariant.
- The operation is semantic rather than generic CRUD.
- The returned value is only an ordered learning-unit reference array.
- No total candidate count is exposed to the application or PWA.
- Application validation requires no full candidate loading.
- Observable invalid results are rejected without normalization.
- Empty and under-100 arrays remain valid application results.
- Later retrieval still rechecks availability independently.
- No concrete algorithm, SQL, index, transport, or framework decision entered the design.
