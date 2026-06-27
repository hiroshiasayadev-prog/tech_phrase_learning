# PRODUCT-WORK-LEARNING-001: Review first-MVP learning contract completeness

- **id**: PRODUCT-WORK-LEARNING-001
- **status**: in_progress
- **date**: 2026-06-27
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **impact_refs**:
  - PRODUCT-ADR-LEARNING-001
  - PRODUCT-ADR-LEARNING-005
  - PRODUCT-ADR-LEARNING-006
  - spec:product.learning
  - spec:product.learning.learning_model
  - spec:product.learning.learning_path
  - spec:product.learning.learning_unit
  - spec:product.learning.quiz_session
  - spec:product.pipeline
  - spec:product.application.pwa_interface
  - spec:product.ui.learning_flow
  - spec:product.ui.components.top_bar
  - spec:product.ui.components.quiz_card
  - spec:product.ui.components.answered_card
- **tasks**:
  - PRODUCT-TASK-LEARNING-001-01
  - PRODUCT-TASK-LEARNING-001-02
  - PRODUCT-TASK-LEARNING-001-03
  - PRODUCT-TASK-LEARNING-001-04
  - PRODUCT-TASK-LEARNING-001-05

## Goal

Establish an independently reviewed first-MVP learning contract that is complete enough to constrain pipeline and UI implementation planning.

Resolve learning-owned gaps without moving processing mechanics, runtime selection, or PWA state into the learning area.

## Boundary

This work item owns:

- consistency among the target learner, learning gap, and intended learning outcome;
- valid learning-path meaning, composition, and suitability criteria;
- required learning-unit elements, cardinalities, identities, and invariants;
- question-formulation and reply-formulation interaction composition;
- target phrase, prompt, answer-option, summary, grounding, and attribution semantics;
- the learning-owned meaning of discussion title and option identity when required by downstream consumers;
- quiz-session progression, reveal order, skip behavior, and terminal behavior;
- learning-owned publication-readiness criteria;
- explicit learning constraints consumed by pipeline and UI contracts;
- ADR-first resolution of missing normative decisions;
- specification reflection and independent review.

This work item does not own:

- source acquisition, parsing, normalization, path enumeration, filtering, generation, validation, retry, or orchestration mechanics;
- concrete model, provider, prompt, threshold, or publication-gate implementation choices;
- runtime learning-unit selection, availability-aware retrieval, or application failure semantics;
- PWA queue, session, loading, retry, navigation, disposal, or presentation state;
- persistence, transport, serialization, route, framework, component-file, or deployment choices.

A downstream need may expose a learning-contract gap.
The resulting learning meaning must be authorized by an accepted Learning ADR before specification reflection.

## Impact Scope

| ref | impact |
|---|---|
| PRODUCT-ADR-LEARNING-001 | Preserve the target learner, technical-conversation source, and context-first learning direction. |
| PRODUCT-ADR-LEARNING-005 | Preserve path-based unit identity, mixed interactions, summarized source representation, and automated publication gating. |
| PRODUCT-ADR-LEARNING-006 | Preserve progressive quiz-to-summary card semantics and final-card behavior. |
| `spec:product.learning` | Reconcile the whole-area contract and child ownership boundaries. |
| `spec:product.learning.learning_model` | Verify target learner, learning gap, participation model, and learning outcome consistency. |
| `spec:product.learning.learning_path` | Verify valid-path meaning, suitability, cardinality, and source-grounding constraints. |
| `spec:product.learning.learning_unit` | Complete required content, identity, option, summary, grounding, attribution, and publication-readiness semantics. |
| `spec:product.learning.quiz_session` | Complete question/reply composition, progression, skip, reveal, and terminal behavior. |
| `spec:product.pipeline` | State learning-owned inputs that pipeline generation and publication validation must satisfy. |
| `spec:product.application.pwa_interface` | Ensure retrieved complete content contains every learning-owned learner-visible element. |
| `spec:product.ui.learning_flow` | Ensure immutable content provides the discussion title, stable option identity, attribution, and correctness inputs consumed by PWA state. |
| `spec:product.ui.components.top_bar` | Resolve the learning-owned meaning and source of the current discussion title. |
| `spec:product.ui.components.quiz_card` | Preserve prompt, option, and correct-answer meaning without defining UI controls. |
| `spec:product.ui.components.answered_card` | Preserve summary, result, target phrase, and attribution meaning without defining UI state. |

## Task flow

```text
T01 Establish learning completeness baseline and gap inventory
  |
  v
T02 Resolve missing learning decisions through accepted ADRs
  |
  v
T03 Reconcile learning-path and learning-unit contracts
  |
  v
T04 Reconcile quiz-session and downstream constraints
  |
  v
T05 Independent integrated review and closure
```

- T01 classifies current authority, specification gaps, downstream mismatches, and implementation-only concerns.
- T02 obtains user decisions and accepts Learning ADRs only where current authority is insufficient.
- T03 reflects accepted authority into complete learning-path and learning-unit contracts.
- T04 reflects session semantics and records explicit constraints for pipeline and UI follow-up work.
- T05 independently verifies authority, ownership, completeness, and implementation-planning readiness.

## Task Candidates

| task | responsibility |
|---|---|
| PRODUCT-TASK-LEARNING-001-01 | Establish the current learning baseline and exact unresolved gap set. |
| PRODUCT-TASK-LEARNING-001-02 | Resolve missing normative learning decisions through the ADR-first gate. |
| PRODUCT-TASK-LEARNING-001-03 | Reconcile valid-path and complete learning-unit contracts. |
| PRODUCT-TASK-LEARNING-001-04 | Reconcile quiz-session semantics and downstream learning constraints. |
| PRODUCT-TASK-LEARNING-001-05 | Perform an independent integrated review and close the work item. |

## Completion Condition

- The target learner, learning gap, participation model, and intended learning outcome are mutually consistent.
- Valid learning-path meaning, cardinality, coherence, suitability, and source-grounding criteria are explicit.
- Every complete learning unit has explicit required elements, cardinalities, identities, and invariants.
- Question-formulation and reply-formulation interactions have complete and consistent composition rules.
- Target phrase, prompt, answer option, correct option, summary, grounding, discussion title, and attribution semantics are explicit where required.
- Option identity is stable enough for learner-answer state without defining a wire representation.
- Quiz-session progression, reveal order, skip behavior, final-card behavior, and terminal behavior are deterministic.
- Learning-owned publication-readiness criteria are explicit and distinguishable from pipeline validation mechanics.
- Pipeline and UI can identify every learning-owned input they must produce or consume.
- Processing, provider, runtime-selection, persistence, transport, and PWA-state choices remain outside this work item.
- Every new normative decision is recorded in an accepted Learning ADR before specification reflection.
- Current learning specifications contain the accepted contract without using task or work-item evidence as authority.
- PRODUCT-TASK-LEARNING-001-05 records a final `PASS` verdict with no blocking or major finding.
- Pipeline and UI implementation planning can proceed without reconstructing missing learning semantics.

## Evidence

TBD
