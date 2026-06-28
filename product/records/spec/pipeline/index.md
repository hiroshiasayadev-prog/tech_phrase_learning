# Overview: Content pipeline

- **id**: `spec:product.pipeline`
- **status**: draft
- **date**: 2026-06-28
- **parent**: `spec:product`

## What this is

Owner of source processing, generated-content validation, publication decisions, and published-content writes.
The Pipeline implements Learning contracts while keeping processing internals outside Application runtime reads.

## Current contract

| concern | contract |
|---|---|
| Source boundary | Source Adapters discover, fetch, and normalize source-specific discussions before source-independent Common Pipeline processing. |
| Processing boundary | Deterministic stages own mechanically observable checks; bounded model stages own semantic interpretation and generation. |
| Accepted progression | A downstream stage consumes only declared accepted upstream results. |
| Artifact model | The first MVP retains current reusable and publication-relevant artifacts without requiring historical generations or exact replay. |
| Learning boundary | Pipeline produces complete Learning Units under Learning-owned path, content, attribution, and readiness semantics. |
| Publication boundary | Pipeline owns gate decisions and atomic writes to the Application-owned current published-content boundary. |
| Runtime opacity | Application and UI must not inspect Pipeline validation, retry, component, version, or provenance internals. |

## Non-goals

- Learner, Learning Path, Learning Unit, phrase, option, session, or publication-readiness meaning.
- Runtime queue selection, availability-aware retrieval, or `LearningUnitRef` semantics.
- PWA state, navigation, retry presentation, or learner-flow behavior.
- Programming language, framework, workflow engine, queue, scheduler, worker topology, or concurrency model.
- Database, ORM, SQL, transport, route, serialization, deployment, or persistence technology.
- Concrete model, provider deployment, prompt text, retry count, timing, or backoff algorithm.

## Topics

| title | kind | ref | summary |
|---|---|---|---|
| Source acquisition | Concept | `spec:product.pipeline.source_acquisition` | Adapter-led discovery, canonical URL handling, retained lookup, fetch-or-reuse, and acquisition outcomes. |
| Source normalization | Concept | `spec:product.pipeline.source_normalization` | Source-independent authentic conversations, authored-text separation, relationship evidence, and Discussion Paths. |
| Path enumeration | Concept | `spec:product.pipeline.path_enumeration` | Bounded candidate derivation, source-grounded identity, deterministic order, duplicate merging, and origin evidence. |
| Path validation | Concept | `spec:product.pipeline.path_validation` | Structural checks, independent semantic suitability units, coverage, rejection, and retained valid paths. |
| Content generation | Concept | `spec:product.pipeline.content_generation` | Reusable summaries, phrase evidence, path-specific summaries, target phrases, prompts, and options. |
| Validation | Concept | `spec:product.pipeline.validation` | Deterministic checks, semantic evaluations, controlled outcomes, interaction completion, and content-validation completion. |
| Artifact identity and provenance | Concept | `spec:product.pipeline.artifact_identity_and_provenance` | Source-grounded identity, current-only artifacts, reusable scopes, behavior evidence, and opaque provenance. |
| LLM provider boundary | Concept | `spec:product.pipeline.llm_provider` | Provider-neutral invocation, OpenAI-compatible baseline, adapter isolation, capabilities, and untrusted output. |
| Publication | Concept | `spec:product.pipeline.publication` | Gate authorization, unattended eligibility, outcomes, atomic handoff, and availability-only mutation. |
| Orchestration | Concept | `spec:product.pipeline.orchestration` | Stage progression, retry, rerun, reuse, continuation, terminal outcomes, and current-run diagnostics. |

## Rules

- Pipeline specifications must reference Learning-owned meanings instead of redefining them.
- Pipeline specifications must reference Application published-content semantics instead of redefining runtime reads.
- Source-specific listing, URL, API, HTML, and reply-field representation must remain outside Common Pipeline semantics.
- Model output must remain untrusted until deterministic and required semantic validation complete.
- A valid rejection must remain distinct from provider failure, invalid output, incomplete processing, and contradiction.
- Generated-content changes must not create a sibling Learning Unit when source-grounded identity remains unchanged.
- Pipeline writes must preserve one complete committed current state for Application readers.

## Boundary

| concern | owner |
|---|---|
| Learning Path validity and learner-visible content meaning | `spec:product.learning`. |
| Source acquisition, normalization, generation, validation, publication, and orchestration | `spec:product.pipeline`. |
| Committed current state, availability-aware selection, and retrieval | `spec:product.application`. |
| Learner-facing runtime state and presentation | `spec:product.ui`. |
| Concrete implementation technology | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product` | PRODUCT placement router and dependency direction. |
| `spec:product.learning.learning_path` | Defines Learning Path meaning and suitability. |
| `spec:product.learning.learning_unit` | Defines complete learner-visible content and publication readiness. |
| `spec:product.learning.quiz_session` | Defines ordered interaction materialization obligations. |
| `spec:product.application.published_content` | Defines committed current state read by Application. |
| PRODUCT-ADR-PIPELINE-002 | Establishes the internal OpenAI-compatible provider boundary. |
| PRODUCT-ADR-PIPELINE-005 | Establishes staged processing and current-only retention. |
