# Concept: Top bar

- **id**: `spec:product.ui.components.top_bar`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.ui.components`

## What this is

Persistent header for the learning page.
The header shows the current learning context and provides an immediate return to main.

## Non-goals

- Main-page navigation.
- Discussion selection.
- Exact truncation and responsive rules.
- Branding and global application navigation.

## Concept model

```text
+------------------------------------------------------------+
| All shuffle · <discussion title>          [ Back to main ] |
+------------------------------------------------------------+
  ^             ^                              ^
  |             |                              |
  mode          current source discussion      discard flow
```

For a narrow viewport, the discussion title may shorten visually.
The semantic title and return action remain unchanged.

## Rules

- The top bar must remain visible on the learning page.
- The top bar must identify complete shuffle as the current mode.
- The top bar must identify the current discussion.
- The top bar must provide a return-to-main action.
- The return action must remain available during loading and error states.
- Returning to main must discard the current queue and session.
- The top bar must not expose backend selection controls in the first MVP.

## Boundary

| concern | owner |
|---|---|
| Header content and actions | `spec:product.ui.components.top_bar` |
| Return transition | `spec:product.ui.learning_flow` |
| Discussion title source | Published learning-unit content or future application contract. |
| Exact copy, iconography, truncation, and layout | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.ui.components` | Parent component overview. |
| `spec:product.ui.pages.learning_page` | Places the top bar above the learning content. |
| `spec:product.ui.learning_flow` | Defines the effect of `Back to main`. |
