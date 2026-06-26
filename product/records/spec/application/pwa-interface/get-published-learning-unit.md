# Contract: Get published learning unit (PWA interface)

- **id**: `spec:product.application.pwa_interface.get_published_learning_unit`
- **status**: draft
- **date**: 2026-06-27
- **parent**: `spec:product.application.pwa_interface`
- **contract_class**: `interface`

## What this is

PWA-facing contract for the `GetPublishedLearningUnit` operation.
The contract defines the semantic request, normal results, and failure categories without specifying transport, serialization, or retry timing.

## Non-goals

- HTTP route, method, header, or status code.
- JSON field names, schemas, or serialization format.
- Retry delay, backoff, timeout, or client configuration.
- Frontend framework, state library, or source layout.
- Complete learning-unit field list. (Defined by `spec:product.learning.learning_unit`.)
- Retrieval use-case orchestration details. (See `spec:product.application.learning_unit_retrieval`.)
- Concrete exception types or programming-language interface shapes.

## Request

| property | contract |
|---|---|
| Input | Exactly one `LearningUnitRef`. |
| Origin | The reference must come unchanged from the PWA queue returned by `CreateCompleteShuffleQueue`. |
| Interpretation | The PWA must not parse, normalize, enrich, or reinterpret the reference before supplying it. |
| Excluded inputs | Queue position, session state, and initial or replacement context must not be included. |

## Response

```text
Available(complete_learning_unit)
| Unavailable
```

| result | meaning |
|---|---|
| `Available(complete_learning_unit)` | The current published state for the reference exists and is available. The result contains one complete learning unit. |
| `Unavailable` | The current state for the reference is missing or currently unavailable. |

Rules:

- A missing reference and a currently unavailable reference both produce `Unavailable`.
- `Unavailable` is a normal availability result. It is not a technical failure.
- `Available` contains one complete learning unit satisfying `spec:product.learning.learning_unit`.

### Available content boundary

| included | excluded |
|---|---|
| Complete learning unit under `spec:product.learning.learning_unit` | Partial learning-unit content |
| Learner-visible attribution | Opaque provenance |
| | Availability metadata |
| | Queue metadata |
| | Pipeline processing data |

See `spec:product.learning.learning_unit` for the complete learning-unit field contract. The field list is not duplicated here.

## Errors

| failure | meaning | retryable |
|---|---|---|
| `MappingFailure` | Application-visible data could not be mapped into the learning-unit contract. | No. |
| `InfrastructureFailure` | Required technical infrastructure could not complete retrieval. | Yes. |

Rules:

- Each failure must provide safe diagnostic information identifying the failure category, affected operation, and a sanitized summary when available.
- Failures must not expose raw exceptions, stack traces, credentials, SQL, filesystem paths, framework internals, or equivalent unsafe implementation details.
- Failures must not be converted into `Available` or `Unavailable`.

## Boundary

| concern | owner |
|---|---|
| PWA-facing retrieval request, results, and failure categories | `spec:product.application.pwa_interface.get_published_learning_unit` |
| Retrieval use-case orchestration | `spec:product.application.learning_unit_retrieval` |
| Current published state and availability | `spec:product.application.published_content` |
| Complete learning-unit semantics and field definitions | `spec:product.learning.learning_unit` |
| `LearningUnitRef` semantics | `spec:product.application.pwa_interface` |
| Shared application-interface verification obligations | `spec:product.application.pwa_interface` |
| UI retry attempts, `Unavailable` skipping, and navigation after retrieval | `spec:product.ui.learning_flow` |
| `InfrastructureFailure` current-screen preservation and loading or retry surface | `spec:product.ui.pages.learning_page` |
| Terminal `MappingFailure` safe diagnostic surface | `spec:product.ui.pages.main_page` |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application.pwa_interface` | Parent interface overview. Defines `LearningUnitRef` semantics and verification obligations. |
| `spec:product.application.learning_unit_retrieval` | Retrieval use-case orchestration referenced by this contract. |
| `spec:product.application.outbound_queries.get_published_learning_unit` | Outbound query used by the retrieval use case. |
| `spec:product.application.published_content.availability` | Defines the availability meaning applied during retrieval. |
| `spec:product.learning.learning_unit` | Defines the complete learning unit returned in `Available`. |
| `spec:product.ui.learning_flow` | PWA retry, `Unavailable` skipping, and session ownership. |
| `spec:product.ui.pages.learning_page` | Current-screen preservation during `InfrastructureFailure` retry; loading and retry surface. |
| `spec:product.ui.pages.main_page` | Owning failure surface after terminal retrieval `MappingFailure`. |
| PRODUCT-ADR-APPLICATION-003 | Establishes retrieval results, attribution, and provenance exclusion. |
| PRODUCT-ADR-APPLICATION-004 | Establishes the result-shaped outbound retrieval port. |
| PRODUCT-ADR-APPLICATION-005 | Establishes `MappingFailure`, `InfrastructureFailure`, safe diagnostics, and retryability. |
| PRODUCT-ADR-APPLICATION-006 | Establishes `LearningUnitRef` stability, opacity, equality, and pass-through semantics. |
