# PRODUCT-TASK-APPLICATION-002-05: Review published-content and handoff design

- **id**: PRODUCT-TASK-APPLICATION-002-05
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-002
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 0.5d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-002-04
- **outputs**:

## Goal

Independently verify that the published-content and publication-handoff design is consistent and implementation-ready.

## Work

1. Use a reviewer who did not implement PRODUCT-TASK-APPLICATION-002-02 through PRODUCT-TASK-APPLICATION-002-04.
2. Review every impact ref from PRODUCT-WORK-APPLICATION-002.
3. Verify stable identity, current projection, availability separation, and lifecycle semantics.
4. Verify the publication handoff, validation precondition, writer ownership, and reader ownership.
5. Verify atomic replacement and consistency for concurrent application reads.
6. Verify opaque provenance reachability and learner-visible attribution.
7. Check application, pipeline, learning, and UI ownership for contradictions or duplication.
8. Check that no concrete persistence, transport, or framework decision entered the design scope.
9. Record findings by severity and give a final `PASS` or `NEEDS REVISION` verdict.
10. Re-run the review after any blocking finding is corrected.

Do not implement fixes during the independent review.

## Done condition

- The review covers every completion condition in PRODUCT-WORK-APPLICATION-002.
- Findings identify exact refs and conflicting claims.
- Blocking findings are corrected and independently re-reviewed.
- The final verdict is `PASS`.
- The evidence states whether implementation planning may begin for this module.

## Verification

- Confirm reviewer independence from T02 through T04 implementation.
- Trace every reviewed claim to a current ADR or specification.
- Confirm validation results for every modified specification.
- Confirm the final verdict and remaining non-blocking advisories are explicit.

## Evidence

### Reviewer independence

- The reviewer did not implement PRODUCT-TASK-APPLICATION-002-02 through PRODUCT-TASK-APPLICATION-002-04.
- The review used current ADR and specification files instead of relying on T04 conclusions.

### Verdict

- **Verdict**: NEEDS REVISION.
- Two blocking findings prevent a final `PASS` verdict.
- Implementation planning must not begin for this module until both findings are corrected and independently re-reviewed.

### Reviewed impact refs

- PRODUCT-ADR-APPLICATION-001
- PRODUCT-ADR-PIPELINE-001
- PRODUCT-ADR-PIPELINE-002
- PRODUCT-ADR-PIPELINE-004
- PRODUCT-ADR-PIPELINE-005
- `spec:product`
- `spec:product.application`
- `spec:product.application.published_content`
- `spec:product.pipeline`
- `spec:product.learning.learning_unit`
- `spec:product.ui.learning_flow`

The review also checked these directly related ownership records:

- PRODUCT-ADR-LEARNING-005
- PRODUCT-ADR-UI-001
- `spec:product.application.learning_unit_selection`

### Blocking findings

#### F-B-01: Withdrawal preconditions are not separated from publication preconditions

- **Severity**: Blocking.
- **Refs**: PRODUCT-TASK-APPLICATION-002-01 `## Evidence / Concern classification`; `spec:product.pipeline` `## Publication handoff`.
- T01 requires publication and republication preconditions to remain distinguishable from a withdrawal decision.
- `spec:product.pipeline` applies the complete unit, validation, model-judgment, provenance, and publication-judgment preconditions to all published-content mutation.
- The same specification defines withdrawal as an availability-only change that leaves content and provenance unchanged.
- The current wording does not state whether withdrawal requires a newly validated learning unit or only an existing current projection and withdrawal decision.
- The ambiguity prevents unambiguous publication, withdrawal, and republication transition semantics.

Required correction:

- Separate initial publication, replacement, and republication preconditions from availability-only withdrawal preconditions.
- State the withdrawal input, required existing state, and resulting observable state without introducing transport or persistence mechanisms.

#### F-B-02: Loaded-unit immutability has duplicated normative ownership

- **Severity**: Blocking.
- **Refs**: `spec:product.application` `## Current contract`; `spec:product.application.published_content` `### Loaded content`; `spec:product.application.learning_unit_selection` `### Retrieval and availability`; `spec:product.ui.learning_flow` `## Concept model` and `### Loading and replacement`.
- `spec:product.ui.learning_flow` owns the immutable loaded unit and replacement behavior.
- Application specifications repeat normative loaded-unit behavior despite routing that concern to the UI owner.
- `spec:product.application.published_content` also lists learner session state and loaded-content mutation as non-goals.
- The duplicated rules conflict with the work-item requirement that each contract have one clear semantic owner.

Required correction:

- Keep loaded-copy immutability and learner-flow replacement normative only in `spec:product.ui.learning_flow`.
- Keep application specifications limited to publication-state and retrieval-result semantics.
- Use references to the UI contract instead of repeated application-side requirements.

### Completion-condition coverage

| condition | result | evidence |
|---|---|---|
| Stable identity | PASS | PRODUCT-ADR-LEARNING-005 and `spec:product.learning.learning_unit` anchor identity to one valid learning path. |
| Four-element current projection | PASS | `spec:product.application.published_content` defines identity, complete learning unit, availability, and opaque provenance. |
| Content and availability separation | PASS | Application contracts retain content during unavailability and exclude unavailable units from normal retrieval. |
| Publication, withdrawal, replacement, and republication semantics | NEEDS REVISION | F-B-01 leaves withdrawal preconditions ambiguous. |
| Semantic handoff input | PASS | `spec:product.pipeline` defines one implementation-independent `PublicationHandoff`. |
| Validation and publication judgment | NEEDS REVISION | Publication preconditions are explicit, but their scope incorrectly includes or ambiguously includes withdrawal. |
| Atomic replacement | PASS | Content, matching provenance, and resulting availability switch as one observable state. |
| Concurrent-read consistency | PASS | Reads observe no projection or one complete projection for initial publication, and the previous or new complete projection for replacement. |
| Opaque provenance reachability | PASS | Application logic treats provenance as opaque while current pipeline evidence remains reachable. |
| Learner-visible attribution | PASS | Attribution remains inside the complete learning unit and does not require pipeline traversal during normal retrieval. |
| Pipeline writer and application reader ownership | PASS | The pipeline owns writes and the application reads only the published projection. |
| Cross-area ownership | NEEDS REVISION | F-B-02 duplicates loaded-unit behavior across application and UI specifications. |
| Implementation independence | PASS | No database, transaction, transport, command, event, or framework mechanism is selected. |

### Validation

- T04 evidence records strict repository-local validation of all 20 specification files after its edits.
- T04 evidence also records a clean `git diff --check` after its edits.
- Design Records MCP validation was not accepted as evidence because the active MCP index targets another repository.
- This review modified no specification or ADR file.
- No specification fix was implemented during this independent review.

### Re-review gate

A final review must confirm:

- F-B-01 is closed by explicit operation-specific preconditions.
- F-B-02 is closed by single ownership of loaded-unit behavior.
- Specification validation still passes after the corrections.
- The final verdict is `PASS` before implementation planning begins.

### Final independent re-review

- **Verdict**: PASS.
- F-B-01 is CLOSED.
- F-B-02 is CLOSED.
- No new blocking finding was found.
- Implementation planning may begin for this module.
- PRODUCT-WORK-APPLICATION-002 may proceed to completion review.
- PRODUCT-WORK-APPLICATION-002 status was not changed by this re-review.

### Previous finding closure

| finding | result | evidence |
|---|---|---|
| F-B-01 | CLOSED | `spec:product.pipeline` now separates `PublicationHandoff` from `AvailabilityChange`. |
| F-B-01 | CLOSED | Initial publication and content replacement use `PublicationHandoff` preconditions. |
| F-B-01 | CLOSED | Availability-only changes require an existing current projection and a pipeline-owned decision. |
| F-B-01 | CLOSED | Availability-only changes do not require a new complete learning unit or new provenance. |
| F-B-01 | CLOSED | Availability-only changes leave current content and current provenance unchanged. |
| F-B-01 | CLOSED | Republication with new content and availability-only restoration are distinct operations. |
| F-B-01 | CLOSED | Failed preconditions produce no partial mutation for either operation type. |
| F-B-02 | CLOSED | Loaded-unit immutability is normatively owned by `spec:product.ui.learning_flow`. |
| F-B-02 | CLOSED | `spec:product.application` no longer contains a loaded-content ownership row. |
| F-B-02 | CLOSED | `spec:product.application.published_content` references the UI owner instead of redefining behavior. |
| F-B-02 | CLOSED | `spec:product.application.learning_unit_selection` no longer defines active PWA session immutability. |

### Critical findings

None.

### Non-critical findings

- The `product/src/tools/validate_spec.py` path named in the review prompt is not present in this checkout.
- The shared Brewprint `validate_spec.py` tool was run against this repository's current `product/records/spec` tree.
- `git diff --check` reported CRLF conversion warnings only and no whitespace errors.

### Final completion-condition coverage

| condition | result | evidence |
|---|---|---|
| Stable learning-unit identity | PASS | PRODUCT-ADR-LEARNING-005 and `spec:product.learning.learning_unit` anchor identity to one valid learning path. |
| Four-element current projection | PASS | `spec:product.application.published_content` defines identity, complete learning unit, availability, and opaque provenance. |
| Separation of current content and availability | PASS | Availability is separate from content and unavailability retains current content. |
| Initial publication semantics | PASS | `spec:product.pipeline` defines `PublicationHandoff` for initial publication. |
| Content replacement semantics | PASS | Replacement switches content, matching provenance, and resulting availability together. |
| Withdrawal semantics | PASS | `AvailabilityChange` changes only availability for an existing current projection. |
| Republication or availability restoration semantics | PASS | New content uses `PublicationHandoff`; restoration without content change uses `AvailabilityChange`. |
| Semantic pipeline handoff | PASS | `PublicationHandoff` and `AvailabilityChange` are semantic inputs, not transport or storage contracts. |
| Validation and publication-judgment preconditions | PASS | Complete-unit validation is scoped to `PublicationHandoff`; availability-only changes have separate preconditions. |
| Atomic replacement | PASS | Application reads cannot observe mixed content, provenance, or availability for replacement. |
| Availability-only atomic state change | PASS | Availability-only changes produce one observable state transition. |
| Concurrent-read consistency | PASS | Reads observe no projection or one complete projection for initial publication, and previous or new complete projection for replacement. |
| Opaque provenance reachability | PASS | Application logic treats provenance as opaque while current pipeline-owned evidence remains reachable. |
| Learner-visible attribution | PASS | Attribution remains inside the complete learning unit. |
| Pipeline writer ownership | PASS | The pipeline is the only semantic owner of published-content writes. |
| Application reader ownership | PASS | The application reads only the published-content projection. |
| Learning, pipeline, application, and UI ownership | PASS | Application specs reference UI-owned loaded-copy behavior instead of redefining it. |
| Current-only retention | PASS | PRODUCT-ADR-PIPELINE-005 and `spec:product.pipeline` exclude historical source snapshots, intermediate generations, previous publications, exact replay, and rollback. |
| No runtime revision-history requirement | PASS | `spec:product.application.published_content` excludes runtime revision history and rollback. |
| No persistence, transport, transaction, or framework decision | PASS | The corrected specs defer database, transaction, HTTP, framework, command, and event mechanisms. |

### Final validation results

Strict specification validation was run with the available shared validator:

```text
python -X utf8 C:\Users\imved\projects\brewprint\product\src\tools\validate_spec.py product/records/spec --strict --no-color
[strict]  All 20 file(s) OK.
```

The prompt-requested repository-local path was checked and is absent:

```text
python -X utf8 product/src/tools/validate_spec.py product/records/spec --strict --no-color
can't open file 'C:\Users\imved\projects\tech_phrase_learning\product\src\tools\validate_spec.py': [Errno 2] No such file or directory
```

`git diff --check` produced no whitespace errors.
The command printed CRLF conversion warnings for existing changed files.

`git status --short` confirmed the expected dirty working tree with modified ADR, specification, requirement, task, work-item, and protocol files.
It also confirmed the untracked PRODUCT-TASK-APPLICATION-002 task chain and PRODUCT-WORK-APPLICATION-002 records remain untracked in the current checkout.
