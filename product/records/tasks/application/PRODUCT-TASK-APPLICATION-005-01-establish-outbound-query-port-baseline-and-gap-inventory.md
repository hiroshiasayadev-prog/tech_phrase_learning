# PRODUCT-TASK-APPLICATION-005-01: Establish outbound query-port baseline and gap inventory

- **id**: PRODUCT-TASK-APPLICATION-005-01
- **status**: not_started
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-005
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 0.5d
- **depends_on**:
- **outputs**:

## Goal

Establish the authoritative outbound query-port baseline before any decision or specification change.

Classify every candidate gap by its correct owning artifact kind.

## Work

1. Read PRODUCT-ADR-APPLICATION-003 and PRODUCT-ADR-APPLICATION-004 as current decision authority.
2. Treat PRODUCT-ADR-APPLICATION-001 and PRODUCT-ADR-APPLICATION-002 as superseded history only.
3. Read PRODUCT-WORK-APPLICATION-003 and its final review evidence.
4. Read PRODUCT-WORK-APPLICATION-004 and its final review evidence.
5. Read the current application, published-content, learning-unit, and pipeline specifications.
6. Inventory the selection operation, retrieval port, inputs, results, adapter obligations, and failure boundaries.
7. Classify each topic as one of:
   - already decided by an accepted ADR;
   - already specified by WORK-003 or WORK-004;
   - missing specification reflection;
   - genuinely unresolved architectural decision;
   - implementation detail deferred from product design.
8. Identify duplicated contracts and unclear specification ownership.
9. Verify the proposed topic decomposition from PRODUCT-WORK-APPLICATION-005.
10. Preserve existing semantic refs when a current leaf topic may become an `index.md`.
11. Record UI refs only when a direct UI-contract impact exists.
12. Do not modify specifications or create an ADR.

Use concrete runtime situations when explaining each candidate gap.
Do not present abstract alternatives without showing where the behavior occurs.

## Done condition

- Every selection and retrieval concern has one classification.
- Current authority is limited to PRODUCT-ADR-APPLICATION-003 and PRODUCT-ADR-APPLICATION-004.
- Completed selection and retrieval semantics are not reopened.
- Genuine decision gaps are separated from missing specification reflection.
- Deferred implementation details remain explicit.
- Duplicate or misplaced specification content is identified.
- The proposed topic decomposition has a ref-preservation and ownership judgment.
- T005-02 can proceed without another conversation handoff.

## Verification

- Trace every already-decided claim to an accepted ADR.
- Trace every already-specified claim to a current specification.
- Confirm superseded ADRs are not used as current authority.
- Confirm no specification or ADR changed.
- Confirm every proposed normative change is routed to T005-02.
- Confirm physical paths are not used as canonical refs.

## Evidence

TBD
