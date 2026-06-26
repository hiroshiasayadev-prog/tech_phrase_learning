# PRODUCT-TASK-APPLICATION-004-02: Define retrieval result and availability semantics

- **id**: PRODUCT-TASK-APPLICATION-004-02
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-004
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-004-01
- **outputs**:
  - PRODUCT-ADR-APPLICATION-003

## Goal

Record the adopted retrieval, publication-state, provenance, and integrity decisions in one accepted ADR.

## Work

1. Review the unresolved decisions from PRODUCT-TASK-APPLICATION-004-01.
2. Present retrieval-result terminology and publication-state choices for user judgment.
3. Record adopted decisions in a new APPLICATION ADR.
4. Supersede conflicting accepted APPLICATION ADRs through the new ADR lineage.
5. Keep specification changes outside this task.
6. Record execution and verification evidence in this task.

## Done condition

- One accepted ADR owns the adopted retrieval-result terminology.
- The accepted ADR owns transactional current-state publication semantics.
- The accepted ADR owns provenance exposure and integrity-validation boundaries.
- Conflicting earlier APPLICATION ADRs are superseded without decision-bearing body edits.
- This task contains evidence rather than canonical decision text.
- No specification is changed by this task.

## Verification

- Confirm the accepted ADR uses all required sections and metadata.
- Confirm the replacing ADR lists every replaced ADR in `supersedes`.
- Confirm replaced ADRs move from `accepted` to `superseded` without decision-bearing body changes.
- Confirm any historical ADR metadata correction does not change decision meaning.
- Confirm current specifications remain unchanged until the reflection task.
- Confirm the task references the accepted ADR in `outputs` and `## Evidence`.

## Evidence

### Result

- **Verdict**: PASS.
- PRODUCT-ADR-APPLICATION-003 records the adopted retrieval and current published-content decisions.
- PRODUCT-ADR-APPLICATION-003 supersedes PRODUCT-ADR-APPLICATION-001 and PRODUCT-ADR-APPLICATION-002.
- PRODUCT-ADR-APPLICATION-001 received a status-only supersession change.
- PRODUCT-ADR-APPLICATION-002 received a supersession status change and one missing required metadata field.
- No decision-bearing section changed in either superseded ADR.
- No specification was changed by this task.

### Decision authority

- Retrieval-result terminology: PRODUCT-ADR-APPLICATION-003.
- Transactional current-state publication: PRODUCT-ADR-APPLICATION-003.
- Pipeline publication-integrity ownership: PRODUCT-ADR-APPLICATION-003.
- Provenance exclusion from normal PWA retrieval: PRODUCT-ADR-APPLICATION-003.

### Remaining boundary

PRODUCT-ADR-APPLICATION-003 intentionally defers the outbound retrieval-port result shape.
PRODUCT-TASK-APPLICATION-004-03 must resolve that boundary through a new accepted ADR before specification reflection.
