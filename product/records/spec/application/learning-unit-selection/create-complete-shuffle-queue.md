# Contract: Create complete-shuffle queue

- **id**: `spec:product.application.learning_unit_selection.create_complete_shuffle_queue`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.application.learning_unit_selection`
- **contract_class**: `interface`

## What this is

Semantic application use-case contract for creating the first-MVP learning-unit reference queue.
The contract applies application policy and delegates reference selection to the outbound selection query.

## Non-goals

- Complete learning-unit content loading.
- Backend queue storage, identity, reservation, position, history, or learner progress.
- PWA queue consumption and retry behavior.
- Exact randomization algorithm or persistence query.
- HTTP route, status code, wire schema, class, method, or source directory.

## Request

The first-MVP PWA does not submit selection parameters.

| application policy | value |
|---|---|
| `selection_scope` | `All` |
| `maximum_count` | `100` |

## Response

The use case returns the accepted ordered `LearningUnitRef[]`.
The response does not include `eligible_count`, queue identity, reservation token, backend position, or queue history.

| condition | response |
|---|---|
| Zero eligible candidates | Empty ordered array. |
| One or more eligible candidates | Ordered array accepted by `spec:product.application.learning_unit_selection.result_validation`. |

## Errors

| condition | handling |
|---|---|
| Observable invalid returned array | Reject the complete result as an application failure. |
| Outbound selection technical failure | Propagate as a technical failure outside the normal queue result. |

Concrete error types and transport mappings remain deferred.

## Boundary

| concern | owner |
|---|---|
| First-MVP selection policy | `spec:product.application.learning_unit_selection.create_complete_shuffle_queue` |
| Selection scope meaning | `spec:product.application.learning_unit_selection.selection_scope` |
| Queue result invariants | `spec:product.application.learning_unit_selection.queue_contract` |
| Observable result validation | `spec:product.application.learning_unit_selection.result_validation` |
| Persistence-adapter selection guarantees | `spec:product.application.outbound_queries.select_learning_unit_refs` |
| PWA queue state | `spec:product.ui.learning_flow` |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application.learning_unit_selection` | Parent selection overview. |
| `spec:product.application.outbound_queries.select_learning_unit_refs` | Outbound query used by this use case. |
| `spec:product.application.published_content.availability` | Defines current availability used during selection. |
| PRODUCT-ADR-APPLICATION-003 | Establishes the first-MVP queue use case and no backend learner state. |
