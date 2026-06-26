# PRODUCT-TASK-APPLICATION-002-03: Define publication handoff and consistency

- **id**: PRODUCT-TASK-APPLICATION-002-03
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-002
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-002-02
- **outputs**:
  - PRODUCT-ADR-PIPELINE-005

## Goal

Define the semantic pipeline handoff and the consistency guarantees visible to application reads.

## Work

1. Use the projection contract resolved by PRODUCT-TASK-APPLICATION-002-02.
2. Trace pipeline write ownership, application read ownership, atomic replacement, and opaque provenance to accepted ADRs.
3. Define one semantic publication handoff input without selecting a command, event, or wire schema.
4. Define validation and publication-judgment preconditions before published-content mutation.
5. Define pipeline writer obligations for initial publication and replacement.
6. Define the independent availability-only write obligation used for withdrawal.
7. Define application reader obligations over the published projection.
8. Define observable consistency for reads concurrent with publication writes.
9. Define current provenance reachability without exposing pipeline processing semantics to application logic.
10. Determine whether any adopted result requires a new ADR.
11. Record the resolved handoff, consistency guarantees, and ADR judgment in `## Evidence`.
12. Leave specification reflection and cross-area reconciliation to PRODUCT-TASK-APPLICATION-002-04.

Do not define concrete commands, event formats, tables, transactions, retry mechanisms, or historical artifact schemas.

## Done condition

- The handoff has one explicit semantic input.
- Validation and publication judgment are complete before published-content mutation.
- Pipeline write ownership and application read ownership are explicit.
- Publication cannot expose mixed content, provenance, or availability.
- A concurrent application read observes one complete publication state.
- Withdrawal may change availability without deleting current content or replacing provenance.
- Current provenance remains reachable through an opaque reference.
- Application code need not interpret pipeline source, model, prompt, gate, or validation details.
- The ADR requirement judgment is explicit.
- PRODUCT-TASK-APPLICATION-002-04 has sufficient inputs to reflect both owning contract sides.

## Verification

- Trace each handoff element to PRODUCT-TASK-APPLICATION-002-02 and the accepted ADRs.
- Check initial publication, replacement, and withdrawal against the resolved projection invariants.
- Check that application reads cannot require pipeline-internal joins or processing-data interpretation.
- Check that consistency language describes observable behavior rather than a transaction mechanism.
- Confirm that source reuse and retention choices are backed by an accepted ADR.
- Confirm that any new architectural decision has an accepted ADR before task completion.

## Evidence

### Result

- **Verdict**: PASS.
- The semantic publication handoff and observable consistency guarantees are resolved.
- The handoff design exposed a new source-reuse and retention decision.
- PRODUCT-ADR-PIPELINE-005 records and accepts that decision.
- PRODUCT-TASK-APPLICATION-002-04 owns specification reflection.

### Accepted decision sources

- PRODUCT-ADR-APPLICATION-001 assigns published-area writes to the pipeline and reads to the application.
- PRODUCT-ADR-APPLICATION-001 requires atomic replacement of content, provenance reference, and resulting availability.
- PRODUCT-ADR-APPLICATION-001 requires concurrent reads to observe one complete publication.
- PRODUCT-ADR-PIPELINE-005 requires completed automated publication judgment before availability.
- PRODUCT-ADR-PIPELINE-005 defines source reuse and current-only first-MVP retention.

### Semantic handoff input

```text
PublicationHandoff
  +-- stable_learning_unit_id
  +-- learning_unit
  +-- provenance_ref
  +-- resulting_availability
```

- `stable_learning_unit_id` identifies the unit anchored to one valid learning path.
- `learning_unit` is one complete unit under `spec:product.learning.learning_unit`.
- Attribution remains inside `learning_unit` and is not a duplicate handoff element.
- `provenance_ref` identifies current pipeline-owned evidence and remains opaque to application logic.
- `resulting_availability` is the explicit result of the completed publication judgment.
- The handoff is semantic and does not select a command, event, request body, or storage schema.

### Preconditions

- The learning unit is complete and structurally valid.
- Required source references and learner-visible attribution are present.
- Mechanical validation is complete.
- Model-based quality judgment is complete when required by publication policy.
- One publication judgment has produced the resulting availability.
- Current provenance is established before the published projection changes.
- A failed precondition produces no partial published-content mutation.

### Pipeline writer obligations

- The pipeline is the only semantic owner of published-area writes.
- Initial publication writes one complete projection.
- Replacement under the same stable identity switches content, matching provenance, and publication-judged availability together.
- Replacement does not create another current projection or sibling learning unit.
- An availability-only withdrawal changes availability without replacing content or provenance.
- The pipeline need not retain historical source snapshots, intermediate generations, previous publications, exact replay data, or rollback state.

### Application reader obligations

- The application reads only the published-content projection.
- The application does not interpret pipeline source, model, prompt, validation, or processing-data structures.
- Queue creation uses only currently available unit identities.
- Retrieval rechecks current availability.
- An unavailable or missing identity returns an unavailable result.

### Observable consistency

- A read concurrent with initial publication observes either no current projection or one complete projection.
- A read concurrent with replacement observes either the previous complete projection or the new complete projection.
- A read must not observe partial learning-unit content.
- A read must not observe content paired with a mismatched provenance reference.
- A read must not observe replacement content with an availability value from a different publication judgment.
- The contract does not require a particular database transaction or isolation mechanism.

### Provenance boundary

- The application treats `provenance_ref` as opaque.
- The reference must reach current pipeline-owned source and generation evidence.
- Current evidence may use retained source data previously fetched for the same source URL.
- Provenance reachability does not imply historical generations or source freshness guarantees.

### ADR judgment

The projection and writer-reader obligations detail PRODUCT-ADR-APPLICATION-001.
The source-reuse and retention boundary reverses earlier pipeline retention decisions.
PRODUCT-ADR-PIPELINE-005 supersedes PRODUCT-ADR-PIPELINE-001 and PRODUCT-ADR-PIPELINE-004 while carrying their active pipeline decisions forward.

### T04 inputs

PRODUCT-TASK-APPLICATION-002-04 must:

- treat PRODUCT-ADR-PIPELINE-005 as the current pipeline decision;
- reflect the semantic handoff on the pipeline-owned side of `spec:product.pipeline`;
- reflect projection and read guarantees in `spec:product.application.published_content`;
- keep attribution meaning owned by `spec:product.learning.learning_unit`;
- preserve loaded-copy behavior owned by `spec:product.ui.learning_flow`;
- remove duplicated or historical-retention language outside the accepted first-MVP scope.
