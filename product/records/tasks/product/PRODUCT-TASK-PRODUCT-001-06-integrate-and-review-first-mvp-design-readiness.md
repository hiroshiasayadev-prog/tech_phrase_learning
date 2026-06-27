# PRODUCT-TASK-PRODUCT-001-06: Integrate and review first-MVP design readiness

- **id**: PRODUCT-TASK-PRODUCT-001-06
- **status**: not_started
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PRODUCT-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 2d
- **depends_on**:
  - PRODUCT-TASK-PRODUCT-001-02
  - PRODUCT-TASK-PRODUCT-001-03
  - PRODUCT-TASK-PRODUCT-001-04
  - PRODUCT-TASK-PRODUCT-001-05
- **outputs**:
  - PRODUCT-REQ-PRODUCT-001
  - PRODUCT-WORK-PRODUCT-001

## Goal

Integrate completed first-MVP design work and determine whether implementation planning may begin without reopening unresolved semantic contracts.

## Work

1. Read PRODUCT-WORK-PRODUCT-001 and every focused child work item created by T02 through T05.
2. Require each focused child work item to be `done` or explicitly deferred without blocking implementation planning.
3. Read PRODUCT-WORK-APPLICATION-001 as completed application input.
4. Read every accepted ADR and current specification changed or relied on by the child work items.
5. Build one cross-area ownership, dependency, result, state, publication, and integration matrix.
6. Verify that learning semantics constrain pipeline and UI without depending on their implementation.
7. Verify that pipeline production and publication match learning and published-content contracts.
8. Verify that application selection, retrieval, outbound ports, and PWA-facing results remain consistent with pipeline and UI contracts.
9. Verify that UI normal, empty, unavailable, loading, retry, failure, terminal, and disposal transitions cover every application outcome.
10. Verify that runtime integration obligations preserve semantic ownership across writers, readers, transport adapters, and PWA state.
11. Reconcile contradictions only when an accepted ADR authorizes the correction.
12. Stop and create decision follow-up work when accepted authority is missing.
13. Confirm that unresolved choices are implementation-only and have explicit owners.
14. Record implementation work-item candidates without starting implementation.
15. Request an independent review of the complete first-MVP design baseline.
16. Apply authorized corrections and repeat independent review until `PASS`.
17. Update PRODUCT-WORK-PRODUCT-001 Evidence and completion state only after all conditions pass.

Required integration checks:

- Every learner-visible field and transition has one semantic owner.
- Every pipeline stage has explicit input, output, validation, failure, identity, and downstream obligations.
- Publication exposes one complete committed current state without partial mutation.
- Application consumes only published-content and application-owned port contracts.
- Transport mapping adds no new application or UI semantics.
- PWA state remains transient and backend-session-free.
- Normal empty and unavailable outcomes remain distinct from failures.
- Retry applies only to retryable infrastructure failure.
- Provenance remains pipeline-owned and opaque outside the publication boundary.
- Concrete technology choices remain outside normative semantic specifications unless separately decided.

## Done condition

- Every focused child work item is resolved or non-blockingly deferred.
- Learning, pipeline, application, UI, and runtime integration contracts are consistent.
- Every normative specification change traces to an accepted ADR.
- Requirement, work-item, and task Evidence does not act as design authority.
- No unresolved semantic ownership, result, transition, publication, or integration gap blocks implementation planning.
- Implementation work-item candidates are recorded separately from design completion.
- Strict validators and working-tree checks succeed for the complete change set.
- An independent reviewer records `PASS` with no blocking or major finding.
- PRODUCT-REQ-PRODUCT-001 required outcomes are satisfied at the design level.
- PRODUCT-WORK-PRODUCT-001 contains substantive final Evidence and can be marked `done`.

## Verification

- Validate H1, metadata, canonical refs, reciprocal workflow links, and required sections for all new and modified records.
- Review dependency direction against `spec:product`.
- Confirm current accepted ADR status and supersession chains.
- Confirm accepted ADR decision-bearing text was not rewritten during integration.
- Confirm every changed specification is owned by the area whose contract it defines.
- Run strict specification validation for the complete PRODUCT spec tree.
- Run `git diff --check` and inspect `git status --short`.
- Inspect a scoped diff covering requirements, investigations, ADRs, work items, tasks, and specifications changed by this hub.
- Record the independent review verdict and finding disposition in Evidence.

## Evidence

TBD
