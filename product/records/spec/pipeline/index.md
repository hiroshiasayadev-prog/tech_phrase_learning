# Overview: Content pipeline

- **id**: `spec:product.pipeline`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product`

## What this is

Owner of implementation contracts for producing validated learning content from technical conversations.
The area implements learning-domain needs without owning their pedagogical meaning.

## Current contract

| concern | contract |
|---|---|
| Source structure | Preserve authentic posts and conversation relationships during ingestion and normalization. |
| Source reuse | Reuse retained source data for a previously fetched source URL. Periodic refetch and freshness guarantees are not required. |
| Deterministic processing | Use explicit rules for parsing, cleanup, path enumeration, validation, deduplication, and stable artifact identity. |
| LLM augmentation | Limit models to bounded tasks that require semantic interpretation. |
| Context size | Provide each model task with the smallest sufficient context. |
| Output trust | Treat model output as untrusted input and validate structured results. |
| Working artifacts | Keep only current or transient stage data needed for processing. Historical intermediate generations are not required. |
| Provider boundary | Use an internal boundary with an OpenAI-compatible chat-completion baseline. |
| Provider isolation | Keep vendor-specific SDKs, credentials, model names, and error translation inside adapters. |
| Compatibility meaning | Treat API compatibility as transport compatibility, not behavioral equivalence. |
| Initial corpus | Use public `discuss.python.org` Packaging topics for the first MVP. |
| Path production | Retain zero or more independently valid source-post paths per discussion. |
| Learning-unit production | Treat each valid path as exactly one logical learning unit. |
| Summary production | Create reusable source-post summaries and grounded path-specific revisions when required. |
| Quiz production | Select one target phrase before generating one three-option quiz for each selected post. |
| Publication gate | Use automated publication gating under human-approved criteria. |
| Human review | Use human review for golden fixtures, policy development, evaluation, and selected exceptional cases. |
| Availability | Make passing units available and preserve current publication data when a unit becomes unavailable. |

## Non-goals

- Target learner definition.
- Learning outcome and pedagogical rationale.
- Learner-visible phrase, summary, and card meaning.
- Runtime learning-unit selection and availability-aware retrieval.
- Selection of a permanent concrete model or provider.
- Complete cross-vendor support for every optional LLM feature.
- Source freshness, periodic synchronization, and historical source reconstruction.
- Historical intermediate generations, exact replay, and rollback.

## Rules

- Deterministic stages handle every task that does not require semantic judgment.
- LLM stages use explicit input and output contracts.
- Invalid model output is retried or rejected according to pipeline policy.
- Learning-domain logic must not call vendor SDKs directly.
- Logical model roles must remain separate from provider-specific model names.
- Provider capability differences require explicit handling.
- Source-specific fields must not become the source-independent domain model.
- A successful source fetch may establish retained source data for its source URL.
- The pipeline may reuse retained source data for the same URL without another network request.
- Intermediate stage data may be transient or overwritten after downstream use.
- The first MVP does not require historical source or intermediate generations.
- The pipeline must not select one canonical path during ingestion.
- A path must be judged against learning suitability criteria without sibling ranking.
- Prefix-overlapping valid paths may coexist.
- Regeneration must replace current generated content for the same logical learning unit.
- Phrase selection and quiz generation must use separate bounded tasks.
- A learning unit must pass the automated publication gate before session availability.
- Routine publication must not require individual human approval.
- Humans must approve publication criteria and material changes to those criteria.
- Manual fixture review must not become a routine publication queue.
- Unavailability must preserve current content, source references, attribution, and current publication provenance.
- Publication availability must not change valid-path to learning-unit cardinality.

## Publication handoff

```text
PublicationHandoff
  +-- stable learning-unit identity
  +-- complete learning unit
  +-- opaque provenance reference
  +-- resulting availability
```

```text
AvailabilityChange
  +-- stable learning-unit identity
  +-- resulting availability
```

- Both operations are semantic and do not define a command, event, request body, or storage schema.
- `PublicationHandoff` introduces or replaces content and provenance under one stable learning-unit identity.
- `AvailabilityChange` changes only the availability of an existing published projection.
- Stable learning-unit identity must remain anchored to one valid learning path.
- The complete learning unit in a `PublicationHandoff` must satisfy `spec:product.learning.learning_unit`.
- Learner-visible attribution remains inside the complete learning unit.
- The opaque provenance reference in a `PublicationHandoff` must identify current pipeline-owned source and generation evidence.
- Resulting availability must be the explicit outcome of a pipeline-owned decision for both operation types.

Before initial publication or content replacement (`PublicationHandoff`):

- the learning unit must be complete and structurally valid;
- required source references and attribution must be present;
- required mechanical validation must be complete;
- required model-based quality judgment must be complete;
- current provenance must be established;
- one publication judgment must determine resulting availability.

Before an availability-only change (`AvailabilityChange`):

- one current published projection must exist for the stable learning-unit identity;
- a pipeline-owned decision must determine the resulting availability.

Writer obligations:

- The pipeline is the only semantic owner of published-content writes.
- Initial publication must write one complete projection.
- Replacement under one stable identity must switch content, matching provenance, and publication-judged availability together.
- Replacement must not create another current projection or sibling learning unit.
- Republication that introduces new or changed content must use `PublicationHandoff` and satisfy its preconditions.
- Republication that restores availability without changing content must use `AvailabilityChange` and must not alter the current content or current provenance reference.
- An availability-only change must leave current content unchanged.
- An availability-only change must leave the current provenance reference unchanged.
- An availability-only change must produce one observable state transition from the prior availability.
- Failed preconditions must not produce partial published-content mutation for either operation type.
- Each `PublicationHandoff` must commit all fields of the complete published state in one transaction.
- Each `AvailabilityChange` must commit the availability change in one transaction.
- A failed transaction must leave the existing committed current published state unchanged. See `spec:product.application.published_content` for the current-state contract.
- Transaction syntax, isolation level, and persistence technology remain implementation details.
- The first MVP does not require historical source snapshots, intermediate generations, previous publications, exact replay, or rollback state.

## Boundary

| content | owner |
|---|---|
| Learning goals and learner-visible semantics | `spec:product.learning`. |
| Learning-path meaning and suitability | `spec:product.learning.learning_path`. |
| Learning-unit field meaning | `spec:product.learning.learning_unit`. |
| Source ingestion and conversation normalization | `spec:product.pipeline`. |
| Path enumeration, validation, and filtering | `spec:product.pipeline`. |
| Summary, phrase, and quiz generation mechanics | `spec:product.pipeline`. |
| Publication-gate implementation | `spec:product.pipeline`. |
| Concrete provider adaptation | `spec:product.pipeline`. |
| Runtime learning-unit selection and availability-aware retrieval | `spec:product.application`. |

## Topic map

No child pipeline specifications are established yet.
This overview owns the current pipeline-domain contract.

## Related specs

| ref | relation |
|---|---|
| `spec:product` | PRODUCT placement router and dependency direction. |
| `spec:product.learning` | Learning contract implemented by the pipeline. |
| `spec:product.learning.learning_path` | Defines valid source-post path semantics. |
| `spec:product.learning.learning_unit` | Defines the learner-visible unit produced by the pipeline. |
| `spec:product.application.published_content` | Defines the runtime projection written after publication decisions. |
| PRODUCT-ADR-PIPELINE-002 | Establishes the OpenAI-compatible provider boundary. |
| PRODUCT-ADR-PIPELINE-005 | Establishes staged path generation, automated publication gating, source reuse, and current-only retention. |
