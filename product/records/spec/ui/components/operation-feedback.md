# Concept: Operation feedback

- **id**: `spec:product.ui.components.operation_feedback`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.ui.components`

## What this is

Visible feedback for learning-unit loading and request failure.
The feedback remains attached to the current stable page.

## Non-goals

- Backend error classification.
- Retry delay algorithms.
- Global notification design.
- Logging and diagnostics.

## Concept model

### Main-page loading

```text
[ Start ] disabled

Loading discussion...
```

### Learning-page loading

```text
Current quiz or final answered card remains visible.

Loading next discussion...
[ initiating action ] disabled
```

### Failure

```text
Current stable page remains visible.

Could not load the discussion.  [ Retry ]
```

### Attempt flow

```text
initial attempt
  -> automatic retry 1
  -> automatic retry 2
  -> automatic retry 3
  -> error + manual Retry
```

## Rules

- Loading feedback must appear on the current stable page.
- The initiating action must remain disabled during loading.
- The UI must perform three automatic retries after the initial attempt.
- Failed attempts must not advance the queue or replace the session.
- Final failure must show a manual retry action.
- Manual retry must preserve the current stable page.
- `Back to main` must remain available on the learning page.

## Boundary

| concern | owner |
|---|---|
| Visible loading and failure feedback | `spec:product.ui.components.operation_feedback` |
| State replacement and retry count | `spec:product.ui.learning_flow` |
| Transport errors | Future backend or application contract. |
| Exact copy, indicators, and animation | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.ui.components` | Parent component overview. |
| `spec:product.ui.pages.main_page` | Uses feedback while loading the first unit. |
| `spec:product.ui.pages.learning_page` | Uses feedback while replacing the current unit. |
| `spec:product.ui.learning_flow` | Defines loading and retry behavior. |
