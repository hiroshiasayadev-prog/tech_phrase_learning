# PRODUCT-ADR-APPLICATION-004: Return availability results from the published-unit retrieval port

- **status**: accepted
- **date**: 2026-06-26
- **depends_on**: [PRODUCT-ADR-APPLICATION-003]
- **supersedes**: []
- **migrated_to_spec**: 2026-06-26

## Context

PRODUCT-ADR-APPLICATION-003 defines `Available(complete_learning_unit) | Unavailable` as the normal retrieval result.

The application requires an outbound port to retrieve one published learning unit by stable reference.

The remaining boundary question is where committed availability becomes the normal retrieval result.

The persistence adapter already owns reading committed published content through application-owned outbound contracts.

## Decision

The application owns a semantic outbound retrieval port.

The port accepts one stable `LearningUnitRef`.

The port returns one normal result:

```text
Available(complete_learning_unit)
| Unavailable
```

The persistence adapter implements the outbound retrieval port.

The persistence adapter must:

- read the committed current published state for the supplied reference;
- read the committed availability value;
- return `Available(complete_learning_unit)` when current content exists and is available;
- return `Unavailable` when no current state exists;
- return `Unavailable` when current content exists but is unavailable;
- map persisted complete content into the learning-unit contract;
- keep provenance inside the published-content and pipeline boundary;
- propagate mapping and infrastructure failures as technical failures.

The persistence adapter does not decide whether a learning unit should be available.

The pipeline owns the availability decision and stores its result during publication or availability change.

The application use case coordinates the outbound port result.

The application use case does not receive a published projection containing separate content, availability, and provenance fields.

The PWA receives the application result through a later transport boundary.

The concrete port name, programming-language interface, persistence technology, query, and transport mapping remain implementation details.

## Rationale

The persistence adapter already reads the stored current state and availability.

Returning the application result avoids leaking persistence projection structure into application orchestration.

The application still owns the port contract because the application defines the capability it requires.

The adapter only translates the committed pipeline decision into that contract.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Return the full published projection to the application use case | The use case does not need provenance or separate persistence fields. |
| Let the application use case inspect stored availability | The persistence adapter already reads and maps the stored current state. |
| Let the persistence adapter decide availability policy | Availability policy belongs to the pipeline publication decision. |
| Convert mapping or infrastructure failures to `Unavailable` | Technical failure must remain distinct from a normal availability outcome. |

## Consequences

- The outbound retrieval port is result-shaped rather than projection-shaped.
- Persistence adapter contract tests must cover available, missing, unavailable, mapping-failure, and infrastructure-failure cases.
- Application tests may use a test double that returns the semantic result directly.
- Normal application orchestration does not depend on provenance or persistence projection fields.
- PRODUCT-TASK-APPLICATION-004-04 must reflect this decision in current application specifications.

## Evidence

- The root application responsibility assigns committed published-content reads to the persistence adapter.
- The user confirmed that database reading and committed-availability mapping both belong to the persistence adapter.
- PRODUCT-ADR-APPLICATION-003 assigns availability decisions and publication integrity to the pipeline.
