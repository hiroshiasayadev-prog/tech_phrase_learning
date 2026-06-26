# PRODUCT-ADR-APPLICATION-005: Expose classified failures to the PWA

- **status**: accepted
- **date**: 2026-06-27
- **depends_on**:
  - PRODUCT-ADR-APPLICATION-003
  - PRODUCT-ADR-APPLICATION-004
- **supersedes**:
- **migrated_to_spec**: 2026-06-27

## Context

The PWA consumes queue creation and published learning-unit retrieval through the application boundary.

Current authority keeps technical failures outside normal queue and availability results.

Current authority does not define the failure categories exposed to the PWA.

The PWA requires semantic categories that distinguish contract violations, mapping failures, and infrastructure failures.

The categories must support later UI decisions without exposing implementation internals.

## Decision

The PWA-facing application interface exposes these queue-creation failure categories:

- `InvalidSelectionResult`;
- `MappingFailure`;
- `InfrastructureFailure`.

The PWA-facing application interface exposes these retrieval failure categories:

- `MappingFailure`;
- `InfrastructureFailure`.

`InvalidSelectionResult` means the application detected that an outbound selection result violated the accepted selection contract.

`InvalidSelectionResult` does not mean the PWA submitted an invalid request.

`MappingFailure` means application-visible data could not be mapped into an application-owned contract.

`MappingFailure` is non-retryable for the failed operation.

`InfrastructureFailure` means required technical infrastructure could not complete the operation.

`InfrastructureFailure` is retryable for the failed operation.

Each exposed failure must provide safe diagnostic information for the owning failure surface.

Safe diagnostic information may identify the failure category, affected operation, and a sanitized summary.

The product contract must not expose:

- raw exceptions;
- stack traces;
- credentials or secrets;
- SQL or database internals;
- filesystem paths;
- framework internals;
- equivalent unsafe implementation details.

These failure categories remain outside normal queue, `Available`, `Unavailable`, and successful empty-queue results.

This decision does not define retry counts, screen transitions, navigation, queue disposal, session disposal, or diagnostic presentation.

## Rationale

Distinct failure categories let the PWA react without interpreting exceptions or adapter details.

Separating `InvalidSelectionResult` prevents an outbound contract violation from appearing as invalid PWA input.

Retryability classification gives the UI a stable semantic input while preserving UI ownership of retry behavior.

Sanitized diagnostics support learner-visible failure handling and operational investigation without creating an unsafe public contract.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Expose one generic application failure | The PWA could not distinguish retryable infrastructure failure from non-retryable contract or mapping failure. |
| Treat `InvalidSelectionResult` as an invalid PWA request | Queue creation has no learner-supplied semantic parameters in the first MVP. |
| Convert mapping failure to `Unavailable` | Data or adapter failure must not look like a normal availability result. |
| Expose raw exceptions to the PWA | Raw implementation details are unsafe and transport-dependent. |
| Define concrete UI transitions in this ADR | Screen and transient-state behavior belong to the UI area. |

## Consequences

- PWA-facing queue creation must preserve three distinct failure categories.
- PWA-facing retrieval must preserve mapping and infrastructure failure categories.
- Future transport adapters must preserve category and safe diagnostic meaning.
- UI decisions may use retryability without owning application failure classification.
- UI-owned transition behavior requires separate accepted authority.
- Concrete wire schemas, exception types, and diagnostic serialization remain deferred.
- PRODUCT-TASK-APPLICATION-006-03 may use this ADR as application failure authority after T006-02 closes.

## Evidence

- PRODUCT-REQ-APPLICATION-002 records the need for a PWA-facing failure contract.
- PRODUCT-TASK-APPLICATION-006-01 identifies the public failure taxonomy, safe diagnostics, and retryability as genuine decision gaps.
- PRODUCT-ADR-APPLICATION-003 separates technical failures from normal availability results.
- PRODUCT-ADR-APPLICATION-004 preserves mapping and infrastructure failures outside normal retrieval results.
- The user selected the failure categories, safe diagnostic boundary, and retryability classifications during T006 baseline review.
