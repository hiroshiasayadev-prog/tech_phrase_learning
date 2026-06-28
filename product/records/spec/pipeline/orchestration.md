# Concept: Pipeline orchestration

- **id**: `spec:product.pipeline.orchestration`
- **status**: draft
- **date**: 2026-06-28
- **parent**: `spec:product.pipeline`

## What this is

Outer Pipeline control boundary for operation paths, accepted-stage progression, retry, rerun, reuse, continuation, completion, and current-run diagnostics.
The contract remains independent from any workflow engine, queue, scheduler, worker, or concurrency implementation.

## Non-goals

- Workflow engine, queue, scheduler, worker topology, or concurrency model.
- Concrete retry count, timeout, delay, backoff, jitter, repair prompt, or provider fallback.
- Logging stack, diagnostic UI, deployment, or persistence layout.
- Stage-specific semantic meaning owned by focused Pipeline specs.
- Application runtime selection or retrieval behavior.

## Concept model

| concept | contract |
|---|---|
| Orchestration | Outer Pipeline control boundary coordinating Source Adapter, Common Pipeline, gate, and writes. |
| Source-discussion scope | One canonical discussion and all dependent path and publication outcomes. |
| Path-local suffix | Downstream stages that depend on one path-local result. |
| Retry | Repetition of one failed operation under unchanged current input and behavior. |
| Rerun | Re-execution from the earliest stage affected by changed input or behavior. |
| Terminal outcome | Scope-specific result that ends processing for that scope without implying success. |
| Aggregate operational result | Controlled source-discussion or batch completion summary. |

## Rules

### Operation paths

Orchestration coordinates two distinct paths.

Initial publication or complete replacement follows:

1. Source Adapter discovery;
2. retained-source lookup and fetch-or-reuse selection;
3. Source Adapter fetching and normalization when required;
4. Common Pipeline execution through declared stage dependencies;
5. publication-gate evaluation;
6. `PublicationHandoff` when accepted.

Withdrawal or same-content restoration follows:

1. Pipeline-owned availability decision;
2. `AvailabilityChange` without Common Pipeline or gate rerun.

- The Source Adapter runs before the Common Pipeline.
- Source-specific listing, URL, API, HTML, and reply fields must not enter Common Pipeline semantics.
- Orchestration may invoke source-specific components without defining their internal implementation.

### Declared dependency graph

- Every stage must declare its required accepted upstream artifacts.
- A stage may begin only when every declared prerequisite is accepted and current.
- Non-accepted output must not enter a dependent stage.
- Failure or rejection must stop only the affected dependent suffix unless shared required input is absent.
- Shared acquisition or normalization failure must stop all dependent paths for that discussion.
- Path-local failure must not stop independent sibling paths.
- Discussion-local failure must not stop independent source discussions.

The first-MVP common progression is:

1. bounded candidate enumeration;
2. deterministic structural validation;
3. accepted reusable summaries and phrase evidence;
4. semantic path filtering;
5. path-specific summary revision;
6. target-phrase selection;
7. Quiz-prompt generation;
8. correct-option and distractor generation;
9. content-validation completion;
10. publication gate;
11. `PublicationHandoff` when accepted.

- Shared reusable source-post artifacts may be produced before path filtering.
- Processing becomes path-specific at path-specific summary revision.
- The declared graph must preserve stage requirements from the owning focused specs.

### Independent continuation

- Candidate rejection must stop only that candidate's dependent chain.
- One path's incomplete interaction must stop only that path-local suffix.
- One publication failure must not stop sibling paths or independent discussions.
- A batch may continue after rejection, incompleteness, contradiction, or mutation failure in one discussion.
- Batch-wide processing may stop only when one shared precondition makes all remaining work invalid.
- Shared-precondition examples include invalid shared Pipeline configuration, invalid unattended gate configuration, or unavailable provider configuration required by all remaining work.
- Continuation must never bypass required validation or publication-gate dimensions.

### Retry classification

Retry is allowed only when the requested operation did not complete reliably.

Retryable conditions are:

- transient source-acquisition failure;
- provider execution failure;
- invalid provider output;
- transient `PublicationHandoff` write failure;
- transient `AvailabilityChange` write failure.

The following outcomes are non-retryable under unchanged input and behavior:

- structural rejection;
- valid semantic rejection;
- deterministic invalid state;
- contradictory validation state;
- publication precondition failure;
- availability-change precondition failure.

- Invalid-output retry must not become repeated sampling of valid rejected content.
- Contradiction requires defect correction or rerun from the earliest invalidated stage.

### Retry scope and finite termination

- Retry must rerun only the failed operation by default.
- Orchestration must confirm that required inputs and behavior references remain current before retry.
- Changed input or behavior converts retry into rerun.
- Retry blocks only the dependent suffix for the affected path or mutation.
- Independent sibling paths and discussions may continue during retry.
- Every retryable operation must terminate under a finite implementation-configured bound.
- Design defines retryable categories, scope, input recheck, exhaustion meaning, and continuation.
- Implementation defines attempt counts, timeouts, delay, backoff, jitter, repair prompts, and provider switching.
- The Pipeline must not impose one universal retry count across operations.

### Retry exhaustion

| exhausted operation | terminal meaning |
|---|---|
| Initial acquisition | Acquisition failure; no dependent processing begins. |
| Provider execution or invalid output | Affected stage exhausted; affected Learning Unit remains incomplete. |
| `PublicationHandoff` write | Mutation failure; initial publication creates no state and replacement preserves prior state. |
| `AvailabilityChange` write | Mutation failure; prior availability remains unchanged. |

- Exhaustion terminalizes only the affected scope.
- Exhaustion must not continue without a new explicit rerun or operational action.
- Path-local exhaustion must not stop independent sibling paths.

### Distinct unpublished outcomes

| outcome | meaning |
|---|---|
| `rejected` | Processing completed but source, content, validation, or publication criteria did not pass. |
| `incomplete` | Required generation, evaluation, or mutation processing did not complete. |
| `contradictory` | Current evidence contains internally incompatible claims and indicates invalid aggregation or a Pipeline defect. |

- These outcomes must not create or replace Application-visible current state.
- Replacement failure with any unpublished outcome must preserve previous committed state.
- Internal controlled cause evidence may support diagnosis, rerun selection, and aggregate reporting.

### Scope-specific terminal outcomes

A terminal outcome ends processing for its scope but does not imply acceptance or downstream eligibility.

| scope | terminal outcomes |
|---|---|
| Source acquisition | Acquired, reused, or acquisition failed. |
| Normalization | Accepted normalized source, normalization failed, or accepted zero-path result. |
| Candidate path | Retained valid path, structural rejection, semantic rejection, or semantic evaluation failure. |
| Learning Unit | Complete, rejected, incomplete, or contradictory. |
| Publication gate | Accepted, rejected, or contradictory. |
| Publication mutation | Committed, precondition failed, or mutation failed. |
| Availability change | Committed withdrawal, committed restoration, precondition failed, or mutation failed. |

- A source discussion completes when every required child path and publication attempt is terminal.
- A batch completes when every discussion is terminal or a shared-precondition failure terminalizes remaining work as unexecutable.
- A discussion may complete successfully with zero valid paths or zero Learning Units.
- Completion may contain mixed outcomes.

### Aggregate operational results

Source-discussion and batch orchestration must expose one aggregate result.

| result | meaning |
|---|---|
| `completed_with_output` | Processing completed and produced committed output without mixed terminal failures. |
| `completed_with_zero_output` | Processing completed normally with no committed output. |
| `completed_with_mixed_outcomes` | Processing completed with a mixture of output, rejection, incompleteness, contradiction, or mutation failure. |
| `failed_shared_precondition` | A shared precondition made remaining work unexecutable. |

- Aggregate results may include controlled counts for valid paths, published units, rejected units, incomplete units, contradictions, and publication failures.
- Internal outcomes, retries, versions, and diagnostics must remain outside the Application publication surface.

### Current artifact reuse

- Retained artifacts may be reused only when their inputs, source identity, acquisition evidence, and relevant behavior references remain current and compatible.
- Shared artifacts may be reused across compatible sibling paths.
- Path-specific artifacts may be reused only for the same valid-path identity and unaffected suffix.
- One path-local failure must not invalidate accepted shared artifacts.
- A narrow suffix rerun is an optimization, not a requirement.

### Conservative rerun rule

A rerun must begin at the earliest stage whose accepted input, source identity, acquisition evidence, behavior, provider, prompt, validator, or configuration may have changed.

- Only proven unaffected accepted upstream artifacts may be reused.
- When a narrower Common Pipeline boundary cannot be proven, rerun from the first Common Pipeline stage.
- When a Source Adapter impact cannot be isolated, rerun from Source Adapter discovery.
- Conservative source rerun must canonicalize URLs again and repeat retained-source lookup.

### Source Adapter rerun boundaries

| changed behavior | default rerun start |
|---|---|
| Listing discovery, eligibility, URL extraction, canonicalization, or same-crawl deduplication | Source Adapter discovery, canonicalization, deduplication, and retained-source lookup. |
| Fetch execution, request construction, complete-fetch determination, result interpretation, or acquisition evidence | Acquisition compatibility check; reacquire unless retained-source compatibility is proven. |
| Normalization, quote separation, relationship interpretation, post identity, or Discussion Path derivation | Reuse compatible complete retained source and rerun normalization plus all dependents. |
| Unisolated Source Adapter change | Source Adapter discovery with repeated lookup and acquisition decisions. |

- A Source Adapter version change alone does not authorize reuse from normalization.
- Reuse depends on proven compatibility of source identity, acquisition evidence, and retained source.

### Other rerun boundaries

| material change | default rerun start |
|---|---|
| Retained authentic source replacement | Normalization and every dependent stage. |
| Common Pipeline orchestration or composition | First Common Pipeline stage. |
| Generation provider or prompt | Earliest affected generation stage. |
| Evaluator provider, prompt, or behavior | Earliest affected evaluation stage. |
| Deterministic validator | Earliest affected deterministic validation stage. |
| Publication-gate configuration | Gate evaluation unless upstream evidence is also invalidated. |
| Failed publication write with unchanged accepted handoff | Failed write operation only. |
| Withdrawal or same-content restoration | Applicable `AvailabilityChange` only. |

- Narrower rerun is valid only when compatibility is proven.
- Stable path and Learning Unit identity may be preserved only after source identity and ordered post identities remain unchanged.
- Generated-content or component-behavior changes alone must not create sibling Learning Units.

### Current-run diagnostics

Current-run diagnostics must explain retry, rejection, exhaustion, incompleteness, contradiction, skipped stages, continuation, and mutation failure.

Minimum evidence includes:

- applicable discussion, path, Learning Unit, publication attempt, and stage scope;
- retry or terminal outcome;
- controlled cause category;
- configured retry limit, attempts used, and exhaustion state;
- orchestration and relevant component behavior references;
- skipped dependent stages and skip cause;
- sibling-path and discussion continuation result;
- preservation of previous committed state after failed mutation.

- Diagnostics must explain the current run without complete attempt history.
- Raw prompts, complete provider responses, and permanent historical replay are not required.

## Boundary

| concern | owner |
|---|---|
| Source-specific discovery and fetch interpretation | `spec:product.pipeline.source_acquisition`. |
| Stage-specific inputs, outputs, and acceptance meaning | Owning focused Pipeline specifications. |
| Retry, rerun, reuse, continuation, completion, and diagnostics | `spec:product.pipeline.orchestration`. |
| Identity and behavior evidence | `spec:product.pipeline.artifact_identity_and_provenance`. |
| Publication operation semantics | `spec:product.pipeline.publication`. |
| Runtime reads | `spec:product.application`. |
| Workflow and deployment technology | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.pipeline` | Parent Pipeline overview. |
| `spec:product.pipeline.source_acquisition` | Defines discovery, lookup, fetch, and reuse outcomes. |
| `spec:product.pipeline.source_normalization` | Defines accepted normalized source and zero-path outcomes. |
| `spec:product.pipeline.path_validation` | Defines path-local rejection and evaluation failure. |
| `spec:product.pipeline.validation` | Defines common stage and completion outcomes. |
| `spec:product.pipeline.artifact_identity_and_provenance` | Defines reusable artifacts and behavior evidence. |
| `spec:product.pipeline.publication` | Defines gate, handoff, and availability-change semantics. |
| PRODUCT-ADR-PIPELINE-020 | Establishes the outer orchestration boundary and independent progression. |
| PRODUCT-ADR-PIPELINE-022 | Establishes finite operation-local retry, exhaustion, terminal outcomes, and diagnostics. |
| PRODUCT-ADR-PIPELINE-024 | Establishes current reuse and source-stage-aware rerun boundaries. |
