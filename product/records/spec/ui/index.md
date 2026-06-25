# Overview: Learner UI

- **id**: `spec:product.ui`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product`

## What this is

Owner of PWA screen flow, transient learner-flow state, and user-visible operation feedback.
The area implements learning semantics without owning content generation or backend selection policy.

## Current contract

| concern | contract |
|---|---|
| Frontend role | Present published learning units and own temporary learner-flow state. |
| Learning content | Treat each loaded learning unit as immutable content. |
| Queue state | Keep cross-unit shuffle order separate from within-unit session progress. |
| Session state | Track one learning unit's current interaction, selected answers, and quiz phase. |
| Durability | Do not guarantee recovery after reload, tab closure, or navigation to the main screen. |
| Progressive reveal | Show only the current quiz or its answered card while preserving earlier summaries. |
| Skip | Leave the current discussion and begin loading the next available unit. |
| Final interaction | Show attribution and `Next discussion` on the final answered card. |
| Loading | Keep the current screen visible until replacement content loads successfully. |
| Retry | Retry failed learning-unit requests three times after the initial attempt. |
| Main screen | Initially provide one complete-shuffle start action. |
| Learning shell | Show shuffle context, the discussion title, and `Back to main`. |

## Non-goals

- Backend API shape.
- Learning-unit selection and shuffle-generation policy.
- Availability and publication ownership.
- Durable learner progress and learner history.
- Authentication and account behavior.
- Concrete frontend framework, state library, route structure, or implementation component tree.
- Styling, spacing, animation, and responsive measurements.

## Topic map

| topic | owner |
|---|---|
| Main-to-learning navigation | `spec:product.ui.learning_flow` |
| Learning queue and session state | `spec:product.ui.learning_flow` |
| Answer, continue, skip, and next-discussion transitions | `spec:product.ui.learning_flow` |
| Loading, retry, reload, and return-to-main behavior | `spec:product.ui.learning_flow` |
| Page composition and visual flow | `spec:product.ui.pages` |
| Reusable visual component responsibilities | `spec:product.ui.components` |
| Learning content meaning | `spec:product.learning` |
| Content generation and publication | `spec:product.pipeline` |

## Topics

| title | kind | ref | summary |
|---|---|---|---|
| Learning flow | Concept | `spec:product.ui.learning_flow` | PWA state ownership, screen transitions, loading, retry, and transient lifecycle. |
| UI pages | Overview | `spec:product.ui.pages` | Main and learning page composition shown as visual flows. |
| UI components | Overview | `spec:product.ui.components` | Visual responsibilities for the learning-page parts. |

## Boundary

| concern | owner |
|---|---|
| Learner-facing phrase, quiz, summary, and attribution meaning | `spec:product.learning` |
| PWA runtime state and screen behavior | `spec:product.ui` |
| Page and component visual models | `spec:product.ui.pages` and `spec:product.ui.components` |
| Content ingestion, generation, validation, and publication | `spec:product.pipeline` |
| Backend selection, API, and repository boundaries | Future application or backend contract. |

## Related specs

| ref | relation |
|---|---|
| `spec:product` | PRODUCT placement router and dependency direction. |
| `spec:product.learning` | Defines the learner-visible semantics implemented by the UI. |
| `spec:product.learning.quiz_session` | Defines progressive quiz-to-summary behavior. |
| `spec:product.ui.pages` | Shows the first-MVP page composition and navigation. |
| `spec:product.ui.components` | Shows the reusable visual parts. |
| `spec:product.pipeline` | Produces the published content consumed by the UI. |
| PRODUCT-ADR-UI-001 | Establishes PWA ownership of transient learner-flow state. |
