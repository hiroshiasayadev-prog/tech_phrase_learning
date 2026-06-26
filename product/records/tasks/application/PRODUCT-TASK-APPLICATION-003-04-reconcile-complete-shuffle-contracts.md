# PRODUCT-TASK-APPLICATION-003-04: Reconcile complete-shuffle contracts

- **id**: PRODUCT-TASK-APPLICATION-003-04
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-003
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 0.5d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-003-03
- **outputs**:
  - spec:product.application
  - spec:product.application.learning_unit_selection
  - spec:product.ui.learning_flow

## Goal

Reflect the T02 and T03 design results across affected ADRs and specifications without duplicating ownership.

## Work

1. Read the completed evidence from PRODUCT-TASK-APPLICATION-003-01 through PRODUCT-TASK-APPLICATION-003-03.
2. Reflect `SelectionScope`, the first-MVP `all` scope, and queue invariants in `spec:product.application.learning_unit_selection`.
3. Reflect bounded-selection semantics, adapter obligations, validation, and invalid-result handling in the application-owned specification.
4. Keep current availability meaning owned by `spec:product.application.published_content`.
5. Keep PWA queue position, exhaustion flow, retry, and learner progression owned by `spec:product.ui.learning_flow`.
6. Update `spec:product.application` only when overview or routing statements require alignment.
7. Update PRODUCT-ADR-APPLICATION-001 only when its accepted decision text or migration state requires correction.
8. Create or update another ADR only when T02 or T03 adopted a new architectural decision.
9. Remove contradictory, stale, or duplicated normative statements.
10. Preserve exclusions for exact algorithms, SQL, indexes, persistence, transport, and learner-history implementation.
11. Update ADR `migrated_to_spec` dates when changed decision meaning is fully reflected.
12. Record exact changed refs and explicit no-change judgments in `## Evidence`.

Do not adopt a new design decision in this task.

Report any unresolved decision as a blocker instead of resolving it inside specification edits.

## Done condition

- Every T02 and T03 result is reflected in one owning ADR or specification.
- `SelectionScope` and the first-MVP `all` scope are explicit.
- Queue bounds, uniqueness, later repetition, and smaller valid queues are explicit.
- Bounded selection and adapter obligations preserve database-side execution.
- Invalid adapter-result handling is explicit and implementation-independent.
- Current availability remains owned by the published-content contract.
- PWA queue state remains owned by the UI contract.
- Future scope extensions do not introduce backend queue state.
- Learner-history scope remains deferred behind a separate decision.
- Accepted ADRs and current specifications do not conflict.
- ADR `migrated_to_spec` metadata matches the reflected decision state.
- Concrete implementation choices remain deferred.

## Verification

- Review every `impact_ref` from PRODUCT-WORK-APPLICATION-003.
- Trace every T02 and T03 evidence statement to one owning specification or accepted ADR.
- Check affected records for full-corpus queue assumptions, cross-queue uniqueness, backend queue history, and duplicated UI ownership.
- Confirm that no specification text becomes the source of a new unrecorded architectural decision.
- Confirm canonical references, ADR metadata, and application topic routing after edits.
- Run available validation for affected PRODUCT ADRs, specifications, and workflow records.
- Record validation and working-tree evidence in `## Evidence`.

## Evidence

### Result

- **Verdict**: PASS after correction.
- T02 and T03 contracts are reflected in their owning specifications.
- The initial T05 review found one UI transition gap for valid empty queue results.
- The gap was corrected in `spec:product.ui.learning_flow` without changing application selection semantics.
- No blocker remains.
- No new ADR was required.
- T05 independent re-review may begin.

### Changed refs

| ref | change |
|---|---|
| `spec:product.application` | Aligned the overview with exact bounded cardinality, first-MVP `All`, no total-count result, and absent backend queue history. |
| `spec:product.application.learning_unit_selection` | Added `SelectionScope`, exact cardinality, queue invariants, the semantic operation, adapter obligations, validation ownership, invalid-array rejection, availability timing, and future-scope boundaries. |
| `spec:product.ui.learning_flow` | Made returned-array initialization and ordering explicit, then defined stable UI handling for empty initial and replacement queues. |
| PRODUCT-TASK-APPLICATION-003-04 | Recorded reconciliation evidence, outputs, validation, and completion status. |

### Impact-ref judgments

| impact ref | judgment |
|---|---|
| PRODUCT-ADR-APPLICATION-001 | No change. The accepted decision already requires `All`, at most 100 unique references, later repetition, database-side bounded random selection, no reservation, and retrieval-time availability checks. The resolved detail refines this decision without contradicting it. `migrated_to_spec: 2026-06-26` remains correct. |
| PRODUCT-ADR-UI-001 | No change. The accepted decision already assigns transient `LearningQueue`, queue position, retry, and learner progression to the PWA. `migrated_to_spec: 2026-06-25` remains correct. |
| `spec:product.application` | Changed. The overview now summarizes the exact bounded result and excludes a total eligible-count result. |
| `spec:product.application.learning_unit_selection` | Changed. This spec is the normative owner of the complete-shuffle selection contract. |
| `spec:product.application.published_content` | No change. The spec already owns current availability, the `available` and `unavailable` runtime states, selection eligibility, content separation, and availability-only withdrawal. |
| `spec:product.ui.learning_flow` | Changed to connect the returned ordered array to `LearningQueue` and define empty-result transitions. Queue position, exhaustion, stale-reference removal, loading, retry, skip, and progression remain UI-owned. |

### Contract traceability

| resolved contract | owning ref |
|---|---|
| `SelectionScope = All | Constrained(non_empty_constraints)` | `spec:product.application.learning_unit_selection` |
| First-MVP `All` application policy | `spec:product.application.learning_unit_selection` |
| `queue_size = min(maximum_count, eligible_count)` with `maximum_count = 100` | `spec:product.application.learning_unit_selection` |
| Within-result uniqueness and later repetition | `spec:product.application.learning_unit_selection` |
| Randomized ordered reference-array result | `spec:product.application.learning_unit_selection` |
| No total count, queue identity, reservation, backend position, or history | `spec:product.application.learning_unit_selection` |
| Database-compatible bounded selection and no complete candidate loading | `spec:product.application.learning_unit_selection` |
| Application-observable validation | `spec:product.application.learning_unit_selection` |
| Adapter-test ownership for availability, scope, exact cardinality, and randomization | `spec:product.application.learning_unit_selection` |
| Reject observable invalid arrays without normalization | `spec:product.application.learning_unit_selection` |
| Current availability meaning and published-state ownership | `spec:product.application.published_content` |
| Returned-array storage, queue position, exhaustion, retry, skip, and progression | `spec:product.ui.learning_flow` |

### Verification

- `All` adds no content-based constraint and does not require a full-corpus queue.
- The first-MVP result contains at most 100 references.
- The adapter exact-cardinality obligation remains `min(maximum_count, eligible_count)`.
- `eligible_count` is semantic only and is not returned to the application or PWA.
- The PWA receives and preserves only the ordered reference array.
- A successful empty initial queue shows the empty-queue screen and does not trigger another queue request.
- A successful empty replacement queue ends the current learning flow and shows the same empty-queue screen.
- The empty-queue screen provides only `Back to main`; it provides no queue retry.
- Observable invalid arrays are rejected as complete results without normalization.
- Availability meaning remains in `spec:product.application.published_content`.
- Queue state and learner progression remain in `spec:product.ui.learning_flow`.
- Retrieval independently rechecks current availability after selection-time availability observation.
- No SQL, table, index, query plan, exact algorithm, transport schema, framework, or persistence decision was introduced.
- Learner-history selection remains deferred behind a separate durable identity and progress-ownership decision.
- Both ADR `migrated_to_spec` values remain accurate.
- No `TBD` remains in this done task.

### Correction after initial T05 review

- The initial independent review identified an undefined UI transition for valid empty queue results.
- `spec:product.application.learning_unit_selection` already defined an empty array as valid.
- `spec:product.ui.learning_flow` now distinguishes valid empty results from infrastructure failures.
- A successful empty initial result shows `Quiz list was empty.` with `Back to main`.
- A successful empty replacement result ends the current learning flow and shows the same screen.
- Successful empty results provide no automatic or manual queue retry.
- Queue-acquisition request failures continue to use the existing retry behavior.
- No application, availability, persistence, transport, or algorithm contract changed.

### Validation evidence

- Design Records MCP does not index the target application and UI spec refs; exact `get_records` requests returned `record_not_found`.
- Filesystem MCP was therefore used for all target reads and edits.
- Targeted rereads confirmed the H1, canonical `id`, `parent`, metadata placement, required sections, and owning-reference links for every changed spec.
- Deterministic filesystem edit output confirmed changes only to the three changed spec files before this task evidence update.
- No repository command runner was available through the filesystem MCP, so no repository-wide Git status or CLI validator result is claimed.
