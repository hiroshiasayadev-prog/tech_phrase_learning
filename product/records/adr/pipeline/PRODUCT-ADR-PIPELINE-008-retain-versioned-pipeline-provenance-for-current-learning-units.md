# PRODUCT-ADR-PIPELINE-008: Retain versioned Pipeline provenance for current Learning Units

- **status**: accepted
- **date**: 2026-06-27
- **depends_on**:
  - PRODUCT-ADR-PIPELINE-002
  - PRODUCT-ADR-PIPELINE-005
  - PRODUCT-ADR-PIPELINE-006
  - PRODUCT-ADR-PIPELINE-007
  - PRODUCT-ADR-LEARNING-012
  - PRODUCT-ADR-APPLICATION-003
- **supersedes**:
- **migrated_to_spec**:

## Context

The first MVP retains current generated content and current provenance without generation history.

The Pipeline needs enough current evidence to trace one Learning Unit to its authentic source and processing behavior.
The Application must not interpret Pipeline processing details.

Adapter defects and common Pipeline defects may affect many current Learning Units.
The product needs a way to identify affected units without introducing runtime revision history.

## Decision

Each current Learning Unit will have one Pipeline-owned provenance bundle.

The bundle will link the current Learning Unit to:

- the retained authentic discussion;
- the current normalized authentic conversation;
- the valid Learning Path;
- stage-specific provider provenance;
- stage-specific prompt provenance;
- validation results;
- Source Adapter Version;
- Common Pipeline Version;
- the resulting publication outcome.

The Application will receive only one opaque provenance reference.
Application code and the PWA must not parse or interpret the provenance bundle.

### Version meanings

Source Adapter Version identifies one release-level source-specific behavior set.
The behavior set includes normalization, quote separation, relationship interpretation, authentic-post identity materialization, and Discussion Path derivation.

Common Pipeline Version identifies one release-level shared behavior set.
The behavior set includes Learning Path processing, content generation, validation, and publication behavior.

Both versions identify behavior releases rather than individual executions.
A Pipeline run identifier, when needed for diagnostics, is not a substitute for either version.

Exact version syntax and release tooling remain implementation choices.

### Publication outcome

A Learning Unit that successfully completes the approved Common Pipeline publication gate will become the current published Learning Unit.
The Pipeline will not add a separate per-unit publication-decision identity after gate completion.

The current provenance bundle will record the gate and publication outcome that matches the current content.
Current content and current provenance must be replaced together under PRODUCT-ADR-PIPELINE-007.

### Version-targeted withdrawal

Current provenance must allow Pipeline operations to select current Learning Units by either:

- Source Adapter Version;
- Common Pipeline Version.

A selected set may receive an availability-only bulk withdrawal.
The withdrawal must preserve current content and current provenance.

Exact selection commands, authorization, restoration, batching, and mutation mechanics remain later publication and orchestration decisions.

## Rationale

One provenance bundle keeps source, generation, validation, and publication evidence aligned with current content.

Separate adapter and common Pipeline versions localize defects to the behavior boundary that introduced them.
Release-level versions group all units exposed to the same processing defect.
Execution identifiers would be too narrow for that purpose.

Opaque Application handling preserves the Pipeline ownership boundary.
Version-targeted availability withdrawal contains defects without deleting source evidence or introducing revision history.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Expose provider, prompt, or version fields to Application readers | Application must not depend on Pipeline internals. |
| Store only one undifferentiated Pipeline version | Adapter defects and shared Pipeline defects require different affected-unit scopes. |
| Use one version per execution | Run-level identity is too narrow for release-level defect containment. |
| Record one provider or prompt for the whole unit | Different generation and validation stages may use different configurations. |
| Create a separate publication-decision identity after gate success | The successful approved gate outcome already defines the publication outcome. |
| Delete units affected by a defective version | Availability withdrawal must preserve current content, source routes, and provenance. |
| Retain every historical provenance bundle | The first MVP does not require runtime generation history or rollback. |

## Consequences

- T04 must expose stage-specific provider, prompt, and validation evidence for current provenance.
- T05 must define publication outcome, availability withdrawal, restoration, and handoff semantics.
- T06 must define run diagnostics separately from release-level Adapter and Common Pipeline Versions.
- T07 must reflect opaque provenance and version meanings into focused Pipeline specifications.
- Current units can be selected for withdrawal by either processing-version boundary.
- Application runtime reads remain independent from Pipeline version and provenance structure.
- Exact version format, provenance schema, storage layout, and bulk-operation implementation remain deferred.

## Evidence

- PRODUCT-TASK-PIPELINE-001-01 identified provider, prompt, validator, publication, and opaque provenance as missing Pipeline authority.
- PRODUCT-ADR-PIPELINE-002 establishes provider isolation and untrusted model output.
- PRODUCT-ADR-LEARNING-012 establishes the approved publication-readiness gate meaning.
- PRODUCT-ADR-APPLICATION-003 requires one matching opaque provenance reference in current published state.
- The user selected one Pipeline-owned provenance bundle with stage-specific evidence.
- The user selected separate Source Adapter Version and Common Pipeline Version concepts.
- The user selected release-level versions and version-targeted availability-only bulk withdrawal.
- The user selected successful approved Pipeline completion as immediate publication without a second per-unit decision layer.
