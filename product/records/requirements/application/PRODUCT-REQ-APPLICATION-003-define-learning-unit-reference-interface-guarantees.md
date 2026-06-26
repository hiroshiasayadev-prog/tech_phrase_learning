# PRODUCT-REQ-APPLICATION-003: Define learning-unit reference interface guarantees

- **id**: PRODUCT-REQ-APPLICATION-003
- **status**: accepted
- **date**: 2026-06-27
- **source_refs**:
  - PRODUCT-REQ-APPLICATION-001
  - PRODUCT-TASK-APPLICATION-006-01
  - PRODUCT-ADR-APPLICATION-003
  - spec:product.application.learning_unit_selection
  - spec:product.application.learning_unit_retrieval
- **work_items**:

## Requirement

The PWA-facing application interface requires stable semantic guarantees for `LearningUnitRef` values.

The guarantees must allow a reference returned by queue creation to be retained and supplied unchanged to learning-unit retrieval.

The interface must preserve reference abstraction without committing to a concrete wire representation.

## Evidence

PRODUCT-TASK-APPLICATION-006-01 confirmed that stable reference identity is already present in current application contracts.

The same inventory identified opaque handling, equality comparison, and unchanged pass-through as unresolved normative decisions.

Current specifications do not define the complete PWA-facing reference contract.

## Required Outcome

- `LearningUnitRef` remains stable for the published learning-unit identity it addresses.
- The PWA treats `LearningUnitRef` as opaque.
- The PWA may compare two `LearningUnitRef` values for equality.
- The PWA passes a queued `LearningUnitRef` unchanged to learning-unit retrieval.
- Queue creation and retrieval use the same semantic reference type.
- Reference semantics do not expose pipeline provenance, database identity, or mutable queue position.
- The concrete wire representation remains deferred.
- An accepted APPLICATION ADR authorizes these guarantees before specification reflection.

## Explicitly Excluded Scope

- String, integer, UUID, composite-key, or encoded wire representation.
- JSON field names and serialization rules.
- Database primary keys and persistence schemas.
- Reference generation algorithms.
- URL structure and transport routing.
- Queue identity, reservation, backend position, and learner progress.

## Boundary

This requirement owns PWA-facing `LearningUnitRef` semantics shared by queue creation and retrieval.

Persistence identity and transport serialization remain implementation concerns.
