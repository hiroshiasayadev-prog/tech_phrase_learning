# PRODUCT-ADR-APPLICATION-003: Consolidate current published-content and retrieval boundary

- **status**: accepted
- **date**: 2026-06-26
- **depends_on**: [PRODUCT-ADR-LEARNING-005, PRODUCT-ADR-PIPELINE-005, PRODUCT-ADR-UI-001]
- **supersedes**: [PRODUCT-ADR-APPLICATION-001, PRODUCT-ADR-APPLICATION-002]
- **migrated_to_spec**: 2026-06-26

## Context

PRODUCT-ADR-APPLICATION-001 established the application and published-content boundary.

PRODUCT-ADR-APPLICATION-002 replaced previous and new publication wording with transactional current-state publication.

The two ADRs leave the current decision split across records.

The retrieval work also requires explicit result terminology and integrity ownership.

## Decision

Create one current published-content boundary for learner runtime reads.

The first MVP may use one physical database for pipeline and runtime data.

The physical database must preserve two semantic areas:

- pipeline processing data;
- current published runtime content.

The pipeline owns generation, validation, publication decisions, and published-content writes.

The application reads only committed current published content.

The application must not read or interpret pipeline processing data.

One stable learning-unit identity addresses at most one current published state.

The current published state contains:

- one complete learning unit;
- current availability;
- one matching opaque provenance reference.

The pipeline must validate the complete published state before mutation.

The pipeline must commit each published-content change inside one transaction.

A failed transaction must leave the previously committed current state unchanged.

The runtime contract does not model previous or new publication revisions.

The runtime contract does not expose revision identities, tokens, history, selection, or rollback.

The application exposes these semantic use cases:

- `CreateCompleteShuffleQueue`;
- `GetPublishedLearningUnit`.

The first MVP queue uses all currently available units.

One queue contains at most 100 unique stable learning-unit references.

Queue creation creates no reservation or backend learner state.

Learning-unit retrieval rechecks current availability.

The normal retrieval result is:

```text
Available(complete_learning_unit)
| Unavailable
```

`Available` means the current published unit is available to a new learner flow.

`Unavailable` covers a missing stable reference or a currently unavailable published state.

`Unavailable` is not an infrastructure or data-integrity failure.

The complete learning unit contains learner-visible attribution.

Normal retrieval does not return provenance, availability metadata, queue metadata, or pipeline processing data.

The opaque provenance reference remains pipeline-owned traceability information.

The PWA owns queue position, loaded content, session state, retry behavior, and unavailable-reference skipping.

A loaded learning unit remains immutable under the UI contract.

The application retains no learner-specific loaded-copy state.

Published-content integrity validation belongs to the pipeline before commit.

The application may assume committed published content satisfies the published contract.

A persistence mapping failure indicates technical data corruption or adapter failure.

A persistence mapping failure must not become `Available` or `Unavailable`.

This ADR does not decide the exact outbound query-port result shape.

A later ADR must decide whether the persistence adapter returns a retrieval result or a published projection to application code.

## Rationale

One current-state model matches the first-MVP retention policy.

Transactional writes prevent partial published states without runtime revision semantics.

Availability-based result names distinguish learner usability from storage existence.

Pipeline-side validation keeps publication integrity with the writer that creates the state.

Opaque provenance preserves operational traceability without coupling learner runtime to pipeline internals.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Model previous and new runtime publications | The first MVP has no revision consumer. |
| Return `Found(complete_learning_unit)` | `Found` describes existence rather than learner availability. |
| Return provenance to the PWA | Learner runtime does not consume pipeline traceability. |
| Convert malformed published content to `Unavailable` | Data corruption must not look like a normal availability decision. |
| Revalidate complete learning-unit integrity in the application | Publication integrity belongs to the pipeline writer before commit. |
| Store queue position or learner session state in the backend | PRODUCT-ADR-UI-001 assigns transient learner-flow state to the PWA. |

## Consequences

- PRODUCT-ADR-APPLICATION-001 and PRODUCT-ADR-APPLICATION-002 are superseded.
- Current specifications must migrate to this ADR before changing retrieval contracts.
- Specifications must remove previous and new runtime publication language.
- Specifications must replace `Found` with `Available`.
- Normal learner retrieval must exclude provenance.
- Pipeline publication planning must include validation before one transactional commit.
- Application adapter planning must preserve technical failure separation.
- A separate ADR remains required for the outbound retrieval-port shape.

## Evidence

- The user selected `Available` because unavailable content may still exist in persistence.
- The user assigned published-content consistency validation to the pipeline.
- The user required transaction-backed published-content changes.
- PRODUCT-ADR-PIPELINE-005 owns current-only pipeline retention and publication decisions.
- PRODUCT-ADR-UI-001 owns transient queue and learner session state.
