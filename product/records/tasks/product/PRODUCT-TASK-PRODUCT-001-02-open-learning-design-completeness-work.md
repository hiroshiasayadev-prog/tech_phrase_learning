# PRODUCT-TASK-PRODUCT-001-02: Open learning design-completeness work

- **id**: PRODUCT-TASK-PRODUCT-001-02
- **status**: not_started
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PRODUCT-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-PRODUCT-001-01
- **outputs**: []

## Goal

Create one focused work item that verifies learning contracts are complete enough to constrain pipeline and UI implementation planning.

## Work

1. Read the T01 baseline and learning-owned gaps.
2. Read all current learning ADRs, investigations, and specifications.
3. Create the first LEARNING work item under PRODUCT-REQ-PRODUCT-001.
4. Use a title equivalent to `Review first-MVP learning contract completeness`.
5. Add the new work item to PRODUCT-REQ-PRODUCT-001 `work_items`.
6. Record the created work-item ID in this task's `outputs` and Evidence.
7. Give the child work item a task graph that covers:
   - target learner and learning outcome consistency;
   - valid learning-path meaning and suitability criteria;
   - learning-unit required fields and invariants;
   - question and reply interaction composition;
   - target phrase, prompt, option, summary, grounding, and attribution semantics;
   - quiz-session progression and terminal behavior;
   - publication-readiness criteria owned by learning;
   - downstream constraints required by pipeline and UI;
   - ADR-first resolution of missing normative decisions;
   - specification reflection and independent review.
8. Keep processing mechanics, provider choices, runtime selection, and PWA state outside the child work item.

## Done condition

- One focused LEARNING work item exists under PRODUCT-REQ-PRODUCT-001.
- The child work item has a self-contained boundary, task graph, completion conditions, and impact refs.
- PRODUCT-REQ-PRODUCT-001 lists the child work item.
- The child work item distinguishes learning semantics from pipeline mechanics and UI runtime state.
- This task records the child work-item ID in `outputs` and Evidence.

## Verification

- Check the child work item's H1, metadata, source requirement, and reciprocal link.
- Confirm the child work item does not make pipeline or UI implementation choices.
- Confirm unresolved learning judgments require an accepted ADR before specification changes.
- Confirm a new session can start the child work item from repository records only.
- Run relevant record validation, `git diff --check`, and `git status --short`.

## Evidence

TBD
