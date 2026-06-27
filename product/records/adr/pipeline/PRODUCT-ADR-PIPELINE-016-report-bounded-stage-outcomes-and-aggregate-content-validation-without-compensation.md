# PRODUCT-ADR-PIPELINE-016: Report bounded stage outcomes and aggregate content validation without compensation

- **status**: accepted
- **date**: 2026-06-28
- **depends_on**:
  - PRODUCT-ADR-PIPELINE-002
  - PRODUCT-ADR-PIPELINE-008
  - PRODUCT-ADR-PIPELINE-011
  - PRODUCT-ADR-PIPELINE-012
  - PRODUCT-ADR-PIPELINE-013
  - PRODUCT-ADR-PIPELINE-014
  - PRODUCT-ADR-PIPELINE-015
  - PRODUCT-ADR-LEARNING-012
- **supersedes**:
- **migrated_to_spec**:

## Context

T04 generation and semantic-evaluation stages can fail for different reasons.
A provider failure, malformed output, semantic rejection, missing evaluation, and contradictory evaluation require distinct orchestration evidence.

One selected post with incomplete generated content prevents a complete Learning Unit for its valid path.
The Pipeline must not hide that failure by skipping the post or averaging successful dimensions.

The Pipeline also needs a completion boundary before the later publication gate.
A universal model verdict must not override accepted independent failures.

## Decision

### Common stage outcomes

Every generation and semantic-evaluation stage will report exactly one orchestration-facing outcome from this set:

| outcome | meaning |
|---|---|
| `accepted` | Required input, output, deterministic validation, and semantic evaluation are complete and valid. |
| `incomplete_input` | Required accepted input is absent or incomplete before model execution. |
| `provider_failure` | The configured provider could not complete the requested operation. |
| `invalid_provider_output` | Provider output is structurally unusable, identity-invalid, malformed, or otherwise untrusted before semantic acceptance. |
| `semantic_rejection` | Structurally valid generated content fails one or more accepted semantic criteria. |
| `incomplete_evaluation` | One or more required semantic evaluation results are missing or uncovered. |
| `contradictory_evaluation` | Required evaluation results contain internally incompatible valid claims. |

Invalid provider output will remain distinct from semantic rejection.
Incomplete and contradictory evaluation will remain distinct from both.

Retry count, provider switching, repair prompts, rerun scope, delay, and backoff remain orchestration decisions outside this ADR.

No non-accepted model output or evaluation result may become input to a downstream stage.

### Interaction completion

One interaction remains incomplete until all required artifacts and evaluations for its selected post are accepted.
Required artifacts include:

- accepted learner-visible summary;
- accepted target phrase;
- accepted Quiz prompt;
- exactly three accepted options;
- semantic option identities;
- one resolvable correct-option reference;
- complete accepted semantic evaluation coverage.

One incomplete interaction prevents materialization of the whole Learning Unit for that valid Learning Path.

The Pipeline will not:

- skip the failed selected post;
- shorten the valid Learning Path;
- mutate the valid Learning Path;
- publish a partial Learning Unit.

Accepted intermediate artifacts may remain reusable.
A later rerun may resume from the failed stage when all upstream accepted inputs remain current.

Failure will remain localized to the affected:

- valid Learning Path;
- selected post;
- stage;
- evaluation unit.

The failure will not invalidate:

- normalized source artifacts;
- accepted reusable summaries;
- accepted phrase evidence;
- other valid Learning Paths;
- Learning Units derived from other valid Learning Paths.

### Content-validation completion

Content-validation completion will use deterministic, non-compensating aggregation.
The Pipeline will not add one universal model verdict over the completed Learning Unit.

Completion requires all of these conditions:

- every selected valid-path post has exactly one complete interaction;
- interaction order matches source order;
- every required structural result is present and accepted;
- every required semantic result is present and accepted;
- identities and references agree;
- source routes remain available;
- generated content remains distinguishable from source-authored content;
- required stage provenance remains available;
- no semantic rejection remains;
- no incomplete result remains;
- no contradictory result remains.

A pass in one dimension will not compensate for a failure or missing result in another dimension.
Aggregate scoring will not override a failed required dimension.

Content-validation completion establishes readiness to enter the later publication gate.
It does not authorize publication.

### Large-model improvement boundary

A large external model may analyze retained failures and recommend improvements.
Examples, not exhaustive:

- identify recurring failure clusters;
- distinguish prompt, context, schema, criterion, and model-capability causes;
- recommend stage-boundary changes;
- recommend prompt or fixture improvements;
- propose new harder evaluation cases.

Large-model analysis will not replace production stage verdicts.
A large-model recommendation requires separate human acceptance and ADR, specification, prompt, criterion, or fixture updates as appropriate.

## Rationale

Distinct outcomes let orchestration choose appropriate follow-up without misclassifying unsuitable content as infrastructure failure.
Blocking downstream use of non-accepted output prevents invalid artifacts from contaminating later stages.

Whole-unit incompleteness preserves the one-interaction-per-selected-post Learning contract and stable path identity.
Localized failures preserve reusable source and intermediate work.

Deterministic non-compensating aggregation enforces every required Learning readiness dimension.
Using large models for diagnosis and improvement applies their broader reasoning where it adds value without weakening production gates.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Return one generic `failed` outcome | Orchestration could not distinguish provider, structure, semantic, coverage, and contradiction failures. |
| Send malformed output to semantic evaluation | Untrusted structure and identity would contaminate content judgment. |
| Skip a failed interaction and publish the remaining posts | The result would no longer represent the accepted valid Learning Path. |
| Discard all accepted intermediates after one failure | Reruns would repeat validated work and increase cost. |
| Let successful dimensions compensate for one failed dimension | Learning readiness dimensions are non-compensating. |
| Ask one universal model to approve the complete unit | One fluent verdict could override explicit independent failures or missing coverage. |
| Let a large model directly change production criteria | Criteria changes require human-approved design authority and fixture validation. |

## Consequences

- Every T04 stage exposes one controlled orchestration-facing outcome.
- T06 may define concrete retry, fallback, rerun, reuse, and batch behavior without changing outcome meaning.
- One incomplete interaction blocks Learning Unit materialization for its path.
- Accepted shared and path-local intermediate artifacts may be reused when still current.
- Content-validation completion remains separate from T05 publication authorization.
- Large-model review becomes an improvement workflow rather than a production-line override.
- Stage-specific provider, prompt, and validation provenance remains governed by PRODUCT-ADR-PIPELINE-008.
- Concrete status encoding, persistence, retry algorithms, and diagnostic presentation remain deferred.

## Evidence

- PRODUCT-ADR-LEARNING-012 establishes non-compensating structural and semantic readiness dimensions.
- PRODUCT-ADR-PIPELINE-008 establishes retained stage-specific provider, prompt, and validation provenance.
- PRODUCT-ADR-PIPELINE-011 through PRODUCT-ADR-PIPELINE-015 establish bounded generation and independent evaluation stages.
- PRODUCT-ADR-PIPELINE-010 provides precedent for separating semantic rejection from evaluator failure.
- The user selected controlled common outcomes, whole-unit incompleteness, localized retained intermediates, deterministic aggregation, and large-model use for failure analysis and improvement proposals.
