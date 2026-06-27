# PRODUCT-TASK-LEARNING-001-04: Reconcile quiz-session and downstream constraints

- **id**: PRODUCT-TASK-LEARNING-001-04
- **status**: done
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-LEARNING-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-LEARNING-001-03
- **outputs**:
  - spec:product.learning
  - spec:product.learning.quiz_session
  - PRODUCT-ADR-LEARNING-010
  - PRODUCT-ADR-LEARNING-011

## Goal

Complete quiz-session semantics and make every Learning-owned pipeline and UI constraint explicit.

## Work

1. Read the reconciled learning-model, learning-path, and learning-unit contracts from T03.
2. Reconcile `spec:product.learning.quiz_session` with question and reply interaction composition.
3. Reconcile active-quiz, answered-card, continue, skip, final-card, and next-discussion semantics.
4. Define deterministic progression, reveal order, and terminal behavior without defining PWA state storage.
5. Confirm the final answered card exposes the accepted attribution semantics.
6. Confirm correctness can be derived from immutable learning content and a stable selected-option identity.
7. Map every learning-owned production constraint required by `spec:product.pipeline`.
8. Map every immutable content constraint required by the application interface and UI.
9. Record downstream mismatches as explicit inputs for PRODUCT pipeline and UI work.
10. Change only Learning specifications in this task unless a separate owner task authorizes a downstream correction.
11. Update each reflected ADR's `migrated_to_spec` date when applicable.
12. Record changed specs, no-change judgments, downstream constraints, and owner follow-ups in Evidence.

Do not define pipeline stages, provider choices, runtime selection, PWA queue or session state, navigation, loading, retry, or component implementation.

## Done condition

- Question and reply interactions compose into one deterministic first-MVP session.
- Progressive reveal, continue, skip, final-card, and next-discussion behavior are explicit.
- No separate completion screen is required unless accepted authority changes.
- Unanswered content remains unrevealed after skip.
- Attribution appears at the accepted terminal learner-visible point.
- Selected-option identity and correctness derivation are consistent with the learning-unit contract.
- Pipeline can identify every learning-owned generation and publication-readiness obligation.
- Application and UI can identify every immutable learner-visible field they must preserve or consume.
- Downstream mismatches are routed to their semantic owners instead of being silently corrected here.
- Every normative Learning change traces to accepted authority.

## Verification

- Trace each session transition to accepted Learning authority and current learning-unit semantics.
- Confirm session semantics remain independent from PWA state representation.
- Confirm pipeline constraints state required outcomes rather than generation algorithms.
- Confirm UI constraints state immutable content needs rather than component or navigation behavior.
- Verify all modified specs retain correct parent refs and related refs.
- Run strict specification validation, `git diff --check`, and `git status --short`.

## Evidence

### Result

- The Learning overview and quiz-session contract now reflect the accepted session, identity, title, attribution-access, and generated-source constraints.
- No new Learning decision was introduced.
- Per-interaction skip was not introduced because PRODUCT-ADR-LEARNING-006 defines skip as leaving the current discussion.
- The Learning-owned reflection and downstream constraint inventory are complete within the T04 boundary.
- Required CLI verification completed successfully from PowerShell.
- T04 is complete within the accepted task boundary.

### Changed specifications

| ref | change |
|---|---|
| `spec:product.learning` | Added exact session cardinality, title, stable shuffled presentation, semantic answer identity, skip concealment, attribution access, and generated-source distinction. |
| `spec:product.learning.quiz_session` | Removed the stale Introduction-page model and defined session order, progression, answer reveal, early exit, option shuffling, correctness, title, attribution access, legal-notices access, and downstream outcomes. |

### Changed design records

| ref | change |
|---|---|
| PRODUCT-ADR-LEARNING-010 | Set `migrated_to_spec` to `2026-06-27` after identity, correct-option, first-activation shuffle, stable permutation, selection, and correctness reflection completed. |
| PRODUCT-ADR-LEARNING-011 | Set `migrated_to_spec` to `2026-06-27` after noncommercial use, complete attribution, current-unit access, main-page legal-notices access, and UI-owned mechanism boundaries were all present in current Learning specifications. |

### Intentionally unchanged specifications

| ref | reason |
|---|---|
| `spec:product.learning.learning_model` | The learner, gap, source-context, participation, and learning-outcome model already matches accepted authority. |
| `spec:product.learning.learning_path` | Path cardinality, source order, adjacency, and suitability were completed in T03. |
| `spec:product.learning.learning_unit` | Unit content, title, identities, correct-option references, attribution content, and publication readiness were completed in T03. |
| `spec:product.pipeline` | Generation stages, materialization contracts, gate mechanics, schemas, prompts, thresholds, and retries remain Pipeline-owned. |
| `spec:product.application` | Queue, selection, retrieval, transport, failure, and persistence contracts remain Application-owned. Existing complete-unit references remain valid. |
| `spec:product.ui` | PWA state, page composition, controls, routes, modal behavior, and permutation storage require UI-owned follow-up authority. |

### Authority trace

| authority | reflected contract |
|---|---|
| PRODUCT-ADR-LEARNING-001 | Authentic technical conversation remains the primary source. Generated content remains supplemental and distinguishable. |
| PRODUCT-ADR-LEARNING-005 | One available unit supplies one ordered interaction per selected source post. Generated quiz content remains separate from source evidence. |
| PRODUCT-ADR-LEARNING-006 | One active quiz, progressive quiz-to-summary replacement, reviewable answered cards, discussion-level skip, final attribution, and no separate terminal screen. |
| PRODUCT-ADR-LEARNING-007 | One session presents two to six ordered interactions. |
| PRODUCT-ADR-LEARNING-009 | The original source discussion title is the learner-visible session title. |
| PRODUCT-ADR-LEARNING-010 | Options use interaction-local identities, one correct-option reference, first-activation shuffle, stable session permutation, semantic answer retention, and identity-based correctness. |
| PRODUCT-ADR-LEARNING-011 | Noncommercial source use, complete attribution, current-unit access, main-page legal-notices access, and UI-owned presentation mechanisms. |
| PRODUCT-ADR-LEARNING-012 | Generated and source-authored wording remain distinguishable. Pipeline receives publication-ready unit outcomes without Learning-owned gate mechanics. |

### Ownership boundary

| owner | responsibility preserved by T04 |
|---|---|
| Learning | Session scope, interaction order, reveal and conceal outcomes, semantic option identity, correctness meaning, stable-presentation outcome, title meaning, attribution access, and generated-source distinction. |
| Pipeline | Source extraction, ordered content materialization, generation, validation, gate implementation, schemas, prompts, thresholds, retries, and publication mechanics. |
| Application | Available-unit selection, complete-unit retrieval, queue behavior, replacement, transport-independent operations, failure semantics, and persistence-facing read contracts. |
| UI | Concrete option permutation state, selected-answer state, page and component composition, navigation, controls, routes, modals, styling, and accessibility implementation. |

### Downstream follow-up

| owner | current mismatch or required follow-up |
|---|---|
| Pipeline | Materialize the two-to-six ordered interactions, source title, semantic option identities, correct-option references, complete attribution, generated-source distinction, and approved publication-ready result in focused Pipeline contracts. |
| Application | Add explicit verification that complete retrieved content preserves interaction order, title, semantic identities, correct-option references, summaries, target phrases, attribution, and generated-source distinction. |
| UI | Replace the unresolved top-bar title source with the learning unit's original source discussion title. |
| UI | Shuffle options on first activation, keep each permutation stable, retain selected semantic identity, and derive correctness from immutable content. |
| UI | Add current-unit attribution access and main-page global legal-notices access through UI-owned authority and mechanisms. |
| UI | Keep generated or adapted wording visually distinguishable from source-authored wording without changing Learning meaning. |

### Stale contract cleanup

- The Learning-owned `Introduction` page model was removed from `spec:product.learning.quiz_session`.
- Current UI page specifications already define only the main page and learning page.
- No new page, route, modal, or control was introduced by Learning.
- Start-flow and legal-notices presentation remain UI-owned concerns.

### Skip authority boundary

- PRODUCT-ADR-LEARNING-006 defines skip as leaving the current discussion before remaining quizzes are completed.
- Current UI specifications use the same discussion-level skip behavior.
- T04 therefore defines skip as early session exit with all unanswered summaries and correct phrases concealed.
- A per-interaction skip that continues within the same unit would require a new accepted Learning ADR.

### Verification

Filesystem reread confirmed:

- `spec:product.learning.quiz_session` contains no Learning-owned Introduction page;
- session cardinality is two to six ordered interactions;
- title, option identity, stable permutation, correctness, attribution access, and generated-source distinction are explicit;
- PRODUCT-ADR-LEARNING-010 and PRODUCT-ADR-LEARNING-011 record `migrated_to_spec: 2026-06-27`;
- Pipeline, Application, and UI implementation mechanics remain outside the Learning contract.

PowerShell verification completed with these results:

- `git diff --check` produced no output.
- `validate_spec.py product/records/spec --strict --no-color` returned `[strict]  All 34 file(s) OK.`
- `git status --short` listed exactly the five expected T04 files.

Verified T04 paths:

- `product/records/spec/learning/index.md`;
- `product/records/spec/learning/quiz-session.md`;
- `product/records/adr/learning/PRODUCT-ADR-LEARNING-010-use-stable-option-identity-and-shuffled-presentation.md`;
- `product/records/adr/learning/PRODUCT-ADR-LEARNING-011-expose-unit-level-source-attribution-for-noncommercial-first-mvp.md`;
- `product/records/tasks/learning/PRODUCT-TASK-LEARNING-001-04-reconcile-quiz-session-and-downstream-constraints.md`.

### Closure

- Learning-owned T04 semantic and ownership conditions are satisfied.
- ADR migration assessment is complete.
- Downstream mismatches are routed without unauthorized downstream edits.
- Strict validation, `git diff --check`, and working-tree inspection succeeded.
- Every T04 done condition is satisfied.
- PRODUCT-TASK-LEARNING-001-04 is complete and ready for commit.
