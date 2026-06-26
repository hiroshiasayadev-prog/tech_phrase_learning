# PRODUCT-ADR-PIPELINE-004: Use path-based generation and automated publication gating for the first MVP

- **status**: superseded
- **date**: 2026-06-26
- **depends_on**: [PRODUCT-ADR-LEARNING-005, PRODUCT-ADR-PIPELINE-001, PRODUCT-ADR-PIPELINE-002]
- **supersedes**: [PRODUCT-ADR-PIPELINE-003]
- **migrated_to_spec**: 2026-06-26

## Context

PRODUCT-ADR-PIPELINE-003 selected `discuss.python.org` and a manually reviewed segment pipeline.

Later learning decisions replaced one segment per learning unit with two separate concepts:

- a valid source-post path;
- exactly one logical learning unit defined by that path.

The learning contract also removed routine human approval for every learning unit.
Routine item review cannot scale to the expected content volume.

The pipeline still needs human-reviewed evidence for publication criteria, golden fixtures, and model evaluation.
The pipeline must preserve the initial corpus, source provenance, deterministic processing, and bounded model tasks.

## Decision

The first MVP will continue to use public Packaging topics from `discuss.python.org`.

The pipeline will use this flow:

1. discover eligible topics;
2. fetch and retain immutable source snapshots;
3. normalize authored post content and source relationships;
4. create reusable source-post summaries and source-grounded phrase evidence;
5. enumerate bounded connected source-post paths;
6. apply deterministic validation;
7. judge each path independently against learning suitability criteria;
8. retain zero or more valid paths per discussion;
9. revise summaries for path-level conversational continuity when required;
10. select one target quiz phrase per selected post;
11. generate one three-option quiz per selected post;
12. apply an automated publication gate;
13. publish current generated content for the logical learning unit when the gate passes.

The pipeline will not select one canonical path during ingestion.
Prefix-overlapping valid paths may remain available for learning-unit generation.

One valid source-post path defines exactly one logical learning unit.
Regeneration may replace the current generated content for that logical learning unit.
Changing the target phrase or quiz content through regeneration does not create a separate learning unit.
The first MVP will not maintain runtime learning-unit revision history.
Pipeline artifacts will reference source posts instead of copying source ownership into the learning domain.

Phrase selection and quiz generation will remain separate bounded model tasks.

The automated publication gate may combine:

- deterministic schema and provenance validation;
- source-grounding checks;
- model-based quality judgment;
- availability policy.

Humans will approve publication criteria and material changes to those criteria.
Routine learning-unit publication will not require individual human approval.

Human review will remain available for:

- golden fixtures;
- publication-policy development;
- model and prompt evaluation;
- selected borderline or sampled units.

A manually reviewed validation set may contain 50 to 100 representative units.
The validation set is evidence for gate development and does not become a publication prerequisite.

A failed or withdrawn learning unit will become unavailable to new sessions.
Unavailability will preserve source snapshots, source references, evidence, attribution, provenance, pipeline version, model identity, and prompt version.
Unavailability will not create an old unavailable sibling unit when regenerated content becomes available for the same path.

## Rationale

Path-based processing matches the current learning model.
The separation allows one discussion to retain several useful paths.
The separation anchors one logical learning-unit identity to each valid path.

An automated gate provides a scalable publication boundary.
Human-approved criteria retain product control without requiring routine item review.

Golden fixtures and selected manual evaluations provide evidence for improving filters, prompts, schemas, and models.

Immutable source snapshots and versioned pipeline artifacts preserve diagnosis and regeneration.
They do not introduce runtime learning-unit revision history.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Keep one reviewed segment as one learning unit | The current learning contract separates source-post paths from learning units. |
| Select one canonical path per discussion | One discussion may contain several independently valid learning paths. |
| Require human approval for every published learning unit | Routine item review does not scale to the intended content volume. |
| Publish every structurally valid unit | Structural validity does not establish source grounding or learning quality. |
| Remove human review entirely | Golden fixtures and policy evaluation still require human judgment. |
| Delete failed units and their source evidence | Deletion would prevent diagnosis, audit, and regeneration. |
| Send complete topics directly to one model task | The approach would weaken boundedness, reproducibility, and relationship accuracy. |

## Consequences

- PRODUCT-ADR-PIPELINE-003 is superseded.
- The initial `discuss.python.org` Packaging corpus remains unchanged.
- Pipeline specifications must use valid-path and learning-unit terminology.
- Pipeline specifications must replace routine human review with automated publication gating.
- Pipeline specifications must treat one valid path as one logical learning unit with replaceable current content.
- Human-reviewed fixtures remain evaluation evidence rather than a publication queue.
- Deterministic validation and model-based judgment may share one publication result.
- Exact prompts, schemas, thresholds, retries, and model roles belong to pipeline specifications or later architecture work.
- Session-time learning-unit selection remains outside this ADR.
- Source licensing, attribution, retention, and redistribution still require a separate decision or investigation.

## Evidence

- PRODUCT-INV-PIPELINE-002 retained multiple independently valid paths from one discussion.
- PRODUCT-ADR-LEARNING-005 separates source-post paths from learning units.
- PRODUCT-ADR-LEARNING-005 requires automated publication gating under human-approved criteria.
- Earlier generation experiments used bounded model tasks and source-grounded validation.
- Routine human review cannot cover the expected generated content volume.
