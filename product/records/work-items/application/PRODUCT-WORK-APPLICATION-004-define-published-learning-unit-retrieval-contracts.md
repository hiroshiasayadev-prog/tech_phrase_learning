# PRODUCT-WORK-APPLICATION-004: Define published learning-unit retrieval contracts

- **id**: PRODUCT-WORK-APPLICATION-004
- **status**: done
- **date**: 2026-06-26
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **impact_refs**:
  - PRODUCT-ADR-APPLICATION-001
  - PRODUCT-ADR-APPLICATION-002
  - PRODUCT-ADR-APPLICATION-003
  - PRODUCT-ADR-APPLICATION-004
  - spec:product
  - PRODUCT-ADR-UI-001
  - spec:product.application
  - spec:product.application.learning_unit_selection
  - spec:product.application.published_content
  - spec:product.learning.learning_unit
  - spec:product.pipeline
  - spec:product.ui.learning_flow
- **tasks**:
  - PRODUCT-TASK-APPLICATION-004-01
  - PRODUCT-TASK-APPLICATION-004-02
  - PRODUCT-TASK-APPLICATION-004-03
  - PRODUCT-TASK-APPLICATION-004-04
  - PRODUCT-TASK-APPLICATION-004-05

## Goal

Resolve published learning-unit retrieval decisions through accepted ADRs.

Reflect those decisions into current specifications only after the decision records are accepted.

## Boundary

This work item owns the resolution flow for:

- retrieval input and normal result semantics;
- transactional current published-state semantics;
- provenance exposure at learner runtime boundaries;
- publication-integrity ownership;
- the outbound retrieval-port shape;
- adapter obligations and technical failure separation;
- specification reflection from accepted ADRs;
- independent ADR-to-spec traceability review.

This work item does not own:

- concrete HTTP routes or status codes;
- JSON or other wire schemas;
- retry timing or retry-count policy;
- database tables, columns, indexes, ORM, or SQL;
- learner session state or PWA queue position;
- pipeline provenance internals;
- backend queue state, reservation, or queue history;
- design decisions recorded only in task or work-item evidence.

Workflow rules:

- An adopted design decision must be recorded in an accepted ADR.
- A specification must not change normatively before the authorizing ADR is accepted.
- An accepted ADR must not be rewritten to reverse its decision.
- A replacing ADR must supersede the replaced ADR.
- Tasks record work and evidence only.

## Impact Scope

| ref | impact |
|---|---|
| PRODUCT-ADR-APPLICATION-001 | Historical application boundary decision superseded by PRODUCT-ADR-APPLICATION-003. |
| PRODUCT-ADR-APPLICATION-002 | Historical transactional-publication decision superseded by PRODUCT-ADR-APPLICATION-003. |
| PRODUCT-ADR-APPLICATION-003 | Current retrieval, current-state publication, provenance, and integrity decision. |
| PRODUCT-ADR-APPLICATION-004 | Current outbound retrieval-port and persistence-adapter boundary decision. |
| `spec:product` | Keep the cross-area system flow aligned with current accepted ADRs. |
| PRODUCT-ADR-UI-001 | Preserve PWA ownership of loaded content, queue state, session state, and retry behavior. |
| `spec:product.application` | Route current application behavior and accepted outbound boundaries. |
| `spec:product.application.learning_unit_selection` | Reflect retrieval input and normal result semantics. |
| `spec:product.application.published_content` | Reflect one committed current published state and provenance boundary. |
| `spec:product.learning.learning_unit` | Preserve complete learner-visible content and attribution ownership. |
| `spec:product.pipeline` | Preserve publication validation and transactional write ownership. |
| `spec:product.ui.learning_flow` | Preserve unavailable-reference skipping and loaded-content behavior. |

## Task flow

```text
T01 Establish baseline and identify decision gaps
  |
  v
T02 Record retrieval and current-state decisions in ADR-003
  |
  v
T03 Record the outbound retrieval-port boundary in ADR-004
  |
  v
T04 Reflect accepted ADRs into specifications
  |
  v
T05 Independently review ADR-first traceability and consistency
```

## Task Candidates

| task | responsibility |
|---|---|
| PRODUCT-TASK-APPLICATION-004-01 | Establish the baseline and identify unresolved decisions. |
| PRODUCT-TASK-APPLICATION-004-02 | Record adopted retrieval, publication-state, provenance, and integrity decisions in an accepted ADR. |
| PRODUCT-TASK-APPLICATION-004-03 | Record the result-shaped outbound retrieval port and persistence-adapter obligations in an accepted ADR. |
| PRODUCT-TASK-APPLICATION-004-04 | Reflect accepted ADRs into current specifications without adopting new decisions. |
| PRODUCT-TASK-APPLICATION-004-05 | Independently review decision lineage, specification traceability, and implementation readiness. |

## Completion Condition

- PRODUCT-ADR-APPLICATION-003 remains the current accepted retrieval and published-state decision.
- PRODUCT-ADR-APPLICATION-001 and PRODUCT-ADR-APPLICATION-002 remain superseded historical records.
- PRODUCT-ADR-APPLICATION-004 records the outbound retrieval-port and persistence-adapter boundary.
- Every normative specification change traces to an accepted ADR.
- No task or work-item evidence acts as canonical decision or specification authority.
- Current specifications use `Available` and `Unavailable` for normal retrieval results.
- Current specifications model one committed current published state.
- Current specifications explicitly define `LearningUnitRef`, application use case, outbound retrieval port, persistence adapter, `Available`, and `Unavailable`.
- Pipeline publication validation and writes remain pipeline-owned.
- Provenance does not reach normal PWA retrieval.
- Technical mapping and infrastructure failures remain distinct from normal availability results.
- Concrete persistence and transport choices remain deferred.
- PRODUCT-TASK-APPLICATION-004-05 records a final `PASS` verdict.

## Evidence

### Resolution summary

- PRODUCT-ADR-APPLICATION-003 consolidates the current published-content and retrieval boundary.
- PRODUCT-ADR-APPLICATION-004 defines the result-shaped outbound retrieval port and persistence-adapter obligations.
- PRODUCT-ADR-APPLICATION-001 and PRODUCT-ADR-APPLICATION-002 remain superseded historical records.
- Current application and pipeline specifications reflect the accepted decisions.
- PRODUCT-TASK-APPLICATION-004-05 recorded a final independent `PASS` verdict.

### Completed outcomes

- Normal retrieval uses `Available(complete_learning_unit) | Unavailable`.
- Missing and currently unavailable references map to `Unavailable`.
- Mapping and infrastructure failures remain technical failures.
- The pipeline owns publication validation, availability decisions, and transactional published-content writes.
- The persistence adapter reads committed current content and stored availability through an application-owned port.
- Normal retrieval excludes opaque provenance.
- `LearningUnitRef`, application use case, outbound retrieval port, persistence adapter, current published state, `Available`, and `Unavailable` are explicitly defined.
- UI ownership of queue, loaded content, session, retry, and unavailable-reference skipping remains unchanged.
- Concrete transport, persistence schema, query, and framework choices remain deferred.

### Verification

- All five child tasks are `done`.
- ADR-to-spec traceability was independently reviewed.
- All review findings were closed.
- Strict specification validation reported all 20 files OK.
- `git diff --check` reported no whitespace errors.
- This work item is ready to feed the parent application-design integration flow.
