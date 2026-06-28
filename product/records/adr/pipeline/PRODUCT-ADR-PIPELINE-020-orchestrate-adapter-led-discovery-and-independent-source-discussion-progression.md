# PRODUCT-ADR-PIPELINE-020: Orchestrate adapter-led discovery and independent source-discussion progression

- **status**: accepted
- **date**: 2026-06-28
- **depends_on**:
  - PRODUCT-ADR-PIPELINE-005
  - PRODUCT-ADR-PIPELINE-006
  - PRODUCT-ADR-PIPELINE-009
  - PRODUCT-ADR-PIPELINE-016
  - PRODUCT-ADR-PIPELINE-017
  - PRODUCT-ADR-PIPELINE-018
  - PRODUCT-ADR-PIPELINE-019
- **supersedes**:
- **migrated_to_spec**:

## Context

The first-MVP Pipeline needs one orchestration contract from source discovery through publication without selecting a workflow engine, queue, scheduler, concurrency model, or persistence technology.

PRODUCT-ADR-PIPELINE-006 assigns source-specific discovery, fetching, interpretation, and normalization to Source Adapters.
PRODUCT-ADR-PIPELINE-016 through PRODUCT-ADR-PIPELINE-019 establish controlled stage outcomes, complete-unit blocking, a separate publication gate, and atomic current-state mutations.

The missing boundary is how orchestration invokes the Source Adapter, avoids duplicate acquisition, advances independent paths and discussions, aggregates completion, and reports operational results without leaking Pipeline internals to Application readers.

## Decision

### Orchestration boundary

Orchestration is the outer Pipeline control boundary.
It coordinates two distinct operation paths.

Initial publication or complete-content replacement follows:

1. Source Adapter discovery;
2. retained-source lookup and fetch-or-reuse selection;
3. Source Adapter fetching and normalization when required;
4. Common Pipeline processing according to the declared dependent stage graph;
5. publication-gate evaluation;
6. `PublicationHandoff` when accepted.

Withdrawal or same-content restoration follows:

1. one Pipeline-owned availability decision;
2. `AvailabilityChange` without rerunning the Common Pipeline or publication gate.

The Source Adapter is an orchestration-invoked source-specific component before the Common Pipeline.
It is not part of Common Pipeline semantics.
The Common Pipeline will not depend on source-specific listing, URL, API, HTML, or reply-field representation.

Code layout, process boundaries, workers, queues, and concurrency remain implementation choices.

### Adapter-led discovery and URL deduplication

The first-MVP Source Adapter will crawl configured eligible discussion listings.
The orchestration caller will not be required to submit one canonical discussion URL per discussion.

The Source Adapter will:

- discover eligible discussion references;
- canonicalize each discussion URL;
- deduplicate repeated canonical URLs within one crawl result;
- emit each canonical discussion discovery once;
- retain source-specific evidence needed to interpret the discovery.

Canonicalization and same-crawl deduplication remain source-specific because only the Adapter owns source URL meaning.

### Retained-source lookup and fetch selection

After one canonical discussion discovery, orchestration will look up retained authentic source by canonical discussion URL before requesting a fetch.

| condition | outcome |
|---|---|
| Complete retained source exists | Orchestration records `reused_retained_source` and does not request a new fetch. |
| No retained source exists | Orchestration requests source-specific fetching from the Source Adapter. |
| Requested fetch completes | Orchestration may establish retained authentic source and continue to normalization. |
| Requested fetch is partial, unavailable, or failed | No retained source is established and no dependent stage begins. |

The Source Adapter owns source-specific fetching and fetch-result interpretation.
Orchestration owns retained-source lookup, fetch-versus-reuse selection, retry control, and downstream continuation.
The Source Adapter does not need retained-source persistence access to decide whether a previous source is reusable.

### Source-discussion and path progression

One canonical discussion is one source-discussion orchestration scope.
Its result will preserve distinct outcomes for acquisition, normalization, candidate paths, valid Learning Paths, Learning Unit processing, publication attempts, and current-run diagnostics.

After shared acquisition, normalization, candidate derivation, and structural validation, each retained candidate follows its own dependent chain:

1. accepted reusable summaries and accepted phrase evidence;
2. semantic path filtering;
3. accepted path-specific summaries;
4. accepted target phrases;
5. accepted Quiz prompts;
6. accepted correct and distractor options;
7. deterministic content-validation completion;
8. publication-gate decision;
9. `PublicationHandoff` when accepted.

Each stage consumes only declared accepted upstream outputs.
Failure or rejection stops only the affected dependent suffix.
Independent sibling paths may continue.
A shared acquisition or normalization failure prevents all dependent paths because valid shared input does not exist.

### Batch continuation

A processing batch may contain multiple independent source discussions.
Failure, rejection, incompleteness, contradiction, or publication failure in one discussion will not stop independent discussions.

Batch-wide processing will stop only when a shared precondition makes all remaining work invalid to execute.
Examples include invalid shared Pipeline configuration, invalid unattended gate configuration, or an unavailable provider configuration required by every remaining item.

Continuation will never bypass required validation or publication-gate dimensions.

### Scope-specific completion

The Pipeline will not use one generic `completed` marker for every scope.
Each scope will retain its semantic terminal outcome.

A candidate path completes when it becomes retained, rejected, or incomplete.
A Learning Unit completes when it becomes published, rejected, incomplete, or publication-failed.
A publication attempt completes when it becomes committed, gate-rejected, precondition-failed, or mutation-failed.
A source discussion completes when every required child path and publication attempt reaches a terminal outcome.
A batch completes when every source discussion reaches a terminal outcome, or a batch-wide precondition failure terminalizes all remaining items as unexecutable.

Completion does not imply success.
A discussion or batch may complete with mixed outcomes.
A discussion may complete normally with zero valid paths or zero Learning Units.

### Aggregate operational result

Source-discussion and batch orchestration will expose one controlled aggregate result:

- `completed_with_output`;
- `completed_with_zero_output`;
- `completed_with_mixed_outcomes`;
- `failed_shared_precondition`.

The operational result may include controlled counts for valid paths, published units, rejected units, incomplete units, and publication failures.

Application-visible publication will expose only committed current published content and the already permitted opaque provenance reference.
Internal rejection, incompleteness, retries, component versions, and diagnostics remain outside the Application publication surface.

### Orchestration input and output boundary

Conceptual orchestration input is:

- current Source Adapter and crawl-scope configuration;
- current Common Pipeline and component configuration;
- available retained-source and current-artifact references;
- operation intent, such as new crawl processing or rerun from retained source.

The Source Adapter outputs canonical discussion discovery and, when a fetch is requested, complete fetch evidence or acquisition failure.
Orchestration records whether retained source was reused or newly established.

Orchestration output includes aggregate results, child-scope outcomes, committed publication references, current-run diagnostics, and reusable accepted current artifacts.

No orchestration input may authorize validation skipping, publication-gate override, partial-unit publication, or removal of failed posts from an accepted path.

## Rationale

Keeping orchestration outside Source Adapter and Common Pipeline semantics gives each boundary one reason to change.
The Adapter remains responsible for source-specific discovery and interpretation.
Orchestration remains responsible for retained-state decisions and progression.
The Common Pipeline remains source-independent.

Canonicalizing and deduplicating before retained-source lookup prevents duplicate work in one crawl.
Looking up retained source before fetching prevents unnecessary network acquisition without coupling the Adapter to persistence.

Independent path and discussion progression preserves useful output despite localized failure.
Scope-specific outcomes and aggregate results distinguish successful zero-output processing from infrastructure failure.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Require callers to submit every canonical discussion URL | The accepted first-MVP acquisition model is listing crawl through a Source Adapter. |
| Let the Source Adapter own retained-source storage lookup | Source-specific parsing would become coupled to Pipeline persistence and reuse policy. |
| Fetch before retained-source lookup | Already retained discussions would be requested unnecessarily. |
| Put source-specific crawl logic in the Common Pipeline | Common processing would depend on one source platform. |
| Stop a discussion after one path failure | Independent sibling paths could still produce valid complete units. |
| Stop a batch after one discussion failure | Independent discussions should continue. |
| Use one generic success or failure result | Zero output, mixed outcomes, and shared-precondition failure have different operational meanings. |
| Allow orchestration overrides for validation or publication | Overrides would weaken non-compensating readiness and complete-unit contracts. |

## Consequences

- Source Adapter discovery and same-crawl URL deduplication precede retained-source lookup.
- Orchestration decides fetch versus retained-source reuse.
- Source Adapter fetching occurs only when orchestration requests it.
- Common Pipeline processing begins only from accepted normalized source input.
- Path-local failure does not stop sibling paths.
- Discussion-local failure does not stop independent discussions.
- Completion and aggregate outcome remain distinct from all-success meaning.
- Application readers remain isolated from Pipeline operational data.
- T07 must reflect these boundaries into `spec:product.pipeline.orchestration`, source acquisition, source normalization, and publication specifications.
- Exact APIs, schemas, processes, queues, schedulers, workers, storage, and concurrency remain deferred.

## Evidence

- PRODUCT-ADR-PIPELINE-006 establishes Adapter-led listing crawl, canonical URL identity, retained-source reuse, and source-independent normalization.
- PRODUCT-ADR-PIPELINE-016 establishes controlled stage outcomes and complete-unit blocking.
- PRODUCT-ADR-PIPELINE-017 establishes separate fail-closed publication gating.
- PRODUCT-ADR-PIPELINE-019 establishes atomic mutation and no-mutation failure behavior.
- The user selected Orchestration as the outer control boundary, Adapter-owned canonicalization and same-crawl deduplication, Orchestration-owned retained lookup and fetch selection, independent path and discussion continuation, and scope-specific aggregate completion.
