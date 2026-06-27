# PRODUCT-WORK-PIPELINE-001: Define first-MVP content-pipeline contracts

- **id**: PRODUCT-WORK-PIPELINE-001
- **status**: in_progress
- **date**: 2026-06-27
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **impact_refs**:
  - PRODUCT-ADR-PIPELINE-002
  - PRODUCT-ADR-PIPELINE-005
  - PRODUCT-ADR-PIPELINE-006
  - PRODUCT-ADR-PIPELINE-007
  - PRODUCT-ADR-PIPELINE-008
  - PRODUCT-ADR-PIPELINE-009
  - PRODUCT-ADR-PIPELINE-010
  - PRODUCT-ADR-PIPELINE-011
  - PRODUCT-ADR-PIPELINE-012
  - PRODUCT-ADR-PIPELINE-013
  - PRODUCT-ADR-PIPELINE-014
  - PRODUCT-ADR-PIPELINE-015
  - PRODUCT-ADR-PIPELINE-016
  - PRODUCT-ADR-PIPELINE-017
  - PRODUCT-ADR-PIPELINE-018
  - PRODUCT-ADR-PIPELINE-019
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
| PRODUCT-ADR-PIPELINE-006 | Apply source-specific adapters, complete-fetch retention, source-independent normalization, and mechanical Discussion Path derivation. |
| PRODUCT-ADR-PIPELINE-007 | Anchor valid-path and Learning Unit identity to ordered authentic posts and replace current content atomically. |
| PRODUCT-ADR-PIPELINE-008 | Retain opaque versioned provenance and support Adapter- or Common-Pipeline-Version withdrawal selection. |
| PRODUCT-ADR-PIPELINE-009 | Derive one bounded candidate per maximal Discussion Path, merge exact duplicates, validate source structure, and retain edge and origin evidence. |
| PRODUCT-ADR-PIPELINE-010 | Filter structurally valid candidates through independent semantic units with positive evidence, bounded invalid-output retry, and deterministic terminal outcomes. |
| PRODUCT-ADR-PIPELINE-011 | Generate reusable summaries from complete authored text and ordered ancestor summaries, then validate four independent fidelity dimensions. |
| PRODUCT-ADR-PIPELINE-012 | Extract zero to three exact same-post phrase candidates and validate conversational function and phrase usefulness independently. |
| PRODUCT-ADR-PIPELINE-013 | Revise accepted summaries in path order for continuity while independently preserving source meaning. |
| PRODUCT-ADR-PIPELINE-014 | Select one evidence-grounded target phrase and generate a non-revealing Quiz prompt through separate validated stages. |
| PRODUCT-ADR-PIPELINE-015 | Generate correct and distractor options through sequential tasks with deterministic identity and individual plus set-level validation. |
| PRODUCT-ADR-PIPELINE-016 | Report controlled stage outcomes, block partial units, aggregate content validation without compensation, and reserve large models for improvement analysis. |
| PRODUCT-ADR-PIPELINE-017 | Require complete non-compensating gate evidence, fail-closed contradiction handling, human-approved fixtures, and validated unattended-publication eligibility. |
| PRODUCT-ADR-PIPELINE-018 | Define publication outcomes, current publication provenance, and the opaque Application-facing provenance boundary. |
| PRODUCT-ADR-PIPELINE-019 | Define atomic `PublicationHandoff`, availability-only `AvailabilityChange`, preservation rules, and writer-reader ownership separation. |
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

### T01 authority baseline and gap inventory

PRODUCT-TASK-PIPELINE-001-01 confirmed two current Pipeline decision authorities:

- PRODUCT-ADR-PIPELINE-002 owns the internal OpenAI-compatible provider boundary and provider isolation.
- PRODUCT-ADR-PIPELINE-005 owns staged processing, retained-source reuse, path multiplicity, current-only retention, replacement, automated publication gating, and unavailability preservation.

The supersession chain is explicit:

```text
PRODUCT-ADR-PIPELINE-005
  +-- supersedes PRODUCT-ADR-PIPELINE-001
  +-- supersedes PRODUCT-ADR-PIPELINE-004
       +-- supersedes PRODUCT-ADR-PIPELINE-003
```

PRODUCT-INV-PIPELINE-001, PRODUCT-INV-PIPELINE-002, fixtures, experiment runs, and scripts remain evidence only.
The completed Learning contract and Application published-content contract remain fixed semantic inputs.

T01 classified all nine Pipeline design areas.
The remaining normative gaps route to T02 through T06 under the ADR-first gate.
Specification elaboration routes to T07 after those decisions are accepted.
Concrete providers, prompts, schemas, algorithms, thresholds, retry timing, persistence, orchestration technology, and deployment remain implementation-only choices.

T01 assigned the follow-up ownership:

| task | owned gap group |
|---|---|
| PRODUCT-TASK-PIPELINE-001-02 | Acquisition, normalization, identity, current generated-content versioning, and provenance. |
| PRODUCT-TASK-PIPELINE-001-03 | Enumeration, structural validation, absolute suitability filtering, duplicates, and rejection evidence. |
| PRODUCT-TASK-PIPELINE-001-04 | Summary, phrase, prompt, quiz generation, grounding, and per-stage validation results. |
| PRODUCT-TASK-PIPELINE-001-05 | Publication gate, unattended eligibility, handoff, withdrawal, restoration, and availability decisions. |
| PRODUCT-TASK-PIPELINE-001-06 | Orchestration, rerun, reuse, retry, exhaustion, partial failure, batch continuation, and completion. |
| PRODUCT-TASK-PIPELINE-001-07 | ADR-backed reflection into focused Pipeline specifications. |

T01 proposed these focused child specifications for T07:

- `spec:product.pipeline.source_acquisition`;
- `spec:product.pipeline.source_normalization`;
- `spec:product.pipeline.path_enumeration`;
- `spec:product.pipeline.path_validation`;
- `spec:product.pipeline.content_generation`;
- `spec:product.pipeline.validation`;
- `spec:product.pipeline.artifact_identity_and_provenance`;
- `spec:product.pipeline.llm_provider`;
- `spec:product.pipeline.publication`;
- `spec:product.pipeline.orchestration`.

`spec:product.pipeline` remains the overview router and cross-area boundary.
T01 did not create or change any ADR or normative specification.

The final post-closure verification run completed successfully:

- `git diff --check` reported no whitespace error;
- LF-to-CRLF messages were non-blocking working-copy warnings;
- strict specification validation returned `[strict]  All 34 file(s) OK.`;
- `git status --short` showed only T01 and this Work Item as modified.

PRODUCT-TASK-PIPELINE-001-01 is `done` and its change scope is commit-ready.
This Work Item remains `in_progress` for T02 through T08.

### T02 accepted Pipeline authority

PRODUCT-TASK-PIPELINE-001-02 materialized its user-approved decision register into three accepted ADRs:

- PRODUCT-ADR-PIPELINE-006 owns acquisition, retained-source reuse, source-specific Adapter normalization, authentic-post identity, Discussion Paths, and normalization outcomes.
- PRODUCT-ADR-PIPELINE-007 owns valid-path identity inputs, stable Learning Unit identity, current-only generated content, and atomic replacement.
- PRODUCT-ADR-PIPELINE-008 owns Pipeline-internal opaque provenance, Source Adapter Version, Common Pipeline Version, publication outcome, and version-targeted withdrawal selection.

No normative specification changed during T02 ADR authoring.
The initial independent review found two minor Task Evidence wording defects.
Both defects were corrected, and the focused re-review returned `PASS` with no regression finding.

Final T02 verification completed successfully.
`git diff --check` completed without reported output.
Strict specification validation returned `[strict]  All 34 file(s) OK.`
`git status --short` showed only the T02 change scope.

PRODUCT-TASK-PIPELINE-001-02 is `done`.
The Work Item remains `in_progress` for T03 through T08.

### T03 accepted Pipeline authority

PRODUCT-TASK-PIPELINE-001-03 materialized its user-approved decision register into two accepted ADRs:

- PRODUCT-ADR-PIPELINE-009 owns bounded candidate derivation, exact duplicate merging, source-only identity, deterministic structural validation, edge evidence, origin provenance, and structural rejection reasons.
- PRODUCT-ADR-PIPELINE-010 owns independent semantic evaluation units, minimal context, positive evidence, full evaluation coverage, bounded invalid-output retry, and deterministic terminal aggregation.

The first MVP does not enumerate every intermediate prefix and does not perform semantic segmentation.
Each maximal Discussion Path yields at most one candidate, bounded to its first six posts.
Longer-path origins remain internal provenance after exact duplicate merging.

Semantic filtering judges each candidate independently.
It separates path coherence, opening-post suitability, and each reply-post suitability into distinct evaluation units.
No sibling ranking or canonical-path selection is introduced.

No normative specification changed during T03 ADR authoring.
Final T03 verification completed successfully.
`git diff --check` completed without reported output.
Strict specification validation returned `[strict]  All 34 file(s) OK.`
`git status --short` showed only the T03 change scope.

PRODUCT-TASK-PIPELINE-001-03 is `done`.
The Work Item remains `in_progress` for T04 through T08.

### T04 accepted Pipeline authority

PRODUCT-TASK-PIPELINE-001-04 materialized its user-approved decision register into six accepted ADRs:

- PRODUCT-ADR-PIPELINE-011 owns reusable-summary context, structured meaning, and four independent fidelity evaluations.
- PRODUCT-ADR-PIPELINE-012 owns bounded exact phrase-evidence extraction, valid zero-candidate outcomes, and independent function and usefulness evaluations.
- PRODUCT-ADR-PIPELINE-013 owns source-order path-specific summary revision and independent preservation and continuity evaluations.
- PRODUCT-ADR-PIPELINE-014 owns grounded target-phrase transformation, non-revealing Quiz prompt generation, and their independent evaluation units.
- PRODUCT-ADR-PIPELINE-015 owns sequential correct-option and distractor generation, deterministic semantic identities, and individual plus set-level option validation.
- PRODUCT-ADR-PIPELINE-016 owns controlled stage outcomes, incomplete-unit handling, localized retained intermediates, non-compensating content-validation aggregation, and large-model improvement analysis.

No normative specification changed during T04 ADR authoring.
Final T04 verification completed successfully.
`git diff --check` completed without reported output.
Strict specification validation returned `[strict]  All 34 file(s) OK.`
`git status --short` showed only the T04 change scope.

PRODUCT-TASK-PIPELINE-001-04 is `done`.
The Work Item remains `in_progress` for T05 through T08.

### T05 accepted Pipeline authority

PRODUCT-TASK-PIPELINE-001-05 materialized its user-approved decision register into three accepted ADRs:

- PRODUCT-ADR-PIPELINE-017 owns complete non-compensating publication-gate evidence, fail-closed contradictory-state handling, human approval, harder-fixture validation, and unattended-publication eligibility.
- PRODUCT-ADR-PIPELINE-018 owns publication and availability outcome meanings, current publication provenance, and opaque Application-facing provenance references.
- PRODUCT-ADR-PIPELINE-019 owns `PublicationHandoff`, `AvailabilityChange`, atomic complete-current-state replacement, availability-only preservation, and Pipeline-writer/Application-reader separation.

No normative specification changed during T05 ADR authoring.
Final T05 verification completed successfully.
`git diff --check` completed without reported error.
Strict specification validation returned `[strict]  All 34 file(s) OK.`
`git status --short` showed only the T05 Task, this Work Item, and three new T05 ADRs.

PRODUCT-TASK-PIPELINE-001-05 is `done`.
The Work Item remains `in_progress` for T06 through T08.
