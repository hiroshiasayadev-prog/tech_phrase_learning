# PRODUCT-WORK-APPLICATION-001: Coordinate detailed application design

- **id**: PRODUCT-WORK-APPLICATION-001
- **status**: done
- **date**: 2026-06-26
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **impact_refs**: [PRODUCT-ADR-APPLICATION-003, PRODUCT-ADR-APPLICATION-004, spec:product.application, spec:product.application.published_content, spec:product.application.learning_unit_selection, spec:product.pipeline, spec:product.ui.learning_flow, spec:product.ui.pages, spec:product.ui.components, spec:product.ui.components.operation_feedback]
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
- reopening decisions already accepted by PRODUCT-ADR-APPLICATION-003 or PRODUCT-ADR-APPLICATION-004.

The hub tasks must provide enough scope for each focused work item to start without a separate conversation handoff.

## Impact Scope

| ref | impact |
|---|---|
| PRODUCT-ADR-APPLICATION-003 | Preserve the accepted current published-content and retrieval boundary. |
| PRODUCT-ADR-APPLICATION-004 | Preserve the accepted outbound retrieval-port and persistence-adapter boundary. |
| `spec:product.application` | Expand the application topic map as detailed modules become owned. |
| `spec:product.application.published_content` | Refine publication projection, availability, and handoff contracts. |
| `spec:product.application.learning_unit_selection` | Refine queue creation, retrieval, and result semantics. |
| `spec:product.pipeline` | Define the pipeline side of the published-content handoff. |
| `spec:product.ui.learning_flow` | Align application results with PWA skip, retry, and replacement behavior. |
| `spec:product.ui.pages` | Keep page-level terminal transitions aligned with the owning learning-flow contract. |
| `spec:product.ui.components` | Keep component-level failure feedback aligned with application categories and UI transitions. |
| `spec:product.ui.components.operation_feedback` | Distinguish infrastructure retry feedback from non-retryable diagnostic surfaces. |

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

### Result

- **Verdict**: PASS.
- Implementation planning readiness: ready.
- PRODUCT-TASK-APPLICATION-001-01 through PRODUCT-TASK-APPLICATION-001-06 are complete.
- PRODUCT-WORK-APPLICATION-002 through PRODUCT-WORK-APPLICATION-006 are complete.
- Each focused child work item recorded a final independent `PASS`.
- PRODUCT-TASK-APPLICATION-001-06 recorded a final independent integrated `PASS` with no remaining findings.
- PRODUCT-REQ-APPLICATION-001 required outcomes are satisfied at the design level.
- PRODUCT-REQ-APPLICATION-001 remains `accepted`.

### Completed coordination flow

| task | output or responsibility | final status |
|---|---|---|
| PRODUCT-TASK-APPLICATION-001-01 | Open published-content and handoff design as PRODUCT-WORK-APPLICATION-002. | done |
| PRODUCT-TASK-APPLICATION-001-02 | Open complete-shuffle selection design as PRODUCT-WORK-APPLICATION-003. | done |
| PRODUCT-TASK-APPLICATION-001-03 | Open published learning-unit retrieval design as PRODUCT-WORK-APPLICATION-004. | done |
| PRODUCT-TASK-APPLICATION-001-04 | Open outbound query-port design as PRODUCT-WORK-APPLICATION-005. | done |
| PRODUCT-TASK-APPLICATION-001-05 | Open PWA-facing application-interface design as PRODUCT-WORK-APPLICATION-006. | done |
| PRODUCT-TASK-APPLICATION-001-06 | Integrate application, pipeline, learning, and UI contracts and complete independent review. | done |

### Integrated readiness

- Pipeline owns generation, validation, publication decisions, availability decisions, and published-content writes.
- Application reads only committed current published content through application-owned outbound query contracts.
- Persistence adapters depend on application contracts and preserve normal-result versus technical-failure separation.
- Complete-shuffle selection remains bounded to 100 unique currently available references without backend queue or reservation state.
- Retrieval rechecks availability and returns `Available(complete_learning_unit) | Unavailable` as the normal result.
- Provenance remains opaque and excluded from normal learner retrieval.
- PWA-facing failure categories, retryability, safe diagnostics, and `LearningUnitRef` semantics are explicit and transport independent.
- UI owns queue position, loaded content, session state, retry attempts, transitions, disposal, and diagnostic-surface placement.
- UI component and page overviews now match the category-specific failure and terminal-transition authority.
- Concrete frameworks, database schemas, ORM, SQL, HTTP routes, JSON schemas, frontend state libraries, deployment, and source layout remain deferred.

### Independent integration review

- Initial verdict: `NEEDS REVISION` with no blocking finding and three major findings.
- M1 closed: operation feedback restricts automatic and manual retry to `InfrastructureFailure` and separates non-retryable surfaces.
- M2 closed: page overview includes retrieval `MappingFailure` and replacement `Success([])` terminal transitions.
- M3 closed: working-tree, whitespace, strict specification, and scoped-diff validation completed successfully.
- Final re-review verdict: `PASS`.
- Remaining findings: none.
- PRODUCT-ADR-UI-001 stale historical wording and stale ADR wording in child completion Evidence remain non-blocking advisories.

### Validation

- `git status --short` reported only the six expected integration records before closure metadata and final Evidence were added.
- `git diff --check` reported no whitespace error.
- Strict specification validation reported `[strict]  All 34 file(s) OK.`
- Scoped diff inspection confirmed no accepted ADR modification.
- The PRODUCT-REQ-APPLICATION-001 edit was an Evidence-only historical wording correction.
- LF-to-CRLF working-copy warnings were non-blocking line-ending warnings.
- No implementation work item was created and no implementation began.
- No commit or staging operation was performed.

### Implementation work-item candidates

Detailed candidates are recorded in PRODUCT-TASK-APPLICATION-001-06 for:

- application domain and use cases;
- pipeline published-content writer;
- persistence storage model and adapters;
- PWA-facing transport adapter;
- PWA integration;
- architecture and contract tests;
- integration and end-to-end tests.
