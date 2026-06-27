# PRODUCT-TASK-PRODUCT-001-02: Open learning design-completeness work

- **id**: PRODUCT-TASK-PRODUCT-001-02
- **status**: done
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PRODUCT-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-PRODUCT-001-01
- **outputs**:
  - PRODUCT-WORK-LEARNING-001

## Goal

Create one focused work item that verifies learning contracts are complete enough to constrain pipeline and UI implementation planning.

## Work

1. Read the T01 baseline and learning-owned gaps.
2. Read all current learning ADRs, investigations, and specifications.
3. Create the first LEARNING work item under PRODUCT-REQ-PRODUCT-001.
4. Use a title equivalent to `Review first-MVP learning contract completeness`.
5. Add the new work item to PRODUCT-REQ-PRODUCT-001 `work_items`.
6. Record the created work-item ID in this task's `outputs` and Evidence.
7. Give the child work item a task graph that covers:
   - target learner and learning outcome consistency;
   - valid learning-path meaning and suitability criteria;
   - learning-unit required fields and invariants;
   - question and reply interaction composition;
   - target phrase, prompt, option, summary, grounding, and attribution semantics;
   - quiz-session progression and terminal behavior;
   - publication-readiness criteria owned by learning;
   - downstream constraints required by pipeline and UI;
   - ADR-first resolution of missing normative decisions;
   - specification reflection and independent review.
8. Keep processing mechanics, provider choices, runtime selection, and PWA state outside the child work item.

## Done condition

- One focused LEARNING work item exists under PRODUCT-REQ-PRODUCT-001.
- The child work item has a self-contained boundary, task graph, completion conditions, and impact refs.
- PRODUCT-REQ-PRODUCT-001 lists the child work item.
- The child work item distinguishes learning semantics from pipeline mechanics and UI runtime state.
- This task records the child work-item ID in `outputs` and Evidence.

## Verification

- Check the child work item's H1, metadata, source requirement, and reciprocal link.
- Confirm the child work item does not make pipeline or UI implementation choices.
- Confirm unresolved learning judgments require an accepted ADR before specification changes.
- Confirm a new session can start the child work item from repository records only.
- Run relevant record validation, `git diff --check`, and `git status --short`.

## Evidence

### Result

- **Verdict**: PASS.
- Created PRODUCT-WORK-LEARNING-001 with the title `Review first-MVP learning contract completeness`.
- Added PRODUCT-WORK-LEARNING-001 to PRODUCT-REQ-PRODUCT-001 `work_items`.
- Created PRODUCT-TASK-LEARNING-001-01 through PRODUCT-TASK-LEARNING-001-05.
- No normative ADR or specification changed in this task.

### Child work-item boundary

PRODUCT-WORK-LEARNING-001 owns learning-contract completeness for:

- target learner, learning gap, participation model, and learning outcome consistency;
- valid learning-path meaning and suitability;
- complete learning-unit fields, identities, cardinalities, and invariants;
- question-formulation and reply-formulation composition;
- discussion-title, phrase, prompt, option, summary, grounding, and attribution semantics;
- quiz-session progression and terminal behavior;
- learning-owned publication-readiness criteria;
- immutable constraints consumed by pipeline, application, and UI.

The child work item excludes processing mechanics, provider choices, runtime selection, persistence, transport, and PWA state.

### Task graph

| task | responsibility |
|---|---|
| PRODUCT-TASK-LEARNING-001-01 | Establish current authority, completeness gaps, downstream mismatches, and implementation-only exclusions. |
| PRODUCT-TASK-LEARNING-001-02 | Resolve missing normative learning decisions through accepted ADRs and explicit user decisions. |
| PRODUCT-TASK-LEARNING-001-03 | Reconcile learning-model, learning-path, and learning-unit specifications. |
| PRODUCT-TASK-LEARNING-001-04 | Reconcile quiz-session semantics and explicit downstream learning constraints. |
| PRODUCT-TASK-LEARNING-001-05 | Perform an independent integrated review and close the work item. |

### Authority and downstream coverage

- PRODUCT-ADR-LEARNING-001, PRODUCT-ADR-LEARNING-005, and PRODUCT-ADR-LEARNING-006 are current decision inputs.
- Superseded Learning ADRs and PRODUCT-INV-LEARNING-001 remain historical or investigative evidence.
- Missing discussion-title, option-identity, attribution, publication-readiness, or other normative semantics require an accepted Learning ADR before specification reflection.
- Pipeline receives learning-owned production and publication-readiness obligations without generation algorithms.
- Application and UI receive immutable content requirements without runtime selection or PWA-state decisions.

### Reciprocal relation verification

- PRODUCT-REQ-PRODUCT-001 lists PRODUCT-WORK-LEARNING-001.
- PRODUCT-WORK-LEARNING-001 references PRODUCT-REQ-PRODUCT-001.
- PRODUCT-WORK-LEARNING-001 lists five child tasks.
- Every child task references PRODUCT-WORK-LEARNING-001 and PRODUCT-REQ-PRODUCT-001.
- Child-task dependencies form one acyclic sequence from T01 through T05.
- H1 IDs, metadata IDs, file-name prefixes, and domain sequences match on filesystem reread.

### Validation limitation

- Filesystem reread verified the created records, reciprocal relations, required sections, impact refs, and scope exclusions.
- The active filesystem toolset does not execute the repository validator, `git diff --check`, or `git status --short`.
- No CLI validation or working-tree cleanliness claim is made.
- The limitation is explicit and does not change the record-creation done conditions.

### Closure

- One focused LEARNING work item now exists under PRODUCT-REQ-PRODUCT-001.
- A new session can start PRODUCT-TASK-LEARNING-001-01 from repository records only.
- PRODUCT-TASK-PRODUCT-001-02 is complete.
