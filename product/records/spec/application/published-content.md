# Concept: Published content

- **id**: `spec:product.application.published_content`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.application`

## What this is

Runtime-facing projection of one published learning unit and its current selection availability.
The concept separates application reads from pipeline internal artifacts while allowing shared physical persistence.

## Non-goals

- Pipeline generation stages and intermediate artifact schemas.
- Publication-gate criteria and validation implementation.
- Database tables, columns, indexes, and transaction syntax.
- Runtime revision history and rollback.
- Learner session state and loaded-content mutation.
- Concrete HTTP or serialization contracts.

## Concept model

```text
One physical database
  +-- pipeline internal area
  |     +-- source snapshots
  |     +-- intermediate artifacts
  |     +-- validation evidence
  |
  +-- published content area
        +-- current learning-unit content
        +-- current availability
        +-- source attribution
        +-- opaque provenance reference
               ^
               |
          application reads
```

| concept | meaning |
|---|---|
| Stable learning-unit identity | Identity used to replace and retrieve the current published projection. |
| Current content | One complete learning unit that follows the learning contract. |
| Availability | Mutable decision about inclusion in new learner flows. |
| Source attribution | Learner-visible source identification required by the learning contract. |
| Provenance reference | Opaque route to pipeline-owned source and generation evidence. |

## Rules

### Ownership

- The pipeline must own generation, validation, publication decisions, and published-area writes.
- The application must read only the published-content area.
- The application must not read pipeline intermediate artifacts.
- One physical database may contain both semantic areas.
- Physical database sharing must not transfer pipeline-internal schema ownership to the application.

### Current content

- One stable learning-unit identity must identify at most one current published content projection.
- Current content must contain one complete learning unit.
- Current content may be replaced after pipeline regeneration.
- Runtime revision history is not required for the first MVP.
- Pipeline internal evidence must remain the diagnostic source for older generation artifacts.

### Availability

- Availability must remain separate from current learning-unit content.
- Availability must be `available` or `unavailable` for runtime selection.
- Only available units may enter a newly created queue.
- Unavailable content must retain source attribution and its provenance reference.
- Withdrawal may change availability without deleting current content.
- A later publication decision may make the same stable identity available again.

### Atomic replacement

The pipeline must publish replacement content as one observable state transition.

| observable state | content | provenance reference | availability |
|---|---|---|---|
| Before switch | Previous complete content | Previous reference | Previous state |
| After switch | New complete content | New reference | Resulting state |
| Prohibited intermediate | Mixed or partial content | Mismatched reference | Any state |

- The application must observe either the complete previous publication or the complete new publication.
- The application must not observe partially replaced content.
- Content, provenance reference, and resulting availability must switch atomically for a new publication.
- A withdrawal that changes only availability remains a separate valid operation.

### Loaded content

- Content loaded into the PWA must remain immutable for that learner flow.
- A later replacement of current published content must not mutate the loaded copy.
- A later withdrawal must not force the PWA to terminate a unit already loaded successfully.

### Provenance boundary

- The application must treat the provenance reference as opaque.
- The application must not interpret pipeline model, prompt, validation, or source-snapshot identities.
- Pipeline-owned evidence must remain reachable from the provenance reference.
- The learner-visible attribution must not require traversal of pipeline internal artifacts during normal unit retrieval.

## Boundary

| concern | owner |
|---|---|
| Learning-unit field meaning | `spec:product.learning.learning_unit` |
| Generation, publication decision, and provenance evidence | `spec:product.pipeline` |
| Runtime projection and availability-aware reads | `spec:product.application` |
| Loaded-unit immutability and learner state | `spec:product.ui.learning_flow` |
| Physical schema and transaction implementation | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application` | Parent application overview. |
| `spec:product.application.learning_unit_selection` | Selects and retrieves current available publications. |
| `spec:product.learning.learning_unit` | Defines complete learner-visible content and attribution. |
| `spec:product.pipeline` | Produces the current publication and owns detailed provenance. |
| `spec:product.ui.learning_flow` | Treats a successfully loaded unit as immutable content. |
| PRODUCT-ADR-APPLICATION-001 | Establishes the published-content boundary. |
