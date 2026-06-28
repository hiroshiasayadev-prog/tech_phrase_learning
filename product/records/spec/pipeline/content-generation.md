# Concept: Learning content generation

- **id**: `spec:product.pipeline.content_generation`
- **status**: draft
- **date**: 2026-06-28
- **parent**: `spec:product.pipeline`

## What this is

Pipeline contract for generating reusable summaries, source-grounded phrase evidence, path-specific summaries, target phrases, Quiz prompts, and semantic options.
The contract defines accepted stage inputs and outputs without redefining learner-visible meaning.

## Non-goals

- Learner-visible summary, phrase, prompt, option, or interaction meaning.
- Concrete prompts, models, thresholds, token budgets, or serialized schemas.
- Retry counts, fallback, or scheduling.
- Publication-gate authorization.
- UI option shuffling or session behavior.

## Concept model

| stage artifact | reuse scope | required downstream role |
|---|---|---|
| Reusable source-post summary | Shared across compatible sibling paths. | Path filtering, phrase extraction, and later path-specific revision. |
| Source-grounded phrase evidence | Shared across compatible sibling paths. | Path suitability and target-phrase selection. |
| Path-specific summary | One valid Learning Path. | Learner-visible summary and later path-local generation. |
| Target phrase | One interaction in one valid path. | Correct-option generation and learner phrase exposure. |
| Quiz prompt | One interaction in one valid path. | Option generation and contextual-fit validation. |
| Correct option | One interaction. | One option identified by the correct-option reference. |
| Distractor | One interaction. | Natural but unsuitable alternative phrase exposure. |
| Complete option set | One interaction. | Exactly three accepted semantic options. |

## Rules

### Accepted-input rule

- Every generation stage must consume only declared accepted upstream artifacts.
- A stage must report `incomplete_input` when any required accepted input is absent or incomplete.
- A non-accepted model result must not enter a downstream stage.
- Later-post context must remain excluded from stages that do not authorize it.
- Generated content must remain distinguishable from authentic source-authored wording.

### Reusable source-post summary

Reusable-summary generation must receive:

- target authentic-post identity and complete authored text;
- source binding and quote-boundary evidence;
- every accepted reusable summary on the mechanically derived ancestor chain;
- ancestor summaries ordered from the opening post to the immediate predecessor.

- Opening-post generation receives no prior summary context.
- Sibling, later, unrelated, and unvalidated content must remain excluded.
- Resolved quote evidence may enter as separated context.
- Quoted evidence must not establish the target author's position or phrase evidence.
- Silent authored-text truncation is invalid.
- Generation may begin only after complete authored-text coverage is established.

Reusable-summary output must keep these semantic elements distinct:

- target authentic-post identity;
- reusable English summary text;
- source-author position or question;
- source-author certainty or qualification;
- conversational response meaning.

Every structurally valid summary must receive independent evaluations for:

- position fidelity;
- certainty fidelity;
- response-meaning fidelity;
- unsupported claims and attribution.

- Each valid pass must provide a non-empty explanation and exact target-authored evidence.
- Deterministic validation must confirm identity, evidence membership, quote exclusion, coverage, and non-contradiction.
- Any valid semantic failure rejects the reusable summary.
- Only accepted reusable summaries may enter ancestor context, phrase extraction, or path filtering.

### Source-grounded phrase evidence

Phrase-evidence extraction must be separate from summary generation.

The extraction unit must receive:

- target post identity and complete authored text;
- required question or reply interaction role;
- accepted reusable summary;
- ordered accepted ancestor summaries;
- quote-boundary evidence.

- Each candidate span must come from the target post's authored text.
- Quoted text must not qualify as target-author phrase evidence.
- Extraction must return zero to three candidates per target post.
- Zero candidates is a valid semantic result, not provider failure or invalid output.

Each non-zero candidate must identify:

- target authentic-post identity;
- exact authored-text span;
- source location sufficient to distinguish repeated text;
- required interaction role;
- conversational function.

Deterministic checks must confirm identity, exact membership, source location, quote exclusion, role, cardinality, and unique spans.

Each mechanically valid candidate must independently pass:

- conversational-function fit;
- phrase usefulness.

- Accepted phrase evidence must contain reusable conversational English beyond technical vocabulary alone.
- One failed candidate must not reject accepted sibling candidates.
- A zero-candidate result requires separate semantic confirmation over the complete authored post.
- Bare model assertion must not establish accepted zero-candidate meaning.
- Only accepted phrase evidence may enter path filtering or target-phrase selection.

### Path-specific summary revision

Path-specific revision may begin only after candidate retention as a valid Learning Path.

Each revision unit must receive:

- valid Learning Path identity;
- target post identity;
- accepted reusable summary and structured meaning;
- every preceding accepted path-specific summary for the same path.

- Posts must be processed in source order.
- Later-post context must remain excluded.
- An unaccepted preceding revision must not enter the next unit.
- An unchanged summary result is valid.

Each revision result must identify:

- valid Learning Path identity;
- target authentic-post identity;
- revised summary or unchanged outcome;
- reason for every textual change.

Revision may improve reference clarity, continuity, repetition, and technical compression.
Revision must preserve position, certainty, response meaning, required technical claims, attribution, source grounding, accepted phrase evidence, and path identity.

Each revised or unchanged result must independently pass:

- semantic preservation;
- path continuity.

Deterministic checks must confirm matching identities, one result per post, source order, result exclusivity, accepted reusable input, later-context exclusion, complete evaluation coverage, and non-contradiction.

### Target-phrase selection

Target-phrase selection may begin only after path-specific summary acceptance.

Each selection unit must receive:

- valid path and target-post identities;
- interaction type;
- one to three accepted same-post phrase-evidence candidates;
- accepted path-specific summary and structured meaning;
- every preceding accepted path-specific summary;
- complete target authored text.

- Later-post context must remain excluded.
- The stage must select exactly one accepted same-post evidence candidate.
- The stage must produce exactly one unchanged or generalized target phrase.
- The stage must not create a phrase without selected same-post evidence.
- The stage must not combine wording from another post.

Each target-phrase result must identify:

- target authentic-post identity;
- selected accepted phrase-evidence reference;
- target phrase;
- conversational function;
- unchanged or generalized transformation kind;
- transformation explanation.

Permitted transformation may replace technical nouns, extract a reusable span, add minimum usage context, or apply minor grammatical adjustment.
The transformation must preserve conversational function, source-author position, certainty, and target-post grounding.

Every target phrase must independently pass:

- grounded transformation;
- phrase usefulness;
- contextual sufficiency.

Deterministic checks must confirm one phrase, resolvable same-post evidence, matching identities, non-empty text, transformation-kind exclusivity, later-context exclusion, coverage, and generated-source separation.

### Quiz-prompt generation

Quiz-prompt generation may begin only after target-phrase acceptance.

The generator may receive:

- valid path and target-post identities;
- interaction type;
- accepted path-specific summary and structured meaning;
- accepted target phrase's conversational function;
- every preceding accepted path-specific summary.

The generator must not receive:

- target-phrase text;
- selected phrase-evidence wording;
- current authored text;
- answer options;
- later-post context.

- Existing validated semantic fields must supply communicative intent.
- The Pipeline must not add a separate intent-extraction stage.
- The prompt must preserve position, certainty, and interaction role.
- The prompt must minimize technical detail and provide only enough context to judge options.
- The prompt must not reveal the target phrase or near-verbatim answer wording.

Every Quiz prompt must independently pass:

- intent fidelity;
- answer leakage;
- prompt usability.

Deterministic checks must confirm one non-empty prompt, matching identities, absence of exact target-phrase text, later-context exclusion, coverage, and generated-source separation.

### Semantic option generation

Exactly three options must be generated through sequential bounded stages.

| stage | visible accepted context | required output |
|---|---|---|
| Correct-option generation | Quiz prompt, target phrase, interaction type, conversational function, position, certainty, and minimum accepted preceding path context. | One correct-option candidate. |
| First-distractor generation | Quiz prompt, accepted correct option, interaction type, conversational function, position, certainty, and minimum accepted preceding path context. | One first-distractor candidate. |
| Second-distractor generation | Quiz prompt, accepted correct option, accepted first distractor, interaction type, conversational function, position, certainty, and minimum accepted preceding path context. | One second-distractor candidate. |

- Minimum preceding context means only the accepted earlier path context required to preserve the current interaction meaning.
- The accepted target phrase is a direct input only to correct-option generation because that stage must realize the phrase.
- Distractor stages receive target wording only through accepted earlier option text, not as a separate target-phrase input.
- Distractor generation must receive accepted earlier options but must not depend on presentation order or learner-visible labels.
- Later-post context and unaccepted path context must remain excluded from every option stage.
- A later stage must not start until every required earlier option is accepted.
- The correct option must contain or directly realize the target phrase.
- The correct option must fit the prompt and preserve position, certainty, and function.
- Each distractor must be grammatical, natural, useful in another situation, clearly unsuitable for the current prompt, semantically distinct, and free of unsupported technical claims.
- The Pipeline must not use intentionally broken grammar as a distractor strategy.

The correct option must independently pass:

- naturalness;
- target-phrase realization;
- prompt fit;
- meaning preservation.

Each distractor must independently pass:

- naturalness and usefulness;
- prompt mismatch;
- unsupported-claim avoidance.

After individual acceptance, the complete set must independently pass:

- exactly one best fit;
- pairwise semantic distinction;
- no trivial answer cue.

### Option identity and completion

- Deterministic orchestration must assign one semantic identity to each accepted option.
- Option identity must not derive from array position, display label, display order, or option text.
- Deterministic orchestration must create one correct-option reference resolving to the correct option identity in the same interaction.
- Models must not assign option identities or determine correctness through array position.
- Deterministic validation must confirm exactly three non-empty options, unique identities, no exact duplicate text, one resolvable correct reference, complete evaluation coverage, non-contradiction, identity independence, and generated-source separation.
- Only a complete accepted option set may enter Learning Unit materialization.

## Boundary

| concern | owner |
|---|---|
| Learner-visible meaning and cardinality | `spec:product.learning.learning_unit`. |
| Generation stages and accepted artifact dependencies | `spec:product.pipeline.content_generation`. |
| Common result categories and completion aggregation | `spec:product.pipeline.validation`. |
| Provider invocation | `spec:product.pipeline.llm_provider`. |
| Retry, rerun, and stage progression | `spec:product.pipeline.orchestration`. |
| Shared and path-specific artifact provenance | `spec:product.pipeline.artifact_identity_and_provenance`. |
| UI option shuffling | `spec:product.learning.quiz_session` and `spec:product.ui`. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.pipeline` | Parent Pipeline overview. |
| `spec:product.pipeline.path_validation` | Consumes reusable artifacts and supplies retained valid paths. |
| `spec:product.pipeline.validation` | Defines common stage outcomes and content-validation completion. |
| `spec:product.pipeline.artifact_identity_and_provenance` | Defines shared, path-specific, and current provenance. |
| `spec:product.learning.learning_unit` | Defines learner-visible content and readiness meaning. |
| PRODUCT-ADR-PIPELINE-011 | Establishes reusable-summary generation and evaluation. |
| PRODUCT-ADR-PIPELINE-012 | Establishes source-grounded phrase evidence. |
| PRODUCT-ADR-PIPELINE-013 | Establishes path-specific summary revision. |
| PRODUCT-ADR-PIPELINE-014 | Establishes target phrases and non-revealing Quiz prompts. |
| PRODUCT-ADR-PIPELINE-015 | Establishes sequential option generation and deterministic identity. |
