# PRODUCT-WORK-PRODUCT-001: Coordinate first-MVP design completion

- **id**: PRODUCT-WORK-PRODUCT-001
- **status**: in_progress
- **date**: 2026-06-27
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **impact_refs**:
  - spec:product
  - spec:product.learning
  - spec:product.pipeline
  - PRODUCT-WORK-PIPELINE-001
  - spec:product.application
  - spec:product.ui
  - PRODUCT-WORK-APPLICATION-001
- **tasks**:
  - PRODUCT-TASK-PRODUCT-001-01
  - PRODUCT-TASK-PRODUCT-001-02
  - PRODUCT-TASK-PRODUCT-001-03
  - PRODUCT-TASK-PRODUCT-001-04
  - PRODUCT-TASK-PRODUCT-001-05
  - PRODUCT-TASK-PRODUCT-001-06

## Goal

Coordinate the remaining first-MVP design work and establish one independently reviewed implementation-planning baseline.

Use completed application design as an input while opening focused work for learning, pipeline, UI, and cross-area runtime integration.

## Boundary

This work item owns:

- current design-readiness inventory across all first-MVP areas;
- focused child work-item creation and dependency ordering;
- routing each normative gap to its semantic owner;
- coordination of learning, pipeline, UI, and runtime integration design;
- final cross-area consistency and implementation-planning review.

This work item does not own:

- normative learning, pipeline, application, or UI contracts;
- design decisions without an accepted ADR;
- implementation tasks or implementation progress;
- concrete technology, deployment, schema, route, or source-layout choices;
- silent reopening of completed application contracts.

## Impact Scope

| ref | impact |
|---|---|
| `spec:product` | Preserve area ownership and dependency direction during remaining design work. |
| `spec:product.learning` | Verify learner-facing contracts are complete enough to constrain pipeline and UI design. |
| `spec:product.pipeline` | Decompose the current overview into focused stage and publication contracts. |
| PRODUCT-WORK-PIPELINE-001 | Track the focused Pipeline decision, specification, and review flow opened by T03. |
| `spec:product.application` | Treat completed application design as a fixed integration input. |
| `spec:product.ui` | Verify whole-area flow, state, page, and feedback consistency. |
| PRODUCT-WORK-APPLICATION-001 | Reuse the completed application integration evidence and implementation candidates. |

## Task flow

```text
T01 Establish remaining-design baseline and ownership split
  |
  v
T02 Open learning design-completeness work
  |
  +--------------------+
  |                    |
  v                    v
T03 Open pipeline       T04 Open UI
    detailed design         detailed design
  |                    |
  +----------+---------+
             |
             v
T05 Open cross-area runtime integration design
             |
             v
T06 Integrate and independently review first-MVP design
```

- T01 inventories current readiness and defines child ownership boundaries.
- T02 opens focused learning completeness work before downstream design is finalized.
- T03 opens detailed pipeline design using learning contracts as constraints.
- T04 opens whole-area UI design using learning and application contracts as constraints.
- T05 opens runtime integration design after pipeline, application, and UI boundaries are explicit.
- T06 starts only after every focused child work item is complete or explicitly deferred without blocking readiness.

## Task Candidates

| task | responsibility |
|---|---|
| PRODUCT-TASK-PRODUCT-001-01 | Establish the current first-MVP design baseline, gap inventory, and child ownership split. |
| PRODUCT-TASK-PRODUCT-001-02 | Create focused learning design-completeness work. |
| PRODUCT-TASK-PRODUCT-001-03 | Create focused pipeline detailed-design work. |
| PRODUCT-TASK-PRODUCT-001-04 | Create focused UI detailed-design work. |
| PRODUCT-TASK-PRODUCT-001-05 | Create focused cross-area runtime integration design work. |
| PRODUCT-TASK-PRODUCT-001-06 | Integrate results, identify implementation work, and obtain independent final review. |

## Completion Condition

- The current design baseline and ownership gaps are recorded.
- Focused child work items exist for learning, pipeline, UI, and cross-area runtime integration.
- Every child work item is complete or explicitly deferred without blocking implementation planning.
- Normative changes trace to accepted ADRs and current owner specifications.
- Application design remains consistent with downstream and upstream contracts.
- No unresolved ownership, result-semantic, state-transition, publication, or integration gap blocks implementation planning.
- Implementation candidates are recorded without starting implementation.
- Strict validation, working-tree inspection, and independent cross-area review complete successfully.

## Evidence

### T01 baseline

PRODUCT-TASK-PRODUCT-001-01 records the coordination inventory used by this work item.

| area | current judgment | child route |
|---|---|---|
| Learning | Core semantics exist, but whole-area implementation-planning completeness is unreviewed. | T02 opens focused Learning work. |
| Pipeline | Broad current contracts exist in one overview. Detailed stage, artifact, validation, identity, provenance, publication, and orchestration contracts are incomplete. | T03 opens focused Pipeline work. |
| Application | Detailed design is complete with independent integrated `PASS`. | Reuse PRODUCT-WORK-APPLICATION-001 as a fixed input. |
| UI | Normal and failure-transition contracts exist. Whole-area empty-state, recovery, accessibility, and consistency review remains. | T04 opens focused UI work. |
| Runtime integration | Owner contracts exist, but writer, persistence, transport, PWA, and test obligations lack one coordinated boundary. | T05 opens focused PRODUCT integration work. |

The dependency order remains T02, then parallel T03 and T04, then T05, then T06.

No ownerless normative gap blocks child work-item creation.
Normative corrections must remain in owner ADRs and specifications.
Persistence and transport remain adapter concerns rather than new semantic specification areas.

The active Design Records MCP index does not cover this repository and is not used as validation authority.

T01 local verification completed:

- strict specification validation passed all 34 specification files;
- `git diff --check` reported no whitespace error;
- `git status --short` reported only the expected T01 task and parent work-item changes;
- scoped diff inspection showed coordination status and Evidence changes only;
- LF-to-CRLF warnings were non-blocking.

PRODUCT-TASK-PRODUCT-001-01 is complete.
PRODUCT-WORK-PRODUCT-001 remains `in_progress` for T02 through T06.

### T03 Pipeline work opening

PRODUCT-TASK-PRODUCT-001-03 created PRODUCT-WORK-PIPELINE-001.

The focused Pipeline Work Item contains PRODUCT-TASK-PIPELINE-001-01 through PRODUCT-TASK-PIPELINE-001-08.
The task graph covers authority baseline, source and normalization decisions, path contracts, generation, publication, orchestration, specification reflection, and independent review.

The Work Item consumes the completed PRODUCT-WORK-LEARNING-001 contract without reopening Learning meaning.
The Work Item preserves the Application published-content read boundary.
Pipeline ownership remains limited to generation, validation, publication decisions, writes, and internal provenance.

PRODUCT-ADR-PIPELINE-002 and PRODUCT-ADR-PIPELINE-005 are current Pipeline decision inputs.
Superseded Pipeline ADRs remain historical records.
PRODUCT-INV-PIPELINE-001 and PRODUCT-INV-PIPELINE-002 remain evidence only.

PRODUCT-REQ-PRODUCT-001 lists PRODUCT-WORK-PIPELINE-001.
PRODUCT-WORK-PIPELINE-001 lists all eight child tasks.
Every child task references PRODUCT-WORK-PIPELINE-001 and PRODUCT-REQ-PRODUCT-001.

T03 changed no normative ADR or specification.
T04 through T06 remain unstarted.

Filesystem reread verified record identity, parent relations, task dependencies, required sections, and reciprocal links.

The user supplied repository-root CLI results after T03 record creation:

- `git diff --check` reported no whitespace errors;
- strict specification validation returned `[strict]  All 34 file(s) OK.`;
- `git status --short` showed the expected three modified PRODUCT coordination records and the new Pipeline Work Item and Task directories;
- LF-to-CRLF messages were non-blocking working-copy conversion warnings.

The T03 opening scope is commit-ready.
