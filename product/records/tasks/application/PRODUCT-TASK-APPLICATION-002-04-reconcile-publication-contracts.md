# PRODUCT-TASK-APPLICATION-002-04: Reconcile publication contracts

- **id**: PRODUCT-TASK-APPLICATION-002-04
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-002
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 0.5d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-002-03
- **outputs**:
  - PRODUCT-ADR-PIPELINE-001
  - PRODUCT-ADR-PIPELINE-002
  - PRODUCT-ADR-PIPELINE-004
  - PRODUCT-ADR-PIPELINE-005
  - PRODUCT-ADR-APPLICATION-001
  - spec:product
  - spec:product.application
  - spec:product.application.published_content
  - spec:product.pipeline
  - spec:product.learning.learning_unit

## Goal

Reflect the T02 and T03 design results across affected ADRs and specifications without duplicating ownership.

## Work

1. Read the completed evidence from PRODUCT-TASK-APPLICATION-002-01 through PRODUCT-TASK-APPLICATION-002-03.
2. Treat publication-related ADR and specification edits already present in the working tree as candidate reflection work.
3. Verify that PRODUCT-ADR-PIPELINE-005 records the source-reuse and retention decision exposed by T03.
4. Confirm that PRODUCT-ADR-PIPELINE-005 supersedes PRODUCT-ADR-PIPELINE-001 and PRODUCT-ADR-PIPELINE-004 without dropping their active pipeline decisions.
5. Reconcile PRODUCT-ADR-APPLICATION-001 with PRODUCT-ADR-PIPELINE-005 and current-only provenance ownership.
6. Reflect the four-element published projection and its invariants in `spec:product.application.published_content`.
7. Reflect the semantic publication handoff and pipeline writer obligations in `spec:product.pipeline`.
8. Keep attribution meaning owned by `spec:product.learning.learning_unit` and remove projection-level duplication.
9. Preserve loaded-content immutability as UI-owned behavior in `spec:product.ui.learning_flow`.
10. Update `spec:product` and `spec:product.application` routing only when current decision or topic refs changed.
11. Remove contradictory, stale, historical-retention, or duplicated normative statements.
12. Preserve implementation exclusions for persistence, transport, framework, exact replay, and rollback details.
13. Update ADR `migrated_to_spec` dates when the changed decision meaning is fully reflected in current specifications.
14. Record exact changed refs and explicit no-change judgments in `## Evidence`.

Do not adopt a new design decision in this task.
Report any unresolved decision as a blocker instead of resolving it inside specification edits.

## Done condition

- Every T02 and T03 result is reflected in one owning ADR or specification.
- Each contract has one clear semantic owner.
- Application and pipeline specifications describe compatible sides of the publication boundary.
- The published projection contains identity, complete learning unit, availability, and opaque provenance reference.
- Attribution is not redefined independently from the complete learning unit.
- Historical source snapshots, intermediate generations, previous publications, exact replay, and rollback are not first-MVP requirements.
- Learning attribution and unavailability rules remain compatible with the published projection.
- UI loaded-content behavior remains compatible with withdrawal and replacement.
- PRODUCT-ADR-PIPELINE-001 and PRODUCT-ADR-PIPELINE-004 are superseded by PRODUCT-ADR-PIPELINE-005.
- Accepted ADRs and current specifications do not conflict.
- ADR `migrated_to_spec` metadata matches the reflected decision state.
- No unresolved ownership ambiguity remains within PRODUCT-WORK-APPLICATION-002 scope.
- Concrete implementation choices remain deferred.

## Verification

- Review all `impact_refs` from PRODUCT-WORK-APPLICATION-002.
- Trace every T02 and T03 evidence statement to one owning specification or accepted ADR.
- Search affected records for stale multiplicity, source-snapshot, intermediate-history, revision-history, and duplicated-attribution language.
- Confirm that no specification text becomes the source of a new unrecorded architecture decision.
- Confirm supersession links, canonical references, ADR metadata, and topic routing after edits.
- Run available validation for affected PRODUCT ADRs, specifications, and workflow records.
- Show `git diff --check` and `git status --short` in `## Evidence`.

## Evidence

### Result

- **Semantic verdict**: PASS.
- T02 and T03 results are reflected across the owning ADRs and specifications.
- PRODUCT-ADR-PIPELINE-005 records the source-reuse and current-only retention decision.
- PRODUCT-ADR-PIPELINE-005 supersedes PRODUCT-ADR-PIPELINE-001 and PRODUCT-ADR-PIPELINE-004.
- Repository-local validation and Git checks passed.

### Changed ADRs

| ref | reflected contract |
|---|---|
| PRODUCT-ADR-PIPELINE-001 | Status changed to `superseded`. Its deterministic-stage decision is carried forward by PRODUCT-ADR-PIPELINE-005. |
| PRODUCT-ADR-PIPELINE-002 | Dependency now points to PRODUCT-ADR-PIPELINE-005 instead of the superseded PRODUCT-ADR-PIPELINE-001. |
| PRODUCT-ADR-PIPELINE-004 | Status changed to `superseded`. Its path, cardinality, and publication-gate decisions are carried forward by PRODUCT-ADR-PIPELINE-005. |
| PRODUCT-ADR-PIPELINE-005 | Accepted current pipeline decision for staged processing, path generation, publication gating, source reuse, and current-only retention. `migrated_to_spec` is `2026-06-26`. |
| PRODUCT-ADR-APPLICATION-001 | Dependency and evidence references now point to PRODUCT-ADR-PIPELINE-005. |

### Changed specifications

| ref | reflected contract |
|---|---|
| `spec:product` | Routes the current pipeline architecture to PRODUCT-ADR-PIPELINE-005. |
| `spec:product.application` | The current runtime projection contains identity, complete learning unit, availability, and opaque provenance. Pipeline isolation now refers to processing data instead of historical artifact structures. |
| `spec:product.application.published_content` | Defines the four-element projection. Removes independent attribution duplication. Defines unavailable retrieval, publication-judged replacement availability, and availability-only invariants. |
| `spec:product.pipeline` | Defines the semantic `PublicationHandoff`, its preconditions, pipeline writer obligations, source reuse, and current-only retention boundary. |
| `spec:product.learning.learning_unit` | Keeps source evidence and attribution as learning-owned semantics. Published-content retention and provenance are delegated to application and pipeline specifications. |

### Explicit no-change judgment

- `spec:product.ui.learning_flow` already defines loaded learning content as immutable.
- Its loading and replacement rules already preserve the current screen until a new unit loads successfully.
- No UI specification change was required.

### Ownership result

| concern | owner |
|---|---|
| Learning-unit composition and attribution meaning | `spec:product.learning.learning_unit` |
| Generation, validation, publication judgment, semantic handoff, and writes | `spec:product.pipeline` |
| Current published projection, availability-aware reads, and opaque provenance handling | `spec:product.application.published_content` |
| Loaded-copy immutability and learner-flow replacement | `spec:product.ui.learning_flow` |

### Stale-language review

- No active contract retains one-path-to-many-learning-unit semantics.
- No active contract requires historical source snapshots, historical intermediate generations, previous publication revisions, exact replay, or rollback.
- Superseded ADRs retain the earlier retention decisions as history.
- PRODUCT-ADR-PIPELINE-005 and current specifications own the replacement contract.
- Attribution is no longer represented as a separate published-projection element.
- Application contracts do not require pipeline processing-data interpretation.

### Manual format and reference checks

- Affected ADR H1 values, IDs, statuses, dates, dependency fields, and `migrated_to_spec` values remain well-formed by inspection.
- Affected specification IDs still match their existing paths.
- Specification parent refs and related refs remain canonical `spec:` refs.
- PRODUCT-WORK-APPLICATION-002 includes PRODUCT-ADR-PIPELINE-001, PRODUCT-ADR-PIPELINE-002, PRODUCT-ADR-PIPELINE-004, and PRODUCT-ADR-PIPELINE-005 in `impact_refs` and `## Impact Scope`.
- `prompt_chappy.md` lists PRODUCT-ADR-PIPELINE-005 as the current pipeline decision.
- T04 outputs list the ADRs and specifications modified by reconciliation.

### Repository-local verification

Strict specification validation passed after PRODUCT-ADR-PIPELINE-005 and all final reference updates:

```text
[strict] All 20 file(s) OK.
```

`git diff --check` produced no errors.

`git status --short` confirmed the expected ADR, specification, requirement, task, work-item, and protocol changes.
The status also showed the temporary untracked recovery file:

```text
before-retention-adr-revert.patch
```

The recovery patch is not a design-record output and must not be committed.

No design, ownership, format, or whitespace blocker remains.

### Post-review corrections (F-B-01 and F-B-02)

Corrections applied after PRODUCT-TASK-APPLICATION-002-05 identified two blocking findings.

#### F-B-01: Separation of publication and availability-only change preconditions

Changed: `spec:product.pipeline` `## Publication handoff`.

- Added `AvailabilityChange` semantic struct alongside the existing `PublicationHandoff` struct.
- Added descriptions distinguishing the two operation types.
- Renamed the single precondition block to `Before initial publication or content replacement (PublicationHandoff)`.
- Added a separate `Before an availability-only change (AvailabilityChange)` block requiring only an existing current projection and a pipeline-owned decision.
- Expanded writer obligations to distinguish republication with new content (`PublicationHandoff`) from availability restoration without content change (`AvailabilityChange`).
- Made explicit that an availability-only change must not alter current content or the current provenance reference.
- Made explicit that an availability-only change must produce one observable state transition.
- Stated that failed preconditions must not produce partial mutation for either operation type.

#### F-B-02: Removal of duplicated normative loaded-unit rules from application specs

Changed: `spec:product.application` `## Current contract` — removed the `Loaded content` row, which stated a UI-owned behavioral rule.

Changed: `spec:product.application.published_content` `### Loaded content` — replaced three normative UI-behavior rules with a single reference to the normative owner `spec:product.ui.learning_flow`. This resolves the contradiction with the existing Non-goals entry "Learner session state and loaded-content mutation."

Changed: `spec:product.application.learning_unit_selection` `### Retrieval and availability` — removed "A unit already loaded successfully must remain usable in the active PWA session," which is owned by `spec:product.ui.learning_flow`.

No change was required to `spec:product.ui.learning_flow`; it already owns the normative loaded-unit and replacement behavior.

#### Post-correction validation

`git diff --check` produced no whitespace errors (CRLF conversion warnings only; pre-existing on this platform).

`git status --short` confirms only the four expected specification files changed by these corrections:

- `product/records/spec/pipeline/index.md`
- `product/records/spec/application/index.md`
- `product/records/spec/application/published-content.md`
- `product/records/spec/application/learning-unit-selection.md`

No unrelated files were modified.
Design Records MCP validation was not used; its active index targets another repository.

Repository-local strict specification validation passed after corrections:

```text
[strict] All 20 file(s) OK.
```
