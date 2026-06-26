# PRODUCT-ADR-APPLICATION-001: Separate published runtime content from pipeline internals

- **status**: accepted
- **date**: 2026-06-26
- **depends_on**: [PRODUCT-ADR-LEARNING-005, PRODUCT-ADR-PIPELINE-005, PRODUCT-ADR-UI-001]
- **supersedes**: []
- **migrated_to_spec**: 2026-06-26

## Context

The pipeline generates, validates, and publishes learning units before learner use.
The PWA owns transient queue and session state.

The remaining runtime boundary must select available units and return complete learning-unit content.
The boundary must not expose pipeline intermediate artifacts to the PWA or application use cases.

The first MVP may use one physical database for pipeline and runtime data.
A shared database must not make pipeline internal structures part of the runtime contract.

Availability may change after a queue is issued.
Published content may also be regenerated for the same stable learning-unit identity.

## Decision

Create a top-level `application` specification area.
The area owns runtime selection, availability-aware retrieval, application use cases, and outbound query ports.

The first MVP may use one physical database with two semantic areas:

- pipeline internal data;
- published runtime content.

The pipeline owns generation, validation, publication decisions, and writes to the published area.
The application reads only the published area.
The application must not depend on pipeline internal artifact structures.

The published area will separate current learning-unit content from mutable availability.
Unavailable content will retain source attribution and an opaque provenance reference.

The pipeline may replace current published content under the same stable learning-unit identity.
The replacement must atomically switch content, provenance reference, and resulting availability.
The application must observe either the previous complete publication or the new complete publication.

A learning unit loaded into the PWA remains immutable for that learner flow.
A later publication replacement does not mutate the already loaded copy.

The application will expose two semantic use cases:

- `CreateCompleteShuffleQueue`;
- `GetPublishedLearningUnit`.

The first MVP complete-shuffle queue will use all available units as its selection scope.
The queue will contain at most 100 unique learning-unit references.
The same learning unit may appear again in a later queue.

The database adapter will perform bounded random selection efficiently.
The domain layer will own the selection invariants rather than the concrete randomization algorithm.

Learning-unit retrieval will recheck current availability.
An unavailable or missing reference will produce an unavailable result.
The PWA will skip that queue entry and continue with the next reference.

A queue does not reserve availability.
A learning unit already loaded by the PWA will not be forcibly removed after withdrawal.

The application will treat provenance as an opaque reference.
Pipeline-specific model, prompt, validation, and source-snapshot details remain pipeline-owned.

The dependency direction will be:

```text
adapter -> application -> domain
```

The application may depend on learning contracts.
The application must not depend on pipeline internals.

## Rationale

A semantic published-content boundary allows one physical database without coupling runtime reads to pipeline implementation tables.

Separating content from availability preserves current content while allowing reversible selection changes.

A bounded queue avoids transferring or retaining every available reference as the corpus grows.
The PWA can still own queue position without backend session state.

Database-side sampling avoids loading the complete candidate set into the domain layer.
Domain-owned invariants keep infrastructure choices from defining selection semantics.

Opaque provenance references preserve traceability without importing pipeline-specific version models into the application.

Atomic publication replacement prevents mixed content and provenance from becoming visible to runtime queries.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Let the application read pipeline intermediate artifacts directly | Pipeline schema changes would become runtime contract changes. |
| Use separate physical databases as a mandatory boundary | Physical separation is not required to preserve semantic ownership. |
| Route publication writes through application commands | The pipeline already owns publication judgment and no additional application decision is required. |
| Return every available learning-unit reference in one queue | Queue size would grow with the corpus and add unnecessary transfer and client state. |
| Keep published revisions under separate runtime identities | The first MVP does not require runtime revision history or rollback. |
| Put all selection behavior inside application use cases | Selection invariants would become harder to extend and test independently. |
| Shuffle the full candidate set inside the domain layer | Full candidate loading would couple clean layering to inefficient execution. |
| Expose detailed pipeline provenance fields in the application model | The application would depend on pipeline-specific artifact and version structures. |

## Consequences

- `spec:product.application` becomes the owner of runtime selection and retrieval contracts.
- The pipeline must write a stable published-content projection after publication decisions.
- The application requires semantic query ports over the published area.
- The PWA remains the owner of queue position and learner session progress.
- Queue issuance creates no reservation, token, or server-side queue state.
- Availability is checked during both queue creation and learning-unit retrieval.
- HTTP routes, response schemas, database tables, and randomization algorithms remain implementation work.
- Future source, topic, discussion, or difficulty scopes can extend the selection scope without moving queue state to the backend.

## Evidence

- PRODUCT-ADR-LEARNING-005 requires session-time selection of available pre-generated learning units.
- PRODUCT-ADR-PIPELINE-005 assigns generation, validation, publication gating, source reuse, and current provenance retention to the pipeline.
- PRODUCT-ADR-UI-001 assigns transient `LearningQueue` and `Session` state to the PWA.
- The accepted architecture discussion selected a shared physical database with separate pipeline-internal and published-content boundaries.
