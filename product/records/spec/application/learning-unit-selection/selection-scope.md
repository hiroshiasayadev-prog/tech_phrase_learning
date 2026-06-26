# Reference: Selection scope

- **id**: `spec:product.application.learning_unit_selection.selection_scope`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.application.learning_unit_selection`

## What this is

Reference for content constraints accepted by application selection.
Scope is separate from current availability.

## Current contract

```text
SelectionScope =
  All
  | Constrained(non_empty_constraints)
```

| scope | meaning |
|---|---|
| `All` | No content-based constraint beyond current availability. |
| `Constrained` | Future content constraint set that narrows eligible candidates. |

## Rules

- The first MVP supports only `All`.
- `All` includes every currently available unit in the eligible candidate set.
- `All` does not require one queue to contain the complete eligible corpus.
- A constrained scope must contain at least one constraint.
- An empty constraint set must be represented as `All`.
- Future non-history constraints may cover source, topic, discussion, and difficulty.
- Future non-history constraints must combine by intersection.
- Every non-history constraint must be evaluable from the published runtime boundary.
- A scope must not contain queue position, prior queue references, learner answers, or learner progress.
- Learner-history selection remains excluded.
- Durable learner identity, progress ownership, and history access require a separate decision before learner-history selection is added.

## Boundary

| concern | owner |
|---|---|
| Selection-scope vocabulary | `spec:product.application.learning_unit_selection.selection_scope` |
| Current availability | `spec:product.application.published_content.availability` |
| Learner-flow state | `spec:product.ui.learning_flow` |
| Durable learner history | Future decision. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.application.learning_unit_selection` | Parent selection overview. |
| `spec:product.application.learning_unit_selection.create_complete_shuffle_queue` | Applies `All` as first-MVP policy. |
| `spec:product.application.outbound_queries.select_learning_unit_refs` | Receives selection scope as query input. |
