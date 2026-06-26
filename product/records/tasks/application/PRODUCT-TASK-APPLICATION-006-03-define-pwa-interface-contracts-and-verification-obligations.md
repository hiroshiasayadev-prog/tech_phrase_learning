# PRODUCT-TASK-APPLICATION-006-03: Define PWA-interface contracts and verification obligations

- **id**: PRODUCT-TASK-APPLICATION-006-03
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-006
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-006-02
- **outputs**:

## Goal

Define the complete transport-independent contract map consumed by the first-MVP PWA.

Define verification obligations without selecting a transport, framework, or serialization format.

## Work

1. Read the T006-01 classification and T006-02 authority disposition.
2. Use only accepted ADRs and current specifications as normative authority.
3. Stop as `blocked` when any required normative claim lacks accepted ADR authority.
4. Define the queue-creation request contract for the first-MVP PWA.
5. Define successful non-empty and successful empty queue results.
6. Define invalid-request and technical-failure handling only under accepted authority.
7. Define the complete-unit retrieval request using one stable `LearningUnitRef`.
8. Define available and unavailable retrieval outcomes.
9. Keep unavailable content distinct from invalid requests and technical failures.
10. Define which technical failures are exposed as retryable request failures without choosing retry timing.
11. Define the content required in an available complete-unit result.
12. Preserve learner-visible attribution and exclude opaque provenance.
13. Map each interface outcome to the owning PWA transition.
14. Preserve unavailable-reference skipping without retrying the unavailable reference.
15. Preserve queue acquisition and unit-loading retry behavior for request failures.
16. Preserve successful empty initial and replacement queue behavior.
17. Preserve queue exhaustion as a PWA-owned trigger for another queue request.
18. Preserve the current screen, queue position, loaded unit, and session until a replacement unit loads successfully.
19. Define interface-level tests using application-boundary test doubles.
20. Define future transport-adapter contract-test responsibilities.
21. Keep routes, status codes, JSON fields, serialization, retry delays, and client configuration deferred.
22. Record the complete contract map and explicit no-change judgments in `## Evidence`.
23. Do not modify specifications in this task.

## Done condition

- Both PWA-facing operations have explicit transport-independent request contracts.
- Both operations have explicit normal-result contracts.
- Successful empty queue is distinct from request failure.
- `Unavailable` is distinct from invalid request and technical failure.
- Stable reference semantics are explicit without a wire representation.
- Available complete content includes all learner-visible fields required by the learning flow.
- Attribution remains available and provenance remains excluded.
- Every interface outcome maps to one owning PWA transition.
- Unavailable-reference skipping remains distinct from retryable request failure.
- Queue exhaustion remains PWA-owned.
- Replacement occurs only after successful complete-unit loading.
- Application-interface tests and future transport-adapter tests have separate responsibilities.
- No transport, framework, persistence, authentication, or backend-session choice enters the contract map.
- T006-04 can reflect the contract map without another conversation handoff.

## Verification

- Trace every contract claim to an accepted ADR or current specification.
- Confirm task evidence does not become decision authority.
- Compare queue outcomes with `spec:product.application.learning_unit_selection`.
- Compare retrieval outcomes with `spec:product.application.learning_unit_retrieval`.
- Compare state transitions with `spec:product.ui.learning_flow`.
- Compare visible content with `spec:product.learning.learning_unit`.
- Confirm HTTP and serialization details remain absent.
- Confirm no application or UI specification changed.

## Evidence

### Result

- **Verdict**: PASS.
- The accepted ADRs and current specifications provide complete authority for the required contract map.
- This task records an execution map for T006-04 and does not become normative authority.
- No ADR or specification changed in this task.
- The task created no new artifact, so `outputs` remains empty.

### Authority traceability

| concern | authority |
|---|---|
| Current published-content boundary, application use cases, normal retrieval results, attribution, and provenance exclusion | PRODUCT-ADR-APPLICATION-003; `spec:product.application`; `spec:product.application.learning_unit_retrieval`; `spec:product.application.published_content` |
| Result-shaped retrieval port and adapter failure separation | PRODUCT-ADR-APPLICATION-004; `spec:product.application.outbound_queries`; `spec:product.application.outbound_queries.get_published_learning_unit` |
| PWA-facing failure categories, safe diagnostics, and retryability | PRODUCT-ADR-APPLICATION-005 |
| `LearningUnitRef` stability, opacity, equality, and unchanged pass-through | PRODUCT-ADR-APPLICATION-006 |
| PWA queue, loaded-unit, session, retry-count, navigation, and transient-state ownership | PRODUCT-ADR-UI-001; `spec:product.ui`; `spec:product.ui.learning_flow` |
| Category-specific failure transitions and diagnostic surfaces | PRODUCT-ADR-UI-002 |
| Queue policy, ordered result, empty success, and observable result validation | `spec:product.application.learning_unit_selection`; `spec:product.application.learning_unit_selection.create_complete_shuffle_queue`; `spec:product.application.learning_unit_selection.queue_contract`; `spec:product.application.learning_unit_selection.result_validation` |
| Selection outbound-query guarantees | `spec:product.application.outbound_queries.select_learning_unit_refs` |
| Complete learner-visible unit and attribution meaning | `spec:product.learning.learning_unit` |
| Main-page and learning-page visible ownership | `spec:product.ui.pages.main_page`; `spec:product.ui.pages.learning_page` |

PRODUCT-ADR-APPLICATION-001 and PRODUCT-ADR-APPLICATION-002 were treated as superseded history only.

### Shared interface rules

| concern | contract |
|---|---|
| Boundary | The PWA-facing application interface is transport-independent. |
| Operations | The interface exposes `CreateCompleteShuffleQueue` and `GetPublishedLearningUnit`. |
| Normal-result separation | Each operation returns its normal semantic result separately from exposed failures. |
| Failure separation | Failure categories must not be converted into empty queues, `Available`, or `Unavailable`. |
| `LearningUnitRef` identity | One `LearningUnitRef` stably addresses one published learning-unit identity. |
| `LearningUnitRef` handling | The PWA treats the reference as opaque and may compare references for equality. |
| Pass-through | The PWA passes a queued reference unchanged into retrieval. |
| Availability | A reference does not carry availability. Retrieval rechecks current availability. |
| Safe diagnostics | Exposed failures provide category, affected operation, and a sanitized summary when available. |
| Unsafe detail exclusion | The interface excludes raw exceptions, stack traces, credentials, SQL, filesystem paths, framework internals, and equivalent details. |
| Application ownership | Application contracts own requests, normal result categories, failure categories, retryability, and safe diagnostic meaning. |
| UI ownership | UI contracts own screens, retry attempts, navigation, queue disposal, session disposal, and diagnostic presentation. |
| Initial or replacement context | The PWA owns the context. Neither operation receives an initial or replacement flag. |
| Deferred implementation | HTTP, serialization, concrete exception types, frameworks, source layout, retry timing, and client configuration remain deferred. |

### `CreateCompleteShuffleQueue` contract map

| item or outcome | semantic contract | retryability | owning UI transition | state rule |
|---|---|---|---|---|
| Request | The PWA supplies no semantic request parameter. The use case applies `SelectionScope = All` and `maximum_count = 100`. | Not applicable. | The PWA starts queue acquisition from its current UI-owned lifecycle context. | The request creates no backend queue identity, position, reservation, history, or learner progress. |
| Successful non-empty result | Return an ordered `LearningUnitRef[]` accepted by selection-result validation. Complete learning-unit content is not returned. | Not applicable. | For initial acquisition, keep main visible and begin first-unit retrieval. For replacement acquisition, begin retrieval from the replacement queue without sending replacement context to the application. | Preserve returned order. Do not change loaded content or session before a unit loads successfully. |
| Successful empty result | Return `Success([])` as a normal success. Do not introduce an `EmptyQueue` failure category. | Not applicable. | Show the UI-owned empty-queue screen for initial or replacement acquisition. | Discard any current queue and session on entry to the empty-queue screen. Do not automatically or manually retry the accepted empty result. |
| `InvalidSelectionResult` | The application detected an observable outbound selection-contract violation. The outcome is not an invalid PWA request. | Non-retryable. | Do not enter automatic retry. Remain on the main-page failure surface and show only the safe diagnostic. | Do not create or normalize a partial queue. No backend queue state exists. |
| `MappingFailure` | Application-visible data could not be mapped into an application-owned contract. | Non-retryable. | Do not enter automatic retry. Remain on the main-page failure surface and show only the safe diagnostic. | Do not create or normalize a partial queue. No backend queue state exists. |
| `InfrastructureFailure` | Required technical infrastructure could not complete queue creation. | Retryable. | Enter the existing queue-creation retry flow on the main-page surface. | Keep main-page state stable through retry. The application creates no queue or session state. |

The PWA-facing operation does not expose `eligible_count`, queue identity, reservation data, backend position, queue history, or complete content.

### `GetPublishedLearningUnit` contract map

| item or outcome | semantic contract | retryability | owning UI transition | state-preservation or disposal rule |
|---|---|---|---|---|
| Request | Supply exactly one opaque `LearningUnitRef` unchanged from the PWA queue. | Not applicable. | Request the selected pending reference from the current PWA-owned lifecycle context. | The request does not transfer queue position, session state, or initial or replacement context. |
| `Available(complete_learning_unit)` | The current published state exists, remains available, and yields one complete learning unit. | Not applicable. | Initial loading enters the learning page. Replacement loading enters a new learning session on the learning page. | Replace queue position, loaded unit, and session only after the complete unit loads successfully. |
| `Unavailable` | The current state is missing or currently unavailable. This outcome is normal availability, not technical failure. | No retry of the affected reference. | Remove only the affected pending reference and request the next pending reference. | Keep the current loaded unit, queue position, and session unchanged until a later reference loads successfully. |
| `MappingFailure` | Current data could not be mapped into the complete application learning-unit contract. | Non-retryable. | End the active learning flow, return to main, and show the safe diagnostic on the returned main-page surface. | Discard the active queue and session. Do not retain the previous learning screen as a manual retry surface. |
| `InfrastructureFailure` | Required technical infrastructure could not complete retrieval. | Retryable. | Enter the existing retrieval retry flow on the current screen. | Preserve the current screen, loaded unit, queue position, and session during automatic and manual retry. |

### Available content boundary

`Available` must contain one complete learning unit satisfying `spec:product.learning.learning_unit`.

The result must:

- include learner-visible attribution;
- preserve the learning-unit contract as one complete result;
- avoid partial learning-unit content;
- exclude opaque provenance;
- exclude availability metadata;
- exclude queue metadata;
- exclude pipeline processing data.

This task does not duplicate the learning-unit field list.

### Queue and lifecycle transitions

| lifecycle point | trigger or result | required PWA behavior | application-interface boundary |
|---|---|---|---|
| Initial non-empty queue | Queue creation returns one or more references. | Preserve returned order and begin loading the first pending reference while main remains visible. | The result contains references only. |
| Initial empty queue | Queue creation returns `Success([])`. | Show the empty-queue screen and do not request another queue for that accepted result. | Empty success remains separate from failure. |
| Initial first-unit loading | The PWA has an initial non-empty queue. | Request references in order until one returns `Available` or the queue exhausts. | Retrieval accepts one unchanged reference per call. |
| Unavailable-reference skipping | Retrieval returns `Unavailable`. | Remove only that pending reference and continue with the next reference. | The application does not select the replacement reference. |
| Queue exhaustion | No pending reference remains. | Trigger one parameter-free `CreateCompleteShuffleQueue` request without an intermediate application context flag. | Queue exhaustion is a PWA-owned trigger. |
| Replacement non-empty queue | Replacement acquisition returns references. | Preserve returned order and begin loading replacement candidates. | The operation does not know that the request is a replacement. |
| Replacement empty queue | Replacement acquisition returns `Success([])`. | End the learning flow, show the empty-queue screen, and discard queue and session state. | Empty success remains a normal queue result. |
| Successful replacement | Retrieval returns `Available` for a pending replacement reference. | Replace queue position, loaded content, and session together after successful loading. | The application returns complete content and does not mutate PWA state. |
| Infrastructure retry | Either operation returns `InfrastructureFailure`. | Use the existing operation-specific retry flow and preserve the owning retry surface. | Retryability is application-owned. Retry attempts and presentation are UI-owned. |
| Terminal queue-creation mapping or selection failure | Queue creation returns `MappingFailure` or `InvalidSelectionResult`. | Do not automatically retry. Use the main-page failure surface. | The failure remains distinct from normal empty success. |
| Terminal retrieval mapping failure | Retrieval returns `MappingFailure`. | End the active flow, discard queue and session, and return to main. | The failure remains distinct from `Unavailable`. |
| Return to main | The learner selects `Back to main` or a terminal retrieval mapping transition returns to main. | Discard the current queue and session. | The application owns no retained learner-flow state. |

Initial and replacement context must not be added to either application request.

### Verification obligations

#### Application-interface tests

Application-interface tests use application use-case test doubles.

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
| Unavailable preservation | `Unavailable` remains a normal result and does not become failure or missing-content exception. |

Application-interface tests must not reverify:

- database queries;
- persistence mapping implementation;
- randomization algorithms;
- transport serialization;
- UI component implementation.

#### Future transport-adapter contract tests

| obligation | required verification |
|---|---|
| Request conversion | Convert each wire request into the corresponding semantic application request without inventing application parameters. |
| Result-category preservation | Preserve queue success, empty success, `Available`, `Unavailable`, and each permitted failure category. |
| Reference round trip | Preserve `LearningUnitRef` identity across serialization and deserialization. |
| Safe diagnostic boundary | Preserve permitted safe diagnostic meaning across the transport boundary. |
| Unsafe-detail exclusion | Prevent raw exceptions, stack traces, secrets, SQL, paths, framework internals, and equivalent details from reaching the PWA. |
| Category non-conflation | Do not conflate normal results, `InvalidSelectionResult`, `MappingFailure`, and `InfrastructureFailure`. |

Future transport-adapter contract tests do not define a route, method, status code, header, JSON field, schema, or serialization format.

### Required no-change judgments

| concern | judgment |
|---|---|
| Accepted selection policy | No change. `SelectionScope = All` and `maximum_count = 100` remain fixed. |
| Accepted retrieval semantics | No change. Retrieval remains `Available(complete_learning_unit) | Unavailable`. |
| Outbound-query contracts | No change. Existing selection and retrieval adapter obligations remain authoritative. |
| Published-content ownership | No change. The pipeline writes published state and the application reads committed current state. |
| Attribution and provenance boundary | No change. Learner-visible attribution remains available and opaque provenance remains excluded. |
| PWA transient-state ownership | No change. Queue, loaded unit, session, navigation, and retry attempts remain PWA-owned. |
| Retry count | No change. One initial attempt and three automatic retries remain the accepted UI behavior, followed by manual retry where permitted. |
| Backend state | No backend session, queue persistence, reservation, history, or durable progress is introduced. |
| Deferred implementation | HTTP, serialization, frameworks, concrete exception types, source layout, retry delays, backoff, and timeout remain deferred. |

### Done-condition check

- Both PWA-facing operations have explicit transport-independent request contracts.
- Both operations have explicit normal-result contracts.
- Empty queue success remains distinct from request failure.
- `Unavailable` remains distinct from invalid request and technical failure.
- `LearningUnitRef` semantics remain explicit without a wire representation.
- Available content remains complete and includes learner-visible attribution.
- Every exposed outcome maps to an owning PWA transition.
- Unavailable-reference skipping remains distinct from retryable failure.
- Queue exhaustion remains PWA-owned.
- Replacement occurs only after successful complete-unit loading.
- Application-interface and future transport-adapter tests have separate responsibilities.
- No transport, framework, persistence, authentication, or backend-session choice was introduced.

### Verification result and limitations

- Design Records MCP did not index the PRODUCT records, so filesystem fallback was used for reads and updates.
- `validate_records` rejected the PRODUCT task ID range as unsupported, so no Design Records MCP validation success is claimed.
- The active repository toolset exposes filesystem operations but no shell execution.
- `git diff --check` and `git status --short` could not be executed in this tool environment.
- Filesystem operation history confirms that this task file was the only repository file edited during this execution.
- A full filesystem reread confirmed the required headings, substantive Evidence, empty `outputs`, reciprocal parent relation, and matching source requirement before closure.
- No application or UI specification was edited.
- No ADR was created or edited.
- The validation and Git limitations are explicit and do not change the completed contract-map judgment.
