# Overview: Tech Phrase Learning product specifications

- **id**: `spec:product`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `root`

## What this is

Placement router for Tech Phrase Learning PRODUCT specifications.
It separates learning semantics, content production, runtime application behavior, and learner-facing UI behavior.

## Current contract

| area | owns | must route elsewhere |
|---|---|---|
| `learning/` | Target learner, learning outcome, source-context model, phrase-exposure model, and learner-facing content semantics. | Source ingestion mechanics, processing stages, provider adapters, PWA state ownership, and operation feedback. |
| `pipeline/` | Source ingestion, conversation-tree normalization, filtering, candidate extraction, LLM augmentation, output validation, publication decisions, and published-content writes. | Learning goals, pedagogical meaning, runtime selection, PWA state, and session progress. |
| `application/` | Runtime learning-unit selection, availability-aware retrieval, application use cases, and outbound query ports. | Content generation, publication judgment, pipeline internals, PWA state, and concrete adapters. |
| `ui/` | PWA screen flow, transient learner-flow state, navigation, loading, and operation feedback. | Learning-content meaning, content generation, application selection policy, persistence, and provider integration. |

## Topics

| title | kind | ref | summary |
|---|---|---|---|
| Learning | Overview | `spec:product.learning` | Product concept and learner-facing phrase-exposure contract. |
| Content pipeline | Overview | `spec:product.pipeline` | Implementation contract for producing and publishing validated learning content. |
| Application | Overview | `spec:product.application` | Runtime selection, availability-aware retrieval, use cases, and outbound ports. |
| Learner UI | Overview | `spec:product.ui` | PWA screen flow and transient learner-flow state. |

## Placement rules

| question | route |
|---|---|
| Does the content define who learns, what they learn, or why conversation context matters? | Place it under `learning/`. |
| Does the content define the shape or meaning of a learner-visible learning item? | Place it under `learning/`. |
| Does the content define ingestion, parsing, normalization, filtering, extraction, generation, or validation? | Place it under `pipeline/`. |
| Does the content define an LLM request boundary, model role, or provider adapter? | Place it under `pipeline/`. |
| Does the content define runtime selection, availability-aware retrieval, application use cases, or outbound query ports? | Place it under `application/`. |
| Does the content define PWA screen flow, transient state, navigation, loading, or operation feedback? | Place it under `ui/`. |
| Does the content define deployment, persistence technology, or adapter implementation outside these boundaries? | Keep it in implementation records unless a separate semantic owner is established. |

Physical location is not ownership evidence.
Classify content by the contract it defines before choosing a path.

## Dependency direction

| dependency | rule |
|---|---|
| Pipeline to learning | Allowed. The pipeline may implement learning-domain requirements. |
| Learning to pipeline | No normative dependency. Learning semantics must remain valid when processing technology changes. |
| Learning to concrete LLM providers | Prohibited. Provider choice is a pipeline concern. |
| Pipeline to concrete providers | Allowed only through provider-specific adapters. |
| Application to learning | Allowed. The application serves complete learning units under learning contracts. |
| Application to pipeline internals | Prohibited. The application reads only the published-content boundary. |
| Pipeline to application published contract | Allowed. The pipeline writes the runtime projection defined at the boundary. |
| UI to application | Allowed through application interfaces. The UI does not own selection policy. |
| UI to learning | Allowed. The UI implements learner-visible semantics. |
| Learning to UI | No normative dependency. Learning semantics must remain valid when UI technology changes. |
| UI to pipeline internals | Prohibited. The UI consumes application interfaces instead. |

## Authoring boundary

- The root overview routes content and defines cross-area dependency direction.
- Child overviews own detailed contracts for their areas.
- Cross-area contracts remain references instead of copied text.
- New top-level areas require a distinct semantic owner.

## Related specs

| ref | relation |
|---|---|
| `spec:product.learning` | Learner-facing product contract. |
| `spec:product.pipeline` | Content-production and publication implementation contract. |
| `spec:product.application` | Runtime selection and published-content retrieval contract. |
| `spec:product.ui` | Learner-facing runtime and transient-state contract. |
| PRODUCT-ADR-LEARNING-001 | Establishes technical conversation trees as the primary learning source. |
| PRODUCT-ADR-PIPELINE-002 | Establishes the OpenAI-compatible provider boundary. |
| PRODUCT-ADR-PIPELINE-005 | Establishes staged path generation, publication gating, source reuse, and current-only retention. |
| PRODUCT-ADR-UI-001 | Establishes PWA ownership of transient learner-flow state. |
| PRODUCT-ADR-APPLICATION-001 | Establishes the published-content and runtime application boundary. |
