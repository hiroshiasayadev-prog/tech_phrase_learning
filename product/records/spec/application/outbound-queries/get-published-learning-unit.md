# Contract: Get published learning unit

- **id**: `spec:product.application.outbound_queries.get_published_learning_unit`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.application.outbound_queries`
- **contract_class**: `interface`

## What this is

Outbound query contract for retrieving one published learning unit by stable reference.
The persistence adapter maps committed published state into the application-owned retrieval result.

## Non-goals

- Retrieval use-case orchestration.
- PWA stale-reference skipping or retry behavior.
- Published projection exposure to application code.
- SQL, schema, ORM, query library, database product, transaction configuration, or source layout.
- HTTP route, status code, JSON schema, or concrete exception class.
- Concrete test database, container, fixture, or framework.

## Request

| input | meaning |
|---|---|
| `LearningUnitRef` | Stable reference to one published learning unit. |

## Response

```text
Available(complete_learning_unit)
| Unavailable
```

| condition | normal result |
|---|---|
| Current state exists and is available | `Available(complete_learning_unit)` |
| No current state exists | `Unavailable` |
| Current state exists but is unavailable | `Unavailable` |

The complete learning unit must satisfy `spec:product.learning.learning_unit`.
The normal result must not return provenance.

## Errors

| condition | handling |
|---|---|
| Complete learning-unit mapping failure | Technical failure outside `Available` and `Unavailable`. |
| Infrastructure failure | Technical failure outside `Available` and `Unavailable`. |

Mapping failure and infrastructure failure must not become `Available` or `Unavailable`.

## Adapter guarantees

- Read the committed current published state for the supplied reference.
- Read the committed availability value.
- Return `Available(complete_learning_unit)` only when current content exists and is currently available.
- Return `Unavailable` when no current state exists for the reference.
- Return `Unavailable` when current content exists but is unavailable.
- Map persisted complete content into the learning-unit contract.
- Keep provenance inside the published-content and pipeline boundary.
- Propagate mapping and infrastructure failures as technical failures.
- Avoid deciding whether a learning unit should be available.

## Contract-test coverage

Persistence-adapter contract tests must cover:

- available current content;
- missing current content;
- unavailable current content;
- complete learning-unit mapping;
- provenance exclusion;
- mapping failure;
- infrastructure failure.

## Boundary

| concern | owner |
|---|---|
| Retrieval adapter guarantees | `spec:product.application.outbound_queries.get_published_learning_unit` |
| Retrieval use-case orchestration | `spec:product.application.learning_unit_retrieval` |
| Current state and availability | `spec:product.application.published_content` |
| Complete learning-unit semantics | `spec:product.learning.learning_unit` |
| Availability decisions and published-content writes | `spec:product.pipeline` |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application.outbound_queries` | Parent outbound-query overview. |
| `spec:product.application.learning_unit_retrieval` | Application use case that calls this query. |
| `spec:product.application.published_content.current_state` | Defines committed state read by this query. |
| `spec:product.application.published_content.availability` | Defines current availability mapped by this query. |
| `spec:product.learning.learning_unit` | Defines complete content returned in `Available`. |
| PRODUCT-ADR-APPLICATION-003 | Establishes availability-shaped retrieval and provenance exclusion. |
| PRODUCT-ADR-APPLICATION-004 | Establishes the result-shaped outbound retrieval port and adapter obligations. |
