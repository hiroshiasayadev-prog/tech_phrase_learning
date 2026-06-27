# PRODUCT-ADR-PIPELINE-018: Record current publication outcomes and expose only opaque provenance references

- **status**: accepted
- **date**: 2026-06-28
- **depends_on**:
  - PRODUCT-ADR-PIPELINE-005
  - PRODUCT-ADR-PIPELINE-008
  - PRODUCT-ADR-PIPELINE-017
  - PRODUCT-ADR-APPLICATION-003
- **supersedes**:
- **migrated_to_spec**:

## Context

The Pipeline must distinguish publication decisions from Application-visible availability.
The first MVP also needs current evidence explaining why committed content received its publication state.

PRODUCT-ADR-PIPELINE-008 establishes one Pipeline-owned current provenance bundle and one opaque Application-facing reference.
It leaves publication outcomes, withdrawal, restoration, and publication-decision evidence to T05.

The Application contract interprets only `available` and `unavailable`.
Application code and the PWA must not depend on Pipeline validation, model, prompt, version, or decision internals.

## Decision

### Outcome meanings

`available` and `unavailable` will remain current published-state values.
`rejected`, `withdrawn`, and `restored` will be Pipeline decision outcomes or transitions.
They will not become additional Application-visible availability values.

| term | meaning |
|---|---|
| `available` | The committed current Learning Unit may enter new queues and new learner flows. |
| `unavailable` | The committed current Learning Unit remains retained but cannot enter new queues or new learner flows. |
| `rejected` | The current publication candidate or requested change is not adopted. The committed current state remains unchanged. |
| `withdrawn` | An existing committed current state changes from `available` to `unavailable`. |
| `restored` | An existing committed current state changes from `unavailable` to `available` without content or provenance replacement. |

A rejected initial publication will create no current published state.
A rejected replacement will preserve the previous committed current state.
A rejected availability change will preserve the previous committed availability.

Withdrawal will preserve current content, source references, source evidence, attribution, and current provenance.
Restoration without content change will preserve current content and provenance.
Republication with changed content will use complete publication replacement rather than availability-only restoration.

The Application will continue to interpret only `available` and `unavailable`.
Pipeline decision causes and transition labels will remain Pipeline-owned.

### Current publication provenance

Each committed current published Learning Unit will have one matching Pipeline-owned current provenance bundle.

The bundle will retain:

- retained authentic-source and valid Learning Path references;
- current generation-stage evidence;
- stage-specific provider, prompt, and validator provenance;
- Source Adapter Version;
- Common Pipeline Version;
- structural readiness results;
- all required semantic readiness results;
- the gate configuration used for the decision;
- golden- and harder-fixture validation evidence for that configuration;
- the publication-gate result that established the current content;
- the availability selected by that publication decision.

Concrete provenance schema, identifier encoding, and persistence layout remain implementation choices.

### Opaque external reference

Application-facing current published state will contain one opaque provenance reference.
The reference will identify the current Pipeline provenance bundle that matches the committed content.

Application code and the PWA will not:

- parse the reference;
- interpret Pipeline evidence;
- expose provider, prompt, validator, or version data;
- use provenance for runtime selection or retrieval decisions;
- include provenance in `LearningUnitRef`.

A content introduction or replacement will replace the complete content, matching current provenance bundle, opaque provenance reference, and resulting availability together.
A state containing content and provenance from different publication decisions is invalid.

An availability-only withdrawal or restoration will preserve the complete content, current provenance bundle, and opaque provenance reference.
Pipeline will retain separate internal evidence for the current availability decision.
That evidence will not replace the provenance bundle for the unchanged content.

A rejected unpublished candidate may retain Pipeline-internal rejection evidence.
It will not create Application-facing current publication provenance or an opaque current-state reference.

## Rationale

Separating state values from decision outcomes keeps the Application contract stable.
The Application needs current eligibility rather than Pipeline decision history.

One current provenance bundle keeps source, generation, validation, gate configuration, publication outcome, and current content aligned.

An opaque reference permits current-state integrity without coupling Application code to Pipeline internals.
Preserving the reference during availability-only changes keeps content provenance stable.

Rejected candidates are not current publications.
Keeping rejection evidence internal avoids exposing failed processing artifacts as runtime state.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Add `rejected`, `withdrawn`, and `restored` as Application availability values | The Application needs current eligibility, not Pipeline decision history. |
| Remove content during withdrawal | Withdrawal must preserve source routes, attribution, and current evidence. |
| Replace content provenance during availability-only changes | The content-generation evidence has not changed. |
| Expose Pipeline provenance fields through `LearningUnitRef` | Runtime consumers must not depend on Pipeline internals. |
| Give rejected candidates opaque current-state references | Rejected candidates have no committed current published state. |
| Retain every historical publication provenance bundle | The first MVP requires current provenance, not runtime revision history. |

## Consequences

- Application-visible availability remains limited to `available` and `unavailable`.
- Pipeline retains distinct rejected, withdrawn, and restored decision evidence.
- Each committed current content projection has one matching current provenance bundle and opaque reference.
- Availability-only changes preserve content provenance and its opaque reference.
- Current availability-decision evidence remains Pipeline-owned and separate from unchanged content provenance.
- Application and PWA behavior remain independent from Pipeline evidence structure.
- PRODUCT-ADR-PIPELINE-019 must preserve these outcome and provenance boundaries during writes.
- T07 must reflect current outcome and opaque-provenance contracts into focused Pipeline specifications.
- Concrete provenance storage, serialization, and identifier formats remain deferred.

## Evidence

- PRODUCT-ADR-PIPELINE-005 requires unavailability to preserve current content, source references, attribution, and current publication provenance.
- PRODUCT-ADR-PIPELINE-008 establishes one current Pipeline provenance bundle and one opaque Application-facing reference.
- PRODUCT-ADR-APPLICATION-003 establishes one current published state and Application-side provenance opacity.
- PRODUCT-ADR-PIPELINE-017 establishes the publication-gate evidence retained by current provenance.
- The user approved the outcome meanings, current provenance contents, opaque-reference boundary, and availability-only provenance preservation.
