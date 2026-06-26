# PRODUCT-TASK-APPLICATION-001-03: Open learning-unit retrieval design

- **id**: PRODUCT-TASK-APPLICATION-001-03
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-001
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**: [PRODUCT-TASK-APPLICATION-001-01]
- **outputs**:
  - PRODUCT-WORK-APPLICATION-004

## Goal

Create a focused work item for the published learning-unit retrieval module.

The created work item must be executable without a separate conversation handoff.

## Work

1. Read PRODUCT-ADR-APPLICATION-001 and `spec:product.application.learning_unit_selection`.
2. Read `spec:product.application.published_content` and `spec:product.learning.learning_unit`.
3. Read the loaded-unit and stale-reference behavior in `spec:product.ui.learning_flow`.
4. Create the next APPLICATION work item under PRODUCT-REQ-APPLICATION-001.
5. Use a title equivalent to `Define published learning-unit retrieval contracts`.
6. Add the new work item to PRODUCT-REQ-APPLICATION-001 `work_items`.
7. Record the created work-item ID in this task's `outputs` and evidence.
8. Give the child work item a task graph that resolves the module contracts below.

Required child scope:

- `GetPublishedLearningUnit` input and transport-independent result model;
- current availability check at retrieval time;
- complete learning-unit content required by the learning contract;
- mapping from the published projection into the application result;
- treatment of missing and unavailable references at the application boundary;
- separation of unavailable results from infrastructure failures;
- source attribution returned with normal learner content;
- opaque provenance handling inside the application;
- loaded-unit immutability after successful retrieval;
- behavior when publication replacement occurs between queue creation and retrieval;
- required ADR or spec updates.

Required exclusions:

- concrete HTTP status codes and routes;
- JSON wire shape;
- retry timing;
- database schema and SQL;
- learner session state;
- pipeline provenance internals.

The child work item must not create backend queue state.
The child work item must not force withdrawal onto a unit already loaded by the PWA.

## Done condition

- One focused APPLICATION work item exists for published learning-unit retrieval design.
- The child work item references PRODUCT-REQ-APPLICATION-001.
- PRODUCT-REQ-APPLICATION-001 lists the child work item.
- The child work item contains the required scope, exclusions, task flow, and completion conditions.
- The child work item separates domain results from transport and infrastructure failures.
- This task records the child work-item ID in `outputs` and `## Evidence`.

## Verification

- Check the child work item's path, H1, metadata, source requirement, and impact refs.
- Check reciprocal linkage from PRODUCT-REQ-APPLICATION-001.
- Confirm alignment with the UI rule that unavailable references are bypassed without network retry.
- Confirm that a new session can start the child work item using repository records only.

## Evidence

- Created PRODUCT-WORK-APPLICATION-004 under `product/records/work-items/application/`.
- Created PRODUCT-TASK-APPLICATION-004-01 through PRODUCT-TASK-APPLICATION-004-05 as its task graph.
- Added PRODUCT-WORK-APPLICATION-004 to PRODUCT-REQ-APPLICATION-001 `work_items`.
- Confirmed that unavailable results remain separate from infrastructure failures.
- Confirmed that successful content includes source attribution while provenance remains opaque.
- Confirmed that retrieval-time availability remains separate from queue creation.
- Confirmed that loaded-unit immutability and unavailable-reference bypass remain UI-owned.
- Confirmed every child task references PRODUCT-WORK-APPLICATION-004 and PRODUCT-REQ-APPLICATION-001.
- A new session can begin with PRODUCT-TASK-APPLICATION-004-01 without a separate handoff.
