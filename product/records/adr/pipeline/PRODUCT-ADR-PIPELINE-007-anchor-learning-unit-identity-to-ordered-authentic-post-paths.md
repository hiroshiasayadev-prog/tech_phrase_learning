# PRODUCT-ADR-PIPELINE-007: Anchor learning-unit identity to ordered authentic-post paths

- **status**: accepted
- **date**: 2026-06-27
- **depends_on**:
  - PRODUCT-ADR-PIPELINE-005
  - PRODUCT-ADR-PIPELINE-006
  - PRODUCT-ADR-LEARNING-005
  - PRODUCT-ADR-APPLICATION-003
- **supersedes**:
- **migrated_to_spec**: 2026-06-28

## Context

PRODUCT-ADR-LEARNING-005 defines one valid Learning Path as the identity source for one Learning Unit.
Generated-content changes must not create sibling Learning Units.

The Pipeline still needs identity inputs for valid paths and replacement semantics for current generated content.

The decision must not select hashes, UUIDs, database keys, or serialized identifier shapes.
The decision must also preserve the Application current-state boundary.

## Decision

Valid Learning Path identity will use:

- the authentic discussion identity;
- the ordered authentic-post identities in the valid path.

Post order is part of path identity.
A different ordered post sequence defines a different valid Learning Path.

The following values are not valid-path or Learning Unit identity inputs:

- reusable or path-specific summaries;
- target phrases;
- quiz prompts;
- answer options;
- provider identity;
- prompt provenance;
- validator provenance;
- generated-content values.

Each valid Learning Path will materialize exactly one stable Learning Unit identity.

Regeneration will replace current generated content under the same stable Learning Unit identity.
Regeneration will not create a sibling Learning Unit.
The first MVP will not expose a Learning Unit revision identity.

The Pipeline will not require a separate generated-content instance identity.

A current-content replacement must update these values as one atomic semantic change:

- the complete current Learning Unit content;
- the matching current opaque provenance reference;
- the resulting current availability when publication changes it.

Partial replacement is invalid.
A failed replacement must leave the previous committed current state unchanged.

Concrete transaction syntax, persistence layout, identifier encoding, and isolation mechanism remain implementation concerns.

## Rationale

Ordered authentic-post identity distinguishes different paths from the same discussion.
The identity remains independent from generated content that may improve over time.

One stable Learning Unit identity preserves continuity across provider, prompt, validator, and content changes.

Avoiding a generated-content instance identity keeps the first-MVP current-only model simple.
Atomic replacement prevents summaries, quizzes, and provenance from different generations from becoming one visible unit.

The decision matches the Application contract without exposing runtime revisions.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Include generated summaries or quiz content in path identity | Regeneration would create a different logical Learning Unit. |
| Use only the discussion identity | One discussion may produce several independently valid Learning Paths. |
| Ignore post order in path identity | Different conversational sequences could collapse into one identity. |
| Create a new Learning Unit for every generation | The first MVP requires current replacement, not sibling revisions. |
| Introduce a generation-instance identity | No first-MVP runtime consumer requires generation history or selection. |
| Replace generated fields independently | Partial replacement could mix content and provenance from different processing results. |
| Select UUID, hash, or composite-string encoding now | Concrete representation remains an implementation choice. |

## Consequences

- T03 may materialize candidate and valid-path references from ordered authentic-post identities.
- T04 must generate all path-scoped summaries, phrases, and quizzes for the identified valid path.
- T05 must produce a complete current-state handoff rather than field-level publication changes.
- Application receives one stable Learning Unit reference and one matching opaque provenance reference.
- Provider, prompt, validator, and generated-content changes do not change logical Learning Unit identity.
- Historical generation retention, rollback, and runtime revision selection remain outside the first MVP.
- T07 must reflect path identity and replacement continuity into focused Pipeline specifications.

## Evidence

- PRODUCT-TASK-PIPELINE-001-01 identified valid-path identity and generated-content replacement as missing Pipeline authority.
- PRODUCT-ADR-LEARNING-005 anchors one logical Learning Unit to one valid Learning Path.
- PRODUCT-ADR-APPLICATION-003 requires one committed current state per stable Learning Unit identity.
- The user selected authentic discussion identity plus ordered authentic-post identities as valid-path identity inputs.
- The user selected one stable Learning Unit identity per valid path.
- The user rejected a separate generated-content instance identity and required transactional complete replacement.
