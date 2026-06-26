# PRODUCT-TASK-APPLICATION-003-01: Establish complete-shuffle design baseline

- **id**: PRODUCT-TASK-APPLICATION-003-01
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-003
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 0.5d
- **depends_on**:
- **outputs**:

## Goal

Establish the accepted complete-shuffle contract and the exact unresolved decision set for downstream design tasks.

## Work

1. Read PRODUCT-ADR-APPLICATION-001 and PRODUCT-ADR-UI-001.
2. Read `spec:product.application`, `spec:product.application.learning_unit_selection`, and `spec:product.application.published_content`.
3. Read `spec:product.ui.learning_flow` for transient queue-state ownership.
4. Classify every concern in PRODUCT-WORK-APPLICATION-003 as accepted contract, specification gap, architectural decision, or implementation detail.
5. Cover scope meaning, maximum count, uniqueness, later repetition, fewer-than-maximum behavior, reservation, queue history, bounded random selection, adapter obligations, validation, and future scopes.
6. Identify contradictions or duplicated ownership across application and UI records.
7. Create an APPLICATION investigation only when repository evidence cannot support a required design decision.
8. Record downstream decision inputs and any created investigation in `## Evidence`.

Do not adopt a new architectural decision in this task.

## Done condition

- Every required work-item concern has one explicit classification.
- Accepted contracts and unresolved decisions are distinguishable.
- Database-side bounded selection is identified as an accepted constraint.
- Domain-owned invariants remain separate from adapter implementation details.
- PWA queue state remains separate from backend selection policy.
- Any evidence gap that blocks design has a focused investigation record.
- T02 and T03 can proceed without reconstructing repository context.

## Verification

- Compare the classified concerns with PRODUCT-WORK-APPLICATION-003 `## Boundary` and `## Completion Condition`.
- Confirm that accepted ADR decisions are not reopened without a new conflict.
- Confirm that `all` does not imply returning every eligible reference in one queue.
- Confirm that exact algorithms, SQL, indexes, and transport schemas remain implementation details.
- Confirm that unresolved research is not placed in an ADR or specification.

## Evidence

### Result

- **Verdict**: PASS.
- Every required complete-shuffle concern has an explicit classification.
- No accepted ADR conflict was found.
- No APPLICATION investigation was created.
- Existing records provide enough evidence for T02 and T03.
- No unresolved concern is automatically an architectural decision.
- T02 or T03 requires a new ADR only when the adopted result changes an accepted ownership, dependency, or policy decision.

### Reviewed records

- PRODUCT-WORK-APPLICATION-003
- PRODUCT-REQ-APPLICATION-001
- PRODUCT-ADR-APPLICATION-001
- PRODUCT-ADR-UI-001
- `spec:product.application`
- `spec:product.application.learning_unit_selection`
- `spec:product.application.published_content`
- `spec:product.ui.learning_flow`

### Concern classification

| concern | classification | accepted baseline | downstream input |
|---|---|---|---|
| `SelectionScope` meaning | `specification gap` | Selection scope defines the eligible candidate set. The first MVP accepts only `all`. | T02 must define the implementation-independent scope value, validity rules, and extension boundary. |
| First-MVP `all` scope | `accepted contract` | Every currently available unit is eligible. `all` does not require every eligible reference in one queue. | T02 must preserve unrestricted eligibility without full-corpus queue materialization. |
| Maximum count | `accepted contract` | One queue contains at most 100 references. The limit is application policy. | T02 must express the bound as a domain invariant. T03 may pass the policy value into the selection operation. |
| Fewer-than-maximum behavior | `specification gap` | Fewer than 100 eligible units may produce a smaller valid queue. | T02 must define exact cardinality expectations, including the zero-eligible case and adapter underfill. |
| Within-queue uniqueness | `accepted contract` | One queue contains no duplicate learning-unit reference. | T02 must preserve uniqueness as a domain invariant. |
| Later repetition | `accepted contract` | A later queue may repeat a reference from an earlier queue. | T02 must keep uniqueness local to one queue request. |
| Randomized ordering | `accepted contract` | Queue order is randomized by the selection implementation. | T02 must define only the semantic ordering requirement. Statistical guarantees remain outside the current contract. |
| Reservation | `accepted contract` | Queue issuance creates no learner-specific reservation. | T02 must preserve current availability as request-time eligibility only. |
| Backend queue identity, position, and history | `accepted contract` | The application retains no queue identity, position, progress, or history. The PWA owns transient queue position. | T02 must keep all backend queue-state concepts excluded. |
| Selection-time availability | `accepted contract` | Queue creation uses availability observed during that request. Later retrieval rechecks availability independently. | T03 must state that later withdrawal does not invalidate the earlier selection result retroactively. |
| Bounded-selection architecture | `accepted contract` | The database adapter may perform bounded random selection without loading every candidate into the domain layer. | T03 must preserve database-side execution and adapter-independent invariants. |
| Semantic bounded-selection operation | `specification gap` | The operation accepts scope and a maximum count, then returns ordered references. | T03 must define exact transport-independent inputs, outputs, and failure boundaries without choosing a port name. |
| Adapter obligations | `accepted contract` | The adapter must enforce availability, scope, maximum count, uniqueness, and randomized ordering. | T03 must trace each obligation to one domain invariant. |
| Result validation and invalid-result handling | `specification gap` | Empty or smaller valid results must remain distinct from adapter contract violations. | T03 must assign validation ownership and decide rejection or normalization for duplicate, over-limit, out-of-scope, malformed, and otherwise invalid results. |
| Future non-history scopes | `specification gap` | Source, topic, discussion, and difficulty scopes may extend selection without moving queue state to the backend. | T02 must define whether scopes are exclusive variants or composable constraints. |
| Learner-history scope | `accepted contract` | Learner-history selection requires a separate durable identity and progress decision. | T02 must keep learner history outside the first-MVP scope model. |
| Exact algorithms and infrastructure | `implementation detail` | Exact sampling, SQL, indexes, query plans, transport schemas, and framework types are excluded. | Later implementation design may choose mechanisms that satisfy the semantic contract. |

### Cross-area reconciliation findings

| finding | classification | downstream action |
|---|---|---|
| Application selection and published-content records both mention current availability. | Duplicated ownership risk; no contradiction. | T04 must keep availability meaning in `spec:product.application.published_content` and selection eligibility in `spec:product.application.learning_unit_selection`. |
| Application and UI records both mention queue exhaustion and acquiring another queue. | Boundary overlap; no contradiction. | T04 must keep queue-production capability in application and the exhaustion transition in UI. |
| Application and UI records both mention unavailable queued references. | Boundary overlap; no contradiction. | T04 must keep `Unavailable` result semantics in application and pending-reference removal in UI. |
| PRODUCT-ADR-APPLICATION-001 and PRODUCT-ADR-UI-001 both state PWA queue-state ownership. | Reinforcing decision; no contradiction. | No ownership change is required. |

### Downstream decision inputs

T02 must resolve:

- the exact semantic shape and validity rules of `SelectionScope`;
- the first-MVP `all` value;
- exact queue cardinality for zero, fewer-than-maximum, and at-least-maximum eligible counts;
- within-queue uniqueness and cross-queue repetition;
- randomized ordering without an algorithm contract;
- the absence of reservation and backend queue state;
- future non-history scope composition;
- the ADR requirement judgment.

T03 must resolve:

- one semantic bounded-selection operation;
- scope and maximum-count inputs;
- adapter obligations for availability, scope, count, uniqueness, and ordering;
- validation ownership for every returned-result invariant;
- rejection or normalization for each invalid-result class;
- a transport-independent invalid-result outcome;
- empty and smaller valid result handling;
- selection-time availability versus later retrieval-time withdrawal;
- the ADR requirement judgment.

### Verification

- The classifications cover every concern in PRODUCT-WORK-APPLICATION-003 `## Boundary`.
- The downstream inputs cover the work-item `## Completion Condition` without choosing persistence or transport technology.
- Database-side bounded selection remains an accepted constraint.
- Domain invariants remain separate from adapter implementation details.
- PWA queue state remains separate from backend selection policy.
- Accepted ADR decisions remain closed.
- No missing external evidence blocks T02 or T03.
