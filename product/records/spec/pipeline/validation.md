# Concept: Pipeline validation

- **id**: `spec:product.pipeline.validation`
- **status**: draft
- **date**: 2026-06-28
- **parent**: `spec:product.pipeline`

## What this is

Pipeline contract for deterministic validation, semantic evaluation, controlled stage outcomes, interaction completion, and non-compensating content-validation completion.
The contract establishes readiness to enter the publication gate without authorizing publication.

## Non-goals

- Learning-owned readiness meaning.
- Publication-gate approval or published-content mutation.
- Concrete schemas, validation libraries, thresholds, or scoring scales.
- Retry counts, delays, backoff, provider fallback, or scheduling.
- Permanent raw model transcript retention.

## Concept model

| concept | contract |
|---|---|
| Deterministic validation | Mechanical validation of structure, identity, evidence membership, references, cardinality, and coverage. |
| Semantic evaluation | One bounded judgment over one explicitly owned semantic dimension. |
| Stage outcome | One controlled orchestration-facing result for a generation or evaluation operation. |
| Interaction completion | Complete accepted artifact and evaluation set for one selected post. |
| Content-validation completion | Deterministic proof that one complete Learning Unit candidate satisfies every required upstream result. |

## Rules

### Validation order

- Deterministic validation must precede semantic acceptance whenever structure or evidence can be checked mechanically.
- Malformed, identity-invalid, structurally unusable, or untrusted output must not enter semantic evaluation.
- Semantic evaluation must remain limited to judgments that require semantic interpretation.
- Every required semantic dimension must have an independent evaluation result unless an owning spec explicitly defines a combined unit.
- Deterministic aggregation must verify complete and unique required coverage.

### Controlled stage outcomes

Every generation and semantic-evaluation stage must report exactly one outcome.

| outcome | meaning |
|---|---|
| `accepted` | Required input, output, deterministic validation, and semantic evaluation are complete and valid. |
| `incomplete_input` | Required accepted input is absent or incomplete before execution. |
| `provider_failure` | The configured provider could not complete the requested operation. |
| `invalid_provider_output` | Provider output is malformed, structurally unusable, identity-invalid, or otherwise untrusted. |
| `semantic_rejection` | Structurally valid generated content fails one or more accepted semantic criteria. |
| `incomplete_evaluation` | One or more required semantic results are missing or uncovered. |
| `contradictory_evaluation` | Required valid results contain internally incompatible claims. |

- Invalid provider output must remain distinct from semantic rejection.
- Provider failure must remain distinct from invalid provider output.
- Incomplete and contradictory evaluation must remain distinct from rejection and provider failure.
- A valid semantic rejection must not be retried under unchanged input and behavior.
- No non-accepted output may become downstream input.

### Semantic evaluation evidence

Every semantic evaluation result must identify:

- its target scope and identity;
- its owned semantic dimension;
- its pass or controlled failure meaning;
- non-empty reasoning;
- required positive or negative grounding evidence.

Deterministic validation must confirm, where applicable:

- target identity agreement;
- exact evidence membership in supplied source evidence;
- quote exclusion;
- required role agreement;
- complete and unique coverage;
- no candidate-external or unit-external identity;
- no contradictory pass and failure claim.

- A bare model success assertion must not establish acceptance.
- A model-produced score must not override a failed required dimension.
- One evaluator or universal model verdict must not override independent required failures.

### Interaction completion

One interaction is complete only when all required current artifacts and evaluations are accepted.

Required completion includes:

- one accepted learner-visible summary;
- one accepted target phrase;
- one accepted Quiz prompt;
- exactly three accepted options;
- three semantic option identities;
- one resolvable correct-option reference;
- complete accepted deterministic and semantic evaluation coverage;
- matching path, post, and interaction identities;
- retained source route and generated-source separation.

- An incomplete interaction makes the complete Learning Unit for its valid path incomplete.
- The Pipeline must not skip the failed post.
- The Pipeline must not shorten or mutate the accepted valid path.
- The Pipeline must not publish a partial Learning Unit.
- Failure must remain localized to the affected path, post, stage, and evaluation unit.
- Localized failure must not invalidate accepted shared artifacts or independent sibling paths.

### Content-validation completion

Content-validation completion must use deterministic non-compensating aggregation.

Completion requires:

- exactly one complete interaction for every selected valid-path post;
- source-order interaction agreement;
- every required structural result present and accepted;
- every required semantic result present and accepted;
- identity and reference agreement across all artifacts;
- retained source routes for every interaction;
- generated content distinguishable from source-authored content;
- required stage provenance available;
- no semantic rejection;
- no incomplete result;
- no contradictory result.

- A pass in one dimension must not compensate for failure or missing evidence in another.
- Aggregate scoring and majority voting must not override a required failure.
- The Pipeline must not add one universal model verdict over the complete unit.
- Content-validation completion permits entry into `spec:product.pipeline.publication` only.
- Content-validation completion does not authorize publication.

### Failure retention and improvement analysis

- Accepted intermediate artifacts may remain reusable when their inputs and behavior references remain current.
- Current outcome evidence must identify controlled rejection, incompleteness, contradiction, or invalid output.
- Raw prompts, complete provider responses, every transient attempt, and permanent historical replay are not required.
- A larger external model may analyze retained failures and recommend improvements.
- Improvement analysis must not replace production verdicts.
- Recommendations affecting criteria, stages, prompts, fixtures, or authority require separate human acceptance and applicable design updates.

## Boundary

| concern | owner |
|---|---|
| Learning readiness dimensions | `spec:product.learning.learning_unit`. |
| Stage-specific generation and evaluation units | `spec:product.pipeline.content_generation` and `spec:product.pipeline.path_validation`. |
| Common validation order, outcomes, and completion | `spec:product.pipeline.validation`. |
| Retry, exhaustion, diagnostics, and rerun | `spec:product.pipeline.orchestration`. |
| Publication-gate authorization | `spec:product.pipeline.publication`. |
| Provider invocation and error translation | `spec:product.pipeline.llm_provider`. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.pipeline` | Parent Pipeline overview. |
| `spec:product.pipeline.path_validation` | Defines path-specific validation units and outcomes. |
| `spec:product.pipeline.content_generation` | Defines generation-stage inputs, outputs, and semantic checks. |
| `spec:product.pipeline.publication` | Consumes complete current validation evidence. |
| `spec:product.pipeline.orchestration` | Owns retry, exhaustion, terminal progression, and diagnostics. |
| `spec:product.learning.learning_unit` | Defines non-compensating structural and semantic readiness. |
| PRODUCT-ADR-PIPELINE-016 | Establishes controlled outcomes, whole-unit blocking, and content-validation completion. |
| PRODUCT-ADR-PIPELINE-017 | Establishes publication-gate evidence beyond content-validation completion. |
| PRODUCT-ADR-PIPELINE-022 | Establishes retry classification and current-run diagnostics. |
