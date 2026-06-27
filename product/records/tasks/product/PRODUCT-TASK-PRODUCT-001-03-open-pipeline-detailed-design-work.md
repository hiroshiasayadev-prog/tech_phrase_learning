# PRODUCT-TASK-PRODUCT-001-03: Open pipeline detailed-design work

- **id**: PRODUCT-TASK-PRODUCT-001-03
- **status**: not_started
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PRODUCT-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-PRODUCT-001-02
- **outputs**: []

## Goal

Create one focused work item that decomposes the first-MVP content pipeline into implementation-ready semantic contracts.

## Work

1. Read the T01 baseline and the focused learning work item created by T02.
2. Read all current pipeline ADRs, investigations, fixtures, experiments, and `spec:product.pipeline`.
3. Create the first PIPELINE work item under PRODUCT-REQ-PRODUCT-001.
4. Use a title equivalent to `Define first-MVP content-pipeline contracts`.
5. Add the new work item to PRODUCT-REQ-PRODUCT-001 `work_items`.
6. Record the created work-item ID in this task's `outputs` and Evidence.
7. Give the child work item a task graph that covers:
   - source acquisition and retained-source reuse;
   - authentic post and conversation-tree normalization;
   - deterministic path enumeration;
   - path validation and suitability filtering;
   - reusable post-summary generation;
   - path-specific summary revision;
   - target-phrase selection;
   - three-option quiz generation;
   - mechanical and model-based validation;
   - retry, rejection, and invalid-output handling;
   - stable artifact and learning-unit identity;
   - current provenance ownership;
   - automated publication-gate inputs and outcomes;
   - `PublicationHandoff` and `AvailabilityChange` production;
   - pipeline orchestration and stage dependency order;
   - child specification decomposition under `spec:product.pipeline`;
   - ADR-first resolution, specification reflection, and independent review.
8. Require explicit stage input/output boundaries without selecting concrete source layout or workflow framework.
9. Preserve learning ownership of pedagogical meaning and application ownership of runtime reads.

## Done condition

- One focused PIPELINE work item exists under PRODUCT-REQ-PRODUCT-001.
- The child work item has a complete task graph for pipeline decisions, specifications, and review.
- PRODUCT-REQ-PRODUCT-001 lists the child work item.
- The child scope separates deterministic processing, semantic model tasks, validation, and publication.
- The child scope requires focused child pipeline specifications.
- Concrete implementation technologies remain excluded.
- This task records the child work-item ID in `outputs` and Evidence.

## Verification

- Check the child work item's H1, metadata, source requirement, reciprocal link, and impact refs.
- Confirm the child scope preserves PRODUCT-ADR-PIPELINE-002 and PRODUCT-ADR-PIPELINE-005.
- Confirm learning semantics are consumed rather than redefined.
- Confirm publication outputs match the current published-content boundary.
- Confirm a new session can start the child work item from repository records only.
- Run relevant record validation, `git diff --check`, and `git status --short`.

## Evidence

TBD
