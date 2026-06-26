# Overview: UI components

- **id**: `spec:product.ui.components`
- **status**: draft
- **date**: 2026-06-27
- **parent**: `spec:product.ui`

## What this is

Visual catalog of the first-MVP learner UI parts.
The catalog defines visible responsibilities without requiring one React component per specification concept.

## Current contract

```text
Learning page
  |
  +-- Top bar
  |
  +-- Card stack
  |     |
  |     +-- zero or more Answered cards
  |     |
  |     +-- one Quiz card
  |           or
  |         newest Answered card
  |
  +-- Operation feedback
        +-- loading
        +-- infrastructure error + Retry
        +-- non-retryable safe diagnostic
        +-- replacement Back to main
```

| component concept | visible responsibility |
|---|---|
| Top bar | Show shuffle context, discussion title, and return action. |
| Quiz card | Present one unanswered interaction and skip action. |
| Answered card | Preserve the summary and expose collapsible answer detail. |
| Operation feedback | Show loading and category-specific failure feedback on the owning page. Retry UI appears only for `InfrastructureFailure`. |

## Non-goals

- React component names.
- Component file locations.
- Props and event-handler signatures.
- Design-system tokens.
- Styling and animation.

## Topic map

| concern | owner |
|---|---|
| Persistent learning header | `spec:product.ui.components.top_bar` |
| Active interaction | `spec:product.ui.components.quiz_card` |
| Completed interaction | `spec:product.ui.components.answered_card` |
| Loading and category-specific failure feedback | `spec:product.ui.components.operation_feedback` |
| Page-level assembly | `spec:product.ui.pages` |

## Topics

| title | kind | ref | summary |
|---|---|---|---|
| Top bar | Concept | `spec:product.ui.components.top_bar` | Shuffle context, discussion title, and `Back to main`. |
| Quiz card | Concept | `spec:product.ui.components.quiz_card` | Prompt, three options, and skip action. |
| Answered card | Concept | `spec:product.ui.components.answered_card` | Summary, result detail, continuation, and final attribution. |
| Operation feedback | Concept | `spec:product.ui.components.operation_feedback` | Loading, infrastructure retry, non-retryable diagnostics, and owning-page failure surfaces. |

## Boundary

| concern | owner |
|---|---|
| Visible component responsibility | `spec:product.ui.components` |
| Page composition | `spec:product.ui.pages` |
| Runtime state transitions | `spec:product.ui.learning_flow` |
| Concrete component implementation | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.ui` | Parent learner UI overview. |
| `spec:product.ui.pages` | Assembles these component concepts into pages. |
| `spec:product.ui.learning_flow` | Defines the state and category-specific transitions that drive component visibility. |
| `spec:product.application.pwa_interface` | Defines application failure categories, retryability, and safe diagnostic meaning. |
| PRODUCT-ADR-APPLICATION-005 | Establishes application failure categories and retryability. |
| PRODUCT-ADR-UI-002 | Establishes category-specific PWA transitions and failure surfaces. |
