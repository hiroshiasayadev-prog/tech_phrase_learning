# PRODUCT-ADR-PIPELINE-012: Extract and independently validate bounded source-grounded phrase evidence

- **status**: accepted
- **date**: 2026-06-28
- **depends_on**:
  - PRODUCT-ADR-PIPELINE-002
  - PRODUCT-ADR-PIPELINE-006
  - PRODUCT-ADR-PIPELINE-008
  - PRODUCT-ADR-PIPELINE-010
  - PRODUCT-ADR-PIPELINE-011
  - PRODUCT-ADR-LEARNING-005
  - PRODUCT-ADR-LEARNING-012
- **supersedes**:
- **migrated_to_spec**:

## Context

PRODUCT-ADR-PIPELINE-010 requires source-verified phrase candidates before per-post suitability filtering.
Reusable-summary generation and phrase-evidence extraction serve different purposes.

A reusable summary preserves post meaning.
Phrase evidence identifies authentic wording that may support one learner-facing target phrase.

A model can produce a plausible phrase that does not occur in the target author's text.
A model can also select technical vocabulary that lacks reusable conversational value.
The Pipeline needs bounded extraction, exact source binding, and independent semantic checks.

## Decision

### Separate bounded stage

Source-grounded phrase-evidence extraction will be separate from reusable-summary generation.
Summary failure and phrase-evidence failure will remain independently observable.

The extraction unit will receive:

- target authentic-post identity;
- complete target authored text;
- required question or reply interaction role;
- accepted reusable summary;
- ordered accepted ancestor summaries;
- quote-boundary evidence.

Every candidate text span must come from the target post's authored text.
Quoted text will not qualify as target-author phrase evidence.

### Candidate result

Extraction will return zero to three candidates for one target post.

Zero candidates is a valid semantic result.
The result means complete processing found no usable conversational phrase.
It is not an invalid provider output, grounding failure, or Pipeline execution failure.

Each non-zero candidate will identify:

- target authentic-post identity;
- exact authored-text span;
- source location sufficient to distinguish repeated text;
- required question or reply role;
- conversational function.

A candidate may contain technical terms.
A candidate will fail phrase usefulness when no reusable conversational English remains beyond technical vocabulary.

A path containing a post with zero accepted candidates will fail that post's PRODUCT-ADR-PIPELINE-010 suitability evaluation.
The zero-candidate result will not become a Pipeline execution failure.

### Deterministic validation

Deterministic validation will establish:

- matching target identity;
- exact authored-text membership;
- valid source location;
- no overlap with quoted material;
- matching interaction role;
- zero-to-three cardinality;
- no duplicate source span.

### Independent semantic evaluation

Every mechanically valid candidate will receive two independent semantic evaluation units.

| evaluation unit | owned judgment |
|---|---|
| Conversational-function fit | The claimed function matches how the exact phrase operates in the target post and prior context. |
| Phrase usefulness | The candidate is natural, reusable conversational English rather than technical vocabulary alone. |

Only candidates that pass both units will remain accepted phrase evidence.
One candidate may remain accepted when another candidate fails.

A zero-candidate extraction result will receive a separate semantic confirmation.
The confirmation will judge whether the complete target post contains no usable conversational phrase.
A bare model assertion will not establish an accepted zero-candidate result.

Only accepted phrase evidence may enter path filtering or target-phrase selection.

## Rationale

A separate extraction stage isolates source-span grounding from summary fidelity.
Zero-to-three candidates avoid forcing weak expressions from every post.

Exact authored-text spans enable deterministic grounding checks.
Independent function and usefulness evaluations keep contextual meaning separate from learning value.
Partial candidate retention avoids discarding valid evidence because a sibling candidate failed.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Generate summaries and phrase candidates in one model task | One failed responsibility would force regeneration of otherwise accepted output. |
| Require at least one phrase from every post | The model would invent or select weak expressions to satisfy cardinality. |
| Accept any exact text span | Technical identifiers and vocabulary alone do not provide reusable conversational English. |
| Allow phrases from quoted material | Quoted wording is not target-author phrase evidence. |
| Validate usefulness and function in one verdict | One dimension can pass while the other fails. |
| Treat zero candidates as provider failure | A post may genuinely lack a useful phrase while processing remains correct. |

## Consequences

- Phrase evidence becomes a distinct validated source artifact.
- PRODUCT-ADR-PIPELINE-010 consumes only accepted candidates.
- Target-phrase selection must trace to one accepted candidate from the same post.
- Zero accepted candidates prevent path suitability without reporting infrastructure failure.
- Stage-specific provider, prompt, and validation provenance remains governed by PRODUCT-ADR-PIPELINE-008.
- Concrete offsets, schemas, prompts, models, thresholds, and retry execution remain deferred.

## Evidence

- PRODUCT-ADR-LEARNING-005 requires source support for each target phrase.
- PRODUCT-ADR-LEARNING-012 establishes phrase usefulness and source grounding as independent readiness dimensions.
- PRODUCT-ADR-PIPELINE-006 separates authored text and quoted text.
- PRODUCT-ADR-PIPELINE-010 requires exact supplied phrase evidence for per-post suitability passes.
- PRODUCT-INV-PIPELINE-001 and PRODUCT-INV-PIPELINE-002 provide non-normative phrase-extraction examples and harder controls.
- The user selected a separate extraction stage, zero-to-three candidates, valid zero-candidate outcomes, and independent function and usefulness checks.
