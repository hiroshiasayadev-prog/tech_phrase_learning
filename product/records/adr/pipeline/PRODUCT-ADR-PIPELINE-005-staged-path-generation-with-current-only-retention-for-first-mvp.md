# PRODUCT-ADR-PIPELINE-005: Use staged path generation with current-only retention for the first MVP

- **status**: accepted
- **date**: 2026-06-26
- **depends_on**: [PRODUCT-ADR-LEARNING-005]
- **supersedes**: [PRODUCT-ADR-PIPELINE-001, PRODUCT-ADR-PIPELINE-004]
- **migrated_to_spec**: 2026-06-26

## Context

PRODUCT-ADR-PIPELINE-001 established deterministic processing before bounded LLM augmentation.
PRODUCT-ADR-PIPELINE-004 established path-based generation and automated publication gating.

Both ADRs also required immutable source snapshots or persisted intermediate artifacts.
The first MVP does not need historical pipeline generations, exact replay, or rollback.

Source API capacity is limited.
Repeatedly fetching an unchanged source URL would add cost without improving the phrase-learning goal.
The learning value does not require synchronization with later edits to the technical discussion.

The pipeline still needs current source grounding, explicit stages, validation, and publication provenance.

## Decision

The first MVP will use staged deterministic and LLM processing.

Deterministic stages will own mechanically observable processing.

Examples, not exhaustive:

- source parsing and relationship preservation;
- markup cleanup and normalization;
- path enumeration and structural validation;
- deduplication and stable candidate identity.

Bounded LLM tasks will own semantic interpretation and generation.

Examples, not exhaustive:

- path suitability judgment;
- source-post summarization;
- target-phrase selection;
- quiz-option generation;
- model-based publication judgment.

Each model task will receive the smallest sufficient context.
Each task will use a structured output contract when practical.
Application code will validate every model-produced structure.
Invalid output may be retried, rejected, or selected for review.

The first MVP will continue to use public Packaging topics from `discuss.python.org`.

The pipeline will use this flow:

1. discover eligible topics;
2. reuse retained source data for a known source URL, or fetch the source when no reusable record exists;
3. normalize authored post content and source relationships;
4. create reusable source-post summaries and source-grounded phrase evidence;
5. enumerate bounded connected source-post paths;
6. apply deterministic validation;
7. judge each path independently against learning suitability criteria;
8. retain zero or more valid paths per discussion;
9. revise summaries for path-level continuity when required;
10. select one target quiz phrase per selected post;
11. generate one three-option quiz per selected post;
12. apply an automated publication gate;
13. publish current generated content for the logical learning unit when the gate passes.

The pipeline will not select one canonical path during ingestion.
Each path will be judged independently against learning suitability criteria.
Prefix-overlapping valid paths may coexist.

One valid source-post path defines exactly one logical learning unit.
Regeneration replaces current generated content for that logical learning unit.
Generated phrase or quiz changes do not create sibling learning units.
The first MVP will not maintain runtime learning-unit revision history.
Pipeline artifacts will reference source posts instead of copying source ownership into the learning domain.

Phrase selection and quiz generation will remain separate bounded model tasks.

The pipeline may reuse retained source data after one successful fetch for a source URL.
The first MVP will not require periodic refetch or source-freshness guarantees.

The pipeline will retain only data needed for current processing and current publication:

- reusable current source data;
- current generated learning-unit content;
- current source references and learner-visible attribution;
- current validation and publication provenance.

Intermediate stage outputs may be transient or overwritten after downstream use.
The first MVP will not require historical source snapshots or intermediate generations.
The first MVP will not require previous publication revisions, exact replay, or rollback state.

The pipeline will preserve explicit stage boundaries and current-run diagnostics.
The pipeline will not preserve historical stage output solely for diagnosis.

The automated publication gate may combine:

- deterministic schema and provenance validation;
- source-grounding checks;
- model-based quality judgment;
- availability policy.

Humans will approve publication criteria and material changes to those criteria.
Routine publication will not require individual human approval.

Human review will remain available for:

- golden fixtures;
- publication-policy development;
- model and prompt evaluation;
- selected borderline or sampled units.

A manually reviewed validation set may contain 50 to 100 representative units.
The validation set is evidence for gate development and is not a publication prerequisite.

A failed or withdrawn learning unit will become unavailable to new sessions.
Unavailability will preserve current content, source references, attribution, and current publication provenance.
Unavailability will not create an old unavailable sibling when regenerated content becomes available for the same path.

## Rationale

Deterministic processing remains cheaper, reproducible, and easier to test than model-based processing.
Bounded LLM tasks reduce context size and provider requirements.

Current retained source data avoids unnecessary API requests.
Phrase learning does not require later source edits to update existing learning material automatically.

Historical artifact retention would introduce generation identity, lifecycle, storage, and cleanup complexity.
The first MVP receives little value from exact reconstruction or rollback.

Current-run diagnostics and validated current outputs provide enough operational visibility.
The current source and provenance route provide enough grounding for learner-visible content.

Automated publication gating scales better than routine human approval.
Golden fixtures and sampled review remain available for policy and model evaluation.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Retain immutable source snapshots and every intermediate generation | Historical reconstruction does not justify the first-MVP lifecycle and storage complexity. |
| Refetch every known source URL before processing | Repeated requests consume source API capacity without improving the learning goal. |
| Guarantee synchronization with later source edits | Source freshness is not required for phrase-learning usefulness. |
| Require exact replay and rollback | The first MVP does not need historical publication recovery. |
| Send complete topics to one model task | The approach weakens boundedness, validation, and failure diagnosis. |
| Select one canonical path per discussion | One discussion may contain several independently valid learning paths. |
| Require human approval for every learning unit | Routine item review does not scale to the expected content volume. |

## Consequences

- PRODUCT-ADR-PIPELINE-001 and PRODUCT-ADR-PIPELINE-004 are superseded.
- Their deterministic-stage, bounded-LLM, path-generation, cardinality, and publication-gate decisions remain active through this ADR.
- The pipeline may process the same source URL without another network request.
- The first MVP provides no source-freshness or periodic-synchronization guarantee.
- Intermediate stage data may be transient or overwritten.
- Historical source snapshots and intermediate generations are not required.
- Previous publication revisions, exact replay, and rollback are not required.
- Model or prompt changes may replace current content from retained source data.
- Current source references, attribution, and publication provenance remain required.
- Concrete prompts, schemas, thresholds, retries, storage mechanisms, and provider assignments remain later design work.
- Source licensing, attribution, retention duration, and redistribution remain separate concerns.

## Evidence

- PRODUCT-TASK-APPLICATION-002-03 identified retention as an architectural decision requiring an ADR.
- The user selected source reuse because source API capacity is limited.
- The user rejected periodic refetch and freshness guarantees for the first MVP.
- The user rejected historical source, intermediate, and publication generations.
- The existing pipeline specification already separates current publication from processing data.
