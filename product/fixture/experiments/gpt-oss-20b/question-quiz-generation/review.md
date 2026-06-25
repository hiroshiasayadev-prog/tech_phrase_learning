# Question quiz generation review

## Scope

This review summarizes the first `gpt-oss-20b` question-formulation experiments.

The original request payloads were not preserved.
The output files for topic `107844` were copied from recorded model responses.
The prompt versions were reconstructed from the constraints added between runs.

## Topic 107763 observations

The first possibility-question experiments showed these failure classes:

- all options expressed nearly the same intent;
- the preferred choice became arbitrary;
- the source phrase selected only technical wording;
- a source phrase was generated rather than copied exactly;
- distractors introduced unsupported details such as dictionaries or `**kwargs`;
- some distractor wording was linguistically unnatural.

Prompt revisions improved:

- option contrast;
- exact source-span fidelity;
- selection of question-formulation wording;
- JSON structure stability.

The later product judgment relaxed the same-intent constraint.
Natural exposure to varied phrases is more important than strict quiz purity.

## Topic 107844 medium reasoning

Strengths:

- all three options expose distinct reusable question patterns;
- the preferred option asks for current best practice clearly;
- the authentic phrase is exact and conversational;
- technical alternatives come from the source situation rather than invented mechanisms.

Weaknesses:

- `How do we manage nested contexts in Python?` is slightly unnatural;
- the source phrase function label `question` is too broad.

Assessment:

- suitable as reviewed experiment evidence;
- sufficient draft quality for normal generation.

## Topic 107844 high reasoning

Strengths:

- clear contrast among asking for a newer pattern, vague improvement, and comparing known choices;
- strong authentic phrase: `What do you all use in production?`;
- all options are linguistically plausible.

Weaknesses:

- the preferred option narrows the broader source intent to alternatives beyond `ExitStack`;
- no consistent quality improvement over medium reasoning;
- observed latency was about three minutes.

Assessment:

- valid under the phrase-exposure learning model;
- not a better cost-latency trade-off for routine generation.

## Reasoning-level judgment

Use `medium` reasoning for normal candidate and draft generation.

Use `high` reasoning only for targeted comparison or difficult regeneration when evidence justifies the latency.
Human review remains mandatory at either level.

## Current acceptance criteria

A generated interaction is reviewable when:

- every option sounds natural;
- every option provides reusable conversational phrasing;
- options remain plausible in the broad technical situation;
- exactly one option best fits the generated context;
- generated text does not claim source authorship;
- no unsupported technical facts are introduced;
- the authentic phrase occurs verbatim in the source turn;
- the authentic span contains conversational wording rather than only technical vocabulary.

## Topic 107565 golden-run prompt observations

The first golden-run prompt was refined to preserve the proposal-feedback social situation and emit one complete JSON object.

A copied transcript appeared to omit the backticks around `targets` in the required source phrase.
The omission occurred when the prompt was copied from a rendered ChatGPT message before invocation.
It was not evidence that `gpt-oss-20b` failed an exact-copy instruction.

Operational judgment:

- run prompts from repository files;
- store the exact request payload before invocation;
- verify transport fidelity before judging model source fidelity;
- preserve raw model responses without manual repair;
- use deterministic checks and human review after generation.

The topic-specific prompt is:

`prompt-v5-topic-107565-golden-run.md`

The observed medium-reasoning latency for an early topic `107565` run was approximately 37 seconds.

## Candidate-filter experiment summary

Across the recorded opening-post batches:

- ten candidates were selected;
- five were assessed as strong;
- two were useful;
- two were weak;
- one was a false positive.

The false positive selected technical text rather than a question phrase.
This supports deterministic exact-span checks plus human semantic review.
