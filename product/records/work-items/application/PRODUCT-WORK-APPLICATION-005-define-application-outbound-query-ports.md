# PRODUCT-WORK-APPLICATION-005: Define application outbound query ports

- **id**: PRODUCT-WORK-APPLICATION-005
- **status**: not_started
- **date**: 2026-06-26
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **impact_refs**:
  - PRODUCT-ADR-APPLICATION-003
  - PRODUCT-ADR-APPLICATION-004
  - spec:product
  - spec:product.application
  - spec:product.application.learning_unit_selection
  - spec:product.application.published_content
  - spec:product.learning.learning_unit
  - spec:product.pipeline
- **tasks**:
  - PRODUCT-TASK-APPLICATION-005-01
  - PRODUCT-TASK-APPLICATION-005-02
  - PRODUCT-TASK-APPLICATION-005-03
  - PRODUCT-TASK-APPLICATION-005-04
  - PRODUCT-TASK-APPLICATION-005-05

## Goal

Define the application-owned outbound query boundaries required by queue creation and published learning-unit retrieval.

Consolidate ownership, adapter obligations, and verification boundaries without reopening completed selection or retrieval semantics.

## Boundary

This work item owns:

- classification of existing selection and retrieval contracts;
- the application ownership boundary for outbound query operations;
- input and result ownership for each operation;
- persistence-adapter dependency and mapping obligations;
- normal-result and technical-failure separation;
- application-test test doubles;
- persistence-adapter contract-test coverage;
- specification ownership, placement, and focused decomposition;
- ADR-first resolution of any genuine remaining architectural decision;
- independent review and closure.

This work item treats the following contracts as fixed inputs:

- first-MVP `SelectionScope = All`;
- first-MVP `maximum_count = 100`;
- exact `min(maximum_count, eligible_count)` selection cardinality;
- unique stable references in randomized returned order;
- current availability filtering during selection;
- no reservation, backend queue identity, position, or history;
- retrieval input `LearningUnitRef`;
- retrieval result `Available(complete_learning_unit) | Unavailable`;
- retrieval-time availability recheck;
- committed current-state reads;
- technical mapping and infrastructure failures outside normal retrieval results;
- pipeline ownership of availability decisions and published-content writes.

This work item does not own:

- concrete SQL, tables, columns, indexes, or schema design;
- ORM, query-library, database product, or connection-pool selection;
- exact randomization or sampling algorithms;
- transaction configuration or isolation-level selection;
- concrete programming-language interfaces, classes, or method names;
- source directory layout;
- HTTP routes, status codes, JSON schemas, or transport mappings;
- PWA retry timing or learner-flow behavior.

Specification organization must follow these authoring constraints:

- one independently understandable responsibility belongs in one leaf specification;
- multiple related leaf specifications belong under a topic directory with an `index.md` overview;
- an overview routes direct child topics instead of listing every descendant;
- shared rules belong in the nearest common overview instead of being copied into every child;
- each leaf specification must remain small enough to read with its task and parent overview.

Expected topic decomposition, subject to T005-01 verification:

```text
application/
  index.md
  learning-unit-retrieval.md
  published-content/
    index.md
    current-state.md
    availability.md
    publication-handoff.md
  learning-unit-selection/
    index.md
    create-complete-shuffle-queue.md
    selection-scope.md
    queue-contract.md
    result-validation.md
  outbound-queries/
    index.md
    select-learning-unit-refs.md
    get-published-learning-unit.md
```

The decomposition must preserve active semantic refs where an existing topic becomes an `index.md`.

## Impact Scope

| ref | impact |
|---|---|
| PRODUCT-ADR-APPLICATION-003 | Preserve current published-state, retrieval-result, availability, provenance, and integrity decisions. |
| PRODUCT-ADR-APPLICATION-004 | Preserve the accepted result-shaped retrieval port and persistence-adapter obligations. |
| `spec:product` | Keep the system flow aligned with application-owned outbound query boundaries. |
| `spec:product.application` | Route focused application topics and preserve dependency direction. |
| `spec:product.application.learning_unit_selection` | Preserve selection policy while separating use-case and outbound-query responsibilities. |
| `spec:product.application.published_content` | Preserve current-state, availability, provenance, and pipeline-write boundaries during decomposition. |
| `spec:product.learning.learning_unit` | Preserve complete learning-unit meaning and attribution ownership. |
| `spec:product.pipeline` | Preserve pipeline ownership of publication decisions and published-content writes. |

UI specifications are excluded unless T005-01 finds a direct contradiction with an existing UI-owned contract.

## Task flow

```text
T005-01 Establish outbound-port baseline and gap inventory
  |
  v
T005-02 Resolve remaining outbound-port decisions
  |
  v
T005-03 Define adapter and verification obligations
  |
  v
T005-04 Reflect accepted contracts into specifications
  |
  v
T005-05 Independent review and closure
```

- T005-01 classifies every topic before any normative change.
- T005-02 processes only genuine unresolved architectural decisions.
- T005-03 defines adapter and verification obligations under accepted authority.
- T005-04 performs focused specification reflection and decomposition.
- T005-05 independently verifies consistency and implementation readiness.

## Task Candidates

| task | responsibility |
|---|---|
| PRODUCT-TASK-APPLICATION-005-01 | Inventory current contracts and classify duplication, missing reflection, genuine decisions, and deferred implementation details. |
| PRODUCT-TASK-APPLICATION-005-02 | Resolve only genuine remaining decisions through accepted ADRs, or conclude that no new ADR is required. |
| PRODUCT-TASK-APPLICATION-005-03 | Define application inputs, results, adapter obligations, test doubles, and contract-test boundaries. |
| PRODUCT-TASK-APPLICATION-005-04 | Reflect accepted contracts into focused specifications without duplicating selection or retrieval semantics. |
| PRODUCT-TASK-APPLICATION-005-05 | Independently review every impact ref and close the work item after blocking findings are corrected. |

## Completion Condition

- Selection and retrieval remain distinct semantic operations.
- Application ownership of outbound query contracts is explicit.
- Persistence adapters depend on application contracts.
- Application contracts remain independent from persistence and framework types.
- Selection availability, bound, cardinality, uniqueness, and randomized ordering obligations remain intact.
- Retrieval committed-state, availability, mapping, and provenance obligations remain intact.
- Normal outcomes remain distinct from mapping and infrastructure failures.
- Application-test test doubles and persistence-adapter contract tests have explicit boundaries.
- Every normative specification change traces to an accepted ADR.
- No new ADR exists without a genuine unresolved normative decision.
- Specification ownership is focused and navigable through topic overviews.
- Existing semantic refs remain stable when topics move from leaf files to `index.md` files.
- No concrete persistence, transport, framework, or source-layout decision enters the design.
- PRODUCT-TASK-APPLICATION-005-05 records `PASS` with no blocking findings.

## Evidence

TBD
