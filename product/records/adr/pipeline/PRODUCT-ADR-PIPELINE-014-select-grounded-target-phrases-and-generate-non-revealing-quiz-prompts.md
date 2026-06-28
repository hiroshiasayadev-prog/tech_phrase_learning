# PRODUCT-ADR-PIPELINE-014: Select grounded target phrases and generate non-revealing quiz prompts

- **status**: accepted
- **date**: 2026-06-28
- **depends_on**:
  - PRODUCT-ADR-PIPELINE-002
  - PRODUCT-ADR-PIPELINE-008
  - PRODUCT-ADR-PIPELINE-012
  - PRODUCT-ADR-PIPELINE-013
  - PRODUCT-ADR-LEARNING-005
  - PRODUCT-ADR-LEARNING-012
- **supersedes**:
- **migrated_to_spec**: 2026-06-28

## Context

Each selected source post requires one target phrase and one Quiz prompt.
The target phrase must remain grounded in authentic source wording while minimizing source-specific technical detail.
The Quiz prompt must state the communicative situation without revealing the answer wording.

Free target-phrase generation can drift from the source conversational move.
Giving target-phrase text to the prompt generator can leak the answer into the problem statement.
The Pipeline needs separate bounded stages and independent validation for both artifacts.

## Decision

### Target-phrase selection input

Target-phrase selection will run after path-specific summary acceptance.
Each selection unit will receive:

- valid Learning Path identity;
- target authentic-post identity;
- question or reply interaction type;
- one to three accepted phrase-evidence candidates from the target post;
- accepted path-specific summary;
- structured position;
- structured certainty or qualification;
- structured conversational response meaning;
- every preceding accepted path-specific summary;
- target post's complete authored text.

Later-post context will be excluded.

### Grounded transformation

The stage will select exactly one accepted phrase-evidence candidate.
It will produce exactly one target phrase as an unchanged or generalized transformation of that candidate.

Permitted transformations include:

- replacing technical nouns with pronouns or general nouns;
- extracting the reusable conversational span from a longer sentence;
- adding minimum context needed to demonstrate usage;
- applying minor grammatical adjustment.

The transformation must preserve:

- conversational function;
- source-author position;
- source-author certainty or qualification;
- target-post grounding.

The stage will not create a target phrase without a selected same-post evidence candidate.
It will not combine wording from another post.

Output will identify:

- target authentic-post identity;
- selected phrase-evidence reference;
- target phrase;
- conversational function;
- unchanged or generalized transformation kind;
- transformation explanation.

### Target-phrase validation

Every target phrase will receive three independent semantic evaluation units.

| evaluation unit | owned judgment |
|---|---|
| Grounded transformation | The target phrase remains traceable to selected evidence and preserves function, position, certainty, and valid technical generalization. |
| Phrase usefulness | The target phrase is natural, reusable conversational English rather than technical vocabulary alone. |
| Contextual sufficiency | The target phrase preserves enough wording to show usage and fits the interaction role and preceding path context. |

All three units must pass.

Deterministic validation will establish:

- exactly one target phrase per interaction;
- a resolvable same-post accepted evidence reference;
- matching path and post identities;
- non-empty target text;
- mutually exclusive unchanged or generalized classification;
- exclusion of later-post context;
- complete unique evaluation coverage;
- generated-source separation.

### Quiz-prompt generation input

Quiz-prompt generation will run after target-phrase acceptance.
The generator will receive:

- valid Learning Path identity;
- target authentic-post identity;
- question or reply interaction type;
- accepted path-specific summary;
- structured position;
- structured certainty or qualification;
- structured conversational response meaning;
- accepted target phrase's conversational function;
- every preceding accepted path-specific summary.

The generator will not receive:

- target-phrase text;
- selected phrase-evidence wording;
- current authored text;
- answer options;
- later-post context.

The existing validated semantic fields will supply the intended communicative meaning.
The Pipeline will not add another intent-extraction stage.

The generated English prompt will:

- state the communicative situation;
- preserve position and certainty;
- match the interaction role;
- minimize source-specific technical detail;
- include only enough context to judge answer options;
- avoid revealing the target phrase or near-verbatim wording.

### Quiz-prompt validation

Every Quiz prompt will receive three independent semantic evaluation units.

| evaluation unit | owned judgment |
|---|---|
| Intent fidelity | The prompt preserves communicative intent, position, certainty, and interaction role. |
| Answer leakage | The prompt does not directly or semantically disclose the accepted target phrase. |
| Prompt usability | The prompt gives enough situation detail to distinguish options while remaining concise and technically minimal. |

All three units must pass.

Deterministic validation will establish:

- exactly one non-empty prompt per interaction;
- matching path and post identities;
- absence of exact target-phrase text;
- exclusion of later-post context;
- complete unique evaluation coverage;
- generated-source separation.

Only accepted target phrases and prompts may enter option generation.

## Rationale

Selecting one accepted evidence candidate before transformation preserves an explicit grounding chain.
Permitting narrow generalization supports reusable phrase learning without free semantic invention.

Withholding target-phrase text from the prompt generator reduces direct answer leakage.
Existing structured meaning avoids an unnecessary additional extraction task.

Independent evaluations distinguish grounding, learning usefulness, context sufficiency, intent fidelity, leakage, and prompt usability.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Generate a target phrase directly from the summary | The result would lack explicit traceability to authentic phrase evidence. |
| Require exact source wording as the target phrase | Source wording may contain technical detail that limits reuse. |
| Combine target-phrase selection and Quiz prompt generation | One task can leak answer wording and blur grounding failures. |
| Give target-phrase text to the prompt generator | The model can reproduce or closely paraphrase the answer. |
| Add a separate intent-extraction stage | Accepted structured summary meaning already provides the required intent representation. |
| Use one combined evaluation for each artifact | One pass can hide failure in an independently required dimension. |

## Consequences

- Each interaction traces one target phrase to one accepted same-post phrase-evidence candidate.
- Target phrases may generalize technical wording without changing conversational meaning.
- Quiz prompts derive from validated meaning rather than answer text.
- Option generation consumes only accepted target phrases and prompts.
- Stage-specific provider, prompt, and validation provenance remains governed by PRODUCT-ADR-PIPELINE-008.
- Concrete prompts, models, schemas, thresholds, and retry execution remain deferred.

## Evidence

- PRODUCT-ADR-LEARNING-005 separates target-phrase selection from quiz generation and permits technical generalization.
- PRODUCT-ADR-LEARNING-012 establishes source grounding, phrase usefulness, contextual fit, and generated-source separation.
- PRODUCT-ADR-PIPELINE-012 establishes accepted same-post phrase evidence.
- PRODUCT-ADR-PIPELINE-013 establishes accepted preceding path context.
- The user selected evidence-backed transformation, three independent target-phrase checks, answer-text withholding, no extra intent stage, and three independent prompt checks.
