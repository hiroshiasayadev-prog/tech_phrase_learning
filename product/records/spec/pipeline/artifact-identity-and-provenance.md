# Concept: Pipeline artifact identity and provenance

- **id**: `spec:product.pipeline.artifact_identity_and_provenance`
- **status**: draft
- **date**: 2026-06-28
- **parent**: `spec:product.pipeline`

## What this is

Pipeline contract for current artifact identity, reusable artifact scope, processing-behavior evidence, and opaque publication provenance.
The contract preserves stable source-grounded Learning Unit identity without introducing generated-content revision history.

## Non-goals

- Identifier encoding, hash algorithms, UUID selection, or persistence keys.
- Historical source snapshots, generated revisions, or rollback state.
- Permanent raw provider request and response retention.
- Application interpretation of Pipeline provenance.
- Concrete version syntax, package layout, or source-file naming.

## Concept model

| artifact or identity | contract |
|---|---|
| Authentic discussion identity | Identity established by the canonical discussion URL and retained authentic source. |
| Authentic-post identity | Adapter-materialized identity unique within one retained authentic discussion. |
| Normalized artifact | At most one current source-independent authentic conversation for one authentic discussion. |
| Valid Learning Path identity | Candidate identity retained unchanged after acceptance under `spec:product.pipeline.path_enumeration` and `spec:product.pipeline.path_validation`. |
| Stable Learning Unit identity | One identity materialized from one retained valid Learning Path identity. |
| Current generated content | The complete current content under one stable Learning Unit identity. |
| Current provenance bundle | Pipeline-owned evidence matching one current generated result or committed publication. |
| Opaque provenance reference | Application-facing reference to the matching current Pipeline provenance bundle. |

## Rules

### Valid-path and Learning Unit continuity

- Candidate identity is defined only by `spec:product.pipeline.path_enumeration`.
- Structural and semantic acceptance must retain the candidate identity unchanged as the valid Learning Path identity.
- Each retained valid Learning Path must materialize exactly one stable Learning Unit identity.
- Distinct candidate identities must remain distinct valid-path and Learning Unit identities.
- Summaries, phrase evidence, target phrases, prompts, options, providers, validators, and generated values must not alter valid-path or Learning Unit identity.
- Concrete valid-path and Learning Unit identity representation remains an implementation choice.

### Current-only artifact model

The Pipeline must retain current reusable or publication-relevant artifacts.

| retained current artifact | retention purpose |
|---|---|
| Retained authentic source | Current source evidence and reuse. |
| Normalized authentic conversation | Current Common Pipeline input. |
| Valid paths and candidate rejection evidence | Current path outcomes and diagnosis. |
| Accepted reusable summaries | Shared source-post meaning for filtering and sibling paths. |
| Accepted source-grounded phrase evidence | Shared same-post phrase evidence. |
| Accepted path-local intermediates | Resume current path processing from an unaffected stage. |
| Validation and publication-gate evidence | Prove current readiness and publication decisions. |
| Current publication provenance | Match committed current content and availability decisions. |

- Regeneration must replace current generated content under the same stable Learning Unit identity when source identity remains unchanged.
- The Pipeline must not create a sibling Learning Unit solely because generated content or processing behavior changed.
- The first MVP does not require a generated-content instance identity.
- The first MVP does not expose a Learning Unit revision identity.
- Historical normalized artifacts, generated intermediates, and previous publications are not required.
- Raw provider exchanges, invalid retry attempts, temporary calculations, and complete attempt history may be transient or overwritten.

### Shared and path-specific artifacts

| reuse scope | artifacts |
|---|---|
| Shared across compatible sibling paths | Retained authentic source, normalized authentic conversation, accepted reusable summaries, and accepted phrase evidence. |
| Path-specific | Summary revisions, target phrases, Quiz prompts, options, complete unit candidates, path-local validation, publication gate, and publication outcomes. |

- Processing becomes path-specific at path-specific summary revision.
- One path-specific failure must not invalidate accepted shared artifacts.
- Shared artifacts may be reused only when their inputs and relevant behavior evidence remain current and compatible.
- Path-specific artifacts may be reused only within the same valid-path identity and compatible dependent chain.

### Processing behavior evidence

Each current provenance bundle must identify the behavior required to explain and validate the current result.

Required behavior evidence includes, when applicable:

- Source Adapter Version;
- Common Pipeline Version;
- source discovery, canonicalization, deduplication, acquisition, interpretation, and normalization behavior;
- orchestration behavior;
- generation providers and prompts;
- evaluator providers, prompts, and evaluator behavior;
- deterministic validators;
- publication-gate configuration;
- stage results and publication outcome.

- Source Adapter Version identifies one release-level source-specific behavior set.
- Common Pipeline Version identifies one release-level shared Pipeline behavior set.
- A Pipeline run identifier does not replace either behavior version.
- Behavior references must identify the behavior used for the current result.
- Exact representation of behavior references remains an implementation choice.

### Current provenance bundle

Each current Learning Unit result must have one Pipeline-owned provenance bundle linking it to:

- retained authentic discussion;
- current normalized authentic conversation;
- valid Learning Path;
- stage-specific provider and prompt evidence;
- evaluator and deterministic-validator evidence;
- current validation results;
- Source Adapter Version and Common Pipeline Version;
- orchestration and participating component behavior;
- publication-gate configuration and fixture-validation evidence when published;
- resulting publication and availability outcome.

- Current content and its matching current provenance must change together during complete replacement.
- Availability-only changes must preserve current content provenance and its opaque reference.
- Separate Pipeline-internal evidence may record the current availability decision.
- Current provenance must support selecting affected current Learning Units by Source Adapter Version or Common Pipeline Version.
- Selection by processing version does not itself mutate published state.

### Opaque Application boundary

- Application-facing current state must contain only one opaque provenance reference.
- The opaque reference must identify the Pipeline provenance bundle matching committed current content.
- Application code and the PWA must not parse the reference.
- Application code and the PWA must not inspect providers, prompts, validators, versions, gate evidence, rejection causes, or retry history.
- Provenance must not enter `LearningUnitRef` or runtime selection logic.
- A rejected unpublished candidate must not receive an Application-facing current-state provenance reference.

### Identity under rerun

- Rerun may preserve path and Learning Unit identity only after authentic discussion identity and ordered authentic-post identities remain unchanged.
- Provider, prompt, evaluator, validator, gate, orchestration, and component behavior changes are not identity inputs.
- Canonicalization, acquisition, normalization, post-identity, or Discussion Path changes may change source-grounded identity.
- The Pipeline must not preserve an identity whose source basis is no longer equivalent.
- Rerun start and compatibility decisions belong to `spec:product.pipeline.orchestration`.

## Boundary

| concern | owner |
|---|---|
| Candidate identity, duplicate handling, and origin evidence | `spec:product.pipeline.path_enumeration`. |
| Valid-path identity retention, stable Learning Unit materialization, and current artifact continuity | `spec:product.pipeline.artifact_identity_and_provenance`. |
| Learner-visible Learning Unit identity meaning | `spec:product.learning.learning_unit`. |
| Reuse and rerun execution | `spec:product.pipeline.orchestration`. |
| Publication mutation and availability changes | `spec:product.pipeline.publication`. |
| Committed runtime state and provenance opacity | `spec:product.application.published_content`. |
| Identifier and persistence implementation | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.pipeline` | Parent Pipeline overview. |
| `spec:product.pipeline.source_acquisition` | Establishes retained authentic source. |
| `spec:product.pipeline.source_normalization` | Establishes the current normalized artifact. |
| `spec:product.pipeline.path_enumeration` | Defines candidate identity, duplicate handling, and origin evidence. |
| `spec:product.pipeline.content_generation` | Produces shared and path-specific current artifacts. |
| `spec:product.pipeline.publication` | Commits content with matching opaque provenance. |
| `spec:product.pipeline.orchestration` | Applies compatibility and rerun boundaries. |
| `spec:product.application.published_content` | Reads only committed state and opaque provenance. |
| PRODUCT-ADR-PIPELINE-005 | Establishes current-only retention and replacement. |
| PRODUCT-ADR-PIPELINE-007 | Establishes source-path identity and stable Learning Unit replacement. |
| PRODUCT-ADR-PIPELINE-008 | Establishes current Pipeline provenance and behavior versions. |
| PRODUCT-ADR-PIPELINE-018 | Establishes current publication provenance and opacity. |
| PRODUCT-ADR-PIPELINE-024 | Establishes shared reuse, component evidence, and identity preservation under rerun. |
