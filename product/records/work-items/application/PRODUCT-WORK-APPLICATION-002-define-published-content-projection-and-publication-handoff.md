# PRODUCT-WORK-APPLICATION-002: Define published-content projection and publication handoff

- **id**: PRODUCT-WORK-APPLICATION-002
- **status**: done
- **date**: 2026-06-26
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **impact_refs**:
  - PRODUCT-ADR-APPLICATION-001
  - PRODUCT-ADR-PIPELINE-001
  - PRODUCT-ADR-PIPELINE-002
  - PRODUCT-ADR-PIPELINE-004
  - PRODUCT-ADR-PIPELINE-005
  - spec:product
  - spec:product.application
  - spec:product.application.published_content
  - spec:product.pipeline
  - spec:product.learning.learning_unit
  - spec:product.ui.learning_flow
- **tasks**:
  - PRODUCT-TASK-APPLICATION-002-01
  - PRODUCT-TASK-APPLICATION-002-02
  - PRODUCT-TASK-APPLICATION-002-03
  - PRODUCT-TASK-APPLICATION-002-04
  - PRODUCT-TASK-APPLICATION-002-05

## Goal

Define an implementation-independent published-content projection and pipeline publication handoff.

Make the boundary precise enough for later application, pipeline, and persistence implementation planning.

## Boundary

This work item owns:

- stable learning-unit identity within the current published projection;
- separation of current content and runtime availability;
- publication, withdrawal, and republication transition semantics;
- the semantic publication handoff from pipeline ownership to published content;
- the precondition that publication validation has already completed;
- atomic switching of content, provenance reference, and resulting availability;
- concurrent-read consistency across publication transitions;
- opaque current-provenance-reference reachability;
- pipeline write ownership and application read ownership;
- specification and ADR updates required by the resolved design.

This work item does not own:

- concrete database tables, columns, indexes, or constraints;
- database product, ORM, or transaction syntax;
- pipeline generation prompts, model roles, or publication-gate criteria;
- queue selection or learning-unit retrieval behavior beyond handoff constraints;
- HTTP routes, wire schemas, or framework-specific commands;
- historical source snapshots, intermediate generations, runtime revision history, exact replay, or rollback unless a new requirement adopts them.

## Impact Scope

| ref | impact |
|---|---|
| PRODUCT-ADR-APPLICATION-001 | Preserve the accepted published-content boundary and atomic replacement decision. |
| PRODUCT-ADR-PIPELINE-001 | Historical decision superseded by PRODUCT-ADR-PIPELINE-005. |
| PRODUCT-ADR-PIPELINE-002 | Keep the provider boundary dependent on the current pipeline architecture. |
| PRODUCT-ADR-PIPELINE-004 | Historical path-generation and publication-gate decision superseded by PRODUCT-ADR-PIPELINE-005. |
| PRODUCT-ADR-PIPELINE-005 | Preserve staged path generation, automated publication gating, source reuse, and current-only retention. |
| `spec:product` | Route the current pipeline architecture to PRODUCT-ADR-PIPELINE-005. |
| `spec:product.application` | Keep application ownership and topic routing aligned with the detailed boundary. |
| `spec:product.application.published_content` | Define projection identity, lifecycle, availability, provenance, and observable consistency. |
| `spec:product.pipeline` | Define the pipeline side of publication, withdrawal, and republication handoff. |
| `spec:product.learning.learning_unit` | Preserve complete learning-unit, attribution, and unavailability requirements. |
| `spec:product.ui.learning_flow` | Preserve immutability of a successfully loaded learning unit. |

## Task flow

```text
T01 Establish contract baseline and unresolved decisions
  |
  v
T02 Define projection identity and lifecycle
  |
  v
T03 Define publication handoff and consistency
  |
  v
T04 Reconcile ADR and specification contracts
  |
  v
T05 Independent integrated review
```

- T01 classifies accepted contracts, specification gaps, and decisions requiring investigation.
- T02 resolves the current projection and publication lifecycle semantics.
- T03 resolves the pipeline handoff, provenance reachability, and concurrent visibility guarantees.
- T04 reflects the resolved design across all affected records without duplicating ownership.
- T05 independently verifies implementation readiness and cross-area consistency.

## Task Candidates

| task | responsibility |
|---|---|
| PRODUCT-TASK-APPLICATION-002-01 | Establish the accepted contract baseline and explicit unresolved decision set. |
| PRODUCT-TASK-APPLICATION-002-02 | Define stable identity, current projection, availability, and lifecycle transitions. |
| PRODUCT-TASK-APPLICATION-002-03 | Define the semantic publication handoff, provenance obligations, and observable consistency. |
| PRODUCT-TASK-APPLICATION-002-04 | Reconcile accepted ADRs and application, pipeline, learning, and UI specifications. |
| PRODUCT-TASK-APPLICATION-002-05 | Perform an independent integrated review and record readiness findings. |

## Completion Condition

- Stable identity and current projection semantics are explicit.
- Current content and runtime availability remain separate concepts.
- Publication, withdrawal, replacement, and republication transitions have unambiguous preconditions and outcomes.
- The pipeline-to-published-content handoff defines its semantic input and writer obligations.
- Publication requires completed validation and publication judgment.
- Content, provenance reference, and resulting availability switch as one observable publication state.
- Concurrent application reads cannot observe a mixed or partial publication.
- The provenance reference remains opaque to the application and reaches current pipeline-owned evidence.
- Pipeline write ownership and application read ownership remain explicit.
- Any new architectural decision is recorded in an accepted ADR.
- Affected specifications contain the current contract without duplicated ownership.
- PRODUCT-TASK-APPLICATION-002-05 records a `PASS` verdict with no blocking findings.
- Concrete implementation work can be identified without selecting persistence or transport technology.

## Evidence

### Completion review

- **Verdict**: PASS.
- T01 through T05 are complete.
- PRODUCT-TASK-APPLICATION-002-05 records a final `PASS`.
- F-B-01 is `CLOSED`.
- F-B-02 is `CLOSED`.
- No critical finding remains.
- Implementation planning may begin for this module.
- No persistence technology was selected.
- No transport technology was selected.
- PRODUCT-REQ-APPLICATION-001 remains open until its other work items are completed.

### Task completion

| task | status | reviewed outcome |
|---|---|---|
| PRODUCT-TASK-APPLICATION-002-01 | done | Baseline contracts and unresolved design inputs were classified. |
| PRODUCT-TASK-APPLICATION-002-02 | done | Published projection identity, lifecycle, availability, and replacement invariants were resolved. |
| PRODUCT-TASK-APPLICATION-002-03 | done | Publication handoff, provenance reachability, writer ownership, and read consistency were resolved. |
| PRODUCT-TASK-APPLICATION-002-04 | done | ADRs and specifications were reconciled across the affected records. |
| PRODUCT-TASK-APPLICATION-002-05 | done | Independent final re-review passed with F-B-01 and F-B-02 closed. |

All five tasks reference PRODUCT-WORK-APPLICATION-002.
All five tasks reference PRODUCT-REQ-APPLICATION-001.
The work-item `tasks` metadata lists PRODUCT-TASK-APPLICATION-002-01 through PRODUCT-TASK-APPLICATION-002-05 exactly once.
No `blocked` or `not_started` child task remains for this work item.
No task evidence contains an unresolved blocker that conflicts with T05 closure.

### Impact-ref review

| ref | closure result |
|---|---|
| PRODUCT-ADR-APPLICATION-001 | Accepted application boundary remains aligned with the published-content projection and atomic replacement contract. |
| PRODUCT-ADR-PIPELINE-001 | Exists as `superseded`; its active deterministic-stage decision is carried forward by PRODUCT-ADR-PIPELINE-005. |
| PRODUCT-ADR-PIPELINE-002 | Exists as `accepted`; its provider boundary depends on PRODUCT-ADR-PIPELINE-005. |
| PRODUCT-ADR-PIPELINE-004 | Exists as `superseded`; its active path and publication-gate decisions are carried forward by PRODUCT-ADR-PIPELINE-005. |
| PRODUCT-ADR-PIPELINE-005 | Exists as `accepted`; it owns staged path generation, publication gating, source reuse, and current-only retention. |
| `spec:product` | Routes learning, pipeline, application, and UI ownership consistently. |
| `spec:product.application` | Owns runtime selection, availability-aware retrieval, use cases, and query ports. |
| `spec:product.application.published_content` | Defines identity, complete learning unit, availability, and opaque provenance as the current projection. |
| `spec:product.application.learning_unit_selection` | Defines queue and retrieval semantics without owning loaded-unit immutability. |
| `spec:product.pipeline` | Defines `PublicationHandoff` and `AvailabilityChange` without selecting storage or transport mechanisms. |
| `spec:product.learning.learning_unit` | Owns learning-unit composition, attribution meaning, and publication-gate learning semantics. |
| `spec:product.ui.learning_flow` | Owns loaded-unit immutability and learner-flow replacement behavior. |

### Completion-condition coverage

| condition | result | evidence |
|---|---|---|
| Stable identity and current projection semantics are explicit. | PASS | `spec:product.application.published_content` defines stable identity and the four-element projection. |
| Current content and runtime availability remain separate. | PASS | Availability is separate from complete current content. |
| Publication transitions have unambiguous preconditions and outcomes. | PASS | `spec:product.pipeline` defines `PublicationHandoff` preconditions and writer obligations. |
| Withdrawal transitions have unambiguous preconditions and outcomes. | PASS | `AvailabilityChange` requires an existing current projection and changes only availability. |
| Replacement transitions have unambiguous preconditions and outcomes. | PASS | Replacement uses `PublicationHandoff` and switches content, provenance, and availability together. |
| Republication or availability-restoration semantics are unambiguous. | PASS | New content uses `PublicationHandoff`; availability restoration without content change uses `AvailabilityChange`. |
| The pipeline-to-published-content handoff defines its semantic input. | PASS | `PublicationHandoff` includes identity, complete unit, opaque provenance, and resulting availability. |
| Publication requires completed validation and publication judgment. | PASS | `PublicationHandoff` preconditions require structural validation and publication judgment before mutation. |
| Content, provenance, and availability switch as one observable publication state. | PASS | Atomic replacement prohibits mixed content, mismatched provenance, or availability from another judgment. |
| Concurrent reads cannot observe mixed or partial publication. | PASS | Application reads observe no projection or one complete projection for initial publication, and previous or new complete projection for replacement. |
| Availability-only changes preserve content and provenance. | PASS | `AvailabilityChange` leaves current content and current provenance unchanged. |
| Provenance remains opaque to application logic. | PASS | Application specs require opaque provenance and prohibit pipeline processing-data interpretation. |
| Current pipeline-owned evidence remains reachable. | PASS | The provenance reference reaches current pipeline-owned source and generation evidence. |
| Pipeline write ownership is explicit. | PASS | The pipeline is the only semantic owner of published-content writes. |
| Application read ownership is explicit. | PASS | The application reads only the published-content projection. |
| Attribution meaning remains learning-owned. | PASS | Attribution remains inside `spec:product.learning.learning_unit`. |
| Loaded-unit behavior remains UI-owned. | PASS | Loaded-unit immutability is normative only in `spec:product.ui.learning_flow`. |
| Current-only retention remains the first-MVP contract. | PASS | PRODUCT-ADR-PIPELINE-005 and `spec:product.pipeline` exclude historical source snapshots and intermediate generations. |
| No runtime revision history, exact replay, or rollback requirement was introduced. | PASS | Published-content and pipeline specs exclude runtime revision history, exact replay, and rollback. |
| No persistence, transport, transaction, command, event, or framework decision entered the design. | PASS | The current records remain semantic and defer storage, transaction, transport, and framework mechanisms. |
| T05 records a final `PASS`. | PASS | PRODUCT-TASK-APPLICATION-002-05 final re-review records `PASS`. |
| Implementation planning can begin without reopening the ownership boundary. | PASS | T05 states implementation planning may begin for this module. |

### Validation

The repository-local preferred validator path is absent:

```text
Test-Path -LiteralPath 'product\src\tools\validate_spec.py'
False
```

The shared Brewprint validator was run against this repository's specification tree:

```text
python -X utf8 C:\Users\imved\projects\brewprint\product\src\tools\validate_spec.py product/records/spec --strict --no-color
[strict]  All 20 file(s) OK.
```

`git diff --check` produced no whitespace errors.
The command printed only CRLF conversion warnings for existing changed files in this checkout.

`git status --short` showed a dirty working tree with the expected ADR, specification, requirement, task, work-item, and protocol changes.
The status also showed PRODUCT-ADR-PIPELINE-005, PRODUCT-TASK-APPLICATION-002-01 through PRODUCT-TASK-APPLICATION-002-05, and this work item as untracked.
