# PRODUCT-TASK-APPLICATION-001-01: Open published-content and handoff design

- **id**: PRODUCT-TASK-APPLICATION-001-01
- **status**: not_started
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-001
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**: []
- **outputs**: []

## Goal

Create a focused work item for the published-content projection and pipeline-to-application handoff module.

The created work item must be executable without a separate conversation handoff.

## Work

1. Read PRODUCT-ADR-APPLICATION-001 and `spec:product.application.published_content`.
2. Read the publication and provenance rules in `spec:product.pipeline` and `spec:product.learning.learning_unit`.
3. Create the next APPLICATION work item under PRODUCT-REQ-APPLICATION-001.
4. Use a title equivalent to `Define published-content projection and publication handoff`.
5. Add the new work item to PRODUCT-REQ-APPLICATION-001 `work_items`.
6. Record the created work-item ID in this task's `outputs` and evidence.
7. Give the child work item a task graph that resolves the module contracts below.

Required child scope:

- stable learning-unit identity and current published projection;
- separation of current content and availability;
- publication, withdrawal, and republication transitions;
- atomic switch of content, provenance reference, and resulting availability;
- semantic artifact or write contract crossing from pipeline to published content;
- validation already complete before publication;
- opaque provenance reference reachability;
- pipeline write ownership and application read ownership;
- consistency requirements visible to concurrent application reads;
- required ADR or spec updates.

Required exclusions:

- concrete tables and columns;
- database product selection;
- ORM selection;
- transaction syntax;
- pipeline generation prompts;
- application retrieval and shuffle behavior except where the handoff constrains them.

The child work item may create an investigation when evidence is insufficient.
The child work item must create an ADR when it adopts a new architectural decision.

## Done condition

- One focused APPLICATION work item exists for the published-content and handoff module.
- The child work item references PRODUCT-REQ-APPLICATION-001.
- PRODUCT-REQ-APPLICATION-001 lists the child work item.
- The child work item contains the required scope, exclusions, task flow, and completion conditions.
- The child scope does not duplicate PRODUCT-WORK-APPLICATION-001 coordination ownership.
- This task records the child work-item ID in `outputs` and `## Evidence`.

## Verification

- Check the child work item's path, H1, metadata, source requirement, impact refs, and canonical references.
- Check reciprocal linkage from PRODUCT-REQ-APPLICATION-001.
- Confirm that a new session can start the child work item using repository records only.

## Evidence

TBD
