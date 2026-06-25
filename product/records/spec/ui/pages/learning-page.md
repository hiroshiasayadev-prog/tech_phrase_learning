# Concept: Learning page

- **id**: `spec:product.ui.pages.learning_page`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.ui.pages`

## What this is

Single page for presenting one learning unit and moving through the transient queue.
The page keeps the current unit visible until replacement content loads successfully.

## Non-goals

- A separate completion page.
- A skipped page.
- Topic or discussion selection controls.
- Concrete card dimensions and animation.

## Concept model

### Active quiz

```text
+------------------------------------------------------------+
| All shuffle · <discussion title>          [ Back to main ] |
+------------------------------------------------------------+
|                                                            |
| Earlier answered cards may appear above the quiz.        |
| +--------------------------------------------------------+ |
| | Answered card                                         | |
| | Source-post summary                                   | |
| | [ Answer detail: closed ]                             | |
| +--------------------------------------------------------+ |
|                                                            |
| +--------------------------------------------------------+ |
| | Quiz                                                   | |
| | <intent prompt>                                        | |
| |                                                        | |
| | [A] <option>                                           | |
| | [B] <option>                                           | |
| | [C] <option>                                           | |
| |                                                        | |
| | [ Skip this discussion ]                               | |
| +--------------------------------------------------------+ |
|                                                            |
+------------------------------------------------------------+
```

### Answered interaction

```text
+------------------------------------------------------------+
| All shuffle · <discussion title>          [ Back to main ] |
+------------------------------------------------------------+
|                                                            |
| +--------------------------------------------------------+ |
| | Answered card                                         | |
| | Source-post summary                                   | |
| |                                                        | |
| | +----------------------------------------------------+ | |
| | | Correct / Incorrect                               | | |
| | | Prompt                                             | | |
| | | Correct phrase                                     | | |
| | +----------------------------------------------------+ | |
| |                                         [ Continue ]  | |
| +--------------------------------------------------------+ |
|                                                            |
+------------------------------------------------------------+
```

### Final answered interaction

```text
+------------------------------------------------------------+
| All shuffle · <discussion title>          [ Back to main ] |
+------------------------------------------------------------+
|                                                            |
| +--------------------------------------------------------+ |
| | Final answered card                                   | |
| | Source-post summary                                   | |
| |                                                        | |
| | +----------------------------------------------------+ | |
| | | Correct / Incorrect                               | | |
| | | Prompt                                             | | |
| | | Correct phrase                                     | | |
| | +----------------------------------------------------+ | |
| |                                                        | |
| | Source attribution                                     | |
| |                              [ Next discussion ]       | |
| +--------------------------------------------------------+ |
|                                                            |
+------------------------------------------------------------+
```

### Loading the next unit

```text
+------------------------------------------------------------+
| All shuffle · <current discussion>        [ Back to main ] |
+------------------------------------------------------------+
|                                                            |
| Current quiz or final answered card remains visible.       |
|                                                            |
|                         Loading next discussion...          |
|                         [ initiating action ] disabled      |
|                                                            |
+------------------------------------------------------------+
```

### Error after automatic retries

```text
+------------------------------------------------------------+
| All shuffle · <current discussion>        [ Back to main ] |
+------------------------------------------------------------+
|                                                            |
| Current card remains visible.                              |
|                                                            |
| Could not load the next discussion.          [ Retry ]     |
|                                                            |
+------------------------------------------------------------+
```

## Rules

| current view | action or result | resulting view |
|---|---|---|
| Active quiz | Select an option. | Answered interaction for the same card. |
| Answered non-final interaction | Select `Continue`. | Active quiz for the next interaction. |
| Active quiz | Select `Skip this discussion`. | Load the next unit on the same page. |
| Final answered interaction | Select `Next discussion`. | Load the next unit on the same page. |
| Any learning view | Select `Back to main`. | Main page with queue and session discarded. |
| Next-unit loading | Load succeeds. | New active quiz with a new session. |
| Next-unit loading | All automatic retries fail. | Current card plus error and manual retry. |

- The top bar must remain visible during the learning flow.
- Earlier source-post summaries must remain visible.
- Only answer details may collapse.
- The page must not show a separate terminal state.
- Loading must not remove the current learning unit.
- `Back to main` must remain available during loading and error states.

## Boundary

| concern | owner |
|---|---|
| Page assembly and visible states | `spec:product.ui.pages.learning_page` |
| Card content meaning | `spec:product.learning.quiz_session` |
| Queue and session transitions | `spec:product.ui.learning_flow` |
| Individual visual parts | `spec:product.ui.components` |
| Concrete scrolling and responsive layout | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.ui.pages` | Parent page overview. |
| `spec:product.ui.learning_flow` | Defines runtime state and transitions. |
| `spec:product.ui.components.top_bar` | Defines the persistent learning header. |
| `spec:product.ui.components.quiz_card` | Defines active quiz composition. |
| `spec:product.ui.components.answered_card` | Defines answered and final-card composition. |
| `spec:product.ui.components.operation_feedback` | Defines loading and error feedback. |
