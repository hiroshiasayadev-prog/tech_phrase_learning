# PRODUCT-TASK-APPLICATION-001-06: Integrate and review application design

- **id**: PRODUCT-TASK-APPLICATION-001-06
- **status**: not_started
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-001
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 2d
- **depends_on**: [PRODUCT-TASK-APPLICATION-001-04, PRODUCT-TASK-APPLICATION-001-05]
- **outputs**: []

## Goal

Integrate the focused module designs and determine whether application design is ready for implementation planning.

## Work

1. Read PRODUCT-WORK-APPLICATION-001 and the child work items recorded by T01 through T05.
2. Require each child work item to be `done` or explicitly deferred with a non-blocking reason.
3. Read all ADRs and specs created or changed by the child work items.
4. Build one cross-module ownership and dependency check.
5. Reconcile duplicated or contradictory contracts only when an accepted ADR authorizes the normative change.
6. Stop and create decision follow-up work when an accepted ADR is missing.
7. Confirm that unresolved implementation choices remain outside the specification boundary.
8. Request an independent review of the integrated application design.
9. Apply specification corrections only from accepted ADRs or create follow-up work items for unresolved gaps.
10. Record implementation work-item candidates without starting implementation.
11. Update PRODUCT-WORK-APPLICATION-001 evidence and completion state when all conditions are satisfied.

Required integration checks:

- Pipeline owns publication decisions and published-area writes.
- Application reads only the published-content boundary.
- Published content and availability remain separate.
- Published-content changes commit one complete current state transactionally.
- Application provenance remains opaque.
- Queue creation returns at most 100 unique available references.
- Queue generation creates no reservation or backend queue state.
- Retrieval rechecks current availability.
- `Unavailable` remains distinct from mapping, infrastructure, and retryable failures.
- The PWA owns queue position and learner session state.
- Loaded content is not revoked from an active learner flow.
- Ports are application-owned and implemented by adapters.
- Application domain rules remain independent from frameworks and persistence.

Implementation-planning output categories:

- application domain and use cases;
- published-content writer on the pipeline side;
- persistence adapters and storage model;
- PWA-facing transport adapter;
- PWA integration;
- architecture, contract, and integration tests.

## Done condition

- Every focused module work item is resolved or explicitly deferred without blocking implementation planning.
- Application, pipeline, learning, and UI specs contain consistent ownership and result semantics.
- All normative specification changes trace to accepted ADRs.
- No task or work-item evidence acts as design authority.
- An independent review records `PASS` or all blocking findings are resolved.
- PRODUCT-REQ-APPLICATION-001 required outcomes are satisfied at the design level.
- Implementation work-item candidates are recorded separately from this design hub.
- PRODUCT-WORK-APPLICATION-001 contains final evidence and can be marked `done`.

## Verification

- Validate H1, metadata, canonical refs, reciprocal workflow links, and required sections for all new records.
- Review cross-area dependency direction against `spec:product` and PRODUCT-ADR-APPLICATION-003.
- Confirm superseded ADR bodies remain historical and unchanged except for lifecycle status.
- Check that no detailed design depends on pipeline internal artifact structures.
- Check that no implementation progress or concrete technology choice was placed in an ADR or spec without a dedicated decision.
- Record the independent review verdict and addressed findings in `## Evidence`.

## Evidence

TBD
