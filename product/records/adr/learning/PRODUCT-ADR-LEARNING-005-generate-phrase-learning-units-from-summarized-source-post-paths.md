# PRODUCT-ADR-LEARNING-005: Generate phrase-learning units from summarized source-post paths

- **status**: accepted
- **date**: 2026-06-25
- **depends_on**: [PRODUCT-ADR-LEARNING-001]
- **supersedes**: [PRODUCT-ADR-LEARNING-004]
- **migrated_to_spec**: 2026-06-25

## Context

One technical discussion may contain several source-post sequences that support different phrase-learning value.
The pipeline investigation concluded that the product must retain multiple valid sequences instead of selecting one canonical sequence during ingestion.

One source-post sequence may also support more than one learning unit.
Different quizzes may focus on different phrases or conversational functions within the same source conversation.

Raw source posts may contain code, links, and long technical explanations.
The product must preserve source evidence without turning the learner session into technical-reading practice.

The first MVP also cannot require human review for every generated learning unit.
Humans cannot review the expected content volume.
Human responsibility should remain at the approval-policy level.

## Decision

The learning domain will define the principles for source-post sequences that are suitable for phrase learning.
The pipeline will implement candidate generation, validation, and exclusion logic that satisfies those principles.

A source-post path is an ordered sequence of connected source posts from one technical discussion.
One discussion may retain zero or more valid source-post paths.
The pipeline will not select one canonical path during ingestion.

One valid source-post path may produce zero or more learning units.
A learning unit will reference its source-post path instead of copying the source posts or conversation tree.
The source posts and conversation tree will remain separately managed source artifacts.

The application will select one available learning unit when a learner session starts.
The application will not select a raw source-post path and generate unapproved quiz content during the session.

Every first-MVP learning unit will contain:

- one question-formulation interaction for the opening post;
- at least one reply-formulation interaction;
- one coherent source-post path;
- progressive presentation in source order;
- source attribution.

Generated quiz content will remain distinct from source-derived summaries and source evidence.

Each selected source post in a learning unit will have:

- one learner-visible English summary;
- one English quiz prompt;
- one target quiz phrase;
- one quiz with three English answer options.

The first MVP will create one quiz for every selected source post.
The first MVP will use one target quiz phrase per quiz.
Context-only selected posts and multi-phrase quizzes remain deferred.

### Summary model

The pipeline will first create one reusable summary for each source post.
The reusable summary will preserve the technical meaning needed to understand the post.

When a source-post path becomes a learning-unit candidate, the pipeline may revise the summaries for that path.
Path-specific revision will preserve conversational continuity across adjacent turns.
A learning unit may therefore reference the reusable post summary or contain a path-specific revised summary.

The default learner-visible source representation will be the summary.
Raw source-post display is not required for the first MVP.

### Phrase and quiz model

The target quiz phrase will be generated from:

- the preceding path context, including the previous turn summary when present;
- the current source post as evidence for the conversational move and wording.

The target quiz phrase will minimize source-specific technical detail.
The phrase may replace technical nouns with pronouns or general nouns.
The phrase must preserve enough situation detail to show how the expression is used.

The target quiz phrase does not need to reproduce one complete source sentence.
The current source post must still provide evidence for the expression and its conversational function.

Quiz generation will occur after target-phrase selection.
Phrase selection and quiz generation will use separate model tasks.

The correct option will use the target quiz phrase in a response that fits the prompt.
Incorrect options will remain grammatical and natural English.
Incorrect options will be clearly unsuitable for the stated conversational intent.

### Initial generation flow

```text
source posts and preserved relationships
  -> reusable post summaries and source-grounded phrase evidence
  -> valid source-post path generation and filtering
  -> path-specific conversational summary revision
  -> one target quiz phrase per selected post
  -> one three-option quiz per selected post
  -> automated publication gate
  -> available learning unit
```

The exact prompts, model roles, schemas, retry rules, and validation thresholds belong to pipeline specifications.

### Publication boundary

The first MVP will not require human review for every learning unit.
Humans will approve the publication criteria and material changes to those criteria.
Larger models may help draft and evaluate the criteria before human approval.

Generated learning units will pass an automated publication gate before becoming available to sessions.
For the first MVP, this gate may combine mechanical validation and model-based quality judgment behind one publication decision.

Independent model sampling audits remain a later addition.
When audits are added, a failed audit will initially affect only the audited learning unit.
The data model must allow an available unit to become unavailable without deleting its source artifacts.

This ADR supersedes PRODUCT-ADR-LEARNING-004.
It retains mixed question-and-reply sessions, progressive order, source grounding, attribution, and generated/source separation.
It replaces raw source-turn reveal with validated summaries as the default learner-visible representation.
It also replaces per-learning-unit human review with policy-level human approval and automated publication gating.

## Rationale

Retaining several valid paths preserves different legitimate learning opportunities within one discussion.
Selecting one canonical path during ingestion would discard useful alternatives before learner needs are known.

Separating source posts, conversation trees, paths, and learning units avoids source duplication.
The separation also allows one path to support several quiz variants.

Reusable summaries reduce repeated work.
Path-specific revision fixes pronouns, omitted context, and other continuity problems that only appear inside one selected sequence.

One quiz and one target phrase per selected post keep the first pipeline contract simple.
The constraint also reduces pressure on small models to invent low-value phrases to satisfy a requested count.

Separate phrase-selection and quiz-generation tasks keep each model call bounded.
The separation also allows source grounding to be checked before distractors are generated.

Policy-level human approval can scale better than item-level human review.
An automated publication gate preserves a clear release boundary without requiring humans to inspect every unit.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Retain one canonical source-post path per discussion | One discussion may contain several independently useful phrase-learning sequences. |
| Treat a source-post path as the learning unit | One path may support several quiz sets and target phrases. |
| Copy source posts into every path and unit | Duplication would weaken provenance and complicate source updates. |
| Generate every summary only for one path | Repeated generation would waste work shared across path candidates. |
| Use only one reusable summary in every path | A locally accurate summary may still produce unnatural conversation continuity. |
| Extract several phrases from every post | Small models may fill the requested count with weak or irrelevant phrases. |
| Select phrases and generate quizzes in one model call | The combined task would increase output complexity and reduce grounding quality. |
| Show raw source posts by default | Code and long technical detail would distract from phrase learning. |
| Require human approval for every learning unit | Item-level review would not scale to the intended content volume. |
| Implement independent sampling audits in the initial pipeline | The audit workflow is useful but not required to validate the first end-to-end product flow. |

## Consequences

- Learning specifications must define valid source-post path principles independently from pipeline implementation.
- Pipeline specifications must define path generation, filtering, summary stages, phrase selection, quiz generation, and publication gating.
- The source-post path, conversation tree, source posts, and learning unit require separate identities and references.
- One source-post path may be referenced by several learning units.
- Each selected source post requires one summary, one quiz, and one target phrase in the first MVP.
- Learner-facing content generated by this flow must be English.
- The application session selector will query available learning units rather than raw paths.
- Publication availability must be reversible without deleting source evidence.
- PRODUCT-ADR-LEARNING-004 is superseded by this ADR.
- Prefix-path deduplication, context-only posts, multi-phrase quizzes, learner-history selection, and independent audits remain deferred.

## Evidence

- PRODUCT-INV-PIPELINE-002 concluded that one topic may yield multiple independently valid paths.
- The filtering comparison retained valid prefix-overlapping paths without ranking them against each other.
- Earlier experiments found that raw posts can contain code and technical detail that overwhelm phrase-learning context.
- Earlier experiments also found that summaries can become misleading when quote text and authored text are not separated.
- The agreed product flow uses technical summaries for revealed source turns and abstracted English phrases for quiz choices.
- The user cannot review every generated learning unit and requires human approval to operate at the policy level.
