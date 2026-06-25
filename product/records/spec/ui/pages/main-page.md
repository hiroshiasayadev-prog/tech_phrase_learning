# Concept: Main page

- **id**: `spec:product.ui.pages.main_page`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.ui.pages`

## What this is

Entry page for starting the first-MVP complete-shuffle flow.
The page remains visible until the first learning unit loads successfully.

## Non-goals

- Topic or discussion selection.
- Learner history and progress display.
- Account controls.
- Concrete branding and styling.

## Concept model

### Idle

```text
+--------------------------------------------------+
| Tech Phrase Learning                             |
|--------------------------------------------------|
|                                                  |
|                  All shuffle                     |
|                                                  |
|                    [ Start ]                     |
|                                                  |
+--------------------------------------------------+
```

### Loading

```text
+--------------------------------------------------+
| Tech Phrase Learning                             |
|--------------------------------------------------|
|                                                  |
|                  All shuffle                     |
|                                                  |
|                 [ Start ] disabled               |
|                                                  |
|              Loading discussion...               |
|                                                  |
+--------------------------------------------------+
```

### Error after automatic retries

```text
+--------------------------------------------------+
| Tech Phrase Learning                             |
|--------------------------------------------------|
|                                                  |
|                  All shuffle                     |
|                                                  |
|          Could not load a discussion.            |
|                                                  |
|                    [ Retry ]                     |
|                                                  |
+--------------------------------------------------+
```

## Rules

| current state | action or result | resulting state |
|---|---|---|
| Idle | Select `Start`. | Loading. |
| Loading | First unit loads. | Learning page. |
| Loading | Initial attempt and three retries fail. | Error. |
| Error | Select `Retry`. | Loading. |

- The page must expose only complete shuffle in the first MVP.
- The page must not create a shuffle-mode state for unavailable modes.
- The page must disable the initiating action during loading.
- The page must not navigate before the first unit loads successfully.

## Boundary

| concern | owner |
|---|---|
| Page composition | `spec:product.ui.pages.main_page` |
| Retry count and state replacement | `spec:product.ui.learning_flow` |
| Queue acquisition and unit loading contract | Future backend or application contract. |
| Exact learner-facing copy | UI implementation unless separately specified. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.ui.pages` | Parent page overview. |
| `spec:product.ui.learning_flow` | Defines start, loading, and retry behavior. |
| `spec:product.ui.components.operation_feedback` | Defines loading and error feedback placement. |
