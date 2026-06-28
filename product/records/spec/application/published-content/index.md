# Overview: Published content

- **id**: `spec:product.application.published_content`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.application`

## What this is

Owner of the runtime-facing published state read by application use cases.
The topic separates current application reads from pipeline processing internals while allowing shared physical persistence.

## Current contract

| concern | contract |
|---|---|
| Current state | One stable learning-unit identity has at most one committed current state. |
| Content | Current state contains one complete learning unit under `spec:product.learning.learning_unit`. |
| Availability | Current state records whether the unit is available to new learner flows. |
| Provenance | Current state retains one opaque provenance reference for pipeline-owned evidence. |
| Application reads | The application reads only committed current published state. |
| Pipeline writes | The pipeline owns publication decisions and published-content mutation. |
| Partial state | The application must not observe incomplete or partially replaced current state. |

## Non-goals

- Pipeline generation stages and processing-data schemas.
- Publication-gate criteria and validation implementation.
- Database tables, columns, indexes, and transaction syntax.
- Runtime revision history and rollback.
- Learner session state and loaded-content mutation.
- Concrete HTTP or serialization contracts.

## Topics

| title | kind | ref | summary |
|---|---|---|---|
| Current state | Concept | `spec:product.application.published_content.current_state` | Stable identity, complete learning unit, opaque provenance, committed visibility, and no runtime revision model. |
| Availability | Reference | `spec:product.application.published_content.availability` | `available` and `unavailable` meanings for selection and retrieval. |
| Publication handoff | Reference | `spec:product.application.published_content.publication_handoff` | Application-side meaning of pipeline publication and availability-change handoff inputs. |

## Boundary

| concern | owner |
|---|---|
| Learning-unit field meaning | `spec:product.learning.learning_unit` |
| Generation and validation | `spec:product.pipeline.content_generation` and `spec:product.pipeline.validation` |
| Publication decision and current provenance evidence | `spec:product.pipeline.publication` and `spec:product.pipeline.artifact_identity_and_provenance` |
| Runtime projection and availability-aware reads | `spec:product.application.published_content` |
| Loaded-unit immutability and learner state | `spec:product.ui.learning_flow` |
| Physical schema and transaction implementation | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application` | Parent application overview. |
| `spec:product.application.learning_unit_selection` | Selects currently available published content by reference. |
| `spec:product.application.learning_unit_retrieval` | Retrieves one current published unit through application orchestration. |
| `spec:product.application.outbound_queries.get_published_learning_unit` | Defines the persistence-adapter read contract for one published unit. |
| `spec:product.learning.learning_unit` | Defines complete learner-visible content and attribution. |
| `spec:product.pipeline.publication` | Owns publication decisions and current-state writes. |
| `spec:product.pipeline.artifact_identity_and_provenance` | Owns current Pipeline provenance and the opaque reference. |
| PRODUCT-ADR-APPLICATION-003 | Establishes the current published-content and retrieval boundary. |
