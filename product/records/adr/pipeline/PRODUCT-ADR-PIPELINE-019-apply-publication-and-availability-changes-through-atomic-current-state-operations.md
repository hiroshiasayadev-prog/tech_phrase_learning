# PRODUCT-ADR-PIPELINE-019: Apply publication and availability changes through atomic current-state operations

- **status**: accepted
- **date**: 2026-06-28
- **depends_on**:
  - PRODUCT-ADR-PIPELINE-007
  - PRODUCT-ADR-PIPELINE-008
  - PRODUCT-ADR-PIPELINE-017
  - PRODUCT-ADR-PIPELINE-018
  - PRODUCT-ADR-APPLICATION-003
- **supersedes**:
- **migrated_to_spec**:

## Context

The Pipeline must write complete current published state without exposing partial replacement to Application readers.

PRODUCT-ADR-PIPELINE-007 requires complete content, matching provenance, and publication-judged availability to change atomically under one stable Learning Unit identity.
PRODUCT-ADR-PIPELINE-018 distinguishes complete publication replacement from availability-only withdrawal and restoration.

The Application contract requires at most one committed current state for each stable identity.
Application readers must observe only complete committed state.

The Pipeline therefore needs semantic contracts for `PublicationHandoff` and `AvailabilityChange`.
The contracts must define inputs, preconditions, outputs, failure behavior, and ownership without selecting persistence technology.

## Decision

### PublicationHandoff

`PublicationHandoff` will introduce the first current published state or replace the complete current published state for one stable Learning Unit identity.

Its semantic input will contain:

- stable Learning Unit identity;
- one complete Learning Unit;
- one opaque provenance reference;
- resulting availability of `available` or `unavailable`.

The handoff preconditions are:

- the Learning Unit is complete;
- content-validation completion is established;
- the publication gate accepted the candidate;
- every required structural and semantic readiness condition passed;
- one complete matching current provenance bundle exists;
- the opaque provenance reference identifies that bundle;
- identity, content, provenance, and decision targets agree;
- resulting availability matches the Pipeline publication decision.

A successful initial handoff will produce exactly one complete committed current state.
A successful replacement will atomically replace complete content, matching provenance reference, and resulting availability under the same stable identity.
Replacement will not create a sibling Learning Unit or a second current projection.

A failed precondition will produce no published-content mutation.
A failed initial write will leave no current state.
A failed replacement will leave the previous complete committed current state unchanged.
No partial or mixed content-and-provenance state may become observable.

### AvailabilityChange

`AvailabilityChange` will change only the availability of one existing complete current published state.

Its semantic input will contain:

- stable Learning Unit identity;
- resulting availability of `available` or `unavailable`.

The change preconditions are:

- exactly one complete current published state exists for the stable identity;
- one Pipeline-owned availability decision exists;
- the decision target matches the input identity;
- the requested availability differs from the committed current value;
- no contradictory decision evidence remains.

A successful withdrawal will change `available` to `unavailable`.
A successful restoration will change `unavailable` to `available`.

An availability-only change will preserve:

- the complete Learning Unit content;
- interaction order;
- source references and source evidence;
- learner-visible attribution;
- the current provenance bundle;
- the opaque provenance reference;
- the stable Learning Unit identity.

A missing current state, no-op requested value, failed precondition, or failed write will produce no mutation.
The previous complete committed current state will remain unchanged.
`AvailabilityChange` will not create a new current state or introduce changed content.
Changed or new content must use `PublicationHandoff`.

### Atomic current-state replacement

Each successful operation will expose one observable committed state transition.
Application readers may observe only the previous complete state or the new complete state.
They must not observe an in-progress or partial mutation.

Initial publication and replacement will commit every field of complete current state together.
Availability-only mutation will commit only the availability change while preserving all other current values.

Transaction syntax, locking, isolation level, persistence layout, and storage technology remain implementation concerns.

### Writer and reader ownership

Pipeline will own:

- publication-gate execution;
- `rejected`, `withdrawn`, and `restored` decisions;
- `PublicationHandoff` and `AvailabilityChange` initiation;
- current provenance bundles and opaque provenance references;
- published current-state mutation;
- mutation preconditions and atomic complete-state replacement.

Application will own:

- reads of committed current published state;
- interpretation of `available` and `unavailable`;
- available-unit selection;
- availability recheck during retrieval;
- return of one complete Learning Unit.

Application will not reevaluate publication readiness, inspect validation results, parse Pipeline provenance, interpret rejection causes, or repair partial state.
Pipeline will not own queue construction, runtime selection, `LearningUnitRef` consumption, or Application read-result semantics.

Shared physical persistence is allowed.
Application contracts will not depend on Pipeline processing schemas or internal validation data.

## Rationale

Complete-state handoff prevents content and provenance from different decisions from becoming one runtime unit.
Stable identity replacement preserves one logical Learning Unit across regeneration.

Availability-only mutation supports withdrawal and restoration without repeating content publication or changing content evidence.

Failing without mutation preserves the last valid committed state.
The semantic atomicity requirement permits different persistence implementations while protecting Application reads.

Writer and reader separation keeps publication authority in Pipeline and runtime interpretation in Application.
Shared storage does not require shared semantic ownership.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Publish fields independently | Application readers could observe incomplete or mismatched state. |
| Create a sibling Learning Unit for replacement content | Generated-content changes must preserve stable Learning Unit identity. |
| Use `AvailabilityChange` to introduce content | Availability-only mutation cannot establish complete content and provenance. |
| Replace provenance during withdrawal or restoration | Availability changes do not change the content-generation evidence. |
| Remove the current state after a failed replacement | The previous complete committed state remains valid until a successful replacement. |
| Let Application perform publication checks | Publication readiness and write authority belong to Pipeline. |
| Couple Application reads to Pipeline processing data | Runtime consumers must depend only on the published-content boundary. |
| Select database transaction syntax in this decision | Concrete persistence mechanics remain implementation choices. |

## Consequences

- Initial publication and replacement use `PublicationHandoff`.
- Withdrawal and same-content restoration use `AvailabilityChange`.
- Replacement preserves stable identity and produces only one current projection.
- Availability-only changes preserve content, source evidence, attribution, and provenance.
- Failed preconditions and failed writes leave committed current state unchanged.
- Application readers observe only complete committed state.
- Pipeline and Application may share physical persistence without sharing internal contracts.
- T06 may define execution, retry, batching, and rerun behavior without changing these operation meanings.
- T07 must reflect handoff, availability, atomicity, and ownership contracts into focused Pipeline specifications.
- Concrete database, transaction, route, and serialization design remain deferred.

## Evidence

- PRODUCT-ADR-PIPELINE-007 establishes stable Learning Unit identity and atomic complete replacement.
- PRODUCT-ADR-PIPELINE-008 establishes current provenance and availability-only version-targeted withdrawal.
- PRODUCT-ADR-PIPELINE-017 establishes publication-gate acceptance prerequisites.
- PRODUCT-ADR-PIPELINE-018 establishes outcome meanings and opaque provenance boundaries.
- PRODUCT-ADR-APPLICATION-003 establishes one committed current state per stable identity and Application read isolation.
- The user approved the `PublicationHandoff`, `AvailabilityChange`, atomicity, preservation, and writer-reader ownership contracts.
