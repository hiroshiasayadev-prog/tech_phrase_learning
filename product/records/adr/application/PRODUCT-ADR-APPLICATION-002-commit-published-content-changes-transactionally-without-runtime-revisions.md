# PRODUCT-ADR-APPLICATION-002: Commit published-content changes transactionally without runtime revisions

- **status**: superseded
- **date**: 2026-06-26
- **depends_on**: [PRODUCT-ADR-APPLICATION-001, PRODUCT-ADR-PIPELINE-005]
- **supersedes**: []
- **migrated_to_spec**:

## Context

PRODUCT-ADR-APPLICATION-001 established a current published-content boundary and required publication changes to avoid exposing partial content.

Its wording described application reads in terms of a previous complete publication or a new complete publication.
That wording implies runtime revision states and a defined overlap between publication writes and learner retrieval.

The first MVP does not require runtime publication revisions, revision selection, or application behavior defined around concurrent publication and retrieval.
The pipeline owns published-content changes and can commit each change transactionally.

## Decision

Published content has one current runtime state per stable learning-unit identity.
The runtime contract does not model previous and new publication revisions.

The pipeline must apply each published-content change inside one transaction.
The transaction must commit the complete resulting current state together, including:

- complete learning-unit content when content changes;
- current availability;
- the matching opaque provenance reference.

A failed transaction must leave the previously committed current state unchanged.
No partial published-content state may become visible to application reads.

Application retrieval reads only committed current published content.
Concurrent overlap between a publication transaction and one retrieval operation is not a product-level semantic scenario for the first MVP.
The application contract therefore does not define a choice between previous and new revisions.

The first MVP does not expose or require:

- runtime publication revision identity;
- previous-publication or next-publication result variants;
- revision tokens;
- revision selection;
- optimistic revision comparison;
- runtime publication history;
- rollback behavior.

This decision replaces only the previous/new publication observation language in PRODUCT-ADR-APPLICATION-001.
All other ownership, published-boundary, availability, retrieval, and PWA-state decisions in PRODUCT-ADR-APPLICATION-001 remain accepted.

## Rationale

A transactional write boundary is sufficient to prevent partial runtime data.
Runtime revision semantics would add concepts that have no first-MVP consumer.

The pipeline needs provenance for generation traceability and maintenance.
The learner-facing application and PWA do not need publication revision information.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Model retrieval as returning either a previous or new publication | Introduces runtime revision concepts that the first MVP does not use. |
| Expose a publication revision to the application or PWA | Neither runtime layer has revision-dependent behavior. |
| Define application behavior for retrieval overlapping an active publication write | Transactional publication removes partial visibility; explicit overlap semantics add unnecessary contract surface. |
| Allow content, availability, and provenance to commit independently | Application reads could observe an invalid or mismatched current state. |

## Consequences

- Pipeline publication implementation requires a transaction around each published-content change.
- Application retrieval reads one committed current state.
- Runtime specifications must not describe previous and new publication revisions.
- Runtime retrieval results must not include revision metadata.
- Transaction syntax, database product, and isolation configuration remain implementation details.
- PRODUCT-TASK-APPLICATION-004-02 must define retrieval without previous/new publication result cases.
- PRODUCT-TASK-APPLICATION-004-04 must reconcile PRODUCT-ADR-APPLICATION-001 and affected specifications.

## Evidence

- The first MVP keeps only current published runtime content.
- No learner-facing requirement consumes publication revision identity or history.
- The pipeline already owns publication writes and provenance.
- The accepted product decision requires pipeline publication changes to use a transaction and excludes concurrent publication/retrieval overlap from the product-level retrieval model.
