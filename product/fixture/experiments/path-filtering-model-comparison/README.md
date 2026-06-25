# Quiz-path filtering model comparison

This experiment compares `gpt-oss:20b` and `qwen3.6-27b:q4_k_m-tools` as absolute quiz-path filters.

It does not ask either model to choose one best path.
Each path is judged independently, without seeing any alternative candidate or expected label.

## Question

Can each model:

- retain every real path that has usable conversational phrase value;
- reject clearly invalid controls;
- attach a useful learning focus and exact supplied phrase evidence to accepted paths?

## Cases

The fixture contains six real paths from topic `107565`.
All six are expected to remain valid:

```text
T001  #1 -> #2
T002  #1 -> #2 -> #4
T003  #1 -> #2 -> #4 -> #5
T004  #1 -> #2 -> #4 -> #6
T005  #1 -> #2 -> #4 -> #7
T006  #1 -> #3
```

It also contains three negative controls:

```text
T007  disconnected structure: #1 -> #5
T008  valid structure but no supplied phrase candidates
T009  valid structure but supplied phrase evidence is technical terms only
```

Expected labels and control classes are never sent to the models.

## Filtering contract

A path is accepted only when:

- the supplied structure is mechanically valid;
- the summarized conversation is understandable;
- at least one supplied source-verified phrase is reusable conversational wording;
- technical detail does not overwhelm the phrase-learning value;
- the path contains two to six posts.

A path must not be rejected merely because another path could be shorter, richer, or more interesting.

## Script

From the repository root:

```powershell
python -X utf8 scripts/run_path_filtering_comparison_experiment.py `
  --force
```

Default models and reasoning:

```text
gpt-oss:20b                    medium
qwen3.6-27b:q4_k_m-tools      high
```

Default output:

```text
.tmp/path-filtering-comparison/topic-107565-v1
```

Prepare all case inputs without calling Ollama:

```powershell
python -X utf8 scripts/run_path_filtering_comparison_experiment.py `
  --prepare-only `
  --force
```

Run only one model:

```powershell
python -X utf8 scripts/run_path_filtering_comparison_experiment.py `
  --models gpt `
  --force
```

```powershell
python -X utf8 scripts/run_path_filtering_comparison_experiment.py `
  --models qwen `
  --force
```

## Validation

Each response is checked mechanically:

- returned `case_id` matches the input;
- `valid_for_quiz` agrees with `decision`;
- an accepted path has at least one learning focus;
- an accepted path cites at least one supplied phrase candidate;
- cited phrase evidence was actually present in the case input;
- an accepted path has no exclusion reasons;
- a rejected path has at least one controlled exclusion reason.

Invalid structured output receives two retries by default.
Reasoning effort is reduced on later attempts.

## Metrics

For each model, the report includes:

- overall accuracy;
- valid-path recall;
- invalid-control rejection rate;
- false rejections;
- false acceptances;
- whether the strict acceptance target was met.

The strict target is:

```text
valid-path recall = 1.0
invalid-control rejection rate = 1.0
```

When both models run, the report also includes inter-model agreement and disagreement case IDs.

## Preserved result

The first comparison run is stored at `runs/topic-107565-v1`.

Both models met the strict provisional target:

| model | valid-path recall | invalid-control rejection | agreement |
|---|---:|---:|---:|
| `gpt-oss:20b` | 1.0 | 1.0 | 1.0 |
| `qwen3.6-27b:q4_k_m-tools` | 1.0 | 1.0 | 1.0 |

Both models accepted all six real paths and rejected all three controls on their first attempt.
GPT-OSS used medium reasoning and Qwen used high reasoning.

The binary filtering decisions were equivalent on this fixture.
The generated labels were not fully equivalent: Qwen more consistently identified the final branch post's distinctive learning focus and phrase evidence, while GPT-OSS sometimes accepted a path using only reusable phrases from its shared prefix.
For example, GPT-OSS accepted the post `#7` path without naming its adoption-threshold phrase as the learning focus, whereas Qwen explicitly labeled it as stating conditions for action.

## Interpretation

Passing this fixture supports using GPT-OSS or Qwen as a first-pass absolute filter for topic `107565`.
It does not prove general filtering quality across unrelated discussions.

The current negative controls are intentionally clear:

- structural invalidity is already supplied as deterministic metadata;
- an empty phrase list is mechanically detectable;
- technical-only phrase evidence is the main semantic rejection test.

The result therefore establishes basic policy adherence and absence of false rejection on the current golden topic, not production-grade filtering accuracy.
Additional golden topics, borderline phrase-value cases, misleading summaries, and high-burden but still valid paths are required before making the filter an unattended production gate.
