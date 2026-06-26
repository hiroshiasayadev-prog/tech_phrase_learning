# Concept: Main page

- **id**: `spec:product.ui.pages.main_page`
- **status**: draft
- **date**: 2026-06-27
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

### Error after automatic retries (infrastructure failure)

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

### Non-retryable failure (mapping or selection-contract failure)

```text
+--------------------------------------------------+
| Tech Phrase Learning                             |
|--------------------------------------------------|
|                                                  |
|                  All shuffle                     |
|                                                  |
|          Could not load a discussion.            |
|            <safe diagnostic information>         |
|                                                  |
+--------------------------------------------------+
```

The main page is the owning failure surface for its safe diagnostic information.
The exact recovery action available after a non-retryable failure is not defined by current accepted authority.

## Rules

| current state | action or result | resulting state |
|---|---|---|
| Idle | Select `Start`. | Loading. |
| Loading | First unit loads. | Learning page. |
| Loading | `InfrastructureFailure` after initial attempt and three retries. | Infrastructure error. |
| Infrastructure error | Select `Retry`. | Loading. |
| Loading | `MappingFailure` or `InvalidSelectionResult` received. | Non-retryable failure. |

- The page must expose only complete shuffle in the first MVP.
- The page must not create a shuffle-mode state for unavailable modes.
- The page must disable the initiating action during loading.
- The page must not navigate before the first unit loads successfully.
- The page must not show a retry action for `MappingFailure` or `InvalidSelectionResult`.
- The page must present only safe diagnostic information supplied by the application interface.
- The recovery action available after a non-retryable failure is not defined by current accepted authority.

## Boundary

| concern | owner |
|---|---|
| Page composition | `spec:product.ui.pages.main_page` |
| Retry count and state replacement | `spec:product.ui.learning_flow` |
| Queue acquisition and unit loading contract | `spec:product.application`. |
| Exact learner-facing copy | UI implementation unless separately specified. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.ui.pages` | Parent page overview. |
| `spec:product.ui.learning_flow` | Defines start, loading, retry, and category-specific failure-transition behavior. |
| `spec:product.application.pwa_interface` | Provides queue creation and defines the failure categories consumed by this page. |
| `spec:product.application.learning_unit_selection` | Provides queue creation. |
| `spec:product.application.learning_unit_retrieval` | Provides complete-unit retrieval. |
| `spec:product.ui.components.operation_feedback` | Defines loading and error feedback placement. |
| PRODUCT-ADR-UI-002 | Establishes main-page ownership of mapping and selection-contract failure surfaces. |
