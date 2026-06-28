# Concept: Quiz session

- **id**: `spec:product.learning.quiz_session`
- **status**: draft
- **date**: 2026-06-27
- **parent**: `spec:product.learning`

## What this is

Learner-visible interaction contract for presenting one available learning unit.
The session progressively replaces each active quiz card with an answered summary card.

## Non-goals

- Learning-unit selection, queue, replacement, and availability policy.
- Account, learner-history, scoring, analytics, and durable progress behavior.
- Source ingestion, quiz generation, and publication-gate mechanics.
- Shuffle algorithms, random sources, permutation serialization, and state storage.
- Transport, persistence, and restoration schemas.
- Concrete pages, routes, components, modals, layout measurements, and styling.
- Raw source-post display.
- Unrestricted generated chat.

## Concept model

### Session elements

| element | meaning |
|---|---|
| Quiz session | Progressive learner interaction over exactly one available learning unit. |
| Active interaction | The only interaction that currently accepts an answer. |
| Future interaction | A later interaction that remains unavailable until progression reaches it. |
| Answered card | A completed interaction that shows its source-post summary and answer result. |
| Answer detail | A collapsible region containing the result, prompt, and correct target phrase. |
| Question interaction | The first interaction, linked to the source discussion opening post. |
| Reply interaction | A later interaction, linked to one authentic reply in source-post order. |
| Continue action | Advances from a non-final answered interaction to the next interaction. |
| Skip discussion action | Ends the current unit without revealing any remaining unanswered content. |
| Next discussion action | Ends a normally completed unit from the final answered card. |
| Attribution access | Learner access to the current unit's source and license details. |

### Progression model

| current state | learner action | resulting state |
|---|---|---|
| Session start | None. | The first question interaction becomes active. |
| Active interaction | Select one answer option. | The same interaction becomes an open answered card. |
| Open non-final answered card | Continue. | The answer detail becomes collapsible and the next interaction becomes active. |
| Earlier answered card | Open or close its answer detail. | The answered card keeps its summary and result semantics. |
| Active interaction | Skip discussion. | The current unit ends and all unanswered content remains concealed. |
| Final open answered card | Next discussion. | The current unit ends without a separate terminal screen. |

## Rules

### Session scope and order

- A quiz session must use exactly one available learning unit.
- A quiz session must present the unit's two to six ordered interactions.
- The first interaction must be the opening-post question-formulation interaction.
- Every later interaction must be a reply-formulation interaction.
- Interaction order must match the learning unit and its source-post order.
- Normal progression must not reorder or omit interactions.
- The session must not generate or replace learning-unit content at session start.

### Discussion title and content origin

- The learner-visible session title must be the learning unit's original source discussion title.
- The title must not be replaced by a generated or path-specific title.
- Generated prompts, phrases, options, and summaries must not appear as authentic source quotations.
- Generated or adapted wording must remain distinguishable from source-authored wording throughout the session.
- Concrete visual distinction belongs to `spec:product.ui`.

### Progressive presentation

- The session may show zero or more answered cards and one active interaction.
- Only the active interaction may accept a learner answer.
- Future interactions must remain unavailable until progression reaches them.
- Answering must replace the active quiz card with one answered card for the same source post.
- The newest answered card must initially remain open.
- The newest answered card must remain open until the learner continues.
- Earlier answered cards may open or close their answer details.
- Closing an answered card must not hide its source-post summary.
- The accumulated summaries provide conversation context for the active interaction.

### Option presentation and correctness

- Each interaction must present exactly three semantic options.
- The three options must be shuffled when the interaction first becomes active.
- The selected display permutation must remain stable for that interaction until the current learning-unit session ends.
- A learner selection must retain the selected semantic option identity.
- A learner selection must not use array position, display order, display label, or option text as semantic identity.
- Correctness must compare the selected semantic option identity with the interaction's immutable correct-option reference.
- Shuffle algorithm, random source, permutation serialization, persistence, restoration, and UI state storage are not Learning-owned.

### Active quiz card

- The active quiz card must show the quiz prompt.
- The active quiz card must show exactly three answer options.
- The active quiz card must not show the source-post summary before the learner answers.
- The active quiz card must not identify the correct option before the learner answers.
- The active quiz card must provide the accepted action to skip the current discussion.

### Answered card

- The answered card must show the corresponding source-post summary outside the collapsible answer detail.
- The open answer detail must show whether the learner was correct.
- The open answer detail must show the original quiz prompt.
- The open answer detail must show the target quiz phrase as the correct phrase.
- A non-final newest answered card must provide the continue action.
- Continuing must activate the next interaction without changing interaction order.
- Previously answered cards remain reviewable through the summary and collapsible answer-detail behavior authorized by PRODUCT-ADR-LEARNING-006.

### Attribution and legal access

- The current learning unit's attribution record must remain learner-accessible throughout the active session.
- The final answered card must provide access to the current learning unit's attribution record.
- Global legal notices must remain learner-accessible from the main-page experience.
- Learning owns the required access outcomes.
- UI owns placement, controls, routes, modals, prominence, and accessibility implementation.

### Session completion and early exit

- Normal completion occurs after every interaction has been answered and the final answered card is shown.
- The final answered card must provide a `Next discussion` action.
- The session must not require a separate completion screen.
- Skip discussion ends the current learning-unit session before normal completion.
- Skip discussion must not reveal summaries or correct target phrases for unanswered interactions.
- Skip discussion must not mark unanswered interactions as answered.
- Scoring, persistence, analytics, retry, replacement, and runtime-selection policy remain outside this contract.

### Downstream constraints

| owner | required outcome |
|---|---|
| Pipeline | Materialize two to six ordered interactions, the original source discussion title, semantic option identities, correct-option references, summaries, target phrases, complete attribution, generated-source distinction, and a publication-ready unit result. |
| Application | Preserve one complete learning unit without losing interaction order, title, semantic option identity, correct-option reference, summary, target phrase, attribution, or generated-source distinction. |
| UI | Present the source title, shuffle each interaction on first activation, keep its permutation stable, retain semantic selections, derive correctness from immutable content, conceal unanswered content after skip, and preserve legal and attribution access. |

- Pipeline generation stages, model tasks, prompts, thresholds, retries, gate implementation, schemas, and path mechanics remain Pipeline-owned.
- Application queue, selection, replacement, transport, persistence, failure, and method-shape decisions remain Application-owned.
- UI components, layout, styling, routes, modals, state stores, and permutation persistence remain UI-owned.

### Language boundary

- All learner-facing prompts, options, summaries, results, labels, and controls must be English.

## Boundary

| concern | owner |
|---|---|
| Valid path and path-to-unit relationship | `spec:product.learning.learning_path` |
| Meaning of title, prompts, options, phrases, summaries, identities, and attribution | `spec:product.learning.learning_unit` |
| Session scope, order, progressive reveal, shuffled-presentation outcome, and access outcomes | `spec:product.learning.quiz_session` |
| Runtime learning-unit selection, retrieval, and availability behavior | `spec:product.application` |
| PWA queue, session state, loading, retry, navigation, and presentation mechanisms | `spec:product.ui` |
| Learning-content generation and materialization | `spec:product.pipeline.content_generation` |
| Content validation and completion | `spec:product.pipeline.validation` |
| Publication-gate implementation and writes | `spec:product.pipeline.publication` |
| Transport, persistence, serialization, and concrete styling | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.learning` | Parent learning overview. |
| `spec:product.learning.learning_path` | Defines the source-post path presented by the session. |
| `spec:product.learning.learning_unit` | Defines immutable content and attribution consumed by the session. |
| `spec:product.pipeline.content_generation` | Produces the complete ordered interaction content. |
| `spec:product.pipeline.validation` | Validates complete ordered content before publication. |
| `spec:product.pipeline.publication` | Authorizes and writes session-available current content. |
| `spec:product.application.published_content` | Holds the complete current learning unit read by runtime use cases. |
| `spec:product.application.learning_unit_selection` | Selects available learning-unit references used by the session. |
| `spec:product.application.learning_unit_retrieval` | Retrieves the available complete unit used by the session. |
| `spec:product.ui.learning_flow` | Implements transient PWA state and transitions for this session contract. |
| PRODUCT-ADR-LEARNING-005 | Establishes the current summarized learning-unit model. |
| PRODUCT-ADR-LEARNING-006 | Establishes progressive quiz-to-summary card behavior. |
| PRODUCT-ADR-LEARNING-007 | Establishes the two-to-six session interaction range. |
| PRODUCT-ADR-LEARNING-009 | Establishes the original source discussion title. |
| PRODUCT-ADR-LEARNING-010 | Establishes semantic option identity and stable shuffled presentation. |
| PRODUCT-ADR-LEARNING-011 | Establishes noncommercial source use and attribution-access outcomes. |
| PRODUCT-ADR-LEARNING-012 | Establishes generated-source separation and publication readiness. |
