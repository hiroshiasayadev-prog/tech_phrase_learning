# Concept: Learning unit

- **id**: `spec:product.learning.learning_unit`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product.learning`

## What this is

Learner-visible semantic model for phrase quizzes generated from one valid learning path.
The model separates generated quiz content, source-derived summaries, and authentic source evidence.

## Non-goals

- Source ingestion and conversation-tree construction.
- Learning-path enumeration and filtering.
- LLM provider selection and prompt design.
- Serialized package and persistence schemas.
- Concrete component styling and responsive layout.
- Runtime learner-answer state.

## Concept model

| element | origin | learner-visible purpose |
|---|---|---|
| Learning-path reference | Source-derived | Identifies the ordered source-post sequence used by the unit. |
| Interaction type | Defined | Distinguishes question formulation from reply formulation. |
| Quiz prompt | Generated and validated | States what the source author intends to communicate. |
| Answer options | Generated and validated | Present three natural English candidate responses to the stated intent. |
| Target quiz phrase | Generated and validated | Identifies the reusable expression taught by the interaction. |
| Correct option | Generated and validated | Uses or directly realizes the target phrase in the one response that fits the prompt. |
| Source-post summary | Source-derived and validated | Reveals the technical meaning of the corresponding source post after the answer. |
| Source evidence | Authentic source reference | Grounds the summary and target phrase in the corresponding source post. |
| Attribution | Source metadata | Identifies the source discussion and original location. |

## Cardinality

| relationship | contract |
|---|---|
| Learning unit to learning path | One learning unit references exactly one valid learning path. |
| Learning path to learning unit | Each valid learning path defines exactly one learning unit. |
| Selected source post to interaction | Every selected source post has exactly one interaction in the first MVP. |
| Interaction to source-post summary | Every interaction has exactly one learner-visible summary. |
| Interaction to quiz prompt | Every interaction has exactly one prompt. |
| Interaction to answer option | Every interaction has exactly three answer options. |
| Interaction to correct option | Exactly one answer option is the correct option. |
| Interaction to target quiz phrase | Every interaction has exactly one target phrase. |

## Rules

### Unit composition

- Every first-MVP learning unit must contain at least one question-formulation interaction.
- Every first-MVP learning unit must contain at least one reply-formulation interaction.
- The first interaction must correspond to the source discussion opening post.
- Every later interaction must correspond to an authentic reply in the selected path.
- Interaction order must match source-post order.
- Every selected source post must have one interaction.
- Stable learning-unit identity is anchored to valid learning-path identity.
- Generated-content changes must not change the logical learning-unit identity.
- Target phrases, quiz prompts, answer options, and correct-option wording are not identity inputs.
- Source-post summaries, model identity, prompt versions, and validation implementations are not identity inputs.
- A different valid path creates a different learning unit.

### Source-post summary

- A reusable source-post summary may support several valid paths.
- A path-specific summary may revise the reusable summary for conversational continuity.
- One learning-unit interaction may use the reusable summary or a grounded path-specific revision.
- Both summary forms must remain grounded in the same authentic source post.
- Summary generation order and revision mechanics belong to `spec:product.pipeline`.
- The learner-visible summary must be English.
- The learner-visible summary must preserve the technical meaning needed to understand the source post.
- The learner-visible summary may omit code, links, examples, and technical detail that do not support phrase learning.
- The learner-visible summary must preserve the source author's position, certainty, and conversational response.
- The learner-visible summary must remain coherent with the preceding summaries in the selected path.
- The learner-visible summary must not add unsupported technical claims.
- The learner-visible summary is the default learner-visible representation of the source post.
- Raw source-post display is not required for the first MVP.

### Quiz prompt

- The prompt must be English.
- The prompt must state what the source author intends to communicate.
- The prompt must remain concise.
- The prompt must contain only enough situation detail to judge the answer options.
- The prompt must minimize source-specific technical terminology.
- The prompt must not reveal the target quiz phrase.

### Answer options

- Every answer option must be a grammatical and natural English candidate response.
- Every answer option must minimize source-specific technical detail.
- Every answer option must preserve enough situation detail to show how its expression is used.
- Exactly one option must fit the stated author intent.
- The correct option must contain or directly realize the target quiz phrase.
- The correct option may equal the target phrase when the target phrase is already a complete response.
- Incorrect options must be clearly unsuitable for the stated intent.
- Incorrect options must remain useful English phrase exposure.
- Generated options must not be presented as source quotations.
- Per-option explanations are not required for the first MVP.

### Target quiz phrase

- The target quiz phrase is the reusable expression taught by the interaction.
- The target quiz phrase must express the source author's conversational move.
- The target quiz phrase must remain grounded in the current source post.
- The target quiz phrase may replace technical nouns with pronouns or general nouns.
- The target quiz phrase does not need to reproduce one complete source sentence.
- The target quiz phrase must preserve enough context to show its usage situation.
- Each interaction uses one target quiz phrase in the first MVP.

### Source grounding and attribution

- Every interaction must retain a reference to its corresponding authentic source post.
- The source post must provide evidence for the target phrase's expression or conversational function.
- Source-derived summaries and generated quiz content must remain distinguishable.
- Attribution must remain available for every session-available learning unit.

### Publication boundary

- A learning unit must pass an automated publication gate before becoming session-available.
- The publication gate must evaluate source grounding, summary fidelity, phrase usefulness, option naturalness, and contextual fit.
- Human approval applies to the publication criteria and material changes to those criteria.
- The first MVP does not require human approval for each learning unit.
- A learning unit that no longer passes the gate must become unavailable to new sessions.
- Unavailability must preserve source-post references, source evidence, and attribution.
- Published-content retention and provenance belong to `spec:product.application.published_content` and `spec:product.pipeline`.

## Boundary

| concern | owner |
|---|---|
| Valid learning-path meaning | `spec:product.learning.learning_path` |
| Learner-visible meaning of summaries and quizzes | `spec:product.learning.learning_unit` |
| Card order and progressive session behavior | `spec:product.learning.quiz_session` |
| Generation, validation, and publication-gate implementation | `spec:product.pipeline` |
| Serialized learning-unit package | Future pipeline contract. |
| Concrete UI styling | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.learning` | Parent learning overview. |
| `spec:product.learning.learning_path` | Defines the source-post path used by one learning unit. |
| `spec:product.learning.quiz_session` | Defines progressive presentation of unit interactions. |
| `spec:product.pipeline` | Produces and validates learning units for this contract. |
| PRODUCT-ADR-LEARNING-001 | Establishes technical conversation trees as the primary source. |
| PRODUCT-ADR-LEARNING-005 | Establishes summarized source-post paths, abstracted quiz phrases, and automated publication gating. |
| PRODUCT-ADR-LEARNING-006 | Establishes progressive quiz-to-summary cards. |
