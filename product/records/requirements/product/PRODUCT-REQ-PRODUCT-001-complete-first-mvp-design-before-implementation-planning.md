# PRODUCT-REQ-PRODUCT-001: Complete first-MVP design before implementation planning

- **id**: PRODUCT-REQ-PRODUCT-001
- **status**: accepted
- **date**: 2026-06-27
- **source_refs**:
  - spec:product
  - spec:product.learning
  - spec:product.pipeline
  - spec:product.application
  - spec:product.ui
  - PRODUCT-WORK-APPLICATION-001
- **work_items**:
  - PRODUCT-WORK-PRODUCT-001
  - PRODUCT-WORK-LEARNING-001
  - PRODUCT-WORK-PIPELINE-001

## Requirement

The first MVP requires an integrated design baseline across learning, pipeline, application, UI, and runtime integration boundaries before implementation planning begins.

Application detailed design is complete and acts as a fixed input unless later cross-area review identifies an accepted-authority conflict.

The remaining design areas must reach comparable implementation-planning readiness without moving layer-owned semantics into PRODUCT coordination records.

## Evidence

PRODUCT-WORK-APPLICATION-001 completed detailed application design and recorded an independent integrated `PASS`.

`spec:product.pipeline` still owns all pipeline contracts in one overview and states that no child pipeline specifications exist.

At capture time, learning specifications defined learner-facing semantics without a focused work item for implementation-planning completeness.

UI specifications define the first-MVP learner flow, pages, and component responsibilities.
The only completed UI work item addresses failure-category transitions rather than whole-area readiness.

Before this requirement was opened, no requirement or work item coordinated remaining first-MVP design across all areas.

## Required Outcome

- Application detailed design remains a completed input to cross-area design work.
- Learning contracts receive a focused completeness review before pipeline implementation planning.
- Pipeline contracts are decomposed into focused design work with explicit stage, artifact, validation, publication, and orchestration boundaries.
- UI contracts receive a focused whole-area design review beyond failure-transition handling.
- Cross-area runtime integration boundaries are designed for publication writes, persistence reads, application transport, and PWA consumption.
- Each normative change is authorized by an accepted ADR and reflected in the owning specification area.
- Cross-area dependency direction remains consistent with `spec:product`.
- An independent final review records `PASS` with no blocking or major finding.
- Implementation work can be planned without reopening unresolved first-MVP semantic ownership or result contracts.

## Explicitly Excluded Scope

- Application, pipeline, persistence, transport, or PWA implementation.
- Concrete programming language, framework, database, ORM, SQL, HTTP route, JSON schema, state library, deployment, or source-layout selection.
- Reopening completed application design without a cross-area conflict or new accepted decision.
- Using PRODUCT requirement, work-item, or task evidence as normative design authority.

## Boundary

This requirement owns first-MVP design-completion readiness across areas.

Each area owns its normative contracts through accepted ADRs and current specifications.

PRODUCT work items coordinate gap discovery, focused work-item creation, dependency order, integration review, and readiness judgment.
