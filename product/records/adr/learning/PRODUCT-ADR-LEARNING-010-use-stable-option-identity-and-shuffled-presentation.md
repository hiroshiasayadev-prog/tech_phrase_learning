# PRODUCT-ADR-LEARNING-010: Use stable option identity and shuffled presentation

- **status**: accepted
- **date**: 2026-06-27
- **depends_on**: [PRODUCT-ADR-LEARNING-005, PRODUCT-ADR-LEARNING-006]
- **supersedes**: []
- **migrated_to_spec**: null

## Context

Every first-MVP interaction contains exactly three answer options and exactly one correct option.

The current Learning contract does not define stable option identity.
The UI must retain the learner's selected option and derive correctness from immutable learning-unit content.

Recorded quiz-generation experiments used option IDs `A`, `B`, and `C`.
Both reviewed topic `107844` outputs placed the preferred option first as option `A`.
The experiment prompt also encoded the preferred option first in its output example.

Presenting generated order directly would allow option position to reveal the correct answer pattern.
Using display labels, array positions, or option text as identity would also couple learner-answer state to presentation details.

## Decision

Every answer option will have one stable semantic identity within its interaction in the current published learning-unit content.

Each interaction will contain one correct-option reference that identifies exactly one option by semantic identity.

Option identity will not be derived from:

- generated array position;
- learner-visible `A`, `B`, or `C` labels;
- current display order;
- option text.

The first-MVP learner session will present the three options in a shuffled order for each interaction.

One display permutation will be selected when the interaction first becomes active.
The selected permutation will remain stable for that interaction until the current learning-unit session ends.

The UI domain owns permutation generation, storage, and restoration mechanics.

Learner-visible labels such as `A`, `B`, and `C` may be assigned after shuffling.
The labels identify display positions only and do not identify semantic options.

The learner's answer state will retain the selected semantic option identity.
Correctness will compare that identity with the interaction's correct-option reference.

Option identities do not need to remain stable across replacement of the current published learning-unit content.
Concrete identifier values, wire representation, and shuffle algorithms remain implementation choices.

## Rationale

Stable semantic identity lets the UI retain an answer without depending on presentation order or wording.

Shuffling prevents a generation convention such as "the first option is correct" from becoming a learner-visible answer pattern.

Keeping one permutation stable prevents options from moving after rerendering, answer selection, or card replacement.

Interaction-local identity is sufficient for first-MVP answer state.
Cross-publication identity would add lifecycle complexity without current value.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Use array index as option identity | Shuffling or reordering would change the meaning of stored learner answers. |
| Use `A`, `B`, or `C` as semantic identity | Display labels change when options are shuffled. |
| Use option text as identity | Wording may change and duplicate text cannot be ruled out safely. |
| Preserve generated order in the learner session | Recorded experiments place the preferred option first and would create a position bias. |
| Reshuffle on every render | Moving options would make the interaction unstable and could confuse the learner. |
| Require identity stability across published-content replacement | The first MVP does not retain learner progress or publication revision history. |

## Consequences

- `spec:product.learning.learning_unit` must require one identity per option and one correct-option reference per interaction.
- Option identity must be unique within its interaction.
- Generated order and display order must remain non-semantic.
- `spec:product.learning.quiz_session` must require one stable shuffled permutation per active interaction.
- `spec:product.ui.learning_flow` must consume the selected semantic option identity and stable-permutation constraint.
- UI-owned state must preserve the chosen permutation while the interaction remains in the current session.
- Pipeline output may place the correct option first, but published content must not rely on position for correctness.
- Transport and persistence contracts must preserve option identity and correct-option reference without prescribing their concrete encoding.

## Evidence

- `spec:product.ui.learning_flow` currently requires the session to retain each selected option identifier.
- `topic-107844-medium.json` records the preferred option as the first option with ID `A`.
- `topic-107844-high.json` records the preferred option as the first option with ID `A`.
- `prompt-v4-current.md` shows the preferred option first in the expected output shape.
- The user selected stable semantic option identity and required learner-visible option shuffling.
