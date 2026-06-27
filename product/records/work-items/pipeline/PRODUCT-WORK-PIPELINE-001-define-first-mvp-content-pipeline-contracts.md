# PRODUCT-WORK-PIPELINE-001: Define first-MVP content-pipeline contracts

- **id**: PRODUCT-WORK-PIPELINE-001
- **status**: not_started
- **date**: 2026-06-27
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **impact_refs**:
  - PRODUCT-ADR-PIPELINE-002
  - PRODUCT-ADR-PIPELINE-005
  - PRODUCT-INV-PIPELINE-001
  - PRODUCT-INV-PIPELINE-002
  - PRODUCT-WORK-LEARNING-001
  - spec:product.pipeline
  - spec:product.learning.learning_path
  - spec:product.learning.learning_unit
  - spec:product.learning.quiz_session
  - spec:product.application.published_content
- **tasks**:
  - PRODUCT-TASK-PIPELINE-001-01
  - PRODUCT-TASK-PIPELINE-001-02
  - PRODUCT-TASK-PIPELINE-001-03
  - PRODUCT-TASK-PIPELINE-001-04
  - PRODUCT-TASK-PIPELINE-001-05
  - PRODUCT-TASK-PIPELINE-001-06
  - PRODUCT-TASK-PIPELINE-001-07
  - PRODUCT-TASK-PIPELINE-001-08

## Goal

Establish implementation-planning-ready semantic contracts for the first-MVP content pipeline.

Consume the completed Learning contract and produce validated publication outputs for the fixed Application published-content boundary.

## Boundary

This work item owns:

- source acquisition, retained authentic-source reuse, refresh, replacement, identity, and acquisition-failure meaning;
- source-independent authentic-post normalization and conversation relationship preservation;
- deterministic path enumeration, structural validation, and suitability-filtering mechanics;
- reusable summary, path-specific summary, target-phrase, prompt, and quiz-generation contracts;
- mechanical validation, semantic validation, bounded retry, rejection, and incomplete-unit handling;
- current artifact identity, generated-content versioning, and pipeline-owned provenance;
- publication-gate inputs, approvals, decisions, withdrawal, and unattended-publication eligibility;
- `PublicationHandoff` and `AvailabilityChange` production obligations;
- stage order, rerun, reuse, partial failure, batch continuation, and completion semantics;
- focused specification decomposition under `spec:product.pipeline`;
- ADR-first resolution and independent review.

This work item consumes but does not redefine:

- learner-visible path, unit, interaction, phrase, option, summary, attribution, and publication-readiness meaning;
- Application runtime selection, availability-aware retrieval, `LearningUnitRef`, or read-result semantics;
- UI state, navigation, retry presentation, or learner-flow behavior.

This work item excludes:

- programming language, framework, workflow engine, source layout, module layout, database, ORM, SQL, and transport protocol;
- HTTP routes, JSON schemas, deployment, containers, cloud services, and persistence technology;
- exact provider deployment, model selection, prompt text, thresholds, retry delays, and backoff algorithms;
- implementation, runtime integration design, UI detailed design, and Application contract redesign.

A missing normative decision requires an accepted Pipeline ADR before specification reflection.

## Impact Scope

| ref | impact |
|---|---|
| PRODUCT-ADR-PIPELINE-002 | Preserve the OpenAI-compatible provider boundary and provider isolation. |
| PRODUCT-ADR-PIPELINE-005 | Preserve staged deterministic and model processing, source reuse, current-only retention, path multiplicity, and automated publication gating. |
| PRODUCT-INV-PIPELINE-001 | Use the reviewed question-and-reply fixture as evidence for source fidelity, generated-content separation, and provenance needs. |
| PRODUCT-INV-PIPELINE-002 | Use the coarse-tree and path-filtering experiments as evidence for normalization, path enumeration, validation, and harder fixtures. |
| PRODUCT-WORK-LEARNING-001 | Treat the independently reviewed Learning contract as fixed input. |
| `spec:product.pipeline` | Decompose the overview into focused current contracts. |
| `spec:product.learning.learning_path` | Consume path cardinality, adjacency, coherence, suitability, and path-to-unit meaning. |
| `spec:product.learning.learning_unit` | Produce complete units that satisfy content, identity, grounding, attribution, and publication-readiness semantics. |
| `spec:product.learning.quiz_session` | Materialize every immutable learner-visible input required by a session. |
| `spec:product.application.published_content` | Produce atomic current-state writes without changing Application read semantics. |

## Task flow

```text
T01 Establish Pipeline authority baseline and exact gap inventory
  |
  v
T02 Resolve source, normalization, artifact, identity, and provenance decisions
  |
  v
T03 Define deterministic path enumeration and validation contracts
  |
  v
T04 Define summary, phrase, quiz generation, and semantic-validation contracts
  |
  v
T05 Define publication gate, provenance, and publication-output contracts
  |
  v
T06 Define orchestration, retry, rejection, and stage-dependency contracts
  |
  v
T07 Reflect accepted contracts into focused Pipeline specifications
  |
  v
T08 Independently review and close Pipeline detailed design
```

- T01 records current authority, exact gaps, decision points, and the focused specification map.
- T02 resolves source, normalization, artifact, identity, versioning, and provenance decisions through accepted ADRs.
- T03 defines deterministic enumeration, structural validation, absolute filtering, and retained rejection evidence.
- T04 defines bounded generation stages and model-based semantic validation.
- T05 defines the approved publication gate and published-content write outputs.
- T06 defines stage dependencies, retry, rejection, partial failure, rerun, reuse, and batch continuation.
- T07 reflects only accepted decisions into focused Pipeline specifications.
- T08 performs an independent integrated review and records the final readiness verdict.

## Task Candidates

| task | responsibility |
|---|---|
| PRODUCT-TASK-PIPELINE-001-01 | Establish the current Pipeline authority baseline, exact gap inventory, and child-specification plan. |
| PRODUCT-TASK-PIPELINE-001-02 | Resolve source acquisition, normalization, artifact identity, versioning, and provenance decisions. |
| PRODUCT-TASK-PIPELINE-001-03 | Define deterministic path enumeration, structural validation, filtering, and rejection contracts. |
| PRODUCT-TASK-PIPELINE-001-04 | Define summary, target-phrase, prompt, quiz generation, and semantic-validation contracts. |
| PRODUCT-TASK-PIPELINE-001-05 | Define publication readiness, gate approval, handoff, availability change, and withdrawal contracts. |
| PRODUCT-TASK-PIPELINE-001-06 | Define orchestration, retry, incomplete-output, rerun, partial-failure, and completion contracts. |
| PRODUCT-TASK-PIPELINE-001-07 | Reflect accepted Pipeline contracts into focused child specifications. |
| PRODUCT-TASK-PIPELINE-001-08 | Independently review the integrated Pipeline design and close this work item. |

## Completion Condition

- Source acquisition, retained-source reuse, refresh, replacement, source identity, and failure outcomes are explicit.
- Authentic-post normalization preserves authored text, source metadata, author identity, reply meaning, topic-level responses, and unavailable-target distinctions.
- Deterministic path enumeration has explicit inputs, outputs, bounds, identities, duplicate handling, and prefix-overlap behavior.
- Structural validation and semantic suitability filtering are distinct and retain rejection evidence.
- Summary, phrase, prompt, and three-option quiz generation have explicit stage contracts and grounding obligations.
- Semantic option identity and correct-option references remain independent from generated array position.
- Mechanical validation, semantic validation, invalid provider output, contradictory results, retry, rejection, and incomplete units have explicit outcomes.
- Source, normalized artifact, valid path, learning unit, generated content, validators, providers, prompts, and publication decisions have coherent current provenance.
- Pipeline-internal provenance remains opaque outside the published-content boundary.
- Publication gating implements every non-compensating Learning readiness dimension without redefining its meaning.
- Human approval, representative golden and harder fixtures, gate configuration, and unattended-publication eligibility are explicit.
- `PublicationHandoff` and `AvailabilityChange` preserve complete committed current state and availability-only mutation boundaries.
- Orchestration defines stage order, rerun, reuse, retained intermediates, partial failure, batch continuation, and completion semantics.
- Focused Pipeline child specifications replace the overview-only contract while preserving `spec:product.pipeline` as the router.
- Every normative decision traces to an accepted Pipeline ADR before specification reflection.
- Concrete implementation technologies remain excluded.
- An independent final review records `PASS` with no blocking or major finding.
- Pipeline implementation planning can proceed without reconstructing missing stage, artifact, validation, publication, or orchestration semantics.

## Evidence

### Opening basis

PRODUCT-TASK-PRODUCT-001-03 opened this focused work item from the PRODUCT coordination baseline.

The completed PRODUCT-WORK-LEARNING-001 is the fixed semantic input.
PRODUCT-ADR-PIPELINE-002 and PRODUCT-ADR-PIPELINE-005 are current Pipeline decision authority.
PRODUCT-ADR-PIPELINE-001, PRODUCT-ADR-PIPELINE-003, and PRODUCT-ADR-PIPELINE-004 remain superseded history.
PRODUCT-INV-PIPELINE-001 and PRODUCT-INV-PIPELINE-002 remain evidence rather than normative authority.

No child Pipeline specification exists at opening time.
The current `spec:product.pipeline` overview contains broad contracts and publication handoff obligations.

### Opening boundary

- Learning meaning is consumed and not re-decided.
- Application published-content reads remain fixed.
- Pipeline writes and internal provenance remain Pipeline-owned.
- Concrete implementation technology remains outside this design work.
- T01 must identify every missing ADR before any new normative specification text is added.
