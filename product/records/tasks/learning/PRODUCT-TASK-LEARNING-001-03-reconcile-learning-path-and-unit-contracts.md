# PRODUCT-TASK-LEARNING-001-03: Reconcile learning-path and learning-unit contracts

- **id**: PRODUCT-TASK-LEARNING-001-03
- **status**: not_started
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-LEARNING-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-LEARNING-001-02
- **outputs**:
  - spec:product.learning
  - spec:product.learning.learning_model
  - spec:product.learning.learning_path
  - spec:product.learning.learning_unit

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

TBD
