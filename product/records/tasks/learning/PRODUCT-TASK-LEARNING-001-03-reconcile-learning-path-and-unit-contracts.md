# PRODUCT-TASK-LEARNING-001-03: Reconcile learning-path and learning-unit contracts

- **id**: PRODUCT-TASK-LEARNING-001-03
- **status**: done
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-LEARNING-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-LEARNING-001-02
- **outputs**:
  - spec:product.learning
  - spec:product.learning.learning_path
  - spec:product.learning.learning_unit
  - PRODUCT-ADR-LEARNING-007
  - PRODUCT-ADR-LEARNING-008
  - PRODUCT-ADR-LEARNING-009
  - PRODUCT-ADR-LEARNING-012

## Goal

Reflect accepted authority into complete and internally consistent learning-model, learning-path, and learning-unit contracts.

## Work

1. Read the final authority map from T01 and every accepted ADR produced or confirmed by T02.
2. Reconcile `spec:product.learning.learning_model` with the target learner, learning gap, participation model, and intended learning outcome.
3. Reconcile `spec:product.learning.learning_path` with valid-path composition, cardinality, coherence, suitability, and source-grounding rules.
4. Reconcile `spec:product.learning.learning_unit` with complete required elements, identities, cardinalities, and invariants.
5. Define question-formulation and reply-formulation composition only where owned by the learning-unit contract.
6. Reconcile learner-visible semantics for:
   - discussion title;
   - interaction type;
   - quiz prompt;
   - target quiz phrase;
   - answer options;
   - correct option;
   - stable option identity;
   - source-post summary;
   - source grounding;
   - source attribution.
7. Reconcile learning-owned publication-readiness criteria without defining pipeline validation mechanics.
8. Update `spec:product.learning` only as needed to route the completed child contracts.
9. Update each reflected ADR's `migrated_to_spec` date when applicable.
10. Record every changed and intentionally unchanged specification in Evidence.

Do not define generation stages, model tasks, retries, thresholds, serialization, runtime selection, or PWA state.

## Done condition

- Learning-model, path, and unit contracts are mutually consistent.
- Valid-path suitability is explicit without prescribing enumeration or filtering algorithms.
- Every complete learning unit has explicit required elements, cardinalities, identities, and invariants.
- Every learner-visible field has one clear semantic owner.
- Stable option identity supports answer recording without defining its wire representation.
- Discussion-title and attribution semantics satisfy accepted authority.
- Publication-readiness criteria state learning quality requirements without prescribing pipeline mechanics.
- Each normative specification change traces to an accepted ADR.
- No processing, provider, application, UI-state, persistence, or transport decision enters the specifications.

## Verification

- Trace every changed normative claim to an accepted Learning ADR.
- Verify path-to-unit cardinality and stable learning-unit identity remain unchanged unless explicitly superseded.
- Verify generated quiz content remains distinguishable from source-derived summaries and authentic source evidence.
- Verify publication-readiness criteria are testable by downstream work without becoming pipeline algorithms.
- Verify all modified specs retain correct parent refs and related refs.
- Run strict specification validation, `git diff --check`, and `git status --short`.

## Evidence

### Result

- Accepted Learning authority was reflected into the Learning overview, learning-path contract, and learning-unit contract.
- Independent review found two major findings and one minor finding.
- The findings were corrected without introducing a new design decision.
- Post-correction CLI verification completed successfully.

### Changed specifications

| ref | change |
|---|---|
| `spec:product.learning` | Added current-contract summaries for path bounds, adjacency, source title, option identity, attribution, and publication readiness. |
| `spec:product.learning.learning_path` | Defined two-to-six cardinality, source-grounded adjacency, unavailable-target distinction, coherence, and per-post suitability. |
| `spec:product.learning.learning_unit` | Defined title, interaction bounds, option identity, correct-option references, attribution, complete publication readiness, and harder-fixture validation before unattended publication approval. |

### Changed design records

| ref | change |
|---|---|
| PRODUCT-ADR-LEARNING-007 | Set `migrated_to_spec` to `2026-06-27` after path and unit cardinality reflection completed. |
| PRODUCT-ADR-LEARNING-008 | Set `migrated_to_spec` to `2026-06-27`. |
| PRODUCT-ADR-LEARNING-009 | Set `migrated_to_spec` to `2026-06-27`. |
| PRODUCT-ADR-LEARNING-012 | Kept `migrated_to_spec: 2026-06-27` after completing the harder-fixture approval condition. |

### Intentionally unchanged specifications

| ref | reason |
|---|---|
| `spec:product.learning.learning_model` | The current learner, learning-gap, participation, source-context, and learning-outcome contract already matches accepted authority. |
| `spec:product.learning.quiz_session` | Session progression, shuffled presentation, and attribution access belong to T04. |
| `spec:product.pipeline` | Generation, projection, gate implementation, model, prompt, threshold, retry, and schema choices remain Pipeline-owned. |
| `spec:product.application` | Runtime selection, retrieval, published-content transport, and availability behavior remain Application-owned. |
| `spec:product.ui` | PWA state, title placement, option permutation state, and attribution presentation remain UI-owned. |

### Authority trace

| authority | reflected contract | migration state |
|---|---|---|
| PRODUCT-ADR-LEARNING-001 | Authentic technical conversations remain the primary source and generated content remains supplemental. | Previously migrated. |
| PRODUCT-ADR-LEARNING-005 | One valid path defines one unit with one interaction per selected post and distinct generated and source-derived content. | Previously migrated. |
| PRODUCT-ADR-LEARNING-006 | Quiz and summary field semantics remain compatible with progressive quiz-to-summary cards. | Previously migrated. |
| PRODUCT-ADR-LEARNING-007 | Learning paths contain two to six posts and units contain two to six interactions. | `2026-06-27`; the Learning path and unit decision is fully reflected. |
| PRODUCT-ADR-LEARNING-008 | Adjacency uses explicit replies or genuine topic-level opening-post projection. | `2026-06-27`. |
| PRODUCT-ADR-LEARNING-009 | Every unit uses the original source discussion title. | `2026-06-27`. |
| PRODUCT-ADR-LEARNING-010 | Options have interaction-local identities and correctness uses one identity reference. | `null`; T04 must define stable shuffled presentation. |
| PRODUCT-ADR-LEARNING-011 | Noncommercial corpus use and complete unit-specific attribution are explicit. | `null`; T04 must define global and current-unit access constraints. |
| PRODUCT-ADR-LEARNING-012 | Structural and semantic readiness, non-compensation, automated gating, human approval, and harder-fixture validation before unattended publication are explicit. | `2026-06-27`. |

### T04 constraints

- One session must present two to six ordered interactions from one available learning unit.
- Each interaction must shuffle its three options when first activated.
- The selected permutation must remain stable until the current learning-unit session ends.
- Learner-answer state must retain the selected semantic option identity.
- Correctness must compare the selected identity with the interaction's correct-option reference.
- The current unit's attribution must remain learner-accessible during the session.
- Global legal notices must remain accessible from the main page.
- Unanswered summaries and correct phrases must remain hidden after skip.
- Generated content must remain distinguishable from source-authored wording throughout the session.
- The stale Learning-owned Introduction page claim must be removed or rerouted without adding a new Learning decision.

### Downstream owner follow-up

| owner | required follow-up |
|---|---|
| Pipeline | Materialize valid source-grounded paths, original titles, option identities, correct-option references, complete attribution, and approved gate results. |
| Pipeline | Define deterministic checks, semantic evaluation contracts, coverage checks, thresholds, retries, and representative harder-fixture evidence. |
| Application | Preserve the original title, option identities, correct-option reference, attribution record, and all complete unit content. |
| UI | Use the unit's source discussion title in the top bar. |
| UI | Preserve selected semantic identity and one stable option permutation per interaction. |
| UI | Define global legal-notices and unit-attribution access after obtaining UI-owned authority for the anchor-style modal direction. |

### Independent review correction

- M1 closed by requiring gate-configuration validation against approved golden and harder fixtures before unattended publication approval.
- M2 closed by setting PRODUCT-ADR-LEARNING-007 `migrated_to_spec` to `2026-06-27`.
- The minor outputs finding closed by removing unchanged `spec:product.learning.learning_model` from `outputs`.

### Verification

- Filesystem reread confirmed the corrected spec wording, ADR migration state, task outputs, and Evidence synchronization.
- PRODUCT-ADR-LEARNING-007, PRODUCT-ADR-LEARNING-008, PRODUCT-ADR-LEARNING-009, and PRODUCT-ADR-LEARNING-012 record `migrated_to_spec: 2026-06-27`.
- PRODUCT-ADR-LEARNING-010 and PRODUCT-ADR-LEARNING-011 remain `null` pending T04 reflection.
- Post-correction `git diff --check` completed without whitespace errors.
- Post-correction `validate_spec.py product/records/spec --strict --no-color` returned `[strict]  All 34 file(s) OK.`
- Post-correction `git status --short` listed exactly the eight expected modified T03 files.
- DRMCP validation was not used and no DRMCP success is claimed.

### Closure

- T03 specification reflection and independent-review corrections are complete.
- Every done condition is satisfied.
- Required post-correction verification succeeded.
- PRODUCT-TASK-LEARNING-001-03 is complete and ready for commit.
