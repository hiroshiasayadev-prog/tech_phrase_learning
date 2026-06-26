# PRODUCT-TASK-APPLICATION-005-03: Define adapter and verification obligations

- **id**: PRODUCT-TASK-APPLICATION-005-03
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-005
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-005-02
- **outputs**:

## Goal

Prepare a complete authority-backed contract map for outbound query adapters and their verification boundaries.

Keep application tests separate from persistence-adapter contract tests.

## Work

1. Read the T005-01 inventory and the T005-02 authority disposition.
2. Stop as `blocked` when a normative obligation lacks accepted ADR authority.
3. Define application-owned inputs and normal results for selection and retrieval.
4. Preserve the dependency direction from persistence adapter to application-owned outbound contract.
5. Define persistence-adapter obligations for bounded selection.
6. Define persistence-adapter obligations for current published-unit retrieval.
7. Keep selection and retrieval as distinct operations.
8. Separate normal empty selection results from selection technical failures.
9. Preserve `Unavailable` as a normal retrieval result.
10. Preserve mapping and infrastructure failures as technical failures.
11. Define the application-test boundary using test doubles for outbound contracts.
12. Define persistence-adapter contract-test coverage against the real adapter boundary.
13. Cover zero, below-limit, exact-limit, and above-limit selection candidate sets.
14. Cover unavailable candidates, uniqueness, stable-reference mapping, and randomized returned order.
15. Cover available, missing, unavailable, mapping-failure, and infrastructure-failure retrieval cases.
16. Keep concrete database products, fixtures, containers, queries, and algorithms deferred.
17. Record the contract map as task evidence for T005-04.

This task must not become canonical decision or specification authority.
Any new normative decision must return to T005-02 and an accepted ADR.

## Done condition

- Selection and retrieval inputs and results are separately mapped.
- Application and persistence-adapter responsibilities are explicit.
- Normal outcomes and technical failures are separated.
- Application-test test doubles have a defined boundary.
- Persistence-adapter contract tests have defined required coverage.
- Every normative obligation traces to an accepted ADR.
- Implementation details remain deferred.
- T005-04 can reflect the contract without inventing decisions.

## Verification

- Trace every obligation to PRODUCT-ADR-APPLICATION-003, PRODUCT-ADR-APPLICATION-004, or an accepted T005-02 ADR.
- Confirm task evidence contains no unsupported normative claim.
- Confirm selection tests cover observable and adapter-owned guarantees separately.
- Confirm retrieval tests preserve `Available | Unavailable` semantics.
- Confirm contract tests exercise the persistence adapter rather than another mock.
- Confirm database and transport implementation choices remain absent.

## Evidence

### Result

- **Verdict**: PASS.
- This evidence records a contract map for T005-04.
- This task is not decision authority.
- No new ADR is required.
- No specification changed in this task.
- Authority conflicts: none.
- Genuine decisions required: none.

### Contract map

#### 1. Selection input and normal result

topic:
Selection input and normal result.

authority:
`spec:product.application`, `spec:product.application.learning_unit_selection`.

existing contract:
The application owns `CreateCompleteShuffleQueue`.
The first MVP supplies `SelectionScope = All` and `maximum_count = 100`.
The selection operation receives `selection_scope` and `maximum_count`.
The normal result is an ordered `LearningUnitRef[]`.
An empty array is a valid normal result when there are zero eligible candidates.
The result does not include `eligible_count`, queue identity, reservation token, backend position, or queue history.

contradiction or gap:
none.

T005-04 action:
Reflect this contract in the outbound selection-query specification.
Keep the selection use case separate from the persistence adapter obligations.

#### 2. Selection normal result and technical failure boundary

topic:
Selection normal result and technical failure separation.

authority:
`spec:product.application.learning_unit_selection`, `spec:product.application.published_content`.

existing contract:
Zero candidates produce an empty ordered reference array as a normal result.
Duplicate references are an observable invalid result.
Over-limit arrays are an observable invalid result.
Malformed references fail domain mapping or reject the complete result.
The application must not truncate, deduplicate, discard malformed entries, or return a partial queue.
Persistence mapping failure and database or infrastructure failure are technical failures.
Technical failures must not be converted into an empty queue or a normalized partial result.

contradiction or gap:
missing spec reflection.
The current selection spec has the boundary, but T005-04 must place the outbound-query failure boundary in the focused outbound-query topic.

T005-04 action:
State that empty selection is a normal result.
State that mapping and infrastructure failures are outside the normal selection result.
State that observable invalid arrays are rejected rather than normalized.

#### 3. Selection application validation

topic:
Selection properties validated by the application.

authority:
`spec:product.application.learning_unit_selection`.

existing contract:
The application validates only properties observable from the returned array.
The application validates that result length does not exceed `maximum_count`.
The application validates uniqueness within the returned array.
The application validates that each element is a valid `LearningUnitRef`.
The application preserves the accepted returned order.
The application cannot independently validate availability filtering, scope filtering, exact cardinality, or randomization from the returned array alone.
The application must not request `eligible_count` only to revalidate adapter behavior.

contradiction or gap:
none.

T005-04 action:
Move observable application validation rules into the selection result-validation topic.
Keep adapter-owned guarantees out of application validation.

#### 4. Selection persistence-adapter guarantees

topic:
Selection properties guaranteed by the persistence adapter.

authority:
`spec:product.application`, `spec:product.application.learning_unit_selection`, `spec:product.application.published_content`.

existing contract:
The persistence adapter implements the application-owned selection operation.
The adapter filters by current availability during the operation.
The adapter applies `SelectionScope`.
The adapter returns exactly `min(maximum_count, eligible_count)` references.
The adapter returns unique stable `LearningUnitRef` values.
The adapter returns references in randomized order.
The adapter preserves the returned order.
The adapter retains no learner-specific queue state.
The adapter may perform bounded selection inside persistence.
Exact randomization algorithms, queries, indexes, query plans, transactions, isolation mechanisms, and persistence technology are implementation details.

contradiction or gap:
none.

T005-04 action:
Reflect adapter guarantees in the outbound selection-query specification.
Keep algorithm, query, schema, and technology choices deferred.

#### 5. Retrieval input, normal result, and failure boundary

topic:
Retrieval input, normal result, and technical failure boundary.

authority:
PRODUCT-ADR-APPLICATION-003, PRODUCT-ADR-APPLICATION-004, `spec:product.application.learning_unit_selection`, `spec:product.application.published_content`, `spec:product.learning.learning_unit`, `spec:product.pipeline`.

existing contract:
The application owns `GetPublishedLearningUnit`.
The outbound retrieval port accepts one stable `LearningUnitRef`.
The normal retrieval result is `Available(complete_learning_unit) | Unavailable`.
`Available` requires current content that exists and is currently available.
`Unavailable` covers missing current state and unavailable current content.
Retrieval reads committed current published state and rechecks current availability.
The complete learning unit follows `spec:product.learning.learning_unit`.
The persistence adapter maps persisted complete content into the learning-unit contract.
The persistence adapter keeps provenance inside the published-content and pipeline boundary.
Mapping failure and infrastructure failure are technical failures.
Mapping failure and infrastructure failure must not become `Available` or `Unavailable`.
The pipeline owns availability decisions and published-content writes.

contradiction or gap:
none.

T005-04 action:
Reflect the accepted ADR-003 and ADR-004 retrieval contract without changing result names or persistence-adapter responsibility.
Keep provenance excluded from the normal learner retrieval result.

#### 6. Application test double boundary

topic:
Application tests and outbound-port test doubles.

authority:
PRODUCT-ADR-APPLICATION-004, `spec:product.application`, `spec:product.application.learning_unit_selection`.

existing contract:
Application tests may use a test double at the application-owned outbound contract boundary.
The selection-side test double represents returned ordered `LearningUnitRef[]` values and technical failures from the outbound selection operation.
The retrieval-side test double represents `Available(complete_learning_unit) | Unavailable` and technical failures from the outbound retrieval port.
Application tests verify application orchestration and observable application validation.
Application tests do not verify the real database, queries, randomization algorithm, persistence mapping, or persistence technology.

contradiction or gap:
missing spec reflection.
The retrieval test-double permission exists in ADR-004.
The selection test-double boundary and shared application-test boundary need focused specification reflection.

T005-04 action:
Add an application-test boundary to the outbound-query specification.
Separate application-test obligations from persistence-adapter contract-test obligations.

#### 7. Persistence-adapter contract test scope

topic:
Persistence-adapter contract-test scope.

authority:
PRODUCT-ADR-APPLICATION-004, `spec:product.application.learning_unit_selection`, `spec:product.application.published_content`, `spec:product.learning.learning_unit`, `spec:product.pipeline`.

existing contract:
Contract tests target the real persistence adapter boundary rather than an application test double.
Selection contract tests cover zero candidates, below-limit candidates, exact-limit candidates, above-limit candidates, unavailable candidates, scope filtering, exact cardinality, uniqueness, stable-reference mapping, randomized order, mapping failure, and infrastructure failure.
Retrieval contract tests cover available current content, missing current content, unavailable current content, complete learning-unit mapping, provenance exclusion, mapping failure, and infrastructure failure.
The tests verify adapter-owned guarantees that the application cannot observe from one returned array or one mocked result.
Concrete database product, container, fixture strategy, SQL, ORM, and query library choices remain deferred.

contradiction or gap:
missing spec reflection.
The required selection coverage is already present in the selection spec.
ADR-004 requires retrieval coverage.
T005-04 must place the combined contract-test boundary in the focused outbound-query topic.

T005-04 action:
Reflect required adapter contract-test coverage for selection and retrieval.
State that these tests exercise the persistence adapter boundary, not application test doubles.
Keep concrete persistence-test infrastructure deferred.

### Contradiction and gap handling

| class | result |
|---|---|
| missing spec reflection | Application test-double boundary and combined outbound-query contract-test boundary require focused reflection in T005-04. |
| duplicated content | Selection, retrieval, outbound-query, and verification content are concentrated in `spec:product.application.learning_unit_selection`. T005-04 should assign one focused owner for each topic. |
| misplaced content | Retrieval-port and outbound-query verification details should move to focused retrieval and outbound-query topics during T005-04. |
| authority conflict | none |
| genuine decision required | none |
| implementation detail | Database product, schema, query, ORM, container, fixture, transaction, randomization algorithm, transport, source layout, concrete interface, and exception choices remain deferred. |

### T005-04 inputs

- Reflect selection input and normal result in an outbound selection-query topic.
- Reflect selection technical failures separately from empty normal results.
- Reflect observable application validation separately from adapter-owned guarantees.
- Reflect persistence-adapter guarantees for availability, scope, cardinality, uniqueness, stable-reference mapping, randomized order, returned order, and no learner-specific state.
- Reflect retrieval input, result, availability recheck, committed-state read, mapping, failure, and provenance boundaries from ADR-003 and ADR-004.
- Reflect application-test test doubles at the outbound contract boundary.
- Reflect persistence-adapter contract tests against the real adapter boundary.
- Keep implementation details deferred.

### Verification

- Every mapped obligation traces to PRODUCT-ADR-APPLICATION-003, PRODUCT-ADR-APPLICATION-004, or a current specification.
- The evidence uses PRODUCT-TASK-APPLICATION-005-01 and PRODUCT-TASK-APPLICATION-005-02 as execution context only.
- Selection tests separate observable application validation from adapter-owned guarantees.
- Retrieval tests preserve `Available | Unavailable` semantics.
- Contract tests target the persistence adapter boundary rather than an application mock.
- Database, query, transport, source-layout, interface-name, and concrete exception choices are absent.
- Blockers: none.
