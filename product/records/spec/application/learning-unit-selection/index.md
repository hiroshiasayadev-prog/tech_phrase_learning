# Overview: Learning-unit selection

- **id**: `spec:product.application.learning_unit_selection`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.application`

## What this is

Owner of application selection policy and queue-result validity.
The topic keeps selection separate from retrieval and from persistence-adapter query implementation.

## Current contract

| concern | contract |
|---|---|
| First-MVP use case | `CreateCompleteShuffleQueue` creates one ordered reference array. |
| Scope policy | The first MVP uses `SelectionScope = All`. |
| Maximum size | The first MVP uses `maximum_count = 100`. |
| Result shape | The accepted application result is ordered `LearningUnitRef[]`. |
| Content loading | Queue creation does not load complete learning-unit content. |
| Backend state | Queue creation creates no backend queue identity, position, history, or learner progress. |
| Retrieval separation | Complete learning-unit retrieval belongs to `spec:product.application.learning_unit_retrieval`. |

## Non-goals

- Learner history, recommendation ranking, and progress-aware selection.
- Topic, discussion, source, or difficulty controls in the first MVP.
- Backend queue identity, queue persistence, reservation, and queue history.
- Total eligible count in application or PWA results.
- Exact randomization, sampling, and database query algorithms.
- HTTP routes, status-code mappings, and wire schemas.
- PWA queue position, retry timing, and learner progression.

## Topics

| title | kind | ref | summary |
|---|---|---|---|
| Create complete-shuffle queue | Contract | `spec:product.application.learning_unit_selection.create_complete_shuffle_queue` | Application use case that applies first-MVP selection policy and returns selected refs. |
| Selection scope | Reference | `spec:product.application.learning_unit_selection.selection_scope` | `All`, future constrained scope, content constraints, and learner-history exclusion. |
| Queue contract | Reference | `spec:product.application.learning_unit_selection.queue_contract` | Cardinality, uniqueness, randomized order, zero candidates, and no backend queue state. |
| Result validation | Reference | `spec:product.application.learning_unit_selection.result_validation` | Application-observable validation and invalid returned-array handling. |

## Boundary

| concern | owner |
|---|---|
| Selection scope, queue cardinality, result validity, and application orchestration | `spec:product.application.learning_unit_selection` |
| Selection outbound query guarantees | `spec:product.application.outbound_queries.select_learning_unit_refs` |
| Current availability meaning and published runtime state | `spec:product.application.published_content` |
| Published learning-unit retrieval | `spec:product.application.learning_unit_retrieval` |
| PWA queue storage, position, exhaustion, retry, skipping, and progression | `spec:product.ui.learning_flow` |
| Database sampling, persistence, and transport mapping | Implementation adapters. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application` | Parent application overview. |
| `spec:product.application.published_content` | Defines current availability for selection eligibility. |
| `spec:product.application.learning_unit_retrieval` | Retrieves a selected reference when the PWA requests content. |
| `spec:product.application.outbound_queries.select_learning_unit_refs` | Provides the selection query required by the use case. |
| `spec:product.learning.learning_unit` | Defines the complete content intentionally not loaded by queue creation. |
| `spec:product.ui.learning_flow` | Owns returned queue state and progression. |
| PRODUCT-ADR-APPLICATION-003 | Establishes use cases, queue size, availability filtering, and no backend learner state. |
