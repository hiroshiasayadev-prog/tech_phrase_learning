# Concept: Answered card

- **id**: `spec:product.ui.components.answered_card`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.ui.components`

## What this is

Completed form of one learning interaction.
The card keeps the source-post summary visible and places answer information in a collapsible detail region.

## Non-goals

- Raw source-post display.
- Per-option explanations.
- Animation and collapse implementation.
- Persistent expansion state.

## Concept model

### Newest answered card

```text
+--------------------------------------------------------+
| Answered card                                         |
|--------------------------------------------------------|
| <source-post summary remains visible>                 |
|                                                        |
| +----------------------------------------------------+ |
| | Correct / Incorrect                               | |
| |                                                   | |
| | Prompt                                            | |
| | <original intent prompt>                          | |
| |                                                   | |
| | Correct phrase                                    | |
| | <target quiz phrase>                              | |
| +----------------------------------------------------+ |
|                                         [ Continue ]  |
+--------------------------------------------------------+
```

### Earlier answered card

```text
+--------------------------------------------------------+
| Answered card                                         |
|--------------------------------------------------------|
| <source-post summary remains visible>                 |
|                                                        |
| [ Answer detail: closed ]                             |
+--------------------------------------------------------+
```

### Final answered card

```text
+--------------------------------------------------------+
| Final answered card                                   |
|--------------------------------------------------------|
| <source-post summary remains visible>                 |
|                                                        |
| +----------------------------------------------------+ |
| | Correct / Incorrect                               | |
| | Prompt                                            | |
| | Correct phrase                                    | |
| +----------------------------------------------------+ |
|                                                        |
| Source: <attribution>                                  |
|                              [ Next discussion ]       |
+--------------------------------------------------------+
```

## Rules

- Answering must replace the quiz card for the same interaction.
- The source-post summary must remain outside the collapsible detail region.
- The newest answered card must initially keep its detail open.
- The newest answered card must remain open until the learner continues.
- Earlier answered cards may open or close their answer details.
- Earlier-card expansion must remain presentation state outside `Session`.
- A non-final newest card must show `Continue`.
- The final card must show attribution and `Next discussion`.
- The final card must not lead to a separate completion screen.

## Boundary

| concern | owner |
|---|---|
| Visible answered-card composition | `spec:product.ui.components.answered_card` |
| Summary, result, phrase, and attribution meaning | `spec:product.learning.quiz_session` |
| Continue and next-discussion transitions | `spec:product.ui.learning_flow` |
| Expansion mechanics and styling | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.ui.components` | Parent component overview. |
| `spec:product.ui.pages.learning_page` | Shows answered cards in the learning-page stack. |
| `spec:product.ui.components.quiz_card` | Precedes the answered form of the same interaction. |
| `spec:product.learning.quiz_session` | Defines answered-card semantics. |
