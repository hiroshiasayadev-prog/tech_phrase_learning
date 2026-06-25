# PRODUCT-ADR-UI-001: Keep first-MVP learner-flow state in the PWA

- **status**: accepted
- **date**: 2026-06-25
- **depends_on**: [PRODUCT-ADR-LEARNING-005, PRODUCT-ADR-LEARNING-006]
- **supersedes**: []
- **migrated_to_spec**: 2026-06-25

## Context

The learning contract defines progressive quiz-to-summary presentation over one published learning unit.

The first MVP uses a PWA frontend and a separate backend.
The first MVP does not require durable learner progress, session recovery, or learner history.

The UI still needs explicit ownership for temporary progress within one learning unit.
The UI also needs temporary ordering state across several shuffled learning units.

Mixing these concerns into the learning specifications would combine product semantics with concrete runtime behavior.
Assigning them to the backend would add session identity, cleanup, and recovery concerns without first-MVP value.

## Decision

Create a top-level `ui` specification area.
The area owns PWA screen flow, transient learner-flow state, and operation feedback.

The PWA will own two separate transient state concepts:

- `LearningQueue` identifies the ordered learning-unit references used by the current shuffle run.
- `Session` records progress within exactly one loaded learning unit.

A loaded learning unit remains immutable content.
A `Session` references that content and does not own a copied learning-unit model.

The `Session` will not have a session identifier.
The `Session` will not provide durability or reload recovery.

The `Session` will record:

- the current learning-unit reference;
- the current interaction index;
- the selected option identifier for each answered interaction;
- a `quiz` or `answered` phase.

Answering changes the current interaction from `quiz` to `answered`.
Continuing from a non-final answered interaction advances the interaction index and returns to `quiz`.

Answer-detail expansion for earlier cards remains local presentation state.
The expansion state is not part of `Session` progress.

Skipping from an active quiz immediately begins the transition to the next learning unit.
The UI will not show a skipped state or skipped screen.

The final answered card will contain attribution and a `Next discussion` action.
The UI will not show a separate completion screen.

`LearningQueue` will advance only after the next learning unit loads successfully.
The current answered card will remain visible while the next unit loads.

The UI will retry a failed learning-unit request three times after the initial attempt.
After all attempts fail, the current screen will show an error and a manual retry action.

The main screen will initially expose one complete-shuffle start action.
The UI will stay on the main screen while the first learning unit loads.

The learning screen will show a persistent top bar with the shuffle mode, current discussion title, and a `Back to main` action.
Returning to the main screen will discard the current queue and session without confirmation.
Reloading the PWA may also discard both states.

## Rationale

PWA ownership matches the temporary lifetime of the first-MVP learner flow.
The decision avoids backend session management before durable progress is required.

Separating `LearningQueue` from `Session` keeps cross-unit ordering independent from within-unit progression.
Separating immutable learning content from mutable session state prevents learner actions from changing published content.

Keeping the current screen until the next unit loads avoids pointing the UI at content that is not available yet.
The same rule also provides a stable retry surface after request failure.

A separate completion screen adds an unnecessary action between the final answered card and the next discussion.

A dedicated `ui` area keeps runtime behavior traceable without placing implementation state inside the learning concept model.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Store first-MVP session state in the backend | The MVP does not require recovery, history, or cross-device continuity. |
| Combine queue state and within-unit progress | The states have different lifecycles and transition rules. |
| Copy learning-unit content into `Session` ownership | Published content and learner progress have different responsibilities. |
| Add a durable or generated session identifier | The identifier has no first-MVP consumer. |
| Persist state in `sessionStorage` | Reload recovery is outside the first-MVP scope. |
| Show a skipped screen | Skip means immediately leave the current discussion. |
| Show a separate completion screen | The final answered card can contain attribution and the next-discussion action. |
| Put concrete PWA runtime behavior under `learning` | The learning area owns product meaning rather than frontend state ownership. |

## Consequences

- `spec:product.ui` becomes the owner of PWA runtime behavior.
- `spec:product.learning` remains the owner of learner-visible content meaning and progression semantics.
- Backend selection, queue production, availability, API, and repository contracts remain undecided.
- The frontend can test learner-flow transitions without persistence or provider infrastructure.
- A later progress feature will require a new decision about durable session identity and ownership.
- The current quiz-session specification must not require a separate terminal screen.

## Evidence

- PRODUCT-ADR-LEARNING-005 defines published learning units as pre-generated content.
- PRODUCT-ADR-LEARNING-006 defines the final answered card with a next-discussion control.
- The accepted first-MVP scope excludes progress persistence and learner history.
- The reviewed UI design separated `LearningQueue`, `Session`, immutable learning-unit content, and card expansion state.
