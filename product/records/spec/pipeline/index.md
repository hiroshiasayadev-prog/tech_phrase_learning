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
| Deterministic processing | Use explicit rules for parsing, cleanup, path enumeration, validation, deduplication, and stable artifact identity. |
| LLM augmentation | Limit models to bounded tasks that require semantic interpretation. |
| Context size | Provide each model task with the smallest sufficient context. |
| Output trust | Treat model output as untrusted input and validate structured results. |
| Intermediate artifacts | Retain stage outputs for diagnosis and reprocessing. |
| Provider boundary | Use an internal boundary with an OpenAI-compatible chat-completion baseline. |
| Provider isolation | Keep vendor-specific SDKs, credentials, model names, and error translation inside adapters. |
| Compatibility meaning | Treat API compatibility as transport compatibility, not behavioral equivalence. |
| Initial corpus | Use public `discuss.python.org` Packaging topics for the first MVP. |
| Path production | Retain zero or more independently valid source-post paths per discussion. |
| Learning-unit production | Allow one valid path to produce zero or more learning units. |
| Summary production | Create reusable source-post summaries and grounded path-specific revisions when required. |
| Quiz production | Select one target phrase before generating one three-option quiz for each selected post. |
| Publication gate | Use automated publication gating under human-approved criteria. |
| Human review | Use human review for golden fixtures, policy development, evaluation, and selected exceptional cases. |
| Availability | Make passing units available and preserve evidence when a unit becomes unavailable. |

## Non-goals

- Target learner definition.
- Learning outcome and pedagogical rationale.
- Learner-visible phrase, summary, and card meaning.
- Runtime learning-unit selection and availability-aware retrieval.
- Selection of a permanent concrete model or provider.
- Complete cross-vendor support for every optional LLM feature.

## Rules

- Deterministic stages handle every task that does not require semantic judgment.
- LLM stages use explicit input and output contracts.
- Invalid model output is retried or rejected according to pipeline policy.
- Learning-domain logic must not call vendor SDKs directly.
- Logical model roles must remain separate from provider-specific model names.
- Provider capability differences require explicit handling.
- Source-specific fields must not become the source-independent domain model.
- The pipeline must not select one canonical path during ingestion.
- A path must be judged against learning suitability criteria without sibling ranking.
- Prefix-overlapping valid paths may coexist.
- Phrase selection and quiz generation must use separate bounded tasks.
- A learning unit must pass the automated publication gate before session availability.
- Routine publication must not require individual human approval.
- Humans must approve publication criteria and material changes to those criteria.
- Manual fixture review must not become a routine publication queue.
- Unavailability must preserve source references, evidence, attribution, provenance, and generation identities.

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
| PRODUCT-ADR-PIPELINE-001 | Establishes deterministic processing before LLM augmentation. |
| PRODUCT-ADR-PIPELINE-002 | Establishes the OpenAI-compatible provider boundary. |
| PRODUCT-ADR-PIPELINE-004 | Establishes path-based generation and automated publication gating. |
