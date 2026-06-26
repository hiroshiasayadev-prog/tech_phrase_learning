# PRODUCT-TASK-APPLICATION-002-01: Establish publication-boundary design baseline

- **id**: PRODUCT-TASK-APPLICATION-002-01
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-002
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 0.5d
- **depends_on**:
- **outputs**:

## Goal

Establish the accepted publication-boundary contract and the exact unresolved decision set for downstream design tasks.

## Work

1. Read PRODUCT-ADR-APPLICATION-001 and PRODUCT-ADR-PIPELINE-004.
2. Read `spec:product.application.published_content`, `spec:product.pipeline`, and `spec:product.learning.learning_unit`.
3. Classify each required work-item concern as accepted contract, specification gap, architectural decision, or implementation detail.
4. Cover identity, current projection, availability, publication transitions, handoff input, validation preconditions, provenance, ownership, and concurrent reads.
5. Identify contradictions or duplicated ownership across application, pipeline, learning, and UI records.
6. Create an APPLICATION investigation only when repository evidence cannot support a design decision.
7. Record downstream decision inputs and any created investigation in `## Evidence`.

Do not adopt a new architectural decision in this task.

## Done condition

- Every required work-item concern has one explicit classification.
- Accepted contracts and unresolved decisions are distinguishable.
- No persistence, transport, or framework detail is misclassified as a semantic contract.
- Any evidence gap that blocks design has a focused investigation record.
- T02 and T03 can proceed without reconstructing the repository context.

## Verification

- Compare the classified concerns with PRODUCT-WORK-APPLICATION-002 `## Boundary` and `## Completion Condition`.
- Confirm that accepted ADR decisions are not reopened without a new conflict.
- Confirm that unresolved research is not placed in an ADR or specification.
- Confirm that any investigation uses the APPLICATION namespace and references PRODUCT-REQ-APPLICATION-001 where appropriate.

## Evidence

### Result

- **Verdict**: PASS.
- Every required publication-boundary concern has an explicit classification.
- No accepted ADR conflict was found.
- No APPLICATION investigation was created.
- Existing records provide enough context for T02 and T03 to resolve the remaining design choices directly.

### Reviewed records

- PRODUCT-WORK-APPLICATION-002
- PRODUCT-REQ-APPLICATION-001
- PRODUCT-ADR-APPLICATION-001
- PRODUCT-ADR-PIPELINE-004
- `spec:product.application`
- `spec:product.application.published_content`
- `spec:product.pipeline`
- `spec:product.learning.learning_unit`
- `spec:product.ui.learning_flow`

### Concern classification

| concern | classification | accepted baseline | downstream input |
|---|---|---|---|
| Stable identity | `accepted contract` | Stable learning-unit identity is anchored to valid learning-path identity. Generated-content changes preserve identity. A different valid path defines a different learning unit. | T02 must preserve this identity rule in the published projection. |
| Current projection | `specification gap` | Current content is one complete learning unit. Availability is separate. Each publication has one opaque provenance reference. Attribution is required by the learning-unit contract. | T02 must define the exact semantic composition and resolve whether attribution is only part of the complete unit or also a separate projection element. |
| Availability | `accepted contract` | Availability is separate from content. `unavailable` excludes the unit from new queues and normal retrieval while current content remains. | T02 must preserve the independent model and its observable runtime meaning. |
| Publication effects | `accepted contract` | Content replacement atomically changes current content, provenance reference, and publication-judged availability. An availability-only change leaves content and provenance unchanged. | T02 must define projection invariants without pipeline orchestration commands or an exhaustive transition table. |
| Handoff input | `specification gap` | The pipeline owns publication judgment and writes the published area directly. The application does not mediate publication. | T03 must define one semantic input containing identity, complete content, required attribution, provenance reference, and resulting availability. |
| Validation preconditions | `specification gap` | A unit must pass the automated publication gate before becoming session-available. The pipeline owns validation and publication judgment. | T03 must distinguish publication or republication preconditions from a withdrawal decision and require completion before mutation begins. |
| Provenance | `accepted contract` | The application treats provenance as opaque. Current pipeline-owned evidence remains reachable and survives unavailability. | T03 must bind the current opaque reference to the same observable publication state as content and availability. Concrete identity and storage remain implementation details. |
| Ownership | `accepted contract` | The pipeline owns published-area writes. The application owns runtime reads and must not interpret pipeline internals. | T03 and T04 must preserve the split without duplicating the same normative contract across areas. |
| Concurrent reads | `accepted contract` | A read concurrent with replacement observes either the complete previous publication or the complete new publication. | T03 must express the guarantee as observable single-state consistency. Isolation and transaction mechanisms remain implementation details. |
| Persistence, transport, and framework mechanisms | `implementation detail` | Existing records exclude tables, columns, indexes, transaction syntax, commands, events, routes, and wire schemas. | Later implementation design may select mechanisms that satisfy the semantic contracts. |

### Cross-area reconciliation findings

| finding | classification | downstream action |
|---|---|---|
| `spec:product.learning.learning_unit` includes attribution inside the complete learning unit, while `spec:product.application.published_content` also presents attribution beside current content. | Duplicated representation risk; no direct contradiction. | T02 must define one semantic projection shape. T04 must keep attribution meaning owned by learning. |
| Learning, pipeline, and application records each state part of the unavailable-content rule. | Duplicated ownership risk; no direct contradiction. | T04 must keep learning eligibility semantics, pipeline decision and write obligations, and application runtime state distinct. |
| Application published-content and UI learning-flow records both state loaded-unit immutability. | Duplicated ownership risk; no direct contradiction. | T04 must keep loaded PWA state owned by UI and retain only the publication boundary effect in application. |

### Downstream decision inputs

T02 must resolve:

- the exact current-projection composition;
- content and availability independence;
- the observable meaning of `unavailable`;
- replacement and availability-only invariants.

T03 must resolve:

- the semantic publication-handoff input;
- validation and publication-judgment preconditions;
- pipeline writer obligations for publication, withdrawal, and republication;
- the atomic visibility and concurrent-read guarantee;
- provenance-reference binding and reachability.

A new ADR is required when T02 or T03 adopts an architectural choice not already accepted by PRODUCT-ADR-APPLICATION-001 or PRODUCT-ADR-PIPELINE-004.

### Verification

- The classifications cover every concern in PRODUCT-WORK-APPLICATION-002 `## Boundary`.
- The downstream inputs cover the work-item `## Completion Condition` without selecting persistence or transport technology.
- Accepted ADR decisions remain closed.
- Unresolved choices are not written as current specification text.
- No missing external evidence blocks T02 or T03.
