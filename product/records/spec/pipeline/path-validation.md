# Concept: Learning Path candidate validation

- **id**: `spec:product.pipeline.path_validation`
- **status**: draft
- **date**: 2026-06-28
- **parent**: `spec:product.pipeline`

## What this is

Pipeline contract for deterministic candidate structure checks and independent semantic suitability filtering.
The contract produces retained valid Learning Paths or controlled rejection and evaluation-failure outcomes.

## Non-goals

- Learning-owned suitability meaning.
- Sibling ranking or canonical-path selection.
- First-MVP semantic segmentation.
- Concrete model, prompt, threshold, schema, or retry count.
- Publication-gate authorization.

## Concept model

| concept | contract |
|---|---|
| Structural validation | Deterministic proof that one candidate preserves accepted source scope, order, identity, and adjacency. |
| Path-coherence evaluation | Independent judgment of the complete ordered candidate exchange. |
| Opening-post suitability | Independent judgment that the opening post supports one question interaction. |
| Reply-post suitability | One independent judgment per later post that it supports one reply interaction. |
| Semantic evaluation failure | Exhausted invalid, incomplete, contradictory, or uncovered evaluator output. |
| Retained valid Learning Path | Candidate with structural success and complete semantic passes. |

## Rules

### Structural validation

Every candidate must complete deterministic structural validation before semantic filtering.

Validation must establish:

- all posts belong to one authentic discussion;
- the first post is the authentic opening post;
- cardinality is two through six posts;
- source order is preserved;
- each post identity resolves to retained source evidence;
- no post identity repeats;
- every adjacent pair has retained relationship evidence;
- every adjacent pair satisfies `spec:product.learning.learning_path` adjacency.

- The Pipeline must not repair repeated posts by deletion.
- A structural failure must prevent all semantic filtering for that candidate.
- Every adjacent pair must retain endpoint identities, relationship kind, and explicit target identity when present.
- A genuine topic-level response may project to the opening post.
- An unavailable explicit target must not use opening-post fallback.

### Structural rejection reasons

| reason | meaning |
|---|---|
| `invalid_discussion_scope` | Candidate posts do not belong to one authentic discussion. |
| `invalid_opening_post_start` | Candidate does not begin with the authentic opening post. |
| `invalid_cardinality` | Candidate does not contain two through six posts. |
| `invalid_source_order` | Candidate order does not preserve source order. |
| `invalid_adjacency` | An adjacent pair lacks accepted source-grounded adjacency. |
| `unavailable_explicit_reply_target` | An explicit reply target cannot resolve and cannot use fallback. |
| `unresolved_post_identity` | A post identity does not resolve to retained source evidence. |
| `missing_relationship_evidence` | Required source relationship evidence is absent. |
| `repeated_post` | One authentic-post identity appears more than once. |

- Structural rejection must retain all detected structural reasons.
- Structural rejection must retain candidate identity and relevant authentic-post identities.

### Semantic boundary

- Semantic filtering must consume only structurally valid candidates.
- Semantic filtering must consume accepted reusable summaries and accepted source-grounded phrase evidence.
- Each complete bounded candidate must be judged independently.
- Relative sibling quality, path length within the accepted bound, and lack of canonical preference are not rejection reasons.
- The first MVP must not salvage an accepted prefix from a rejected candidate.

### Independent evaluation units

| unit | required context | owned judgment |
|---|---|---|
| Path coherence | Complete ordered reusable summaries. | Whether the summaries form one understandable connected technical exchange. |
| Opening-post suitability | Opening summary and only opening-post accepted phrase evidence. | Whether the post supports one useful question-formulation interaction. |
| Reply-post suitability | Summaries through the target reply and only that reply's accepted phrase evidence. | Whether the post supports one useful reply-formulation interaction. |

- The Pipeline must execute one reply-post suitability unit for every later candidate post.
- Summaries after the target reply must not enter that reply's evaluation context.
- Every evaluator instruction must explain its owned judgment and absolute-judgment rule.
- Every required semantic unit must execute after structural success, even after another valid semantic failure.

### Positive evidence and coverage

- A path-coherence pass must cover each adjacent pair exactly once.
- Each covered pair must include a non-empty explanation of conversational movement.
- An opening- or reply-suitability pass must identify the target post, required interaction role, and accepted exact phrase evidence.
- Positive phrase evidence proves minimum suitability but does not select the final target phrase.
- Deterministic validation must confirm complete and unique unit coverage.
- Deterministic validation must confirm target identities, interaction roles, and supplied phrase evidence.

Evaluator output is invalid when it has:

- missing or duplicate required coverage;
- a candidate-external identity;
- an incorrect interaction role;
- phrase evidence outside supplied accepted evidence;
- contradictory pass and failure claims;
- malformed or unusable structure.

- Invalid evaluator output is not semantic rejection.
- Invalid evaluator output is retryable under `spec:product.pipeline.orchestration`.
- Valid semantic pass and valid semantic failure are not retryable under unchanged input and behavior.
- Exhaustion must remain a semantic evaluation failure rather than a suitability rejection.

### Semantic rejection reasons

| reason | meaning |
|---|---|
| `incoherent_path` | The complete summaries do not form one connected exchange. |
| `unsuitable_opening_post` | The opening post cannot support one useful question interaction. |
| `unsuitable_reply_post` | An identified reply cannot support one useful reply interaction. |

- Semantic failure evidence must identify relevant authentic-post identities.
- The Pipeline must retain all applicable valid semantic failure reasons.

### Candidate aggregation

Final candidate outcome uses this precedence:

1. Any structural failure produces structural rejection.
2. Otherwise, valid semantic failures produce semantic suitability rejection.
3. Exhausted evaluation failures accompanying semantic rejection remain supplemental evidence.
4. Otherwise, exhausted evaluation failures produce semantic evaluation failure.
5. Otherwise, complete passes retain one valid Learning Path.

- One pass, score, or rationale must not compensate for another failure or missing result.
- Non-retained candidates must preserve controlled reasons, relevant identities, available positive and negative evidence, and exhausted unit failures.
- Raw model requests and responses are not required.

## Boundary

| concern | owner |
|---|---|
| Candidate production | `spec:product.pipeline.path_enumeration`. |
| Structural checks and semantic path filtering | `spec:product.pipeline.path_validation`. |
| Common evaluator and stage-result semantics | `spec:product.pipeline.validation`. |
| Retry and exhaustion execution | `spec:product.pipeline.orchestration`. |
| Learning suitability meaning | `spec:product.learning.learning_path`. |
| Publication readiness and gate | `spec:product.learning.learning_unit` and `spec:product.pipeline.publication`. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.pipeline` | Parent Pipeline overview. |
| `spec:product.pipeline.path_enumeration` | Supplies bounded candidates. |
| `spec:product.pipeline.content_generation` | Supplies reusable summaries and phrase evidence and consumes retained valid paths. |
| `spec:product.pipeline.validation` | Defines common validation outcomes and coverage rules. |
| `spec:product.pipeline.orchestration` | Owns retry, exhaustion, and dependent-stage progression. |
| `spec:product.learning.learning_path` | Defines accepted suitability meaning. |
| PRODUCT-ADR-PIPELINE-009 | Establishes structural validation and rejection evidence. |
| PRODUCT-ADR-PIPELINE-023 | Establishes current independent semantic filtering and implementation-configured retry. |
