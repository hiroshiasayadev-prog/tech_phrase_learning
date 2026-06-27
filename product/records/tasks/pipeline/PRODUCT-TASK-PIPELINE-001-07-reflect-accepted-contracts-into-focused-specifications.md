# PRODUCT-TASK-PIPELINE-001-07: Reflect accepted contracts into focused Pipeline specifications

- **id**: PRODUCT-TASK-PIPELINE-001-07
- **status**: not_started
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PIPELINE-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 2.5d
- **depends_on**:
  - PRODUCT-TASK-PIPELINE-001-06
- **outputs**:
  - spec:product.pipeline

## Goal

Reflect accepted Pipeline decisions into focused current specifications without introducing new normative decisions.

## Work

1. Read the T01 child-specification map and accepted ADRs produced by T02 through T06.
2. Confirm every proposed normative specification statement has accepted ADR authority.
3. Keep `spec:product.pipeline` as the overview router and cross-area boundary.
4. Create focused child specifications for the semantic boundaries approved by T01.
5. Cover at least:
   - source acquisition and retained-source reuse;
   - authentic source model and normalization;
   - path enumeration;
   - path validation and suitability filtering;
   - summary, phrase, prompt, and quiz generation;
   - validation and publication readiness;
   - artifact identity and provenance;
   - publication handoff and availability change;
   - orchestration and stage completion.
6. Place each contract in one owning child specification and avoid duplicated normative text.
7. Preserve references to Learning meanings instead of copying or redefining them.
8. Preserve references to Application published-content semantics instead of redefining runtime reads.
9. Update Pipeline ADR `migrated_to_spec` state only after full reflection.
10. Update `outputs` with every created or modified child specification ref.
11. Update parent and related topic maps, boundaries, and related-spec links.
12. Keep concrete implementation technology, schemas, routes, thresholds, and exact prompts outside specifications.
13. Run strict validation after each coherent reflection group.

## Done condition

- `spec:product.pipeline` routes to focused child specifications.
- Every accepted Pipeline decision is reflected once in the owning current specification.
- Source, normalization, path, generation, validation, provenance, publication, and orchestration contracts are implementation-planning ready.
- Learning semantics are referenced and not redefined.
- Application runtime-read semantics are referenced and not changed.
- No task, work-item, investigation, or fixture evidence acts as normative authority.
- Every reflected ADR has accurate `migrated_to_spec` state.
- No unaccepted normative decision appears in specifications.
- Concrete implementation technologies remain excluded.
- T08 can review the complete Pipeline contract from current ADRs and specifications.

## Verification

- Trace every normative change to one accepted Pipeline ADR.
- Check each child specification H1, metadata, path-derived ref, parent, topics, and related refs.
- Check the overview topic map against the filesystem.
- Check for duplicated or conflicting contracts across child specifications.
- Confirm the complete unit and publication outputs match Learning and Application boundaries.
- Run strict specification validation, `git diff --check`, and `git status --short`.
- Record every modified specification and validation result in Evidence.

## Evidence

TBD
