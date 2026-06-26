# PRODUCT-TASK-APPLICATION-004-01: Establish published learning-unit retrieval design baseline

- **id**: PRODUCT-TASK-APPLICATION-004-01
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-004
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 0.5d
- **depends_on**:
- **outputs**:

## Goal

Identify accepted retrieval decisions, stale records, and unresolved decision points before further design work.

## Work

1. Read the current APPLICATION, PIPELINE, LEARNING, and UI ADRs and specifications relevant to retrieval.
2. Separate accepted decisions from specification gaps and implementation details.
3. Identify conflicts that require a replacing ADR.
4. Keep unresolved decisions out of specifications.
5. Record only baseline findings and downstream work in this task.

## Done condition

- Relevant records are reviewed.
- Stale or conflicting decision lineage is identified.
- Unresolved decisions are routed to ADR work.
- Implementation details remain outside decision and specification records.
- Downstream tasks can proceed without treating this task as design authority.

## Verification

- Confirm task evidence cites authoritative ADRs and specifications.
- Confirm task evidence does not act as the canonical retrieval contract.
- Confirm unresolved decisions remain outside specifications.
- Confirm downstream tasks require accepted ADRs before specification reflection.

## Evidence

### Result

- **Verdict**: PASS.
- The baseline review found stale previous and new publication wording in the active APPLICATION decision chain.
- The baseline review found unresolved retrieval-result, provenance-exposure, integrity-ownership, and outbound-port questions.
- The earlier root-spec diagram change was reverted because it preceded an accepted authorizing ADR.

### Follow-up disposition

- PRODUCT-TASK-APPLICATION-004-02 produced PRODUCT-ADR-APPLICATION-003.
- PRODUCT-ADR-APPLICATION-003 supersedes PRODUCT-ADR-APPLICATION-001 and PRODUCT-ADR-APPLICATION-002.
- PRODUCT-TASK-APPLICATION-004-03 owns the remaining outbound retrieval-port decision.
- PRODUCT-TASK-APPLICATION-004-04 owns specification reflection after all required ADRs are accepted.

### Authority boundary

- Current adopted retrieval decisions belong to PRODUCT-ADR-APPLICATION-003.
- Current specification text remains owned by the applicable `spec:product.*` records.
- This task records review evidence only.
