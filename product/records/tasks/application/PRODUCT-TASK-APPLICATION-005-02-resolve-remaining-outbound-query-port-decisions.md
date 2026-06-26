# PRODUCT-TASK-APPLICATION-005-02: Resolve remaining outbound query-port decisions

- **id**: PRODUCT-TASK-APPLICATION-005-02
- **status**: not_started
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-005
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-005-01
- **outputs**:

## Goal

Resolve only the genuine architectural decisions identified by T005-01.

Record each adopted normative decision in an accepted ADR before specification reflection.

## Work

1. Read the classified gap inventory from PRODUCT-TASK-APPLICATION-005-01.
2. Ignore topics classified as already decided, already specified, or deferred implementation details.
3. Do not reopen PRODUCT-ADR-APPLICATION-003 or PRODUCT-ADR-APPLICATION-004.
4. Present each genuine decision through a concrete runtime situation.
5. Ask for one user decision at a time when user judgment is required.
6. Create a new APPLICATION ADR only for an adopted unresolved normative decision.
7. Keep each ADR limited to one coherent decision boundary.
8. Keep SQL, schema, ORM, database, algorithm, framework, source-layout, and transport choices deferred.
9. Do not modify specifications in this task.
10. Conclude explicitly when the inventory requires no new ADR.
11. Stop as `blocked` with `reason: missing ADR` when downstream normative work lacks accepted authority.

Likely decision candidates must remain candidates until T005-01 confirms a genuine gap.
Examples include selection-port ownership and selection technical-failure separation.
These examples are not decision authority.

## Done condition

- Every genuine decision gap from T005-01 has a recorded disposition.
- Every adopted normative decision exists in an accepted ADR.
- No ADR duplicates an existing ADR-003 or ADR-004 decision.
- No ADR exists merely because the task graph contains an ADR step.
- No specification changed before accepted authority existed.
- Deferred implementation details remain deferred.
- T005-03 has an explicit authority set or an explicit no-new-ADR conclusion.

## Verification

- Confirm each new ADR corresponds to a T005-01 genuine decision gap.
- Confirm each new ADR uses required metadata and sections.
- Confirm accepted ADRs precede specification reflection.
- Confirm no decision-bearing accepted or superseded ADR body was rewritten.
- Confirm no selection or retrieval semantic contract was reopened.
- Confirm task evidence is not used as canonical decision authority.

## Evidence

TBD
