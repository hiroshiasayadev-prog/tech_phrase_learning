# Overview: Application

- **id**: `spec:product.application`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product`

## What this is

Owner of runtime learning-unit selection, availability-aware retrieval, application use cases, and outbound query ports.
The area serves published learning content without owning pipeline generation or PWA learner state.

## Current contract

| concern | contract |
|---|---|
| Runtime source | Read only the published-content area. |
| Pipeline isolation | Do not read or model pipeline processing data. |
| Published content | Treat identity, complete learning unit, availability, and opaque provenance as one current runtime projection. |
| Availability | Keep selection availability separate from current unit content. |
| Queue creation | Return at most 100 unique available learning-unit references. |
| Queue scope | Use all available units for the first-MVP complete shuffle. |
| Queue state | Do not retain queue position, queue identity, or learner progress. |
| Unit retrieval | Recheck availability before returning one complete unit. |
| Stale queue entry | Return an unavailable result so the PWA can skip the reference. |
| Provenance | Keep one opaque provenance reference with the current publication. |
| Dependency direction | Keep adapters dependent on application ports and application dependent on domain rules. |

## Non-goals

- Source ingestion, learning-unit generation, and publication judgment.
- Pipeline processing-data schemas and model or prompt semantics.
- PWA queue position, learner answers, and session progression.
- HTTP routes, JSON schemas, and status-code contracts.
- Database tables, indexes, query language, and transaction implementation.
- Exact randomization and sampling algorithms.
- Authentication, learner accounts, and durable learner history.

## Topic map

| concern | owner |
|---|---|
| Published runtime projection and availability | `spec:product.application.published_content` |
| Queue creation and complete-unit retrieval | `spec:product.application.learning_unit_selection` |
| Learner-visible learning-unit semantics | `spec:product.learning.learning_unit` |
| Content generation and publication decisions | `spec:product.pipeline` |
| Transient queue and learner session state | `spec:product.ui.learning_flow` |

## Topics

| title | kind | ref | summary |
|---|---|---|---|
| Published content | Concept | `spec:product.application.published_content` | Shared-database boundary, current content, availability, provenance, and atomic replacement. |
| Learning-unit selection | Concept | `spec:product.application.learning_unit_selection` | Application use cases, queue semantics, retrieval behavior, domain rules, and query ports. |

## Boundary

| concern | owner |
|---|---|
| Learning-unit meaning and composition | `spec:product.learning` |
| Generation, validation, publication decision, and published-area writes | `spec:product.pipeline` |
| Runtime selection and availability-aware reads | `spec:product.application` |
| Learner-flow state and screen behavior | `spec:product.ui` |
| Concrete transport, database, and framework adapters | Implementation. |

## Dependency direction

```text
transport adapter
      |
      v
application use case
      |
      +----> application domain rules
      |
      +----> outbound query port
                    ^
                    |
                DB adapter
```

- Adapters may depend on application contracts.
- Application use cases may depend on application domain rules and learning contracts.
- Application domain rules must not depend on adapters, frameworks, or database schemas.
- Application code must not depend on pipeline processing data.
- UI code must not depend on pipeline processing data.

## Related specs

| ref | relation |
|---|---|
| `spec:product` | PRODUCT placement router and cross-area dependency direction. |
| `spec:product.learning` | Defines the learning content served by this area. |
| `spec:product.pipeline` | Produces and publishes the content read by this area. |
| `spec:product.ui` | Consumes application behavior while owning transient learner state. |
| PRODUCT-ADR-APPLICATION-001 | Establishes the application boundary and runtime architecture. |
