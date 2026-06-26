# PRODUCT-WORK-APPLICATION-003: Define complete-shuffle selection domain contracts

- **id**: PRODUCT-WORK-APPLICATION-003
- **status**: done
- **date**: 2026-06-26
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **impact_refs**:
  - PRODUCT-ADR-APPLICATION-001
  - PRODUCT-ADR-UI-001
  - spec:product.application
  - spec:product.application.learning_unit_selection
  - spec:product.application.published_content
  - spec:product.ui.learning_flow
- **tasks**:
  - PRODUCT-TASK-APPLICATION-003-01
  - PRODUCT-TASK-APPLICATION-003-02
  - PRODUCT-TASK-APPLICATION-003-03
  - PRODUCT-TASK-APPLICATION-003-04
  - PRODUCT-TASK-APPLICATION-003-05

## Goal

Define implementation-independent domain contracts for first-MVP complete-shuffle queue selection.

Make the selection policy and adapter obligations precise enough for later use-case, port, and persistence implementation planning.

## Boundary

This work item owns:

- `SelectionScope` meaning and the first-MVP `all` scope;
- the maximum of 100 references as application policy;
- uniqueness within one queue;
- allowed repetition across later queues;
- behavior when fewer than 100 units are available;
- absence of learner-specific reservation and backend queue history;
- bounded random selection as a semantic operation;
- adapter obligations for availability, scope, maximum count, uniqueness, and ordering;
- domain invariants and invalid-result handling;
- extension boundaries for source, topic, discussion, difficulty, and learner-history scopes;
- ADR and specification updates required by the resolved design.

This work item does not own:

- exact randomization or sampling algorithms;
- SQL, database indexes, query plans, or persistence technology;
- learner-history implementation or durable learner identity;
- queue identity, queue persistence, reservation, or backend queue position;
- PWA queue position, progression, retry, or presentation behavior;
- concrete HTTP requests, responses, routes, or status codes;
- complete learning-unit retrieval beyond constraints required by queue selection.

Database adapters must remain able to perform bounded selection without loading every available reference into the domain layer.

Selection rules and validation must remain independent from database adapter implementation.

## Impact Scope

| ref | impact |
|---|---|
| PRODUCT-ADR-APPLICATION-001 | Preserve the accepted bounded queue, all-available scope, database-side sampling, and domain-owned invariant decisions. |
| PRODUCT-ADR-UI-001 | Preserve PWA ownership of transient queue position and learner-flow state. |
| `spec:product.application` | Keep the application overview aligned with detailed complete-shuffle ownership and exclusions. |
| `spec:product.application.learning_unit_selection` | Define scope, queue policy, selection operation, adapter obligations, and invalid-result semantics. |
| `spec:product.application.published_content` | Preserve current availability as the selection eligibility source. |
| `spec:product.ui.learning_flow` | Preserve UI ownership of queue position, exhaustion, and learner progression. |

## Task flow

```text
T01 Establish selection-design baseline
  |
  v
T02 Define scope and queue invariants
  |
  v
T03 Define bounded selection and adapter obligations
  |
  v
T04 Reconcile ADR and specification contracts
  |
  v
T05 Independent integrated review
```

- T01 classifies accepted contracts, specification gaps, architectural decisions, and implementation details.
- T02 resolves `SelectionScope`, queue bounds, uniqueness, repetition, and state exclusions.
- T03 resolves the semantic selection operation, adapter obligations, validation, and invalid-result handling.
- T04 reflects the resolved contracts in their owning ADRs and specifications without duplicating UI or persistence ownership.
- T05 independently verifies implementation readiness and cross-area consistency.

## Task Candidates

| task | responsibility |
|---|---|
| PRODUCT-TASK-APPLICATION-003-01 | Establish the accepted complete-shuffle baseline and explicit unresolved decision set. |
| PRODUCT-TASK-APPLICATION-003-02 | Define `SelectionScope`, first-MVP queue policy, domain invariants, and future-scope extension boundaries. |
| PRODUCT-TASK-APPLICATION-003-03 | Define bounded random selection semantics, adapter obligations, result validation, and invalid-result handling. |
| PRODUCT-TASK-APPLICATION-003-04 | Reconcile accepted ADRs and application, published-content, and UI specifications. |
| PRODUCT-TASK-APPLICATION-003-05 | Perform an independent integrated review and record readiness findings. |

## Completion Condition

- `SelectionScope` has an implementation-independent meaning.
- The first-MVP `all` scope includes every currently available unit as an eligible candidate without requiring every candidate in one queue.
- Queue maximum, uniqueness, ordering, and fewer-than-maximum behavior are explicit.
- Repetition is prohibited within one queue and allowed across later queue requests.
- Queue issuance creates no learner-specific reservation, queue identity, backend queue position, or queue history.
- Bounded random selection is defined semantically without selecting an exact algorithm.
- The adapter contract preserves database-side bounded selection.
- Adapter obligations cover availability, scope, maximum count, uniqueness, and randomized ordering.
- Domain validation and invalid adapter-result handling are explicit and transport-independent.
- Availability observed during selection is distinguished from later retrieval-time availability changes.
- Future source, topic, discussion, and difficulty scopes fit the selection model without changing queue-state ownership.
- Learner-history scope remains behind a separate durable identity and progress decision.
- Any new architectural decision is recorded in an accepted ADR.
- Affected specifications contain the current contract without duplicated ownership.
- PRODUCT-TASK-APPLICATION-003-05 records a final `PASS` verdict with no blocking findings.
- Concrete implementation work can be identified without selecting persistence or transport technology.

## Evidence

### Result

- **Verdict**: PASS.
- PRODUCT-TASK-APPLICATION-003-01 through PRODUCT-TASK-APPLICATION-003-05 are complete.
- The complete-shuffle selection contract is implementation-ready.
- Implementation planning may begin for this module.

### Contract completion

- `SelectionScope` is implementation-independent.
- The first MVP applies `All` without requiring a full-corpus queue.
- `maximum_count` is `100`.
- Queue size is exactly `min(maximum_count, eligible_count)`.
- Empty, below-limit, exact-limit, and above-limit candidate sets are defined.
- References are unique within one queue and may repeat across later queues.
- Returned order is randomized and preserved.
- `eligible_count` is semantic only and is not returned.
- Queue issuance creates no reservation, backend queue identity, backend position, backend history, or durable learner progress.
- Database-side bounded selection remains possible without loading the complete candidate set into application memory.
- Adapter obligations cover availability, scope, exact cardinality, uniqueness, stable references, and randomized ordering.
- Application validation is limited to observable array properties.
- Observable invalid arrays are rejected without normalization.
- Selection-time and retrieval-time availability are distinct.
- Future source, topic, discussion, and difficulty constraints fit by intersection.
- Learner-history selection remains deferred behind separate durable identity, progress ownership, and history-access decisions.

### Ownership

- `spec:product.application.learning_unit_selection` owns selection scope, cardinality, adapter obligations, validation, and invalid-result handling.
- `spec:product.application.published_content` owns current availability and published runtime state.
- `spec:product.ui.learning_flow` owns transient queue state and learner-flow transitions.
- Successful empty queues show `Quiz list was empty.` with `Back to main` and do not trigger queue retry.
- Queue-acquisition request failures continue to use UI retry behavior.
- No HTTP status, persistence, SQL, framework, or exact randomization decision entered the normative contract.

### Independent review

- Codex independently reviewed every impact ref and completion condition.
- Final verdict: `PASS`.
- Blocking findings: none.
- The previous empty-result transition finding is closed.
- One non-blocking advisory remains in PRODUCT-ADR-UI-001 `## Consequences`.
- The advisory is stale historical wording only and does not block closure.

### Validation

- Design Records MCP does not index the target application and UI refs.
- Filesystem rereads confirmed the final current text and canonical references.
- No repository-wide CLI validator or Git status result is claimed in this tool environment.
