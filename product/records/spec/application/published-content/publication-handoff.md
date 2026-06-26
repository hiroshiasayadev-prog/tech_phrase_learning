# Reference: Publication handoff input

- **id**: `spec:product.application.published_content.publication_handoff`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.application.published_content`

## What this is

Application-side meaning of pipeline handoff inputs that replace current published state or change availability.
This reference does not define pipeline validation procedure, writer implementation, or transaction mechanics.

## Current contract

| handoff | application-visible effect |
|---|---|
| `PublicationHandoff` | Replaces the complete current state for one stable identity. |
| `AvailabilityChange` | Changes only the availability of an existing current state. |

## Rules

- `PublicationHandoff` must include stable learning-unit identity, complete learning unit, opaque provenance reference, and resulting availability.
- `PublicationHandoff` must replace content, matching provenance, and availability together.
- `AvailabilityChange` must include stable learning-unit identity and resulting availability.
- `AvailabilityChange` must not change current content.
- `AvailabilityChange` must not change the current provenance reference.
- A failed published-content change must leave the previous committed current state visible to application reads.
- The application-side contract assumes the pipeline validated the complete state before mutation.
- The application-side contract assumes the pipeline owns the publication or availability decision.
- Publication handoff operations do not define commands, events, request bodies, or storage schemas.

## Boundary

| concern | owner |
|---|---|
| Handoff input meaning visible to application reads | `spec:product.application.published_content.publication_handoff` |
| Validation procedure and publication judgment | `spec:product.pipeline` |
| Writer implementation and mutation preconditions | `spec:product.pipeline` |
| Transaction execution and persistence technology | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application.published_content` | Parent published-content overview. |
| `spec:product.application.published_content.current_state` | Defines the committed state affected by handoffs. |
| `spec:product.application.published_content.availability` | Defines availability changed by handoffs. |
| `spec:product.pipeline` | Owns publication decisions and published-content writes. |
| PRODUCT-ADR-APPLICATION-003 | Establishes transactional current-state publication. |
