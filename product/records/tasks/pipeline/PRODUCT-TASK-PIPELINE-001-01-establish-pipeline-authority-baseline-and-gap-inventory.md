# PRODUCT-TASK-PIPELINE-001-01: Establish Pipeline authority baseline and exact gap inventory

- **id**: PRODUCT-TASK-PIPELINE-001-01
- **status**: not_started
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PIPELINE-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 1.5d
- **depends_on**: []
- **outputs**:
  - PRODUCT-WORK-PIPELINE-001

## Goal

Establish the exact current Pipeline authority, unresolved decisions, specification gaps, evidence inputs, and focused child-specification plan.

## Work

1. Read current Pipeline ADRs and distinguish accepted authority from superseded history.
2. Read PRODUCT-INV-PIPELINE-001, PRODUCT-INV-PIPELINE-002, fixtures, and experiment scripts as evidence.
3. Read `spec:product.pipeline`, the completed Learning specifications, and Application published-content contracts.
4. Inventory current Pipeline contracts for:
   - source acquisition and retained-source reuse;
   - authentic-post normalization and relationship preservation;
   - path enumeration, structural validation, and suitability filtering;
   - summary, phrase, prompt, and quiz generation;
   - mechanical and semantic validation;
   - retry, rejection, and incomplete output;
   - artifact identity, generated-content versioning, and provenance;
   - publication gating, handoff, availability change, and withdrawal;
   - orchestration, rerun, reuse, partial failure, and completion.
5. Classify each gap as existing authority, missing ADR, specification elaboration, evidence need, or implementation-only choice.
6. Record exact decision points for T02 through T06.
7. Define the focused child-specification map for T07.
8. Confirm that Learning meaning and Application runtime reads remain fixed inputs.
9. Do not change normative specifications or adopt new Pipeline decisions.

## Done condition

- Every required Pipeline design area has one current-state judgment.
- Every normative gap names current authority or an explicit missing-ADR route.
- Evidence is separated from normative authority.
- Implementation-only choices are excluded from design decisions.
- T02 through T07 have exact bounded inputs.
- The child-specification map covers source acquisition, normalization, paths, generation, validation, provenance, publication, and orchestration.
- No normative ADR or specification changes occur.

## Verification

- Confirm accepted Pipeline ADR status and supersession chains.
- Confirm PRODUCT-WORK-LEARNING-001 is treated as fixed input.
- Confirm Application published-content semantics are not reopened.
- Confirm each gap has one semantic owner.
- Confirm the proposed specification map preserves `spec:product.pipeline` as the overview router.
- Validate H1, metadata, canonical refs, reciprocal relations, and required sections.
- Run strict specification validation, `git diff --check`, and `git status --short`.

## Evidence

TBD
