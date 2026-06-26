# PRODUCT-REQ-APPLICATION-002: Define the PWA-facing failure contract

- **id**: PRODUCT-REQ-APPLICATION-002
- **status**: accepted
- **date**: 2026-06-27
- **source_refs**:
  - PRODUCT-REQ-APPLICATION-001
  - PRODUCT-TASK-APPLICATION-006-01
  - PRODUCT-ADR-APPLICATION-003
  - PRODUCT-ADR-APPLICATION-004
- **work_items**:

## Requirement

The PWA-facing application interface requires an explicit failure contract for queue creation and learning-unit retrieval.

The contract must distinguish outbound selection-contract violations, mapping failures, and infrastructure failures from normal application results.

The contract must expose safe diagnostic information without exposing unsafe implementation internals.

The contract must classify application-facing failure retryability without defining UI transition behavior.

## Evidence

PRODUCT-TASK-APPLICATION-006-01 identified the public failure taxonomy, safe diagnostic contract, and retryability classification as unresolved normative decisions.

PRODUCT-ADR-APPLICATION-003 separates technical failures from normal availability results.

PRODUCT-ADR-APPLICATION-004 requires mapping and infrastructure failures to remain outside normal retrieval results.

Current application specifications do not define the complete PWA-facing failure contract.

## Required Outcome

- Queue creation exposes `InvalidSelectionResult`, `MappingFailure`, and `InfrastructureFailure` as distinct failure categories.
- `InvalidSelectionResult` represents an outbound selection-contract violation.
- `InvalidSelectionResult` does not represent an invalid PWA request.
- Retrieval exposes `MappingFailure` and `InfrastructureFailure` as distinct technical failure categories.
- Contract violations and technical failures may carry safe diagnostic information.
- Raw exceptions, stack traces, credentials, SQL, filesystem paths, and equivalent unsafe internals are excluded from the product contract.
- `InfrastructureFailure` is classified as retryable.
- `MappingFailure` is classified as non-retryable.
- Normal queue, `Available`, `Unavailable`, and successful empty-queue results remain unchanged.
- An accepted APPLICATION ADR authorizes the failure contract before specification reflection.

## Explicitly Excluded Scope

- UI retry counts, screen preservation, navigation, queue disposal, and session disposal.
- Diagnostic presentation layout and wording.
- HTTP routes, status codes, headers, and wire schemas.
- Concrete exception classes and programming-language result types.
- Retry delays, backoff, timeout values, and client configuration.
- Persistence implementation and database diagnostics.

## Boundary

This requirement owns PWA-facing application failure semantics, safe diagnostic boundaries, and retryability classification.

The UI area owns result-driven screen transitions and diagnostic presentation.
