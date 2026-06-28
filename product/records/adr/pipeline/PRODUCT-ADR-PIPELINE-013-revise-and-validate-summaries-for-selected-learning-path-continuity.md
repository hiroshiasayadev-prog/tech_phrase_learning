# PRODUCT-ADR-PIPELINE-013: Revise and validate summaries for selected Learning Path continuity

- **status**: accepted
- **date**: 2026-06-28
- **depends_on**:
  - PRODUCT-ADR-PIPELINE-002
  - PRODUCT-ADR-PIPELINE-008
  - PRODUCT-ADR-PIPELINE-010
  - PRODUCT-ADR-PIPELINE-011
  - PRODUCT-ADR-LEARNING-005
  - PRODUCT-ADR-LEARNING-012
- **supersedes**:
- **migrated_to_spec**: 2026-06-28

## Context

A reusable summary may remain accurate while reading awkwardly inside one selected Learning Path.
The Learning contract allows a grounded path-specific revision for conversational continuity.

A revision may clarify references or reduce repetition.
A revision must not change source-author position, certainty, response meaning, technical claims, or attribution.

The Pipeline needs an ordered revision contract and independent checks for meaning preservation and path continuity.

## Decision

### Revision boundary

Path-specific summary revision will begin only after a candidate path becomes a valid Learning Path under PRODUCT-ADR-PIPELINE-010.

The Pipeline will process selected posts in source order.
Each revision unit will receive:

- valid Learning Path identity;
- target authentic-post identity;
- target post's accepted reusable summary;
- target post's structured position;
- target post's certainty or qualification;
- target post's conversational response meaning;
- every preceding accepted path-specific summary for the same path.

Later-post context will be excluded.
An unaccepted preceding revision will not enter the next revision unit.

### Permitted revision

Path-specific revision may improve:

- reference clarity;
- omitted-topic clarity;
- conversational continuity;
- unnecessary repetition;
- technical compression.

Revision must preserve:

- source-author position;
- source-author certainty or qualification;
- conversational response meaning;
- technical claims needed for understanding;
- source attribution;
- accepted phrase evidence;
- valid Learning Path identity.

An unchanged result is valid.
The Pipeline will not require a textual change when the reusable summary already fits the path.

Each result will identify:

- valid Learning Path identity;
- target authentic-post identity;
- revised summary or unchanged outcome;
- reason for any change.

Concrete serialized forms remain implementation choices.

### Independent semantic evaluation

Every revised or unchanged result will receive two independent semantic evaluation units.

| evaluation unit | owned judgment |
|---|---|
| Semantic preservation | The result preserves position, certainty, response meaning, technical claims, attribution, and source grounding without unsupported additions. |
| Path continuity | The result remains understandable after preceding accepted summaries through clear references, retained topics, correct conversational relation, and controlled repetition. |

Both evaluations must pass.
An unchanged result must still pass path continuity.

### Deterministic validation

Deterministic validation will establish:

- matching path identity;
- matching target-post identity;
- exactly one result for every selected post;
- source-order processing;
- mutually exclusive revised or unchanged outcomes;
- exclusion of later-post context;
- reference to accepted reusable-summary input;
- complete unique evaluation coverage;
- non-contradictory verdicts.

Only an accepted result may become the learner-visible summary for that path or enter later generation stages.

## Rationale

Sequential revision mirrors the learner-visible conversation order.
Preceding summaries provide enough continuity context without allowing future turns to rewrite earlier meaning.

Allowing unchanged results avoids unnecessary model edits.
Independent preservation and continuity checks distinguish source fidelity from path readability.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Use reusable summaries unchanged for every path | Accurate summaries can still contain unresolved references or awkward repetition. |
| Give each revision the complete path | Later turns can leak future meaning into earlier summaries. |
| Revise all summaries in one combined task | One model output can omit posts or hide which revision caused a failure. |
| Require every summary to change | Unnecessary rewriting increases semantic-drift risk. |
| Evaluate preservation and continuity together | A readable revision can change meaning, and a faithful revision can remain incoherent. |

## Consequences

- Every valid Learning Path receives zero or more grounded summary text changes.
- Revision runs in source order and depends on preceding accepted revisions.
- Later content cannot influence earlier learner-visible summaries.
- Accepted path-specific summaries become inputs to target-phrase and prompt generation.
- Stage-specific provider, prompt, and validation provenance remains governed by PRODUCT-ADR-PIPELINE-008.
- Concrete prompts, models, schemas, thresholds, and retry execution remain deferred.

## Evidence

- PRODUCT-ADR-LEARNING-005 authorizes grounded path-specific revision for continuity.
- PRODUCT-ADR-LEARNING-012 requires summary fidelity and path coherence to pass independently.
- PRODUCT-ADR-PIPELINE-010 establishes valid Learning Paths and excludes later summaries from target-reply suitability context.
- PRODUCT-ADR-PIPELINE-011 establishes accepted reusable-summary inputs and structured semantic fields.
- The user selected source-order revision, all preceding accepted summaries, no later-post context, valid unchanged results, and two independent evaluations.
