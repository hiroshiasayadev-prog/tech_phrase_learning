# Concept: Learning unit

- **id**: `spec:product.learning.learning_unit`
- **status**: draft
- **date**: 2026-06-27
- **parent**: `spec:product.learning`

## What this is

Learner-visible semantic model for phrase quizzes generated from one valid learning path.
The model separates generated quiz content, source-derived summaries, and authentic source evidence.

## Non-goals

- Source ingestion and conversation-tree construction.
- Learning-path enumeration and filtering.
- LLM provider selection and prompt design.
- Publication-gate schemas, thresholds, retries, and algorithms.
- Serialized package and persistence schemas.
- Concrete component styling and responsive layout.
- Runtime learner-answer state.
- Option-shuffle generation and storage.

## Concept model

| element | origin | learner-visible purpose |
|---|---|---|
| Learning-path reference | Source-derived | Identifies the ordered source-post sequence used by the unit. |
| Source discussion title | Source metadata | Identifies the original discussion represented by the unit. |
| Interaction type | Defined | Distinguishes question formulation from reply formulation. |
| Quiz prompt | Generated and validated | States what the source author intends to communicate. |
| Answer option | Generated and validated | Presents one natural English candidate response to the stated intent. |
| Option identity | Defined | Identifies one semantic option within its interaction. |
| Correct-option reference | Defined | Identifies the one option that best fits the prompt. |
| Target quiz phrase | Generated and validated | Identifies the reusable expression taught by the interaction. |
| Source-post summary | Source-derived and validated | Reveals the technical meaning of the corresponding source post after the answer. |
| Source evidence | Authentic source reference | Grounds the summary, conversational move, and target phrase in the corresponding source post. |
| Attribution record | Source metadata and required disclosure | Identifies the source, selected authors, license, adaptation, and no-endorsement terms. |

## Cardinality

| relationship | contract |
|---|---|
| Learning unit to learning path | One learning unit references exactly one valid learning path. |
| Learning path to learning unit | Each valid learning path defines exactly one learning unit. |
| Learning unit to source discussion title | Every learning unit has exactly one original source discussion title. |
| Learning unit to interaction | Every first-MVP learning unit has two to six ordered interactions. |
| Selected source post to interaction | Every selected source post has exactly one interaction in the first MVP. |
| Interaction to source-post summary | Every interaction has exactly one learner-visible summary. |
| Interaction to quiz prompt | Every interaction has exactly one prompt. |
| Interaction to answer option | Every interaction has exactly three answer options. |
| Answer option to option identity | Every answer option has exactly one semantic identity. |
| Interaction to correct-option reference | Every interaction has exactly one correct-option reference. |
| Interaction to target quiz phrase | Every interaction has exactly one target phrase. |
| Learning unit to attribution record | Every learning unit has exactly one unit-specific attribution record. |

## Rules

### Unit composition

- Every first-MVP learning unit must contain exactly one question-formulation interaction.
- Every first-MVP learning unit must contain one to five reply-formulation interactions.
- The first interaction must correspond to the source discussion opening post.
- Every later interaction must correspond to an authentic reply in the selected path.
- Interaction order must match source-post order.
- Every selected source post must have one interaction.
- Stable learning-unit identity is anchored to valid learning-path identity.
- Generated-content changes must not change the logical learning-unit identity.
- Target phrases, quiz prompts, answer options, option identities, and correct-option references are not learning-unit identity inputs.
- Source-post summaries, model identity, prompt versions, and validation implementations are not learning-unit identity inputs.
- A different valid path creates a different learning unit.

### Discussion title

- The learning unit must retain the original source discussion title.
- The source discussion title is the learner-visible discussion title for the first MVP.
- The title must identify the discussion referenced by the learning path.
- The first MVP must not replace the source title with a generated or path-specific title.

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

- Every answer option must be grammatical and natural English.
- Every answer option must minimize source-specific technical detail.
- Every answer option must preserve enough situation detail to show how its expression is used.
- Exactly one option must best fit the stated author intent.
- The option referenced as correct must contain or directly realize the target quiz phrase.
- The correct option may equal the target phrase when the target phrase is already a complete response.
- Incorrect options must be clearly unsuitable for the stated intent.
- Incorrect options must remain useful English phrase exposure.
- Generated options must not be presented as source quotations.
- Per-option explanations are not required for the first MVP.

### Option identity and correctness

- Every option must have one semantic identity within its interaction.
- Option identities must be unique within the interaction.
- The correct-option reference must resolve to exactly one option in the same interaction.
- Generated array position must not define option identity.
- Learner-visible labels such as `A`, `B`, and `C` must not define option identity.
- Display order must not define option identity.
- Option text must not define option identity.
- Option identity must remain stable within the current published learning-unit content.
- Option identity does not need to remain stable after published-content replacement.
- The learner's selected semantic option identity is sufficient to derive correctness from immutable unit content.
- Display shuffling and permutation state remain outside this specification.

### Target quiz phrase

- The target quiz phrase is the reusable expression taught by the interaction.
- The target quiz phrase must express the source author's conversational move.
- The target quiz phrase must remain grounded in the current source post.
- The target quiz phrase may replace technical nouns with pronouns or general nouns.
- The target quiz phrase does not need to reproduce one complete source sentence.
- The target quiz phrase must preserve enough context to show its usage situation.
- Each interaction uses one target quiz phrase in the first MVP.

### Source grounding and generated-source separation

- Every interaction must retain a reference to its corresponding authentic source post.
- The source post must support the interaction's summary, conversational move, and target phrase.
- Source-derived summaries and generated quiz content must remain distinguishable.
- Generated prompts, summaries, phrases, and options must not be presented as authentic quotations.
- Generated content must not be attributed as source-authored wording.

### Attribution and source-use boundary

- The accepted `discuss.python.org` corpus is limited to noncommercial first-MVP use.
- Commercial release with that corpus requires separate permission, corpus replacement, or qualified legal confirmation.
- Every learning unit must retain one learner-accessible attribution record.
- The attribution record must contain the original source discussion title.
- The attribution record must identify `Discussions on Python.org` as the source platform.
- The attribution record must contain one direct URL to the original discussion.
- The attribution record must contain every selected source-post author's displayed username.
- The attribution record must identify `CC BY-NC-SA 3.0` and provide a license link.
- The attribution record must disclose that learner-visible material was generated, summarized, or adapted from the linked discussion.
- The attribution record must state that attribution does not imply endorsement by source authors, the Python Software Foundation, or the source platform.
- The first MVP does not require a separate direct URL for every selected post.
- Global legal notices must identify the accepted `discuss.python.org` corpus and `Discussions on Python.org` source platform.
- Global legal notices must identify `CC BY-NC-SA 3.0` and provide a license link.
- Global legal notices must disclose that learner-visible material is generated, summarized, or adapted from source discussions.
- Global legal notices must disclose the noncommercial first-MVP source-use boundary.
- Global legal notices must disclose that the source license includes a share-alike condition.
- Global legal notices must state that attribution does not imply endorsement by source authors, the Python Software Foundation, or the source platform.
- Attribution presentation and interaction mechanisms belong to `spec:product.ui`.

### Publication readiness

A learning unit is publication-ready only when structural readiness and semantic readiness both pass.

#### Structural readiness

- The referenced learning path must satisfy `spec:product.learning.learning_path`.
- Every selected source post must have exactly one interaction.
- Every required field must be present and non-empty.
- Every interaction must have exactly three answer options.
- Option identities must be unique within each interaction.
- Exactly one correct-option reference must resolve within each interaction.
- Every interaction must retain a route to its authentic source post.
- Source-derived content and generated content must remain distinguishable.
- Unit-specific attribution must be complete.
- Every required automated evaluation result must cover the complete unit scope.
- Internally contradictory gate results must reject the unit.

#### Semantic readiness

| dimension | publication-ready meaning |
|---|---|
| Path coherence | The ordered summaries and interactions remain understandable as one connected technical exchange. |
| Per-post quiz suitability | Every selected source post supports one useful phrase-learning interaction. |
| Source grounding | Each summary, conversational move, and target phrase remains supported by its authentic source post. |
| Summary fidelity | Each summary preserves the source author's position, certainty, and response without unsupported claims. |
| Phrase usefulness | Each target phrase is natural, reusable conversational English rather than technical vocabulary alone. |
| Option naturalness | Every option is grammatical, natural, useful English without unsupported technical claims. |
| Contextual fit | Exactly one option best fits the prompt and directly realizes the target phrase. |
| Generated-source separation | Generated content is not presented as authentic quotation or source-authored wording. |

#### Decision and approval boundary

- Failure of any required structural or semantic dimension must block publication.
- An aggregate score must not compensate for a failed required dimension.
- Routine units may become available through an approved automated per-unit gate.
- A model-only success result is insufficient for publication readiness.
- The automated gate must combine deterministic validation with semantic quality evaluation.
- Humans must approve the publication-readiness criteria.
- Humans must approve representative golden and harder evaluation fixtures.
- An automated gate configuration must be validated against the approved representative golden and harder fixtures before unattended publication is approved.
- Humans must approve material changes to the criteria or their intended meaning.
- Humans must resolve borderline policy judgments not covered by accepted criteria.
- The first MVP does not require human approval for every learning unit.
- Concrete models, prompts, thresholds, retries, schemas, and gate algorithms belong to `spec:product.pipeline`.
- A unit that no longer passes the approved gate must become unavailable to new sessions.
- Unavailability must preserve source-post references, source evidence, and attribution.

## Boundary

| concern | owner |
|---|---|
| Valid learning-path meaning | `spec:product.learning.learning_path` |
| Learner-visible meaning of summaries, quizzes, title, identities, and attribution | `spec:product.learning.learning_unit` |
| Card order, progressive behavior, and shuffled-presentation constraints | `spec:product.learning.quiz_session` |
| Option-permutation generation, storage, and restoration | `spec:product.ui` |
| Attribution presentation and interaction behavior | `spec:product.ui` |
| Generation, validation, and publication-gate implementation | `spec:product.pipeline` |
| Published-content retention and runtime availability | `spec:product.application.published_content` and `spec:product.pipeline` |
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
| PRODUCT-ADR-LEARNING-007 | Establishes two to six interactions through path cardinality. |
| PRODUCT-ADR-LEARNING-009 | Establishes the original source discussion title. |
| PRODUCT-ADR-LEARNING-010 | Establishes interaction-local option identity and correct-option references. |
| PRODUCT-ADR-LEARNING-011 | Establishes noncommercial source use and unit-specific attribution. |
| PRODUCT-ADR-LEARNING-012 | Establishes structural and semantic publication readiness. |
