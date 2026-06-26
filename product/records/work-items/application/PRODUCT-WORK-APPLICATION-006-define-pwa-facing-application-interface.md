# PRODUCT-WORK-APPLICATION-006: Define the PWA-facing application interface

- **id**: PRODUCT-WORK-APPLICATION-006
- **status**: done
- **date**: 2026-06-26
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **impact_refs**:
  - PRODUCT-ADR-APPLICATION-003
  - PRODUCT-ADR-APPLICATION-004
  - PRODUCT-ADR-APPLICATION-005
  - PRODUCT-ADR-APPLICATION-006
  - PRODUCT-ADR-UI-001
  - PRODUCT-ADR-UI-002
  - spec:product.application
  - spec:product.application.pwa_interface
  - spec:product.application.pwa_interface.create_complete_shuffle_queue
  - spec:product.application.pwa_interface.get_published_learning_unit
  - spec:product.application.learning_unit_selection
  - spec:product.application.learning_unit_selection.create_complete_shuffle_queue
  - spec:product.application.learning_unit_retrieval
  - spec:product.learning.learning_unit
  - spec:product.ui.learning_flow
  - spec:product.ui.pages.main_page
  - spec:product.ui.pages.learning_page
- **tasks**:
  - PRODUCT-TASK-APPLICATION-006-01
  - PRODUCT-TASK-APPLICATION-006-02
  - PRODUCT-TASK-APPLICATION-006-03
  - PRODUCT-TASK-APPLICATION-006-04
  - PRODUCT-TASK-APPLICATION-006-05

## Goal

Define the transport-independent application interface consumed by the first-MVP PWA.

Make request, result, failure, and state-preservation contracts precise enough for later transport and implementation planning.

## Boundary

This work item owns the resolution flow for:

- PWA-facing queue-creation requests and results;
- PWA-facing complete-unit retrieval requests and results;
- stable learning-unit reference representation at the interface boundary;
- normal-result, invalid-request, and technical-failure classification;
- unavailable-reference skipping versus retryable request failure;
- successful empty-queue and exhausted-queue behavior;
- preservation of PWA queue, loaded-unit, session, navigation, and retry ownership;
- replacement only after successful complete-unit loading;
- learner-visible attribution returned with available complete content;
- future HTTP mapping without making HTTP semantics normative;
- interface-level verification obligations;
- ADR-first resolution of genuine normative gaps;
- specification reflection only after accepted authority exists;
- independent review and closure.

This work item treats the following contracts as fixed inputs:

- `CreateCompleteShuffleQueue` returns an ordered `LearningUnitRef[]`.
- The first-MVP queue request supplies no learner-selected scope parameters.
- An empty queue is a successful normal result.
- Queue creation creates no backend queue identity, position, reservation, history, or learner progress.
- `GetPublishedLearningUnit` accepts one `LearningUnitRef`.
- Retrieval returns `Available(complete_learning_unit) | Unavailable` as its normal result.
- Missing and currently unavailable references both produce `Unavailable`.
- Mapping and infrastructure failures remain outside normal availability results.
- The PWA owns queue position, loaded content, session state, navigation, and retry behavior.
- The PWA skips an unavailable queued reference without retrying that reference.
- The PWA replaces queue position, loaded content, and session only after successful loading.
- Available complete content includes learner-visible attribution and excludes provenance.

This work item does not own:

- concrete HTTP routes, methods, headers, or status codes;
- JSON field names, serialization formats, or generated client schemas;
- retry delays, backoff, timeout values, or transport-client configuration;
- component implementation, state-management libraries, or source layout;
- database queries, persistence schemas, or adapter algorithms;
- authentication, authorization, learner accounts, or durable learner identity;
- backend session identity, queue persistence, or learner progress;
- pipeline provenance internals.

Network and infrastructure failures must remain distinct from unavailable content.

The work item must not introduce backend session identity or transfer PWA-owned transient state into the application boundary.

## Impact Scope

| ref | impact |
|---|---|
| PRODUCT-ADR-APPLICATION-003 | Preserve application use cases, availability-shaped retrieval, attribution, provenance exclusion, and PWA state ownership. |
| PRODUCT-ADR-APPLICATION-004 | Preserve result-shaped retrieval and technical-failure separation. |
| PRODUCT-ADR-APPLICATION-005 | Define PWA-facing failure categories, safe diagnostic boundaries, and classified application retryability. |
| PRODUCT-ADR-APPLICATION-006 | Define stable opaque `LearningUnitRef` semantics without a wire representation. |
| PRODUCT-ADR-UI-001 | Preserve PWA ownership of transient queue, loaded content, session, navigation, and retry behavior. |
| PRODUCT-ADR-UI-002 | Define initial, replacement, and retrieval category-specific UI transitions and failure surfaces. |
| `spec:product.application` | Add or route the transport-independent inbound interface without changing application dependency direction. |
| `spec:product.application.pwa_interface` | Own shared PWA-facing interface semantics and verification obligations. |
| `spec:product.application.pwa_interface.create_complete_shuffle_queue` | Define the parameter-free queue-creation request, normal results, failures, and UI ownership pointers. |
| `spec:product.application.pwa_interface.get_published_learning_unit` | Define single-reference retrieval, availability results, failures, and attribution boundary. |
| `spec:product.application.learning_unit_selection` | Preserve queue creation semantics and ordered stable references. |
| `spec:product.application.learning_unit_selection.create_complete_shuffle_queue` | Preserve the first-MVP parameter-free request and successful empty result. |
| `spec:product.application.learning_unit_retrieval` | Preserve retrieval input, availability results, attribution, and technical failures. |
| `spec:product.learning.learning_unit` | Preserve complete learner-visible content and attribution meaning. |
| `spec:product.ui.learning_flow` | Align interface outcomes with skipping, retry, exhaustion, and successful replacement transitions. |
| `spec:product.ui.pages.main_page` | Preserve initial queue acquisition and first-unit loading behavior. |
| `spec:product.ui.pages.learning_page` | Preserve current-screen visibility and replacement only after successful loading. |

## Task flow

```text
T006-01 Establish PWA-interface baseline and gap inventory
  |
  v
T006-02 Resolve remaining PWA-interface decisions
  |
  v
T006-03 Define interface contracts and verification obligations
  |
  v
T006-04 Reflect accepted contracts into specifications
  |
  v
T006-05 Independent review and closure
```

- T006-01 classifies current authority, missing reflection, genuine decisions, and deferred transport details.
- T006-02 creates an ADR only for a genuine unresolved normative decision.
- T006-03 defines the complete transport-independent contract map under accepted authority.
- T006-04 reflects accepted contracts into focused application and UI specifications.
- T006-05 independently verifies traceability, state ownership, failure classification, and implementation readiness.

## Task Candidates

| task | responsibility |
|---|---|
| PRODUCT-TASK-APPLICATION-006-01 | Establish the current PWA-facing interface baseline and classify every candidate gap. |
| PRODUCT-TASK-APPLICATION-006-02 | Resolve only genuine normative decisions through accepted ADRs, or record that no new ADR is required. |
| PRODUCT-TASK-APPLICATION-006-03 | Define transport-independent request, result, failure, state-preservation, and verification contracts. |
| PRODUCT-TASK-APPLICATION-006-04 | Reflect accepted interface contracts into focused specifications without introducing transport semantics. |
| PRODUCT-TASK-APPLICATION-006-05 | Independently review every impact ref and close the work item after blocking findings are corrected. |

## Completion Condition

- Queue creation has a transport-independent PWA-facing request and result contract.
- Complete-unit retrieval has a transport-independent PWA-facing request and result contract.
- The interface uses a stable learning-unit reference without defining a wire representation.
- Successful non-empty queue, successful empty queue, available unit, and unavailable unit outcomes are explicit.
- Invalid requests remain distinct from normal unavailable content and infrastructure failures.
- Infrastructure and network failures remain distinct from normal queue and retrieval outcomes.
- Unavailable-reference skipping remains distinct from retryable request failure.
- Queue exhaustion and empty replacement-queue behavior align with `spec:product.ui.learning_flow`.
- The PWA retains ownership of queue position, loaded content, session, navigation, and retry behavior.
- Queue position, loaded content, and session change only after successful complete-unit loading.
- Available complete content includes learner-visible attribution and excludes provenance.
- Future HTTP mapping is possible without making routes, status codes, or JSON normative.
- No backend session identity, queue persistence, authentication, or learner account enters the design.
- Every normative specification change traces to an accepted ADR.
- No new ADR exists without a genuine unresolved normative decision.
- Interface tests and future transport-adapter tests have explicit boundaries.
- PRODUCT-TASK-APPLICATION-006-05 records `PASS` with no blocking findings.

## Evidence

### Result

- **Verdict**: DONE.
- T006-01 through T006-05 completed the planned resolution flow.
- Queue creation and complete-unit retrieval remain distinct transport-independent operations.
- PRODUCT-ADR-APPLICATION-005 and PRODUCT-ADR-APPLICATION-006 define public failures and stable-reference semantics.
- PRODUCT-ADR-UI-002 defines initial, replacement, and retrieval failure transitions.
- Current application and UI specifications reflect the accepted decisions.
- Independent T006-05 review returned PASS with no blocking or major findings.

### Delivered contracts

| ref | result |
|---|---|
| `spec:product.application.pwa_interface` | Owns shared interface semantics and verification obligations. |
| `spec:product.application.pwa_interface.create_complete_shuffle_queue` | Defines parameter-free queue creation, ordered references, empty success, and exposed failures. |
| `spec:product.application.pwa_interface.get_published_learning_unit` | Defines single-reference retrieval, availability results, complete content, attribution, and provenance exclusion. |
| `spec:product.ui.learning_flow` | Defines initial and replacement queue lifecycle, retry, state preservation, disposal, and outcome transitions. |
| `spec:product.ui.pages.main_page` | Owns initial queue retry and failure surfaces. |
| `spec:product.ui.pages.learning_page` | Owns retrieval and replacement queue retry or failure surfaces. |

### Completion verification

- `LearningUnitRef` is stable, opaque, comparable, and wire-format agnostic.
- Empty queue and `Unavailable` remain normal results.
- Selection-contract, mapping, and infrastructure failures remain distinct.
- Queue exhaustion and replacement context remain PWA-owned.
- Queue position, loaded content, and session change only after successful complete-unit loading.
- Available content includes learner-visible attribution and excludes provenance.
- No HTTP, JSON, framework, authentication, backend session, queue persistence, or durable progress decision entered the design.
- Application-interface and future transport-adapter test boundaries are explicit.
- Every normative specification change traces to accepted ADR authority.

### Review finding disposition

- F-MIN-01 was corrected by moving this work item through `in_progress` before closure.
- F-ADV-01 was adopted by extending `impact_refs` and `## Impact Scope` to the delivered ADRs and PWA-interface specs.
- F-ADV-02 through F-ADV-04 remain non-blocking and require no closure change.

### Validation

- Independent review reported `git diff --check` PASS with only Windows line-ending normalization warnings.
- Independent review reported no unexplained out-of-scope working-tree edits.
- Design Records MCP was not treated as PRODUCT validation authority because the active instance does not index this repository namespace.
- Filesystem inspection confirmed IDs, parent refs, metadata, required sections, and accepted ADR dates.

### Closure

- PRODUCT-WORK-APPLICATION-006 is complete.
- Transport mapping and PWA implementation planning may begin.
- PRODUCT-TASK-UI-001-02 may verify the reflected UI transitions and close its UI-owned coordination flow.

