# Concept: Learning model

- **id**: `spec:product.learning.learning_model`
- **status**: draft
- **date**: 2026-06-25
- **parent**: `spec:product.learning`

## What this is

Learner, learning-gap, source-context, and phrase-exposure model for the product.
The model remains independent from pipeline implementation and concrete UI technology.

## Non-goals

- Learning-unit field semantics.
- Quiz-session progression.
- Source ingestion and processing mechanics.
- LLM provider and model selection.
- General grammar, vocabulary, TOEIC, or daily-conversation instruction.

## Concept model

| topic | contract |
|---|---|
| Initial audience | Engineers who can already read technical English. |
| Primary learning gap | Limited exposure to natural conversational phrasing in familiar technical situations. |
| Primary source | Real technical conversation trees. |
| Context model | Preserve enough parent, ancestor, and reply context to explain conversational intent. |
| Learning focus | Reusable phrases for initiating and responding within technical conversations. |
| Participation model | Teach both question formulation and reply formulation. |
| Generated content | May supplement source material but does not replace observed conversation as the primary source. |
| Quiz role | Provide structured exposure to natural alternative phrasings rather than strict knowledge assessment. |

## Rules

- Technical familiarity must reduce subject-matter load during phrase learning.
- Learning content must prioritize reusable conversational phrasing.
- Learning content must preserve enough context to explain phrase intent.
- Every MVP session must expose both question and reply formulation.
- Question formulation must use an authentic opening post as its source target.
- Reply formulation must use an authentic reply as its source target.
- Generated choices may express different intents when each choice remains natural and useful.
- The initial product must remain focused on engineers.
- Broader native content remains a later expansion.

## Boundary

| concern | owner |
|---|---|
| Target learner and learning gap | `spec:product.learning.learning_model` |
| Source-context and phrase-exposure model | `spec:product.learning.learning_model` |
| Learning-path suitability | `spec:product.learning.learning_path` |
| Learner-visible learning-unit semantics | `spec:product.learning.learning_unit` |
| Session progression and reveal behavior | `spec:product.learning.quiz_session` |
| Ingestion, extraction, generation, and validation | `spec:product.pipeline` |

## Related specs

| ref | relation |
|---|---|
| `spec:product.learning` | Parent learning overview. |
| `spec:product.learning.learning_path` | Defines suitable source-post paths for learning-unit generation. |
| `spec:product.learning.learning_unit` | Defines the learner-visible content unit. |
| `spec:product.learning.quiz_session` | Defines the learner-visible session flow. |
| PRODUCT-ADR-LEARNING-001 | Establishes technical conversation trees as the primary learning source. |
| PRODUCT-ADR-LEARNING-005 | Establishes the current mixed question-and-reply learning-unit model. |
