# PRODUCT-TASK-APPLICATION-006-02: Resolve remaining PWA-interface decisions

- **id**: PRODUCT-TASK-APPLICATION-006-02
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-006
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-006-01
- **outputs**:
  - PRODUCT-ADR-APPLICATION-005
  - PRODUCT-ADR-APPLICATION-006

## Goal

Resolve only the genuine normative decisions identified by T006-01.

Record each adopted decision in an accepted ADR before specification reflection.

## Work

1. Read the classified gap inventory from PRODUCT-TASK-APPLICATION-006-01.
2. Ignore topics classified as already decided, already specified, or deferred implementation details.
3. Do not reopen PRODUCT-ADR-APPLICATION-003, PRODUCT-ADR-APPLICATION-004, or PRODUCT-ADR-UI-001.
4. Present each genuine decision through a concrete PWA runtime situation.
5. Ask for one user decision at a time when user judgment is required.
6. Create a new APPLICATION ADR only for an adopted unresolved normative decision.
7. Stop and route any UI-owned state or transition decision to the owning UI decision flow.
8. Keep each APPLICATION ADR limited to one coherent application-interface decision boundary.
9. Keep HTTP, serialization, client configuration, framework, and source-layout choices deferred.
10. Do not modify specifications in this task.
11. Conclude explicitly when the inventory requires no new ADR.
12. Stop as `blocked` with `reason: missing ADR` when downstream normative work lacks accepted authority.

Candidate topics must remain candidates until T006-01 confirms a genuine gap.

Examples, not exhaustive:

- invalid-request classification at the PWA-facing boundary;
- retryable versus non-retryable technical failure classification;
- stable reference representation at the interface boundary;
- public result categories required for future transport mapping.

These examples are not decision authority.

## Done condition

- Every genuine decision gap from T006-01 has a recorded disposition.
- Every adopted normative decision exists in an accepted ADR.
- No ADR duplicates an existing application or UI decision.
- UI-owned decisions are routed to the UI area instead of being adopted by this APPLICATION work item.
- No ADR exists merely because the task graph contains an ADR step.
- No specification changed before accepted authority existed.
- Completed queue, retrieval, and PWA state semantics remain closed.
- Deferred transport and implementation details remain deferred.
- T006-03 has an explicit authority set or an explicit no-new-ADR conclusion.

## Verification

- Confirm each new ADR corresponds to a T006-01 genuine decision gap.
- Confirm each new ADR uses required metadata and sections.
- Confirm accepted ADRs precede specification reflection.
- Confirm no accepted or superseded ADR body was rewritten to replace its decision.
- Confirm PWA-owned state did not move into the application boundary.
- Confirm UI-owned decisions were routed rather than adopted in an APPLICATION ADR.
- Confirm no HTTP or serialization choice entered an ADR without explicit scope authority.
- Confirm task evidence is not used as canonical decision authority.

## Evidence

### Result

- **Verdict**: PASS.
- Every genuine decision gap from PRODUCT-TASK-APPLICATION-006-01 now has accepted authority.
- No specification changed in this task.
- Completed queue, retrieval, outbound-query, attribution, provenance, and PWA state-ownership decisions were not reopened.

### Accepted APPLICATION authority

- PRODUCT-ADR-APPLICATION-005 records the PWA-facing failure taxonomy, safe diagnostic boundary, and retryability classification.
- PRODUCT-ADR-APPLICATION-006 records `LearningUnitRef` stability, opacity, equality, and unchanged pass-through semantics.
- Both ADRs are additive and do not supersede PRODUCT-ADR-APPLICATION-003 or PRODUCT-ADR-APPLICATION-004.

### Accepted UI authority and route

- PRODUCT-REQ-UI-001 records the UI-owned transition requirement.
- PRODUCT-WORK-UI-001 owns the UI resolution flow.
- PRODUCT-TASK-UI-001-01 created PRODUCT-ADR-UI-002 under the UI domain.
- PRODUCT-ADR-UI-002 records category-specific retry, flow termination, queue and session disposal, return-to-main, and diagnostic-surface behavior.
- PRODUCT-ADR-UI-002 is additive and does not supersede PRODUCT-ADR-UI-001.
- PRODUCT-TASK-UI-001-02 remains pending coordinated specification reflection and review.

### Authority set supplied to T006-03

- PRODUCT-ADR-APPLICATION-003
- PRODUCT-ADR-APPLICATION-004
- PRODUCT-ADR-APPLICATION-005
- PRODUCT-ADR-APPLICATION-006
- PRODUCT-ADR-UI-001
- PRODUCT-ADR-UI-002

### Deferred details

- HTTP routes, methods, headers, and status codes
- JSON fields, serialization formats, and wire representation of `LearningUnitRef`
- Concrete exception and programming-language result types
- Retry delays, backoff, timeout values, and client configuration
- Exact diagnostic wording, layout, and styling
- Framework, state library, route structure, and source layout

### Verification

- Each new ADR corresponds to a genuine decision gap identified by PRODUCT-TASK-APPLICATION-006-01.
- APPLICATION and UI decisions are recorded under their owning domains.
- Existing PRODUCT-ADR-APPLICATION-003, PRODUCT-ADR-APPLICATION-004, and PRODUCT-ADR-UI-001 remain valid.
- Superseded application ADRs remain historical only.
- No specification changed.
- Filesystem rereads confirmed the created records and reciprocal Requirement, Work Item, and Task relations.
- Design Records MCP did not index the PRODUCT namespace, so filesystem fallback was used.
- Git and repository-wide validator execution were unavailable in this tool environment and are not claimed.
