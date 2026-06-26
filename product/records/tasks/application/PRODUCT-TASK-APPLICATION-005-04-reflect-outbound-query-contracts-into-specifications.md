# PRODUCT-TASK-APPLICATION-005-04: Reflect outbound query contracts into specifications

- **id**: PRODUCT-TASK-APPLICATION-005-04
- **status**: not_started
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-005
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-005-03
- **outputs**:

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

TBD
