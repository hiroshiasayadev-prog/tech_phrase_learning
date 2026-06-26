# PRODUCT-TASK-APPLICATION-001-04: Open outbound query-port design

- **id**: PRODUCT-TASK-APPLICATION-001-04
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-001
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-001-02
  - PRODUCT-TASK-APPLICATION-001-03
- **outputs**:
  - PRODUCT-WORK-APPLICATION-005

## Goal

Create a focused work item for application outbound query ports and persistence-adapter obligations.

The created work item must be executable without a separate conversation handoff.

## Work

1. Read PRODUCT-ADR-APPLICATION-003 and all current `spec:product.application` topics.
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
- reads against one committed current published state;
- handling of available, unavailable, missing, mapping-failure, and infrastructure-failure outcomes;
- prohibition on generic CRUD as the primary application contract;
- test doubles and contract-test boundaries;
- accepted ADRs required before any normative specification update;
- specification reflection only after the authorizing ADR is accepted.

Required exclusions:

- concrete SQL;
- table and index design;
- ORM or query-library selection;
- connection-pool configuration;
- database deployment;
- concrete source directory layout.

The child work item must keep port definitions inside the application boundary.
The child work item must keep adapter algorithms outside the domain layer.
The child task flow must separate decision ADRs from later specification reflection.
The child task flow must stop as blocked when a normative change lacks an accepted ADR.

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
- Confirm that the child flow applies the ADR-first change gate from `prompt_chappy.md`.
- Confirm that a new session can start the child work item using repository records only.

## Evidence

### Result

- **Verdict**: PASS with an explicit host-command limitation.
- PRODUCT-WORK-APPLICATION-005 was created as the next APPLICATION work-item ID.
- PRODUCT-TASK-APPLICATION-005-01 through PRODUCT-TASK-APPLICATION-005-05 were created.
- No current specification or ADR was modified.
- PRODUCT-TASK-APPLICATION-001-05 was not started.
- PRODUCT-WORK-APPLICATION-001 remains open.

### Reciprocal workflow links

- PRODUCT-WORK-APPLICATION-005 uses PRODUCT-REQ-APPLICATION-001 as `source_requirement`.
- PRODUCT-REQ-APPLICATION-001 lists PRODUCT-WORK-APPLICATION-005 in `work_items`.
- PRODUCT-WORK-APPLICATION-005 lists all five child tasks.
- Every child task references PRODUCT-WORK-APPLICATION-005 and PRODUCT-REQ-APPLICATION-001.
- Child dependencies form one valid T005-01 through T005-05 sequence.
- This task records PRODUCT-WORK-APPLICATION-005 as its only output.

### Preserved contracts

- PRODUCT-ADR-APPLICATION-003 and PRODUCT-ADR-APPLICATION-004 remain current authority.
- Superseded PRODUCT-ADR-APPLICATION-001 and PRODUCT-ADR-APPLICATION-002 are not current impact authorities.
- Completed selection and retrieval semantics are fixed inputs.
- The child flow classifies gaps before deciding whether another ADR is required.
- Selection and retrieval remain distinct operations.
- Concrete persistence, transport, framework, algorithm, and source-layout choices remain excluded.

### Child work-item readiness

- T005-01 can start from repository records without another handoff.
- T005-01 inventories and classifies current contracts without changing specifications.
- T005-02 creates an ADR only for a genuine unresolved normative decision.
- T005-03 defines adapter and verification obligations under accepted authority.
- T005-04 reflects accepted contracts and applies the agreed focused specification organization.
- T005-05 requires an independent `PASS` review before work-item closure.

### File and relation verification

- Filesystem directory listings confirmed WORK-005 is the only APPLICATION work item after WORK-004.
- Filesystem rereads confirmed every new H1, metadata ID, filename prefix, source requirement, and dependency.
- Impact refs use current design-record IDs and active `spec:` refs.
- Empty task relations use empty list fields rather than literal `[]` values.
- The Design Records MCP validator was not used as evidence because its configured root is the Brewprint repository.

### Tooling limitation

- The active filesystem tool has no host command-execution capability.
- Repository CLI validation, `git diff --check`, and `git status --short` were not executed in this session.
- No success claim is made for those host commands.

