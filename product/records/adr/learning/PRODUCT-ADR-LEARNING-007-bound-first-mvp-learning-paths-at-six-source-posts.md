# PRODUCT-ADR-LEARNING-007: Bound first-MVP learning paths at six source posts

- **status**: accepted
- **date**: 2026-06-27
- **depends_on**: [PRODUCT-ADR-LEARNING-005]
- **supersedes**: []
- **migrated_to_spec**: 2026-06-27

## Context

PRODUCT-ADR-LEARNING-005 defines one valid source-post path as the identity source for one learning unit.

A valid first-MVP path must begin with the opening post and include at least one authentic reply.
The minimum path length is therefore two selected source posts.

The current Learning specification sets a maximum of six selected source posts.
No accepted Learning ADR currently authorizes that maximum.

Longer paths increase session duration and the number of required quiz interactions.
Excessive length may weaken repeated phrase exposure by increasing fatigue within one discussion.

## Decision

A valid first-MVP learning path will contain two to six ordered source-post references.

The lower bound requires:

- one opening post;
- at least one authentic reply.

The upper bound limits one learning unit to six learner interactions.

The Learning domain owns this first-MVP cardinality because path length directly constrains learner-session scope.

The Pipeline must produce only first-MVP path candidates within this cardinality.
Path enumeration and filtering mechanics remain Pipeline concerns.

A later change to the maximum requires a new Learning decision.

## Rationale

Two posts provide the minimum complete question-and-reply exchange.

Six posts allow several related conversational turns without making one discussion excessively long.
The bound limits learner fatigue and keeps one session focused.

Learning ownership prevents processing convenience from silently changing learner-session length.
The Pipeline can still choose shorter valid paths when they satisfy Learning suitability criteria.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Define no concrete Learning-owned maximum | Pipeline policy could change learner-session length without a Learning decision. |
| Use a maximum below six posts | The smaller bound may remove useful multi-turn exchanges without current evidence that six is excessive. |
| Use a maximum above six posts | Longer sessions increase fatigue risk and are not required for the first MVP. |

## Consequences

- `spec:product.learning.learning_path` must retain the two-to-six cardinality.
- `spec:product.learning.learning_unit` must contain two to six interactions because every selected post has one interaction.
- `spec:product.learning.quiz_session` must present two to six ordered interactions for one learning unit.
- Pipeline path enumeration and validation must enforce the accepted bounds.
- The bound does not require every path to contain six posts.
- Path suitability, coherence, and independent validity remain separate requirements.

## Evidence

- PRODUCT-ADR-LEARNING-005 establishes one interaction per selected source post and one unit per valid path.
- PRODUCT-ADR-LEARNING-006 establishes progressive presentation across the selected source posts.
- PRODUCT-INV-PIPELINE-002 used bounded root-starting paths of two to six posts as its investigated first-MVP range.
- The user adopted six posts as the first-MVP maximum to avoid excessively long and tiring discussions.
