# PRODUCT-TASK-APPLICATION-005-01: Establish outbound query-port baseline and gap inventory

- **id**: PRODUCT-TASK-APPLICATION-005-01
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-005
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 0.5d
- **depends_on**:
- **outputs**:

## Goal

Establish the authoritative outbound query-port baseline before any decision or specification change.

Classify every candidate gap by its correct owning artifact kind.

## Work

1. Read PRODUCT-ADR-APPLICATION-003 and PRODUCT-ADR-APPLICATION-004 as current decision authority.
2. Treat PRODUCT-ADR-APPLICATION-001 and PRODUCT-ADR-APPLICATION-002 as superseded history only.
3. Read PRODUCT-WORK-APPLICATION-003 and its final review evidence.
4. Read PRODUCT-WORK-APPLICATION-004 and its final review evidence.
5. Read the current application, published-content, learning-unit, and pipeline specifications.
6. Inventory the selection operation, retrieval port, inputs, results, adapter obligations, and failure boundaries.
7. Classify each topic as one of:
   - already decided by an accepted ADR;
   - already specified by WORK-003 or WORK-004;
   - missing specification reflection;
   - genuinely unresolved architectural decision;
   - implementation detail deferred from product design.
8. Identify duplicated contracts and unclear specification ownership.
9. Verify the proposed topic decomposition from PRODUCT-WORK-APPLICATION-005.
10. Preserve existing semantic refs when a current leaf topic may become an `index.md`.
11. Record UI refs only when a direct UI-contract impact exists.
12. Do not modify specifications or create an ADR.

Use concrete runtime situations when explaining each candidate gap.
Do not present abstract alternatives without showing where the behavior occurs.

## Done condition

- Every selection and retrieval concern has one classification.
- Current authority is limited to PRODUCT-ADR-APPLICATION-003 and PRODUCT-ADR-APPLICATION-004.
- Completed selection and retrieval semantics are not reopened.
- Genuine decision gaps are separated from missing specification reflection.
- Deferred implementation details remain explicit.
- Duplicate or misplaced specification content is identified.
- The proposed topic decomposition has a ref-preservation and ownership judgment.
- T005-02 can proceed without another conversation handoff.

## Verification

- Trace every already-decided claim to an accepted ADR.
- Trace every already-specified claim to a current specification.
- Confirm superseded ADRs are not used as current authority.
- Confirm no specification or ADR changed.
- Confirm every proposed normative change is routed to T005-02.
- Confirm physical paths are not used as canonical refs.

## Evidence

### Result

- **Verdict**: PASS.
- Current authority is limited to PRODUCT-ADR-APPLICATION-003 and PRODUCT-ADR-APPLICATION-004.
- PRODUCT-ADR-APPLICATION-001 and PRODUCT-ADR-APPLICATION-002 were treated as superseded history only.
- Selection semantics from PRODUCT-WORK-APPLICATION-003 remain fixed.
- Retrieval semantics from PRODUCT-WORK-APPLICATION-004 remain fixed.
- No genuine unresolved architectural decision was identified.
- No new ADR is required before T005-03.
- No specification changed in this task.

### Reviewed records

- PRODUCT-REQ-APPLICATION-001
- PRODUCT-WORK-APPLICATION-003 and all child tasks
- PRODUCT-WORK-APPLICATION-004 and all child tasks
- PRODUCT-WORK-APPLICATION-005
- PRODUCT-ADR-APPLICATION-003
- PRODUCT-ADR-APPLICATION-004
- `spec:product`
- `spec:product.application`
- `spec:product.application.published_content`
- `spec:product.application.learning_unit_selection`
- `spec:product.learning.learning_unit`
- `spec:product.pipeline`

### Authority map

| concern | authority |
|---|---|
| Current published state, application use cases, availability results, provenance boundary, and technical retrieval failures | PRODUCT-ADR-APPLICATION-003 |
| Result-shaped retrieval port and retrieval persistence-adapter obligations | PRODUCT-ADR-APPLICATION-004 |
| Selection scope, cardinality, uniqueness, ordering, validation, and adapter-owned guarantees | `spec:product.application.learning_unit_selection` as completed by PRODUCT-WORK-APPLICATION-003 |
| Current availability and committed runtime state | `spec:product.application.published_content` |
| Complete learner-visible learning-unit meaning | `spec:product.learning.learning_unit` |
| Availability decisions, validation before publication, and published-content writes | `spec:product.pipeline` |

### Classification

| topic group | classification | evidence and disposition |
|---|---|---|
| Selection input and result | Already specified by WORK-003. | The application supplies `SelectionScope` and `maximum_count`. The operation returns only ordered `LearningUnitRef[]`. |
| Selection availability, maximum, exact cardinality, uniqueness, randomized order, and zero candidates | Already specified by WORK-003. | Preserve the existing contract without redesign. |
| Duplicate, over-limit, or malformed returned references | Already specified by WORK-003. | The application rejects observable invalid results without normalization. |
| Selection outbound-port ownership | Existing contract refinement; not a genuine decision. | `spec:product.application` requires adapters to depend on application contracts. `spec:product.application.learning_unit_selection` already defines the semantic outbound selection operation and persistence-adapter behavior. T005-03 may make this boundary explicit without changing ownership. |
| Selection mapping or infrastructure failure | Existing normal-result boundary refinement; not a genuine decision. | A valid normal result is an ordered reference array, including an empty array. Mapping and infrastructure failures cannot become a valid empty queue or a normalized partial queue. T005-03 must keep them as technical failures without choosing concrete error types. |
| Retrieval input, result, missing content, unavailable content, committed-state read, mapping, technical failures, and provenance | Already decided by ADR-003 and ADR-004 and specified by WORK-004. | Preserve the current retrieval contract. |
| Selection application-test double | Missing focused specification reflection. | T005-03 must define a test double at the application-owned outbound contract boundary. |
| Retrieval application-test double | Decision exists but specification reflection is incomplete. | ADR-004 allows application tests to return the semantic result directly. T005-03 must include this boundary. |
| Selection adapter contract tests | Already specified by WORK-003. | Preserve coverage for candidate counts, availability, scope, uniqueness, valid references, exact cardinality, and randomized order. |
| Retrieval adapter contract tests | Decision exists but specification reflection is incomplete. | ADR-004 requires available, missing, unavailable, mapping-failure, and infrastructure-failure coverage. |
| SQL, schema, ORM, database, algorithm, transaction configuration, interface names, source layout, and transport mappings | Implementation detail. | Keep deferred from PRODUCT design. |

### Specification ownership judgment

The verified decomposition from PRODUCT-WORK-APPLICATION-005 is suitable for T005-04.

- `spec:product.application.learning_unit_selection` remains the selection topic ref.
- `spec:product.application.published_content` remains the published-content topic ref.
- Selection use-case rules remain separate from outbound selection-query rules.
- Retrieval use-case rules remain separate from outbound retrieval-query rules.
- Shared outbound-query dependency, failure, and verification rules belong in `spec:product.application.outbound_queries`.
- Application-side publication-handoff content must describe the runtime boundary only.
- Pipeline writer procedure remains owned by `spec:product.pipeline`.
- Thin child specifications must not be created when a responsibility cannot stand independently.

### Semantic-ref preservation judgment

These physical moves preserve their current canonical refs:

```text
application/published-content.md
  -> application/published-content/index.md
  -> spec:product.application.published_content

application/learning-unit-selection.md
  -> application/learning-unit-selection/index.md
  -> spec:product.application.learning_unit_selection
```

New child files receive new path-derived refs.
Existing semantic refs must not be renamed merely because the files become topic indexes.

### Duplicate or misplaced content

- The current selection spec contains selection policy, selection operation, retrieval behavior, both outbound boundaries, and verification rules.
- The content is not contradictory, but the responsibilities are too concentrated for implementation planning.
- Retrieval-port content belongs under the retrieval and outbound-query topics during T005-04.
- Published-state invariants belong under published content.
- Pipeline mutation procedure remains under pipeline.
- Application-wide dependency direction belongs in the application overview or outbound-query overview, not every leaf.

### Genuine decision candidates

None.

The previously suspected selection-port ownership and selection technical-failure topics do not change accepted ownership, dependency direction, or application policy.
They are implementation-independent contract refinements under the current application specifications.

### Deferred implementation details

- SQL, tables, columns, indexes, query plans, and schema design
- ORM, query library, database product, and connection pool
- Exact randomization and sampling algorithms
- Transaction configuration and isolation level
- Concrete exception and result type names
- Programming-language interfaces, classes, and methods
- Source directories
- HTTP routes, status codes, and JSON schemas
- Retry timing
- Concrete test database, fixtures, and container strategy

### Next-task input

- T005-02 should record that no genuine architectural decision remains and no new ADR is required.
- T005-03 may prepare the selection and retrieval contract map from current authority.
- T005-03 must separate normal outcomes, observable application validation, and adapter-owned technical failures.
- T005-03 must distinguish application tests using outbound-port test doubles from persistence-adapter contract tests.
- T005-04 owns all specification decomposition and reflection.

### Verification

- Every required selection and retrieval concern has one classification.
- Superseded ADRs were not used as current authority.
- Completed selection and retrieval semantics were not reopened.
- No ADR or specification changed.
- Physical paths were used only to explain semantic-ref preservation.
- Blockers: none.
