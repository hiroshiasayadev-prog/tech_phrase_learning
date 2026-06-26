# Concept: Operation feedback

- **id**: `spec:product.ui.components.operation_feedback`
- **status**: draft
- **date**: 2026-06-27
- **parent**: `spec:product.ui.components`

## What this is

Visible feedback for loading, retryable infrastructure failure, and non-retryable application failures.
Each feedback state appears on the owning page defined by `spec:product.ui.learning_flow`.

## Non-goals

- Application failure-category meaning and retryability classification.
- Retry delay algorithms.
- Global notification design.
- Logging implementation and unsafe diagnostic detail.

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

### Infrastructure failure after automatic retries

```text
Owning page remains visible.

Could not load the discussion.  [ Retry ]
```

### Initial non-retryable failure

```text
Main page remains visible.

<safe diagnostic information>
```

### Replacement non-retryable failure

```text
Current learning page remains visible.

<safe diagnostic information>
[ Back to main ]
```

### Retrieval mapping failure

```text
Learning flow ends.
Queue and session are discarded.
Main page shows <safe diagnostic information>.
```

### Infrastructure-failure attempt flow

```text
initial attempt
  -> InfrastructureFailure
  -> automatic retry 1
  -> automatic retry 2
  -> automatic retry 3
  -> error + manual Retry
```

## Rules

- Loading feedback must appear on the current stable page.
- The initiating action must remain disabled during loading.
- Automatic and manual retry feedback applies only to `InfrastructureFailure`.
- One initial attempt and three automatic retries apply to each retryable operation.
- Failed infrastructure attempts must not advance the queue or replace the session.
- Exhausted infrastructure retries must show a manual `Retry` action on the owning page.
- Manual retry must preserve the state defined by `spec:product.ui.learning_flow`.
- Initial `MappingFailure` and `InvalidSelectionResult` must remain on the main page.
- Initial non-retryable failures must show safe diagnostic information without a retry action.
- Replacement `MappingFailure` and `InvalidSelectionResult` must remain on the learning page.
- Replacement non-retryable failures must show safe diagnostic information and `Back to main` without a retry action.
- Retrieval `MappingFailure` must not provide automatic or manual retry for the failed retrieval operation.
- Retrieval `MappingFailure` must not leave a retry action on the learning page.
- Retrieval `MappingFailure` must end the learning flow and show safe diagnostic information on the main page.
- Feedback must present only safe diagnostic information supplied by the application interface.
- `Back to main` must remain available on the learning page where the current transition preserves that page.

## Boundary

| concern | owner |
|---|---|
| Visible loading and category-specific failure feedback | `spec:product.ui.components.operation_feedback` |
| Retry count, state preservation, transition, and disposal | `spec:product.ui.learning_flow` |
| Failure meaning, retryability, and safe diagnostic content | `spec:product.application.pwa_interface` |
| Exact copy, indicators, and animation | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.ui.components` | Parent component overview. |
| `spec:product.ui.pages.main_page` | Uses feedback while loading the first unit. |
| `spec:product.ui.pages.learning_page` | Uses feedback while replacing the current unit. |
| `spec:product.ui.learning_flow` | Defines loading, retry, failure transitions, state preservation, and disposal. |
| `spec:product.application.pwa_interface` | Defines failure categories, retryability, and safe diagnostic meaning. |
| PRODUCT-ADR-APPLICATION-005 | Establishes application failure categories and retryability. |
| PRODUCT-ADR-UI-002 | Establishes category-specific PWA transitions and failure surfaces. |
