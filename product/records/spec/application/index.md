# Overview: Application

- **id**: `spec:product.application`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product`

## What this is

Owner of runtime learning-unit selection, availability-aware retrieval, application use cases, and outbound query ports.
The area serves published learning content without owning pipeline generation, persistence implementation, or PWA learner state.

## Current contract

| concern | contract |
|---|---|
| Runtime source | Read only committed published content. |
| Application use cases | Provide `CreateCompleteShuffleQueue` and `GetPublishedLearningUnit`. |
| Selection | Create an ordered reference array for currently available learning units. |
| Retrieval | Recheck availability before returning one complete learning unit. |
| Outbound queries | Define application-owned read capabilities implemented by persistence adapters. |
| Dependency direction | Keep persistence adapters dependent on application contracts. |
| Pipeline isolation | Do not read or model pipeline processing data. |
| UI boundary | Do not own queue position, loaded content, learner answers, retry timing, or navigation. |

## Definitions

| term | definition |
|---|---|
| `application use case` | Application-owned operation that coordinates domain rules and outbound queries before returning a semantic result. |
| `persistence adapter` | Adapter that implements application-owned outbound query contracts by reading committed published content. |
| `LearningUnitRef` | Stable reference to one published learning unit inside the published-content boundary. |

## Non-goals

- Source ingestion, learning-unit generation, and publication judgment.
- Pipeline processing-data schemas and model or prompt semantics.
- PWA queue position, learner answers, session progression, loading, and retry behavior.
- HTTP routes, JSON schemas, and status-code contracts.
- Database tables, indexes, query language, and transaction implementation.
- Exact randomization and sampling algorithms.
- Programming-language interfaces, classes, method names, and source layout.

## Topics

| title | kind | ref | summary |
|---|---|---|---|
| Published content | Overview | `spec:product.application.published_content` | Current runtime state, availability, provenance boundary, and pipeline handoff input. |
| Learning-unit selection | Overview | `spec:product.application.learning_unit_selection` | Selection policy, scope, queue result, and application-side result validation. |
| Learning-unit retrieval | Contract | `spec:product.application.learning_unit_retrieval` | Application use case for retrieving one currently available complete learning unit. |
| Outbound queries | Overview | `spec:product.application.outbound_queries` | Shared query-port dependency, failure, adapter, and verification rules. |

## Boundary

| concern | owner |
|---|---|
| Learning-unit meaning and composition | `spec:product.learning.learning_unit` |
| Generation, validation, publication decisions, and published-content writes | `spec:product.pipeline` |
| Runtime selection, retrieval orchestration, and outbound read contracts | `spec:product.application` |
| Learner-flow state and screen behavior | `spec:product.ui` |
| Concrete transport, database, framework, and source-layout choices | Implementation. |

## Dependency direction

```text
transport adapter
      |
      v
application use case
      |
      +----> application domain rules
      |
      +----> outbound query contract
                    ^
                    |
            persistence adapter
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
| `spec:product.learning.learning_unit` | Defines the complete learning unit served by this area. |
| `spec:product.pipeline` | Produces and publishes the content read by this area. |
| `spec:product.ui` | Consumes application behavior while owning transient learner state. |
| PRODUCT-ADR-APPLICATION-003 | Establishes the application boundary, current published-content model, and retrieval result names. |
| PRODUCT-ADR-APPLICATION-004 | Establishes the outbound retrieval-port result shape and persistence-adapter obligations. |
