# PRODUCT-WORK-APPLICATION-001: Coordinate detailed application design

- **id**: PRODUCT-WORK-APPLICATION-001
- **status**: in_progress
- **date**: 2026-06-26
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **impact_refs**: [PRODUCT-ADR-APPLICATION-001, spec:product.application, spec:product.application.published_content, spec:product.application.learning_unit_selection, spec:product.pipeline, spec:product.ui.learning_flow]
- **tasks**: [PRODUCT-TASK-APPLICATION-001-01, PRODUCT-TASK-APPLICATION-001-02, PRODUCT-TASK-APPLICATION-001-03, PRODUCT-TASK-APPLICATION-001-04, PRODUCT-TASK-APPLICATION-001-05, PRODUCT-TASK-APPLICATION-001-06]

## Goal

Coordinate focused design work items for the first-MVP application modules.

Integrate their results into a coherent, implementation-ready application specification set.

## Boundary

This work item owns:

- module-level design decomposition;
- creation of focused child work items under `PRODUCT-REQ-APPLICATION-001`;
- cross-module dependency ordering;
- integration review across application, pipeline, learning, and UI contracts;
- readiness judgment before implementation work is planned.

This work item does not own:

- detailed design inside each focused child work item;
- implementation tasks;
- concrete frameworks, database schemas, SQL, HTTP routes, or deployment choices;
- reopening decisions already accepted by PRODUCT-ADR-APPLICATION-001.

The hub tasks must provide enough scope for each focused work item to start without a separate conversation handoff.

## Impact Scope

| ref | impact |
|---|---|
| PRODUCT-ADR-APPLICATION-001 | Preserve the accepted top-level application architecture. |
| `spec:product.application` | Expand the application topic map as detailed modules become owned. |
| `spec:product.application.published_content` | Refine publication projection, availability, and handoff contracts. |
| `spec:product.application.learning_unit_selection` | Refine queue creation, retrieval, and result semantics. |
| `spec:product.pipeline` | Define the pipeline side of the published-content handoff. |
| `spec:product.ui.learning_flow` | Align application results with PWA skip, retry, and replacement behavior. |

## Task flow

```text
T01 Publication boundary work item
  |
  +--> T02 Queue-selection work item
  |
  +--> T03 Learning-unit retrieval work item
          |
          +--> T04 Outbound ports work item
          |
          +--> T05 PWA-facing interface work item
                    |
                    v
             T06 Integration review
```

- T01 establishes the base published-content and pipeline-handoff design scope.
- T02 and T03 divide selection from complete-unit retrieval.
- T04 defines outbound ports after use-case requirements are explicit.
- T05 defines the PWA-facing application interface after use-case results are explicit.
- T06 starts after the focused module work items have resolved their design scopes.

## Task Candidates

| task | module | hub responsibility |
|---|---|---|
| PRODUCT-TASK-APPLICATION-001-01 | Published-content and pipeline handoff | Create a focused work item with the unresolved boundary questions and required outputs. |
| PRODUCT-TASK-APPLICATION-001-02 | Complete-shuffle selection domain | Create a focused work item for scope, policy, invariants, and bounded selection semantics. |
| PRODUCT-TASK-APPLICATION-001-03 | Published learning-unit retrieval | Create a focused work item for retrieval inputs, results, availability, and content mapping. |
| PRODUCT-TASK-APPLICATION-001-04 | Outbound query ports | Create a focused work item for semantic port operations and adapter obligations. |
| PRODUCT-TASK-APPLICATION-001-05 | PWA-facing application interface | Create a focused work item for transport-independent requests, results, and UI error classification. |
| PRODUCT-TASK-APPLICATION-001-06 | Integrated application design review | Verify child work-item completion, reconcile specifications, and identify implementation work. |

## Completion Condition

- Tasks T01 through T05 have created focused work items under PRODUCT-REQ-APPLICATION-001.
- Each focused work item contains its own task graph, boundaries, completion conditions, and affected refs.
- The focused work items have completed or explicitly deferred every required application design decision.
- T06 confirms consistency across application, pipeline, learning, and UI specifications.
- Any new architectural decisions are recorded in accepted ADRs.
- The current specification set contains no unresolved ownership ambiguity blocking implementation planning.
- Implementation work items are identified but remain outside this hub work item.

## Evidence

TBD
