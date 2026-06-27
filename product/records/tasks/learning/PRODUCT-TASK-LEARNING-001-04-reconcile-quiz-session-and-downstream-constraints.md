# PRODUCT-TASK-LEARNING-001-04: Reconcile quiz-session and downstream constraints

- **id**: PRODUCT-TASK-LEARNING-001-04
- **status**: not_started
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-LEARNING-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-LEARNING-001-03
- **outputs**:
  - spec:product.learning
  - spec:product.learning.quiz_session

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

TBD
