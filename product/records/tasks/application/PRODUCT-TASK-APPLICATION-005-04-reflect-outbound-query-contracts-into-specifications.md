# PRODUCT-TASK-APPLICATION-005-04: Reflect outbound query contracts into specifications

- **id**: PRODUCT-TASK-APPLICATION-005-04
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-005
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-005-03
- **outputs**:
  - `spec:product.application`
  - `spec:product.application.published_content`
  - `spec:product.application.published_content.current_state`
  - `spec:product.application.published_content.availability`
  - `spec:product.application.published_content.publication_handoff`
  - `spec:product.application.learning_unit_selection`
  - `spec:product.application.learning_unit_selection.create_complete_shuffle_queue`
  - `spec:product.application.learning_unit_selection.selection_scope`
  - `spec:product.application.learning_unit_selection.queue_contract`
  - `spec:product.application.learning_unit_selection.result_validation`
  - `spec:product.application.learning_unit_retrieval`
  - `spec:product.application.outbound_queries`
  - `spec:product.application.outbound_queries.select_learning_unit_refs`
  - `spec:product.application.outbound_queries.get_published_learning_unit`

## Goal

Reflect accepted outbound query contracts into focused application specifications.

Decompose oversized specifications without duplicating selection, retrieval, or published-content authority.

## Work

1. Read the T005-01 ownership inventory, T005-02 authority disposition, and T005-03 contract map.
2. Stop as `blocked` when any proposed normative change lacks an accepted ADR.
3. Preserve PRODUCT-ADR-APPLICATION-003 and PRODUCT-ADR-APPLICATION-004 decisions.
4. Reflect any additional accepted T005-02 ADR decisions.
5. Keep selection policy separate from the outbound selection query contract.
6. Keep application retrieval behavior separate from the outbound retrieval query contract.
7. Put shared outbound-query rules in the nearest common topic overview.
8. Avoid copying shared dependency, failure, and verification rules into every child specification.
9. Use the verified topic decomposition from T005-01.
10. Keep `application/index.md` limited to direct child topics and the application-wide overview.
11. Preserve `spec:product.application.published_content` when moving `published-content.md` to `published-content/index.md`.
12. Preserve `spec:product.application.learning_unit_selection` when moving `learning-unit-selection.md` to `learning-unit-selection/index.md`.
13. Create focused child specs only for independently understandable responsibilities.
14. Keep each leaf spec small enough to read with its task and parent overview.
15. Record every changed ref and explicit no-change judgment.
16. Update `migrated_to_spec` only after an accepted ADR is fully reflected.
17. Run strict specification validation.
18. Run `git diff --check` and inspect `git status --short`.

Expected structure, subject to the verified T005-01 judgment:

```text
application/
  index.md
  learning-unit-retrieval.md
  published-content/
    index.md
    current-state.md
    availability.md
    publication-handoff.md
  learning-unit-selection/
    index.md
    create-complete-shuffle-queue.md
    selection-scope.md
    queue-contract.md
    result-validation.md
  outbound-queries/
    index.md
    select-learning-unit-refs.md
    get-published-learning-unit.md
```

Do not create thin child specifications when the responsibility cannot stand independently.
Do not adopt a new design decision in this task.

## Done condition

- Every normative statement traces to accepted ADR authority.
- Application, selection, retrieval, published-content, and pipeline ownership remain distinct.
- Selection and retrieval query contracts are separate child specifications.
- Shared outbound-query rules are owned once by their topic overview.
- Application use-case behavior remains outside persistence-adapter query specifications.
- Existing semantic refs remain stable for converted topic indexes.
- Parent overviews route direct child topics only.
- Leaf specifications remain focused and independently scoped.
- No concrete persistence, transport, framework, or algorithm decision enters the specifications.
- Strict validation and whitespace verification pass.

## Verification

- Trace each changed normative statement to an accepted ADR.
- Confirm no task or work-item evidence acts as specification authority.
- Confirm `spec:product.application.published_content` and `spec:product.application.learning_unit_selection` remain path-correct.
- Confirm Topics tables use active path-derived semantic refs.
- Confirm shared rules are not duplicated across child specs.
- Confirm moved content retains its original semantic meaning.
- Confirm no superseded ADR is presented as current authority.
- Record validation commands and results in `## Evidence`.

## Evidence

### Result

- **Verdict**: PASS.
- Existing selection, retrieval, and published-content contracts were decomposed into focused application specifications.
- No new ADR was created.
- PRODUCT-ADR-APPLICATION-003 and PRODUCT-ADR-APPLICATION-004 remained unchanged.
- No genuine unresolved architectural decision was found during reflection.
- Blockers: none.

### Final structure

```text
product/records/spec/application/
  index.md
  learning-unit-retrieval.md
  published-content/
    index.md
    current-state.md
    availability.md
    publication-handoff.md
  learning-unit-selection/
    index.md
    create-complete-shuffle-queue.md
    selection-scope.md
    queue-contract.md
    result-validation.md
  outbound-queries/
    index.md
    select-learning-unit-refs.md
    get-published-learning-unit.md
```

### Files moved

| from | to | semantic ref |
|---|---|---|
| `product/records/spec/application/published-content.md` | `product/records/spec/application/published-content/index.md` | `spec:product.application.published_content` |
| `product/records/spec/application/learning-unit-selection.md` | `product/records/spec/application/learning-unit-selection/index.md` | `spec:product.application.learning_unit_selection` |

### Files created

| file | ref | owner |
|---|---|---|
| `product/records/spec/application/learning-unit-retrieval.md` | `spec:product.application.learning_unit_retrieval` | Application retrieval use-case orchestration. |
| `product/records/spec/application/published-content/current-state.md` | `spec:product.application.published_content.current_state` | Committed current published-state concept. |
| `product/records/spec/application/published-content/availability.md` | `spec:product.application.published_content.availability` | Runtime availability values. |
| `product/records/spec/application/published-content/publication-handoff.md` | `spec:product.application.published_content.publication_handoff` | Application-side publication handoff meaning. |
| `product/records/spec/application/learning-unit-selection/create-complete-shuffle-queue.md` | `spec:product.application.learning_unit_selection.create_complete_shuffle_queue` | First-MVP queue creation use case. |
| `product/records/spec/application/learning-unit-selection/selection-scope.md` | `spec:product.application.learning_unit_selection.selection_scope` | Selection-scope vocabulary and future constraint boundary. |
| `product/records/spec/application/learning-unit-selection/queue-contract.md` | `spec:product.application.learning_unit_selection.queue_contract` | Queue cardinality, uniqueness, order, and no backend state. |
| `product/records/spec/application/learning-unit-selection/result-validation.md` | `spec:product.application.learning_unit_selection.result_validation` | Application-observable selection result validation. |
| `product/records/spec/application/outbound-queries/index.md` | `spec:product.application.outbound_queries` | Shared outbound-query dependency and verification rules. |
| `product/records/spec/application/outbound-queries/select-learning-unit-refs.md` | `spec:product.application.outbound_queries.select_learning_unit_refs` | Selection query adapter guarantees. |
| `product/records/spec/application/outbound-queries/get-published-learning-unit.md` | `spec:product.application.outbound_queries.get_published_learning_unit` | Retrieval query adapter guarantees. |

### Files updated

| file | update |
|---|---|
| `product/records/spec/application/index.md` | Reduced to application overview and direct child topic router. |
| `product/records/spec/learning/index.md` | Updated runtime selection and retrieval routing to the application area. |
| `product/records/spec/learning/quiz-session.md` | Split selection and retrieval related refs. |
| `product/records/spec/ui/learning-flow.md` | Split availability, queue generation, and complete-unit retrieval refs. |
| `product/records/spec/ui/pages/main-page.md` | Split queue creation and complete-unit retrieval refs. |
| `product/records/tasks/application/PRODUCT-TASK-APPLICATION-005-04-reflect-outbound-query-contracts-into-specifications.md` | Recorded outputs, evidence, and completion status. |

### Semantic refs preserved

| ref | preservation result |
|---|---|
| `spec:product.application.published_content` | Preserved by moving from `application/published-content.md` to `application/published-content/index.md`. |
| `spec:product.application.learning_unit_selection` | Preserved by moving from `application/learning-unit-selection.md` to `application/learning-unit-selection/index.md`. |

The strict validator confirmed path-derived IDs for the final 31 specification files.

### Contract ownership map

| concern | owning spec |
|---|---|
| Application overview, use-case routing, and dependency direction | `spec:product.application` |
| Published runtime state | `spec:product.application.published_content.current_state` |
| Current availability | `spec:product.application.published_content.availability` |
| Publication handoff meaning visible to application reads | `spec:product.application.published_content.publication_handoff` |
| First-MVP queue creation policy | `spec:product.application.learning_unit_selection.create_complete_shuffle_queue` |
| Selection scope | `spec:product.application.learning_unit_selection.selection_scope` |
| Queue result invariants | `spec:product.application.learning_unit_selection.queue_contract` |
| Application-observable selection validation | `spec:product.application.learning_unit_selection.result_validation` |
| Published learning-unit retrieval use case | `spec:product.application.learning_unit_retrieval` |
| Shared outbound-query dependency and verification rules | `spec:product.application.outbound_queries` |
| Selection query adapter guarantees | `spec:product.application.outbound_queries.select_learning_unit_refs` |
| Retrieval query adapter guarantees | `spec:product.application.outbound_queries.get_published_learning_unit` |

### T005-03 trace table

| T005-03 topic | reflected spec |
|---|---|
| Selection input and normal result | `spec:product.application.learning_unit_selection.create_complete_shuffle_queue`; `spec:product.application.outbound_queries.select_learning_unit_refs` |
| Selection normal result and technical failure boundary | `spec:product.application.outbound_queries`; `spec:product.application.outbound_queries.select_learning_unit_refs` |
| Selection application validation | `spec:product.application.learning_unit_selection.result_validation` |
| Selection persistence-adapter guarantees | `spec:product.application.outbound_queries.select_learning_unit_refs` |
| Retrieval input, normal result, and failure boundary | `spec:product.application.learning_unit_retrieval`; `spec:product.application.outbound_queries.get_published_learning_unit` |
| Application test double boundary | `spec:product.application.outbound_queries` |
| Persistence-adapter contract test scope | `spec:product.application.outbound_queries`; `spec:product.application.outbound_queries.select_learning_unit_refs`; `spec:product.application.outbound_queries.get_published_learning_unit` |

### Duplicate content removed

- The previous `spec:product.application.learning_unit_selection` leaf no longer owns retrieval-port details.
- The previous `spec:product.application.learning_unit_selection` leaf no longer owns shared outbound-query verification rules.
- Shared outbound-query dependency, failure, and test-boundary rules are owned once by `spec:product.application.outbound_queries`.
- Application retrieval behavior is owned by `spec:product.application.learning_unit_retrieval`.
- Persistence-adapter retrieval guarantees are owned by `spec:product.application.outbound_queries.get_published_learning_unit`.

### Explicit no-change judgments

| item | judgment |
|---|---|
| PRODUCT-ADR-APPLICATION-003 | No change. Current published-content and retrieval result decisions were already accepted. |
| PRODUCT-ADR-APPLICATION-004 | No change. Result-shaped retrieval-port and adapter obligations were already accepted. |
| Selection semantics | No semantic change. Existing `All`, `maximum_count = 100`, cardinality, uniqueness, random order, and no backend queue state were preserved. |
| Retrieval semantics | No semantic change. Existing `Available(complete_learning_unit) | Unavailable` result shape was preserved. |
| Pipeline ownership | No change. Publication decisions and published-content writes remain pipeline-owned. |

### Deferred implementation details

- SQL, tables, columns, indexes, schemas, and query plans.
- ORM, query library, database product, and connection pool.
- Exact randomization algorithm and statistical distribution threshold.
- Transaction configuration and isolation level.
- Programming-language interface, class, method, and source directory.
- HTTP route, status code, JSON schema, retry timing, and concrete exception type.
- Concrete test database, container, fixture, and framework.

### Validation

Strict specification validation passed:

```text
python -X utf8 C:\Users\imved\projects\brewprint\product\src\tools\validate_spec.py product/records/spec --strict --no-color
[strict]  All 31 file(s) OK.
```

Whitespace verification passed with Git line-ending warnings only:

```text
git diff --check
```

Git reported no whitespace errors.

### Git status

```text
 M product/records/spec/application/index.md
 D product/records/spec/application/learning-unit-selection.md
 D product/records/spec/application/published-content.md
 M product/records/spec/learning/index.md
 M product/records/spec/learning/quiz-session.md
 M product/records/spec/ui/learning-flow.md
 M product/records/spec/ui/pages/main-page.md
 M product/records/tasks/application/PRODUCT-TASK-APPLICATION-005-01-establish-outbound-query-port-baseline-and-gap-inventory.md
 M product/records/tasks/application/PRODUCT-TASK-APPLICATION-005-02-resolve-remaining-outbound-query-port-decisions.md
 M product/records/tasks/application/PRODUCT-TASK-APPLICATION-005-03-define-adapter-and-verification-obligations.md
 M product/records/tasks/application/PRODUCT-TASK-APPLICATION-005-04-reflect-outbound-query-contracts-into-specifications.md
 M product/records/work-items/application/PRODUCT-WORK-APPLICATION-005-define-application-outbound-query-ports.md
?? product/records/spec/application/learning-unit-retrieval.md
?? product/records/spec/application/learning-unit-selection/
?? product/records/spec/application/outbound-queries/
?? product/records/spec/application/published-content/
```

The T005-01, T005-02, T005-03, and parent work-item changes were present before this task execution.
