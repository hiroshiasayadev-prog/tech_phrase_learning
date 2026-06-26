# PRODUCT-WORK-UI-001: Define failure-category-specific PWA transitions

- **id**: PRODUCT-WORK-UI-001
- **status**: in_progress
- **date**: 2026-06-27
- **source_requirement**: PRODUCT-REQ-UI-001
- **impact_refs**:
  - PRODUCT-ADR-APPLICATION-005
  - PRODUCT-ADR-UI-001
  - PRODUCT-ADR-UI-002
  - spec:product.ui
  - spec:product.ui.learning_flow
  - spec:product.ui.pages.main_page
  - spec:product.ui.pages.learning_page
- **tasks**:
  - PRODUCT-TASK-UI-001-01
  - PRODUCT-TASK-UI-001-02

## Goal

Establish accepted UI authority for category-specific PWA failure transitions.

Coordinate later specification reflection with the existing PWA-interface design flow.

## Boundary

This work item owns UI behavior driven by application failure categories.

The owned behavior includes:

- automatic retry eligibility;
- current-screen preservation;
- learning-flow termination;
- queue and session disposal;
- return-to-main behavior;
- safe diagnostic presentation surfaces.

PRODUCT-ADR-APPLICATION-005 remains the authority for failure meaning, safe diagnostic content, and retryability classification.

PRODUCT-WORK-APPLICATION-006 remains the coordinated owner of PWA-interface contract definition, specification reflection, and independent review.

This work item does not own:

- application failure-category definitions;
- queue creation or retrieval result semantics;
- retry counts, delays, backoff, or timeout configuration;
- HTTP or serialization contracts;
- frontend framework, state library, route structure, or source layout;
- durable learner progress or backend session state.

## Impact Scope

| ref | impact |
|---|---|
| PRODUCT-ADR-APPLICATION-005 | Consume the accepted failure taxonomy and retryability classifications. |
| PRODUCT-ADR-UI-001 | Preserve PWA state ownership and refine generic request-failure handling. |
| PRODUCT-ADR-UI-002 | Record category-specific transition authority. |
| `spec:product.ui` | Reflect the category-specific retry and terminal-failure boundary. |
| `spec:product.ui.learning_flow` | Reflect queue-creation and retrieval transitions by failure category. |
| `spec:product.ui.pages.main_page` | Reflect main-page failure surfaces when required. |
| `spec:product.ui.pages.learning_page` | Reflect current-screen preservation and terminal retrieval failure behavior when required. |

## Task flow

```text
T001-01 Resolve category-specific transitions and accept UI ADR
  |
  v
PRODUCT-TASK-APPLICATION-006-03 / 006-04 / 006-05
  |
  v
T001-02 Verify reflected UI authority and close
```

- T001-01 records the selected UI behavior in an accepted ADR.
- PRODUCT-TASK-APPLICATION-006-03 defines the coordinated interface contract map.
- PRODUCT-TASK-APPLICATION-006-04 reflects accepted application and UI authority into specifications.
- PRODUCT-TASK-APPLICATION-006-05 independently reviews the coordinated result.
- T001-02 verifies the accepted UI decision was reflected and closes this work item.

## Task Candidates

| task | responsibility |
|---|---|
| PRODUCT-TASK-UI-001-01 | Record category-specific PWA transitions in accepted UI authority. |
| PRODUCT-TASK-UI-001-02 | Verify coordinated specification reflection and close the UI resolution flow. |

## Completion Condition

- PRODUCT-ADR-UI-002 is accepted.
- Failure-category definitions remain owned by PRODUCT-ADR-APPLICATION-005.
- Infrastructure failures use the existing UI retry flow.
- Queue-creation mapping and selection-contract failures do not enter automatic retry.
- Retrieval mapping failure ends the active flow and disposes transient queue and session state.
- `Unavailable` remains outside technical-failure handling.
- Safe diagnostics appear at the owning UI failure surface.
- Current UI specifications reflect the accepted decision.
- Coordinated independent review records no blocking finding against the UI transition contract.
- PRODUCT-TASK-UI-001-02 records closure evidence.

## Evidence

- PRODUCT-TASK-UI-001-01 created and accepted PRODUCT-ADR-UI-002.
- Specification reflection and closure remain pending PRODUCT-TASK-APPLICATION-006-04 and PRODUCT-TASK-APPLICATION-006-05.
