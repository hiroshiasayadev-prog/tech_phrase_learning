# Contract: Learning-unit retrieval

- **id**: `spec:product.application.learning_unit_retrieval`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.application`
- **contract_class**: `interface`

## What this is

Semantic application use-case contract for retrieving one published learning unit by reference.
The use case coordinates the outbound retrieval query and returns an availability-shaped result.

## Non-goals

- Persistence query implementation.
- Published projection field exposure to application orchestration.
- Provenance return in the normal learner retrieval result.
- PWA skipping, retry timing, or loaded-content replacement.
- HTTP route, status code, JSON schema, class, method, or source directory.

## Request

| input | meaning |
|---|---|
| `LearningUnitRef` | Stable reference to one published learning unit. |

## Response

```text
Available(complete_learning_unit)
| Unavailable
```

| result | meaning |
|---|---|
| `Available(complete_learning_unit)` | Current state exists and remains available at retrieval time. |
| `Unavailable` | Current state is missing or current state exists but is unavailable. |

The complete learning unit must satisfy `spec:product.learning.learning_unit`.
The normal result must not include provenance, availability metadata, queue metadata, or pipeline processing data.

## Errors

| condition | handling |
|---|---|
| Persistence mapping failure | Technical failure outside `Available` and `Unavailable`. |
| Infrastructure failure | Technical failure outside `Available` and `Unavailable`. |

Concrete exception types and transport mappings remain deferred.

## Boundary

| concern | owner |
|---|---|
| Retrieval use-case orchestration | `spec:product.application.learning_unit_retrieval` |
| Current availability meaning | `spec:product.application.published_content.availability` |
| Current state read contract | `spec:product.application.outbound_queries.get_published_learning_unit` |
| Complete learning-unit semantics | `spec:product.learning.learning_unit` |
| PWA stale-reference skipping | `spec:product.ui.learning_flow` |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application` | Parent application overview. |
| `spec:product.application.published_content` | Defines the current state retrieved by this use case. |
| `spec:product.application.learning_unit_selection` | Creates references later supplied to retrieval. |
| `spec:product.application.outbound_queries.get_published_learning_unit` | Outbound query used by this use case. |
| `spec:product.learning.learning_unit` | Defines complete learner-visible content. |
| PRODUCT-ADR-APPLICATION-003 | Establishes retrieval availability results and provenance exclusion. |
| PRODUCT-ADR-APPLICATION-004 | Establishes the result-shaped outbound retrieval port. |
