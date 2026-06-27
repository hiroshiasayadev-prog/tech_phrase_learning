# PRODUCT-TASK-PRODUCT-001-05: Open runtime integration-boundary design work

- **id**: PRODUCT-TASK-PRODUCT-001-05
- **status**: not_started
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PRODUCT-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-PRODUCT-001-03
  - PRODUCT-TASK-PRODUCT-001-04
- **outputs**: []

## Goal

Create one focused PRODUCT work item for cross-area runtime integration boundaries that do not belong to one semantic layer alone.

## Work

1. Read the T01 baseline and the focused pipeline and UI work items created by T03 and T04.
2. Read PRODUCT-WORK-APPLICATION-001 and all current publication, outbound-query, PWA-interface, and UI transition specifications.
3. Create the next PRODUCT work item under PRODUCT-REQ-PRODUCT-001.
4. Use a title equivalent to `Define first-MVP runtime integration boundaries`.
5. Add the new work item to PRODUCT-REQ-PRODUCT-001 `work_items`.
6. Record the created work-item ID in this task's `outputs` and Evidence.
7. Give the child work item a task graph that covers:
   - pipeline publication writer to current published-state boundary;
   - atomic replacement and availability-only mutation verification;
   - persistence adapter implementation obligations for application-owned outbound queries;
   - one committed current-state read semantics;
   - application use-case to transport-adapter mapping;
   - transport preservation of normal results, failure categories, safe diagnostics, and `LearningUnitRef` semantics;
   - PWA consumption of transport results without moving UI state into the backend;
   - cross-boundary error translation and unsafe-detail exclusion;
   - integration-test and contract-test ownership;
   - end-to-end acceptance boundaries from publication through learner-visible flow;
   - ADR-first resolution of genuine cross-area decisions;
   - owner-spec reflection and independent review.
8. Route each normative correction back to the owning pipeline, application, learning, or UI specification.
9. Keep database, ORM, SQL, protocol, route, JSON, framework, deployment, and source-layout choices outside the child work item.
10. Do not create a new semantic specification area for persistence or transport without an accepted decision.

## Done condition

- One focused PRODUCT work item exists under PRODUCT-REQ-PRODUCT-001.
- The child work item has a self-contained cross-area boundary and task graph.
- PRODUCT-REQ-PRODUCT-001 lists the child work item.
- The child scope distinguishes owner contracts from adapter implementation obligations.
- The child scope includes contract-test and end-to-end verification ownership.
- Concrete technology choices remain excluded.
- This task records the child work-item ID in `outputs` and Evidence.

## Verification

- Check the child work item's H1, metadata, source requirement, reciprocal link, and impact refs.
- Confirm no PRODUCT work-item evidence becomes normative authority.
- Confirm publication writes remain pipeline-owned, outbound ports remain application-owned, and transient learner state remains UI-owned.
- Confirm the child work item routes normative changes to owning ADRs and specifications.
- Confirm a new session can start the child work item from repository records only.
- Run relevant record validation, `git diff --check`, and `git status --short`.

## Evidence

TBD
