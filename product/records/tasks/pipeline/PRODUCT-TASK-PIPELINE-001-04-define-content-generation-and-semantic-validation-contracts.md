# PRODUCT-TASK-PIPELINE-001-04: Define content generation and semantic-validation contracts

- **id**: PRODUCT-TASK-PIPELINE-001-04
- **status**: not_started
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PIPELINE-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 2.5d
- **depends_on**:
  - PRODUCT-TASK-PIPELINE-001-03
- **outputs**: []

## Goal

Define bounded summary, target-phrase, intent-prompt, quiz-generation, and semantic-validation stage contracts.

## Work

1. Read accepted Pipeline ADRs, T03 path outputs, and the fixed Learning unit contract.
2. Define reusable source-post summary inputs, outputs, grounding evidence, and validation obligations.
3. Define path-specific summary revision inputs, outputs, and continuity constraints.
4. Require summaries to preserve position, certainty, response meaning, and source grounding.
5. Define unsupported-claim rejection and generated-versus-source-authored separation.
6. Define target-phrase selection as a distinct bounded stage.
7. Define concise intent-prompt generation as a distinct bounded stage.
8. Define exactly-three-option quiz generation as a distinct bounded stage.
9. Require generated option identity to be semantic and independent from array position.
10. Require one correct-option reference that resolves within the interaction.
11. Define naturalness, contextual fit, target-phrase realization, and incorrect-option usefulness evaluation.
12. Define per-stage input completeness, structured-output validation, source-grounding checks, and semantic evaluation results.
13. Define invalid provider output as untrusted stage output without selecting a retry policy.
14. Define how contradictory or incomplete stage results are reported to orchestration.
15. Preserve provider isolation and smallest-sufficient-context requirements from current ADRs.
16. Create or update Pipeline ADRs when current authority does not determine observable generation or validation semantics.
17. Keep exact prompts, model names, thresholds, schemas, and provider assignments outside the contract.
18. Update `outputs` and Evidence with accepted ADRs or specification inputs.

## Done condition

- Reusable and path-specific summary stages have explicit inputs, outputs, and grounding obligations.
- Conversational continuity and unsupported-claim rejection are explicit.
- Generated and source-authored content remain distinguishable.
- Target-phrase selection, prompt generation, and quiz generation are separate bounded stages.
- Every interaction produces exactly three semantically identified options and one correct-option reference.
- Naturalness, contextual fit, phrase realization, and distractor usefulness have explicit evaluation outcomes.
- Every model-produced structure has mechanical validation and semantic evaluation obligations.
- Invalid, incomplete, and contradictory stage results have explicit orchestration-facing outcomes.
- Every new normative decision has accepted Pipeline ADR authority.
- Concrete model, prompt, threshold, and serialized schema choices remain deferred.

## Verification

- Trace each output obligation to `spec:product.learning.learning_unit` or accepted Pipeline authority.
- Confirm the stage contracts do not redefine learner-visible meaning.
- Confirm option identity never derives from generated array position, labels, display order, or option text.
- Confirm source grounding does not rely only on model assertion.
- Confirm a model-only success result cannot establish publication readiness.
- Check the reviewed golden fixture and harder experiment findings as evidence, not authority.
- Run relevant record validation, strict specification validation, `git diff --check`, and `git status --short`.

## Evidence

TBD
