# PRODUCT-TASK-APPLICATION-002-02: Define published projection and lifecycle

- **id**: PRODUCT-TASK-APPLICATION-002-02
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-002
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-002-01
- **outputs**:

## Goal

Define the current published projection and its content, availability, and replacement invariants.

## Work

1. Use the classifications and evidence from PRODUCT-TASK-APPLICATION-002-01.
2. Trace stable identity, availability separation, atomic replacement, and loaded-content behavior to accepted ADRs.
3. Define the semantic elements of the current published projection without selecting a storage schema.
4. Define the observable meaning of `available` and `unavailable` for application runtime reads.
5. Define replacement invariants under one stable learning-unit identity.
6. Define availability-only change invariants independently from content replacement.
7. Keep attribution inside the complete learning-unit contract instead of redefining it at projection level.
8. Determine whether any adopted result requires a new ADR.
9. Record the resolved design and ADR judgment in `## Evidence`.
10. Leave specification reflection and cross-area reconciliation to PRODUCT-TASK-APPLICATION-002-04.

## Done condition

- Stable learning-unit identity remains anchored to one valid learning path.
- The current published projection is complete and implementation-independent.
- Complete learning-unit content, availability, and provenance remain independently defined.
- `unavailable` retains current content while excluding the unit from new queues and normal retrieval.
- Content replacement cannot create two current projections for one stable identity.
- Content replacement publishes content, provenance, and publication-judged availability as one observable state.
- An availability-only change does not replace content or provenance.
- Attribution remains owned by the complete learning-unit contract.
- The ADR requirement judgment is explicit.
- PRODUCT-TASK-APPLICATION-002-04 has sufficient inputs to reflect the design in specifications.

## Verification

- Compare every resolved design statement with PRODUCT-ADR-APPLICATION-001 and PRODUCT-ADR-LEARNING-005.
- Confirm that the result defines observable projection invariants rather than pipeline orchestration commands.
- Confirm that no exhaustive invalid-transition state machine is introduced.
- Confirm that no concrete database or transaction mechanism enters the design.
- Confirm that loaded PWA content is not retroactively mutated.
- Confirm that any new architectural decision has an accepted ADR before task completion.

## Evidence

### Result

- **Verdict**: PASS.
- The current published projection and its observable invariants are resolved.
- No new architectural decision was adopted.
- No new ADR is required for this task.
- PRODUCT-TASK-APPLICATION-002-04 owns specification reflection.

### Accepted decision sources

- PRODUCT-ADR-LEARNING-005 anchors one stable learning-unit identity to one valid learning path.
- PRODUCT-ADR-APPLICATION-001 separates current content from mutable availability.
- PRODUCT-ADR-APPLICATION-001 requires atomic replacement under one stable identity.
- PRODUCT-ADR-APPLICATION-001 defines unavailable retrieval and loaded-copy immutability.

### Resolved projection

```text
PublishedLearningUnitProjection
  +-- stable_learning_unit_id
  +-- learning_unit
  +-- availability
  +-- provenance_ref
```

- `learning_unit` is one complete unit defined by `spec:product.learning.learning_unit`.
- Attribution remains part of the complete learning unit.
- The projection does not redefine attribution as an independent semantic field.
- `provenance_ref` is opaque to application logic.
- One stable identity addresses at most one current projection.

### Availability meaning

- `available` permits inclusion in a newly created queue and normal learning-unit retrieval.
- `unavailable` excludes the unit from new queues.
- Normal application retrieval of an unavailable unit returns an unavailable result.
- Unavailability retains current content, attribution, source references, and current provenance.
- Unavailability does not create another learning-unit identity.

### Replacement invariants

- Generated-content changes preserve stable identity when the valid learning path is unchanged.
- Replacement publishes complete content, its matching opaque provenance reference, and publication-judged availability as one observable state.
- The resulting availability comes from the current publication judgment rather than implicit inheritance.
- A concurrent read observes either the previous complete projection or the new complete projection.
- Replacement does not require runtime revision history, rollback, or a sibling learning unit.

### Availability-only invariants

- An availability-only change leaves current content unchanged.
- An availability-only change leaves the provenance reference unchanged.
- Withdrawal does not delete current content.
- A later publication judgment may make the same stable identity available again.

### ADR judgment

The resolved projection composition and invariants detail decisions already accepted by PRODUCT-ADR-LEARNING-005 and PRODUCT-ADR-APPLICATION-001.
They do not introduce a new architectural choice, so no ADR was created.

### T04 inputs

PRODUCT-TASK-APPLICATION-002-04 must:

- reflect the four-element projection in `spec:product.application.published_content`;
- remove independent attribution duplication at projection level;
- preserve availability-only and replacement invariants;
- keep persistence and transport mechanisms deferred.
