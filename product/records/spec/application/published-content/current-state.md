# Concept: Published current state

- **id**: `spec:product.application.published_content.current_state`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.application.published_content`

## What this is

Concept model for the committed runtime state of one published learning unit.
The concept defines what application reads may observe, not how persistence stores the state.

## Non-goals

- Pipeline validation procedure.
- Publication judgment procedure.
- Writer implementation.
- Database schema, transaction syntax, or isolation level.
- Runtime revision, rollback, or historical publication model.

## Concept model

```text
CurrentPublishedState
  +-- stable learning-unit identity
  +-- complete learning unit
  +-- current availability
  +-- opaque provenance reference
```

| concept | meaning |
|---|---|
| Stable learning-unit identity | Identity anchored to one valid learning path. |
| Complete learning unit | Learner-visible unit satisfying `spec:product.learning.learning_unit`. |
| Current availability | Current eligibility for new learner flows. |
| Opaque provenance reference | Pipeline-owned route to current source and generation evidence. |

## Rules

- One stable learning-unit identity must identify at most one current published state.
- Current content must contain one complete learning unit.
- Learner-visible attribution remains part of the complete learning unit.
- The current state must retain one matching opaque provenance reference.
- The application must treat the provenance reference as opaque.
- The application must read only committed current published state.
- The application must not observe incomplete or partially replaced state.
- The application must not read pipeline processing data.
- Runtime revision history is not required for the first MVP.
- Revision identities, revision tokens, previous publications, and rollback state are not runtime contract elements.

## Boundary

| concern | owner |
|---|---|
| Complete learning-unit semantics | `spec:product.learning.learning_unit` |
| Current publication evidence | `spec:product.pipeline` |
| Committed runtime state visible to application reads | `spec:product.application.published_content.current_state` |
| Physical storage and transaction mechanics | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application.published_content` | Parent published-content overview. |
| `spec:product.application.published_content.availability` | Defines the availability value in current state. |
| `spec:product.application.published_content.publication_handoff` | Defines the application-side handoff meaning for replacing current state. |
| `spec:product.learning.learning_unit` | Defines complete learner-visible content. |
| `spec:product.pipeline` | Owns current provenance evidence and publication decisions. |
| PRODUCT-ADR-APPLICATION-003 | Establishes the current published-content boundary. |
