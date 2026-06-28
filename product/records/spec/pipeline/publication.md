# Concept: Pipeline publication

- **id**: `spec:product.pipeline.publication`
- **status**: draft
- **date**: 2026-06-28
- **parent**: `spec:product.pipeline`

## What this is

Pipeline contract for publication-gate authorization, publication outcomes, complete current-state handoff, and availability-only mutation.
The contract writes the Application-owned published-content boundary without redefining runtime read semantics.

## Non-goals

- Learning-owned readiness criteria meaning.
- Application queue, retrieval, or availability-result behavior.
- Database schema, transaction syntax, locking, or isolation level.
- Concrete gate models, prompts, thresholds, or execution technology.
- Historical publication revisions, exact replay, or rollback state.

## Concept model

| concept | contract |
|---|---|
| Publication gate | Separate authorization boundary after content-validation completion. |
| Gate configuration | Current mapping and behavior used to evaluate complete structural and semantic readiness evidence. |
| Unattended-publication eligibility | Approval state established through human-approved criteria and fixture validation. |
| Publication outcome | Pipeline-owned decision or transition affecting adoption or availability. |
| `PublicationHandoff` | Complete initial publication or current-content replacement operation. |
| `AvailabilityChange` | Availability-only withdrawal or same-content restoration operation. |

## Rules

### Publication-gate input

The gate must consume accepted upstream results rather than rerun generation or semantic evaluation.

Required current input includes:

- stable Learning Unit identity;
- one complete Learning Unit candidate;
- accepted structural validation results;
- complete source bindings for every interaction;
- complete unit attribution;
- generated-source separation results;
- complete and unique required semantic coverage;
- one matching current provenance bundle;
- content-validation completion under `spec:product.pipeline.validation`.

- The gate must not trust a completion marker in isolation.
- The gate must deterministically confirm interaction coverage, evaluation coverage, and identity agreement.
- Missing, duplicate, unresolved, mismatched, partial, or uncovered evidence must fail structural readiness.

### Semantic readiness coverage

- The active gate configuration must map accepted upstream evidence to every semantic readiness dimension in `spec:product.learning.learning_unit`.
- Every required dimension must have complete accepted coverage for the complete current candidate.
- Failed, incomplete, missing, uncovered, duplicate, or contradictory required evidence must block publication.
- A pass in one dimension must not compensate for another dimension.
- Aggregate scores, majority voting, and a universal model verdict must not override required evidence.
- The gate must judge only the current result set represented by current provenance.
- Generated-artifact revision identity and historical comparison are not required.

### Contradictory gate state

Contradictory validation means the current gate input contains internally incompatible claims.

- The gate must not repair contradiction or infer which claim is authoritative.
- The gate must not ask a universal model to choose between conflicting claims.
- Contradictory evidence must fail closed.
- The resulting publication decision must be `rejected` with a contradictory-validation cause.
- A contradictory decision must produce no published-content mutation.

### Human approval and unattended publication

Humans must approve:

- publication-gate criteria and intended meaning;
- representative golden fixtures;
- representative harder fixtures;
- material changes to criteria or intended meaning.

A gate configuration is eligible for unattended publication only after validation confirms:

- every required structural condition is covered;
- every required semantic dimension is covered;
- every approved golden fixture produces its expected decision;
- every approved harder fixture produces its expected decision;
- fixture runs contain no missing, incomplete, uncovered, or contradictory required result;
- validation evidence identifies the exact configuration used for unattended publication.

- Passing golden fixtures alone is insufficient.
- Behavior-affecting configuration changes require fixture revalidation before unattended use.
- Material criteria-meaning changes additionally require human approval and accepted authority.
- Routine units do not require individual human approval after configuration approval.
- Borderline policy cases must seek criteria or authority resolution rather than a one-unit override.

### Publication outcomes

Application-visible availability remains limited to the values defined by `spec:product.application.published_content.availability`.
Pipeline-owned decision outcomes are:

| outcome | meaning |
|---|---|
| `rejected` | The candidate or requested change is not adopted; committed current state remains unchanged. |
| `withdrawn` | Existing current state changes from `available` to `unavailable`. |
| `restored` | Existing current state changes from `unavailable` to `available` without content or provenance replacement. |

- A rejected initial publication creates no current published state.
- A rejected replacement preserves the previous committed current state.
- A rejected availability change preserves the previous committed availability.
- Withdrawal preserves content, source references, source evidence, attribution, and current content provenance.
- Same-content restoration preserves content and current content provenance.
- Changed content must use complete replacement rather than availability-only restoration.
- Application and UI must not interpret Pipeline decision causes or transition labels.

### Current publication provenance

- Each committed current Learning Unit must have one matching provenance bundle under `spec:product.pipeline.artifact_identity_and_provenance`.
- Application-facing current state must contain one opaque reference to that matching bundle.
- Complete content replacement must replace content, matching provenance, opaque reference, and resulting availability together.
- Availability-only change must preserve the content provenance bundle and opaque reference.
- Separate Pipeline-internal evidence may record the current availability decision.

### `PublicationHandoff`

`PublicationHandoff` introduces initial current state or replaces complete current state for one stable Learning Unit identity.

Its semantic input contains:

- stable Learning Unit identity;
- one complete Learning Unit;
- one opaque provenance reference;
- resulting availability of `available` or `unavailable`.

Preconditions are:

- complete Learning Unit content;
- content-validation completion;
- accepted publication-gate decision;
- complete required structural and semantic readiness;
- one complete matching current provenance bundle;
- opaque reference resolution to that bundle;
- identity agreement across content, evidence, provenance, and decision;
- resulting availability agreement with the Pipeline decision.

- Successful initial handoff creates exactly one complete committed current state.
- Successful replacement atomically replaces complete content, matching opaque provenance reference, and resulting availability under the same identity.
- Replacement must not create a sibling Learning Unit or second current projection.
- Failed preconditions must produce no mutation.
- Failed initial write must leave no current state.
- Failed replacement must preserve the previous complete committed current state.
- No partial or mixed content-and-provenance state may become observable.

### `AvailabilityChange`

`AvailabilityChange` changes only availability for one existing complete current state.

Its semantic input contains:

- stable Learning Unit identity;
- resulting availability of `available` or `unavailable`.

Preconditions are:

- exactly one complete current state exists;
- one Pipeline-owned availability decision exists;
- decision and input identity agree;
- requested availability differs from committed availability;
- no contradictory decision evidence remains.

- Successful withdrawal changes `available` to `unavailable`.
- Successful restoration changes `unavailable` to `available`.
- The operation must preserve complete content, interaction order, source evidence, attribution, stable identity, current content provenance, and opaque provenance reference.
- Missing state, no-op value, failed precondition, or failed write must produce no mutation.
- Changed or new content must use `PublicationHandoff`.
- `AvailabilityChange` must not rerun content generation or the publication gate.

### Atomicity and ownership

- Each successful operation must expose one committed state transition.
- Application readers may observe only the previous complete state or new complete state.
- Pipeline owns publication decisions, mutation initiation, mutation preconditions, current provenance, and writes.
- Application owns reads and interpretation of committed `available` and `unavailable` state.
- Application must not reevaluate readiness, inspect validation, parse provenance, interpret rejection causes, or repair partial state.
- Shared physical persistence is allowed without shared semantic ownership.

## Boundary

| concern | owner |
|---|---|
| Readiness meaning | `spec:product.learning.learning_unit`. |
| Content-validation completion | `spec:product.pipeline.validation`. |
| Gate authorization, outcomes, and writes | `spec:product.pipeline.publication`. |
| Retry, rerun, batching, and mutation exhaustion | `spec:product.pipeline.orchestration`. |
| Committed current-state reads and availability interpretation | `spec:product.application.published_content`. |
| Transaction implementation | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.pipeline` | Parent Pipeline overview. |
| `spec:product.pipeline.validation` | Supplies complete current validation evidence. |
| `spec:product.pipeline.artifact_identity_and_provenance` | Supplies matching current provenance and opaque reference. |
| `spec:product.pipeline.orchestration` | Coordinates publication, retry, rerun, and availability-only paths. |
| `spec:product.learning.learning_unit` | Defines structural and semantic publication readiness. |
| `spec:product.application.published_content` | Defines the committed current state read by Application. |
| PRODUCT-ADR-PIPELINE-017 | Establishes complete gate evidence and unattended-publication eligibility. |
| PRODUCT-ADR-PIPELINE-018 | Establishes outcomes and opaque current provenance. |
| PRODUCT-ADR-PIPELINE-019 | Establishes atomic handoff and availability-only mutation. |
