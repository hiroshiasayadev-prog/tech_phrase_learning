# PRODUCT-TASK-PRODUCT-001-03: Open pipeline detailed-design work

- **id**: PRODUCT-TASK-PRODUCT-001-03
- **status**: done
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PRODUCT-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-PRODUCT-001-02
- **outputs**:
  - PRODUCT-WORK-PIPELINE-001

## Goal

Create one focused work item that decomposes the first-MVP content pipeline into implementation-ready semantic contracts.

## Work

1. Read the T01 baseline and the focused learning work item created by T02.
2. Read all current pipeline ADRs, investigations, fixtures, experiments, and `spec:product.pipeline`.
3. Create the first PIPELINE work item under PRODUCT-REQ-PRODUCT-001.
4. Use a title equivalent to `Define first-MVP content-pipeline contracts`.
5. Add the new work item to PRODUCT-REQ-PRODUCT-001 `work_items`.
6. Record the created work-item ID in this task's `outputs` and Evidence.
7. Give the child work item a task graph that covers:
   - source acquisition and retained-source reuse;
   - authentic post and conversation-tree normalization;
   - deterministic path enumeration;
   - path validation and suitability filtering;
   - reusable post-summary generation;
   - path-specific summary revision;
   - target-phrase selection;
   - three-option quiz generation;
   - mechanical and model-based validation;
   - retry, rejection, and invalid-output handling;
   - stable artifact and learning-unit identity;
   - current provenance ownership;
   - automated publication-gate inputs and outcomes;
   - `PublicationHandoff` and `AvailabilityChange` production;
   - pipeline orchestration and stage dependency order;
   - child specification decomposition under `spec:product.pipeline`;
   - ADR-first resolution, specification reflection, and independent review.
8. Require explicit stage input/output boundaries without selecting concrete source layout or workflow framework.
9. Preserve learning ownership of pedagogical meaning and application ownership of runtime reads.

## Done condition

- One focused PIPELINE work item exists under PRODUCT-REQ-PRODUCT-001.
- The child work item has a complete task graph for pipeline decisions, specifications, and review.
- PRODUCT-REQ-PRODUCT-001 lists the child work item.
- The child scope separates deterministic processing, semantic model tasks, validation, and publication.
- The child scope requires focused child pipeline specifications.
- Concrete implementation technologies remain excluded.
- This task records the child work-item ID in `outputs` and Evidence.

## Verification

- Check the child work item's H1, metadata, source requirement, reciprocal link, and impact refs.
- Confirm the child scope preserves PRODUCT-ADR-PIPELINE-002 and PRODUCT-ADR-PIPELINE-005.
- Confirm learning semantics are consumed rather than redefined.
- Confirm publication outputs match the current published-content boundary.
- Confirm a new session can start the child work item from repository records only.
- Run relevant record validation, `git diff --check`, and `git status --short`.

## Evidence

### Result

- **Verdict**: PASS.
- Created PRODUCT-WORK-PIPELINE-001.
- Created PRODUCT-TASK-PIPELINE-001-01 through PRODUCT-TASK-PIPELINE-001-08.
- Added PRODUCT-WORK-PIPELINE-001 to PRODUCT-REQ-PRODUCT-001.
- Updated PRODUCT-WORK-PRODUCT-001 with the T03 relation and completion evidence.
- No normative ADR or specification changed.

### Boundary

The focused Work Item owns source acquisition, normalization, path processing, content generation, validation, provenance, publication outputs, and orchestration.

The Work Item consumes completed Learning semantics without redefining them.
The Work Item preserves Application runtime-read semantics.
UI behavior and cross-area runtime integration remain excluded.

Concrete languages, frameworks, workflow engines, schemas, databases, routes, deployments, models, prompts, thresholds, and retry timing remain excluded.

### Task graph

```text
T01 authority baseline and exact gaps
  -> T02 source, normalization, identity, and provenance decisions
  -> T03 path enumeration, validation, and filtering
  -> T04 content generation and semantic validation
  -> T05 publication gate and outputs
  -> T06 orchestration, retry, and completion
  -> T07 focused specification reflection
  -> T08 independent review and closure
```

T02 through T06 must create accepted Pipeline ADRs for unsupported normative decisions.
T07 must reflect only accepted authority.
T08 must use an independent reviewer.

### Authority inputs

- PRODUCT-ADR-PIPELINE-002 and PRODUCT-ADR-PIPELINE-005 are current authority.
- PRODUCT-ADR-PIPELINE-001, PRODUCT-ADR-PIPELINE-003, and PRODUCT-ADR-PIPELINE-004 remain superseded history.
- PRODUCT-INV-PIPELINE-001 and PRODUCT-INV-PIPELINE-002 remain evidence only.
- PRODUCT-WORK-LEARNING-001 is the fixed Learning input.
- `spec:product.application.published_content` is the fixed runtime-state input.

### Relation verification

- PRODUCT-REQ-PRODUCT-001 lists PRODUCT-WORK-PIPELINE-001.
- PRODUCT-WORK-PIPELINE-001 references PRODUCT-REQ-PRODUCT-001.
- PRODUCT-WORK-PIPELINE-001 lists eight child tasks.
- Every child task references PRODUCT-WORK-PIPELINE-001 and PRODUCT-REQ-PRODUCT-001.
- Dependencies form one acyclic sequence from T01 through T08.
- H1 IDs, metadata IDs, and file-name prefixes match on filesystem reread.

### Validation evidence

Targeted filesystem listing and reread verified record shape, required sections, relations, dependencies, and exclusions.

The user supplied repository-root CLI results after record creation:

- `git diff --check` reported no whitespace errors;
- strict specification validation returned `[strict]  All 34 file(s) OK.`;
- `git status --short` showed the expected three modified PRODUCT coordination records and the two new Pipeline record directories;
- LF-to-CRLF messages were working-copy conversion warnings and were non-blocking.

The validated change scope contains no normative ADR or specification changes.
The T03 scope is commit-ready.

### Closure

PRODUCT-TASK-PRODUCT-001-03 is complete.
A new session can start PRODUCT-TASK-PIPELINE-001-01 from repository records only.
