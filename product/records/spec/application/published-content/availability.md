# Reference: Published availability

- **id**: `spec:product.application.published_content.availability`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.application.published_content`

## What this is

Reference for the runtime availability value used by application selection and retrieval.
Availability expresses eligibility for new learner flows without deleting current content.

## Current contract

| value | meaning |
|---|---|
| `available` | The current published unit may enter new queues and may be retrieved for a new learner flow. |
| `unavailable` | The current published unit must not enter new queues and must retrieve as `Unavailable`. |

## Rules

- Only `available` units may enter a newly created queue.
- Retrieval must recheck current availability for the supplied `LearningUnitRef`.
- Missing current state must retrieve as `Unavailable`.
- Unavailable current state must retrieve as `Unavailable`.
- `Unavailable` is a normal result, not a mapping failure or infrastructure failure.
- Withdrawal must change availability without deleting current content.
- Unavailable content must retain source references, source evidence, attribution, and the opaque provenance reference.
- A later publication decision may make the same stable identity available again.
- Availability remains separate from the complete learning-unit content.

## Boundary

| concern | owner |
|---|---|
| Availability decision | `spec:product.pipeline` |
| Availability value read by application use cases | `spec:product.application.published_content.availability` |
| Selection eligibility | `spec:product.application.learning_unit_selection` |
| Retrieval result mapping | `spec:product.application.learning_unit_retrieval` |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application.published_content` | Parent published-content overview. |
| `spec:product.application.learning_unit_selection` | Uses availability for queue eligibility. |
| `spec:product.application.learning_unit_retrieval` | Uses availability for `Available` and `Unavailable` results. |
| `spec:product.application.outbound_queries.get_published_learning_unit` | Reads committed availability through the persistence adapter. |
| `spec:product.pipeline` | Owns availability decisions and writes. |
| PRODUCT-ADR-APPLICATION-003 | Establishes current availability and retrieval result names. |
| PRODUCT-ADR-APPLICATION-004 | Establishes result-shaped retrieval-port mapping. |
