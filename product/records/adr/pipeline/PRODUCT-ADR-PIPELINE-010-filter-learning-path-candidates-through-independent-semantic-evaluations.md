# PRODUCT-ADR-PIPELINE-010: Filter Learning Path candidates through independent semantic evaluations

- **status**: superseded
- **date**: 2026-06-28
- **depends_on**:
  - PRODUCT-ADR-PIPELINE-002
  - PRODUCT-ADR-PIPELINE-008
  - PRODUCT-ADR-PIPELINE-009
  - PRODUCT-ADR-LEARNING-005
  - PRODUCT-ADR-LEARNING-012
- **supersedes**:
- **migrated_to_spec**:

## Context

PRODUCT-ADR-PIPELINE-009 establishes deterministic candidate derivation and structural validation.
Only structurally valid candidates may enter semantic suitability filtering.

The Learning contract requires:

- one connected technical exchange;
- one useful question-formulation interaction from the opening post;
- one useful reply-formulation interaction from every later post;
- independent judgment without sibling ranking or canonical-path selection.

PRODUCT-INV-PIPELINE-002 found that local models could perform reviewed absolute filtering over reusable summaries and source-verified phrase evidence.
The same investigation does not establish that one combined local-model verdict is reliable enough for every required dimension.

The Pipeline needs independent evaluation units, deterministic coverage checks, bounded invalid-output retry, and explicit terminal outcomes.

## Decision

### First-MVP semantic boundary

The first MVP will evaluate each complete bounded candidate.
It will not semantically split one candidate into shorter candidates.
It will not salvage an accepted prefix from an otherwise rejected candidate.

Semantic segmentation may be introduced by a later Pipeline decision after representative fixtures exist.

Semantic filtering will consume grounded reusable summaries and source-verified phrase candidates.
The generation and validation contract for those inputs remains owned by later Pipeline design.

Each candidate will be judged independently.
A shorter, richer, higher-ranked, or otherwise preferred sibling will not be a rejection reason.
The Pipeline will not select one canonical path during filtering.

### Independent evaluation units

Semantic suitability will use separate evaluation units:

| evaluation unit | required input | owned judgment |
|---|---|---|
| Path coherence | Complete ordered reusable summaries for the candidate. | Whether the ordered summaries remain understandable as one connected technical exchange. |
| Opening-post suitability | Opening summary and only the opening post's source-verified phrase candidates. | Whether the opening post supports one useful question-formulation interaction. |
| Reply-post suitability | Ordered summaries from the opening post through the target reply, plus only that reply's source-verified phrase candidates. | Whether the target reply supports one useful reply-formulation interaction. |

The Pipeline will create one reply-post suitability unit for every later candidate post.
Summaries after the target reply will not enter that reply's evaluation context.

Concrete prompt wording remains an implementation and evaluation-fixture choice.
Every evaluator instruction must explain its owned judgment, controlled failure meaning, and independent absolute-judgment rule.

### Semantic suitability outcomes

A valid semantic failure will use one or more controlled reasons:

| reason | meaning |
|---|---|
| `incoherent_path` | The complete ordered summaries do not remain understandable as one connected technical exchange. |
| `unsuitable_opening_post` | The opening post cannot support one useful question-formulation interaction. |
| `unsuitable_reply_post` | An identified later post cannot support one useful reply-formulation interaction. |

Every failure will identify the relevant authentic-post identities.
The Pipeline will retain all applicable semantic failure reasons.

Technical detail, path length within the accepted bound, or relative inferiority will not independently establish semantic failure.
Those characteristics matter only when they cause one of the Learning-owned failures above.

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

The Pipeline will deterministically reject evaluator output as invalid when it contains any of these conditions:

- missing required evaluation coverage;
- duplicate coverage for one required unit or adjacent pair;
- a candidate-external post identity;
- an incorrect interaction role;
- phrase evidence not exactly present in the supplied source-verified candidates;
- contradictory pass and failure claims;
- malformed or otherwise unusable output.

An invalid evaluator output is not a semantic suitability rejection.
It is an evaluation failure for that evaluation unit.

### Evaluation completion and retry

The Pipeline will execute every required semantic evaluation unit after structural validation succeeds.
It will not stop after the first valid semantic failure.
This preserves complete failure evidence for fixture and gate development.

Each independent evaluation unit may receive:

- one initial attempt;
- at most two additional attempts after invalid evaluator output.

A valid pass or valid semantic failure will not be retried.
A unit that remains invalid after three total attempts will become an exhausted semantic evaluation failure.

The retained evaluation-failure evidence will distinguish invalid, incomplete, contradictory, or uncovered evaluator output.
Concrete repair prompts, same-model reuse, fallback-model selection, delay, backoff, and infrastructure retry remain orchestration concerns.

### Deterministic candidate aggregation

The final candidate outcome will follow this precedence:

1. Any structural failure produces structural rejection and prevents semantic processing.
2. Otherwise, one or more valid semantic failures produce semantic suitability rejection.
3. Exhausted evaluation failures accompanying a semantic rejection remain supplemental evidence.
4. Otherwise, one or more exhausted evaluation failures produce semantic evaluation failure.
5. Otherwise, complete passes for every required semantic unit retain one valid Learning Path.

One unit's pass, score, or rationale will not compensate for another unit's failure or missing valid result.

Final path-filtering outcomes are therefore:

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
Raw model requests and responses are not required by this decision.
Stage-specific provider and prompt provenance remains governed by PRODUCT-ADR-PIPELINE-008 and later generation and orchestration contracts.

Concrete model, prompt text, threshold, scoring scale, schema encoding, and storage layout remain implementation choices.

## Rationale

Independent evaluation units narrow each local-model task.
They also allow deterministic validation to prove complete path and post coverage.

Minimal context reduces unrelated information while preserving the conversation needed to judge one target reply.
Excluding later posts prevents future context from changing the target reply's role.

Positive evidence makes a bare model pass insufficient.
Exact supplied phrase matching prevents the evaluator from inventing phrase evidence.

Executing all required units preserves complete diagnosis across one candidate.
Bounded retries recover malformed model output without retrying a valid content rejection.

Deterministic aggregation keeps Learning-owned required dimensions non-compensating.
It also separates unsuitable content from a Pipeline evaluator that could not complete its judgment.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Use one combined semantic verdict for the complete candidate | One local-model call can omit posts or conflate independent Learning dimensions. |
| Let one aggregate score compensate for a failed unit | Every required Learning dimension must pass independently. |
| Give every evaluator the complete candidate context | Unneeded later context increases distraction and can distort one reply's role. |
| Give a reply evaluator only the target post | The evaluator cannot judge whether the post functions as a reply in context. |
| Accept a bare `pass` without evidence | Coverage, target identity, role, and supplied phrase grounding cannot be verified. |
| Stop semantic evaluation after the first failure | Later failures would remain hidden and fixture evidence would be incomplete. |
| Retry valid semantic failures | A valid rejection is a content judgment rather than invalid provider output. |
| Treat exhausted invalid output as semantic rejection | Evaluator failure must remain distinct from unsuitable source content. |
| Select the best sibling path | Learning requires independent validity rather than ranking or canonical selection. |
| Add semantic segmentation in the first MVP | Representative boundary fixtures do not yet exist, and complete-candidate rejection is sufficient for initial delivery. |

## Consequences

- Semantic filtering begins only after PRODUCT-ADR-PIPELINE-009 structural success.
- T04 must define reusable-summary and source-verified phrase generation without changing these evaluation roles.
- T04 may define exact evaluator input and output artifacts while preserving the required evidence and coverage meaning.
- T06 must define retry execution, provider failures, fallback, batching, and rerun behavior around the accepted three-attempt bound.
- T07 must reflect semantic units, controlled reasons, evidence, aggregation, and terminal outcomes into focused Pipeline specifications.
- Later semantic segmentation requires new authority and representative real-discussion fixtures.
- Concrete models, prompts, schemas, thresholds, retry timing, and infrastructure remain deferred.

## Evidence

- PRODUCT-ADR-LEARNING-005 establishes independently valid paths and rejects canonical-path selection.
- PRODUCT-ADR-LEARNING-012 establishes non-compensating path coherence and per-post quiz suitability.
- PRODUCT-ADR-PIPELINE-002 treats model output as untrusted behind a provider boundary.
- PRODUCT-ADR-PIPELINE-008 requires stage-specific provider, prompt, and validation provenance.
- PRODUCT-INV-PIPELINE-002 provides reviewed absolute-filtering fixtures using reusable summaries and source-verified phrase candidates.
- The user selected complete-candidate first-MVP filtering, independent coherence and per-post evaluations, full-unit execution, positive evidence, two invalid-output retries, and deterministic four-outcome aggregation.
