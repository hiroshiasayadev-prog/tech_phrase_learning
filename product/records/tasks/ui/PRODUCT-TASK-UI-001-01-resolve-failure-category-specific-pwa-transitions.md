# PRODUCT-TASK-UI-001-01: Resolve failure-category-specific PWA transitions

- **id**: PRODUCT-TASK-UI-001-01
- **status**: done
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-UI-001
- **source_requirement**: PRODUCT-REQ-UI-001
- **estimate**: 0.5d
- **depends_on**:
- **outputs**:
  - PRODUCT-ADR-UI-002

## Goal

Create accepted UI authority for PWA transitions driven by application failure categories.

## Work

1. Read PRODUCT-ADR-UI-001 as current UI state-ownership authority.
2. Read PRODUCT-ADR-APPLICATION-005 as current application failure authority.
3. Preserve existing retry counts and successful-replacement behavior.
4. Define queue-creation behavior for infrastructure, mapping, and invalid-selection failures.
5. Define retrieval behavior for infrastructure and mapping failures.
6. Preserve `Unavailable` as a normal availability outcome.
7. Assign safe diagnostic presentation to the owning UI failure surface.
8. Record the adopted behavior in an additive UI ADR.
9. Do not modify specifications.

## Done condition

- PRODUCT-ADR-UI-002 exists with `status: accepted`.
- The ADR depends on PRODUCT-ADR-UI-001 and PRODUCT-ADR-APPLICATION-005.
- Application failure meanings are not redefined.
- UI-owned retry, navigation, and state-disposal behavior is explicit.
- `Unavailable` remains outside technical-failure handling.
- Retry counts and implementation details remain unchanged or deferred.
- No specification changed.

## Verification

- Confirm PRODUCT-ADR-UI-002 uses the UI domain and required ADR sections.
- Confirm the ADR is additive and does not supersede PRODUCT-ADR-UI-001.
- Confirm retrieval mapping failure disposes the active queue and session before returning to main.
- Confirm queue-creation mapping and invalid-selection failures do not enter automatic retry.
- Confirm infrastructure failures retain the retry flow from PRODUCT-ADR-UI-001.
- Confirm diagnostic presentation uses only safe application-provided information.
- Confirm no transport or framework choice entered the decision.

## Evidence

- PRODUCT-ADR-UI-002 was created with `status: accepted`.
- PRODUCT-ADR-UI-002 depends on PRODUCT-ADR-UI-001 and PRODUCT-ADR-APPLICATION-005.
- PRODUCT-ADR-UI-002 adds category-specific behavior without replacing existing PWA state ownership.
- No specification changed in this task.
- Design Records MCP did not index the PRODUCT namespace, so filesystem fallback was used.
