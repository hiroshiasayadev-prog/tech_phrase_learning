# PRODUCT-REQ-UI-001: Define failure-category-specific PWA transitions

- **id**: PRODUCT-REQ-UI-001
- **status**: accepted
- **date**: 2026-06-27
- **source_refs**:
  - PRODUCT-REQ-APPLICATION-001
  - PRODUCT-TASK-APPLICATION-006-01
  - PRODUCT-ADR-UI-001
  - spec:product.ui.learning_flow
- **work_items**:
  - PRODUCT-WORK-UI-001

## Requirement

The PWA requires failure-category-specific transitions for queue creation and learning-unit retrieval.

The UI must handle retryable infrastructure failures separately from non-retryable mapping and contract-violation failures.

The UI must preserve PWA ownership of navigation, queue state, session state, retry attempts, and diagnostic presentation.

## Evidence

PRODUCT-TASK-APPLICATION-006-01 identified category-specific PWA transitions as an unresolved UI-owned normative decision.

PRODUCT-ADR-UI-001 defines generic request retry behavior and assigns transient learner-flow state to the PWA.

The current UI specification does not define different transitions for infrastructure, mapping, and selection-contract failures.

## Required Outcome

- `InfrastructureFailure` retains automatic retry behavior.
- Retrieval `MappingFailure` ends the current learning flow.
- Retrieval `MappingFailure` discards the active queue and session before returning to main.
- Queue-creation `MappingFailure` keeps the PWA on the main page without automatic retry.
- Queue-creation `InvalidSelectionResult` keeps the PWA on the main page without automatic retry.
- Safe diagnostic information appears at the UI surface that owns the failure.
- `Unavailable` skips only the affected reference and does not enter technical-failure handling.
- Queue position, loaded content, and session still change only after successful replacement loading.
- The application boundary does not own screen transitions, queue disposal, session disposal, or diagnostic presentation.
- An accepted UI ADR authorizes these transitions before specification reflection.

## Explicitly Excluded Scope

- Application failure-category definitions and retryability semantics.
- HTTP status codes, transport errors, and wire schemas.
- Concrete retry delays, backoff, timeout values, and client configuration.
- Component layout, styling, and exact diagnostic wording.
- Durable learner progress, backend sessions, and queue persistence.
- Framework, state library, route structure, and source layout.

## Boundary

This requirement owns PWA transitions driven by application failure categories.

The application area owns the failure taxonomy, safe diagnostic contract, and retryability classification.
