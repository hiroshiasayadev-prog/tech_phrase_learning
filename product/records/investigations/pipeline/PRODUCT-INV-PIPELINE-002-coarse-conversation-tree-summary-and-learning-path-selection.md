# PRODUCT-INV-PIPELINE-002: Coarse conversation tree, post summaries, and learning-path selection

- **status**: concluded
- **date**: 2026-06-25
- **trigger**: The first golden fixture used a manually selected source sequence, while the current scripts only create a rough reply-tree projection and do not select learning paths.
- **scope**: Determine a lightweight pipeline that builds a coarse traversal tree from Discourse data, summarizes posts with `gpt-oss-20b`, derives multiple coherent path candidates, and filters them for English phrase learning.
- **non_scope**: Excludes exact reconstruction of every conversational dependency, exhaustive quote-span modeling, final serialized schemas, per-post quiz generation, concrete UI layout, and source-use policy.
- **source_refs**:
  - PRODUCT-INV-PIPELINE-001
  - PRODUCT-ADR-PIPELINE-001
  - PRODUCT-ADR-PIPELINE-003
  - spec:product.pipeline
  - spec:product.learning.learning_model
- **follow_up_candidates**:
  - A pipeline requirement for reproducible coarse-tree construction, authored-text derivation, summary generation, path enumeration, and absolute filtering.
  - A domain contract for retaining multiple valid paths with learning focus and source-verified phrase evidence.
  - App design for session-time path selection and quiz generation.
  - Harder filtering fixtures and path-specific learning-focus evaluation.

## Investigation scope

This investigation examined a lightweight path from one captured Discourse topic to a set of usable learning paths.

The resulting flow is:

1. retain the immutable source topic and posts;
2. preserve mechanically observable reply and quote references;
3. derive a coarse rooted tree for traversal;
4. generate a short summary and source-verified phrase candidates for each post;
5. enumerate bounded mechanically connected path candidates;
6. validate each candidate independently through deterministic checks and absolute filtering;
7. retain multiple valid paths with their learning focus and phrase evidence for later quiz generation.

The investigation does not require the derived tree to reproduce every semantic dependency in the original discussion.
The tree only needs to provide a useful search space for finding broadly coherent learning sequences.

Topic `107565` remains the primary worked example.
The sequence `#1 -> #2 -> #4 -> #7` is a reviewed valid example, not a unique canonical answer.
The experiments showed that other paths, including `#1 -> #2 -> #4 -> #5`, can provide different but equally usable learning value.

## Out of scope

- Reconstructing an exact or exhaustive Discourse conversation graph.
- Selecting one canonical parent from multiple quoted posts.
- Preserving every quoted text span as a first-MVP path-selection requirement.
- Reproducing all technical detail from long posts in learner-facing content.
- Generating or reviewing the required quiz for each selected post.
- Selecting or explaining source phrases.
- Defining a learning-unit output or persistence schema.
- Defining concrete UI layout or interaction behavior.
- Final licensing, attribution, retention, or redistribution policy.
- Reversing accepted learning-model or pipeline decisions.

## Background

`PRODUCT-ADR-PIPELINE-001` assigns mechanically observable source structure to deterministic processing and semantic judgment to bounded LLM tasks.

`PRODUCT-ADR-PIPELINE-003` requires explicit reply and reference relationships to be reconstructed before short conversation segments are selected.
This requirement does not imply that the first MVP must reproduce every semantic dependency as one exact tree.
Observable source relationships can remain preserved separately from a derived traversal projection.

The product goal is English phrase learning, not archival reproduction of technical discussions.
Long posts often contain code, link lists, examples, and technical detail that are unnecessary for understanding the conversational movement.
Showing all source text directly may turn a phrase-learning session into a technical-reading task.

A useful first-MVP pipeline may therefore:

- retain complete source posts for provenance and validation;
- construct a rough tree for candidate discovery;
- summarize each post for semantic comparison and path selection;
- later show generated summaries, short source excerpts, and exact source phrases instead of every complete post.

Generated summaries must remain distinguishable from authentic source text.
The source snapshot remains the authority for fidelity checks and exact phrase attribution.

## What was investigated

The investigation examines these questions:

1. Is the current reply-based root projection sufficient as a first-MVP traversal tree?
2. Which source-native relationships must be retained even when they do not determine the tree parent?
3. What minimum summary allows a model to understand each post's conversational role?
4. Can `gpt-oss-20b` summarize long and code-heavy posts without reversing claims or removing important uncertainty?
5. Can a bounded model choose one broadly coherent path from a summarized tree?
6. Which deterministic filters should remove unsuitable paths before model selection?
7. Which judgments require LLM inference or human review?
8. Can generated post summaries also serve as learner-visible conversation text?
9. What authentic excerpt or attribution must remain available when summaries are shown?
10. What evidence is required to reproduce the proposed path from an unchanged source snapshot?

### Initial experiment

For topic `107565`:

1. build the current coarse tree from all seven posts;
2. generate one short summary for every post;
3. render the tree with summaries instead of full post bodies;
4. ask `gpt-oss-20b` to choose one coherent path for English phrase learning;
5. compare the proposed path with `#1 -> #2 -> #4 -> #7`;
6. review summary fidelity, conversational coherence, length, code burden, and phrase-learning potential.

The experiment should not define final JSON fields or publication contracts.

## Findings

### Current coarse tree

Topic `107565` contains seven visible posts.
The API exposes these explicit reply targets:

| post | API reply target | current projected parent |
|---|---:|---:|
| `#1` | none | none |
| `#2` | none | `#1` |
| `#3` | none | `#1` |
| `#4` | `#2` | `#2` |
| `#5` | `#4` | `#4` |
| `#6` | `#4` | `#4` |
| `#7` | `#4` | `#4` |

`fetch_post_tree.py` attaches a post to its explicit reply target when that target exists in the fetched set.
Otherwise, it attaches the post to the lowest-numbered fetched post, normally the opening post.

The resulting traversal tree is:

```text
#1
├─ #2
│  └─ #4
│     ├─ #5
│     ├─ #6
│     └─ #7
└─ #3
```

This projection is sufficient to expose the branch containing the current human-selected path.
It also exposes competing alternatives at posts `#3`, `#5`, and `#6`.

The projected edges `#1 -> #2` and `#1 -> #3` are not explicit Discourse reply edges.
They are traversal assumptions and must not overwrite the source-native `null` reply targets.

### Source relationships and projection

The source snapshot and derived tree have different responsibilities:

| information | purpose |
|---|---|
| API reply target | Preserve the explicit Discourse reply relationship. |
| Quote target or targets | Preserve additional source reference evidence when mechanically available. |
| Projected parent | Provide one coarse parent for traversal and path discovery. |
| Post number | Preserve source order and support deterministic tie-breaking. |

The first MVP does not need quote relationships to determine one exact parent.
They may be retained as supplemental signals for later summarization, path scoring, or review.

The current implementation still conflates two cases:

- no explicit reply target;
- an explicit reply target absent from the fetched set.

The pipeline should keep those cases distinguishable even when both are projected under the root.

### Multi-quote evidence

Packaging topic `107484`, `What would it look like to have a new archival format for distributions?`, contains a post that quotes both post `#12` and post `#10`.
The same post contains more than one quoted excerpt from post `#10`.

Packaging topic `106690`, `Pre PEP discussion: Workspace standardization in pyproject.toml`, contains a post that quotes two separate excerpts from the same earlier post.

These examples establish that complete source references form a graph rather than a strict tree.
They do not establish that the first-MVP learning-path search requires a complete graph.

A coarse reply tree can remain the traversal structure while quote references are retained separately when cheaply extractable.
Exact quote-span modeling can remain deferred unless later summarization or review evidence requires it.

### Current path selection

The golden fixture retains this manually selected source sequence:

```text
#1 -> #2 -> #4 -> #7
```

The tree builder does not select this path.
`capture_golden_source.py` only preserves post numbers supplied through `--posts`.
It verifies that the posts exist but does not verify path coherence or generate alternatives.

Path selection is therefore the missing semantic stage.
This judgment depends on conversational continuity, technical-reading burden, and phrase-learning potential.
Those concerns are suitable for a bounded LLM task followed by human review rather than deterministic reconstruction alone.

### First automated experiment

The first reproducible run used `gpt-oss:20b` through Ollama with topic `107565`.
The run generated summaries for all seven posts and selected this valid coarse-tree path:

```text
#1 -> #2 -> #4 -> #6
```

The reviewed reference path was:

```text
#1 -> #2 -> #4 -> #7
```

The mismatch is not by itself a failure.
Both paths follow valid edges and preserve a broadly coherent discussion.
The selected post `#6` provides a concrete technical clarification, while reference post `#7` provides a more reusable evaluation and adoption criterion.

The run demonstrates that a coarse tree plus short summaries is sufficient for proposing a plausible path without exact relationship reconstruction.
It does not yet demonstrate reliable phrase-learning ranking.

The run exposed these quality problems:

- post `#2` was labeled as seeking feedback, although it primarily challenges and evaluates the proposal;
- post `#7` was summarized as saying a few plugins are truly distinct, while the source says the named plugins are different flavors of the same thing;
- post `#4` was classified as low technical burden despite its long list of examples and links;
- the path response listed post `#4` as both selected and rejected;
- the automated evaluation used the same model and only reviewed selected posts, so it did not detect the inaccurate post `#7` summary.

The path selector received summaries and model-assigned phrase-learning scores but no exact phrase evidence.
It therefore preferred the concrete clarification in post `#6` without seeing the highly reusable wording in post `#7`, such as the general evaluation pattern used to state a standardization threshold.

These findings support adding exact or source-verified phrase candidates to path-selection input and strengthening deterministic consistency checks.

### Second automated experiment

The second run added exact phrase candidates and rejected selected/rejected overlap.
It selected this valid path:

```text
#1 -> #2 -> #4 -> #5
```

The consistency checks passed, and the selected/rejected contradiction from the first run was removed.
The revised summary for post `#2` also correctly described the post as evaluating and challenging the proposal.

The second run exposed a more important source-boundary problem.
Post `#7` contains a quoted excerpt from post `#4` followed by the author's own response.
The summarization input passed the complete raw post, including the quote block.
The model consequently attributed quoted post `#4` language to post `#7` and extracted two phrase candidates from the quoted material rather than from the author of post `#7`.

Exact substring matching against the full raw post did not detect this error because quoted text is physically present in that raw post.
For phrase attribution, source-exact is insufficient unless the pipeline also distinguishes authored text from quoted text.

The second run also showed that asking for all-post evaluation does not guarantee complete coverage.
The automated evaluation returned reviews for only five of seven posts while still claiming that all summaries passed.
Coverage therefore requires deterministic validation of reviewed post identifiers.

The second run demonstrates:

- phrase evidence can influence path selection;
- selected/rejected consistency can be enforced mechanically;
- quote removal or authored-text separation is required before summarization and phrase extraction;
- automated-review coverage must be validated mechanically;
- model-generated phrase candidates still require quality review even when attribution is exact.

### Third automated experiment

The third run removed quoted blocks before summarization and phrase extraction.
It validated phrase candidates against authored text, retried invalid exact-copy results, and required one automated review for every post.

Two post summaries required a second attempt:

- post `#2` initially removed Markdown emphasis from `I don't *know* if that's the case`;
- post `#4` initially changed the source wording `one way of the other` to the more conventional `one way or the other`.

The retry mechanism regenerated exact authored-text candidates and preserved every attempt as evidence.

The v3 run passed:

- phrase attribution against quote-free authored text;
- coarse-tree path validation;
- selected/rejected alternative consistency;
- complete automated-review coverage for posts `#1` through `#7`.

The model again selected:

```text
#1 -> #2 -> #4 -> #5
```

Human review accepted this as a coherent candidate but not as the preferred phrase-learning path.
Post `#5` mainly contributes technical and historical explanation.
Its strongest general phrase is `I'm pretty certain`, while its other candidates are fragments or tool-specific descriptions.

Post `#7` provides the more reusable evaluation pattern:

```text
I want to see more than one tool implementing something with significant adoption before trying to standardize it.
```

The reviewed golden path therefore remains:

```text
#1 -> #2 -> #4 -> #7
```

The v3 summaries are lightweight enough for learner-facing context, but human review still found minor compression risks.
For example, post `#2` says pip has no need for `build_sdist`, while the generated summary can be read as saying pip lacks it.
Post `#4` presents continued use of older build systems as a possibility, not an established fact.

The experiment therefore supports model-proposed paths and generated summaries, but not unreviewed final selection or publication.

### Direction correction

Exact reconstruction of all conversational dependencies is not required for the learning objective.
The first MVP needs a bounded set of paths that are individually understandable enough to support phrase learning.

The working approach is therefore:

```text
source snapshot
  -> authored text plus preserved source relationships
  -> coarse reply tree
  -> short post summaries and exact phrase candidates
  -> mechanically connected path enumeration
  -> deterministic validation
  -> independent absolute filtering
  -> multiple valid paths with learning focus and phrase evidence
  -> session-time path selection
  -> per-post quiz generation
```

Full source text remains available for validation and attribution.
The model may use summaries for path filtering and labeling, and the application may later use reviewed summaries or short excerpts to avoid overwhelming the learner with code and long technical explanations.

## Cross-cutting observations

### Source fidelity does not require full-text display

Source fidelity requires preservation of the original post, accurate attribution, and protection against generated summaries being presented as quotations.
It does not require every learner session to display the complete source post.

A reviewed generated summary can compress technical detail while exact reusable phrases remain linked to authentic source text.

### Tree quality and learning quality are separate

A traversal tree only needs to expose plausible paths.
The best learning path cannot be determined solely from reply metadata because phrase usefulness and reading burden are semantic concerns.

### Model tasks should remain bounded

Post summarization and path selection should be separate tasks.
A path-selection task should receive post identifiers, tree structure, short summaries, and source-verified phrase evidence rather than complete topic bodies.

### Human review remains necessary

A coherent technical summary can still be unsuitable for phrase learning.
Human review remains necessary for establishing and extending golden fixtures, checking learner-visible summaries, and evaluating borderline filtering behavior.

A single model-selected path should not be treated as ground truth.
The experiments showed that post `#5` and post `#7` support different legitimate learning objectives rather than one objectively correct branch.
The useful pipeline output is therefore a validated set of independently usable paths, not one canonical winner.

## Conclusions

- The first MVP does not require exact reconstruction of every conversational dependency.
- The current reply-based root projection is sufficient as a coarse traversal tree when source-native reply targets and projection reasons remain separate.
- Quote targets should be preserved as supplemental relationships, but quote blocks must be excluded from authored-text summarization and phrase attribution.
- `gpt-oss:20b` can produce usable lightweight post summaries and source-grounded phrase candidates from the coarse tree.
- Exact phrase candidates require deterministic authored-text matching and retry on validation failure.
- One topic may yield multiple valid learning paths; no single path should be treated as the canonical answer merely because it was selected by a reviewer or ranked first by a model.
- Candidate paths should be judged independently through absolute filtering rather than rejected for being shorter, longer, or less preferred than another valid path.
- On topic `107565`, GPT-OSS and Qwen both accepted all six real paths and rejected all three invalid controls, so GPT-OSS is sufficient as the provisional first-pass binary filter for this golden fixture.
- Every retained path must carry at least one learning focus and at least one source-verified phrase as evidence; prefix-overlapping paths may coexist.
- Session-time selection, not ingestion-time canonicalization, should choose which valid path becomes a quiz session.
- Human review remains responsible for golden-fixture quality, borderline policy evaluation, and learner-visible summary acceptance rather than routine selection of one final path.
- Reviewed generated summaries are a viable way to reduce technical-reading burden while retaining raw posts for provenance and validation.

## Recommendation

Adopt the following first-MVP boundary:

1. preserve immutable raw posts, explicit reply targets, quote targets, and post order;
2. derive one coarse parent and projection reason per post;
3. remove quote blocks to create attributed authored text;
4. generate short summaries and exact phrase candidates through bounded model calls;
5. enumerate bounded mechanically connected path candidates, initially using root-starting paths of two to six posts;
6. validate structure, authored-text phrase fidelity, path connectivity, identity, and coverage mechanically;
7. filter each candidate independently for quiz validity and attach learning focus plus source-verified phrase evidence;
8. retain zero or more valid paths per topic, including prefix-overlapping variants;
9. select one retained path at session time according to learning state, desired length, reading burden, and repetition policy;
10. generate per-post quiz interactions from the selected path while preserving provenance to its source posts and pipeline version.

Do not implement exhaustive graph reconstruction or ingestion-time canonical path selection for the first MVP.
Treat `#1 -> #2 -> #4 -> #7` as one reviewed valid path for topic `107565`, alongside other valid variants such as `#1 -> #2 -> #4 -> #5`.
Use GPT-OSS as the provisional first-pass binary filter for the current golden fixture, but do not treat the current easy controls as proof of unattended production-grade accuracy.

The decision to make generated summaries the normal learner-visible conversation representation should be recorded separately as a learning-domain ADR.

## Follow-up artifact candidates

- A pipeline requirement for reproducible coarse-tree construction, authored-text derivation, summary generation, bounded path enumeration, and absolute filtering.
- A child specification under `spec:product.pipeline` for relationship preservation, projection reasons, deterministic validation, filter inputs, and retained-path outputs.
- A learning-domain contract for one topic to own zero or more valid paths, each containing ordered posts, learning focus, source-verified phrase evidence, burden metadata, and provenance.
- App design for session-time path selection and per-post quiz generation from the retained valid-path set.
- A learning ADR for reviewed generated summaries as the normal lightweight conversation representation.
- Harder evaluation fixtures for borderline phrase value, misleading summaries, heavy but valid technical context, and path-specific learning-focus extraction.

## Independent Qwen ranking follow-up

The first blind Qwen run ranked all six root-starting path prefixes from the fixed GPT-OSS v3 summaries.
It passed deterministic ranking validation and selected:

```text
#1 -> #2 -> #4
```

The reviewed `#1 -> #2 -> #4 -> #7` path ranked fifth, while the GPT-OSS `#1 -> #2 -> #4 -> #5` path ranked fourth.

This result does not establish that Qwen is a worse branch judge.
The candidate set mixed path-length selection with branch selection, and the rubric explicitly rewarded cognitive lightness.
Qwen consistently preferred shorter paths before comparing the final sibling replies.

The controlled run held the common prefix and path length constant, ranking only:

```text
#1 -> #2 -> #4 -> #5
#1 -> #2 -> #4 -> #6
#1 -> #2 -> #4 -> #7
```

Qwen ranked:

1. `#1 -> #2 -> #4 -> #5`;
2. `#1 -> #2 -> #4 -> #7`;
3. `#1 -> #2 -> #4 -> #6`.

The run passed deterministic validation on its first attempt with high reasoning effort.
Qwen therefore agreed with the GPT-OSS branch choice even after path length and common prefix were controlled.

This result weakens the hypothesis that a different local judge model will recover the reviewed `#7` preference automatically.
Both models viewed post `#5` as providing more short and transferable phrases, especially certainty and historical-reasoning language.
The reviewed preference for post `#7` instead values one longer, broadly useful evaluation criterion.

The disagreement is therefore primarily a learning-objective ambiguity rather than a tree-reconstruction or model-capability failure.
The pipeline should not encode either branch as the uniquely correct answer without a more explicit session objective.
It may preserve both as valid variants:

- post `#5` for certainty and historical explanation;
- post `#7` for evaluation thresholds and standardization criteria.

### Absolute filtering comparison

The ranking experiments do not establish whether GPT-OSS or Qwen can safely retain every usable path while rejecting only genuinely unsuitable paths.
A separate comparison is implemented by `scripts/run_path_filtering_comparison_experiment.py`.

The experiment judges each path independently and does not expose alternative candidates or expected labels to the model.
It includes all six real paths from topic `107565` as positive cases and three negative controls:

- a disconnected path;
- a path with no supplied source-verified phrase evidence;
- a path whose supplied phrase evidence contains technical terms only.

GPT-OSS and Qwen receive the same prompt, schema, case input, and deterministic output validation.
The strict provisional acceptance target for either model is:

```text
valid-path recall = 1.0
invalid-control rejection rate = 1.0
```

The first comparison run met this target for both models.
GPT-OSS and Qwen each accepted all six real paths and rejected all three controls on their first attempt, with complete agreement across all nine cases.

For binary absolute filtering on topic `107565`, GPT-OSS therefore performed equivalently to Qwen in this fixture.
Switching to Qwen is not justified by filtering accuracy alone.

The models differed in secondary labeling quality.
Qwen more consistently identified the distinctive learning focus and exact phrase from the final branch post.
GPT-OSS sometimes accepted a branch using only phrases and learning functions already present in the common prefix.
This does not harm binary filtering, but it matters if the same call is also expected to label path-specific learning focus.

The controls remain easy and partly deterministic.
The result supports GPT-OSS as the provisional first-pass filter for this golden topic, not as an unattended general production gate.
Harder fixtures must test borderline reusable phrases, misleading summaries, heavy but still valid technical context, and path-specific learning-focus extraction.

## Remaining non-blocking questions

- What summary-length range best balances conversational fidelity and light reading?
- Should conversational intent and learning focus use controlled vocabularies or remain generated text?
- How should session-time selection balance desired length, unseen learning focus, phrase repetition, and reading burden?
- When should prefix-overlapping valid paths remain separate variants, and when should the application suppress near-duplicates?
- Which reviewed summary, short source excerpt, and exact source phrase should appear together in the application?
- How should prompt, model, source snapshot, and pipeline versions participate in published learning-unit provenance?
- What harder fixtures are sufficient before absolute filtering can become an unattended production gate?
