# Reference: Selection result validation

- **id**: `spec:product.application.learning_unit_selection.result_validation`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.application.learning_unit_selection`

## What this is

Reference for application validation of the returned selection array.
The application validates only properties observable from the array.

## Current contract

| invariant | application validation | adapter contract verification |
|---|---|---|
| Result length does not exceed `maximum_count` | Required. | Required. |
| References are unique within the array | Required. | Required. |
| Every element is a valid `LearningUnitRef` | Required. | Required at persistence-to-domain mapping. |
| References were available during selection | Not independently observable. | Required. |
| References satisfy the requested scope | Not independently observable from reference identity alone. | Required. |
| Result has exact cardinality | Not independently observable without candidate-total information. | Required. |
| Ordering was randomized | Not provable from one returned array. | Required. |

## Rules

- Observable invalid results must be rejected as a complete result.
- Observable invalid results must not be normalized into a queue.
- The application must not query or receive `eligible_count` only to revalidate adapter behavior.
- The application must not infer underfill from an array shorter than `maximum_count`.

| returned array | handling |
|---|---|
| More than `maximum_count` references | Reject the complete result. |
| Duplicate references | Reject the complete result. |
| Malformed or invalid reference | Fail domain mapping or reject the complete result. |
| Empty array | Accept as a valid result. |
| Fewer than `maximum_count` references | Accept because underfill is not observable from the array alone. |

The application must not:

- truncate an over-limit array;
- remove duplicate references;
- discard malformed references and return a partial queue;
- retry only because fewer than `maximum_count` references were returned.

## Boundary

| concern | owner |
|---|---|
| Observable application validation | `spec:product.application.learning_unit_selection.result_validation` |
| Adapter-owned availability, scope, cardinality, and randomization verification | `spec:product.application.outbound_queries.select_learning_unit_refs` |
| Concrete error type and transport mapping | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application.learning_unit_selection` | Parent selection overview. |
| `spec:product.application.learning_unit_selection.queue_contract` | Defines queue result invariants. |
| `spec:product.application.outbound_queries.select_learning_unit_refs` | Defines adapter guarantees and technical failures. |
