# PRODUCT-TASK-PIPELINE-001-01: Establish Pipeline authority baseline and exact gap inventory

- **id**: PRODUCT-TASK-PIPELINE-001-01
- **status**: done
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PIPELINE-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 1.5d
- **depends_on**: []
- **outputs**:
  - PRODUCT-WORK-PIPELINE-001

## Goal

Establish the exact current Pipeline authority, unresolved decisions, specification gaps, evidence inputs, and focused child-specification plan.

## Work

1. Read current Pipeline ADRs and distinguish accepted authority from superseded history.
2. Read PRODUCT-INV-PIPELINE-001, PRODUCT-INV-PIPELINE-002, fixtures, and experiment scripts as evidence.
3. Read `spec:product.pipeline`, the completed Learning specifications, and Application published-content contracts.
4. Inventory current Pipeline contracts for:
   - source acquisition and retained-source reuse;
   - authentic-post normalization and relationship preservation;
   - path enumeration, structural validation, and suitability filtering;
   - summary, phrase, prompt, and quiz generation;
   - mechanical and semantic validation;
   - retry, rejection, and incomplete output;
   - artifact identity, generated-content versioning, and provenance;
   - publication gating, handoff, availability change, and withdrawal;
   - orchestration, rerun, reuse, partial failure, and completion.
5. Classify each gap as existing authority, missing ADR, specification elaboration, evidence need, or implementation-only choice.
6. Record exact decision points for T02 through T06.
7. Define the focused child-specification map for T07.
8. Confirm that Learning meaning and Application runtime reads remain fixed inputs.
9. Do not change normative specifications or adopt new Pipeline decisions.

## Done condition

- Every required Pipeline design area has one current-state judgment.
- Every normative gap names current authority or an explicit missing-ADR route.
- Evidence is separated from normative authority.
- Implementation-only choices are excluded from design decisions.
- T02 through T07 have exact bounded inputs.
- The child-specification map covers source acquisition, normalization, paths, generation, validation, provenance, publication, and orchestration.
- No normative ADR or specification changes occur.

## Verification

- Confirm accepted Pipeline ADR status and supersession chains.
- Confirm PRODUCT-WORK-LEARNING-001 is treated as fixed input.
- Confirm Application published-content semantics are not reopened.
- Confirm each gap has one semantic owner.
- Confirm the proposed specification map preserves `spec:product.pipeline` as the overview router.
- Validate H1, metadata, canonical refs, reciprocal relations, and required sections.
- Run strict specification validation, `git diff --check`, and `git status --short`.

## Evidence

### Execution boundary

- This task records the Pipeline baseline and gap inventory only.
- No Pipeline ADR or normative specification was created or changed.
- Learning semantics and Application runtime-read semantics remain fixed inputs.
- Concrete technology and implementation design remain excluded.

### Authority baseline

| input | role | current judgment |
|---|---|---|
| PRODUCT-ADR-PIPELINE-002 | Accepted Pipeline decision authority | Establishes the internal OpenAI-compatible provider boundary, provider isolation, capability handling, and untrusted-output validation. |
| PRODUCT-ADR-PIPELINE-005 | Accepted Pipeline decision authority | Establishes staged deterministic and bounded model processing, Packaging corpus use, retained-source reuse, path multiplicity, current-only retention, replacement, automated gating, and unavailability preservation. |
| PRODUCT-ADR-PIPELINE-001 | Superseded history | Superseded directly by PRODUCT-ADR-PIPELINE-005. Its retained deterministic-stage meaning is active only through PRODUCT-ADR-PIPELINE-005. |
| PRODUCT-ADR-PIPELINE-003 | Superseded history | Superseded by PRODUCT-ADR-PIPELINE-004, which is itself superseded by PRODUCT-ADR-PIPELINE-005. |
| PRODUCT-ADR-PIPELINE-004 | Superseded history | Superseded directly by PRODUCT-ADR-PIPELINE-005. Its retained path and publication-gate meaning is active only through PRODUCT-ADR-PIPELINE-005. |
| `spec:product.pipeline` | Current normative Pipeline contract | Holds the current overview-only contract and publication-writer obligations until focused child specifications replace detailed ownership in T07. |
| PRODUCT-WORK-LEARNING-001 | Completed fixed semantic input | Confirms Learning contracts passed independent review and must not be reopened by Pipeline design. |
| `spec:product.learning.learning_path` | Fixed Learning authority | Defines two-to-six path cardinality, source-grounded adjacency, independent validity, prefix overlap, and one-path-to-one-unit meaning. |
| `spec:product.learning.learning_unit` | Fixed Learning authority | Defines complete unit composition, identity exclusions, grounding, attribution, and non-compensating publication readiness. |
| `spec:product.learning.quiz_session` | Fixed Learning authority | Defines ordered materialization obligations consumed by Pipeline without owning Pipeline mechanics. |
| `spec:product.application.published_content` | Fixed Application authority | Defines one committed current state, availability, opaque provenance, atomic replacement visibility, and availability-only mutation meaning. |
| PRODUCT-INV-PIPELINE-001 | Evidence only | Demonstrates source capture, source-native relationship distinctions, exact source evidence, partial question/reply generation, and provenance needs. |
| PRODUCT-INV-PIPELINE-002 | Evidence only | Demonstrates authored-text separation, coarse projection, multiple valid paths, absolute filtering, deterministic coverage checks, and remaining harder-fixture needs. |

### Evidence observations and limits

| evidence | supported observation | limit |
|---|---|---|
| Golden topic `107565` fixture | Source-native reply targets, selected sequence order, authentic text, source capture metadata, and generated content are distinct responsibilities. | Only posts `#1` and `#2` have reviewed interactions. The fixture does not cover one complete two-to-six interaction unit. |
| `scripts/fetch_post_tree.py` | A deterministic tree projection can expose candidate branches. | The current helper projects both missing explicit targets and genuine topic-level responses to the opening post. The helper cannot define the final normalization contract. |
| `scripts/run_path_selection_experiment.py` and v3 run | Authored-text extraction, projection reasons, deterministic path checks, exact phrase validation, retry after invalid structured output, and complete review coverage are feasible. | The model selected `#1 -> #2 -> #4 -> #5`, not the reviewed `#7` variant. One model-selected path is not canonical authority. |
| Path-filtering comparison v1 | GPT-OSS and Qwen accepted six real paths and rejected three invalid controls with complete agreement. | The controls are narrow and partly deterministic. The result does not establish unattended production-gate quality. |
| Multi-quote observations in PRODUCT-INV-PIPELINE-002 | Quote references form a graph and authored text must remain separate from quoted material. | Exact quote-span modeling and unavailable-target behavior lack representative acceptance fixtures. |

### Gap inventory

| area | existing authority | missing ADR route | specification elaboration | evidence need | implementation-only choice |
|---|---|---|---|---|---|
| 1. Source acquisition, reuse, refresh, replacement, and failure | PRODUCT-ADR-PIPELINE-005 authorizes discovery, first fetch, retained reuse by known URL, no periodic refresh, and no freshness guarantee. | T02 owns source acquisition result meaning, reusable-source identity, explicit refresh or replacement semantics, source-change handling, and acquisition-failure outcomes. Each unsupported observable choice requires a Pipeline ADR. | T07 `source_acquisition` must define inputs, outcomes, retained reuse, replacement preconditions, and failure categories after T02 acceptance. | Add representative no-record, retained-record, changed-source, unavailable-source, partial-source, and failed-acquisition fixtures before implementation planning. | HTTP library, pagination code, timeout values, cache layout, retry delays, and storage technology. |
| 2. Authentic-post normalization and relationship preservation | PRODUCT-ADR-PIPELINE-005 assigns parsing and relationship preservation to deterministic processing. Learning fixes valid adjacency meaning. | T02 owns the source-independent authentic-post model, authored-versus-quoted separation, explicit reply evidence, genuine topic-level responses, unavailable explicit targets, projection reasons, source order, author identity, and metadata preservation. | T07 `source_normalization` must define normalized inputs, outputs, invariants, and preserved relationship evidence without exposing Discourse fields as domain semantics. | Add fixtures for unavailable reply targets, deleted or hidden posts, repeated quotes, multiple quote targets, malformed quote blocks, and missing author metadata. | HTML or Markdown parser, quote-removal algorithm, text-cleanup library, in-memory representation, and field serialization. |
| 3. Path enumeration, structural validation, and suitability filtering | PRODUCT-ADR-PIPELINE-005 authorizes deterministic enumeration, independent suitability judgment, zero or more retained paths, no canonical path, and prefix-overlap coexistence. Learning fixes cardinality and adjacency. | T03 owns deterministic enumeration order, candidate and valid-path identity inputs, duplicate meaning, candidate-state transitions, and retained rejection evidence when current authority is insufficient. | T07 `path_enumeration` and `path_validation` must separate candidate production, structural validity, semantic suitability, and rejection outcomes. | Add harder coherent, borderline, code-heavy, misleading-summary, unavailable-target, duplicate, and prefix-overlap fixtures. Current nine-case evidence is insufficient for unattended filtering approval. | Graph traversal algorithm, data structures, batching, model choice, thresholds, and ranking implementation. |
| 4. Summary, phrase, prompt, and quiz generation | PRODUCT-ADR-PIPELINE-005 authorizes reusable summaries, path-specific revision, target-phrase selection, separate quiz generation, bounded model tasks, and smallest-sufficient context. Learning fixes every learner-visible field and cardinality. | T04 owns observable stage boundaries for reusable summary, path revision, phrase selection, intent-prompt generation, and quiz generation. T04 also owns stage result meaning and grounding obligations when unsupported by current authority. | T07 `content_generation` must define declared inputs, outputs, grounding evidence, coverage, and downstream dependencies for each generation stage. | Create a reviewed complete unit with two-to-six interactions. Add harder summary-fidelity, uncertainty, unsupported-claim, distractor, and target-phrase fixtures. | Exact prompt text, model name, token budget, truncation method, provider assignment, JSON field names, and inference parameters. |
| 5. Mechanical and semantic validation | PRODUCT-ADR-PIPELINE-002 and PRODUCT-ADR-PIPELINE-005 require structured-output validation and treat model output as untrusted. Learning fixes structural and semantic readiness dimensions. | T02 owns validator provenance identity. T04 owns per-stage mechanical and semantic validation result meaning, complete coverage, incomplete results, and contradictory stage results. T05 owns final gate aggregation and rejection outcomes. | T07 `validation` must separate deterministic checks, semantic evaluations, coverage, contradiction handling, and orchestration-facing results. `publication` must consume those results without redefining Learning readiness. | Add adversarial structured outputs, missing-coverage outputs, contradictory verdicts, subtly misleading summaries, and plausible but unsupported options. | Validation library, schema language, threshold values, scoring implementation, and test framework. |
| 6. Retry, rejection, and incomplete output | Current authority permits invalid model output to be retried, rejected, or selected for review. Current specifications prohibit partial publication. | T06 owns retryable versus non-retryable outcomes, bounded retry meaning, exhaustion, rejected output, incomplete unit, exceptional review routing, and current-run diagnostic obligations. | T07 `orchestration` must define retry and exhaustion transitions. Stage-specific specs must expose stable failure outcomes without owning retry policy. | Add provider failure, invalid structured output, repeated grounding failure, validation contradiction, gate rejection, and publication-write failure scenarios. | Retry count, delay, backoff, timeout, circuit breaker, queue policy, and alerting implementation. |
| 7. Artifact identity, generated-content versioning, and provenance | PRODUCT-ADR-PIPELINE-005 anchors one logical unit to one valid path, replaces current generated content, excludes runtime revision history, and retains current source, validation, and publication provenance. Application requires one opaque provenance reference. | T02 owns authentic-source identity, normalized-artifact identity, valid-path identity inputs, stable learning-unit identity materialization, current generated-content version meaning, and provider, prompt, validator, and publication-decision provenance composition. | T07 `artifact_identity_and_provenance` must define current identities, replacement continuity, evidence routes, internal opacity, and handoff provenance obligations. | Add regeneration and replacement evidence showing identity stability across prompt, provider, validator, and generated-content changes. | Identifier encoding, UUID or hash choice, digest algorithm, table keys, provenance storage layout, and history retention implementation. |
| 8. Publication gate, handoff, availability change, and withdrawal | PRODUCT-ADR-PIPELINE-005 authorizes automated gating under human-approved criteria, exceptional review, unavailability, and preserved current evidence. Learning fixes non-compensating readiness. Application fixes committed current-state and handoff meaning. | T05 owns gate decision states, unattended eligibility, contradictory-result rejection, borderline escalation, withdrawal, restoration, handoff failure, and availability-decision outcomes not already fixed by Learning or Application. | T07 `publication` must define gate inputs, approvals, decisions, preconditions, `PublicationHandoff`, `AvailabilityChange`, withdrawal, restoration, and failure outcomes. | Add representative golden and harder gate fixtures. Add failed-handoff and availability-only mutation scenarios before implementation planning. | Transaction syntax, isolation level, persistence engine, write API, serialization, thresholds, and approval tooling. |
| 9. Orchestration, rerun, reuse, partial failure, and completion | PRODUCT-ADR-PIPELINE-005 defines the broad stage order, retained-source reuse, current-only retention, replacement, no historical replay, and current-run diagnostics. | T06 owns orchestration scopes, stage dependencies, rerun and reuse triggers, retained-versus-transient current artifacts, source or unit partial failure, batch continuation, publication failure, and completion semantics. | T07 `orchestration` must define source, path, unit, batch, gate, and publication completion outcomes with explicit upstream dependencies. | Add rerun matrices and fault scenarios for source replacement, prompt change, provider change, validator change, gate change, rejected units, and failed publication. | Workflow engine, concurrency, queue technology, scheduling, process topology, logging stack, and deployment. |

### Inputs passed to follow-up tasks

| task | exact input from T01 |
|---|---|
| PRODUCT-TASK-PIPELINE-001-02 | Resolve the missing source-acquisition, source replacement, normalization, relationship, identity, current-version, and provenance decisions listed in areas 1, 2, and 7. Preserve retained reuse, no periodic freshness, current-only retention, stable path-based unit identity, and opaque Application provenance. |
| PRODUCT-TASK-PIPELINE-001-03 | Consume accepted T02 identity and normalization decisions. Resolve remaining enumeration order, path identity, duplicate, state-transition, and rejection-evidence decisions. Define structural validation and independent absolute suitability filtering against fixed Learning rules. |
| PRODUCT-TASK-PIPELINE-001-04 | Consume retained valid paths and fixed Learning unit semantics. Resolve generation-stage and per-stage validation result decisions. Define reusable summary, path revision, phrase, prompt, quiz, grounding, coverage, invalid-output, incomplete-result, and contradiction contracts. |
| PRODUCT-TASK-PIPELINE-001-05 | Consume T02 provenance and T04 validation results. Preserve Learning readiness and Application current-state semantics. Resolve gate decisions, unattended eligibility, rejection, withdrawal, restoration, handoff, availability change, and failed-write outcomes. |
| PRODUCT-TASK-PIPELINE-001-06 | Consume all accepted stage contracts. Resolve orchestration scopes, stage order, reuse, rerun, retained current artifacts, retry, exhaustion, incomplete units, partial failure, batch continuation, diagnostics, and completion outcomes. |
| PRODUCT-TASK-PIPELINE-001-07 | Reflect only accepted ADR-backed decisions. Create the focused children below, convert `spec:product.pipeline` into an overview router, retain cross-area boundaries, and introduce no new normative choice. |

### Focused child-specification map for T07

| canonical ref | responsibility | must route elsewhere |
|---|---|---|
| `spec:product.pipeline.source_acquisition` | Discovery input, fetch and reuse outcomes, retained current source, refresh or replacement, and acquisition failure semantics. | Network client, storage, timeout, pagination, and retry implementation. |
| `spec:product.pipeline.source_normalization` | Source-independent authentic-post model, authored and quoted content separation, metadata, author identity, source order, reply evidence, topic-level projection, unavailable targets, and projection reasons. | Learning path meaning and source-specific serialized fields. |
| `spec:product.pipeline.path_enumeration` | Candidate inputs, deterministic enumeration, bounds, identity, duplicates, order, and prefix-overlap production. | Learning suitability meaning, graph algorithm, and session-time selection. |
| `spec:product.pipeline.path_validation` | Structural validation, independent semantic suitability filtering, coverage, accepted path output, and retained rejection evidence. | Learning-owned criteria, model choice, thresholds, and sibling ranking. |
| `spec:product.pipeline.content_generation` | Reusable summary, path-specific revision, phrase selection, intent prompt, quiz generation, grounding, and declared stage outputs. | Learner-visible meaning, prompt text, model selection, and serialization. |
| `spec:product.pipeline.validation` | Mechanical validation, semantic evaluation, complete-scope coverage, untrusted output, contradiction handling, and stable stage-result categories. | Learning readiness meaning, final publication decision, and validation library. |
| `spec:product.pipeline.artifact_identity_and_provenance` | Current source, normalized artifact, valid path, learning-unit, generated-content, provider, prompt, validator, and publication-decision identity and provenance routes. | Runtime revision history, identifier encoding, and Application interpretation of opaque provenance. |
| `spec:product.pipeline.llm_provider` | Internal provider interface, OpenAI-compatible transport baseline, adapter isolation, capability handling, logical model roles, and stable provider failures. | Vendor SDK use outside adapters, permanent model selection, and behavioral-equivalence assumptions. |
| `spec:product.pipeline.publication` | Gate inputs, approvals, unattended eligibility, decisions, rejection, withdrawal, restoration, publication handoff, availability change, and failed mutation semantics. | Learning readiness meaning, Application read semantics, and transaction implementation. |
| `spec:product.pipeline.orchestration` | Stage dependencies, rerun, reuse, retry, exhaustion, incomplete units, partial failure, batch continuation, current-run diagnostics, and completion. | Workflow engine, concurrency, queues, scheduling, logging stack, and deployment. |

`spec:product.pipeline` remains the area overview and authoritative topic router.
The overview retains Pipeline ownership, cross-area dependency direction, current first-MVP scope, and links to focused children.
Detailed normative stage contracts move to one owning child specification each.

### No-change judgments

- PRODUCT-ADR-PIPELINE-002 and PRODUCT-ADR-PIPELINE-005 remain unchanged.
- PRODUCT-ADR-PIPELINE-001, PRODUCT-ADR-PIPELINE-003, and PRODUCT-ADR-PIPELINE-004 remain unchanged superseded history.
- No Pipeline specification changed during T01.
- No Learning or Application decision was reopened.
- T02 through T07 remain `not_started`.

### Verification

- H1, required metadata, task-to-work-item relation, work-item-to-requirement relation, and T01 reciprocal membership were manually confirmed from current records.
- Accepted and superseded ADR statuses were confirmed from the source files.
- Learning and Application fixed-input boundaries were confirmed from current specifications.
- The final post-closure verification run completed successfully: `git diff --check` reported no whitespace error, strict specification validation returned `[strict]  All 34 file(s) OK.`, and `git status --short` showed only T01 and PRODUCT-WORK-PIPELINE-001 as modified.
- Git reported LF-to-CRLF working-copy warnings for the two changed Markdown files. These are line-ending warnings, not `git diff --check` failures.
- Every T01 done condition is satisfied.
- T01 is `done` and the change scope is commit-ready.
