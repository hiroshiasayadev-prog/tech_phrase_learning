# Concept: Learning path

- **id**: `spec:product.learning.learning_path`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.learning`

## What this is

Semantic model for one ordered source-post sequence that can support phrase-learning units.
The model defines learning suitability without defining pipeline algorithms or storage schemas.

## Non-goals

- Source ingestion and conversation-tree construction.
- Path enumeration and filtering algorithms.
- Concrete source identifiers and Discourse fields.
- Learning-unit generation mechanics.
- Session selection algorithms.
- Persistence and API schemas.

## Concept model

| concept | contract |
|---|---|
| Source discussion | One authentic technical conversation that owns the referenced source posts. |
| Source-post reference | A source-independent reference to one authentic post. |
| Learning path | An ordered sequence of connected source-post references from one source discussion. |
| Valid path | A learning path that satisfies the learning suitability rules in this spec. |
| Learning unit | Learner-facing content generated from one valid path. |

## Cardinality

| relationship | contract |
|---|---|
| Source discussion to valid path | One discussion may provide zero or more valid paths. |
| Valid path to source post | One valid path contains two to six ordered source-post references for the first MVP. |
| Valid path to learning unit | One valid path may support zero or more learning units. |
| Learning unit to valid path | One learning unit references exactly one valid path. |

## Rules

### Path composition

- A valid path must reference posts from one source discussion.
- A valid path must begin with the discussion opening post.
- A valid path must include at least one authentic reply.
- Adjacent path posts must follow the accepted conversation projection.
- Path order must preserve source conversation order.
- A valid path must remain understandable as one coherent exchange.
- Every selected post must support one useful phrase-learning quiz in the first MVP.
- Summarization may reduce technical burden without changing the conversational movement.

### Multiple valid paths

- One discussion may retain several independently valid paths.
- The pipeline must not assign one canonical learning path during ingestion.
- A path must be judged against the learning suitability rules without comparison to sibling paths.
- A shorter or higher-ranked sibling path is not a rejection reason.
- Prefix-overlapping valid paths may coexist.
- Later deduplication policy may suppress variants without changing path validity.

### Source boundary

- A learning path must reference source posts instead of copying source bodies.
- A learning path must not expose source-specific fields as learning-domain semantics.
- The source system must remain responsible for raw post content and source relationships.
- Learning-unit provenance must retain a route from each selected turn to its authentic source post.

### Learning-unit boundary

- A valid path is source material for learning-unit generation.
- A valid path is not itself learner-facing quiz content.
- Different learning units may use different target phrases or quiz choices for the same path.
- A valid path does not become session-available until an associated learning unit passes the publication gate.

## Boundary

| concern | owner |
|---|---|
| Meaning and suitability of a learning path | `spec:product.learning.learning_path` |
| Learner-visible content generated from a path | `spec:product.learning.learning_unit` |
| Session progression over one learning unit | `spec:product.learning.quiz_session` |
| Path enumeration, validation, filtering, and provenance materialization | `spec:product.pipeline` |
| Runtime learning-unit selection | `spec:product.application.learning_unit_selection`. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.learning` | Parent learning overview. |
| `spec:product.learning.learning_model` | Defines the source-context and phrase-exposure goals. |
| `spec:product.learning.learning_unit` | Defines content generated from one valid path. |
| `spec:product.learning.quiz_session` | Defines progressive presentation of one selected learning unit. |
| `spec:product.pipeline` | Implements candidate generation and filtering for this contract. |
| `spec:product.application.learning_unit_selection` | Selects available learning units rather than raw learning paths. |
| PRODUCT-ADR-LEARNING-005 | Establishes multiple valid paths and learning-unit generation from summarized source-post paths. |
