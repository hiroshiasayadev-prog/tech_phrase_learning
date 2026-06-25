# Overview: Learning

- **id**: `spec:product.learning`
- **status**: draft
- **date**: 2026-06-26
- **parent**: `spec:product`

## What this is

Owner of the learner-facing product concept and phrase-exposure semantics.
The area remains valid when content-processing technology changes.

## Current contract

| concept | contract |
|---|---|
| Initial audience | Engineers who can already read technical English. |
| Primary learning gap | Limited exposure to natural conversational phrasing in familiar technical situations. |
| Primary source | Real technical conversation trees. |
| Learning path | Use an ordered source-post sequence that begins with an opening post and continues through replies. |
| Path multiplicity | One discussion may provide zero or more independently valid paths. |
| Learning-unit multiplicity | One valid path may support zero or more learning units. |
| Interaction types | Use question-formulation and reply-formulation interactions. |
| Quiz abstraction | Use one concise intent prompt and three natural English candidate responses per selected post. |
| Target phrase | Use one technically abstracted reusable expression per interaction. |
| Correct option | Use or directly realize the target phrase in the one response that fits the prompt. |
| Source representation | Reveal a validated English source-post summary after the learner answers. |
| Session composition | Require every MVP session to contain at least one question interaction and one reply interaction. |
| Session progression | Replace each active quiz card with an answered summary card before showing the next quiz. |
| Language | Use English for all learner-facing content. |
| Publication gate | Use automated publication gating under human-approved criteria. |

## Non-goals

- Source acquisition and API integration.
- Conversation parsing and normalization algorithms.
- Path enumeration and filtering mechanics.
- LLM model selection or provider integration.
- Runtime learning-unit selection and availability-aware retrieval.
- PWA runtime state, navigation, loading, and retry behavior.
- Deployment, persistence, and concrete UI architecture.

## Boundary

| content | owner |
|---|---|
| Target learner, learning gap, and source-context model | `spec:product.learning.learning_model`. |
| Meaning and suitability of a learning path | `spec:product.learning.learning_path`. |
| Learner-visible learning-unit semantics | `spec:product.learning.learning_unit`. |
| Session card progression and reveal behavior | `spec:product.learning.quiz_session`. |
| PWA runtime state, navigation, loading, and retry behavior | `spec:product.ui`. |
| Ingestion, path enumeration, filtering, generation, and validation | `spec:product.pipeline`. |
| LLM provider and model integration | `spec:product.pipeline`. |
| Runtime learning-unit selection and retrieval | `spec:product.application.learning_unit_selection`. |

## Topics

| title | kind | ref | summary |
|---|---|---|---|
| Learning model | Concept | `spec:product.learning.learning_model` | Target learner, learning gap, source-context model, and phrase-exposure model. |
| Learning path | Concept | `spec:product.learning.learning_path` | Valid source-post sequence meaning and path-to-learning-unit relationship. |
| Learning unit | Concept | `spec:product.learning.learning_unit` | English summaries, intent prompts, target phrases, answer options, grounding, and publication semantics. |
| Quiz session | Concept | `spec:product.learning.quiz_session` | Progressive quiz-to-summary card composition and transition behavior. |

## Related specs

| ref | relation |
|---|---|
| `spec:product` | PRODUCT placement router and dependency direction. |
| `spec:product.pipeline` | Implements content production for this learning contract. |
| `spec:product.application` | Selects and retrieves published learning units. |
| `spec:product.ui` | Implements the transient PWA flow for this learning contract. |
| PRODUCT-ADR-LEARNING-001 | Establishes technical conversation trees as the primary learning source. |
| PRODUCT-ADR-LEARNING-005 | Establishes summarized source-post paths, learning-unit generation, and publication gating. |
| PRODUCT-ADR-LEARNING-006 | Establishes progressive quiz-to-summary cards. |
