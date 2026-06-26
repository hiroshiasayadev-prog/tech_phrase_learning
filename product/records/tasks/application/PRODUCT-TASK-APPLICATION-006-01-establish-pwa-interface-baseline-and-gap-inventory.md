# PRODUCT-TASK-APPLICATION-006-01: Establish PWA-interface baseline and gap inventory

- **id**: PRODUCT-TASK-APPLICATION-006-01
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-006
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 0.5d
- **depends_on**:
- **outputs**:

## Goal

Establish the authoritative PWA-facing application-interface baseline before any decision or specification change.

Classify every candidate interface gap by its correct owning artifact kind.

## Work

1. Read `prompt_chappy.md` and the shared Brewprint authoring standards.
2. Read PRODUCT-ADR-APPLICATION-003, PRODUCT-ADR-APPLICATION-004, and PRODUCT-ADR-UI-001 as current decision authority.
3. Treat superseded application ADRs as historical records only.
4. Read PRODUCT-WORK-APPLICATION-003, PRODUCT-WORK-APPLICATION-004, and PRODUCT-WORK-APPLICATION-005 with their final evidence.
5. Read the current application selection, retrieval, outbound-query, learning-unit, and UI specifications.
6. Inventory queue-creation request and result semantics visible to the PWA.
7. Inventory complete-unit retrieval request and result semantics visible to the PWA.
8. Inventory stable-reference, attribution, provenance, and content-completeness requirements.
9. Inventory empty-queue, queue-exhaustion, unavailable-reference, retry, and successful-replacement transitions.
10. Classify each topic as one of:
    - already decided by an accepted ADR;
    - already specified by a completed work item;
    - missing specification reflection;
    - genuinely unresolved normative decision;
    - implementation detail deferred from product design.
11. Determine whether invalid-request classification has accepted authority for each operation.
12. Determine whether retryability classification has accepted authority beyond UI-owned retry behavior.
13. Identify duplicated contracts and unclear ownership between application and UI specifications.
14. Identify the focused specification placement for the PWA-facing interface.
15. Do not modify specifications or create an ADR.

Use concrete runtime situations when explaining each candidate gap.

Do not infer HTTP routes, status codes, JSON fields, or client behavior from transport-independent semantics.

## Done condition

- Every required PWA-facing interface concern has one classification.
- Current authority is limited to accepted ADRs and current specifications.
- Completed selection, retrieval, and outbound-query semantics are not reopened.
- Genuine decision gaps are separated from missing specification reflection.
- Invalid-request and retryability questions have explicit authority judgments.
- Application-owned interface semantics remain separate from UI-owned transient state.
- Deferred transport and implementation details remain explicit.
- The proposed specification placement has a canonical-ref and ownership judgment.
- T006-02 can proceed without another conversation handoff.

## Verification

- Trace every already-decided claim to an accepted ADR.
- Trace every already-specified claim to a current specification.
- Confirm superseded ADRs are not used as current authority.
- Confirm no application or UI specification changed.
- Confirm no ADR was created.
- Confirm every proposed normative change is routed to T006-02.
- Confirm physical paths are not used as canonical refs.

## Evidence

### Result

- **Verdict**: PASS.
- The PWA-facing application-interface baseline and gap inventory is complete.
- Completed selection, retrieval, and outbound-query contracts remain fixed inputs.
- No application or UI specification changed in this task.
- No ADR was created in this task.
- Genuine normative gaps are routed to PRODUCT-TASK-APPLICATION-006-02.

### Current authority

| concern | current authority |
|---|---|
| Current published-content boundary, application use cases, availability-shaped retrieval, provenance exclusion, and technical-failure separation | PRODUCT-ADR-APPLICATION-003 |
| Result-shaped retrieval outbound port and persistence-adapter obligations | PRODUCT-ADR-APPLICATION-004 |
| PWA queue, loaded-unit, session, navigation, retry, and successful-replacement ownership | PRODUCT-ADR-UI-001 |
| Complete-shuffle selection policy and result validation | `spec:product.application.learning_unit_selection` |
| Complete-unit retrieval request and normal results | `spec:product.application.learning_unit_retrieval` |
| Complete learner-visible learning-unit meaning | `spec:product.learning.learning_unit` |
| PWA transitions and transient state | `spec:product.ui.learning_flow` |

PRODUCT-ADR-APPLICATION-001 and PRODUCT-ADR-APPLICATION-002 were treated as superseded historical records only.

### Classification inventory

| # | topic | classification | judgment |
|---|---|---|---|
| 1 | Queue-creation invalid request | Already specified by completed work. | The first-MVP PWA supplies no semantic request parameters. Queue creation has no application-level invalid-request result. Malformed transport input remains a future transport concern. |
| 2 | Retrieval invalid `LearningUnitRef` | Already decided and specified. | A well-formed reference with no current state returns `Unavailable`. A currently unavailable reference also returns `Unavailable`. A wire value that cannot become `LearningUnitRef` is rejected before application invocation by a future transport adapter. |
| 3 | Public technical-failure categories | Genuine unresolved normative decision. | The PWA-facing interface must expose `MappingFailure` and `InfrastructureFailure` as distinct categories with safe diagnostics. Current ADRs separate technical failures from normal results but do not authorize this public shape. |
| 4 | Retryability and category-specific PWA transitions | Genuine unresolved normative decision. | `InfrastructureFailure` is retryable. `MappingFailure` is non-retryable. Retrieval mapping failure ends the active flow and returns to main. Queue-creation mapping failure remains on main without automatic retry. Existing UI authority does not support this category-specific behavior. |
| 5 | Queue-creation failure boundary | Genuine unresolved normative decision. | `InvalidSelectionResult`, `MappingFailure`, and `InfrastructureFailure` remain distinct PWA-facing categories. `InvalidSelectionResult` is an outbound-contract violation, not an invalid PWA request. |
| 6 | PWA-facing `LearningUnitRef` guarantees | Partly specified and partly unresolved. | Stability is already specified. Opaque handling, equality comparison, and unchanged pass-through from queue creation to retrieval require accepted authority before normative reflection. Wire representation remains deferred. |
| 7 | Available-content completeness | Missing focused specification reflection. | `Available` returns one complete unit satisfying `spec:product.learning.learning_unit`. The interface must not redefine every learning-unit field. Partial content is not returned. |
| 8 | Attribution and provenance | Already decided; missing focused reflection. | Available content retains learner-visible attribution. The PWA-facing result excludes opaque provenance, availability metadata, and queue metadata. |
| 9 | Transition after `Unavailable` | Already decided and specified. | The PWA removes the unavailable pending reference and requests the next reference. The application processes one supplied reference and does not select the next candidate. |
| 10 | Queue exhaustion request boundary | Already decided and specified. | Initial acquisition and replacement acquisition use the same parameter-free `CreateCompleteShuffleQueue` operation. Initial or replacement context is not sent to the application. |
| 11 | Replacement state transition | Already decided and specified under UI ownership. | Queue position, loaded content, and session change only after successful complete-unit loading. The application interface owns the result, not the PWA state replacement. |
| 12 | Empty queue semantics | Already specified. | `Success([])` is a normal successful queue result. No separate `EmptyQueue` result category is introduced. |
| 13 | Focused specification owner | Specification placement judgment. | The PWA-facing interface belongs under `spec:product.application` as `spec:product.application.pwa_interface`. UI transitions remain under `spec:product.ui`. |
| 14 | Specification decomposition | Specification placement judgment. | Use one overview and two operation leaves: `spec:product.application.pwa_interface`, `spec:product.application.pwa_interface.create_complete_shuffle_queue`, and `spec:product.application.pwa_interface.get_published_learning_unit`. |
| 15 | Application and UI duplication boundary | Existing ownership plus unresolved transition changes. | Application specs own request, result, failure category, diagnostic, and retryability semantics. UI specs own retry count, displayed state, navigation, queue disposal, and session disposal. Category-specific UI transitions require new authority under item 4. |
| 16 | PWA-interface test boundary | Missing specification reflection. | Interface tests use application-use-case test doubles and verify exposed semantic categories, diagnostics, pass-through, attribution preservation, and provenance exclusion. They do not repeat use-case policy or persistence-adapter tests. |
| 17 | Future transport-adapter test boundary | Missing future verification reflection. | Transport-adapter tests verify wire-to-semantic mapping and result-category preservation. Concrete routes, methods, status codes, JSON fields, schemas, and client behavior remain deferred. |

### Required decision authority for T006-02

The user selected the following behavior during this baseline review.
The selections are not current normative authority until accepted ADRs record them.

Application decision authority is required for:

- distinct PWA-facing `InvalidSelectionResult`, `MappingFailure`, and `InfrastructureFailure` categories;
- safe diagnostic information on public technical and contract-violation failures;
- retryable `InfrastructureFailure` and non-retryable `MappingFailure` semantics;
- stable, opaque, equality-comparable `LearningUnitRef` values passed unchanged between queue creation and retrieval.

UI decision authority is required for:

- replacing uniform retry behavior with failure-category-specific transitions;
- ending the active learning flow after retrieval `MappingFailure`;
- discarding the queue and session before returning to main after retrieval `MappingFailure`;
- keeping queue-creation `MappingFailure` and `InvalidSelectionResult` on main without automatic retry;
- retaining automatic retry behavior for `InfrastructureFailure`;
- showing safe diagnostics at the owning failure surface.

T006-02 must record accepted authority before T006-03 treats these selections as normative contracts.

### Focused specification placement

```text
spec:product.application.pwa_interface
  +-- spec:product.application.pwa_interface.create_complete_shuffle_queue
  +-- spec:product.application.pwa_interface.get_published_learning_unit
```

The overview owns shared transport-independent interface rules.
The operation leaves own their PWA-facing request, normal-result, and failure contracts.
Existing selection and retrieval specs remain the semantic sources for application use-case behavior.
`spec:product.ui.learning_flow` remains the owner of transient state and result-driven transitions.

### Deferred details

- HTTP routes, methods, headers, and status codes
- JSON field names, schemas, and serialization formats
- Concrete exception, class, and programming-language result types
- Retry delays, backoff, timeout values, and client configuration
- Diagnostic stack traces and unsafe implementation details
- Frontend framework, state library, component implementation, and source layout
- Authentication, learner accounts, durable progress, and backend session identity

### Next-task input

- T006-02 must create accepted decision authority for the unresolved application and UI behavior above.
- T006-02 must not reopen completed queue, retrieval, outbound-query, attribution, provenance, or PWA state-ownership decisions.
- T006-03 may define the complete contract map only after the required authority is accepted.
- T006-04 owns specification creation and reflection.

### Verification

- Every reviewed PWA-facing concern has one classification.
- Every already-decided claim traces to an accepted ADR or current specification.
- Superseded ADRs were not used as current authority.
- Application-owned interface semantics remain separate from UI-owned transient state.
- No specification changed.
- No ADR was created.
- Physical paths were not used as canonical specification references.
- PRODUCT-WORK-APPLICATION-006 lists this task, and both records use PRODUCT-REQ-APPLICATION-001.
- Design Records MCP did not index this task, so filesystem fallback was used.
- A filesystem reread confirmed the final status and Evidence content.
- No Git or repository-wide validator result is claimed in this tool environment.
