# PRODUCT-ADR-PIPELINE-011: Generate and independently validate reusable source-post summaries

- **status**: accepted
- **date**: 2026-06-28
- **depends_on**:
  - PRODUCT-ADR-PIPELINE-002
  - PRODUCT-ADR-PIPELINE-005
  - PRODUCT-ADR-PIPELINE-006
  - PRODUCT-ADR-PIPELINE-008
  - PRODUCT-ADR-PIPELINE-010
  - PRODUCT-ADR-LEARNING-005
  - PRODUCT-ADR-LEARNING-012
- **supersedes**:
- **migrated_to_spec**:

## Context

PRODUCT-ADR-PIPELINE-010 requires grounded reusable summaries before semantic path filtering.
The Pipeline must create one reusable summary without mixing sibling, later, quoted, or unrelated author content.

The Learning contract requires every learner-visible summary to preserve:

- technical meaning needed for the interaction;
- source-author position;
- source-author certainty or qualification;
- conversational response meaning;
- source grounding without unsupported claims.

A natural-looking prose summary can still reverse position, remove uncertainty, or misattribute quoted content.
The Pipeline needs structured summary meaning and independent semantic checks before reuse.

## Decision

### Generation input

Reusable-summary generation will receive the target authentic post's complete authored text and source binding.
Quoted material will remain separated from authored text.

An opening post will receive no prior-post summary context.
A later post will receive every validated reusable summary on its mechanically derived ancestor chain.
The ancestor summaries will appear in source order from the opening post through the immediate predecessor.

The generation unit will exclude:

- sibling posts;
- later posts;
- unrelated discussion posts;
- unvalidated summaries;
- quiz content.

Resolved quote identity and exact quote evidence may enter as separated context.
Quoted evidence will not establish the target author's position or phrase evidence.

Silent truncation is invalid.
Generation may proceed only after complete authored-text coverage is established.

### Generation output

Reusable-summary output will contain these semantic elements:

- target authentic-post identity;
- reusable English summary text;
- source-author position;
- source-author certainty or qualification;
- conversational response meaning.

The semantic elements will remain distinct.
The separation allows validation to detect a prose summary that sounds natural but changes meaning.

Technical-burden and phrase-learning-potential labels are not required summary fields.
Concrete serialized field names and controlled vocabularies remain implementation choices.

### Independent semantic evaluation

Every structurally valid reusable summary will receive four independent semantic evaluation units.

| evaluation unit | owned judgment |
|---|---|
| Position fidelity | The summary preserves the source author's adopted position or question. |
| Certainty fidelity | The summary preserves uncertainty, qualification, and claim boundaries. |
| Response-meaning fidelity | The summary preserves what the post responds to and how it responds. |
| Unsupported-claim and attribution detection | The summary adds no unsupported claim and attributes no quoted or other-author claim to the target author. |

Every valid pass will identify:

- the target authentic-post identity;
- the evaluated dimension;
- a non-empty explanation;
- exact evidence from the target post's authored text.

Deterministic validation will establish:

- complete and unique evaluation coverage;
- matching target identity;
- exact evidence membership in authored text;
- quote exclusion;
- non-contradictory verdicts.

Any valid semantic failure will reject the generated summary as a grounding failure.
Invalid evaluator output will remain distinct from a content rejection.

Only an accepted reusable summary may enter ancestor context, phrase-evidence extraction, or path filtering.

## Rationale

Complete authored text prevents silent information loss.
Ancestor-only context preserves the conversation needed to understand one reply without introducing sibling or future claims.

Structured position, certainty, and response meaning expose failure modes hidden by fluent prose.
Independent evaluations keep each local-model judgment narrow.
Exact authored-text evidence lets deterministic validation reject invented support.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Generate each summary from the target post alone | Later replies may require prior conversational context to preserve response meaning. |
| Give the generator the complete discussion | Sibling and later content can distort attribution and increase irrelevant context. |
| Pass only the immediate predecessor summary | Recursive compression can hide earlier context needed to interpret a later reply. |
| Return summary prose only | Fluent prose can conceal position reversal, lost uncertainty, or changed response meaning. |
| Use one combined semantic verdict | One model judgment can omit an independently required fidelity dimension. |
| Accept model-asserted grounding without exact evidence | Deterministic source verification would be impossible. |

## Consequences

- Reusable summaries become validated shared artifacts before path filtering.
- Later posts may consume every accepted ancestor summary in source order.
- Sibling and future context remain unavailable to reusable-summary generation.
- Summary generation and summary semantic evaluation remain separate bounded tasks.
- PRODUCT-ADR-PIPELINE-010 may consume only accepted reusable summaries.
- Stage-specific provider, prompt, and validation provenance remains governed by PRODUCT-ADR-PIPELINE-008.
- Concrete prompts, models, schemas, thresholds, storage layouts, and retry execution remain deferred.

## Evidence

- PRODUCT-ADR-LEARNING-005 establishes reusable summaries and grounded path-specific revisions.
- PRODUCT-ADR-LEARNING-012 establishes non-compensating summary fidelity and source grounding.
- PRODUCT-ADR-PIPELINE-006 separates authored text from quoted material and retains source relationships.
- PRODUCT-ADR-PIPELINE-010 requires grounded reusable summaries for independent path filtering.
- PRODUCT-INV-PIPELINE-001 and PRODUCT-INV-PIPELINE-002 provide non-normative evidence of quote attribution and summary-fidelity failures.
- The user selected complete authored text, ordered ancestor summaries, structured semantic fields, and four independent evaluations.
