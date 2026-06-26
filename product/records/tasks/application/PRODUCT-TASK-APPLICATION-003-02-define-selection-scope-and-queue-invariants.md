# PRODUCT-TASK-APPLICATION-003-02: Define selection scope and queue invariants

- **id**: PRODUCT-TASK-APPLICATION-003-02
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-003
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-003-01
- **outputs**:

## Goal

Define `SelectionScope` and the domain invariants for one first-MVP complete-shuffle queue.

## Work

1. Use the classifications and evidence from PRODUCT-TASK-APPLICATION-003-01.
2. Define the implementation-independent meaning of `SelectionScope`.
3. Define the first-MVP `all` scope as the unrestricted set of currently available eligible units.
4. Confirm that `all` does not require every eligible unit to enter one queue.
5. Define the maximum of 100 references as application policy.
6. Define uniqueness within one queue and allowed repetition across later queues.
7. Define the result when fewer than 100 eligible units are available.
8. Define queue ordering as randomized without selecting an algorithm.
9. Define the absence of reservation, backend queue identity, backend queue position, and queue history.
10. Define extension boundaries for source, topic, discussion, difficulty, and learner-history scopes.
11. Keep learner-history scope behind a separate durable identity and progress decision.
12. Determine whether any adopted result requires a new ADR.
13. Record the resolved design and ADR judgment in `## Evidence`.
14. Leave adapter execution and invalid-result handling to PRODUCT-TASK-APPLICATION-003-03.

## Done condition

- `SelectionScope` has one precise semantic meaning.
- The first-MVP scope is exactly `all`.
- Every currently available unit is eligible under `all` without requiring full-corpus queue materialization.
- One queue contains at most 100 references.
- One queue contains no duplicate reference.
- A later queue may repeat a reference from an earlier queue.
- Fewer than 100 eligible units produce a smaller valid queue.
- Queue ordering is randomized semantically.
- Queue issuance creates no learner-specific reservation or backend queue state.
- Future non-history scopes extend the scope model without moving queue state to the backend.
- Learner-history scope remains deferred behind a separate ownership decision.
- The ADR requirement judgment is explicit.
- T03 has sufficient domain inputs to define adapter obligations and validation.

## Verification

- Compare every resolved invariant with PRODUCT-ADR-APPLICATION-001.
- Confirm that queue cardinality is bounded rather than equal to total availability.
- Confirm that uniqueness applies only within one queue.
- Confirm that later repetition remains allowed.
- Confirm that the domain model does not depend on SQL, database, HTTP, or framework types.
- Confirm that PWA queue position remains owned by `spec:product.ui.learning_flow`.
- Confirm that any new architectural decision has an accepted ADR before task completion.

## Evidence

### Result

- **Verdict**: PASS.
- `SelectionScope` and all first-MVP queue invariants are explicit.
- No new ADR is required.
- The resolved rules refine PRODUCT-ADR-APPLICATION-001 without changing ownership, dependency direction, or accepted queue policy.

### SelectionScope

`SelectionScope` defines content-based eligibility constraints for one selection operation.

Availability is a separate universal eligibility gate owned by the published-content contract.

A learning unit is eligible only when:

- the unit is currently available during the selection operation;
- the unit satisfies the requested `SelectionScope`.

The first MVP supports exactly one scope:

```text
SelectionScope = All
```

`All` adds no content-based constraint.

The eligible candidate set for `All` is every learning unit observed as currently available during the selection operation.

`All` does not require every eligible unit to enter one queue when the eligible count exceeds the queue maximum.

The first-MVP PWA does not choose or submit a scope value.
`CreateCompleteShuffleQueue` applies `All` as application policy.

### Queue cardinality

Let:

- `eligible_count` be the number of unique units satisfying availability and scope during the selection operation;
- `maximum_count` be the application policy value `100`.

The required queue size is:

```text
queue_size = min(maximum_count, eligible_count)
```

| eligible count | required result size |
|---|---|
| `0` | `0`; an empty queue is a valid no-eligible-unit result. |
| `1..99` | Exactly `eligible_count`; every eligible unit appears once. |
| `100 or more` | Exactly `100` unique references. |

The adapter must not intentionally return fewer references when additional eligible units exist during the same selection operation.

The application and PWA do not receive `eligible_count`.
They determine the queue length from the returned reference array.

The application is not required to detect underfill independently.
The adapter implementation and adapter tests must enforce the exact cardinality contract.

### Queue invariants

- The queue contains only stable learning-unit references.
- The queue contains no duplicate reference.
- Uniqueness applies only within one queue result.
- A later queue request may return any reference returned by an earlier request.
- Each queue request is independent from earlier queue requests.
- Queue issuance creates no learner-specific reservation.
- Queue issuance creates no backend queue identity.
- The backend retains no queue position, queue history, or learner progress.
- The PWA remains the owner of transient queue position and progression.
- Queue ordering is randomized by the selection implementation.
- Randomized ordering defines no ranking preference or deterministic repository order.
- Exact algorithms and statistical quality guarantees remain implementation details.

### Future scope extension boundary

Future non-history scopes may constrain candidates by:

- source;
- topic;
- discussion;
- difficulty.

Future non-history constraints combine by intersection.
A candidate must satisfy every constraint present in the scope.

The scope model has two semantic forms:

```text
All
| Constrained(non_empty_constraints)
```

`All` and `Constrained` are mutually exclusive.
An empty constrained set is represented as `All`.

Every non-history constraint must be evaluable from the published runtime boundary.
A scope must not require the application to inspect pipeline processing data.

The scope value contains only candidate-selection constraints.
The scope value must not contain queue position, prior queue references, learner answers, or progress state.

Learner-history selection remains excluded.
Learner-history selection requires a separate decision for durable learner identity, progress ownership, and history access.

### T03 inputs

T03 must preserve these adapter-facing invariants:

- apply current availability and the requested scope to the same selection operation;
- return exactly `min(maximum_count, eligible_count)` references;
- return unique references;
- return references in randomized order;
- return only the ordered learning-unit reference array to the application;
- do not expose `eligible_count` to the application or PWA;
- allow the adapter to satisfy exact cardinality without returning a total count;
- allow database-side bounded selection;
- avoid loading the complete candidate set into the domain layer;
- treat an empty exact result as valid;
- enforce unexplained underfill through adapter implementation and tests;
- keep later availability changes outside selection-result validity.

T03 owns validation placement and invalid-result handling for invariants observable from the returned array.
The application may validate maximum count, uniqueness, and reference validity.
The application is not required to validate underfill.
T03 does not reopen the scope or queue invariants resolved here.

### ADR judgment

No new ADR is required.

The strict cardinality rule and composable non-history scope boundary are detailed application-domain contracts.
They do not change the accepted architecture in PRODUCT-ADR-APPLICATION-001.

A new ADR is required before learner-history selection introduces durable learner-specific state or changes queue-state ownership.

### Verification

- `All` preserves every currently available unit as an eligible candidate.
- `All` does not imply full-corpus queue materialization above 100 eligible units.
- Queue size is exact and bounded.
- Uniqueness applies within one queue only.
- Later repetition remains allowed.
- No reservation or backend queue state was introduced.
- Future non-history constraints preserve PWA queue-state ownership.
- No SQL, database, transport, or framework type entered the contract.
