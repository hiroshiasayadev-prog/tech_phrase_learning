# PRODUCT-TASK-APPLICATION-006-05: Review and close PWA-facing application-interface design

- **id**: PRODUCT-TASK-APPLICATION-006-05
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-006
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 0.5d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-006-04
- **outputs**:
  - PRODUCT-WORK-APPLICATION-006

## Goal

Independently verify PWA-facing interface consistency, ADR-first traceability, and implementation readiness.

Close PRODUCT-WORK-APPLICATION-006 only after all blocking findings are corrected.

## Work

1. Use a reviewer who did not implement PRODUCT-TASK-APPLICATION-006-02 through PRODUCT-TASK-APPLICATION-006-04.
2. Review every impact ref from PRODUCT-WORK-APPLICATION-006.
3. Review every new or changed specification produced by T006-04.
4. Verify that each normative specification change traces to an accepted ADR.
5. Verify that current application and UI ADRs remain authoritative.
6. Verify that superseded ADRs remain historical only.
7. Verify queue creation and complete-unit retrieval remain distinct operations.
8. Verify stable reference meaning without a concrete wire representation.
9. Verify successful non-empty and empty queue outcomes.
10. Verify available and unavailable retrieval outcomes.
11. Verify invalid requests remain distinct from unavailable content and technical failures.
12. Verify network and infrastructure failures remain distinct from normal outcomes.
13. Verify unavailable-reference skipping remains distinct from retryable request failure.
14. Verify queue exhaustion remains a PWA-owned trigger.
15. Verify queue, loaded-unit, session, navigation, and retry ownership remains in the PWA.
16. Verify replacement occurs only after successful complete-unit loading.
17. Verify attribution remains learner-visible and provenance remains excluded.
18. Verify future HTTP mapping remains possible without normative routes, status codes, or JSON.
19. Verify interface tests and future transport-adapter contract tests have explicit boundaries.
20. Verify no authentication, learner account, backend session, or durable progress entered the design.
21. Record findings with exact refs and severity.
22. Give a final `PASS` or `NEEDS REVISION` verdict.
23. Re-run the independent review after any blocking finding is corrected.
24. Close PRODUCT-WORK-APPLICATION-006 only after the final verdict is `PASS`.

Do not implement fixes during the independent review.

## Done condition

- The review covers every work-item completion condition and impact ref.
- Findings identify exact refs and conflicting claims.
- ADR-first traceability is complete.
- Application and UI ownership remain distinct.
- Normal outcomes, invalid requests, and technical failures remain separated.
- Unavailable-reference skipping and request retry behavior remain distinct.
- PWA state-preservation and successful-replacement rules remain intact.
- Attribution and provenance boundaries remain intact.
- Transport-independent contracts are implementation-ready.
- Blocking findings are corrected and independently re-reviewed.
- The final verdict is `PASS`.
- Evidence states whether transport and PWA implementation planning may begin.

## Verification

- Confirm reviewer independence from T006-02 through T006-04.
- Confirm every reviewed normative claim has accepted ADR authority.
- Confirm strict specification validation passes.
- Confirm `git diff --check` passes.
- Confirm final working-tree evidence is recorded.
- Confirm PRODUCT-WORK-APPLICATION-006 closes only after `PASS`.

## Evidence

### Independent review

- **Reviewer**: Opus independent review session.
- **Independence**: The reviewer did not implement PRODUCT-TASK-APPLICATION-006-02 through PRODUCT-TASK-APPLICATION-006-04.
- **Verdict**: PASS.
- **Blocking findings**: none.
- **Major findings**: none.
- **Minor findings**: one status-hygiene finding.
- **Advisories**: four non-blocking observations.

### Finding disposition

| finding | disposition |
|---|---|
| F-MIN-01: PRODUCT-WORK-APPLICATION-006 remained `not_started` after substantive child-task execution. | Corrected. The work item moved to `in_progress` before this closure transaction and then to `done` after closure evidence was recorded. |
| F-ADV-01: `impact_refs` and `## Impact Scope` did not include the ADRs and PWA-interface specs produced by the resolution flow. | Adopted. Added PRODUCT-ADR-APPLICATION-005, PRODUCT-ADR-APPLICATION-006, PRODUCT-ADR-UI-002, and the three `spec:product.application.pwa_interface` refs. |
| F-ADV-02: T006-04 outputs include ADRs modified only through `migrated_to_spec`. | No change. Task outputs may list modified artifacts. |
| F-ADV-03: Interface-test obligations do not carry a dedicated ADR reference per row. | No change. The obligations restate guarantees from accepted ADR-003, ADR-004, ADR-005, and ADR-006. |
| F-ADV-04: Shared ownership wording could qualify application retryability ownership. | No change. Current operation contracts correctly leave unclassified `InvalidSelectionResult` retry behavior to the UI. |

### Review verdicts

| review area | verdict | evidence summary |
|---|---|---|
| ADR-first traceability | PASS | Every normative change traces to accepted application or UI ADR authority. Task Evidence is not used as authority. |
| Ownership boundary | PASS | Application owns interface semantics. UI owns transient lifecycle, retry attempts, transitions, state preservation, disposal, and diagnostic surfaces. |
| Operation separation | PASS | Queue creation returns ordered references only. Retrieval accepts one reference and returns complete availability-shaped content. |
| Result and failure separation | PASS | Empty queue and `Unavailable` remain normal results. Mapping, infrastructure, and selection-contract failures remain distinct. |
| Replacement queue transitions | PASS | Replacement infrastructure failure retries on the learning page. Replacement mapping and selection-contract failures show diagnostic information and `Back to main` without retry. |
| Stable reference semantics | PASS | `LearningUnitRef` remains stable, opaque, comparable, unchanged through pass-through, and wire-format agnostic. |
| Queue and session ownership | PASS | Queue exhaustion is PWA-owned. Loaded content, queue position, and session change only after successful complete-unit loading. |
| Attribution and provenance | PASS | Available content preserves learner-visible attribution and excludes provenance. |
| Verification obligations | PASS | Application-interface and future transport-adapter test boundaries are explicit and transport independent. |
| Deferred concerns | PASS | No HTTP, JSON, framework, authentication, backend session, queue persistence, or durable progress decision entered the design. |

### Validation

| check | result |
|---|---|
| `git diff --check` from independent review | PASS. Only Windows LF/CRLF normalization warnings were reported. |
| `git status --short` from independent review | Matched the T006-04 scope and showed no unexplained out-of-scope edits. |
| Design Records MCP | Not used as PRODUCT validation authority because the active instance does not index this repository namespace. |
| Filesystem review | Confirmed canonical IDs, parent refs, statuses, dates, required sections, and path-derived refs. |

### Completion judgment

- PRODUCT-WORK-APPLICATION-006 completion conditions are satisfied.
- The transport-independent application interface is implementation-ready.
- Future transport mapping and PWA implementation planning may begin.
- PRODUCT-WORK-APPLICATION-006 may close.

