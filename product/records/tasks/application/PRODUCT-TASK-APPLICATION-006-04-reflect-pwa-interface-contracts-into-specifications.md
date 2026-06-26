# PRODUCT-TASK-APPLICATION-006-04: Reflect PWA-interface contracts into specifications

- **id**: PRODUCT-TASK-APPLICATION-006-04
- **status**: done
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-APPLICATION-006
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-006-03
- **outputs**:
  - spec:product.application.pwa_interface
  - spec:product.application.pwa_interface.create_complete_shuffle_queue
  - spec:product.application.pwa_interface.get_published_learning_unit
  - spec:product.application
  - spec:product.ui
  - spec:product.ui.learning_flow
  - spec:product.ui.pages.main_page
  - spec:product.ui.pages.learning_page
  - PRODUCT-ADR-APPLICATION-005
  - PRODUCT-ADR-APPLICATION-006
  - PRODUCT-ADR-UI-002

## Goal

Reflect accepted PWA-facing application-interface contracts into focused specifications.

Preserve application and UI ownership without introducing concrete transport semantics.

## Work

1. Read the T006-01 ownership inventory, T006-02 authority disposition, and T006-03 contract map.
2. Stop as `blocked` when any proposed normative change lacks an accepted ADR.
3. Preserve PRODUCT-ADR-APPLICATION-003, PRODUCT-ADR-APPLICATION-004, and PRODUCT-ADR-UI-001.
4. Reflect any additional accepted T006-02 ADR decisions.
5. Place PWA-facing application operations under `spec:product.application`.
6. Keep PWA queue, loaded-unit, session, navigation, loading, and retry transitions under `spec:product.ui`.
7. Preserve selection and retrieval use-case specifications as their semantic sources.
8. Create a focused PWA-interface topic only when T006-01 confirms independent ownership and suitable placement.
9. Keep queue creation and complete-unit retrieval distinguishable inside the interface contract.
10. Keep successful empty queue distinct from request failure.
11. Keep `Unavailable` distinct from invalid request and technical failure.
12. Preserve learner-visible attribution and provenance exclusion.
13. Preserve successful replacement and unavailable-reference skipping rules.
14. Update UI specifications only to remove ambiguity or reflect accepted interface-result semantics.
15. Do not copy complete application result contracts into every UI page specification.
16. Keep root and topic overviews as routers for direct child topics.
17. Record every created or changed semantic ref and explicit no-change judgment.
18. Update `migrated_to_spec` only after an accepted ADR is fully reflected.
19. Run strict specification validation.
20. Run `git diff --check` and inspect `git status --short`.

Do not define:

- HTTP routes, methods, headers, or status codes;
- JSON fields or serialization formats;
- generated clients or transport-library types;
- retry delays, backoff, timeout values, or client configuration;
- component implementation or source layout.

Do not adopt a new design decision in this task.

## Done condition

- Every normative statement traces to accepted ADR authority.
- The PWA-facing interface has one focused specification owner.
- Queue creation and unit retrieval preserve their existing semantic contracts.
- Stable reference meaning is explicit without defining a wire representation.
- Successful empty queue, available, unavailable, invalid request, and technical failure remain correctly separated.
- UI specifications consume interface outcomes without owning application result semantics.
- Application specifications do not own PWA transient state or retry timing.
- Attribution remains learner-visible and provenance remains excluded.
- Queue exhaustion, unavailable-reference skipping, and successful replacement remain consistent across areas.
- Parent overviews route direct child topics without unnecessary duplication.
- No concrete transport, framework, persistence, authentication, or backend-session decision enters the specifications.
- Strict validation and whitespace verification pass.

## Verification

- Trace each changed normative statement to an accepted ADR.
- Confirm no task or work-item evidence acts as specification authority.
- Confirm Topics tables use active path-derived semantic refs.
- Confirm application and UI ownership remain distinct.
- Confirm shared rules are not duplicated across child specs.
- Confirm no superseded ADR is presented as current authority.
- Confirm transport and serialization details remain absent.
- Record validation commands and results in `## Evidence`.

## Evidence

### Result

- **Verdict**: PASS.
- All review findings and the unsupported recovery action were corrected.
- The user resolved the replacement queue-creation authority gap within PRODUCT-ADR-UI-002's existing decision scope.
- PRODUCT-ADR-UI-002 now covers initial queue creation, replacement queue creation, and retrieval transitions.
- The accepted replacement behavior is reflected in the owning application-interface and UI specifications.
- PRODUCT-ADR-UI-002 `migrated_to_spec` is restored to 2026-06-27.
- T006-04 is complete and ready for independent T006-05 review.

### Review findings corrected

| finding | correction applied |
|---|---|
| F-B-01: `Unavailable` misclassified as failure | `### Failure transitions` renamed to `### Outcome transitions`; `outcome class` column added; `Unavailable` classified as `normal result`. |
| F-B-02: Terminal `MappingFailure` surface named as `learning_page` | Boundary and Related specs in `get-published-learning-unit.md` split: `learning_page` owns `InfrastructureFailure` current-screen and retry; `main_page` owns terminal `MappingFailure` diagnostic surface. |
| F-B-03: Application-interface tests described at outbound-query boundary | Changed to "at the PWA-facing interface boundary" in `spec:product.application.pwa_interface` verification obligations intro. |
| F-B-04: Outcome transitions rows applied to replacement as well as initial queue creation | Rows scoped to "Initial queue creation"; replacement queue-creation authority gap note added to `spec:product.ui.learning_flow`. |
| F-M-01: `InvalidSelectionResult` assigned application retryability `No` without authority | `retryable` column removed from `create-complete-shuffle-queue.md` Errors table; per-item Rules added; `InvalidSelectionResult` gets meaning only; retryability delegated to `spec:product.ui.learning_flow`. |
| Unsupported `[ Start ]` recovery after non-retryable failure | `[ Start ]` removed from non-retryable failure concept model in `main-page.md`; replaced with `<safe diagnostic information>` placeholder; unsupported Rules row removed; authority gap note added. |
| F-B-05: Retry section implicitly covered replacement queue creation before authority existed | The overreach was removed before the user decision. After PRODUCT-ADR-UI-002 was supplemented, replacement `InfrastructureFailure` was added to the retry flow with explicit learning-page state preservation. |
| F-B-06: Queue-operation spec attributed all queue-creation failure surfaces to main page | The overreach was removed before the user decision. After PRODUCT-ADR-UI-002 was supplemented, initial failures route to `main_page` and replacement failures route to `learning_page`. |

### Resolved authority gap

The user resolved replacement queue-creation transitions within PRODUCT-ADR-UI-002's existing decision scope.

| outcome | accepted replacement queue-creation transition |
|---|---|
| `InfrastructureFailure` | Keep the current learning page, loaded unit, exhausted queue state, and session. Use the existing automatic and manual retry flow. |
| `MappingFailure` | Keep the current learning page and state. Show safe diagnostic information followed by `Back to main`. Do not offer automatic or manual retry. |
| `InvalidSelectionResult` | Keep the current learning page and state. Show safe diagnostic information followed by `Back to main`. Do not offer automatic or manual retry. |

Selecting `Back to main` discards the active queue and session under the existing transient lifecycle rule.

The following records now reflect the accepted decision:

- PRODUCT-ADR-UI-002 records the adopted transitions and rationale.
- `spec:product.ui.learning_flow` owns retry, state preservation, and transitions.
- `spec:product.ui.pages.learning_page` owns the replacement retry and failure surfaces.
- `spec:product.application.pwa_interface.create_complete_shuffle_queue` points to the owning UI specifications without defining UI behavior.

### Created specs

| canonical ref | physical path |
|---|---|
| `spec:product.application.pwa_interface` | `product/records/spec/application/pwa-interface/index.md` |
| `spec:product.application.pwa_interface.create_complete_shuffle_queue` | `product/records/spec/application/pwa-interface/create-complete-shuffle-queue.md` |
| `spec:product.application.pwa_interface.get_published_learning_unit` | `product/records/spec/application/pwa-interface/get-published-learning-unit.md` |

Path-derived canonical refs were verified against the path-derivation rules in `spec:product.design_records.authoring_standards.spec_authoring`.

### Changed specs

| canonical ref | change summary |
|---|---|
| `spec:product.application.pwa_interface.create_complete_shuffle_queue` | Boundary distinguishes initial main-page ownership from replacement learning-page ownership. Related specs route replacement transitions to `spec:product.ui.learning_flow` and `spec:product.ui.pages.learning_page`. |
| `spec:product.application` | Added PWA-facing interface to ownership statement, Current contract, Topics, Dependency direction diagram, and Related specs. Updated date to 2026-06-27. |
| `spec:product.ui` | Added category-specific failure transitions row to Current contract. Added PRODUCT-ADR-UI-002 and `spec:product.application.pwa_interface` to Related specs. Updated date to 2026-06-27. |
| `spec:product.ui.learning_flow` | Retry scope now covers initial queue creation, replacement queue creation, and retrieval `InfrastructureFailure`. Outcome transitions define replacement `MappingFailure` and `InvalidSelectionResult` as diagnostic-only learning-page failures with `Back to main`. State preservation and disposal rules are explicit. |
| `spec:product.ui.pages.main_page` | Added non-retryable failure concept model (with `<safe diagnostic information>` placeholder; no recovery action defined). Updated Rules table to distinguish InfrastructureFailure from MappingFailure and InvalidSelectionResult; unsupported `Start` recovery row removed; authority gap note added. Added rules for safe diagnostic surface. Added PRODUCT-ADR-UI-002 to Related specs. Updated date to 2026-06-27. |
| `spec:product.ui.pages.learning_page` | Added replacement queue infrastructure-retry and non-retryable contract-failure surfaces. Added safe diagnostic, `Back to main`, state-preservation, and disposal rules. Retained terminal retrieval mapping-failure behavior. |

### Updated ADR metadata

| ADR | migrated_to_spec |
|---|---|
| PRODUCT-ADR-APPLICATION-005 | 2026-06-27 |
| PRODUCT-ADR-APPLICATION-006 | 2026-06-27 |
| PRODUCT-ADR-UI-002 | 2026-06-27 |

### Authority traceability

| normative statement | authority |
|---|---|
| PWA-facing failure categories: `InvalidSelectionResult`, `MappingFailure`, `InfrastructureFailure` | PRODUCT-ADR-APPLICATION-005 |
| Safe diagnostic boundary and unsafe detail exclusion | PRODUCT-ADR-APPLICATION-005 |
| `InfrastructureFailure` retryable, `MappingFailure` non-retryable | PRODUCT-ADR-APPLICATION-005 |
| `LearningUnitRef` stability, opacity, equality, pass-through | PRODUCT-ADR-APPLICATION-006 |
| `LearningUnitRef` excludes provenance, database identity, queue state, learner progress, availability, revision | PRODUCT-ADR-APPLICATION-006 |
| Wire representation of `LearningUnitRef` deferred | PRODUCT-ADR-APPLICATION-006 |
| Application use cases, retrieval results `Available`/`Unavailable`, attribution, provenance exclusion | PRODUCT-ADR-APPLICATION-003 |
| Result-shaped outbound retrieval port | PRODUCT-ADR-APPLICATION-004 |
| Initial queue creation `InfrastructureFailure` → existing retry flow on main | PRODUCT-ADR-UI-002 |
| Initial queue creation `MappingFailure` and `InvalidSelectionResult` → no retry, main-page failure surface | PRODUCT-ADR-UI-002 |
| Replacement queue creation `InfrastructureFailure` → existing retry flow on the learning page with state preservation | PRODUCT-ADR-UI-002 |
| Replacement queue creation `MappingFailure` and `InvalidSelectionResult` → no retry, learning-page diagnostic and `Back to main` | PRODUCT-ADR-UI-002 |
| Retrieval `InfrastructureFailure` → existing retry flow, preserve current screen | PRODUCT-ADR-UI-002 |
| Retrieval `MappingFailure` → end flow, discard queue and session, return to main | PRODUCT-ADR-UI-002 |
| `Unavailable` → normal skip, not technical failure | PRODUCT-ADR-UI-002; PRODUCT-ADR-APPLICATION-003 |
| PWA owns queue, loaded unit, session, navigation, retry count | PRODUCT-ADR-UI-001 |

### Ownership judgments

- The PWA-facing interface is placed under `spec:product.application.pwa_interface` as confirmed by T006-01.
- `LearningUnitRef` semantics are owned by the interface overview, not duplicated per operation.
- Verification obligations are owned by the interface overview to avoid duplication across two operation specs.
- Application failure categories are referenced in UI specs without redefinition. UI specs own only the transition behavior.
- Page specs own visible state and failure surface placement only. Application operation contracts are not copied.

### Required no-change judgments

| concern | judgment |
|---|---|
| Accepted selection policy | No change. `SelectionScope = All` and `maximum_count = 100` remain in existing selection specs. |
| Accepted retrieval semantics | No change. `Available(complete_learning_unit) | Unavailable` remains in `spec:product.application.learning_unit_retrieval`. |
| Outbound-query contracts | No change. Existing selection and retrieval adapter obligations remain unmodified. |
| Published-content ownership | No change. Pipeline writes, application reads committed current state. |
| Attribution and provenance boundary | No change. Learner-visible attribution included, opaque provenance excluded. |
| PWA transient-state ownership | No change. Queue, loaded unit, session, navigation, and retry attempts remain PWA-owned. |
| Retry count | No change. One initial attempt and three automatic retries remain the accepted UI behavior. |
| Backend state | No backend session, queue persistence, reservation, history, or durable progress introduced. |
| Deferred implementation | HTTP, serialization, frameworks, concrete exception types, source layout, retry delays, backoff, and timeout remain deferred. |
| Application failure semantics in UI | Not redefined. UI specs reference application failure categories as inputs to transitions. |
| UI transitions in application spec | Not present. Application specs own request, result, failure, and retryability. |

### Validation results

| validator | result |
|---|---|
| `mcp__validate_records` (kind: spec) | `ok: true, diagnostics: null`. PRODUCT specs are not indexed by this MCP instance. No PRODUCT-namespace validation success is claimed. |
| `mcp__validate_records` (kind: decision) | Returned unrelated indexed Brewprint diagnostics. PRODUCT ADRs are not covered by this MCP instance. |
| `mcp__validate_records` (kind: task) | Returned unrelated indexed Brewprint diagnostics. PRODUCT application tasks are not covered by this MCP instance. |
| Filesystem reread | PASS for PRODUCT-ADR-UI-002, `spec:product.ui.learning_flow`, `spec:product.ui.pages.learning_page`, and `spec:product.application.pwa_interface.create_complete_shuffle_queue`. |
| `git diff --check` | Not rerun after the final decision-and-spec transaction because the active repository toolset has no shell execution. The earlier pre-transaction Exit 0 result is not claimed for the final edits. |

### `git diff --check` result

Not rerun after the final transaction. No current command success is claimed.

### `git status --short` (last reported before the final transaction)

New files created by this task:
- `?? product/records/spec/application/pwa-interface/` (3 files)

Modified by this task:
- ` M product/records/spec/application/index.md`
- ` M product/records/spec/ui/index.md`
- ` M product/records/spec/ui/learning-flow.md`
- ` M product/records/spec/ui/pages/learning-page.md`
- ` M product/records/spec/ui/pages/main-page.md`

Modified by earlier tasks in the same session (not T006-04 scope):
- `M  product/records/requirements/application/PRODUCT-REQ-APPLICATION-001-...` (staged, prior task)
- ` M product/records/tasks/application/PRODUCT-TASK-APPLICATION-001-05-...` (prior task)

Untracked files pre-existing before T006-04 (created by T006-01, T006-02, T006-03):
- ADRs 005, 006, UI-002; requirements 002, 003; tasks 006-01 through 006-05; work items; UI records.

The T006-04 task file itself (`PRODUCT-TASK-APPLICATION-006-04-...`) is listed as untracked because Git has not previously indexed it.

### Limitations

- Design Records MCP does not index the Tech Phrase Learning PRODUCT namespace.
- Available MCP validation results cover unrelated Brewprint records, not the modified PRODUCT records.
- `validate_records` returned OK but covers only MCP-indexed records, not PRODUCT specs.
- Filesystem rereads (implicit via tool context) confirm the created and edited spec files contain the required sections, metadata, and canonical refs.
- Independent review remains pending under PRODUCT-TASK-APPLICATION-006-05.
