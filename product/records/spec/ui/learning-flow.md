# Concept: Learning flow

- **id**: `spec:product.ui.learning_flow`
- **status**: draft
- **date**: 2026-06-27
- **parent**: `spec:product.ui`

## What this is

PWA runtime model for starting, presenting, advancing, skipping, and leaving a transient learning flow.
The model separates immutable learning content from queue, session, and presentation state.

## Non-goals

- Backend request and response schemas.
- Learning-unit selection and shuffle-generation policy.
- Durable progress, learner history, or recovery.
- Concrete state-management library or component structure.
- Concrete route paths.
- Styling and responsive layout.

## Concept model

| concept | meaning | lifetime |
|---|---|---|
| Loaded learning unit | Immutable content for one published learning unit. | Until the UI replaces or discards the current unit. |
| Learning queue | Ordered learning-unit references for the current shuffle run. | Until the queue is replaced or the learner returns to main. |
| Session | Mutable progress within exactly one loaded learning unit. | Until the UI starts another unit or returns to main. |
| Presentation state | Card expansion, loading indicator, and operation error state. | Until the relevant view or operation ends. |

```text
LoadedLearningUnit
  ^
  | referenced by
  |
Session
  +-- learning_unit_ref
  +-- current_interaction_index
  +-- answers[]
  +-- phase: quiz | answered

LearningQueue
  +-- unit_refs[]
  +-- current_unit_index
```

## Rules

### Main screen

- The first MVP must show one complete-shuffle start action.
- The first MVP must not require a shuffle-mode state while no alternative mode exists.
- Starting must keep the main screen visible while the initial queue request is pending.
- A successful non-empty initial queue must keep the main screen visible until the first learning unit loads.
- The start action must remain disabled while loading.
- An initial queue-creation `InfrastructureFailure` must use the retry behavior defined by this spec.
- An initial queue-creation `MappingFailure` must not enter automatic retry. The main page is the owning failure surface for its safe diagnostic.
- An initial queue-creation `InvalidSelectionResult` must not enter automatic retry. The main page is the owning failure surface for its safe diagnostic.
- A successful empty initial queue must show the empty-queue screen.
- The PWA must not request another queue after accepting a successful empty initial result.

### Learning screen shell

- The learning screen must show a persistent top bar.
- The top bar must identify the complete-shuffle mode.
- The top bar must show the current discussion title.
- The top bar must provide a `Back to main` action.
- `Back to main` must remain available during loading and retry.
- `Back to main` must remain available on replacement queue-creation failure surfaces.
- `Back to main` must discard the current queue and session without confirmation.

### Learning queue

- `LearningQueue` must remain separate from `Session`.
- The PWA must initialize `LearningQueue.unit_refs` from the ordered reference array returned by `CreateCompleteShuffleQueue`.
- The PWA must preserve the returned reference order.
- `current_unit_index` must identify the unit currently shown by the UI.
- The queue index must advance only after the next learning unit loads successfully.
- Queue exhaustion must trigger one acquisition of another complete-shuffle queue.
- Queue exhaustion must not require an intermediate return to the main screen.
- A non-empty replacement queue must replace the exhausted queue and preserve its returned order.
- A successful empty replacement queue must end the current learning flow and show the empty-queue screen.
- The PWA must not request another queue after accepting a successful empty replacement result.
- A queued reference returned as unavailable must be removed from the pending queue candidates.
- The UI must try the next pending reference without retrying the unavailable reference.
- Removing an unavailable pending reference must not replace the loaded unit or active session.
- `Unavailable` must not enter technical-failure retry or diagnostic handling.
- A retrieval `InfrastructureFailure` must use the retry behavior defined by this spec.
- A retrieval `MappingFailure` must end the active learning flow. The PWA must discard the active queue and session and return to the main page. The returned main page is the owning failure surface for the safe diagnostic. The previous learning screen must not be retained as a manual retry surface.
- Application queue-production policy remains outside this spec.

### Empty queue screen

- The empty-queue screen must represent a successful queue result containing no references.
- The empty-queue screen must show `Quiz list was empty.`.
- The empty-queue screen must provide a `Back to main` action.
- The empty-queue screen must not provide automatic or manual queue retry.
- Entering the empty-queue screen must discard any current queue and active session.
- Request failures must not use the empty-queue screen.

### Session

- One `Session` must reference exactly one loaded learning unit.
- A `Session` must not own a copied mutable learning-unit model.
- A `Session` must not require a session identifier.
- A `Session` must record the current interaction index.
- A `Session` must record each selected option identifier.
- A `Session` phase must be `quiz` or `answered`.
- The current interaction index must identify the card currently acting as the screen focus.

### Answer and continue

| current phase | action | resulting phase | index change |
|---|---|---|---|
| `quiz` | Select an answer option. | `answered` | None. |
| `answered`, non-final interaction | Continue. | `quiz` | Advance by one. |
| `answered`, final interaction | Select `Next discussion`. | New session. | Queue advances after successful load. |

- Answering must retain the selected option identifier.
- Correctness must be derived from the immutable learning unit.
- Answering must not advance the current interaction index.
- The newest answered card must remain open until the learner continues.
- Earlier answer-detail expansion must remain presentation state outside `Session`.

### Final answered card

- The final answered card must remain the last screen for the current learning unit.
- The final answered card must show source attribution.
- The final answered card must provide a `Next discussion` action.
- The UI must not show a separate completion or terminal screen.

### Skip

- Skip must be available from an active quiz.
- Skip must not reveal unanswered summaries or correct phrases.
- Skip must immediately begin loading the next learning unit.
- Skip must not create a `skipped` session phase.
- Skip must not show an intermediate skipped screen.

### Loading and replacement

- The current screen must remain visible while the next learning unit loads.
- The initiating action must remain disabled while loading.
- The UI must show loading feedback on the current screen.
- The UI must replace the queue position, loaded unit, and session only after successful loading.
- A failed request must not advance the queue or replace the session.

### Retry

This retry flow applies only to:

- initial queue creation that returns `InfrastructureFailure`;
- replacement queue creation that returns `InfrastructureFailure`;
- learning-unit retrieval that returns `InfrastructureFailure`.

`MappingFailure`, `InvalidSelectionResult`, and `Unavailable` do not enter this flow. See Outcome transitions below.

```text
initial request
  -> InfrastructureFailure
  -> automatic retry 1
  -> automatic retry 2
  -> automatic retry 3
  -> error + manual Retry
```

Rules:

- One initial attempt and three automatic retries apply to each covered operation.
- A successful empty queue result must not enter retry behavior.
- Failure after all automatic retries must show an error and a manual `Retry` action.

| operation context | retry surface | preserved state |
|---|---|---|
| Initial queue creation | Main page | Main-page state stable through retry. |
| Replacement queue creation | Current learning screen | Loaded unit, exhausted queue state, and session. |
| Learning-unit retrieval | Current learning screen | Loaded unit, queue position, and session. |

### Outcome transitions

The PWA consumes application outcome categories as inputs to UI transitions. The application interface (`spec:product.application.pwa_interface`) owns outcome meaning, retryability, and safe diagnostic content. This spec owns the resulting screen transitions, state disposal, and diagnostic surface placement.

| operation | outcome class | outcome | UI transition | state rule |
|---|---|---|---|---|
| Initial queue creation | failure | `InfrastructureFailure` | Enter the retry flow. Remain on the main page. | Keep main-page state stable through retry. |
| Initial queue creation | failure | `MappingFailure` | Do not enter automatic retry. Remain on the main page. The main page is the owning failure surface for the safe diagnostic. | No partial queue or backend state exists. |
| Initial queue creation | failure | `InvalidSelectionResult` | Do not enter automatic retry. Remain on the main page. The main page is the owning failure surface for the safe diagnostic. | No partial queue or backend state exists. |
| Replacement queue creation | failure | `InfrastructureFailure` | Enter the retry flow on the current learning page. | Keep the loaded unit, exhausted queue state, and session unchanged through automatic and manual retry. |
| Replacement queue creation | failure | `MappingFailure` | Do not enter automatic or manual retry. Keep the current learning page as the safe diagnostic surface and show `Back to main` after the diagnostic. | Keep the loaded unit, exhausted queue state, and session until `Back to main` discards the queue and session. |
| Replacement queue creation | failure | `InvalidSelectionResult` | Do not enter automatic or manual retry. Keep the current learning page as the safe diagnostic surface and show `Back to main` after the diagnostic. | Keep the loaded unit, exhausted queue state, and session until `Back to main` discards the queue and session. |
| Retrieval | failure | `InfrastructureFailure` | Enter the retry flow. Keep the current screen, loaded unit, queue position, and session unchanged. | Preserve all current state through automatic and manual retry. |
| Retrieval | failure | `MappingFailure` | End the active learning flow. Discard the active queue and session. Return to the main page. The returned main page is the owning failure surface for the safe diagnostic. | Do not retain the previous learning screen as a manual retry surface. |
| Retrieval | normal result | `Unavailable` | Remove only the affected pending reference. Continue with the next pending reference. | Keep the current loaded unit, queue position, and session unchanged until a later reference loads successfully. |

Rules:

- The PWA must present only safe diagnostic information supplied by the application contract.
- Retry counts remain as defined in this spec. Application retryability classification does not change the retry count.
- Replacement queue-creation `MappingFailure` and `InvalidSelectionResult` are terminal on the current learning page until the learner selects `Back to main`.

### Transient lifecycle

- Reload recovery is not guaranteed.
- Tab closure may discard the queue and session.
- Returning to the main screen must discard the queue and session.
- The first MVP must not use transient state as durable learner progress.

## Boundary

| concern | owner |
|---|---|
| Quiz, summary, target phrase, option, and attribution meaning | `spec:product.learning` |
| Progressive learner-visible card semantics | `spec:product.learning.quiz_session` |
| PWA state ownership and runtime transitions | `spec:product.ui.learning_flow` |
| Unit availability | `spec:product.application.published_content.availability`. |
| Queue generation | `spec:product.application.learning_unit_selection`. |
| Complete-unit retrieval | `spec:product.application.learning_unit_retrieval`. |
| Content generation and publication | `spec:product.pipeline` |

## Related specs

| ref | relation |
|---|---|
| `spec:product.ui` | Parent UI overview. |
| `spec:product.ui.pages` | Visualizes the page states driven by this flow. |
| `spec:product.ui.components` | Visualizes the component responsibilities driven by this flow. |
| `spec:product.learning.learning_unit` | Defines immutable learner-visible content consumed by the flow. |
| `spec:product.learning.quiz_session` | Defines progressive card meaning and reveal order. |
| `spec:product.pipeline` | Produces validated learning units before the flow starts. |
| `spec:product.application.pwa_interface` | Defines PWA-facing failure categories, retryability, and safe diagnostic boundary consumed by this spec. |
| `spec:product.application.learning_unit_selection` | Creates queues of available learning-unit references. |
| `spec:product.application.learning_unit_retrieval` | Retrieves available complete units for queued references. |
| PRODUCT-ADR-UI-001 | Establishes the state ownership and runtime boundaries in this spec. |
| PRODUCT-ADR-UI-002 | Establishes category-specific failure transitions and diagnostic-surface assignments reflected in this spec. |
