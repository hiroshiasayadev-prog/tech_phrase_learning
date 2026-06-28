# PRODUCT-ADR-PIPELINE-024: Reuse compatible current artifacts and rerun from the earliest affected source or common stage

- **status**: accepted
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
  - PRODUCT-ADR-PIPELINE-021
- **migrated_to_spec**: 2026-06-28

## Context

PRODUCT-ADR-PIPELINE-021 established current artifact reuse, execution-behavior evidence, conservative rerun, and stable identity preservation.

Its Source Adapter change rule started every Adapter-triggered rerun at normalization from retained authentic source.
That boundary is too late for Adapter changes that affect listing discovery, canonical URL identity, same-crawl deduplication, source fetching, completeness judgment, or acquisition interpretation.
Those changes may invalidate the discussion selected for retained-source lookup or the compatibility of the retained source itself.

The material-change table also grouped provider changes with generation stages even though an evaluator-provider change must begin at evaluation.

This ADR supersedes PRODUCT-ADR-PIPELINE-021 in full.
It preserves its current-retention, reuse, behavior-evidence, conservative-rerun, and stable-identity contracts while correcting source-side and evaluator-provider rerun boundaries.

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
Applicable references include:

- Source Adapter discovery, canonicalization, deduplication, acquisition, interpretation, and normalization behavior;
- orchestration behavior;
- generation providers;
- evaluator providers;
- generation prompts;
- evaluator prompts and evaluator behavior;
- deterministic validators;
- publication-gate configuration.

A reference must identify the behavior used for the current result.
Exact representation through module names, Python file names, package versions, Git commits, build artifacts, or manifests remains an implementation choice.
No generated-artifact revision identity or permanent execution-history identity is introduced.

### Conservative rerun rule

A rerun will begin at the earliest stage whose accepted input, source identity, acquisition evidence, behavior, provider, prompt, validator, or configuration may have changed.
Only accepted upstream artifacts proven current, compatible, and unaffected may be reused.

A narrow component-suffix rerun is allowed as an optimization.
When the Pipeline cannot prove a narrower unaffected boundary within the Common Pipeline, it will rerun the complete Common Pipeline from its first common-processing stage.

When the Pipeline cannot isolate the impact of a Source Adapter change, it will rerun from Source Adapter discovery.
It will canonicalize discovered URLs again and repeat retained-source lookup before deciding whether any retained authentic source remains reusable.

### Source Adapter change classes

Source Adapter changes will be classified by the earliest source-side behavior they can affect.

| Source Adapter change class | default rerun start and reuse rule |
|---|---|
| Listing discovery, eligibility, URL extraction, canonicalization, or same-crawl deduplication | Rerun Source Adapter discovery, canonicalize again, deduplicate again, and repeat retained-source lookup using the newly established canonical URL. Do not assume the previously selected discussion identity remains valid. |
| Fetch execution, source request construction, complete-fetch determination, fetch-result interpretation, or acquisition evidence | Reevaluate acquisition compatibility. Reuse retained authentic source only when compatibility with the changed acquisition behavior is proven; otherwise reacquire and establish complete retained source before normalization. |
| Source normalization, quote separation, relationship interpretation, authentic-post identity materialization, or Discussion Path derivation | Reuse compatible complete retained authentic source and rerun normalization plus every dependent stage. |
| Adapter change whose affected source-side boundary cannot be isolated | Rerun from Source Adapter discovery and repeat canonical URL lookup and acquisition decisions conservatively. |

A Source Adapter version change is not by itself permission to reuse retained source from normalization.
Reuse depends on the affected Adapter behavior and proven compatibility of the canonical discussion identity, acquisition evidence, and retained authentic source.

### Other material-change boundaries

| material change | default rerun start |
|---|---|
| Retained authentic source replacement | Normalization and every dependent downstream stage. |
| Common Pipeline orchestration or composition change | First Common Pipeline processing stage. |
| Generation provider or generation-prompt change | Earliest affected generation stage. |
| Evaluator provider, evaluator prompt, or evaluator behavior change | Earliest affected evaluation stage. |
| Deterministic-validator change | Earliest affected deterministic validation stage. |
| Publication-gate configuration change | Gate evaluation, unless the change also invalidates upstream evidence. |
| Failed publication write with unchanged accepted handoff | Retry only the failed write operation. |
| Withdrawal or restoration request | Execute only the applicable `AvailabilityChange`; do not rerun content generation or the publication gate. |

A narrower boundary is valid only when unaffected current artifacts can be proven compatible with current inputs, source identity, acquisition evidence, and behavior references.

### Stable identity under rerun

Rerun will preserve valid-path and Learning Unit identity only when the authentic discussion identity and ordered authentic-post path remain unchanged after all required source-side reevaluation.

Provider, prompt, evaluator, validator, gate, orchestration, and component behavior changes are not identity inputs.
They may replace current generated content and current provenance under the same stable Learning Unit identity when the source-grounded identity inputs remain unchanged.

A canonicalization, acquisition, normalization, post-identity, or Discussion Path change may alter the authentic discussion or ordered-post identity inputs.
In that case, the Pipeline will not preserve an identity whose source basis is no longer the same.

A rerun must not create a sibling Learning Unit solely because current generated content or behavior evidence changed.

## Rationale

Current-only retention keeps first-MVP storage and reasoning bounded.
Separating shared from path-specific artifacts prevents repeated source-post work while preserving path-local meaning.

Behavior evidence is required to prove retained-artifact compatibility.
Keeping its representation implementation-defined avoids turning source layout or filenames into product contracts.

Starting at the earliest affected source or Common Pipeline stage prevents reuse of a retained discussion selected under incompatible discovery or canonicalization behavior.
Separating acquisition compatibility from normalization compatibility prevents changed fetch-completeness or source-interpretation rules from silently trusting stale evidence.

Separating generation-provider and evaluator-provider changes aligns the rerun boundary with the actual affected operation.

Stable identity remains valid only after source identity and ordered-post inputs are shown unchanged.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Start every Source Adapter change at normalization | Discovery, canonicalization, deduplication, and acquisition changes can invalidate the retained discussion or retained-source compatibility before normalization. |
| Always discard retained source after any Adapter change | Normalization-only changes can safely reuse compatible complete retained source. |
| Always refetch every retained discussion | Acquisition reuse remains valid when compatibility is proven. |
| Always perform narrow suffix reruns | Early implementations may not prove every dependency safely. |
| Reuse artifacts without behavior and source-compatibility evidence | Inputs could be combined with outputs produced under incompatible discovery, acquisition, prompts, providers, or validators. |
| Put version numbers in required Python filenames | Physical layout and naming are implementation choices. |
| Retain every provider exchange and attempt forever | Current diagnosis and publication do not require complete historical replay. |
| Treat evaluator-provider change as generation change | The earliest affected operation is evaluation, not generation. |
| Create a new Learning Unit identity after every regeneration | Identity remains anchored to the authentic discussion and ordered authentic-post path. |
| Rerun generation or gate evaluation for withdrawal or restoration | Availability-only changes preserve current content, gate evidence, and provenance. |

## Consequences

- PRODUCT-ADR-PIPELINE-021 becomes superseded history.
- Current source, normalized source, shared summaries, and phrase evidence remain reusable only when compatibility is proven.
- Source Adapter changes no longer default universally to normalization.
- Discovery and canonicalization changes rerun discovery and retained-source lookup.
- Acquisition changes reevaluate whether retained authentic source remains compatible.
- Normalization-only changes may reuse compatible retained authentic source.
- Generation-provider and evaluator-provider changes have separate rerun boundaries.
- Narrow rerun remains optional; conservative source-discovery or Common Pipeline rerun is the safe fallback when impact is uncertain.
- Publication-write retry and availability-only operations do not regenerate content when their inputs remain current.
- Stable valid-path and Learning Unit identity survive only when their authentic source identity inputs remain unchanged.
- T07 must use this ADR rather than PRODUCT-ADR-PIPELINE-021 for current retention, reuse, behavior evidence, and rerun specifications.
- Exact dependency graphs, cache invalidation, storage layout, version syntax, package structure, source layout, and acquisition implementation remain deferred.

## Evidence

- PRODUCT-ADR-PIPELINE-005 establishes staged processing and current-only retention.
- PRODUCT-ADR-PIPELINE-006 establishes Adapter-led discovery, canonical URL identity, complete-fetch-only retention, and replaceable current normalization.
- PRODUCT-ADR-PIPELINE-007 establishes source-path-derived Learning Unit identity and atomic current replacement.
- PRODUCT-ADR-PIPELINE-008 establishes release-level Adapter and Common Pipeline versions plus stage-specific provenance.
- PRODUCT-ADR-PIPELINE-016 permits accepted intermediate reuse while localizing failure.
- PRODUCT-ADR-PIPELINE-019 separates complete publication replacement from availability-only mutation.
- PRODUCT-ADR-PIPELINE-020 assigns listing discovery, canonicalization, deduplication, fetching, interpretation, and normalization to the Source Adapter while assigning retained-source lookup and fetch-versus-reuse selection to Orchestration.
- Independent review F-MAJ-01 identified that PRODUCT-ADR-PIPELINE-021 began pre-normalization Adapter changes too late.
- Independent review F-MIN-01 identified that evaluator-provider changes require an evaluation-stage boundary distinct from generation-provider changes.
