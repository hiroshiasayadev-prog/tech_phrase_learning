# PRODUCT-TASK-PIPELINE-001-05: Define publication gate and output contracts

- **id**: PRODUCT-TASK-PIPELINE-001-05
- **status**: not_started
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PIPELINE-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 2.5d
- **depends_on**:
  - PRODUCT-TASK-PIPELINE-001-04
- **outputs**: []

## Goal

Define publication-gate approval, eligibility, rejection, withdrawal, provenance, and published-content output contracts.

## Work

1. Read the fixed Learning publication-readiness contract and Application published-content boundary.
2. Define structural readiness inputs and complete-scope coverage obligations.
3. Define semantic readiness inputs for every non-compensating Learning quality dimension.
4. Require failure of any required dimension to block publication.
5. Define internally contradictory validation results as rejection outcomes.
6. Define human approval of criteria, representative golden fixtures, harder fixtures, and material criteria changes.
7. Define gate-configuration validation before unattended publication eligibility.
8. Define borderline-policy escalation without creating a routine per-unit human queue.
9. Define publication decisions for available, rejected, unavailable, and withdrawn outcomes.
10. Define current publication-decision provenance and its opaque external reference.
11. Define `PublicationHandoff` inputs, preconditions, outputs, and failure behavior.
12. Define `AvailabilityChange` inputs, preconditions, outputs, and failure behavior.
13. Require complete committed current-state production and atomic replacement.
14. Require availability-only mutation to preserve content and provenance.
15. Require the complete unit payload to remain immutable for Application readers.
16. Preserve Pipeline writer and Application reader ownership separation.
17. Create or update Pipeline ADRs when current authority does not determine observable gate or publication semantics.
18. Keep transaction syntax, database design, thresholds, routes, and serialization outside the contract.
19. Update `outputs` and Evidence with accepted ADRs or specification inputs.

## Done condition

- Structural and semantic gate inputs are explicit and cover the complete unit.
- Every required quality dimension is non-compensating.
- Contradictory results reject publication.
- Human criteria, fixture, configuration, and material-change approval boundaries are explicit.
- Unattended publication eligibility has explicit evidence conditions.
- Rejection, unavailability, withdrawal, and restoration outcomes are explicit.
- Publication-decision provenance is Pipeline-owned and externally opaque.
- `PublicationHandoff` and `AvailabilityChange` have complete semantic contracts.
- Initial publication and replacement produce one committed complete current state.
- Availability-only changes preserve current content and provenance.
- Failed preconditions and failed writes cannot expose partial state.
- Every new normative decision has accepted Pipeline ADR authority.
- Application read semantics remain unchanged.

## Verification

- Trace gate dimensions to `spec:product.learning.learning_unit` without restating their meaning.
- Confirm model success alone cannot pass the gate.
- Confirm representative harder fixtures are required before unattended publication approval.
- Confirm replacement does not create a sibling learning unit or another current projection.
- Confirm unavailability preserves content, source references, attribution, and current provenance.
- Confirm `LearningUnitRef` and Application results expose no Pipeline provenance.
- Run relevant record validation, strict specification validation, `git diff --check`, and `git status --short`.

## Evidence

TBD
