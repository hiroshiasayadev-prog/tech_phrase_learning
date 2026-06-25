# Overview: UI pages

- **id**: `spec:product.ui.pages`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.ui`

## What this is

Visual map of the first-MVP learner-facing pages.
The diagrams show page composition and navigation without fixing framework routes or component files.

## Current contract

```text
+-------------+       Start succeeds       +----------------+
| Main page   | --------------------------> | Learning page  |
|             |                             |                |
| All shuffle | <-------------------------- | Back to main   |
+-------------+      discard flow state     +----------------+
                                                |
                                                | Skip or
                                                | Next discussion
                                                v
                                         replace current unit
                                         on the same page
```

| page | purpose | leaves the page when |
|---|---|---|
| Main page | Start a complete-shuffle learning flow. | The first learning unit loads successfully. |
| Learning page | Present one learning unit and continue through the queue. | The learner selects `Back to main`. |

## Non-goals

- Concrete route paths.
- Browser history behavior.
- React or Next.js file layout.
- Styling and responsive measurements.
- Backend request schemas.

## Topic map

| concern | owner |
|---|---|
| Main page composition and states | `spec:product.ui.pages.main_page` |
| Learning page composition and states | `spec:product.ui.pages.learning_page` |
| Cross-page runtime transitions | `spec:product.ui.learning_flow` |
| Reusable visual parts | `spec:product.ui.components` |

## Topics

| title | kind | ref | summary |
|---|---|---|---|
| Main page | Concept | `spec:product.ui.pages.main_page` | Complete-shuffle entry, loading, and retry states. |
| Learning page | Concept | `spec:product.ui.pages.learning_page` | Learning shell, progressive cards, skip, and next-discussion states. |

## Boundary

| concern | owner |
|---|---|
| Page composition and visible state | `spec:product.ui.pages` |
| Queue and session transition rules | `spec:product.ui.learning_flow` |
| Quiz and summary meaning | `spec:product.learning` |
| Concrete implementation routes and files | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.ui` | Parent learner UI overview. |
| `spec:product.ui.learning_flow` | Defines transient state and transition rules. |
| `spec:product.ui.components` | Defines the visual parts assembled by these pages. |
