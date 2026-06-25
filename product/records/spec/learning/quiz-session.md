# Concept: Quiz session

- **id**: `spec:product.learning.quiz_session`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.learning`

## What this is

Learner-visible interaction contract for presenting one available learning unit.
The session progressively replaces each active quiz card with an answered summary card.

## Non-goals

- Learning-unit selection algorithms.
- Account and learner-history behavior.
- Source ingestion and quiz generation mechanics.
- Session-state persistence technology.
- Concrete component technology, layout measurements, and styling.
- Raw source-post display.
- Unrestricted generated chat.

## Concept model

### Pages

| page | purpose | required action |
|---|---|---|
| Introduction | Starts a learning session without configuration. | Start a discussion. |
| Learning session | Presents one available learning unit as progressive cards. | Answer, continue, skip, or start the next discussion. |

### Session elements

| element | meaning |
|---|---|
| Answered card | A completed interaction that always shows its source-post summary. |
| Answer detail | A collapsible region containing the result, prompt, and correct phrase. |
| Active quiz card | The only interaction that currently accepts a learner answer. |
| Question interaction | An active quiz linked to the source discussion opening post. |
| Reply interaction | An active quiz linked to one later source reply. |
| Continue action | Replaces a non-final completed step with the next active quiz card. |
| Skip action | Leaves the current discussion without completing its remaining quizzes. |
| Next discussion action | Leaves the final answered card and starts another discussion through the UI flow. |

### Card transition

| current state | learner action | resulting state |
|---|---|---|
| Hidden interaction | Continue from the preceding answered card. | Active quiz card. |
| Active quiz card | Select one answer option. | Open answered card. |
| Open newest answered card | Continue. | The card becomes collapsible and the next interaction becomes active. |
| Earlier answered card | Open or close its answer detail. | Answered card with unchanged summary. |
| Final open answered card | Next discussion. | The current unit ends without a separate terminal screen. |

## Rules

### Session composition

- A session must use exactly one session-available learning unit.
- A session must follow the learning unit's one valid source-post path.
- The session must contain one interaction for every selected source post.
- The first interaction must be a question interaction.
- At least one later interaction must be a reply interaction.
- Interaction order must preserve source-post order.
- The session must not generate a new learning unit at session start.

### Progressive presentation

- The session may show zero or more answered cards and one active quiz card.
- Only the active quiz card may accept a learner answer.
- A later interaction must remain hidden until the learner continues from the current answered card.
- Answering must replace the active quiz card with one answered card for the same source post.
- The newest answered card must initially remain open.
- The newest answered card must remain open until the learner continues.
- Earlier answered cards may open or close their answer details.
- Closing an answered card must not hide its source-post summary.
- The accumulated summaries provide conversation context for the active quiz.

### Active quiz card

- The active quiz card must show the quiz prompt.
- The active quiz card must show exactly three answer options.
- The active quiz card must not show the source-post summary before the learner answers.
- The active quiz card must not identify the correct option before the learner answers.
- The active quiz card must provide a control to skip the current discussion.

### Answered card

- The answered card must show the source-post summary outside the collapsible answer detail.
- The open answer detail must show whether the learner was correct.
- The open answer detail must show the original quiz prompt.
- The open answer detail must show the target quiz phrase as the correct phrase.
- Only a non-final newest answered card may show the continue action.
- The continue action must lead to the next interaction.

### Final answered card

- The final answered card must provide source attribution.
- The final answered card must provide a `Next discussion` action.
- The session must not require a separate terminal screen.
- Skipping must leave the current discussion without exposing unanswered summaries or correct phrases.

### Language boundary

- All learner-facing prompts, options, summaries, results, labels, and controls must be English.

## Boundary

| concern | owner |
|---|---|
| Valid path and path-to-unit relationship | `spec:product.learning.learning_path` |
| Meaning of quiz prompts, options, phrases, and summaries | `spec:product.learning.learning_unit` |
| Card order and learner-visible transitions | `spec:product.learning.quiz_session` |
| Runtime learning-unit selection | `spec:product.application.learning_unit_selection`. |
| PWA runtime state, loading, retry, and navigation | `spec:product.ui.learning_flow` |
| Session-state persistence | Out of scope for the first MVP. |
| Package generation and validation | `spec:product.pipeline` |
| Visual styling and responsive layout | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.learning` | Parent learning overview. |
| `spec:product.learning.learning_path` | Defines the source-post path presented by the session. |
| `spec:product.learning.learning_unit` | Defines content shown within each card. |
| `spec:product.pipeline` | Produces the ordered content consumed by the session. |
| `spec:product.application.learning_unit_selection` | Selects and retrieves the available unit used by the session. |
| `spec:product.ui.learning_flow` | Implements the transient PWA flow for this session contract. |
| PRODUCT-ADR-LEARNING-005 | Establishes the current summarized learning-unit model. |
| PRODUCT-ADR-LEARNING-006 | Establishes progressive quiz-to-summary card behavior. |
