# PRODUCT-TASK-PRODUCT-001-01: Establish first-MVP design baseline and gap inventory

- **id**: PRODUCT-TASK-PRODUCT-001-01
- **status**: not_started
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PRODUCT-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 2d
- **depends_on**: []
- **outputs**:
  - PRODUCT-WORK-PRODUCT-001

## Goal

Establish the current first-MVP design-readiness baseline and route each remaining gap to one semantic owner.

## Work

1. Read `spec:product` and every top-level area overview.
2. Read current accepted ADRs for learning, pipeline, application, and UI.
3. Read PRODUCT-WORK-APPLICATION-001 and its final integration evidence.
4. Inventory existing requirements, work items, tasks, investigations, and child specifications by area.
5. Classify each remaining concern as:
   - resolved current contract;
   - missing normative decision;
   - missing specification detail;
   - missing completeness review;
   - implementation-only choice;
   - cross-area integration gap.
6. Assign one semantic owner to every normative gap.
7. Identify dependency order among learning, pipeline, UI, and runtime integration work.
8. Record the child work-item scope needed by T02 through T05.
9. Stop as `blocked` when a gap has no clear owner or requires a user decision before work-item creation.
10. Do not change normative specifications in this task.

Required inventory coverage:

- learning model, path, learning-unit, and quiz-session completeness;
- pipeline stages, intermediate artifacts, validation, retries, identity, provenance, publication, and orchestration;
- UI flow, pages, component responsibilities, terminal states, reload, and empty states;
- pipeline writer to published-content boundary;
- application outbound reader and PWA-facing interface;
- persistence and transport adapter ownership;
- cross-area tests and end-to-end acceptance boundaries.

## Done condition

- Every current first-MVP area has a recorded readiness judgment.
- Each remaining normative gap has one owner or an explicit blocking reason.
- Implementation-only choices are separated from semantic design gaps.
- Child work-item scopes for T02 through T05 are self-contained.
- Dependency order is explicit.
- No normative specification is changed.

## Verification

- Check the inventory against `spec:product` dependency direction.
- Confirm application design is treated as completed input rather than silently reopened.
- Confirm every proposed normative change names an accepted ADR or a missing-ADR follow-up.
- Confirm persistence and transport concerns do not become a new semantic spec area without a decision.
- Validate H1, metadata, canonical refs, reciprocal workflow links, and required sections.
- Run `git diff --check` and inspect `git status --short` before marking done.

## Evidence

TBD
