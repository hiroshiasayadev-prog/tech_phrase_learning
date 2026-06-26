# PRODUCT-TASK-APPLICATION-001-05: Open PWA-facing application-interface design

- **id**: PRODUCT-TASK-APPLICATION-001-05
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-001
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**: [PRODUCT-TASK-APPLICATION-001-02, PRODUCT-TASK-APPLICATION-001-03]
- **outputs**:
  - PRODUCT-WORK-APPLICATION-006

## Goal

Create a focused work item for the transport-independent interface consumed by the PWA.

The created work item must be executable without a separate conversation handoff.

## Work

1. Read PRODUCT-ADR-APPLICATION-003 and `spec:product.application.learning_unit_selection`.
2. Read `spec:product.ui.learning_flow` and the main and learning page specifications.
3. Read the focused selection and retrieval work items created by T02 and T03.
4. Create the next APPLICATION work item under PRODUCT-REQ-APPLICATION-001.
5. Use a title equivalent to `Define the PWA-facing application interface`.
6. Add the new work item to PRODUCT-REQ-APPLICATION-001 `work_items`.
7. Record the created work-item ID in this task's `outputs` and evidence.
8. Give the child work item a task graph that resolves the module contracts below.

Required child scope:

- transport-independent request and result contracts for queue creation;
- transport-independent request and result contracts for complete-unit retrieval;
- stable learning-unit reference representation at the interface boundary;
- result classification for available, unavailable, invalid request, and infrastructure failure;
- distinction between unavailable-reference skipping and retryable failure;
- empty-queue and exhausted-queue behavior;
- preservation of the PWA's queue and session ownership;
- replacement only after successful unit loading;
- attribution content required by the learner flow;
- future mapping to HTTP without making HTTP semantics normative here;
- accepted ADRs required before any normative specification update;
- specification reflection only after the authorizing ADR is accepted.

Required exclusions:

- concrete routes;
- concrete HTTP status codes;
- JSON field names and serialization format;
- retry delays and transport-client configuration;
- component implementation;
- authentication and learner accounts.

The child work item must not introduce backend session identity.
The child work item must keep network failures distinct from unavailable content.
The child task flow must separate decision ADRs from later specification reflection.
The child task flow must stop as blocked when a normative change lacks an accepted ADR.

## Done condition

- One focused APPLICATION work item exists for the PWA-facing application interface.
- The child work item references PRODUCT-REQ-APPLICATION-001.
- PRODUCT-REQ-APPLICATION-001 lists the child work item.
- The child work item contains the required scope, exclusions, task flow, and completion conditions.
- The child work item preserves current UI state ownership and replacement rules.
- This task records the child work-item ID in `outputs` and `## Evidence`.

## Verification

- Check the child work item's path, H1, metadata, source requirement, and impact refs.
- Check reciprocal linkage from PRODUCT-REQ-APPLICATION-001.
- Compare result semantics against PRODUCT-ADR-APPLICATION-003 and `spec:product.ui.learning_flow`.
- Confirm that the child flow applies the ADR-first change gate from `prompt_chappy.md`.
- Confirm that a new session can start the child work item using repository records only.

## Evidence

### Result

- **Verdict**: PASS with an explicit host-command limitation.
- PRODUCT-WORK-APPLICATION-006 was created as the next APPLICATION work-item ID.
- PRODUCT-TASK-APPLICATION-006-01 through PRODUCT-TASK-APPLICATION-006-05 were created.
- No current specification or ADR was modified.
- PRODUCT-TASK-APPLICATION-001-06 was not started.
- PRODUCT-WORK-APPLICATION-001 remains open.

### Reciprocal workflow links

- PRODUCT-WORK-APPLICATION-006 uses PRODUCT-REQ-APPLICATION-001 as `source_requirement`.
- PRODUCT-REQ-APPLICATION-001 lists PRODUCT-WORK-APPLICATION-006 in `work_items`.
- PRODUCT-WORK-APPLICATION-006 lists all five child tasks.
- Every child task references PRODUCT-WORK-APPLICATION-006 and PRODUCT-REQ-APPLICATION-001.
- Child dependencies form one T006-01 through T006-05 sequence.
- This task records PRODUCT-WORK-APPLICATION-006 as its only output.

### Preserved contracts

- PRODUCT-ADR-APPLICATION-003 and PRODUCT-ADR-APPLICATION-004 remain current application authority.
- PRODUCT-ADR-UI-001 remains current PWA state-ownership authority.
- Completed selection, retrieval, and outbound-query semantics remain fixed inputs.
- The child flow classifies gaps before deciding whether another ADR is required.
- Queue creation and complete-unit retrieval remain distinct operations.
- Successful empty queues remain distinct from request failures.
- `Unavailable` remains distinct from invalid requests and technical failures.
- PWA-owned queue, loaded-unit, session, navigation, and retry state remains outside the application boundary.
- Unavailable-reference skipping remains distinct from retryable request failure.
- Replacement remains allowed only after successful complete-unit loading.
- Learner-visible attribution remains required while provenance remains excluded.
- Concrete HTTP, serialization, framework, persistence, authentication, and backend-session choices remain excluded.

### Child work-item readiness

- T006-01 can start from repository records without another handoff.
- T006-01 inventories and classifies current contracts without changing specifications.
- T006-02 creates an ADR only for a genuine unresolved normative decision.
- T006-03 defines the transport-independent interface and verification map under accepted authority.
- T006-04 reflects accepted contracts without introducing HTTP or serialization semantics.
- T006-05 requires an independent `PASS` review before work-item closure.

### File and relation verification

- Filesystem directory listings confirmed WORK-006 is the next APPLICATION work item after WORK-005.
- Filesystem rereads confirmed every new H1, metadata ID, filename prefix, source requirement, and dependency.
- Impact refs use current design-record IDs and active `spec:` refs.
- Empty task relations use empty metadata fields rather than literal `[]` values.
- The Design Records MCP validator was not used as evidence because its configured repository root is not confirmed for this project.

### Tooling limitation

- The active filesystem tool has no host command-execution capability.
- The repository is not mounted in the local command container.
- Strict specification validation, `git diff --check`, and `git status --short` were not executed in this session.
- No success claim is made for those host commands.
