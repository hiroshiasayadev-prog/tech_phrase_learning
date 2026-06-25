# PRODUCT-REQ-APPLICATION-001: Define implementation-ready application design contracts

- **id**: PRODUCT-REQ-APPLICATION-001
- **status**: accepted
- **date**: 2026-06-26
- **source_refs**: [PRODUCT-ADR-APPLICATION-001, spec:product.application, spec:product.application.published_content, spec:product.application.learning_unit_selection]
- **work_items**: [PRODUCT-WORK-APPLICATION-001]

## Requirement

The first-MVP application boundary requires detailed, implementation-independent contracts before implementation planning begins.

The detailed design must separate module ownership while preserving the accepted application architecture.

## Evidence

PRODUCT-ADR-APPLICATION-001 establishes the runtime application boundary and dependency direction.

The current application specs define the architecture slice but intentionally defer module-level contracts.

The deferred contracts include publication handoff, selection policy, retrieval results, outbound ports, and the PWA-facing interface.

## Required Outcome

- Each major application module has a focused design work item with a self-contained scope.
- Module-level decisions are recorded in ADRs when architectural judgment is required.
- Current contracts are reflected in application, pipeline, learning, and UI specifications.
- Cross-module dependencies and result semantics are consistent.
- Implementation work can be planned without reopening the application ownership boundary.
- Concrete frameworks, database schemas, SQL, HTTP routes, and source layouts remain deferred until their owning design work requires them.

## Explicitly Excluded Scope

- Application implementation.
- Pipeline implementation.
- PWA implementation.
- Concrete database selection and schema design.
- Concrete HTTP routes and wire schemas.
- Deployment architecture.

## Boundary

This requirement owns detailed application design readiness.

PRODUCT-ADR-APPLICATION-001 remains the source of truth for the accepted top-level architecture.

Focused work items own each module's detailed resolution flow.
