# PRODUCT-TASK-APPLICATION-004-03: Define projection mapping and adapter obligations

- **id**: PRODUCT-TASK-APPLICATION-004-03
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-004
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-004-02
- **outputs**:
  - PRODUCT-ADR-APPLICATION-004

## Goal

Record the outbound retrieval-port and persistence-adapter boundary in an accepted ADR before specification reflection.

## Work

1. Read PRODUCT-ADR-APPLICATION-003.
2. Explain the runtime request path using concrete responsibilities.
3. Confirm whether database reading and stored-availability mapping belong to the persistence adapter.
4. Record the adopted boundary in a new APPLICATION ADR.
5. Keep pipeline publication-integrity validation owned by PRODUCT-ADR-APPLICATION-003.
6. Keep mapping and infrastructure failures outside normal availability results.
7. Define adapter contract-test obligations as consequences of the accepted ADR.
8. Do not change specifications in this task.
9. Record the created ADR and verification evidence in `outputs` and `## Evidence`.

## Done condition

- One accepted ADR records the outbound retrieval-port result shape.
- The ADR defines application ownership of the port contract.
- The ADR defines persistence-adapter ownership of database reading and stored-availability mapping.
- The ADR preserves pipeline ownership of availability decisions and publication integrity.
- The ADR keeps provenance outside the normal application result.
- Mapping and infrastructure failures remain technical failures.
- No specification is changed by this task.
- This task references the accepted ADR in `outputs` and `## Evidence`.

## Verification

- Confirm the task does not become the source of truth for the port decision.
- Confirm PRODUCT-ADR-APPLICATION-004 precedes specification reflection.
- Confirm normal results remain `Available` and `Unavailable`.
- Confirm the persistence adapter reads committed content and stored availability.
- Confirm the persistence adapter does not own availability policy.
- Confirm provenance does not reach the normal application result.
- Confirm no SQL, table, ORM, transport, or framework type enters the ADR.
- Confirm technical failures remain distinct from normal availability results.

## Evidence

### Result

- **Verdict**: PASS.
- PRODUCT-ADR-APPLICATION-004 records the accepted outbound retrieval-port boundary.
- The earlier projection-shaped alternative was removed because it conflicts with the existing persistence-adapter responsibility.
- No specification was changed by this task.

### Decision authority

- Outbound retrieval-port shape: PRODUCT-ADR-APPLICATION-004.
- Pipeline availability and integrity ownership: PRODUCT-ADR-APPLICATION-003.

### Contract-test consequences

PRODUCT-ADR-APPLICATION-004 requires adapter contract coverage for:

- available current content;
- missing current content;
- unavailable current content;
- persistence mapping failure;
- infrastructure failure.

PRODUCT-TASK-APPLICATION-004-04 owns specification reflection.
