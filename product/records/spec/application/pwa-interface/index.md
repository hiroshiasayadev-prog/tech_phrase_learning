# Overview: PWA-facing application interface

- **id**: `spec:product.application.pwa_interface`
- **status**: draft
- **date**: 2026-06-27
- **parent**: `spec:product.application`

## What this is

Transport-independent boundary between the PWA and the application use cases.
The interface exposes `CreateCompleteShuffleQueue` and `GetPublishedLearningUnit` as semantic operations without defining HTTP, serialization, or transport details.

## Current contract

| concern | contract |
|---|---|
| Boundary | The interface is transport-independent. |
| Exposed operations | `CreateCompleteShuffleQueue` and `GetPublishedLearningUnit`. |
| Normal-result separation | Each operation returns its normal semantic result separately from any exposed failure. |
| Failure separation | Failure categories must not be converted into empty queues, `Available`, or `Unavailable`. |
| `LearningUnitRef` identity | One `LearningUnitRef` stably identifies one published learning-unit identity. |
| `LearningUnitRef` handling | The PWA treats each reference as opaque and may compare references for equality. |
| Pass-through | The PWA passes a queued reference unchanged into `GetPublishedLearningUnit`. |
| Availability | A reference does not carry availability. Retrieval rechecks current availability at call time. |
| Initial or replacement context | Neither operation receives an initial or replacement context flag from the PWA. |
| Safe diagnostics | Each exposed failure provides a category, affected operation, and a sanitized summary when available. |
| Unsafe detail exclusion | The interface must not expose raw exceptions, stack traces, credentials, SQL, filesystem paths, framework internals, or equivalent implementation details. |
| Application ownership | Application contracts own requests, normal result categories, failure categories, retryability, and safe diagnostic meaning. |
| UI ownership | UI contracts own screens, retry attempts, navigation, queue disposal, session disposal, and diagnostic presentation. |
| Deferred implementation | HTTP, serialization, concrete exception types, frameworks, source layout, retry timing, and client configuration remain deferred. |

## LearningUnitRef semantics

`LearningUnitRef` is the shared application-level reference type used by both operations.

| property | contract |
|---|---|
| Stability | The reference stably identifies one published learning-unit identity. |
| Opacity | The PWA must treat each reference as opaque. |
| Equality | The PWA may compare two references for equality. Two equal references identify the same learning-unit identity. |
| Pass-through | The PWA must pass a queued reference unchanged to `GetPublishedLearningUnit`. |
| Availability | A reference does not carry availability. Retrieval rechecks current availability at call time. |
| Wire representation | The concrete wire representation remains deferred. |

A `LearningUnitRef` must not expose:

- pipeline provenance;
- database identity or schema;
- queue identity or position;
- learner progress;
- availability state;
- publication revision information.

## Non-goals

- HTTP routes, methods, headers, and status codes.
- JSON fields, serialization formats, and wire representation of `LearningUnitRef`.
- Concrete exception types and programming-language interface shapes.
- Retry delays, backoff, timeout values, and client configuration.
- Frontend framework, state library, route structure, and source layout.
- Authentication, learner accounts, durable progress, and backend session identity.
- PWA queue position, loaded content, session, navigation, and retry behavior.
- Application selection policy and result-validation algorithm details. (See `spec:product.application.learning_unit_selection`.)
- Retrieval use-case orchestration details. (See `spec:product.application.learning_unit_retrieval`.)

## Topics

| title | kind | ref | summary |
|---|---|---|---|
| Queue creation | Contract | `spec:product.application.pwa_interface.create_complete_shuffle_queue` | PWA-facing request, normal results, and failure contract for `CreateCompleteShuffleQueue`. |
| Learning-unit retrieval | Contract | `spec:product.application.pwa_interface.get_published_learning_unit` | PWA-facing request, normal results, and failure contract for `GetPublishedLearningUnit`. |

## Verification obligations

### Application-interface tests

Application-interface tests use application use-case test doubles at the PWA-facing interface boundary.

| obligation | required verification |
|---|---|
| Parameter-free queue request | Queue creation invokes the semantic use case without a PWA-supplied selection parameter. |
| Ordered reference preservation | A successful ordered reference array reaches the PWA boundary without reordering. |
| Successful empty queue | `Success([])` remains a normal success and does not become failure. |
| Failure-category preservation | `InvalidSelectionResult`, `MappingFailure`, and `InfrastructureFailure` remain distinct where each operation permits them. |
| Safe diagnostic exposure | Public failure data contains only the safe diagnostic contract. |
| Unchanged reference pass-through | A queued `LearningUnitRef` reaches retrieval unchanged. |
| Available complete content | `Available` contains one complete unit satisfying `spec:product.learning.learning_unit`. |
| Attribution preservation | Learner-visible attribution remains present in available complete content. |
| Provenance exclusion | Available results do not expose opaque provenance or pipeline internals. |
| Unavailable preservation | `Unavailable` remains a normal result and does not become failure. |

Application-interface tests must not re-verify:

- database queries or persistence mapping implementation;
- randomization algorithm;
- transport serialization;
- UI component implementation.

### Future transport-adapter contract tests

| obligation | required verification |
|---|---|
| Request conversion | Convert each wire request into the corresponding semantic application request without inventing application parameters. |
| Result-category preservation | Preserve queue success, empty success, `Available`, `Unavailable`, and each permitted failure category. |
| Reference round trip | Preserve `LearningUnitRef` identity across serialization and deserialization. |
| Safe diagnostic boundary | Preserve permitted safe diagnostic meaning across the transport boundary. |
| Unsafe-detail exclusion | Prevent raw exceptions, stack traces, secrets, SQL, paths, and framework internals from reaching the PWA. |
| Category non-conflation | Do not conflate normal results, `InvalidSelectionResult`, `MappingFailure`, and `InfrastructureFailure`. |

Future transport-adapter contract tests must not define a route, method, status code, header, JSON field, schema, or serialization format.

## Boundary

| concern | owner |
|---|---|
| Transport-independent PWA-facing operations and `LearningUnitRef` semantics | `spec:product.application.pwa_interface` |
| Queue-creation request, results, and failure contract | `spec:product.application.pwa_interface.create_complete_shuffle_queue` |
| Retrieval request, results, and failure contract | `spec:product.application.pwa_interface.get_published_learning_unit` |
| Selection policy and result validation | `spec:product.application.learning_unit_selection` |
| Retrieval use-case orchestration | `spec:product.application.learning_unit_retrieval` |
| PWA transient queue, session, navigation, retry, and diagnostic presentation | `spec:product.ui` |
| Transport, serialization, and adapter implementation | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application` | Parent application overview. |
| `spec:product.application.pwa_interface.create_complete_shuffle_queue` | Queue-creation operation contract. |
| `spec:product.application.pwa_interface.get_published_learning_unit` | Learning-unit retrieval operation contract. |
| `spec:product.application.learning_unit_selection` | Selection policy and queue-result semantics. |
| `spec:product.application.learning_unit_retrieval` | Retrieval use-case orchestration. |
| `spec:product.learning.learning_unit` | Complete learner-visible content and attribution. |
| `spec:product.ui.learning_flow` | PWA transitions, retry, queue, and session ownership. |
| PRODUCT-ADR-APPLICATION-003 | Establishes application use cases, retrieval results, and attribution boundary. |
| PRODUCT-ADR-APPLICATION-004 | Establishes the result-shaped outbound retrieval port. |
| PRODUCT-ADR-APPLICATION-005 | Establishes PWA-facing failure categories, safe diagnostics, and retryability. |
| PRODUCT-ADR-APPLICATION-006 | Establishes `LearningUnitRef` stability, opacity, equality, and pass-through semantics. |
