# Concept: Quiz card

- **id**: `spec:product.ui.components.quiz_card`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.ui.components`

## What this is

Active card for one unanswered learning interaction.
The card presents the intent prompt, three options, and the discussion-skip action.

## Non-goals

- Quiz-content generation.
- Option scoring policy.
- Per-option explanations.
- Concrete button styling and keyboard behavior.

## Concept model

```text
+--------------------------------------------------------+
| Quiz                                                   |
|--------------------------------------------------------|
| <intent prompt>                                        |
|                                                        |
| [A] <natural English option>                           |
|                                                        |
| [B] <natural English option>                           |
|                                                        |
| [C] <natural English option>                           |
|                                                        |
| [ Skip this discussion ]                               |
+--------------------------------------------------------+
```

```text
select A, B, or C
        |
        v
same interaction becomes an Answered card
```

## Rules

- The quiz card must represent the current interaction only.
- The quiz card must show exactly three answer options.
- The quiz card must not show the source-post summary.
- The quiz card must not reveal the correct option.
- Selecting an option must replace the card with its answered form.
- Selecting an option must not advance the interaction index.
- Skip must leave the discussion without revealing unanswered content.
- Skip must start next-unit loading without an intermediate skipped view.

## Boundary

| concern | owner |
|---|---|
| Visible quiz-card composition | `spec:product.ui.components.quiz_card` |
| Prompt, option, and correct-answer meaning | `spec:product.learning.learning_unit` |
| Answer and skip transitions | `spec:product.ui.learning_flow` |
| Concrete controls and accessibility implementation | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.ui.components` | Parent component overview. |
| `spec:product.ui.pages.learning_page` | Places the quiz card after earlier answered cards. |
| `spec:product.ui.components.answered_card` | Replaces the quiz card after an answer. |
| `spec:product.learning.quiz_session` | Defines progressive quiz semantics. |
