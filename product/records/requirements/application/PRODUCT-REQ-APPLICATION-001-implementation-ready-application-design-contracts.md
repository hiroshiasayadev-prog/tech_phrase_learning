# PRODUCT-REQ-APPLICATION-001: Define implementation-ready application design contracts

- **id**: PRODUCT-REQ-APPLICATION-001
- **status**: accepted
- **date**: 2026-06-26
- **source_refs**: [PRODUCT-ADR-APPLICATION-003, PRODUCT-ADR-APPLICATION-004, spec:product.application, spec:product.application.published_content, spec:product.application.learning_unit_selection]
- **work_items**:
  - PRODUCT-WORK-APPLICATION-001
  - PRODUCT-WORK-APPLICATION-002
  - PRODUCT-WORK-APPLICATION-003
  - PRODUCT-WORK-APPLICATION-004
  - PRODUCT-WORK-APPLICATION-005
  - PRODUCT-WORK-APPLICATION-006

## Requirement

The first-MVP application boundary requires detailed, implementation-independent contracts before implementation planning begins.

The detailed design must separate module ownership while preserving the accepted application architecture.

## Evidence

PRODUCT-ADR-APPLICATION-003 establishes the current published-content and retrieval boundary.

PRODUCT-ADR-APPLICATION-004 establishes the outbound retrieval-port and persistence-adapter boundary.

Before focused design work, the application specifications defined the architecture slice while deferring module-level contracts.

The deferred set included publication handoff, selection policy, retrieval results, outbound ports, and the PWA-facing interface.

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

PRODUCT-ADR-APPLICATION-003 and PRODUCT-ADR-APPLICATION-004 remain the current decision sources for the accepted application architecture.

Focused work items own each module's detailed resolution flow.
