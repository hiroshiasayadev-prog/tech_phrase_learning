# PRODUCT-TASK-APPLICATION-001-05: Open PWA-facing application-interface design

- **id**: PRODUCT-TASK-APPLICATION-001-05
- **status**: not_started
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-001
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**: [PRODUCT-TASK-APPLICATION-001-02, PRODUCT-TASK-APPLICATION-001-03]
- **outputs**: []

## Goal

Create a focused work item for the transport-independent interface consumed by the PWA.

The created work item must be executable without a separate conversation handoff.

## Work

1. Read PRODUCT-ADR-APPLICATION-001 and `spec:product.application.learning_unit_selection`.
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
- result classification for found, unavailable, invalid request, and infrastructure failure;
- distinction between unavailable-reference skipping and retryable failure;
- empty-queue and exhausted-queue behavior;
- preservation of the PWA's queue and session ownership;
- replacement only after successful unit loading;
- attribution content required by the learner flow;
- future mapping to HTTP without making HTTP semantics normative here;
- required ADR or spec updates.

Required exclusions:

- concrete routes;
- concrete HTTP status codes;
- JSON field names and serialization format;
- retry delays and transport-client configuration;
- component implementation;
- authentication and learner accounts.

The child work item must not introduce backend session identity.
The child work item must keep network failures distinct from unavailable content.

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
- Compare result semantics against `spec:product.ui.learning_flow`.
- Confirm that a new session can start the child work item using repository records only.

## Evidence

TBD
