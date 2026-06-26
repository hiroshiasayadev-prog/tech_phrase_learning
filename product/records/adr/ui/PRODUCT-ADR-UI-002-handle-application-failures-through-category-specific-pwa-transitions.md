# PRODUCT-ADR-UI-002: Handle application failures through category-specific PWA transitions

- **status**: accepted
- **date**: 2026-06-27
- **depends_on**:
  - PRODUCT-ADR-UI-001
  - PRODUCT-ADR-APPLICATION-005
- **supersedes**:
- **migrated_to_spec**: 2026-06-27

## Context

PRODUCT-ADR-UI-001 assigns transient queue, session, navigation, loading, and retry behavior to the PWA.

PRODUCT-ADR-UI-001 defines one generic request-failure retry flow.

PRODUCT-ADR-APPLICATION-005 now exposes distinct PWA-facing failure categories with retryability semantics.

Initial queue creation starts on the main page.

Replacement queue creation starts from an exhausted queue on the learning page.

The PWA requires category-specific transitions for both contexts while preserving existing state ownership and successful-replacement behavior.

## Decision

`InfrastructureFailure` enters the existing PWA request-retry flow.

The existing retry count and manual retry behavior remain unchanged.

During initial queue-creation retry, the PWA must remain on the main page.

During replacement queue-creation retry, the PWA must keep the current learning screen, loaded learning unit, exhausted queue state, and session unchanged.

The learning page remains the owning retry surface after replacement queue-creation automatic retries are exhausted.

During retrieval retry, the PWA must keep the current screen, loaded learning unit, queue position, and session unchanged.

An initial queue-creation `MappingFailure` must not enter automatic retry.

The PWA must remain on the main page after an initial queue-creation `MappingFailure`.

The main page is the owning failure surface for its safe diagnostic information.

An initial queue-creation `InvalidSelectionResult` must not enter automatic retry.

The PWA must remain on the main page after an initial queue-creation `InvalidSelectionResult`.

The main page is the owning failure surface for its safe diagnostic information.

A replacement queue-creation `MappingFailure` must not enter automatic or manual retry.

A replacement queue-creation `InvalidSelectionResult` must not enter automatic or manual retry.

The PWA must keep the current learning screen, loaded learning unit, exhausted queue state, and session while either replacement failure is displayed.

The learning page is the owning failure surface for the safe diagnostic information.

The replacement failure surface must present a `Back to main` action after the safe diagnostic information.

Selecting `Back to main` must discard the active queue and session under the existing transient lifecycle rule.

A retrieval `MappingFailure` must end the current learning flow.

The PWA must discard the active learning queue and session before returning to the main page.

The returned main page is the owning failure surface for the safe retrieval-mapping diagnostic.

A retrieval `MappingFailure` must not retain the previous learning flow as a manual retry surface.

`Unavailable` remains a normal availability result.

The PWA must remove only the affected pending reference and continue with the next pending reference.

`Unavailable` must not enter technical-failure retry or diagnostic handling.

Queue position, loaded content, and session must still change only after successful replacement loading.

Flow termination after retrieval `MappingFailure` is state disposal, not replacement loading.

The PWA must present only safe diagnostic information supplied by the application contract.

This decision does not define exact diagnostic wording, component layout, route paths, or styling.

## Rationale

Infrastructure failure may be transient, so the existing retry flow remains appropriate.

Mapping failure indicates a non-retryable contract or data translation problem.

Ending the active flow after retrieval mapping failure avoids retaining a queue that may lead to repeated unusable content.

Keeping initial queue-creation failures on the main page preserves the page that already owns initial acquisition.

Keeping replacement infrastructure failure on the learning page preserves the current learner context during a potentially transient failure.

Replacement mapping and selection-contract failures indicate unexpected defects rather than learner-recoverable conditions.

A diagnostic-only learning-page surface supports debugging while giving the learner an explicit exit.

Treating `Unavailable` separately preserves normal stale-reference skipping.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Apply the same retry flow to every failure category | Non-retryable mapping and contract failures would repeat without a valid recovery path. |
| Keep the active learning flow after retrieval mapping failure | The active queue may continue to depend on content that cannot be mapped safely. |
| Treat retrieval mapping failure like `Unavailable` | Technical data failure must not appear as normal content unavailability. |
| Return to main without discarding queue and session | Hidden transient state could incorrectly resume a terminated flow. |
| Automatically retry replacement mapping or selection-contract failures | These failures indicate an unexpected contract or mapping defect. |
| Return immediately to main after replacement mapping or selection-contract failure | The current learning page provides the useful diagnostic context and an explicit learner-controlled exit. |
| Define application failure meanings in the UI ADR | Failure taxonomy and retryability belong to PRODUCT-ADR-APPLICATION-005. |

## Consequences

- UI specifications must branch request-failure transitions by application failure category.
- Infrastructure failures continue using the existing automatic and manual retry flow.
- Initial queue-creation mapping and invalid-selection failures remain on main without automatic retry.
- Replacement queue-creation infrastructure failure retains the current learning screen and state through automatic and manual retry.
- Replacement queue-creation mapping and invalid-selection failures remain on the learning page without retry.
- Replacement non-retryable failure surfaces provide safe diagnostic information and `Back to main`.
- Retrieval mapping failure terminates the flow, disposes queue and session, and returns to main.
- Safe diagnostics must appear at the owning main or current-screen failure surface.
- `Unavailable` remains a normal skip transition.
- PRODUCT-ADR-UI-001 remains valid and is not superseded.
- PRODUCT-TASK-APPLICATION-006-03 may use this ADR as UI transition authority after T006-02 closes.

## Evidence

- PRODUCT-REQ-UI-001 records the need for category-specific PWA transitions.
- PRODUCT-TASK-APPLICATION-006-01 identifies the transition behavior as a genuine UI-owned decision gap.
- PRODUCT-ADR-UI-001 owns transient queue, session, navigation, and retry state.
- PRODUCT-ADR-APPLICATION-005 defines the failure categories and retryability classifications consumed by this decision.
- The user selected the initial and retrieval transitions during the PWA-interface baseline review.
- The user selected replacement queue-creation transitions during T006-04 unblock review.
- Replacement `InfrastructureFailure` uses the existing retry flow on the learning page.
- Replacement `MappingFailure` and `InvalidSelectionResult` show a safe diagnostic and `Back to main` without retry.
