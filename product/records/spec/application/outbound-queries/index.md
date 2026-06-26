# Overview: Outbound queries

- **id**: `spec:product.application.outbound_queries`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.application`

## What this is

Owner of application-required read capabilities implemented by persistence adapters.
The topic keeps adapter obligations separate from application use-case policy and persistence implementation details.

## Current contract

| concern | contract |
|---|---|
| Dependency direction | Persistence adapters depend on application outbound-query contracts. |
| Normal results | Normal results are semantic application results, not persistence projections. |
| Technical failures | Mapping and infrastructure failures remain outside normal results. |
| Application tests | Application tests may use test doubles at the outbound-query boundary. |
| Contract tests | Persistence-adapter contract tests exercise the real adapter boundary. |
| Implementation leakage | Persistence, framework, and transport types must not enter application contracts. |

## Non-goals

- SQL, tables, columns, indexes, query plans, or schemas.
- ORM, query library, database product, or connection pool.
- Exact randomization or sampling algorithm.
- Transaction configuration or isolation level.
- Programming-language interface, class, method, or source directory.
- HTTP route, status code, JSON schema, or retry timing.
- Concrete test database, container, fixture, or framework.

## Topics

| title | kind | ref | summary |
|---|---|---|---|
| Select learning-unit refs | Contract | `spec:product.application.outbound_queries.select_learning_unit_refs` | Bounded randomized selection of stable published learning-unit references. |
| Get published learning unit | Contract | `spec:product.application.outbound_queries.get_published_learning_unit` | Availability-shaped retrieval of one complete published learning unit. |

## Verification boundary

| test layer | uses | verifies | does not verify |
|---|---|---|---|
| Application tests | Outbound-query test doubles. | Application orchestration and observable validation. | Real database, queries, mapping, randomization algorithm, or persistence technology. |
| Persistence-adapter contract tests | Real persistence adapter boundary. | Adapter-owned guarantees and technical failure separation. | PWA flow, transport mapping, or application test-double behavior. |

Application tests must be able to represent:

- ordered `LearningUnitRef[]`;
- observable invalid selection arrays;
- selection technical failure;
- `Available(complete_learning_unit)`;
- `Unavailable`;
- retrieval technical failure.

## Boundary

| concern | owner |
|---|---|
| Shared outbound-query dependency and verification rules | `spec:product.application.outbound_queries` |
| Selection use-case policy | `spec:product.application.learning_unit_selection.create_complete_shuffle_queue` |
| Retrieval use-case orchestration | `spec:product.application.learning_unit_retrieval` |
| Current published state and availability | `spec:product.application.published_content` |
| Concrete persistence and transport implementation | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application` | Parent application overview. |
| `spec:product.application.learning_unit_selection` | Defines selection policy and result validation. |
| `spec:product.application.learning_unit_retrieval` | Defines retrieval use-case orchestration. |
| `spec:product.application.published_content` | Defines committed current state and availability. |
| PRODUCT-ADR-APPLICATION-003 | Establishes application use cases and technical retrieval failure separation. |
| PRODUCT-ADR-APPLICATION-004 | Establishes retrieval adapter obligations and application-test double allowance. |
