# PRODUCT-TASK-APPLICATION-001-06: Integrate and review application design

- **id**: PRODUCT-TASK-APPLICATION-001-06
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-001
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 2d
- **depends_on**: [PRODUCT-TASK-APPLICATION-001-04, PRODUCT-TASK-APPLICATION-001-05]
- **outputs**:
  - PRODUCT-REQ-APPLICATION-001
  - PRODUCT-WORK-APPLICATION-001
  - spec:product.ui.components
  - spec:product.ui.components.operation_feedback
  - spec:product.ui.pages

## Goal

Integrate the focused module designs and determine whether application design is ready for implementation planning.

## Work

1. Read PRODUCT-WORK-APPLICATION-001 and the child work items recorded by T01 through T05.
2. Require each child work item to be `done` or explicitly deferred with a non-blocking reason.
3. Read all ADRs and specs created or changed by the child work items.
4. Build one cross-module ownership and dependency check.
5. Reconcile duplicated or contradictory contracts only when an accepted ADR authorizes the normative change.
6. Stop and create decision follow-up work when an accepted ADR is missing.
7. Confirm that unresolved implementation choices remain outside the specification boundary.
8. Request an independent review of the integrated application design.
9. Apply specification corrections only from accepted ADRs or create follow-up work items for unresolved gaps.
10. Record implementation work-item candidates without starting implementation.
11. Update PRODUCT-WORK-APPLICATION-001 evidence and completion state when all conditions are satisfied.

Required integration checks:

- Pipeline owns publication decisions and published-area writes.
- Application reads only the published-content boundary.
- Published content and availability remain separate.
- Published-content changes commit one complete current state transactionally.
- Application provenance remains opaque.
- Queue creation returns at most 100 unique available references.
- Queue generation creates no reservation or backend queue state.
- Retrieval rechecks current availability.
- `Unavailable` remains distinct from mapping, infrastructure, and retryable failures.
- The PWA owns queue position and learner session state.
- Loaded content is not revoked from an active learner flow.
- Ports are application-owned and implemented by adapters.
- Application domain rules remain independent from frameworks and persistence.

Implementation-planning output categories:

- application domain and use cases;
- published-content writer on the pipeline side;
- persistence adapters and storage model;
- PWA-facing transport adapter;
- PWA integration;
- architecture, contract, and integration tests.

## Done condition

- Every focused module work item is resolved or explicitly deferred without blocking implementation planning.
- Application, pipeline, learning, and UI specs contain consistent ownership and result semantics.
- All normative specification changes trace to accepted ADRs.
- No task or work-item evidence acts as design authority.
- An independent review records `PASS` or all blocking findings are resolved.
- PRODUCT-REQ-APPLICATION-001 required outcomes are satisfied at the design level.
- Implementation work-item candidates are recorded separately from this design hub.
- PRODUCT-WORK-APPLICATION-001 contains final evidence and can be marked `done`.

## Verification

- Validate H1, metadata, canonical refs, reciprocal workflow links, and required sections for all new records.
- Review cross-area dependency direction against `spec:product` and PRODUCT-ADR-APPLICATION-003.
- Confirm superseded ADR bodies remain historical and unchanged except for lifecycle status.
- Check that no detailed design depends on pipeline internal artifact structures.
- Check that no implementation progress or concrete technology choice was placed in an ADR or spec without a dedicated decision.
- Record the independent review verdict and addressed findings in `## Evidence`.

## Evidence

### Result

- **Verdict**: PASS.
- PRODUCT-WORK-APPLICATION-002 through PRODUCT-WORK-APPLICATION-006 are complete.
- PRODUCT-WORK-UI-001 and PRODUCT-TASK-UI-001-02 are complete.
- The first independent integrated review reported no blocking finding and three major findings.
- M1 and M2 were corrected under PRODUCT-ADR-APPLICATION-005 and PRODUCT-ADR-UI-002.
- M3 was closed by the required working-tree, whitespace, strict-specification, and scoped-diff validation.
- The independent re-review recorded `PASS` with no remaining findings.
- Implementation planning readiness is `ready`.
- PRODUCT-REQ-APPLICATION-001 required outcomes are satisfied at the design level.
- PRODUCT-WORK-APPLICATION-001 has final evidence and is closed with this task.

### Child work-item completion

| work item | status | final review verdict | blocking findings | implementation readiness | integration notes |
|---|---|---|---|---|---|
| PRODUCT-WORK-APPLICATION-002 | done | PASS | none | ready | Published state, publication handoff, availability changes, and ownership boundaries are complete. |
| PRODUCT-WORK-APPLICATION-003 | done | PASS | none | ready | Complete-shuffle scope, cardinality, ordering, and validation contracts are complete. |
| PRODUCT-WORK-APPLICATION-004 | done | PASS | none | ready | Availability-shaped retrieval and result-shaped outbound retrieval are complete. |
| PRODUCT-WORK-APPLICATION-005 | done | PASS | none | ready | Application-owned outbound query ports and adapter verification boundaries are complete. |
| PRODUCT-WORK-APPLICATION-006 | done | PASS | none | ready | PWA-facing request, result, failure, and stable-reference contracts are complete. |

### Cross-module contract matrix

| concern | semantic owner | accepted ADR | current spec | upstream dependency | downstream consumer | result |
|---|---|---|---|---|---|---|
| Current published state and publication ownership | Pipeline owns decisions and writes. Application owns committed runtime reads. | PRODUCT-ADR-APPLICATION-003; PRODUCT-ADR-PIPELINE-005 | `spec:product.pipeline`; `spec:product.application.published_content`; `spec:product.application.published_content.current_state`; `spec:product.application.published_content.publication_handoff` | `spec:product.learning.learning_unit` | Selection and retrieval adapters | consistent |
| Current availability | Pipeline owns the decision. Application owns runtime interpretation. | PRODUCT-ADR-APPLICATION-003; PRODUCT-ADR-PIPELINE-005 | `spec:product.application.published_content.availability`; `spec:product.pipeline` | Current published state | Selection, retrieval, and UI skip behavior | consistent |
| Complete-shuffle selection | Application | PRODUCT-ADR-APPLICATION-003 | `spec:product.application.learning_unit_selection`; `spec:product.application.learning_unit_selection.selection_scope`; `spec:product.application.learning_unit_selection.queue_contract`; `spec:product.application.learning_unit_selection.result_validation`; `spec:product.application.learning_unit_selection.create_complete_shuffle_queue` | Current availability | PWA queue state | consistent |
| Published learning-unit retrieval | Application | PRODUCT-ADR-APPLICATION-003; PRODUCT-ADR-APPLICATION-004 | `spec:product.application.learning_unit_retrieval`; `spec:product.application.outbound_queries.get_published_learning_unit` | Committed current state and learning-unit semantics | PWA-facing retrieval | consistent |
| Outbound query ports | Application | PRODUCT-ADR-APPLICATION-003; PRODUCT-ADR-APPLICATION-004 | `spec:product.application.outbound_queries`; `spec:product.application.outbound_queries.select_learning_unit_refs`; `spec:product.application.outbound_queries.get_published_learning_unit` | Application use-case needs | Persistence adapters | consistent |
| PWA-facing interface and reference semantics | Application | PRODUCT-ADR-APPLICATION-005; PRODUCT-ADR-APPLICATION-006 | `spec:product.application.pwa_interface`; `spec:product.application.pwa_interface.create_complete_shuffle_queue`; `spec:product.application.pwa_interface.get_published_learning_unit` | Application use cases | PWA | consistent |
| PWA lifecycle and failure transitions | UI | PRODUCT-ADR-UI-001; PRODUCT-ADR-UI-002 | `spec:product.ui`; `spec:product.ui.learning_flow`; `spec:product.ui.pages`; `spec:product.ui.pages.main_page`; `spec:product.ui.pages.learning_page`; `spec:product.ui.components`; `spec:product.ui.components.operation_feedback` | PWA-facing outcomes | Learner-visible flow | consistent after correction and independent PASS |
| Complete learning-unit meaning and attribution | Learning | PRODUCT-ADR-LEARNING-005 | `spec:product.learning`; `spec:product.learning.learning_unit` | Authentic source evidence | Pipeline publication, application retrieval, and UI presentation | consistent |
| Cross-area dependency direction | Root specification | PRODUCT-ADR-APPLICATION-003; PRODUCT-ADR-PIPELINE-005; PRODUCT-ADR-UI-001 | `spec:product`; `spec:product.application`; `spec:product.pipeline`; `spec:product.learning`; `spec:product.ui` | Area contracts | Whole product architecture | consistent |

### Ownership and dependency direction

- Pipeline may depend on learning semantics.
- Learning has no normative dependency on pipeline or UI implementation.
- Pipeline owns validation, publication decisions, availability decisions, and published-content writes.
- Application reads only committed published content.
- Application does not consume pipeline intermediate artifacts.
- Application may depend on learning-unit semantics.
- Persistence adapters depend on application-owned outbound query contracts.
- UI depends on application interfaces and learning semantics.
- UI does not consume pipeline internals.
- PWA queue position, loaded content, session state, retry attempts, navigation, and disposal remain UI-owned.

### Integrated contract results

- Current content and runtime availability remain separate concepts.
- Publication and replacement expose one complete observable current state.
- Availability-only changes preserve current content and current provenance.
- Current provenance remains opaque to application logic.
- First-MVP retention remains current-only.
- Runtime revision history, exact replay, and rollback remain excluded.
- `SelectionScope = All` remains the first-MVP policy.
- `maximum_count = 100` remains application policy.
- Queue size remains `min(maximum_count, eligible_count)`.
- Queue results remain unique within one queue and may repeat across later queues.
- Returned order remains randomized and preserved.
- `eligible_count` remains semantic only and is not returned.
- Selection creates no reservation, backend queue identity, backend position, or backend history.
- Application validation remains limited to observable returned-array properties.
- Invalid observable selection results are rejected without normalization.
- Retrieval accepts exactly one `LearningUnitRef`.
- Normal retrieval remains `Available(complete_learning_unit) | Unavailable`.
- Missing and currently unavailable references both map to `Unavailable`.
- Mapping and infrastructure failures remain outside normal results.
- Available content includes learner-visible attribution and excludes provenance.
- Selection and retrieval remain distinct operations.
- Queue creation and retrieval remain separate PWA-facing operations.
- `LearningUnitRef` remains stable, opaque, equality-comparable, unchanged through pass-through, and wire-format agnostic.
- `Success([])` and `Unavailable` remain normal results.
- Application failure categories and safe diagnostic meaning remain distinct from UI transitions.
- One initial attempt and three automatic retries apply only to `InfrastructureFailure`.
- Manual Retry remains available only after exhausted `InfrastructureFailure` attempts.
- Initial non-retryable queue failures remain on the main page.
- Replacement non-retryable queue failures preserve the learning page and expose `Back to main`.
- Retrieval `MappingFailure` ends the flow and discards queue and session state.
- `Unavailable` removes only the affected pending reference.
- Queue position, loaded content, and session change only after successful complete-unit loading.
- Empty queue remains a normal success and does not enter failure handling.

### Requirement consistency

| required outcome | result |
|---|---|
| Each major module has a focused design work item. | satisfied |
| Architectural judgment is recorded in ADRs. | satisfied |
| Current contracts are reflected across application, pipeline, learning, and UI specs. | satisfied |
| Cross-module dependencies and result semantics are consistent. | satisfied |
| Implementation work can be planned without reopening application ownership. | satisfied |
| Concrete frameworks, schemas, SQL, HTTP routes, and source layouts remain deferred. | satisfied |

PRODUCT-REQ-APPLICATION-001 remains `accepted`.
The requirement was not closed.

### Corrections

- PRODUCT-REQ-APPLICATION-001: Corrected two stale Evidence sentences from present-tense deferral to historical wording.
- `spec:product.ui.components.operation_feedback`: Restricted automatic and manual retry feedback to `InfrastructureFailure`.
- `spec:product.ui.components.operation_feedback`: Added distinct initial, replacement, and retrieval non-retryable failure surfaces.
- `spec:product.ui.components.operation_feedback`: Updated failure authority to `spec:product.application.pwa_interface`.
- `spec:product.ui.components`: Replaced generic `error + Retry` wording with category-specific operation feedback.
- `spec:product.ui.pages`: Added retrieval `MappingFailure` and replacement `Success([])` terminal transitions.
- ADR corrections: none.
- PRODUCT-ADR-UI-001 retains one previously reported stale historical consequence statement.
- The stale consequence does not reverse the accepted UI state-ownership decision.
- The accepted ADR was not edited.

### Implementation work-item candidates

| candidate | owned scope | dependency | excluded decision |
|---|---|---|---|
| Application domain and use cases | Implement queue creation, retrieval orchestration, semantic results, and observable selection validation. | `spec:product.application.learning_unit_selection`; `spec:product.application.learning_unit_retrieval`; outbound query contracts | Persistence technology, transport mapping, UI state, and source layout. |
| Pipeline published-content writer | Implement `PublicationHandoff`, `AvailabilityChange`, validation gates, and complete observable current-state mutation. | `spec:product.pipeline`; `spec:product.application.published_content` | Runtime selection, PWA lifecycle, and transport contracts. |
| Persistence storage model and adapters | Implement current-state persistence and both application-owned outbound queries. | Published-content writer contract; `spec:product.application.outbound_queries` | PWA transport, UI transitions, and pipeline generation logic. |
| PWA-facing transport adapter | Map transport inputs and outputs while preserving operation, result, failure, diagnostic, and reference semantics. | `spec:product.application.pwa_interface` | New application semantics, UI navigation, and persistence policy. |
| PWA integration | Implement queue, loaded-unit, session, retry, navigation, disposal, and failure-surface behavior. | `spec:product.ui.learning_flow`; PWA-facing application interface | Backend queue state, durable learner progress, and application failure meaning. |
| Architecture and contract tests | Verify dependency direction, outbound adapter contracts, application-interface behavior, and unsafe-detail exclusion. | Implemented application, pipeline writer, persistence adapters, and transport adapter | End-to-end learner-flow acceptance coverage. |
| Integration and end-to-end tests | Verify publication-to-selection-to-retrieval-to-PWA flows and failure transitions. | All implementation candidates above | Replacing module-level unit and contract tests. |

No implementation work item was created.
No implementation work began.

### Independent review

- Reviewer: independent review session supplied by the user.
- Independence: the reviewer did not implement this integration or its corrections.
- Initial verdict: `NEEDS REVISION`.
- Final re-review verdict: `PASS`.
- Remaining findings: none.
- Implementation planning readiness: ready.
- T001-06 closure readiness: ready.

| finding | final disposition |
|---|---|
| M1: `spec:product.ui.components.operation_feedback` and `spec:product.ui.components` treated every request failure as retryable. | CLOSED. Retry UI applies only to `InfrastructureFailure`; non-retryable initial, replacement, and retrieval surfaces match accepted authority. |
| M2: `spec:product.ui.pages` limited learning-page exit to learner-selected `Back to main`. | CLOSED. Retrieval `MappingFailure` and replacement `Success([])` terminal transitions are explicit and consistent. |
| M3: strict validation, `git diff --check`, `git status --short`, and scoped diff inspection were not executed. | CLOSED. The required commands were executed; strict validation passed all 34 specification files, no whitespace error was reported, and the scoped diff contained only the six expected records. |
| A1: PRODUCT-ADR-UI-001 contains stale historical Consequences wording. | Non-blocking advisory. Current authority and implementation readiness are unaffected. |
| A2: Some child completion Evidence uses stale superseded-ADR wording. | Non-blocking editorial advisory. Evidence is not used as normative authority. |

- All blocking and major findings are resolved.
- The accepted ADR set was not modified.
- This task is complete.

### Validation

- Filesystem rereads confirmed focused work-item and UI dependency statuses.
- Filesystem rereads confirmed current ADR status and supersession chains for the reviewed authority set.
- Filesystem rereads confirmed canonical specification refs and cross-area ownership statements.
- Filesystem rereads confirmed the M1 and M2 corrections against PRODUCT-ADR-APPLICATION-005, PRODUCT-ADR-UI-002, and `spec:product.ui.learning_flow`.
- Design Records MCP was not treated as PRODUCT validation authority because the active instance is not confirmed to index this repository namespace.
- `git status --short` reported exactly six modified records:
  - PRODUCT-REQ-APPLICATION-001;
  - `spec:product.ui.components`;
  - `spec:product.ui.components.operation_feedback`;
  - `spec:product.ui.pages`;
  - PRODUCT-TASK-APPLICATION-001-06;
  - PRODUCT-WORK-APPLICATION-001.
- `git diff --check` reported no whitespace error.
- Strict specification validation reported `[strict]  All 34 file(s) OK.`
- Scoped diff inspection showed only the expected requirement, task, work-item, and UI specification corrections.
- Scoped diff inspection showed no ADR changes.
- The PRODUCT-REQ-APPLICATION-001 change only converts stale present-tense Evidence wording into historical wording.
- LF-to-CRLF working-copy warnings were emitted for the six modified records. They do not indicate specification or whitespace validation failure.
- M3 is closed.
- No commit or staging operation was performed.
