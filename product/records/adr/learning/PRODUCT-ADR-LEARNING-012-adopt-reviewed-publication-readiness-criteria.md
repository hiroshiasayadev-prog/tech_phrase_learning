# PRODUCT-ADR-LEARNING-012: Adopt reviewed publication-readiness criteria

- **status**: accepted
- **date**: 2026-06-27
- **depends_on**: [PRODUCT-ADR-LEARNING-005, PRODUCT-ADR-LEARNING-007, PRODUCT-ADR-LEARNING-008, PRODUCT-ADR-LEARNING-009, PRODUCT-ADR-LEARNING-010, PRODUCT-ADR-LEARNING-011]
- **supersedes**: []
- **migrated_to_spec**: 2026-06-27

## Context

PRODUCT-ADR-LEARNING-005 requires every learning unit to pass an automated publication gate before becoming session-available.
It assigns human approval to publication criteria and material changes rather than to every generated unit.

The current Learning specification names source grounding, summary fidelity, phrase usefulness, option naturalness, and contextual fit.
Those dimensions are dispersed and do not yet form one complete publication-readiness decision.

PRODUCT-INV-LEARNING-001, PRODUCT-INV-PIPELINE-001, and PRODUCT-INV-PIPELINE-002 investigated local-model generation, path filtering, source fidelity, summary quality, phrase evidence, option quality, deterministic validation, and human review.

The investigations found that bounded local models can produce usable candidate content.
They also found failures that structurally valid output alone does not detect.

Observed failure classes include:

- unsupported technical claims;
- changed source positions or certainty;
- quoted text attributed to the wrong author;
- technically exact but pedagogically weak phrase candidates;
- unnatural or insufficiently contrasting options;
- no uniquely best option for the stated context;
- incomplete evaluation coverage;
- contradictory selected and rejected path results.

The investigation records are evidence rather than normative decision authority.
The product must explicitly adopt the quality contract before T03 reflects it into Learning specifications.

## Decision

A first-MVP learning unit is publication-ready only when it satisfies both structural readiness and semantic readiness.

### Structural readiness

The publication gate must establish all applicable structural conditions:

- the learning path is valid under the accepted Learning path contract;
- every selected source post has exactly one interaction;
- every required field is present and non-empty;
- every interaction has exactly three answer options;
- option identities are unique within the interaction;
- exactly one correct-option reference resolves to an option in that interaction;
- every interaction retains a route to its authentic source post;
- source-derived and generated content remain distinguishable;
- required unit-level attribution is complete;
- every required automated evaluation result covers the complete unit scope;
- internally contradictory gate results are rejected.

The Pipeline may add stricter deterministic checks when they preserve this meaning.

### Semantic readiness

The publication gate must evaluate these Learning-owned quality dimensions:

| dimension | publication-ready meaning |
|---|---|
| Path coherence | The ordered summaries and interactions remain understandable as one connected technical exchange. |
| Per-post quiz suitability | Every selected source post supports one useful phrase-learning interaction. |
| Source grounding | Each summary, conversational move, and target phrase remains supported by the corresponding authentic source post. |
| Summary fidelity | Each learner-visible summary preserves the source author's position, certainty, and conversational response without unsupported claims. |
| Phrase usefulness | Each target phrase is natural, reusable conversational English rather than technical vocabulary alone. |
| Option naturalness | Every option is grammatical, natural, useful English and does not introduce unsupported technical claims. |
| Contextual fit | Exactly one option best fits the prompt and directly realizes the target phrase for the stated conversational intent. |
| Generated-source separation | Generated prompts, summaries, phrases, and options are not presented as authentic quotations or source-authored wording. |

A unit fails publication readiness when any required dimension fails.
A high aggregate score must not compensate for a failed required dimension.

### Review and automation boundary

The first MVP does not require human approval for every learning unit.

Humans will approve:

- the publication-readiness criteria;
- representative golden and harder evaluation fixtures;
- material changes to the criteria or their intended meaning;
- borderline policy judgments that cannot be resolved by the accepted criteria.

Routine learning units may become available through an approved automated gate.

A model-only success result is insufficient.
The automated gate must combine deterministic validation with semantic quality evaluation.

A local model may generate candidates or contribute quality judgments when the Pipeline has evidence that it satisfies the approved gate role.
No particular model, reasoning level, prompt, threshold, retry policy, or scoring implementation is adopted by this ADR.

The current investigation evidence supports local models as provisional bounded components.
It does not by itself establish unattended production-grade publication accuracy across unseen content.
Pipeline validation must use representative harder fixtures before treating a gate configuration as approved for unattended publication.

## Rationale

Structural checks catch missing fields, broken references, incomplete coverage, and contradictory results.
They cannot establish naturalness, faithfulness, learning value, or conversational fit.

Semantic evaluation catches failures that remain valid JSON and satisfy cardinality rules.
The local-model experiments repeatedly demonstrated this distinction.

Required dimensions are preferable to one aggregate quality score because one severe grounding or fidelity failure can make an otherwise polished unit misleading.

Policy-level human approval preserves scalable generation without removing human responsibility for the definition of acceptable learning content.

Keeping concrete models, prompts, thresholds, retries, and evaluation implementations in Pipeline allows the implementation to improve without changing Learning meaning.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Treat schema and deterministic checks as sufficient | Structurally valid outputs introduced unsupported facts, attribution errors, and weak learning content. |
| Let one model verdict establish publication readiness | The investigations found incomplete coverage and model-specific judgment limits. |
| Use one aggregate score with compensating dimensions | A grounding or fidelity failure must not pass because other dimensions score highly. |
| Require human approval for every learning unit | Item-level review does not scale to the intended content volume. |
| Adopt one local model and prompt as Learning authority | Model, prompt, threshold, and retry choices belong to Pipeline and require ongoing evaluation. |
| Add new quality dimensions without investigation evidence | The current evidence already supports a sufficient first-MVP quality contract. |

## Consequences

- `spec:product.learning.learning_path` must consolidate path coherence and per-post quiz suitability.
- `spec:product.learning.learning_unit` must consolidate structural readiness and the learner-visible semantic quality dimensions.
- `spec:product.learning.learning_unit` must state that failure of one required dimension blocks publication.
- `spec:product.learning.learning_unit` must preserve policy-level human approval and automated per-unit gating.
- T03 must reconcile the accepted criteria without prescribing Pipeline algorithms.
- T04 must preserve generated-source separation and session availability semantics where they affect downstream contracts.
- Pipeline specifications must define deterministic checks, semantic evaluator inputs and outputs, coverage validation, retry behavior, thresholds, and release evidence.
- Pipeline must retain representative golden and harder fixtures for gate approval.
- A session-available unit may become unavailable when it no longer passes the approved gate.
- No new per-unit human-review requirement is introduced.

## Evidence

- PRODUCT-INV-LEARNING-001 found medium-reasoning local-model output sufficient for reviewed drafts while retaining human semantic review for naturalness, phrase usefulness, and option quality.
- PRODUCT-INV-PIPELINE-001 found that deterministic checks did not catch unsupported facts, changed social context, close source reconstruction, weak option contrast, or missing contextual fit.
- PRODUCT-INV-PIPELINE-002 found attribution errors caused by quoted text, incomplete automated-review coverage, summary compression risks, and disagreement over learning focus.
- PRODUCT-INV-PIPELINE-002 also found that GPT-OSS and Qwen passed the current easy binary-filter fixture, but that result did not prove unattended production-grade accuracy.
- PRODUCT-ADR-LEARNING-005 already establishes automated publication gating with human approval at the criteria level.
- The user explicitly adopted the investigated quality results as the formal first-MVP publication-readiness decision.
