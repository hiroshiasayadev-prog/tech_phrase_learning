# PRODUCT-TASK-PRODUCT-001-01: Establish first-MVP design baseline and gap inventory

- **id**: PRODUCT-TASK-PRODUCT-001-01
- **status**: done
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PRODUCT-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 2d
- **depends_on**: []
- **outputs**:
  - PRODUCT-WORK-PRODUCT-001

## Goal

Establish the current first-MVP design-readiness baseline and route each remaining gap to one semantic owner.

## Work

1. Read `spec:product` and every top-level area overview.
2. Read current accepted ADRs for learning, pipeline, application, and UI.
3. Read PRODUCT-WORK-APPLICATION-001 and its final integration evidence.
4. Inventory existing requirements, work items, tasks, investigations, and child specifications by area.
5. Classify each remaining concern as:
   - resolved current contract;
   - missing normative decision;
   - missing specification detail;
   - missing completeness review;
   - implementation-only choice;
   - cross-area integration gap.
6. Assign one semantic owner to every normative gap.
7. Identify dependency order among learning, pipeline, UI, and runtime integration work.
8. Record the child work-item scope needed by T02 through T05.
9. Stop as `blocked` when a gap has no clear owner or requires a user decision before work-item creation.
10. Do not change normative specifications in this task.

Required inventory coverage:

- learning model, path, learning-unit, and quiz-session completeness;
- pipeline stages, intermediate artifacts, validation, retries, identity, provenance, publication, and orchestration;
- UI flow, pages, component responsibilities, terminal states, reload, and empty states;
- pipeline writer to published-content boundary;
- application outbound reader and PWA-facing interface;
- persistence and transport adapter ownership;
- cross-area tests and end-to-end acceptance boundaries.

## Done condition

- Every current first-MVP area has a recorded readiness judgment.
- Each remaining normative gap has one owner or an explicit blocking reason.
- Implementation-only choices are separated from semantic design gaps.
- Child work-item scopes for T02 through T05 are self-contained.
- Dependency order is explicit.
- No normative specification is changed.

## Verification

- Check the inventory against `spec:product` dependency direction.
- Confirm application design is treated as completed input rather than silently reopened.
- Confirm every proposed normative change names an accepted ADR or a missing-ADR follow-up.
- Confirm persistence and transport concerns do not become a new semantic spec area without a decision.
- Validate H1, metadata, canonical refs, reciprocal workflow links, and required sections.
- Run `git diff --check` and inspect `git status --short` before marking done.

## Evidence

### Baseline result

- **Verdict**: READY FOR CHILD-WORK CREATION.
- No ownerless normative gap blocks T02 through T05.
- Application design is a completed input and must not be reopened without an accepted-authority conflict.
- No normative specification changed during this task.
- Detailed gaps route to learning, pipeline, UI, or cross-area integration work.

### Artifact inventory

| area | specifications | current decision records | execution records | inventory judgment |
|---|---|---|---|---|
| Learning | Four child specifications: learning model, learning path, learning unit, and quiz session. | Three accepted ADRs, three superseded ADRs, and one concluded investigation. | No learning requirement, work item, or task exists. | Core semantics exist, but no focused implementation-planning completeness review exists. |
| Pipeline | No child specification exists below `spec:product.pipeline`. | Two accepted ADRs, three superseded ADRs, and two concluded investigations. | No pipeline requirement, work item, or task exists. | The overview contains broad contracts, but detailed stage contracts are not implementation-planning ready. |
| Application | Sixteen child specifications cover publication, selection, retrieval, outbound queries, and the PWA interface. | Four current accepted ADRs supersede or extend two historical ADRs. | Three requirements, six work items, and thirty-one tasks exist. PRODUCT-WORK-APPLICATION-001 records final integrated `PASS`. | Complete and fixed as an integration input. |
| UI | Nine child specifications cover learning flow, pages, and components. | Two accepted ADRs exist. | One requirement, one work item, and two tasks are complete. | Failure transitions are complete, but whole-area readiness has not been reviewed. |
| PRODUCT coordination | `spec:product` defines ownership and dependency direction. | No PRODUCT ADR is required for current coordination. | PRODUCT-REQ-PRODUCT-001, PRODUCT-WORK-PRODUCT-001, and six hub tasks exist. | Coordination scope is established. |

### Readiness judgment

| area | readiness | basis |
|---|---|---|
| Learning | Focused review required. | Learner, path, unit, and session semantics are substantial. Runtime-required content completeness has not received an independent whole-area review. |
| Pipeline | Detailed design required. | Stage boundaries, artifacts, validation, retries, identities, provenance, publication gating, and orchestration remain concentrated in one overview. |
| Application | Ready. | PRODUCT-WORK-APPLICATION-001 and every focused child work item are done with independent `PASS`. |
| UI | Focused review required. | Normal flow and category-specific failure transitions exist. Empty-state, recovery, accessibility, and whole-area consistency still require review. |
| Runtime integration | Focused design required. | Owner contracts exist, but writer, persistence, transport, PWA, and cross-boundary test obligations are not coordinated in one work item. |

### Resolved current contracts

- Learning owns learner-visible meaning, path suitability, learning-unit semantics, and quiz progression.
- Pipeline owns source processing, generation, validation, publication decisions, availability decisions, and published-content writes.
- Application owns complete-shuffle selection, availability-aware retrieval, outbound query ports, PWA-facing results, failure categories, and `LearningUnitRef` semantics.
- UI owns queue state, loaded-unit state, session state, loading, retry attempts, navigation, disposal, and failure-surface placement.
- The pipeline writes one committed current published state.
- The application reads only committed current published content.
- Persistence and transport remain adapters, not new semantic specification areas.

### Remaining gap inventory

| id | concern | classification | semantic owner | authority or follow-up | route |
|---|---|---|---|---|---|
| L-01 | Whole learning-area implementation-planning completeness has not been reviewed. | Missing completeness review. | Learning. | Use current learning ADRs and specifications. | T02 child work item. |
| L-02 | The complete learning unit does not explicitly reconcile every runtime-required learner-visible element. The UI requires a discussion title and selected option identifiers, while the learning-unit contract does not define their semantics. Attribution is required, but its minimum composition remains broad. | Missing specification detail. | Learning. | Use PRODUCT-ADR-LEARNING-005, PRODUCT-ADR-LEARNING-006, and current UI consumers. Create a Learning ADR before adding semantics not entailed by accepted authority. | T02 child work item. |
| L-03 | Learning-owned publication-readiness criteria require a completeness check against downstream pipeline validation. | Missing completeness review. | Learning. | `spec:product.learning.learning_unit` provides the current criteria. Add an ADR only for a new criterion or changed meaning. | T02 child work item. |
| P-01 | The pipeline has no focused child specification decomposition. | Missing specification detail. | Pipeline. | PRODUCT-ADR-PIPELINE-005 and PRODUCT-ADR-PIPELINE-002 provide the current direction. | T03 child work item. |
| P-02 | Source acquisition, retained-source reuse, authored-text derivation, relationship preservation, coarse projection, path enumeration, and stage input/output contracts are not defined as focused current contracts. | Missing normative decision and specification detail. | Pipeline. | Investigation evidence is non-normative. Create Pipeline ADRs for unresolved projection, identity, or lifecycle decisions before specification reflection. | T03 child work item. |
| P-03 | Mechanical validation, model-output validation, retry, rejection, invalid-output handling, and publication-gate result rules are not complete enough for implementation planning. | Missing normative decision and specification detail. | Pipeline. | PRODUCT-ADR-PIPELINE-005 authorizes staged validation and retry-or-reject behavior at a high level. New policy choices require Pipeline ADRs. | T03 child work item. |
| P-04 | Stable source, post, path, generated-artifact, and learning-unit identities require one coherent contract. Current provenance ownership and the opaque publication reference also require focused definition. | Missing normative decision and specification detail. | Pipeline, constrained by Learning and Application identities. | PRODUCT-ADR-LEARNING-005, PRODUCT-ADR-PIPELINE-005, and PRODUCT-ADR-APPLICATION-003 provide partial authority. New identity semantics require a Pipeline ADR. | T03 child work item. |
| P-05 | Pipeline stage dependency order, failure propagation, restart boundary, and publication orchestration are not defined. | Missing normative decision and specification detail. | Pipeline. | Create Pipeline ADRs for choices that alter observable semantics. Keep workflow-framework selection in implementation. | T03 child work item. |
| U-01 | The whole UI area has not received an implementation-planning completeness review. | Missing completeness review. | UI. | Use PRODUCT-ADR-UI-001, PRODUCT-ADR-UI-002, and current learning and application contracts. | T04 child work item. |
| U-02 | The recovery action after an initial `MappingFailure` or `InvalidSelectionResult` is explicitly undefined by current accepted authority. | Missing normative decision. | UI. | A new UI ADR is required before changing the owning specification. | T04 child work item. |
| U-03 | The empty-queue screen exists in the learning-flow contract but lacks a focused page composition contract. Accessibility-relevant focus, announcement, and disabled-action behavior also lack a whole-area judgment. | Missing specification detail and possible normative decision. | UI. | Reflect existing authority where sufficient. Create a UI ADR for new behavioral obligations. | T04 child work item. |
| I-01 | Pipeline writer, persistence adapter, application use cases, transport adapter, and PWA consumption require one cross-area mapping and verification boundary. | Cross-area integration gap. | PRODUCT coordination, with normative corrections routed to each owner area. | Current accepted ADRs and owner specifications remain authoritative. | T05 child work item. |
| I-02 | Contract-test ownership and end-to-end acceptance from publication through learner-visible transitions are not coordinated. | Cross-area integration gap. | PRODUCT coordination. | Tests verify owner contracts and must not create new semantics. | T05 child work item. |

### Implementation-only choices

The following choices do not block semantic design completion:

- database engine, ORM, tables, columns, indexes, SQL, and transaction syntax;
- transport protocol, route paths, status codes, JSON shape, and serialization library;
- concrete `LearningUnitRef` wire representation;
- frontend framework, state library, routing library, component files, styling, and animation;
- exact randomization algorithm within the accepted selection contract;
- source layout, package layout, deployment, and process topology;
- concrete model names, provider assignment, prompt wording, and provider SDKs;
- retry delay, backoff, timeout, and operational logging implementation.

A concrete choice becomes design work only when it changes an accepted semantic contract.

### Dependency order

```text
T01 baseline
  |
  v
T02 learning completeness
  |
  +--------------------+
  |                    |
  v                    v
T03 pipeline design    T04 UI design
  |                    |
  +----------+---------+
             |
             v
T05 runtime integration
             |
             v
T06 final integration and review
```

- Learning completes first because pipeline and UI consume learning-owned semantics.
- Pipeline and UI may proceed in parallel after the learning boundary is explicit.
- Application remains a completed input throughout T02 through T05.
- Runtime integration starts after pipeline and UI owner contracts are explicit.

### Child work-item scope required by T02 through T05

| task | required child scope | specific T01 additions |
|---|---|---|
| T02 | Review first-MVP learning contract completeness. | Reconcile discussion title, option identity, attribution minimums, publication-readiness criteria, and downstream completeness. |
| T03 | Define first-MVP content-pipeline contracts. | Decompose child specs and resolve source projection, stage I/O, validation, retry, identity, provenance, publication, and orchestration gaps. |
| T04 | Define first-MVP learner UI contracts. | Resolve initial non-retryable recovery authority, empty-queue page composition, accessibility-relevant behavior, and whole-area state consistency. |
| T05 | Define first-MVP runtime integration boundaries. | Coordinate writer, persistence, application, transport, PWA, contract-test, and end-to-end obligations without creating persistence or transport semantic areas. |

The existing T02 through T05 task records are self-contained enough to create these child work items.
Each task must treat this baseline as scope input rather than normative authority.

### Workflow and authority verification

- PRODUCT-REQ-PRODUCT-001 reciprocally lists PRODUCT-WORK-PRODUCT-001.
- PRODUCT-WORK-PRODUCT-001 lists PRODUCT-TASK-PRODUCT-001-01 through PRODUCT-TASK-PRODUCT-001-06.
- Every PRODUCT hub task references PRODUCT-WORK-PRODUCT-001 and PRODUCT-REQ-PRODUCT-001.
- Current specification refs follow `spec:product` dependency direction.
- Every proposed normative correction names accepted authority or an explicit missing-ADR follow-up.
- Persistence and transport remain implementation adapters.
- No new semantic area is proposed.

### Validation

- Design Records MCP validation was attempted.
- The active MCP index returned diagnostics for Brewprint, DRMCP, and V01 records outside this repository.
- The active MCP index did not validate the Tech Phrase Learning PRODUCT records.
- Those diagnostics are unrelated existing diagnostics and are not current-scope validation authority.
- Strict specification validation reported `[strict]  All 34 file(s) OK.`
- `git diff --check` reported no whitespace error.
- `git status --short` reported only this task and PRODUCT-WORK-PRODUCT-001 as modified.
- Scoped diff inspection confirmed that only coordination status and Evidence changed.
- LF-to-CRLF warnings are non-blocking working-copy line-ending warnings.
- No normative specification, ADR, implementation file, commit, or staging state changed.

### Closure

- Every first-MVP area has a readiness judgment.
- Every remaining normative gap has one semantic owner or an explicit ADR-first follow-up.
- Implementation-only choices are separated from semantic design gaps.
- T02 through T05 have self-contained scope input.
- Dependency order is explicit.
- PRODUCT-TASK-PRODUCT-001-01 is complete.
