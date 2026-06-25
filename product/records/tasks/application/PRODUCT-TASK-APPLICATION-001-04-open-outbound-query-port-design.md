# PRODUCT-TASK-APPLICATION-001-04: Open outbound query-port design

- **id**: PRODUCT-TASK-APPLICATION-001-04
- **status**: not_started
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-001
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**: [PRODUCT-TASK-APPLICATION-001-02, PRODUCT-TASK-APPLICATION-001-03]
- **outputs**: []

## Goal

Create a focused work item for application outbound query ports and persistence-adapter obligations.

The created work item must be executable without a separate conversation handoff.

## Work

1. Read PRODUCT-ADR-APPLICATION-001 and all current `spec:product.application` topics.
2. Read the focused selection and retrieval work items created by T02 and T03.
3. Create the next APPLICATION work item under PRODUCT-REQ-APPLICATION-001.
4. Use a title equivalent to `Define application outbound query ports`.
5. Add the new work item to PRODUCT-REQ-APPLICATION-001 `work_items`.
6. Record the created work-item ID in this task's `outputs` and evidence.
7. Give the child work item a task graph that resolves the module contracts below.

Required child scope:

- semantic query operations required by queue creation and unit retrieval;
- input and result ownership for each outbound port;
- application-defined interfaces and adapter dependency direction;
- availability filtering obligations;
- bounded random selection obligations;
- complete current-publication loading obligations;
- consistency assumptions required by atomic publication replacement;
- handling of unavailable, missing, malformed, and infrastructure-failure outcomes;
- prohibition on generic CRUD as the primary application contract;
- test doubles and contract-test boundaries;
- required ADR or spec updates.

Required exclusions:

- concrete SQL;
- table and index design;
- ORM or query-library selection;
- connection-pool configuration;
- database deployment;
- concrete source directory layout.

The child work item must keep port definitions inside the application boundary.
The child work item must keep adapter algorithms outside the domain layer.

## Done condition

- One focused APPLICATION work item exists for outbound query-port design.
- The child work item references PRODUCT-REQ-APPLICATION-001.
- PRODUCT-REQ-APPLICATION-001 lists the child work item.
- The child work item contains the required scope, exclusions, task flow, and completion conditions.
- The child work item names semantic operations instead of table-oriented CRUD.
- This task records the child work-item ID in `outputs` and `## Evidence`.

## Verification

- Check the child work item's path, H1, metadata, source requirement, and impact refs.
- Check reciprocal linkage from PRODUCT-REQ-APPLICATION-001.
- Confirm that the port direction remains `adapter -> application -> domain`.
- Confirm that a new session can start the child work item using repository records only.

## Evidence

TBD
