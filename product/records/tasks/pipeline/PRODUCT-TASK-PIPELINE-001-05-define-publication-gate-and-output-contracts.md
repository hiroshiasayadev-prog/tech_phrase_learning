# PRODUCT-TASK-PIPELINE-001-05: Define publication gate and output contracts

- **id**: PRODUCT-TASK-PIPELINE-001-05
- **status**: done
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PIPELINE-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 2.5d
- **depends_on**:
  - PRODUCT-TASK-PIPELINE-001-04
- **outputs**:
  - PRODUCT-ADR-PIPELINE-017
  - PRODUCT-ADR-PIPELINE-018
  - PRODUCT-ADR-PIPELINE-019

## Goal

Define publication-gate approval, eligibility, rejection, withdrawal, provenance, and published-content output contracts.

## Work

1. Read the fixed Learning publication-readiness contract and Application published-content boundary.
2. Define structural readiness inputs and complete-scope coverage obligations.
3. Define semantic readiness inputs for every non-compensating Learning quality dimension.
4. Require failure of any required dimension to block publication.
5. Define internally contradictory validation results as rejection outcomes.
6. Define human approval of criteria, representative golden fixtures, harder fixtures, and material criteria changes.
7. Define gate-configuration validation before unattended publication eligibility.
8. Define borderline-policy escalation without creating a routine per-unit human queue.
9. Define publication decisions for available, rejected, unavailable, and withdrawn outcomes.
10. Define current publication-decision provenance and its opaque external reference.
11. Define `PublicationHandoff` inputs, preconditions, outputs, and failure behavior.
12. Define `AvailabilityChange` inputs, preconditions, outputs, and failure behavior.
13. Require complete committed current-state production and atomic replacement.
14. Require availability-only mutation to preserve content and provenance.
15. Require the complete unit payload to remain immutable for Application readers.
16. Preserve Pipeline writer and Application reader ownership separation.
17. Create or update Pipeline ADRs when current authority does not determine observable gate or publication semantics.
18. Keep transaction syntax, database design, thresholds, routes, and serialization outside the contract.
19. Update `outputs` and Evidence with accepted ADRs or specification inputs.

## Done condition

- Structural and semantic gate inputs are explicit and cover the complete unit.
- Every required quality dimension is non-compensating.
- Contradictory results reject publication.
- Human criteria, fixture, configuration, and material-change approval boundaries are explicit.
- Unattended publication eligibility has explicit evidence conditions.
- Rejection, unavailability, withdrawal, and restoration outcomes are explicit.
- Publication-decision provenance is Pipeline-owned and externally opaque.
- `PublicationHandoff` and `AvailabilityChange` have complete semantic contracts.
- Initial publication and replacement produce one committed complete current state.
- Availability-only changes preserve current content and provenance.
- Failed preconditions and failed writes cannot expose partial state.
- Every new normative decision has accepted Pipeline ADR authority.
- Application read semantics remain unchanged.

## Verification

- Trace gate dimensions to `spec:product.learning.learning_unit` without restating their meaning.
- Confirm model success alone cannot pass the gate.
- Confirm representative harder fixtures are required before unattended publication approval.
- Confirm replacement does not create a sibling learning unit or another current projection.
- Confirm unavailability preserves content, source references, attribution, and current provenance.
- Confirm `LearningUnitRef` and Application results expose no Pipeline provenance.
- Run relevant record validation, strict specification validation, `git diff --check`, and `git status --short`.

## Evidence

### Non-normative decision register

The following entries record user-approved T05 design direction before ADR materialization.
They are not normative authority.

#### D01 Publication-gate structural readiness inputs

The publication gate will consume accepted upstream results rather than rerun generation or semantic evaluation.

The structural readiness input set will include:

- stable Learning Unit identity;
- one complete Learning Unit candidate;
- accepted structural validation results;
- complete source bindings for every interaction;
- complete unit-level attribution;
- generated-source separation results;
- complete and unique required evaluation coverage;
- one current provenance bundle matching the candidate;
- T04 content-validation completion.

The gate will not trust a content-validation completion marker in isolation.
It will deterministically confirm identity agreement across the candidate, evaluation targets, current provenance, and publication-handoff target.
It will also confirm complete interaction and evaluation coverage.

A missing result, duplicate result, unresolved identity, mismatched identity, partial unit, or incomplete coverage will fail structural readiness.
An inconsistency between the completion marker and its underlying evidence will become a contradictory gate result and will block publication.

#### D02 Publication-gate semantic readiness inputs

The publication gate will consume the current accepted semantic results recorded in the current Pipeline provenance bundle.
It will not run a new universal model judgment over the complete Learning Unit.

The gate configuration will map accepted upstream evaluation results to every Learning-owned semantic readiness dimension:

- path coherence;
- per-post quiz suitability;
- source grounding;
- summary fidelity;
- phrase usefulness;
- option naturalness;
- contextual fit;
- generated-source separation.

Every required dimension must have complete accepted coverage for the complete current Learning Unit candidate.
A failed, incomplete, missing, uncovered, duplicate, or contradictory required result will block publication.
A pass in one dimension will not compensate for another dimension's failure or missing result.
Aggregate scores, majority voting, and a universal model verdict will not override any required result.

The gate will judge only the current result set supplied through current provenance.
Formation, replacement, reuse, and reevaluation of current results remain T06 orchestration responsibilities.
T05 will not introduce generated-artifact revision identity or historical evaluation comparison.

#### D03 Contradictory validation state fails closed

Contradictory validation means the current publication-gate input set is internally inconsistent.

Examples, not exhaustive:

- content-validation completion claims success while one required current result is non-accepted;
- one current result contains a success verdict and a controlled failure condition that cannot both be true;
- required coverage claims completion while the supplied current evidence proves missing or conflicting coverage.

Such contradictions indicate a defective aggregation state, invalid gate input, or Pipeline defect rather than an ordinary content-quality failure.
The publication gate will not repair the state, infer which claim is authoritative, or ask a universal model to choose.
It will fail closed and produce a rejected publication decision with a contradictory-validation cause.

An initial publication contradiction will create no current published state.
A replacement contradiction will leave the previous committed current state unchanged.
An availability-change contradiction will leave the previous committed availability unchanged.
Retry, rerun, and defect-recovery behavior remain T06 responsibilities.

#### D04 Human approval boundary

Human approval will apply to publication policy and gate evidence rather than routine per-unit publication.

Humans will approve:

- the publication-gate criteria and intended meaning;
- representative golden fixtures;
- representative harder fixtures;
- material changes to gate criteria or their intended meaning.

Routine Learning Units may be evaluated and published automatically after the active gate configuration is approved for unattended publication.
The first MVP will not require individual human approval for every Learning Unit.

A borderline case will escalate only when accepted criteria do not determine the policy judgment.
Escalation will seek a policy decision rather than an exceptional one-unit override.
The resulting decision may require a criteria change, fixture change, or other accepted authority before unattended processing resumes for that case class.

An implementation-only change does not automatically require policy approval when it preserves accepted criteria meaning.
The changed configuration must still satisfy applicable gate-configuration validation before unattended use.

#### D05 Unattended publication eligibility

A gate configuration may be used for unattended publication only after it is validated against the human-approved criteria, representative golden fixtures, and representative harder fixtures.

Validation will confirm that the configuration:

- covers every required structural readiness condition;
- covers every required Learning-owned semantic dimension;
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

A material criteria-meaning change additionally requires the human approval defined by D04.
Concrete model names, prompt text, threshold values, and execution mechanisms remain outside T05.

#### D06 Publication and availability outcome meanings

`available` and `unavailable` are current published-state values.
`rejected`, `withdrawn`, and `restored` are Pipeline decision outcomes or transitions rather than additional Application-visible availability values.

| term | meaning |
|---|---|
| `available` | The committed current Learning Unit may enter new queues and new learner flows. |
| `unavailable` | The committed current Learning Unit remains retained but cannot enter new queues or new learner flows. |
| `rejected` | The current publication candidate or requested change is not adopted. The committed current state remains unchanged. |
| `withdrawn` | An existing committed current state changes from `available` to `unavailable`. |
| `restored` | An existing committed current state changes from `unavailable` to `available` without changing content or provenance. |

A rejected initial publication will create no current published state.
A rejected replacement will preserve the previous committed current state.
A rejected availability change will preserve the previous committed availability.

Withdrawal will preserve current content, source references, source evidence, attribution, and current provenance.
Restoration without content change will use `AvailabilityChange` and preserve current content and provenance.
Republication with new or changed content will use `PublicationHandoff` rather than availability-only restoration.

The Application will continue to interpret only `available` and `unavailable`.
Pipeline decision causes and transition labels will remain Pipeline-owned.

#### D07 Current publication provenance and opaque external reference

Each committed current published Learning Unit will have one matching Pipeline-owned current provenance bundle.

The current provenance bundle will retain:

- retained authentic-source and valid Learning Path references;
- current generation-stage evidence;
- stage-specific provider, prompt, and validator provenance;
- Source Adapter Version;
- Common Pipeline Version;
- structural readiness results;
- all required semantic readiness results;
- the gate configuration used for the decision;
- golden- and harder-fixture validation evidence for that configuration;
- the publication-gate result that established the current content;
- the availability selected by that publication decision.

Concrete provenance schema, identifier encoding, and persistence layout remain implementation choices.

Application-facing current published state will contain only one opaque provenance reference.
Application code and the PWA will not parse, interpret, expose, or use Pipeline provenance for runtime decisions.
The opaque provenance reference will not become part of `LearningUnitRef`.

A `PublicationHandoff` that introduces or replaces content will replace the complete content, matching current provenance bundle, opaque provenance reference, and resulting availability together.
A mixed state containing content and provenance from different publication decisions is invalid.

An availability-only withdrawal or restoration will preserve the complete content, current provenance bundle, and opaque provenance reference.
Pipeline will retain separate internal evidence for the current availability decision.
That evidence will not replace the provenance bundle for the unchanged content.

A rejected unpublished candidate may retain Pipeline-internal rejection evidence.
It will not create Application-facing current publication provenance or an opaque current-state reference.

#### D08 PublicationHandoff contract

`PublicationHandoff` will introduce the first current published state or replace the complete current published state for one stable Learning Unit identity.

Its semantic input will contain:

- stable Learning Unit identity;
- one complete Learning Unit;
- one opaque provenance reference;
- resulting availability of `available` or `unavailable`.

The handoff preconditions are:

- the Learning Unit is complete;
- T04 content-validation completion is established;
- the publication gate accepted the candidate;
- every required structural and semantic readiness condition passed;
- one complete matching current provenance bundle exists;
- the opaque provenance reference identifies that bundle;
- identity, content, provenance, and decision targets agree;
- resulting availability matches the Pipeline publication decision.

A successful initial handoff will produce exactly one complete committed current state.
A successful replacement will atomically replace the complete content, matching provenance reference, and resulting availability under the same stable identity.
Replacement will not create a sibling Learning Unit or a second current projection.

A failed precondition will produce no published-content mutation.
A failed initial write will leave no current state.
A failed replacement will leave the previous complete committed current state unchanged.
No partial or mixed content-and-provenance state may become observable.

Concrete transaction syntax, locking, isolation, and persistence technology remain implementation concerns.

#### D09 AvailabilityChange contract

`AvailabilityChange` will change only the availability of one existing complete current published state.

Its semantic input will contain:

- stable Learning Unit identity;
- resulting availability of `available` or `unavailable`.

The change preconditions are:

- exactly one complete current published state exists for the stable identity;
- one Pipeline-owned availability decision exists;
- the decision target matches the input identity;
- the requested availability differs from the committed current value;
- no contradictory decision evidence remains.

A successful withdrawal will change `available` to `unavailable`.
A successful restoration will change `unavailable` to `available`.

An availability-only change will preserve:

- the complete Learning Unit content;
- interaction order;
- source references and source evidence;
- learner-visible attribution;
- the current provenance bundle;
- the opaque provenance reference;
- the stable Learning Unit identity.

A missing current state, no-op requested value, failed precondition, or failed write will produce no mutation.
The previous complete committed current state will remain unchanged.
`AvailabilityChange` will not create a new current state or introduce changed content.
Changed or new content must use `PublicationHandoff`.

Concrete transaction syntax, locking, isolation, and persistence technology remain implementation concerns.

#### D10 Pipeline-writer and Application-reader ownership separation

Pipeline will own:

- publication-gate execution;
- `rejected`, `withdrawn`, and `restored` decisions;
- `PublicationHandoff` and `AvailabilityChange` initiation;
- current provenance bundles and opaque provenance references;
- published current-state mutation;
- mutation preconditions and atomic complete-state replacement.

Application will own:

- reads of committed current published state;
- interpretation of `available` and `unavailable`;
- available-unit selection;
- availability recheck during retrieval;
- return of one complete Learning Unit.

Application will not reevaluate publication readiness, inspect validation results, parse Pipeline provenance, interpret rejection causes, or repair partial state.
Pipeline will not own queue construction, runtime selection, `LearningUnitRef` consumption, or Application read-result semantics.

Application reads may observe only the previous complete committed state or the new complete committed state.
They must not observe an in-progress or partial replacement.
Shared physical persistence is allowed, but Application contracts will not depend on Pipeline processing schemas or internal validation data.

### Accepted ADR materialization

The user-approved decision register was materialized into three accepted Pipeline ADRs:

- PRODUCT-ADR-PIPELINE-017 owns complete non-compensating publication-gate evidence, contradictory-state rejection, human approval, harder fixtures, and unattended-publication eligibility.
- PRODUCT-ADR-PIPELINE-018 owns publication and availability outcome meanings, current publication provenance, and the opaque external provenance reference.
- PRODUCT-ADR-PIPELINE-019 owns `PublicationHandoff`, `AvailabilityChange`, atomic current-state replacement, availability-only preservation, and Pipeline-writer/Application-reader separation.

No normative specification changed during T05 ADR authoring.
Retry, fallback, rerun, batch continuation, and recovery execution remain T06 scope.

Final T05 verification completed successfully.
`git diff --check` completed without reported error.
Strict specification validation returned `[strict]  All 34 file(s) OK.`
`git status --short` showed only the T05 Task, parent Work Item, and three new T05 ADRs.

PRODUCT-TASK-PIPELINE-001-05 is `done`.
