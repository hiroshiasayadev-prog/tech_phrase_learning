# PRODUCT-ADR-APPLICATION-006: Define learning-unit reference interface semantics

- **status**: accepted
- **date**: 2026-06-27
- **depends_on**:
  - PRODUCT-ADR-APPLICATION-003
- **supersedes**:
- **migrated_to_spec**: 2026-06-27

## Context

`CreateCompleteShuffleQueue` returns ordered `LearningUnitRef` values.

`GetPublishedLearningUnit` accepts one `LearningUnitRef`.

Current authority defines stable learning-unit identity but does not fully define how the PWA may handle the reference between these operations.

The PWA requires enough semantic guarantees to retain, compare, and pass references without depending on their representation.

The interface must preserve those guarantees without selecting a wire format or persistence identity.

## Decision

`LearningUnitRef` is the shared application-level reference type used by queue creation and learning-unit retrieval.

A `LearningUnitRef` stably identifies the published learning-unit identity it addresses.

The PWA must treat each `LearningUnitRef` as opaque.

The PWA may retain a `LearningUnitRef` as transient queue state.

The PWA may compare two `LearningUnitRef` values for equality.

Equality means that both values address the same published learning-unit identity.

The PWA must pass a queued `LearningUnitRef` unchanged to `GetPublishedLearningUnit`.

The application interface must not require the PWA to parse, normalize, enrich, or reinterpret a `LearningUnitRef`.

A `LearningUnitRef` does not expose:

- pipeline provenance;
- database identity or schema;
- queue identity or position;
- learner progress;
- availability state;
- publication revision information.

Reference stability does not guarantee that the addressed learning unit remains available.

Retrieval must continue to recheck current availability under PRODUCT-ADR-APPLICATION-003.

The concrete wire representation of `LearningUnitRef` remains deferred.

This decision does not select a string, integer, UUID, composite key, encoded token, or transport field shape.

## Rationale

One shared semantic reference type keeps queue creation and retrieval aligned.

Opaque handling prevents the PWA from depending on persistence or pipeline internals.

Equality comparison supports queue management without exposing reference structure.

Unchanged pass-through keeps reference interpretation inside the application boundary.

Deferring the wire representation preserves transport independence.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Expose database primary keys directly | Persistence identity would become part of the PWA-facing product contract. |
| Let the PWA parse structured reference fields | Reference structure would become a frontend dependency. |
| Use different reference types for queue creation and retrieval | The PWA would need an additional conversion contract. |
| Include availability in the reference | Availability is mutable and must be rechecked during retrieval. |
| Select a concrete serialized representation now | Transport and serialization remain outside the current design scope. |

## Consequences

- Queue creation and retrieval must use the same semantic `LearningUnitRef` type.
- PWA queue state may retain and compare references without interpreting them.
- Future transport adapters must preserve reference identity across serialization and deserialization.
- Future implementations may choose a concrete representation without changing this decision when the semantic guarantees remain intact.
- Specifications must keep availability, provenance, queue state, and persistence identity outside `LearningUnitRef`.
- PRODUCT-TASK-APPLICATION-006-03 may use this ADR as reference-semantics authority after T006-02 closes.

## Evidence

- PRODUCT-REQ-APPLICATION-003 records the need for complete PWA-facing `LearningUnitRef` guarantees.
- PRODUCT-TASK-APPLICATION-006-01 identifies opaque handling, equality comparison, and unchanged pass-through as genuine decision gaps.
- PRODUCT-ADR-APPLICATION-003 establishes stable learning-unit identity and retrieval-time availability checks.
- Current selection and retrieval specifications already use `LearningUnitRef` on both sides of the PWA interaction.
- The user selected stable, opaque, equality-comparable, unchanged pass-through semantics and deferred the wire representation.
