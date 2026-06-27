# PRODUCT-TASK-PRODUCT-001-04: Open UI detailed-design work

- **id**: PRODUCT-TASK-PRODUCT-001-04
- **status**: not_started
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PRODUCT-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-PRODUCT-001-02
- **outputs**: []

## Goal

Create one focused work item that verifies the whole first-MVP learner UI is implementation-planning ready.

## Work

1. Read the T01 baseline and the focused learning work item created by T02.
2. Read all current UI ADRs, UI specifications, application PWA-interface specifications, and learning quiz-session specifications.
3. Read PRODUCT-WORK-UI-001 as completed failure-transition input.
4. Create the next UI work item under PRODUCT-REQ-PRODUCT-001.
5. Use a title equivalent to `Define first-MVP learner UI contracts`.
6. Add the new work item to PRODUCT-REQ-PRODUCT-001 `work_items`.
7. Record the created work-item ID in this task's `outputs` and Evidence.
8. Give the child work item a task graph that covers:
   - main-page states and start behavior;
   - learning-page composition and progressive card behavior;
   - empty initial queue and empty replacement queue behavior;
   - queue, loaded-unit, and session state invariants;
   - answer, continue, skip, next-discussion, and back-to-main transitions;
   - loading and initiating-action disablement;
   - category-specific failure surfaces and retry behavior;
   - unavailable-reference bypass;
   - retrieval mapping-failure termination;
   - reload, tab closure, and navigation disposal behavior;
   - learner-visible attribution placement;
   - accessibility-relevant interaction obligations that affect behavior;
   - ADR-first resolution, specification reflection, and independent review.
9. Keep framework, routing library, state library, styling, animation, and component file layout outside the child work item.

## Done condition

- One focused UI work item exists under PRODUCT-REQ-PRODUCT-001.
- The child work item has a self-contained whole-area boundary and task graph.
- PRODUCT-REQ-PRODUCT-001 lists the child work item.
- Existing failure-transition work is reused rather than duplicated.
- The child scope preserves learning meaning and application failure semantics.
- Concrete frontend implementation choices remain excluded.
- This task records the child work-item ID in `outputs` and Evidence.

## Verification

- Check the child work item's H1, metadata, source requirement, reciprocal link, and impact refs.
- Confirm the child scope covers all normal, empty, unavailable, and failure terminal states.
- Confirm UI ownership remains limited to transient state, transitions, and presentation behavior.
- Confirm a new session can start the child work item from repository records only.
- Run relevant record validation, `git diff --check`, and `git status --short`.

## Evidence

TBD
