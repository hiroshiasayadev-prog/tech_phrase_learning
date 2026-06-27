# PRODUCT-ADR-PIPELINE-015: Generate and validate semantic quiz options through staged model tasks

- **status**: accepted
- **date**: 2026-06-28
- **depends_on**:
  - PRODUCT-ADR-PIPELINE-002
  - PRODUCT-ADR-PIPELINE-008
  - PRODUCT-ADR-PIPELINE-014
  - PRODUCT-ADR-LEARNING-010
  - PRODUCT-ADR-LEARNING-012
- **supersedes**:
- **migrated_to_spec**:

## Context

Each interaction requires exactly three natural English options and one correct-option reference.
Exactly one option must best fit the Quiz prompt.
The correct option must contain or directly realize the accepted target phrase.

One combined model task can produce overlapping distractors, multiple plausible answers, or one obviously defective option.
Prompt-only role instructions do not isolate failures or prove that each option satisfied its responsibility.

The Pipeline needs staged generation, semantic identities independent from presentation order, individual evaluation, and final set-level evaluation.

## Decision

### Staged generation

Exactly-three-option generation will use three bounded sequential model tasks.

| stage | required output | visible accepted context |
|---|---|---|
| Correct-option generation | One correct option. | Quiz prompt, target phrase, interaction type, conversational function, position, certainty, and minimum preceding context. |
| First-distractor generation | One distractor. | Quiz prompt and accepted correct option, plus required semantic context. |
| Second-distractor generation | One distractor. | Quiz prompt, accepted correct option, and accepted first distractor, plus required semantic context. |

A later option stage will not run until every required earlier option result is accepted.

The correct option will contain or directly realize the target phrase.
The correct option will fit the Quiz prompt and preserve required position and certainty.

Each distractor will:

- remain grammatical and natural English;
- provide useful phrase exposure in another situation;
- remain clearly unsuitable for the current Quiz prompt;
- remain semantically distinct from accepted earlier options;
- avoid unsupported source-specific technical claims.

The Pipeline will not use intentionally broken grammar as a distractor strategy.

### Semantic option identity

Deterministic orchestration will assign one semantic identity to each accepted option.
Option identity will not derive from:

- array position;
- learner-visible labels;
- display order;
- option text.

Deterministic orchestration will create exactly one correct-option reference.
The reference will resolve to the correct option's identity within the same interaction.

The model will not select semantic option identities or determine correctness by generated array position.

### Correct-option evaluation

The correct option will independently pass these semantic evaluation units before distractor generation proceeds:

| evaluation unit | owned judgment |
|---|---|
| Naturalness | The option is grammatical and natural English. |
| Target-phrase realization | The option contains or directly realizes the accepted target phrase. |
| Prompt fit | The option appropriately answers the accepted Quiz prompt. |
| Meaning preservation | The option preserves required position, certainty, and conversational function. |

### Distractor evaluation

Each distractor will independently pass these semantic evaluation units before the next option stage proceeds:

| evaluation unit | owned judgment |
|---|---|
| Naturalness and usefulness | The distractor is natural, grammatical, and useful English in another situation. |
| Prompt mismatch | The distractor is clearly unsuitable for the accepted Quiz prompt. |
| Unsupported-claim avoidance | The distractor introduces no unsupported source-specific technical claim. |

### Set-level evaluation

After three accepted individual options exist, the complete option set will receive three independent semantic evaluation units.

| evaluation unit | owned judgment |
|---|---|
| Exactly one best fit | The correct-option reference identifies the only option that best fits the Quiz prompt. |
| Pairwise semantic distinction | No two options are semantic duplicates or near-equivalent answers. |
| No trivial answer cue | Grammar, length, wording, or prompt-copying patterns do not reveal the answer without understanding intent. |

All required individual and set-level evaluations must pass.

### Deterministic validation

Deterministic validation will establish:

- exactly three non-empty options;
- three unique semantic option identities;
- no exact duplicate option text;
- one same-interaction correct-option reference;
- successful reference resolution;
- complete unique evaluation coverage;
- non-contradictory verdicts;
- option-identity independence from position, labels, display order, and text;
- generated-source separation.

Only a complete accepted three-option set may enter Learning Unit materialization.

## Rationale

Sequential option generation isolates failures and lets later distractors avoid accepted earlier meanings.
Individual evaluation prevents an invalid option from entering set-level judgment.

Set-level evaluation catches multiple-correct-answer and answer-cue failures that individual checks cannot detect.
Deterministic identity and correctness preserve behavior under shuffled presentation.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Generate all three options in one model task | One response can conflate roles, duplicate options, or produce multiple correct answers. |
| Use one prompt with internal role instructions only | Prompt structure does not create independently observable generation outcomes. |
| Assign option identity from array position | Presentation shuffling would change semantic identity. |
| Use option text as identity | Regeneration or text correction would change correctness semantics. |
| Validate options only as a set | One defective option may hide behind an otherwise plausible set verdict. |
| Validate options only individually | Multiple individually plausible options can create more than one correct answer. |
| Make distractors intentionally ungrammatical | Learners could answer through superficial cues rather than conversational meaning. |

## Consequences

- Option generation requires three sequential bounded model tasks.
- Correct-option acceptance gates distractor generation.
- First-distractor acceptance gates second-distractor generation.
- Individual acceptance does not replace final set-level evaluation.
- Option identity and correct-option reference are deterministic Pipeline outputs.
- UI shuffling can preserve immutable correctness semantics.
- Stage-specific provider, prompt, and validation provenance remains governed by PRODUCT-ADR-PIPELINE-008.
- Concrete identity encoding, prompts, models, schemas, thresholds, and retry execution remain deferred.

## Evidence

- PRODUCT-ADR-LEARNING-010 establishes semantic option identity and correct-option references independent from presentation order.
- PRODUCT-ADR-LEARNING-012 establishes option naturalness and contextual fit as non-compensating readiness dimensions.
- PRODUCT-ADR-PIPELINE-014 supplies accepted target phrases and non-revealing Quiz prompts.
- PRODUCT-INV-PIPELINE-001 provides non-normative evidence from combined quiz-generation prompts and reviewed output failures.
- The user selected explicit correct-option and distractor generation stages, deterministic identities, individual evaluation, and final set-level evaluation.
