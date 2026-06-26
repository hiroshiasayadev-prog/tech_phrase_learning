# Contract: Create complete-shuffle queue (PWA interface)

- **id**: `spec:product.application.pwa_interface.create_complete_shuffle_queue`
- **status**: draft
- **date**: 2026-06-27
- **parent**: `spec:product.application.pwa_interface`
- **contract_class**: `interface`

## What this is

PWA-facing contract for the `CreateCompleteShuffleQueue` operation.
The contract defines the semantic request, normal results, and failure categories without specifying transport, serialization, or retry timing.

## Non-goals

- HTTP route, method, header, or status code.
- JSON field names, schemas, or serialization format.
- Retry delay, backoff, timeout, or client configuration.
- Frontend framework, state library, or source layout.
- Application selection policy and result-validation details. (See `spec:product.application.learning_unit_selection`.)
- Concrete exception types or programming-language interface shapes.
- Backend queue identity, reservation, queue history, or learner progress.

## Request

| property | contract |
|---|---|
| Semantic parameters | The PWA supplies no semantic request parameter. |
| Selection policy | The application applies `SelectionScope = All` and `maximum_count = 100`. |
| Context | Initial and replacement context must not be added to this request. |

## Response

```text
Success(LearningUnitRef[])
```

| result | meaning |
|---|---|
| `Success(refs)` where `refs` is non-empty | Ordered list of stable learning-unit references selected for the shuffle queue. |
| `Success([])` | Successful queue creation with no currently available units. |

Rules:

- The returned array is ordered. The PWA must preserve the returned order.
- A successful empty result is `Success([])`. It is not a failure.
- The operation does not return complete learning-unit content.

The operation must not expose:

- `eligible_count`;
- queue identity;
- reservation data;
- backend position;
- queue history;
- learner progress;
- complete learning-unit content.

See `spec:product.application.learning_unit_selection` for selection policy and result-validation details.

## Errors

| failure | meaning |
|---|---|
| `InvalidSelectionResult` | The application detected an observable outbound selection-contract violation. Not an invalid PWA request. |
| `MappingFailure` | Application-visible data could not be mapped into an application-owned contract. |
| `InfrastructureFailure` | Required technical infrastructure could not complete queue creation. |

Rules:

- `MappingFailure` is non-retryable for this operation.
- `InfrastructureFailure` is retryable for this operation.
- `InvalidSelectionResult` retryability is not an application classification. UI automatic retry behavior for `InvalidSelectionResult` belongs to `spec:product.ui.learning_flow`.
- Each failure must provide safe diagnostic information identifying the failure category, affected operation, and a sanitized summary when available.
- Failures must not expose raw exceptions, stack traces, credentials, SQL, filesystem paths, framework internals, or equivalent unsafe implementation details.
- Failures must not be converted into `Success([])` or any normal queue result.

## Boundary

| concern | owner |
|---|---|
| PWA-facing queue-creation request, results, and failure categories | `spec:product.application.pwa_interface.create_complete_shuffle_queue` |
| Selection scope, maximum count, and result validation | `spec:product.application.learning_unit_selection` |
| Selection outbound-query guarantees | `spec:product.application.outbound_queries.select_learning_unit_refs` |
| `LearningUnitRef` semantics | `spec:product.application.pwa_interface` |
| Shared application-interface verification obligations | `spec:product.application.pwa_interface` |
| UI outcome consumption, retry entry, and navigation for queue creation | `spec:product.ui.learning_flow` |
| Initial queue-creation retry and failure surface | `spec:product.ui.pages.main_page` |
| Replacement queue-creation retry and failure surface | `spec:product.ui.pages.learning_page` |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application.pwa_interface` | Parent interface overview. Defines `LearningUnitRef` semantics and verification obligations. |
| `spec:product.application.learning_unit_selection` | Selection policy and queue-result semantics referenced by this contract. |
| `spec:product.application.learning_unit_selection.create_complete_shuffle_queue` | Application use-case policy and orchestration. |
| `spec:product.application.outbound_queries.select_learning_unit_refs` | Outbound query providing the reference array. |
| `spec:product.ui.learning_flow` | PWA retry, queue ownership, and initial or replacement queue-creation transitions. |
| `spec:product.ui.pages.main_page` | Owning retry and failure surface for initial queue creation. |
| `spec:product.ui.pages.learning_page` | Owning retry and failure surface for replacement queue creation. |
| PRODUCT-ADR-APPLICATION-003 | Establishes use cases, queue size, and no backend learner state. |
| PRODUCT-ADR-APPLICATION-005 | Establishes `InvalidSelectionResult`, `MappingFailure`, `InfrastructureFailure`, safe diagnostics, and retryability. |
| PRODUCT-ADR-APPLICATION-006 | Establishes `LearningUnitRef` stability, opacity, equality, and pass-through semantics. |
