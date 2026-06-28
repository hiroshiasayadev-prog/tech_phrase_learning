# Concept: Source acquisition

- **id**: `spec:product.pipeline.source_acquisition`
- **status**: draft
- **date**: 2026-06-28
- **parent**: `spec:product.pipeline`

## What this is

Pipeline contract for source discovery, canonical discussion identification, retained-source reuse, and complete-fetch acquisition outcomes.
The contract ends before source-independent normalization.

## Non-goals

- Network clients, pagination, timeouts, retry counts, concrete crawl cadence, triggers, schedulers, or execution technology.
- Retained-source storage schemas.
- Source-independent post and relationship semantics.
- Source freshness or synchronization with later source edits.
- Application runtime reads.

## Concept model

| concept | contract |
|---|---|
| Repeated eligible listing crawl | Source-specific discovery repeatedly executed over configured discussion listings. |
| Canonical discussion URL | Source-specific canonical identity used for retained-source lookup. |
| Discovery evidence | Source-specific evidence required to interpret one discovered discussion. |
| Retained authentic source | One complete retained source record for a canonical discussion URL. |
| Complete fetch | A fetch result containing the complete source evidence required for normalization. |
| Acquisition outcome | The orchestration-visible result of lookup, reuse, fetch, or acquisition failure. |

## Rules

### Adapter-led discovery

- The first-MVP operation must repeatedly execute Source Adapter discovery over configured eligible discussion listings.
- Repeated discovery must allow newly listed eligible discussions to enter later crawl results.
- Concrete crawl cadence, trigger, scheduler, and execution technology remain implementation choices.
- The first-MVP source scope is eligible Packaging discussions from `discuss.python.org`.
- The Source Adapter must discover source-specific discussion references.
- The Source Adapter must canonicalize every discovered discussion URL.
- The Source Adapter must deduplicate repeated canonical URLs within one crawl result.
- The Source Adapter must emit each canonical discussion discovery once per crawl result.
- Each discovery must retain source-specific evidence required to interpret the discovery.
- Canonicalization and same-crawl deduplication remain Source Adapter responsibilities.

### Retained-source lookup and fetch selection

Orchestration must look up retained authentic source by canonical discussion URL before requesting a fetch.

| condition | acquisition outcome |
|---|---|
| Complete retained authentic source exists | Record `reused_retained_source`, skip fetching, and continue with accepted retained source. |
| No retained authentic source exists | Request source-specific fetching from the Source Adapter. |
| Requested fetch completes | Establish retained authentic source and allow normalization. |
| Requested fetch is partial, unavailable, or failed | Establish no retained source and start no dependent stage. |

- Orchestration owns retained-source lookup and fetch-versus-reuse selection.
- The Source Adapter owns source-specific fetching and fetch-result interpretation.
- The Source Adapter must not require retained-source persistence knowledge.
- Reused retained source and newly established retained source are both accepted normalization inputs.

### Retention and failure meaning

- The canonical discussion URL identifies one retained authentic discussion.
- A partial fetch must not establish retained authentic source.
- An unavailable fetch must not establish retained authentic source.
- A failed fetch must not establish retained authentic source.
- Acquisition failure must prevent normalization and every dependent stage for that discussion.
- A later retry or rerun may establish retained source under `spec:product.pipeline.orchestration`.
- The first MVP does not provide an explicit source-refresh operation.
- The first MVP does not require periodic refetch of retained discussions.
- The first MVP does not detect or synchronize later source changes.
- Source freshness is not part of the learning-content contract.

## Boundary

| concern | owner |
|---|---|
| Source-specific listing, URL, and fetch interpretation | `spec:product.pipeline.source_acquisition` through a Source Adapter. |
| Retained-source lookup and progression | `spec:product.pipeline.orchestration` using this acquisition contract. |
| Source-independent authentic conversation | `spec:product.pipeline.source_normalization`. |
| Retry, exhaustion, rerun, and batch continuation | `spec:product.pipeline.orchestration`. |
| Current source identity and behavior evidence | `spec:product.pipeline.artifact_identity_and_provenance`. |
| Network and persistence implementation | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.pipeline` | Parent Pipeline overview. |
| `spec:product.pipeline.source_normalization` | Consumes accepted complete retained source. |
| `spec:product.pipeline.artifact_identity_and_provenance` | Defines current source identity and acquisition behavior evidence. |
| `spec:product.pipeline.orchestration` | Coordinates lookup, fetch selection, retry, and continuation. |
| PRODUCT-ADR-PIPELINE-005 | Establishes retained-source reuse and no freshness guarantee. |
| PRODUCT-ADR-PIPELINE-006 | Establishes periodic listing discovery, canonical-URL identity, and complete-fetch-only retention. |
| PRODUCT-ADR-PIPELINE-020 | Establishes Adapter-led discovery, deduplication, and orchestration-owned fetch selection. |
| PRODUCT-ADR-PIPELINE-022 | Establishes acquisition retry and exhaustion semantics. |
| PRODUCT-ADR-PIPELINE-024 | Establishes source-stage-aware compatibility and rerun boundaries. |
