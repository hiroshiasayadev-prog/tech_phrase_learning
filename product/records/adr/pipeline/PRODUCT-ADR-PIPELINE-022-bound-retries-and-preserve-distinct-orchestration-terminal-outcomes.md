# PRODUCT-ADR-PIPELINE-022: Bound retries and preserve distinct orchestration terminal outcomes

- **status**: accepted
- **date**: 2026-06-28
- **depends_on**:
  - PRODUCT-ADR-PIPELINE-002
  - PRODUCT-ADR-PIPELINE-016
  - PRODUCT-ADR-PIPELINE-017
  - PRODUCT-ADR-PIPELINE-019
  - PRODUCT-ADR-PIPELINE-020
  - PRODUCT-ADR-PIPELINE-024
- **supersedes**:
- **migrated_to_spec**: 2026-06-28

## Context

Pipeline stages can fail because source acquisition did not complete, a provider could not execute, provider output was invalid, content was validly rejected, validation evidence was contradictory, or publication mutation failed.

Those conditions require different orchestration behavior.
Retrying valid rejection would weaken accepted semantic criteria.
Never retrying transient operational failure would make the Pipeline unnecessarily brittle.
Unbounded retry would prevent processing scopes and batches from reaching completion.

The Pipeline therefore needs retry classification, retry scope, finite exhaustion, unpublished terminal outcomes, whole-unit blocking, and current-run diagnostics without selecting concrete counts, timeouts, delays, backoff, or fallback algorithms.

## Decision

### Retryable outcomes

Retry is allowed only when the requested operation did not complete reliably.

Retryable conditions are:

- transient source-acquisition failure;
- provider execution failure;
- invalid provider output;
- transient `PublicationHandoff` write failure;
- transient `AvailabilityChange` write failure.

Invalid output retry addresses an untrusted or unusable operation result.
It is not permission to regenerate accepted but rejected content until a passing result appears.

### Non-retryable outcomes

The following outcomes will not be retried under unchanged inputs and behavior:

- structural rejection;
- valid semantic rejection;
- deterministic validation failure caused by actual invalid state;
- contradictory validation state;
- publication precondition failure;
- availability-change precondition failure.

A valid rejection remains a terminal content outcome until a later material change triggers a new rerun.
A contradiction requires defect correction or rerun from the earliest invalidated stage rather than repetition of the same operation as though it were transient.

### Retry scope

Retry will rerun only the failed operation by default.
Accepted upstream artifacts remain reusable while their inputs and relevant behavior references remain current.

Before retry, orchestration will confirm that required inputs and behavior references are still current.
Changed input or behavior converts the action into a rerun under PRODUCT-ADR-PIPELINE-024.

A retry blocks only the dependent suffix for the affected path or mutation.
Independent sibling paths and discussions may continue.

Examples include:

- retrying one failed Quiz-prompt generation operation without rerunning accepted summaries or target phrases;
- retrying an unchanged accepted `PublicationHandoff` after transient write failure without rerunning generation or gate evaluation.

### Finite retry and implementation-owned parameters

Every retryable operation will terminate under a finite retry bound.

Design authority defines:

- which outcomes are retryable;
- which scope is retried;
- current-input recheck before retry;
- exhaustion meaning;
- continuation behavior after exhaustion.

Implementation configuration defines:

- maximum attempt count;
- timeout;
- delay;
- backoff;
- jitter;
- repair-prompt details;
- provider fallback or provider switching.

The Pipeline will not impose one universal retry count across acquisition, provider execution, semantic evaluation, publication, and availability operations.

### Exhaustion outcomes

Retry exhaustion produces a terminal orchestration outcome for the affected scope.

| exhausted operation | terminal meaning |
|---|---|
| Initial source acquisition | The source discussion has acquisition failure and no dependent path processing begins. |
| Provider execution or invalid provider output | The affected stage is exhausted and the affected Learning Unit remains incomplete. |
| `PublicationHandoff` write | Publication mutation failure; initial publication creates no current state and replacement preserves the previous committed state. |
| `AvailabilityChange` write | Availability mutation failure; the previous committed availability remains unchanged. |

An exhausted path-local operation does not stop independent sibling paths.
No exhausted operation continues retrying without a new explicit rerun or operational action.

### Distinct unpublished terminal outcomes

The Pipeline will distinguish:

| outcome | meaning |
|---|---|
| `rejected` | Processing completed, but source structure, source suitability, generated content, validation, or publication criteria did not pass. |
| `incomplete` | Required generation, evaluation, or mutation processing did not complete. |
| `contradictory` | Current Pipeline evidence contains internally incompatible claims and indicates invalid aggregation or a Pipeline defect. |

These outcomes will not create or replace Application-visible current published state.
The Pipeline will retain the current internal outcome and controlled cause evidence for diagnosis, rerun selection, and aggregate reporting.

A rejected, incomplete, or contradictory replacement preserves the previous committed published state.
The exact persistence technology and schema remain implementation choices.

### Complete-unit blocking

One failed or incomplete interaction within a valid Learning Path makes the complete Learning Unit for that path incomplete.

The Pipeline will not:

- publish only successful posts;
- skip the failed post;
- shorten the valid Learning Path;
- mutate the accepted path to salvage a partial unit.

Accepted earlier post-level intermediates may remain reusable for a later rerun when their inputs and behavior references remain current.
The incomplete path will not stop independent sibling paths.

### Scope-specific terminal meaning

A terminal outcome means that the scope finished processing.
It does not mean success or permission to enter the next stage.
Only the declared accepted outcome for one scope may enable its dependent stage.

Examples include:

| scope | terminal outcomes |
|---|---|
| Source acquisition | acquired, reused, acquisition failed. |
| Normalization | accepted normalized source, normalization failed, accepted zero-path result. |
| Path processing | retained valid path, structural rejection, semantic rejection, evaluation failure. |
| Learning Unit processing | complete unit, incomplete unit, rejected unit. |
| Publication gate | accepted, rejected, contradictory. |
| Published-content mutation | committed, precondition failed, mutation failed. |
| Availability change | committed withdrawal, committed restoration, precondition failed, mutation failed. |

### Minimum current-run diagnostics

Current-run diagnostics will retain enough evidence to explain retry, rejection, exhaustion, incompleteness, contradiction, skipped dependent stages, continuation, and mutation failure.

Minimum evidence is:

- source discussion, path, Learning Unit, publication attempt, and stage scope when applicable;
- retry or terminal outcome;
- controlled cause category;
- configured retry limit, attempts used, and exhaustion state;
- orchestration and relevant component behavior references;
- skipped dependent stages and skip cause;
- whether sibling paths or discussions continued;
- whether failed publication or availability mutation preserved previous committed state.

Raw prompts, complete provider responses, every transient attempt, and permanent historical replay are not required.
Diagnostics must explain the current run without requiring complete attempt history.

## Rationale

Separating transient operational failure from valid content rejection prevents retries from weakening accepted criteria.
Operation-local retry preserves accepted upstream work and allows independent processing to continue.

Finite bounds guarantee that every scope can reach a terminal state.
Delegating counts and timing to implementation allows tuning from observed reliability without changing product-level semantics.

Distinct terminal outcomes make diagnosis and rerun selection possible.
Whole-unit blocking protects the accepted Learning Path and prevents partial publication.
Current-run diagnostics provide operational accountability without requiring permanent model-transcript retention.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Retry every failure | Valid semantic rejection and deterministic invalid state are not transient execution failures. |
| Retry valid content until it passes | Repeated sampling would turn criteria into probabilistic approval by persistence. |
| Never retry invalid provider output | Malformed or unusable output may be transient and does not establish semantic rejection. |
| Define one fixed attempt count in design | Counts are implementation tuning parameters and may differ by operation. |
| Retry an entire discussion after one path-local failure | Accepted upstream and sibling-path work would be repeated unnecessarily. |
| Publish successful posts from an incomplete path | The resulting unit would not represent the accepted Learning Path. |
| Collapse all terminal outcomes into `failed` | Rejection, incomplete processing, contradiction, and mutation failure have different meanings. |
| Require complete historical replay | Current diagnosis and safe rerun selection do not require permanent retention of every attempt. |

## Consequences

- Retryable and non-retryable outcomes are explicit.
- Each retryable operation has a finite implementation-configured bound.
- Retry defaults to the failed operation and rechecks current inputs first.
- Exhaustion terminalizes the affected scope without stopping independent work.
- Valid rejection is never converted into provider failure or incomplete processing.
- Contradictory evidence cannot continue to publication.
- Failed writes preserve the previous committed state.
- One failed interaction blocks the complete Learning Unit for its path.
- T07 must reflect retry classification, exhaustion, terminal outcomes, complete-unit blocking, and diagnostics into focused Pipeline specifications.
- Exact counts, timing, fallback, persistence, encoding, and diagnostic presentation remain deferred.

## Evidence

- PRODUCT-ADR-PIPELINE-002 treats model output as untrusted behind a provider boundary.
- PRODUCT-ADR-PIPELINE-016 distinguishes accepted, provider, invalid-output, semantic, incomplete, and contradictory stage outcomes.
- PRODUCT-ADR-PIPELINE-017 requires fail-closed publication on incomplete or contradictory evidence.
- PRODUCT-ADR-PIPELINE-019 requires failed preconditions and writes to leave committed state unchanged.
- PRODUCT-ADR-PIPELINE-020 permits independent sibling-path and discussion continuation.
- PRODUCT-ADR-PIPELINE-024 permits accepted current artifact reuse and earliest-affected-stage rerun.
- The user selected operation-local retry, finite implementation-owned retry limits, distinct rejection, incompleteness and contradiction, whole-unit blocking, and current-run diagnostics.
