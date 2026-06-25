# PRODUCT-INV-PIPELINE-001: First golden question-and-reply fixture

- **status**: concluded
- **date**: 2026-06-24
- **trigger**: A concrete question-and-reply fixture is required before defining later pipeline contracts.
- **scope**: Select one suitable Python Discussions source sequence and materialize one reviewed question interaction and one reviewed reply interaction. Use the fixture as evidence for later pipeline design.
- **non_scope**: Excludes the final normative package schema, automation, UI implementation, and final licensing or redistribution decisions.
- **source_refs**:
  - spec:product.learning.learning_model
  - spec:product.learning.learning_unit
  - spec:product.learning.quiz_session
  - spec:product.pipeline
  - PRODUCT-ADR-LEARNING-004
  - PRODUCT-ADR-PIPELINE-003
- **follow_up_candidates**:
  - spec:product.pipeline.learning_unit_package
  - Review-result contract.
  - Source licensing and redistribution investigation, if required.

## Investigation scope

This investigation authored one reviewed question-and-reply pair from one coherent Python Discussions source sequence.

The investigation covered these phases:

1. Select and compare source candidates from the Packaging category.
2. Distinguish source-native relationships, tree projection, and selected source-sequence order.
3. Generate one question interaction for the opening post and one reply interaction for the first response.
4. Retain later source turns as untested continuation evidence without defining a no-quiz turn type.
5. Materialize the reviewed golden fixture under `product/fixture`.
6. Evaluate the fixture against the current learning and pipeline contracts.
7. Extract evidence for later package-boundary and field decisions.

The fixture will remain local investigation evidence.
The fixture will not establish a normative serialized schema.

## Out of scope

- Final normative learning-unit package schema.
- Automated source ingestion or relationship reconstruction.
- Automated quiz generation or phrase extraction.
- Concrete UI implementation.
- Automated publication.
- Final licensing, retention, attribution, or redistribution decisions.
- Changes that reverse or silently modify accepted ADRs.

## Background

The current learning model uses real technical conversation trees as the primary learning source.
Generated quiz abstractions must remain separate from authentic source conversation.

The first MVP reveals one coherent branch through mixed question-and-reply interactions.
Later interactions remain hidden until earlier interactions finish.
This investigation tests one question interaction and one reply interaction only.
Later selected turns remain outside the interaction-generation scope of this investigation.

The pipeline contract selects public `discuss.python.org` Packaging topics as the initial corpus.
The pipeline also requires source fidelity, provenance, validation, and human review before publication.

Before this investigation, `product/fixture` contained no reviewed question-and-reply pair.
No fixture demonstrated that both interaction types could work within one source sequence.

Defining package fields before authoring a complete fixture would have relied on assumptions.
The completed fixture now provides evidence for later package-boundary work.

## What was investigated

The investigation examined these questions:

1. What makes a source branch suitable for one learning session?
2. Which authentic turns are required for conversational coherence?
3. Can one opening-post quiz and one reply quiz work within the same source sequence?
4. Can later source turns be retained without treating them as validated quiz steps?
5. How much technical detail can the generated context remove?
6. Which generated options are useful without becoming false source reconstructions?
7. Which source phrases deserve highlighting?
8. What attribution and provenance must the fixture retain?
9. What responsibilities emerge naturally from the completed fixture?
10. Do the current learning specs contain gaps or contradictions?
11. What evidence supports later package-boundary work?

Candidate source-selection heuristics:

- Candidate: Use one coherent reply branch.
- Candidate: Retain three to eight authentic source turns.
- Candidate: Materialize one question quiz and one reply quiz as minimum experiment evidence.
- Candidate: Prefer low dependence on external documents.
- Candidate: Prefer reusable conversational phrases.
- Candidate: Preserve enough context to understand each reply.
- Candidate: Avoid code-heavy branches.

These heuristics are investigation inputs, not accepted contracts.

### Initial discovery-run correction

The initial topic-discovery run did not apply the intended Packaging filter.

`scripts/fetch_py_topics.py` called `fetch_topics(max_pages=3)` without category arguments.
The script therefore queried `/latest.json` and returned topics across all categories.
The printed output omitted `category_id`, so the scope error was not visible during candidate review.

At least topic `107763` belongs to Python Help rather than Packaging.
The earlier candidate-filtering and quiz-generation experiments remain valid learning-model evidence.
They do not establish Packaging corpus suitability or select a valid Packaging golden branch.

The script now calls the Packaging parent endpoint explicitly with slug `packaging` and category ID `14`.
That collection may return Packaging subcategory topics with their own category IDs.
The output prints `category_id` to expose future scope mismatches.
Packaging-specific source selection completed with topic `107565` and branch `#1 -> #2 -> #4 -> #7`.

## Findings

### Candidate discovery and source selection

A minimal title filter removed obvious announcements, release notices, and event notices.
The filter retained uncertain technical-discussion titles for opening-post review.

Opening-post review selected topics `107565` and `107491` as the strongest question-formulation candidates.
Topic `107565` was selected for the golden fixture.

Topic `107565` provided a coherent technical source sequence:

`#1 MattP -> #2 pf_moore -> #4 MattP -> #7 cjames23`

The arrows express selected source-sequence order. They do not claim that every edge is an explicit Discourse reply.

The source sequence met the investigation heuristics:

- the opening post contained reusable question phrasing;
- post `#2` directly challenged the proposal;
- posts `#4` and `#7` continued the same adoption and standardisation discussion;
- the interaction points remained understandable without reading linked documents;
- code and external examples were not required to understand the selected interaction points.

Topic `107491` also contained strong phrasing.
Topic `107491` was not selected because its discussion depended on emotionally sensitive circumstances around a contributor's death.

### Interaction coverage in this investigation

The fixture validated interactions for two selected source turns.

| post | investigation coverage | evidence |
|---|---|---|
| `#1` | Question interaction generated and reviewed | Supplies the question-formulation source phrase and authentic opening reveal. |
| `#2` | Reply interaction generated and reviewed | Supplies the reply-formulation source phrase and authentic reply reveal. |
| `#4` | Source continuation retained; quiz generation not investigated | Preserves the proposal author's next response in the selected sequence. |
| `#7` | Source continuation retained; quiz generation not investigated | Preserves a later response in the selected sequence. |

The absence of generated quizzes for posts `#4` and `#7` is an investigation limit.
The fixture does not establish a source-turn type that can omit a quiz.

### Golden session composition

The completed fixture is stored under:

`product/fixture/golden/topic-107565`

The fixture contains:

- `source-posts.json`;
- `question-interaction.json`;
- `reply-interaction.json`;
- `README.md`;
- `review.md`.

The reviewed interaction sequence is:

1. show the generated question-formulation interaction;
2. reveal authentic post `#1`;
3. show the generated reply-formulation interaction;
4. reveal authentic post `#2`.

Posts `#4` and `#7` remain in the selected source sequence.
This investigation did not generate or review their corresponding reply interactions.

The sequence demonstrates progressive reveal for one question-and-reply pair.
The generated interactions remain separate from the authentic source posts.

### Question-formulation interaction

The accepted question interaction uses post `#1` as its authentic source turn.

The accepted highlighted phrase is:

> Does including the `targets` as a key confuse users that lack a thorough understanding of their backend?

The accepted interaction contains three natural questions with distinct intents.
Exactly one option best fits the generated context.

The final prompt is:

`product/fixture/experiments/gpt-oss-20b/question-quiz-generation/prompt-v5-topic-107565-golden-run.md`

### Reply-formulation interaction

The accepted reply interaction uses post `#2` as its authentic source turn.

The accepted highlighted phrase is:

> Without a frontend using these new APIs, I don't see a good reason for standardising anything.

The accepted interaction contains three natural replies with distinct concerns.
Exactly one option best fits the generated context.

The reply-generation input used the accepted generated question as the visible prior turn.
The input did not include the full raw post `#1` because the full post consumed too much of the local model context window.
Post `#2` remained the authentic source for reply grounding and phrase attribution.

The final prompt is:

`product/fixture/experiments/gpt-oss-20b/question-quiz-generation/prompt-v1-reply-topic-107565-golden-run.md`

### Model and review evidence

Medium-reasoning `gpt-oss-20b` produced acceptable drafts after prompt refinement.
An early topic `107565` question-generation run took approximately 37 seconds.

`Qwen3.6-27B` was tested as a comparison.
A deeper run took approximately 2 minutes 19 seconds on an RTX 3090.
The deeper run introduced unsupported fallback, skipping, and error-policy details.

A low-effort Qwen run reduced elaboration but still introduced unsupported ecosystem-readiness, compatibility, and tool-requirement claims.
The extra VRAM and latency did not improve acceptance quality for this bounded task.

Human review rejected structurally valid outputs when:

- generated options introduced unsupported technical facts;
- generated context changed the source social situation;
- options reconstructed authentic wording too closely;
- multiple options expressed the same intent;
- no option clearly fit the generated context best.

Human review remains necessary even when deterministic JSON and source-span checks pass.

### Source and provenance evidence

The fixture required source identity, attribution, reply relationships, authentic text, and exact highlighted spans.
The highlighted phrase must occur verbatim in its source turn.

A fresh Discourse API response was preserved as `source-topic.raw.json`.
`source-capture.json` records the request URL, capture timestamp, HTTP status, and SHA-256 digest.

The API-derived `source-posts.json` preserves source-native raw text, post IDs, timestamps, usernames, and reply targets.
The earlier whitespace-normalized fixture remains as `source-posts.pre-api-normalized.json` for comparison evidence.

The capture established these relationship facts:

| post | source-native `reply_to_post_number` | projected tree parent | selected sequence predecessor |
|---|---:|---:|---:|
| `#1` | `null` | none | none |
| `#2` | `null` | `#1` | `#1` |
| `#4` | `#2` | `#2` | `#2` |
| `#7` | `#4` | `#4` | `#4` |

Post `#2` is a topic-level response in the API.
The earlier tree builder projected topic-level responses under root post `#1` for traversal.
The selected source-sequence order also places post `#2` after post `#1`.
These three relationships have different meanings. One overloaded field would lose either source provenance or pedagogical intent.

The comparison found only whitespace and line-break differences in post text.
Both accepted source phrases still matched the API raw text exactly.
No generated interaction required regeneration.

### Package-boundary evidence

The completed fixture exposed these distinct responsibilities:

| responsibility | fixture evidence |
|---|---|
| Source topic and post preservation | `source-posts.json` |
| Source-native reply relationships | API `reply_to_post_number` values in `source-posts.json` |
| Projected conversation-tree parents | Root attachment applied by the tree builder for topic-level responses |
| Selected source-sequence order | Reviewed source sequence in `README.md` |
| Generated interaction content | `question-interaction.json` and `reply-interaction.json` |
| Authentic phrase attribution | `source_phrase` in each reviewed interaction |
| Session reveal order | `README.md` |
| Interaction coverage | Generated and reviewed interactions for posts `#1` and `#2`; untested continuation posts `#4` and `#7` |
| Generation provenance | Prompt IDs, model identity, reasoning level, and observed latency in `review.md` |
| Review outcome | Deterministic checks and human verdicts in `review.md` |

These responsibilities are evidence for later package design.
The fixture does not establish final field names, serialization, or ownership boundaries.

## Cross-cutting observations

### Mechanical and semantic responsibilities

Mechanical processing should preserve source identity, exact text, reply relationships, and deterministic validation.
LLM processing should generate bounded learner-facing context, options, explanations, and phrase-function descriptions.

Exact source fidelity cannot depend only on model behavior.
The review process needed a transport-fidelity check before attributing copied-character mismatches to the model.

### Context-window pressure

The full opening post was too large for efficient reply generation with the local model.
The accepted generated question supplied sufficient visible prior context for the reply interaction.

This result supports compact interaction-local model inputs.
It does not prove that generated prior turns can replace authentic context in every branch.

### Structured output behavior

Prompt-only JSON enforcement was unreliable during early reply-generation trials.
Shorter prompts with JSON-only requirements at both the beginning and end improved compliance.
API-level structured output remains preferable when the provider supports it.

### Current specification fit

The generated question-and-reply pair satisfies the minimum mixed-interaction experiment goal.
The investigation did not validate a complete session across every selected source turn.

The earlier record text incorrectly generalized untested continuation posts into a no-quiz turn type.
That generalization was removed because the experiment did not provide supporting evidence.

The missing contract is a pipeline-owned package boundary for source records, generated interactions, reveal sequencing, provenance, and review results.

## Follow-up judgment candidates

- Candidate: Define the normative learning-unit package boundary from fixture evidence.
- Candidate: Define a review-result contract for publication readiness.
- Candidate: Determine whether source licensing and redistribution require a separate investigation.

## Recommendation

A follow-up package-boundary effort appears preferable.
The effort should use this fixture as its primary worked example.
The follow-up should define semantic responsibilities before choosing serialized field names.

The follow-up should address:

- source snapshot versus normalized source text;
- branch representation and per-turn interaction coverage;
- interaction ordering and progressive reveal;
- generated content versus authentic content;
- prompt and model provenance;
- deterministic validation and human-review results.

A separate licensing and redistribution investigation appears appropriate before publication or corpus distribution.

## Follow-up artifact candidates

- `spec:product.pipeline.learning_unit_package`
- A review-result contract under the owning specification area.
- A source licensing and redistribution Investigation, if evidence requires one.

## Open questions

1. What is the canonical identity of a retrieved source snapshot?
2. Must the package retain both the raw API payload and normalized post text?
3. How should a source-independent model represent branch relationships and per-turn interaction links?
4. How should progressive reveal reference authentic turns and generated interactions?
5. Which generation provenance belongs in the publishable unit versus internal pipeline evidence?
6. What minimum human-review result is required before publication?
7. Which deterministic checks belong to package validation?
8. How should regeneration preserve stable source and interaction identities?
9. What attribution, retention, licensing, and redistribution rules apply to stored source text?
10. When is a compact generated prior turn sufficient for model input, and when is authentic ancestor context required?
