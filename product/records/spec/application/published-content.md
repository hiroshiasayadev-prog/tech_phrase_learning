# Concept: Published content

- **id**: `spec:product.application.published_content`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.application`

## What this is

Runtime-facing projection of one published learning unit and its current selection availability.
The concept separates application reads from pipeline processing internals while allowing shared physical persistence.

## Non-goals

- Pipeline generation stages and processing-data schemas.
- Publication-gate criteria and validation implementation.
- Database tables, columns, indexes, and transaction syntax.
- Runtime revision history and rollback.
- Learner session state and loaded-content mutation.
- Concrete HTTP or serialization contracts.

## Concept model

```text
PublishedLearningUnitProjection
  +-- stable learning-unit identity
  +-- complete learning unit
  +-- current availability
  +-- opaque provenance reference
```

One physical database may contain both pipeline processing data and the published-content area.
The semantic projection remains independent from that physical layout.

| concept | meaning |
|---|---|
| Stable learning-unit identity | Identity used to replace and retrieve the current published projection. |
| Current content | One complete learning unit that follows the learning contract. |
| Availability | Mutable decision about inclusion in new learner flows. |
| Provenance reference | Opaque route to current pipeline source and generation evidence. |

## Rules

### Ownership

- The pipeline must own generation, validation, publication decisions, and published-area writes.
- The application must read only the published-content area.
- The application must not read pipeline processing data.
- One physical database may contain both semantic areas.
- Physical database sharing must not transfer pipeline-internal schema ownership to the application.

### Current content

- Stable learning-unit identity must remain anchored to one valid learning path.
- One stable learning-unit identity must identify at most one current published content projection.
- Current content must contain one complete learning unit.
- Learner-visible attribution remains part of that complete learning unit.
- The projection must not redefine attribution as an independent semantic element.
- Current content may be replaced after pipeline regeneration.
- Runtime revision history is not required for the first MVP.
- Historical generation artifacts are not required by the application boundary.

### Availability

- Availability must remain separate from current learning-unit content.
- Availability must be `available` or `unavailable` for runtime selection.
- Only available units may enter a newly created queue.
- Normal retrieval of an unavailable unit must return an unavailable result instead of its content.
- Unavailable content must retain the complete current learning unit and its provenance reference.
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
- Content, provenance reference, and publication-judged availability must switch atomically for a new publication.
- Resulting availability must come from the current publication judgment rather than implicit inheritance.
- A withdrawal that changes only availability remains a separate valid operation.
- An availability-only change must leave current content unchanged.
- An availability-only change must leave the provenance reference unchanged.

### Loaded content

Loaded-unit immutability and learner-flow replacement behavior are normatively owned by `spec:product.ui.learning_flow`.

### Provenance boundary

- The application must treat the provenance reference as opaque.
- The application must not interpret pipeline model, prompt, validation, or source-record details.
- Current pipeline-owned evidence must remain reachable from the provenance reference.
- The learner-visible attribution must not require traversal of pipeline processing data during normal unit retrieval.

## Boundary

| concern | owner |
|---|---|
| Learning-unit field meaning | `spec:product.learning.learning_unit` |
| Generation, publication decision, and current provenance evidence | `spec:product.pipeline` |
| Runtime projection and availability-aware reads | `spec:product.application` |
| Loaded-unit immutability and learner state | `spec:product.ui.learning_flow` |
| Physical schema and transaction implementation | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application` | Parent application overview. |
| `spec:product.application.learning_unit_selection` | Selects and retrieves current available publications. |
| `spec:product.learning.learning_unit` | Defines complete learner-visible content and attribution. |
| `spec:product.pipeline` | Produces the current publication and owns current provenance. |
| `spec:product.ui.learning_flow` | Treats a successfully loaded unit as immutable content. |
| PRODUCT-ADR-APPLICATION-001 | Establishes the published-content boundary. |
