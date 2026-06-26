# PRODUCT-TASK-APPLICATION-001-02: Open complete-shuffle selection design

- **id**: PRODUCT-TASK-APPLICATION-001-02
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-001
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-001-01
- **outputs**:
  - PRODUCT-WORK-APPLICATION-003

## Goal

Create a focused work item for the complete-shuffle selection domain module.

The created work item must be executable without a separate conversation handoff.

## Work

1. Read PRODUCT-ADR-APPLICATION-001 and `spec:product.application.learning_unit_selection`.
2. Read the availability rules in `spec:product.application.published_content`.
3. Create the next APPLICATION work item under PRODUCT-REQ-APPLICATION-001.
4. Use a title equivalent to `Define complete-shuffle selection domain contracts`.
5. Add the new work item to PRODUCT-REQ-APPLICATION-001 `work_items`.
6. Record the created work-item ID in this task's `outputs` and evidence.
7. Give the child work item a task graph that resolves the module contracts below.

Required child scope:

- `SelectionScope` meaning and the first-MVP `all` scope;
- queue maximum of 100 references as application policy;
- uniqueness within one queue;
- allowed repetition across later queues;
- behavior when fewer than 100 units are available;
- absence of learner-specific reservation and backend queue history;
- bounded random selection as a semantic operation;
- adapter obligations for availability, scope, maximum count, uniqueness, and ordering;
- domain invariants and invalid-result handling;
- extension boundary for source, topic, discussion, difficulty, and learner-history scopes;
- required ADR or spec updates.

Required exclusions:

- exact randomization algorithm;
- SQL and database indexes;
- learner-history implementation;
- queue persistence;
- PWA queue position;
- concrete HTTP request and response schemas.

The child work item must preserve database-side bounded selection.
The child work item must keep selection rules independent from the database adapter.

## Done condition

- One focused APPLICATION work item exists for complete-shuffle selection design.
- The child work item references PRODUCT-REQ-APPLICATION-001.
- PRODUCT-REQ-APPLICATION-001 lists the child work item.
- The child work item contains the required scope, exclusions, task flow, and completion conditions.
- The child work item distinguishes domain invariants from adapter execution.
- This task records the child work-item ID in `outputs` and `## Evidence`.

## Verification

- Check the child work item's path, H1, metadata, source requirement, and impact refs.
- Check reciprocal linkage from PRODUCT-REQ-APPLICATION-001.
- Confirm that the scope does not require all available references to enter one queue.
- Confirm that a new session can start the child work item using repository records only.

## Evidence

- Created PRODUCT-WORK-APPLICATION-003 under `product/records/work-items/application/`.
- Created PRODUCT-TASK-APPLICATION-003-01 through PRODUCT-TASK-APPLICATION-003-05 as the child work-item task graph.
- Added PRODUCT-WORK-APPLICATION-003 to PRODUCT-REQ-APPLICATION-001 `work_items`.
- Verified that the child work item preserves database-side bounded selection.
- Verified that selection invariants remain independent from database adapter implementation.
- Verified that the `all` scope defines the eligible candidate set without requiring every available reference in one queue.
- Verified every child task references PRODUCT-WORK-APPLICATION-003 and PRODUCT-REQ-APPLICATION-001.
- A new session can begin with PRODUCT-TASK-APPLICATION-003-01 without a separate handoff.
