# PRODUCT-ADR-PIPELINE-021: Reuse current artifacts and rerun from the earliest affected stage

- **status**: superseded
- **date**: 2026-06-28
- **depends_on**:
  - PRODUCT-ADR-PIPELINE-005
  - PRODUCT-ADR-PIPELINE-006
  - PRODUCT-ADR-PIPELINE-007
  - PRODUCT-ADR-PIPELINE-008
  - PRODUCT-ADR-PIPELINE-016
  - PRODUCT-ADR-PIPELINE-017
  - PRODUCT-ADR-PIPELINE-019
  - PRODUCT-ADR-PIPELINE-020
- **supersedes**:
- **migrated_to_spec**:

## Context

The Pipeline retains current authentic source, normalized source, generated artifacts, validation evidence, and publication state.
A rerun must reuse accepted work when safe without silently combining artifacts produced from different inputs or behaviors.

PRODUCT-ADR-PIPELINE-005 establishes current-only retention.
PRODUCT-ADR-PIPELINE-007 preserves valid-path and Learning Unit identity across regeneration.
PRODUCT-ADR-PIPELINE-008 retains Source Adapter Version, Common Pipeline Version, stage-specific provider and prompt provenance, validation evidence, and publication outcome.

The missing contract is which artifacts are reusable, what execution-behavior evidence must remain current, and where rerun begins after source, Adapter, orchestration, prompt, provider, validator, gate, or publication changes.

## Decision

### Current retained artifacts

The Pipeline will retain current reusable or publication-relevant artifacts.

Current retained data includes:

- retained authentic source;
- current normalized authentic conversation;
- current valid paths and current rejection evidence;
- accepted reusable summaries;
- accepted source-grounded phrase evidence;
- accepted path-local intermediates required to resume current processing;
- current validation, publication-gate, and provenance evidence for committed published content.

Raw provider requests and responses, invalid retry attempts, temporary calculations, superseded intermediates, historical generations, and complete attempt history are not required.
They may be transient or overwritten after current diagnosis no longer requires them.

### Shared and path-specific reuse

Artifacts independent from one selected Learning Path may be reused across sibling paths.

Shared reusable artifacts are:

- retained authentic source;
- current normalized authentic conversation;
- accepted reusable source-post summaries;
- accepted source-grounded phrase evidence.

Path-specific artifacts are:

- path-specific summary revisions;
- selected target phrases;
- Quiz prompts;
- correct and distractor options;
- complete Learning Unit candidates;
- path-local validation results;
- publication-gate and publication outcomes.

When multiple valid paths include the same authentic post, they may consume the same accepted reusable summary and phrase evidence.
Processing becomes path-specific at path-specific summary revision and remains path-specific afterward.

One path-specific failure does not invalidate accepted shared artifacts or sibling-path results.

### Execution-behavior version evidence

Current provenance will continue to retain the accepted Source Adapter Version and Common Pipeline Version.

It will also identify the exact current orchestration behavior and participating component behavior required to determine reuse and rerun validity.
This includes applicable references for:

- Source Adapter behavior;
- orchestration behavior;
- providers;
- generation prompts;
- evaluator prompts and evaluator behavior;
- deterministic validators;
- publication-gate configuration.

A reference must identify the behavior used for the current result.
Exact representation through module names, Python file names, package versions, Git commits, build artifacts, or manifests remains an implementation choice.
No generated-artifact revision identity or permanent execution-history identity is introduced.

### Conservative rerun rule

A rerun will begin at the earliest stage whose accepted input, behavior, provider, prompt, validator, or configuration may have changed.
Only accepted upstream artifacts proven current and unaffected may be reused.

A narrow component-suffix rerun is allowed as an optimization.
When the Pipeline cannot prove a narrower unaffected boundary, it will rerun the complete Common Pipeline from its first common-processing stage.

A Common Pipeline rerun may reuse retained authentic source and current normalized source when Source Adapter behavior and normalized input remain unchanged.
A Source Adapter behavior change requires re-normalization from retained authentic source.
A retained-source replacement requires re-normalization and every dependent stage.

### Material-change boundaries

| material change | default rerun start |
|---|---|
| Retained authentic source replacement | Normalization and every dependent downstream stage. |
| Source Adapter behavior change | Normalization and every dependent downstream stage. |
| Common Pipeline orchestration or composition change | First Common Pipeline processing stage. |
| Provider or generation-prompt change | Earliest affected generation stage. |
| Evaluator-prompt or evaluator-behavior change | Earliest affected evaluation stage. |
| Deterministic-validator change | Earliest affected deterministic validation stage. |
| Publication-gate configuration change | Gate evaluation, unless the change also invalidates upstream evidence. |
| Failed publication write with unchanged accepted handoff | Retry only the failed write operation. |
| Withdrawal or restoration request | Execute only the applicable `AvailabilityChange`; do not rerun content generation. |

A narrower boundary is valid only when unaffected current artifacts can be proven compatible with current inputs and behavior references.

### Stable identity under rerun

Rerun will preserve valid-path and Learning Unit identity when the authentic discussion and ordered authentic-post path remain unchanged.

Provider, prompt, evaluator, validator, gate, orchestration, and component behavior changes are not identity inputs.
They may replace current generated content and current provenance under the same stable Learning Unit identity.

A rerun must not create a sibling Learning Unit solely because current content or behavior evidence changed.

## Rationale

Current-only retention keeps first-MVP storage and reasoning bounded.
Separating shared from path-specific artifacts prevents repeated source-post work while preserving path-local meaning.

Version evidence is needed to prove that a retained artifact remains compatible with the active behavior.
Keeping representation implementation-defined avoids turning source layout or filenames into product contracts.

Starting at the earliest affected stage preserves accepted work when impact can be demonstrated.
Falling back to a complete Common Pipeline rerun is safer while the Pipeline composition remains likely to change.

Stable identity preserves one logical Learning Unit across regeneration and avoids leaking implementation revisions into Application semantics.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Always discard all artifacts and refetch source | Accepted source and validated shared work would be repeated unnecessarily. |
| Always perform narrow suffix reruns | Early implementation may not prove every dependency safely. |
| Reuse artifacts without behavior references | Inputs could be combined with outputs produced under incompatible prompts, providers, or validators. |
| Put version numbers in required Python filenames | Physical layout and naming are implementation choices. |
| Retain every model exchange and attempt forever | Current diagnosis and publication do not require complete historical replay. |
| Create a new Learning Unit identity after regeneration | Identity is anchored to the authentic ordered post path, not generated content. |
| Rerun content generation for withdrawal or restoration | Availability-only changes preserve current content and provenance. |

## Consequences

- Current source, normalized source, shared summaries, and phrase evidence can be reused when proven compatible.
- Path-specific artifacts remain isolated from sibling-path failure.
- Current provenance can identify orchestration and participating component behavior in addition to accepted release-level versions.
- Narrow rerun is optional; conservative Common Pipeline rerun is the safe fallback.
- Source Adapter changes re-normalize without refetch when complete retained source remains available.
- Publication-write retry and availability-only operations do not regenerate content when their inputs remain current.
- Stable valid-path and Learning Unit identity survive compatible reruns.
- T07 must reflect current retention, reuse, version evidence, and rerun boundaries into Pipeline identity, provenance, validation, and orchestration specifications.
- Exact dependency graphs, cache invalidation, storage layout, version syntax, package structure, and source layout remain deferred.

## Evidence

- PRODUCT-ADR-PIPELINE-005 establishes staged processing and current-only retention.
- PRODUCT-ADR-PIPELINE-006 establishes retained-source reuse and replaceable current normalization.
- PRODUCT-ADR-PIPELINE-007 establishes stable path-derived Learning Unit identity and atomic current replacement.
- PRODUCT-ADR-PIPELINE-008 establishes release-level Adapter and Common Pipeline versions plus stage-specific provenance.
- PRODUCT-ADR-PIPELINE-016 permits accepted intermediate reuse while localizing failure.
- PRODUCT-ADR-PIPELINE-019 separates complete publication replacement from availability-only mutation.
- The user selected current-only reusable artifacts, separately identifiable orchestration and component behavior, conservative complete Common Pipeline rerun when impact is uncertain, and earliest-affected-stage rerun when compatibility is proven.
