# PRODUCT-ADR-PIPELINE-017: Approve unattended publication through complete non-compensating gate evidence

- **status**: accepted
- **date**: 2026-06-28
- **depends_on**:
  - PRODUCT-ADR-PIPELINE-005
  - PRODUCT-ADR-PIPELINE-008
  - PRODUCT-ADR-PIPELINE-010
  - PRODUCT-ADR-PIPELINE-016
  - PRODUCT-ADR-LEARNING-012
- **supersedes**:
- **migrated_to_spec**:

## Context

PRODUCT-ADR-LEARNING-012 defines structural readiness and eight non-compensating semantic readiness dimensions.
It also requires human approval of criteria, representative fixtures, harder fixtures, and material criteria changes.

PRODUCT-ADR-PIPELINE-016 defines content-validation completion as readiness to enter the publication gate.
Content-validation completion does not authorize publication.

The Pipeline still needs one gate contract that proves complete readiness coverage before unattended publication.
The contract must reject incomplete or contradictory current evidence without introducing one universal model verdict.

The Pipeline also needs a controlled approval boundary for gate configurations.
An easy validation set alone does not establish unattended publication reliability.

## Decision

### Structural readiness input

The publication gate will consume accepted upstream results rather than rerun generation or semantic evaluation.

The structural readiness input set will contain:

- stable Learning Unit identity;
- one complete Learning Unit candidate;
- accepted structural validation results;
- complete source bindings for every interaction;
- complete unit-level attribution;
- generated-source separation results;
- complete and unique required evaluation coverage;
- one current provenance bundle matching the candidate;
- content-validation completion under PRODUCT-ADR-PIPELINE-016.

The gate will not trust a content-validation completion marker in isolation.
It will deterministically confirm complete interaction coverage, complete evaluation coverage, and identity agreement across the candidate, evaluation targets, current provenance, and publication target.

A missing result, duplicate result, unresolved identity, mismatched identity, partial unit, or incomplete coverage will fail structural readiness.

### Semantic readiness input

The gate configuration will map accepted upstream evaluation results to every Learning-owned semantic readiness dimension.

| dimension | required gate meaning |
|---|---|
| Path coherence | Complete accepted evidence shows one connected ordered technical exchange. |
| Per-post quiz suitability | Complete accepted evidence shows one useful interaction for every selected post. |
| Source grounding | Complete accepted evidence grounds summaries, conversational moves, target phrases, prompts, and options. |
| Summary fidelity | Complete accepted evidence preserves position, certainty, response meaning, attribution, and supported claims. |
| Phrase usefulness | Complete accepted evidence shows natural reusable conversational English. |
| Option naturalness | Complete accepted evidence shows grammatical, natural, useful options without unsupported claims. |
| Contextual fit | Complete accepted evidence shows exactly one best option for the prompt and target phrase. |
| Generated-source separation | Complete accepted evidence keeps generated content distinct from authentic source-authored wording. |

Every required dimension must have complete accepted coverage for the complete current Learning Unit candidate.
A failed, incomplete, missing, uncovered, duplicate, or contradictory required result will block publication.

A pass in one dimension will not compensate for another dimension's failure or missing result.
Aggregate scores, majority voting, and a universal model verdict will not override any required result.

The gate will judge only the current result set supplied through current provenance.
Generated-artifact revision identity and historical evaluation comparison are not required.

### Contradictory validation state

Contradictory validation means the current publication-gate input set is internally inconsistent.

Examples, not exhaustive:

- content-validation completion claims success while one required current result is non-accepted;
- one current result contains a success verdict and a controlled failure condition that cannot both be true;
- required coverage claims completion while supplied current evidence proves missing or conflicting coverage.

A contradiction indicates a defective aggregation state, invalid gate input, or Pipeline defect.
The publication gate will not repair the state, infer which claim is authoritative, or ask a universal model to choose.
It will fail closed and produce a rejected publication decision with a contradictory-validation cause.

### Human approval boundary

Human approval will apply to publication policy and gate evidence rather than routine per-unit publication.

Humans will approve:

- publication-gate criteria and intended meaning;
- representative golden fixtures;
- representative harder fixtures;
- material changes to criteria or intended meaning.

Routine Learning Units may be evaluated and published automatically after the active gate configuration is approved for unattended publication.
The first MVP will not require individual human approval for every Learning Unit.

A borderline case will escalate only when accepted criteria do not determine the policy judgment.
Escalation will seek a policy decision rather than an exceptional one-unit override.
The resulting decision may require a criteria change, fixture change, or new accepted authority.

### Unattended publication eligibility

A gate configuration may be used for unattended publication only after validation against human-approved criteria, golden fixtures, and harder fixtures.

Validation will confirm that the configuration:

- covers every required structural readiness condition;
- covers every required semantic readiness dimension;
- produces the expected decision for every approved golden fixture;
- produces the expected decision for every approved harder fixture;
- produces no missing, incomplete, uncovered, or contradictory required result during fixture validation;
- retains validation evidence for the exact configuration used by unattended publication.

Passing only the golden fixtures is insufficient.
Harder-fixture validation is mandatory before unattended publication eligibility.

A configuration change that can affect gate behavior requires fixture revalidation before unattended use.

Examples, not exhaustive:

- evaluator model changes;
- evaluator prompt changes;
- deterministic validator changes;
- dimension-to-result mapping changes;
- threshold or decision-setting changes.

A material criteria-meaning change additionally requires human approval.
Concrete model names, prompt text, threshold values, and execution mechanisms remain outside this decision.

## Rationale

Complete structural and semantic coverage prevents a partial or invalid result set from authorizing publication.

Non-compensating aggregation preserves every Learning-owned readiness dimension.
A universal model verdict could conceal missing coverage or override an explicit failure.

Fail-closed contradiction handling prevents a defective Pipeline aggregation state from exposing content.

Policy-level human approval preserves scalability without delegating acceptance meaning entirely to model output.
Golden fixtures verify ordinary behavior.
Harder fixtures verify known boundary and failure cases before unattended use.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Treat content-validation completion alone as publication authority | The marker could be incomplete or inconsistent with its underlying evidence. |
| Run one final model verdict over the complete unit | One verdict could override failed dimensions or conceal incomplete coverage. |
| Use one aggregate score | Strong dimensions could compensate for a grounding, fidelity, or contextual-fit failure. |
| Accept contradictory evidence by precedence | Selecting one claim would hide a Pipeline defect and risk incorrect publication. |
| Approve unattended publication after golden fixtures only | Easy fixtures do not exercise representative boundary failures. |
| Require human approval for every unit | Routine item-level review does not scale. |
| Allow one-unit policy exceptions | Exceptional overrides would weaken consistent unattended gate meaning. |

## Consequences

- T05 publication decisions require complete current structural and semantic evidence.
- A contradictory current result set produces rejection and no published-content mutation.
- Gate configurations require approved golden and harder fixture evidence before unattended use.
- Behavior-affecting configuration changes require fixture revalidation.
- Material criteria changes require human approval and accepted authority.
- Borderline cases become policy inputs rather than routine manual publication work.
- T06 owns formation, replacement, reuse, reevaluation, retry, and rerun of current results.
- T07 must reflect this decision into focused Pipeline publication and validation specifications.
- Concrete schemas, thresholds, models, prompts, and execution technology remain deferred.

## Evidence

- PRODUCT-ADR-LEARNING-012 establishes structural readiness, eight non-compensating semantic dimensions, harder fixtures, and policy-level human approval.
- PRODUCT-ADR-PIPELINE-010 establishes independent semantic evaluations and deterministic complete coverage for path suitability.
- PRODUCT-ADR-PIPELINE-016 establishes non-compensating content-validation completion without universal model override.
- PRODUCT-ADR-PIPELINE-008 establishes the current Pipeline provenance bundle.
- The user approved complete gate inputs, fail-closed contradiction handling, policy-level human approval, and golden-plus-harder fixture validation.
