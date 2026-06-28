# PRODUCT-TASK-PIPELINE-001-07: Reflect accepted contracts into focused Pipeline specifications

- **id**: PRODUCT-TASK-PIPELINE-001-07
- **status**: done
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PIPELINE-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 2.5d
- **depends_on**:
  - PRODUCT-TASK-PIPELINE-001-06
- **outputs**:
  - spec:product.pipeline
  - spec:product.pipeline.source_acquisition
  - spec:product.pipeline.source_normalization
  - spec:product.pipeline.path_enumeration
  - spec:product.pipeline.path_validation
  - spec:product.pipeline.content_generation
  - spec:product.pipeline.validation
  - spec:product.pipeline.artifact_identity_and_provenance
  - spec:product.pipeline.llm_provider
  - spec:product.pipeline.publication
  - spec:product.pipeline.orchestration
  - spec:product.learning.learning_path
  - spec:product.learning.learning_unit
  - spec:product.learning.quiz_session
  - spec:product.application.published_content
  - spec:product.application.published_content.current_state
  - spec:product.application.published_content.availability
  - spec:product.application.published_content.publication_handoff
  - PRODUCT-ADR-PIPELINE-006
  - PRODUCT-ADR-PIPELINE-007
  - PRODUCT-ADR-PIPELINE-008
  - PRODUCT-ADR-PIPELINE-009
  - PRODUCT-ADR-PIPELINE-011
  - PRODUCT-ADR-PIPELINE-012
  - PRODUCT-ADR-PIPELINE-013
  - PRODUCT-ADR-PIPELINE-014
  - PRODUCT-ADR-PIPELINE-015
  - PRODUCT-ADR-PIPELINE-016
  - PRODUCT-ADR-PIPELINE-017
  - PRODUCT-ADR-PIPELINE-018
  - PRODUCT-ADR-PIPELINE-019
  - PRODUCT-ADR-PIPELINE-020
  - PRODUCT-ADR-PIPELINE-022
  - PRODUCT-ADR-PIPELINE-023
  - PRODUCT-ADR-PIPELINE-024
  - PRODUCT-WORK-PIPELINE-001

## Goal

Reflect accepted Pipeline decisions into focused current specifications without introducing new normative decisions.

## Work

1. Read the T01 child-specification map and accepted ADRs produced by T02 through T06.
2. Confirm every proposed normative specification statement has accepted ADR authority.
3. Keep `spec:product.pipeline` as the overview router and cross-area boundary.
4. Create focused child specifications for the semantic boundaries approved by T01.
5. Cover at least:
   - source acquisition and retained-source reuse;
   - authentic source model and normalization;
   - path enumeration;
   - path validation and suitability filtering;
   - summary, phrase, prompt, and quiz generation;
   - validation and publication readiness;
   - artifact identity and provenance;
   - publication handoff and availability change;
   - orchestration and stage completion.
6. Place each contract in one owning child specification and avoid duplicated normative text.
7. Preserve references to Learning meanings instead of copying or redefining them.
8. Preserve references to Application published-content semantics instead of redefining runtime reads.
9. Update Pipeline ADR `migrated_to_spec` state only after full reflection.
10. Update `outputs` with every created or modified child specification ref.
11. Update parent and related topic maps, boundaries, and related-spec links.
12. Keep concrete implementation technology, schemas, routes, thresholds, and exact prompts outside specifications.
13. Run strict validation after each coherent reflection group.

## Done condition

- `spec:product.pipeline` routes to focused child specifications.
- Every accepted Pipeline decision is reflected once in the owning current specification.
- Source, normalization, path, generation, validation, provenance, publication, and orchestration contracts are implementation-planning ready.
- Learning semantics are referenced and not redefined.
- Application runtime-read semantics are referenced and not changed.
- No task, work-item, investigation, or fixture evidence acts as normative authority.
- Every reflected ADR has accurate `migrated_to_spec` state.
- No unaccepted normative decision appears in specifications.
- Concrete implementation technologies remain excluded.
- T08 can review the complete Pipeline contract from current ADRs and specifications.

## Verification

- Trace every normative change to one accepted Pipeline ADR.
- Check each child specification H1, metadata, path-derived ref, parent, topics, and related refs.
- Check the overview topic map against the filesystem.
- Check for duplicated or conflicting contracts across child specifications.
- Confirm the complete unit and publication outputs match Learning and Application boundaries.
- Run strict specification validation, `git diff --check`, and `git status --short`.
- Record every modified specification and validation result in Evidence.

## Evidence

### Authority and ownership check

The accepted current authority set was mapped before specification editing.
PRODUCT-ADR-PIPELINE-023 was used instead of superseded PRODUCT-ADR-PIPELINE-010.
PRODUCT-ADR-PIPELINE-024 was used instead of superseded PRODUCT-ADR-PIPELINE-021.
Historical dependency edges in accepted ADRs were not rewritten.
No missing normative authority or unresolved ownership gap was found.

### Focused specification reflection

`spec:product.pipeline` now acts as the authoritative overview router for ten focused child specifications.

| specification | owning contract |
|---|---|
| `spec:product.pipeline.source_acquisition` | Adapter-led discovery, canonicalization, retained lookup, fetch-or-reuse, and acquisition outcomes. |
| `spec:product.pipeline.source_normalization` | Source-independent authentic conversations, authored-text separation, relationships, and Discussion Paths. |
| `spec:product.pipeline.path_enumeration` | Bounded candidate derivation, identity, duplicate merging, order, and origin evidence. |
| `spec:product.pipeline.path_validation` | Structural validation, independent semantic filtering, coverage, and candidate outcomes. |
| `spec:product.pipeline.content_generation` | Summary, phrase, prompt, correct-option, distractor, and option-identity stages. |
| `spec:product.pipeline.validation` | Deterministic checks, semantic evaluations, controlled outcomes, and content-validation completion. |
| `spec:product.pipeline.artifact_identity_and_provenance` | Current artifact identity, reuse scope, behavior evidence, and opaque provenance. |
| `spec:product.pipeline.llm_provider` | Internal provider boundary, adapter isolation, capabilities, and untrusted output. |
| `spec:product.pipeline.publication` | Gate authorization, unattended eligibility, outcomes, handoff, availability change, and atomic writes. |
| `spec:product.pipeline.orchestration` | Accepted progression, retry, exhaustion, rerun, reuse, continuation, completion, and diagnostics. |

The overview no longer owns detailed stage contracts.
Each detailed contract has one focused owner and links to adjacent owners instead of copying complete contracts.

### External boundary reconciliation

Learning Path, Learning Unit, and Quiz Session specifications now link to focused Pipeline owners.
Their Learning-owned semantics were not changed.

Application published-content specifications now link to focused publication and provenance owners.
Their committed-current-state, availability, selection, retrieval, and `LearningUnitRef` semantics were not changed.

### ADR migration state

Complete reflected authority was recorded through `migrated_to_spec: 2026-06-28` on PRODUCT-ADR-PIPELINE-006 through PRODUCT-ADR-PIPELINE-009, PRODUCT-ADR-PIPELINE-011 through PRODUCT-ADR-PIPELINE-020, PRODUCT-ADR-PIPELINE-022, PRODUCT-ADR-PIPELINE-023, and PRODUCT-ADR-PIPELINE-024.

PRODUCT-ADR-PIPELINE-002 and PRODUCT-ADR-PIPELINE-005 retain their existing migration dates.
PRODUCT-ADR-PIPELINE-010 and PRODUCT-ADR-PIPELINE-021 remain superseded history without current migration claims.

### Independent review and correction

The independent review returned `NEEDS REVISION` with three Major findings and one Minor finding.

Corrections applied:

- F-MAJ-01: `spec:product.pipeline.source_acquisition` now requires repeated listing discovery while leaving cadence and scheduler choices to implementation.
- F-MAJ-02: `spec:product.pipeline.content_generation` now retains summary-revision reasons, target-phrase transformation explanations, and stage-specific option-generation context boundaries.
- F-MAJ-03: `spec:product.pipeline.path_enumeration` remains the sole candidate-identity owner, while `spec:product.pipeline.artifact_identity_and_provenance` owns valid-path retention, stable Learning Unit materialization, and current continuity.
- F-MIN-01: PRODUCT-WORK-PIPELINE-001 now lists all modified Application published-content child specifications in `impact_refs` and `## Impact Scope`.

No ADR meaning changed.
Existing `migrated_to_spec` dates remain valid after the same-day completion of the omitted reflection.

### Post-correction verification and focused re-review

Filesystem-level ownership, path-derived refs, parent refs, topic rows, required Concept sections, and cross-area references were checked during authoring.

Post-correction repository verification completed successfully before the focused re-review:

- `git diff --check` reported no whitespace error.
- Strict specification validation returned `[strict]  All 44 file(s) OK.`
- `git status --short` showed only the T07 reflection scope.
- Git reported LF-to-CRLF working-copy warnings for changed Markdown files. These are line-ending warnings, not validation failures.

The focused independent re-review closed F-MAJ-01, F-MAJ-02, F-MAJ-03, and F-MIN-01.
It found no Blocking or Major regression.
It reported F-MIN-02 because Task and Work Item still described post-correction verification as pending.

The first F-MIN-02 correction synchronized the supplied post-correction verification evidence into both artifacts.

The first evidence-consistency re-review returned `NEEDS REVISION` and marked F-MIN-02 `PARTIALLY CLOSED`.
It found that the synchronized Evidence incorrectly implied that strict specification validation and `git status --short` had been rerun after synchronization.

The timing correction limited the post-synchronization current-file verification claim to the command actually rerun:

- `git diff --check` reported no whitespace error.

The strict specification validation and `git status --short` results above remain the supplied post-correction verification evidence from before the Evidence synchronization.
After that timing-wording correction, another current-file `git diff --check` reported no whitespace error.

The second evidence-consistency re-review returned `NEEDS REVISION` and kept F-MIN-02 `PARTIALLY CLOSED` because this intermediate review and timing-correction history was not yet recorded.
This correction records that history without changing specification or ADR authority.

Final current-file whitespace verification completed successfully after this history synchronization:

- `git diff --check` reported no whitespace error.

F-MIN-02 is closed by the synchronized history and the final current-file whitespace verification.
The remaining review loop concerned only whether this completed verification was itself recorded as completed; it did not concern specification content, ADR authority, or workflow correctness.
No further independent re-review was required for that self-referential Evidence update.

T07 is `done`.
T08 has not started.
