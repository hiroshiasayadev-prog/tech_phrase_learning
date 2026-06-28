# PRODUCT-ADR-PIPELINE-023: Filter Learning Path candidates through independent semantic evaluations with implementation-configured retry

- **status**: accepted
- **date**: 2026-06-28
- **depends_on**:
  - PRODUCT-ADR-PIPELINE-002
  - PRODUCT-ADR-PIPELINE-008
  - PRODUCT-ADR-PIPELINE-009
  - PRODUCT-ADR-PIPELINE-022
  - PRODUCT-ADR-LEARNING-005
  - PRODUCT-ADR-LEARNING-012
- **supersedes**:
  - PRODUCT-ADR-PIPELINE-010
- **migrated_to_spec**: 2026-06-28

## Context

PRODUCT-ADR-PIPELINE-010 established independent semantic evaluation units, minimal context, positive evidence, deterministic coverage checks, complete-unit execution, and deterministic candidate aggregation.

That decision also fixed one initial attempt plus at most two additional invalid-output attempts.
The fixed attempt count is an implementation tuning parameter rather than product-level semantic authority.

The semantic evaluation contract remains valid, but retry authority must align with PRODUCT-ADR-PIPELINE-022: design determines retryability, finite termination, and exhaustion meaning; implementation configuration determines concrete attempt counts and timing.

This ADR supersedes PRODUCT-ADR-PIPELINE-010 in full so that current authority remains available from one complete decision.

## Decision

### First-MVP semantic boundary

The first MVP will evaluate each complete bounded candidate.
It will not semantically split one candidate into shorter candidates.
It will not salvage an accepted prefix from an otherwise rejected candidate.

Semantic segmentation may be introduced only through later accepted authority after representative fixtures exist.

Semantic filtering will consume accepted reusable summaries and source-verified phrase candidates.
Each candidate will be judged independently.
Relative inferiority to a sibling path, path length within the accepted bound, or lack of canonical preference will not be rejection reasons.
The Pipeline will not select one canonical path during filtering.

### Independent evaluation units

Semantic suitability will use separate evaluation units:

| evaluation unit | required input | owned judgment |
|---|---|---|
| Path coherence | Complete ordered reusable summaries for the candidate. | Whether the summaries remain understandable as one connected technical exchange. |
| Opening-post suitability | Opening summary and only the opening post's source-verified phrase candidates. | Whether the opening post supports one useful question-formulation interaction. |
| Reply-post suitability | Ordered summaries from the opening post through the target reply, plus only that reply's source-verified phrase candidates. | Whether the target reply supports one useful reply-formulation interaction. |

The Pipeline will create one reply-post suitability unit for every later candidate post.
Summaries after the target reply will not enter that reply's evaluation context.

Concrete prompt wording remains an implementation and fixture choice.
Each evaluator instruction must explain its owned judgment, controlled failure meaning, and independent absolute-judgment rule.

### Semantic suitability outcomes

A valid semantic failure will use one or more controlled reasons:

| reason | meaning |
|---|---|
| `incoherent_path` | The complete ordered summaries do not remain understandable as one connected technical exchange. |
| `unsuitable_opening_post` | The opening post cannot support one useful question-formulation interaction. |
| `unsuitable_reply_post` | An identified later post cannot support one useful reply-formulation interaction. |

Every failure will identify the relevant authentic-post identities.
The Pipeline will retain all applicable semantic failure reasons.

Technical detail, accepted path length, or relative sibling quality matters only when it causes one of the Learning-owned failures above.

### Positive evidence and deterministic coverage validation

Every semantic pass will retain positive evidence.

A path-coherence pass must cover every ordered adjacent post pair exactly once.
Each covered pair must include a non-empty explanation of the conversational movement.

An opening- or reply-suitability pass must identify:

- the evaluated authentic-post identity;
- the required `question` or `reply` interaction role;
- at least one exact source-verified phrase candidate supplied for that post.

Positive phrase evidence demonstrates minimum suitability.
It does not select the final learner-facing target phrase.

Evaluator output is invalid when deterministic checking finds any of these conditions:

- missing required evaluation coverage;
- duplicate coverage for a required unit or adjacent pair;
- a candidate-external post identity;
- an incorrect interaction role;
- phrase evidence not exactly present in supplied source-verified candidates;
- contradictory pass and failure claims;
- malformed or otherwise unusable output.

Invalid evaluator output is not semantic rejection.
It is an evaluation failure for that evaluation unit.

### Evaluation completion and retry

The Pipeline will execute every required semantic evaluation unit after structural validation succeeds.
It will not stop after the first valid semantic failure.
This preserves complete failure evidence for fixtures, diagnosis, and gate development.

Invalid evaluator output is retryable.
A valid pass or valid semantic failure is not retryable under unchanged input and behavior.

Every invalid-output retry sequence will terminate under a finite bound.
The concrete attempt count, timeout, delay, backoff, repair prompt, provider fallback, and provider switching belong to implementation configuration under PRODUCT-ADR-PIPELINE-022.

A unit that remains invalid when its configured finite retry bound is exhausted becomes an exhausted semantic evaluation failure.
Exhaustion remains distinct from semantic suitability rejection.

Retained evaluation-failure evidence will distinguish invalid, incomplete, contradictory, or uncovered evaluator output.

### Deterministic candidate aggregation

The final candidate outcome will follow this precedence:

1. Any structural failure produces structural rejection and prevents semantic processing.
2. Otherwise, one or more valid semantic failures produce semantic suitability rejection.
3. Exhausted evaluation failures accompanying a semantic rejection remain supplemental evidence.
4. Otherwise, one or more exhausted evaluation failures produce semantic evaluation failure.
5. Otherwise, complete passes for every required semantic unit retain one valid Learning Path.

One unit's pass, score, or rationale will not compensate for another unit's failure or missing valid result.

Final path-filtering outcomes are:

- structural rejection;
- semantic suitability rejection;
- semantic evaluation failure;
- retained valid Learning Path.

Enumerated and structurally valid candidates remain observable processing states rather than retained final outcomes.

### Retained evidence

Each non-retained candidate will preserve candidate-level evidence containing:

- candidate identity;
- final rejection or evaluation-failure stage;
- controlled reason or failure categories;
- relevant authentic-post identities;
- valid positive and negative evaluation evidence produced before aggregation;
- exhausted evaluation-unit failures when applicable.

Run-level counts may be derived from candidate-level outcomes.
Raw model requests and responses are not required.
Stage-specific provider, prompt, validation, orchestration, and retry-configuration provenance remain governed by current Pipeline provenance and orchestration authority.

Concrete model, prompt text, threshold, scoring scale, schema encoding, retry count, retry timing, provider fallback, and storage layout remain implementation choices.

## Rationale

Independent evaluation units narrow local-model responsibility and permit deterministic proof of complete path and post coverage.
Minimal context preserves the conversation required for one judgment while avoiding unrelated later content.
Positive evidence prevents acceptance through a bare model verdict.

Executing all required units preserves complete diagnosis.
Retrying invalid output can recover from unusable model responses without retrying valid content rejection.

Keeping retry counts in implementation configuration preserves the semantic distinction between retryability and tuning.
It also allows different providers and operations to use different finite policies without reopening product design.

Deterministic non-compensating aggregation preserves every Learning-owned dimension and separates unsuitable content from evaluator failure.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Keep the fixed three-attempt contract | The exact attempt count is an implementation parameter rather than product semantics. |
| Remove invalid-output retry entirely | Unusable evaluator output may be transient and does not establish content rejection. |
| Retry valid semantic failures | A valid failure is a content judgment, not invalid execution. |
| Use one combined semantic verdict | One model call can omit posts or conflate independent Learning dimensions. |
| Let one score compensate for another failure | Every required Learning dimension must pass independently. |
| Give every evaluator the complete candidate context | Unneeded later context can distract from one target reply. |
| Give a reply evaluator only the target post | It cannot judge reply function without preceding context. |
| Accept a bare `pass` | Coverage, role, target identity, and phrase grounding could not be verified. |
| Stop after the first semantic failure | Later failures and fixture evidence would remain hidden. |
| Treat exhausted invalid output as semantic rejection | Evaluator failure must remain distinct from unsuitable source content. |
| Select the best sibling path | Learning requires independent validity rather than ranking. |
| Add semantic segmentation in the first MVP | Representative segmentation fixtures do not yet exist. |

## Consequences

- PRODUCT-ADR-PIPELINE-010 becomes superseded history.
- Existing accepted ADRs may retain historical dependency references to PRODUCT-ADR-PIPELINE-010; current specification reflection will use PRODUCT-ADR-PIPELINE-023 and will not introduce dependency cycles by rewriting historical edges.
- Semantic filtering still begins only after deterministic structural success.
- Every candidate uses independent coherence, opening, and per-reply evaluations.
- Positive evidence and deterministic complete coverage remain required.
- Invalid evaluator output remains retryable under a finite implementation-configured bound.
- Valid pass and valid semantic rejection remain non-retryable.
- Exhaustion remains semantic evaluation failure.
- T07 must reference this ADR rather than PRODUCT-ADR-PIPELINE-010 when reflecting semantic filtering into focused specifications.
- Concrete models, prompts, schemas, thresholds, retry counts, retry timing, fallback behavior, and execution technology remain deferred.

## Evidence

- PRODUCT-ADR-PIPELINE-009 establishes deterministic candidate derivation and structural validation.
- PRODUCT-ADR-LEARNING-005 rejects canonical-path selection and requires independent path validity.
- PRODUCT-ADR-LEARNING-012 establishes non-compensating path coherence and per-post suitability.
- PRODUCT-ADR-PIPELINE-002 treats model output as untrusted.
- PRODUCT-ADR-PIPELINE-022 establishes finite retry semantics while assigning concrete counts and timing to implementation configuration.
- The user preserved the complete semantic evaluation contract and corrected the fixed three-attempt rule as an implementation-responsibility leak.
