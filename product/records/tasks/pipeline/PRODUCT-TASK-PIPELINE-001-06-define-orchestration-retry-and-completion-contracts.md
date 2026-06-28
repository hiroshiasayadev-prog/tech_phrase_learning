# PRODUCT-TASK-PIPELINE-001-06: Define orchestration, retry, and completion contracts

- **id**: PRODUCT-TASK-PIPELINE-001-06
- **status**: done
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PIPELINE-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 2.5d
- **depends_on**:
  - PRODUCT-TASK-PIPELINE-001-05
- **outputs**:
  - PRODUCT-ADR-PIPELINE-020
  - PRODUCT-ADR-PIPELINE-024
  - PRODUCT-ADR-PIPELINE-022
  - PRODUCT-ADR-PIPELINE-023

## Goal

Define stage orchestration, dependency order, retry, rejection, rerun, reuse, partial failure, batch continuation, and completion semantics.

## Work

1. Read T02 through T05 accepted decisions and stage contracts.
2. Define orchestration inputs and outputs for one source discussion and one processing batch.
3. Define stage dependency order from acquisition through publication.
4. Distinguish deterministic stages from model stages and publication-decision stages.
5. Define reusable retained-source and reusable summary boundaries.
6. Define rerun boundaries after source replacement, prompt change, provider change, validator change, gate change, and failed publication.
7. Define which current intermediate artifacts must be retained and which may be transient or overwritten.
8. Define retryable and non-retryable outcomes for acquisition, provider output, validation, and publication stages.
9. Define bounded retry without selecting retry count, delay, timeout, or backoff algorithms.
10. Define invalid provider output, exhausted retry, incomplete unit, contradictory result, and rejected unit outcomes.
11. Define partial failure behavior and the boundary between one unit failure and batch continuation.
12. Define whether later independent units may continue after a source, path, generation, validation, or publication failure.
13. Define completion semantics for source processing, path processing, unit generation, gate evaluation, and publication.
14. Require no partial published-content mutation after any failed precondition or write.
15. Define current-run diagnostics without requiring historical intermediate retention.
16. Create or update Pipeline ADRs when current authority does not determine observable orchestration semantics.
17. Keep workflow engines, queues, concurrency models, scheduling, logging stacks, and deployment outside the contract.
18. Update `outputs` and Evidence with accepted ADRs or specification inputs.

## Done condition

- Orchestration inputs, outputs, and stage dependency order are explicit.
- Deterministic, model, validation, gate, and publication stages remain distinct.
- Rerun and reuse boundaries are explicit for every material change or failure class.
- Required current intermediates and transient artifacts are explicit.
- Retryable and non-retryable outcomes are explicit without concrete retry timing.
- Bounded retry, exhaustion, rejection, and incomplete-unit handling are explicit.
- Contradictory validation results cannot continue to publication.
- One unit failure and batch continuation have an explicit boundary.
- Completion semantics are explicit for each processing scope.
- Current-run diagnostics remain available without historical replay requirements.
- Every new normative decision has accepted Pipeline ADR authority.
- Concrete orchestration technology remains deferred.

## Verification

- Confirm each stage consumes only declared upstream outputs.
- Confirm rerun does not silently change stable valid-path or learning-unit identity.
- Confirm source reuse and current-only retention remain consistent with PRODUCT-ADR-PIPELINE-005.
- Confirm bounded retry cannot become unbounded processing.
- Confirm one failed unit cannot produce incomplete published state.
- Confirm batch continuation never bypasses required gate dimensions.
- Confirm no workflow engine, queue technology, or concurrency implementation enters the contract.
- Run relevant record validation, strict specification validation, `git diff --check`, and `git status --short`.

## Evidence

### Execution boundary

- T06 is `in_progress`.
- PRODUCT-TASK-PIPELINE-001-05 is `done`.
- The parent Work Item lists T06, and both records reference PRODUCT-REQ-PRODUCT-001.
- T06 recorded user-approved orchestration direction before ADR materialization.
- Task Evidence is not normative authority.
- No normative specification changes belong to T06.

### Non-normative decision register

#### D01 Source-discussion processing scope

One source discussion is one orchestration scope identified by its canonical discussion URL.

The source-discussion result will preserve distinct outcomes for acquisition, normalization, candidate paths, valid Learning Paths, Learning Unit processing, publication attempts, source-level completion, and current-run diagnostics.

Paths and Learning Units within one discussion may have different outcomes.
A rejected or failed path will not automatically make the whole source discussion a generic failure.

A source discussion may complete normally with zero valid Learning Paths or zero Learning Units.

Job shape, queue structure, worker boundaries, concurrency, and result persistence remain implementation choices.

#### D02 Per-path stage dependency order

After source acquisition, normalization, candidate derivation, and structural validation establish shared discussion inputs, each retained candidate follows its own dependent stage chain.

The per-path chain is:

1. accepted reusable summaries and accepted phrase evidence;
2. semantic path filtering;
3. accepted path-specific summaries;
4. accepted target phrases;
5. accepted Quiz prompts;
6. accepted correct and distractor options;
7. deterministic content-validation completion;
8. publication-gate decision;
9. `PublicationHandoff` when the gate accepts the candidate.

Each stage consumes only declared accepted upstream outputs.
A failed or rejected path stops only that path's dependent suffix.
It does not stop independent sibling paths from the same source discussion.

Shared source or normalized-input failure may prevent every dependent path because those paths lack valid upstream input.

Deterministic processing, model generation, semantic validation, publication-gate decision, and published-content mutation remain separate stage classes.
Job decomposition, parallel execution, scheduling, and worker topology remain implementation choices.

#### D03 Shared and path-specific reuse boundaries

The Pipeline will reuse current artifacts that are independent from one selected Learning Path.

Shared reusable artifacts are:

- retained authentic source;
- current normalized authentic conversation;
- accepted reusable summaries;
- accepted source-grounded phrase evidence.

Path-specific artifacts are:

- path-specific summaries;
- target phrases;
- Quiz prompts;
- correct and distractor options;
- complete Learning Unit candidates;
- path-local validation results;
- publication-gate and publication outcomes.

When two valid paths contain the same authentic post, they may consume the same accepted reusable summary and phrase evidence.
Processing becomes path-specific at path-specific summary revision and remains path-specific afterward.

Failure in one path-specific artifact does not invalidate accepted shared artifacts or sibling-path results.

#### D04 Current retention and execution-behavior version evidence

The Pipeline will retain only current reusable or publication-relevant artifacts.

Current retained data includes:

- retained authentic source;
- current normalized authentic conversation;
- current valid paths and current rejection evidence;
- accepted reusable summaries;
- accepted source-grounded phrase evidence;
- accepted path-local intermediates required to resume current processing;
- current validation, gate, and provenance evidence for committed published content.

Raw model requests and responses, invalid retry attempts, and superseded current intermediates may be transient or overwritten.
Historical generations and complete attempt history are not required.

Current provenance will identify orchestration behavior separately from component behavior.
It will also retain version evidence for source adapters, providers, prompts, evaluators, deterministic validators, and gate configuration.

A component change may therefore invalidate only that component and its dependent stage suffix.
The exact version representation, module layout, Python file names, package structure, Git mapping, and manifest format remain implementation choices.

#### D05 Conservative rerun boundary

A rerun will begin at the earliest stage whose accepted input, behavior, prompt, provider, validator, or configuration may have changed.
Only accepted upstream artifacts proven current and unaffected may be reused.

Narrow component-suffix rerun is an allowed optimization.
When the Pipeline cannot prove a narrower unaffected boundary, it will rerun the complete Common Pipeline from its first common-processing stage.

A Common Pipeline rerun may reuse retained authentic source and current normalized source when Source Adapter behavior and normalized input remain unchanged.

A Source Adapter change begins at its earliest affected source-side stage:

- discovery, URL canonicalization, or same-crawl deduplication change reruns Source Adapter discovery and retained-source lookup;
- fetch execution, completeness, or acquisition-interpretation change reevaluates retained-source compatibility and reacquires source when compatibility cannot be proven;
- normalization, quote, relationship, post-identity, or Discussion Path behavior change reruns normalization from compatible retained authentic source.

When Source Adapter impact cannot be isolated, rerun begins from Source Adapter discovery.
A retained-source replacement requires re-normalization and every dependent downstream stage.

Rerun will preserve valid-path and Learning Unit identity when the authentic discussion and ordered authentic-post path remain unchanged.
Implementation-specific dependency graphs and cache invalidation mechanisms remain deferred.

#### D06 Retryable and non-retryable outcomes

Retry is allowed only for outcomes where the requested operation did not complete reliably.

Retryable outcomes are:

- transient source-acquisition failure;
- provider execution failure;
- invalid provider output;
- transient publication-write failure.

Non-retryable outcomes are:

- structural rejection;
- valid semantic rejection;
- deterministic validation failure caused by actual invalid state;
- contradictory validation state;
- publication precondition failure.

Retry will not be used to repeatedly regenerate valid but rejected content until a pass appears.
A valid rejection remains a terminal content outcome unless a later material change triggers a new rerun.

#### D07 Retry scope

Retry will rerun only the failed operation by default.
Accepted upstream artifacts will remain reusable while their inputs and behavior versions remain current.

Examples, not exhaustive:

- retry one failed Quiz-prompt generation operation without rerunning accepted summaries or target phrases;
- retry one failed `PublicationHandoff` write without rerunning content generation or gate evaluation.

Before retry, orchestration will confirm that required inputs and relevant behavior versions remain current.
A changed input or behavior version converts the attempt into a rerun under D05 rather than a retry.

A retry blocks only the dependent suffix for the affected path or mutation.
Independent sibling paths may continue.

#### D08 Bounded retry and exhaustion

Every retryable operation will have a finite retry bound.
The exact attempt count, delay, timeout, and backoff remain implementation choices.

Retry exhaustion produces a terminal orchestration outcome for the affected scope.

| exhausted operation | terminal meaning |
|---|---|
| Initial source acquisition | The source discussion has acquisition failure and no dependent path processing begins. |
| Provider execution or invalid provider output | The affected stage has retry exhaustion and the affected Learning Unit remains incomplete. |
| `PublicationHandoff` write | Publication mutation failure; initial publication creates no current state and replacement preserves the previous committed state. |
| `AvailabilityChange` write | Availability mutation failure; the previous committed availability remains unchanged. |

Retry exhaustion for one path-local operation does not stop independent sibling paths.
No exhausted operation may continue retrying without a new explicit rerun or operational action.

#### D09 Distinct unpublished terminal outcomes

The Pipeline will distinguish these unpublished terminal outcomes:

| outcome | meaning |
|---|---|
| `rejected` | Processing completed, but the source path, generated content, or publication candidate failed accepted criteria. |
| `incomplete` | Required generation, evaluation, or mutation processing did not complete. |
| `contradictory` | Current Pipeline evidence contains internally incompatible claims and indicates a Pipeline defect. |

None of these outcomes will create or replace Application-visible published current state.
The Pipeline will retain the current internal outcome and controlled cause evidence for diagnosis, rerun selection, and batch reporting.

A rejected replacement, incomplete replacement, or contradictory replacement will preserve the previous committed published state.
The exact persistence technology and database schema remain implementation choices.

#### D10 Batch continuation boundary

A processing batch may contain multiple independent source discussions.
Failure, rejection, incompleteness, contradiction, or publication failure in one discussion will not stop independent discussions in the same batch.

Batch-wide processing will stop only when a shared execution precondition is invalid for the batch as a whole.
Examples, not exhaustive:

- invalid shared Pipeline configuration;
- gate configuration not eligible for unattended publication;
- unavailable shared provider configuration required by every remaining item;
- another common prerequisite that makes every remaining item invalid to execute.

Batch continuation will preserve every required stage and publication-gate dimension.
It will not skip validation or publication checks to keep the batch moving.

#### D11 Scope-specific completion outcomes

The Pipeline will not use one generic `completed` marker across all processing scopes.
Each scope will expose a terminal outcome that preserves its semantic meaning.

Examples, not exhaustive:

| scope | terminal outcomes |
|---|---|
| Source acquisition | acquired, reused, acquisition failed. |
| Normalization | accepted normalized source, normalization failed, accepted zero-path result. |
| Path processing | retained valid path, structural rejection, semantic rejection, evaluation failure. |
| Learning Unit processing | complete unit, incomplete unit, rejected unit. |
| Publication gate | accepted, rejected, contradictory. |
| Published-content mutation | committed, precondition failed, mutation failed. |
| Availability change | committed withdrawal, committed restoration, precondition failed, mutation failed. |

A terminal outcome means the scope finished processing.
It does not imply success or permission to enter the next stage.
Only the declared accepted outcome for one scope may enable its dependent stage.

#### D12 Minimum current-run diagnostics

Current-run diagnostics will retain enough evidence to explain retry, rejection, exhaustion, incompleteness, contradiction, skipped dependent stages, batch continuation, and publication mutation failure.

The minimum evidence is:

- source discussion, path, Learning Unit, publication attempt, and stage scope when applicable;
- terminal or retry outcome;
- controlled cause category;
- retry attempts and exhaustion state;
- orchestration and relevant component behavior versions;
- skipped dependent stages and skip cause;
- whether sibling paths or discussions continued;
- whether a failed publication mutation preserved the previous committed state.

Raw prompts, complete provider responses, every transient attempt, and permanent historical replay are not required.
Diagnostics must explain the current run without requiring retention of all intermediate attempts.

#### D13 Post-level failure blocks the complete Learning Unit

One failed or incomplete interaction within a valid Learning Path makes the complete Learning Unit for that path incomplete.

The Pipeline will not:

- publish only the successful posts;
- skip the failed post;
- shorten the valid Learning Path;
- mutate the path to salvage a partial unit.

Accepted earlier post-level intermediates may remain reusable for a later rerun when their inputs and behavior versions remain current.
The incomplete path will not stop independent sibling paths.

#### D14 Material-change rerun start points

Rerun will begin at the earliest stage affected by the material change.

| material change | default rerun start |
|---|---|
| Retained authentic source replacement | Normalization and every dependent downstream stage. |
| Source Adapter discovery, eligibility, URL extraction, canonicalization, or same-crawl deduplication change | Source Adapter discovery, followed by canonical URL lookup and acquisition decisions. |
| Source Adapter fetch execution, completeness, or acquisition-interpretation change | Acquisition compatibility reevaluation; reacquire source when compatibility cannot be proven. |
| Source Adapter normalization, quote, relationship, post-identity, or Discussion Path behavior change | Normalization from compatible retained authentic source and every dependent downstream stage. |
| Unisolated Source Adapter behavior change | Source Adapter discovery and every dependent decision. |
| Common Pipeline orchestration or composition change | First Common Pipeline processing stage. |
| Generation provider or generation-prompt change | Earliest affected generation stage. |
| Evaluator provider, evaluator prompt, or evaluation behavior change | Earliest affected evaluation stage. |
| Deterministic-validator change | Earliest affected deterministic validation stage. |
| Publication-gate configuration change | Gate evaluation, unless the change also invalidates upstream evaluation evidence. |
| Publication write failure with unchanged accepted handoff | Retry only the failed write operation. |
| Withdrawal or restoration request | Execute only the applicable `AvailabilityChange`; content generation is not rerun. |

A narrower rerun boundary is allowed only when unaffected upstream artifacts can be proven current.
When impact within the Common Pipeline cannot be isolated reliably, the Pipeline will rerun from the first Common Pipeline processing stage.
When Source Adapter impact cannot be isolated reliably, the Pipeline will rerun from Source Adapter discovery.

#### D15 Aggregated completion by processing scope

Each processing scope completes when all required child scopes have reached terminal outcomes.

| scope | completion condition |
|---|---|
| Candidate path | Retained, rejected, or incomplete. |
| Learning Unit | Published, rejected, incomplete, or publication failed. |
| Publication attempt | Committed, gate rejected, precondition failed, or mutation failed. |
| Source discussion | Every retained or rejected path and every required publication attempt has reached a terminal outcome. |
| Batch | Every source discussion has reached a terminal outcome, or a batch-wide precondition failure has terminalized all remaining items as unexecutable. |

Aggregated completion does not mean that every child succeeded.
A source discussion or batch may complete with mixed outcomes.

A source discussion may also complete normally with zero valid paths or zero Learning Units when the required derivation and evaluation scopes finished successfully.

#### D16 Aggregated operational result

Source-discussion and batch orchestration will expose a controlled aggregate result separate from published content.

The aggregate result set is:

- `completed_with_output`;
- `completed_with_zero_output`;
- `completed_with_mixed_outcomes`;
- `failed_shared_precondition`.

The operational result may include controlled counts for valid paths, published units, rejected units, incomplete units, and publication failures.

Application-visible publication will expose only committed current published content and opaque provenance references already allowed by the publication contract.
Pipeline rejection, incompleteness, retry history, component versions, and internal diagnostics remain outside the Application publication surface.

Zero output may be a successful aggregate result when derivation and evaluation completed normally.

#### D17 Adapter-led discovery and orchestration input/output boundary

The first-MVP Source Adapter will discover eligible discussions through configured listing crawl.
The orchestration caller will not be required to submit one canonical discussion URL per source discussion.

Orchestration input consists conceptually of:

- current Source Adapter and crawl-scope configuration;
- current Common Pipeline and component configuration;
- available retained-source and current-artifact references;
- operation intent, such as new crawl processing or rerun from retained source.

The Source Adapter will output:

- discovered canonical discussion URL and authentic discussion identity;
- canonicalized discovery evidence;
- complete fetch evidence or acquisition failure when orchestration requests a fetch.

Orchestration will record whether complete retained source was reused or newly established.
Common Pipeline processing will consume Adapter-established authentic discussion identity, retained authentic source, eligible current artifacts, and rerun intent.

No orchestration input may authorize validation skipping, publication-gate override, partial-unit publication, or removal of failed posts from an accepted path.

#### D18 Canonical-URL deduplication and retained-source reuse boundary

The Source Adapter will canonicalize discovered discussion URLs and deduplicate repeated canonical URLs within one crawl result before handing discussions to orchestration.

Orchestration will perform retained-source lookup by canonical discussion URL before requesting a fetch.

| condition | owner and outcome |
|---|---|
| The same canonical URL appears multiple times in one crawl | Source Adapter emits one canonical discussion discovery. |
| Complete retained source already exists for the canonical URL | Orchestration does not request a new fetch and records `reused_retained_source`. |
| No retained source exists for the canonical URL | Orchestration requests source-specific fetching from the Source Adapter. |
| Requested fetch is partial, unavailable, or failed | Source Adapter reports acquisition failure; orchestration establishes no retained source and starts no dependent processing. |

The Source Adapter owns source-specific URL canonicalization, discovery deduplication, fetching, and fetch-result interpretation.
Orchestration owns retained-source lookup, fetch-versus-reuse selection, retry policy, and dependent-stage continuation.

The Source Adapter will not need direct knowledge of retained-source persistence to decide whether historical source is reusable.

#### D19 Retry-count ownership correction

The design contract will decide whether an outcome is retryable, require every retryable operation to terminate under a finite bound, and define exhaustion semantics.

Concrete retry counts, including the number of invalid-output attempts for semantic evaluators, belong to implementation configuration rather than design authority.

A valid semantic pass or valid semantic rejection will not be retried.
Invalid semantic-evaluator output remains retryable.
Exhaustion remains a semantic evaluation failure rather than a content rejection.

PRODUCT-ADR-PIPELINE-010 fixed one initial attempt plus at most two additional invalid-output attempts.
Because that accepted ADR over-specified an implementation parameter, PRODUCT-ADR-PIPELINE-023 supersedes it while preserving the semantic evaluation contract and removing the fixed attempt count.

The superseding decision does not introduce one universal retry count for acquisition, provider execution, evaluation, or publication operations.

### Accepted ADR authority

| ADR | authority established |
|---|---|
| PRODUCT-ADR-PIPELINE-020 | Orchestration boundary, Adapter-led discovery, canonical-URL deduplication, retained-source fetch-versus-reuse ownership, independent path and discussion continuation, and aggregate completion. |
| PRODUCT-ADR-PIPELINE-024 | Current artifact retention and reuse, execution-behavior evidence, source-stage-aware conservative rerun fallback, material-change rerun boundaries, and stable identity preservation; supersedes PRODUCT-ADR-PIPELINE-021. |
| PRODUCT-ADR-PIPELINE-022 | Retryable and non-retryable outcomes, operation-local retry, finite implementation-configured bounds, exhaustion, unpublished terminal outcomes, whole-unit blocking, and current-run diagnostics. |
| PRODUCT-ADR-PIPELINE-023 | Complete independent semantic evaluation authority with invalid-output retry retained and concrete attempt count delegated to implementation; supersedes PRODUCT-ADR-PIPELINE-010. |

D01, D02, D10, D11, and D15 through D18 materialized primarily in PRODUCT-ADR-PIPELINE-020.
D03 through D05 and D14 materialized in PRODUCT-ADR-PIPELINE-024 after independent review corrected the Source Adapter and evaluator-provider rerun boundaries.
D06 through D09, D12, D13, and the general retry-parameter boundary in D19 materialized in PRODUCT-ADR-PIPELINE-022.
The semantic-evaluator correction in D19 materialized in PRODUCT-ADR-PIPELINE-023.

No normative specification changed during T06 ADR authoring.
PRODUCT-ADR-PIPELINE-010 and PRODUCT-ADR-PIPELINE-021 are superseded history.

### Independent review correction

The first independent review returned `NEEDS REVISION` with no blocking finding.

- F-MAJ-01 found that PRODUCT-ADR-PIPELINE-021 started every Source Adapter change at normalization, which could reuse an incompatible canonical discussion or retained source.
- F-MIN-01 found that evaluator-provider changes were not separated from generation-provider changes.
- F-MIN-02 found that PRODUCT-ADR-PIPELINE-020's coarse orchestration sequence mixed publication handoff with availability-only mutation.

PRODUCT-ADR-PIPELINE-024 supersedes PRODUCT-ADR-PIPELINE-021 and starts rerun at the earliest affected discovery, acquisition, normalization, generation, or evaluation stage.
PRODUCT-ADR-PIPELINE-020 now clarifies distinct publication and availability-only operation paths without changing their accepted meaning.

### Focused re-review and closure

The focused re-review returned `PASS`.

- F-MAJ-01 is closed: Source Adapter discovery, acquisition, and normalization changes now begin at their earliest affected source-side boundary, and unisolated Adapter changes rerun from discovery.
- F-MIN-01 is closed: generation-provider and evaluator-provider changes now have distinct rerun start points.
- F-MIN-02 is closed: publication and availability-only processing are separate orchestration paths.
- No regression finding was reported.
- PRODUCT-ADR-PIPELINE-024 is complete current authority and PRODUCT-ADR-PIPELINE-021 remains superseded history.
- The accepted ADR dependency graph has no cycle.

Final post-closure verification completed successfully:

- `git diff --check` completed without reported output;
- strict specification validation returned `[strict]  All 34 file(s) OK.`;
- `git status --short` showed only the T06 Task, parent Work Item, superseded ADR updates, and new T06 ADRs.

All T06 design, review, and verification conditions are satisfied.
PRODUCT-TASK-PIPELINE-001-06 is `done` and T07 may begin.
