# PRODUCT-TASK-APPLICATION-005-03: Define adapter and verification obligations

- **id**: PRODUCT-TASK-APPLICATION-005-03
- **status**: not_started
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-005
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-005-02
- **outputs**:

## Goal

Prepare a complete authority-backed contract map for outbound query adapters and their verification boundaries.

Keep application tests separate from persistence-adapter contract tests.

## Work

1. Read the T005-01 inventory and the T005-02 authority disposition.
2. Stop as `blocked` when a normative obligation lacks accepted ADR authority.
3. Define application-owned inputs and normal results for selection and retrieval.
4. Preserve the dependency direction from persistence adapter to application-owned outbound contract.
5. Define persistence-adapter obligations for bounded selection.
6. Define persistence-adapter obligations for current published-unit retrieval.
7. Keep selection and retrieval as distinct operations.
8. Separate normal empty selection results from selection technical failures.
9. Preserve `Unavailable` as a normal retrieval result.
10. Preserve mapping and infrastructure failures as technical failures.
11. Define the application-test boundary using test doubles for outbound contracts.
12. Define persistence-adapter contract-test coverage against the real adapter boundary.
13. Cover zero, below-limit, exact-limit, and above-limit selection candidate sets.
14. Cover unavailable candidates, uniqueness, stable-reference mapping, and randomized returned order.
15. Cover available, missing, unavailable, mapping-failure, and infrastructure-failure retrieval cases.
16. Keep concrete database products, fixtures, containers, queries, and algorithms deferred.
17. Record the contract map as task evidence for T005-04.

This task must not become canonical decision or specification authority.
Any new normative decision must return to T005-02 and an accepted ADR.

## Done condition

- Selection and retrieval inputs and results are separately mapped.
- Application and persistence-adapter responsibilities are explicit.
- Normal outcomes and technical failures are separated.
- Application-test test doubles have a defined boundary.
- Persistence-adapter contract tests have defined required coverage.
- Every normative obligation traces to an accepted ADR.
- Implementation details remain deferred.
- T005-04 can reflect the contract without inventing decisions.

## Verification

- Trace every obligation to PRODUCT-ADR-APPLICATION-003, PRODUCT-ADR-APPLICATION-004, or an accepted T005-02 ADR.
- Confirm task evidence contains no unsupported normative claim.
- Confirm selection tests cover observable and adapter-owned guarantees separately.
- Confirm retrieval tests preserve `Available | Unavailable` semantics.
- Confirm contract tests exercise the persistence adapter rather than another mock.
- Confirm database and transport implementation choices remain absent.

## Evidence

TBD
