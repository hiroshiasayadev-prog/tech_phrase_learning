# Reference: Queue contract

- **id**: `spec:product.application.learning_unit_selection.queue_contract`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.application.learning_unit_selection`

## What this is

Reference for the selected reference-array invariants returned by queue creation.
The contract defines application-visible queue contents without creating backend queue state.

## Current contract

```text
queue_size = min(maximum_count, eligible_count)
```

| eligible count | required result size |
|---|---|
| `0` | `0`; an empty queue is valid. |
| `1..99` | Exactly `eligible_count`. |
| `100 or more` | Exactly `100`. |

## Rules

- `maximum_count` is application policy.
- The first-MVP `maximum_count` is `100`.
- `eligible_count` is the number of unique candidates satisfying current availability and requested scope during selection.
- `eligible_count` defines adapter cardinality.
- The application and PWA must not receive `eligible_count`.
- One queue result must contain stable `LearningUnitRef` values only.
- One queue result must contain no duplicate reference.
- Uniqueness applies only within one result.
- A later queue may repeat references from an earlier queue.
- Returned order must be randomized by the selection implementation.
- The application must preserve the accepted returned order.
- Queue issuance must create no learner-specific reservation.
- The backend must retain no queue identity, position, history, or learner progress.
- Exact randomization algorithms and statistical distribution guarantees remain implementation details.

## Boundary

| concern | owner |
|---|---|
| Application-visible queue result invariants | `spec:product.application.learning_unit_selection.queue_contract` |
| Adapter-owned selection guarantees | `spec:product.application.outbound_queries.select_learning_unit_refs` |
| PWA queue storage and progression | `spec:product.ui.learning_flow` |
| Randomization algorithm and persistence strategy | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application.learning_unit_selection` | Parent selection overview. |
| `spec:product.application.learning_unit_selection.result_validation` | Defines what the application can validate from the returned array. |
| `spec:product.application.outbound_queries.select_learning_unit_refs` | Guarantees adapter-owned cardinality and ordering properties. |
| PRODUCT-ADR-APPLICATION-003 | Establishes maximum queue size and no backend learner state. |
