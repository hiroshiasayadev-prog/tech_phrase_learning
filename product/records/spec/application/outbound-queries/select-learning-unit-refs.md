# Contract: Select learning-unit refs

- **id**: `spec:product.application.outbound_queries.select_learning_unit_refs`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.application.outbound_queries`
- **contract_class**: `interface`

## What this is

Outbound query contract for selecting stable references to currently available learning units.
The contract defines persistence-adapter obligations without restating application use-case policy.

## Non-goals

- PWA queue state or learner progression.
- Complete learning-unit content loading.
- Exact randomization algorithm, sampling strategy, query, schema, index, or transaction configuration.
- Database product, ORM, query library, connection pool, or source layout.
- Concrete test database, container, fixture, or framework.

## Request

| input | meaning |
|---|---|
| `selection_scope` | Content constraint supplied by the application use case. |
| `maximum_count` | Upper bound supplied by the application use case. |

## Response

The normal result is ordered `LearningUnitRef[]`.
An empty array is a normal result when zero candidates are eligible.

The result must not include:

- `eligible_count`;
- queue identity;
- reservation token;
- backend position;
- queue history;
- complete learning-unit content.

## Errors

| condition | handling |
|---|---|
| Persistence-to-domain mapping failure | Technical failure outside the normal ordered array result. |
| Infrastructure failure | Technical failure outside the normal ordered array result. |

Technical failures must not be converted into an empty queue or normalized partial result.

## Adapter guarantees

- Select only references currently available during the operation.
- Select only references satisfying `selection_scope`.
- Return exactly `min(maximum_count, eligible_count)` references.
- Return unique stable `LearningUnitRef` values.
- Return references in randomized order.
- Preserve the returned order.
- Retain no learner-specific queue state.
- Allow bounded selection inside persistence without loading the complete candidate set into application memory.

## Contract-test coverage

Persistence-adapter contract tests must cover:

- zero candidates;
- below-limit candidates;
- exact-limit candidates;
- above-limit candidates;
- unavailable candidates;
- scope filtering;
- exact cardinality;
- uniqueness;
- stable-reference mapping;
- randomized order;
- mapping failure;
- infrastructure failure.

Random-selection tests must verify randomized selection rather than fixed repository order.
The contract defines no statistical distribution threshold.

## Boundary

| concern | owner |
|---|---|
| Adapter selection guarantees | `spec:product.application.outbound_queries.select_learning_unit_refs` |
| Selection scope | `spec:product.application.learning_unit_selection.selection_scope` |
| Queue result invariants | `spec:product.application.learning_unit_selection.queue_contract` |
| Observable application validation | `spec:product.application.learning_unit_selection.result_validation` |
| Current availability | `spec:product.application.published_content.availability` |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application.outbound_queries` | Parent outbound-query overview. |
| `spec:product.application.learning_unit_selection.create_complete_shuffle_queue` | Application use case that calls this query. |
| `spec:product.application.published_content.availability` | Defines current availability filtering. |
