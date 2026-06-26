# PRODUCT-TASK-APPLICATION-005-05: Review and close application outbound query-port design

- **id**: PRODUCT-TASK-APPLICATION-005-05
- **status**: not_started
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-005
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 0.5d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-005-04
- **outputs**:

## Goal

Independently verify outbound query-port consistency, ADR-first traceability, and implementation readiness.

Close PRODUCT-WORK-APPLICATION-005 only after all blocking findings are corrected.

## Work

1. Use a reviewer who did not implement PRODUCT-TASK-APPLICATION-005-02 through PRODUCT-TASK-APPLICATION-005-04.
2. Review every impact ref from PRODUCT-WORK-APPLICATION-005.
3. Review every new or moved application specification created by T005-04.
4. Verify that each normative specification change traces to an accepted ADR.
5. Verify that PRODUCT-ADR-APPLICATION-003 and PRODUCT-ADR-APPLICATION-004 remain current authority.
6. Verify that superseded ADRs remain historical only.
7. Verify that selection and retrieval remain distinct operations.
8. Verify application ownership of outbound query contracts.
9. Verify persistence-adapter dependency direction and mapping obligations.
10. Verify bounded randomized selection obligations remain intact.
11. Verify retrieval committed-state and availability behavior remains intact.
12. Verify normal empty selection and `Unavailable` results remain distinct from technical failures.
13. Verify application-test test doubles and persistence-adapter contract-test boundaries.
14. Verify shared rules are owned once and child specifications avoid unnecessary duplication.
15. Verify root and topic overviews route only their direct children.
16. Verify converted topic indexes preserve existing semantic refs.
17. Verify no concrete SQL, schema, ORM, database, algorithm, framework, source-layout, or transport choice entered the design.
18. Record findings with exact refs and severity.
19. Give a final `PASS` or `NEEDS REVISION` verdict.
20. Re-run the independent review after any blocking finding is corrected.
21. Close PRODUCT-WORK-APPLICATION-005 only after the final verdict is `PASS`.

Do not implement fixes during the independent review.

## Done condition

- The review covers every work-item completion condition and impact ref.
- Findings identify exact refs and conflicting claims.
- ADR-first traceability is complete.
- Selection and retrieval ownership remains distinct.
- Normal results and technical failures remain separated.
- Test-double and adapter contract-test boundaries are implementation-ready.
- Specification decomposition remains focused and navigable.
- Blocking findings are corrected and independently re-reviewed.
- The final verdict is `PASS`.
- Evidence states whether implementation planning may begin.

## Verification

- Confirm reviewer independence from T005-02 through T005-04.
- Confirm every reviewed normative claim has accepted ADR authority.
- Confirm strict specification validation passes.
- Confirm `git diff --check` passes.
- Confirm final working-tree evidence is recorded.
- Confirm PRODUCT-WORK-APPLICATION-005 closes only after `PASS`.

## Evidence

TBD
