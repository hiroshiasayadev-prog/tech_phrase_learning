# Qwen path-ranking experiment

This experiment tests Qwen as an independent judge over fixed upstream outputs from the `gpt-oss:20b` conversation-path experiment.

Qwen does not summarize posts, extract phrases, construct the tree, or invent paths in this experiment.
The script mechanically enumerates valid paths, then asks Qwen to rank every candidate for lightweight English phrase learning.

## Fixed upstream evidence

Default source run:

```text
product/fixture/experiments/gpt-oss-20b/
  conversation-path-selection/runs/topic-107565-v3
```

The judge receives:

- the mechanically enumerated candidate paths;
- the fixed v3 post summaries;
- source-validated phrase candidates;
- conversational intent and burden labels.

The judge does not receive:

- the reviewed reference path;
- the path selected by `gpt-oss:20b`;
- human verdict notes.

Those values are compared only after Qwen returns its ranking.

## Candidate enumeration

The script enumerates every root-starting parent-to-child path between 2 and 6 posts, including non-leaf prefixes.

For topic `107565`, the expected candidates are:

```text
#1 -> #2
#1 -> #2 -> #4
#1 -> #2 -> #4 -> #5
#1 -> #2 -> #4 -> #6
#1 -> #2 -> #4 -> #7
#1 -> #3
```

## Run

From the repository root:

```powershell
python -X utf8 scripts/run_qwen_path_ranking_experiment.py
```

Default configuration:

- Ollama base URL: `http://192.168.11.22:11434`
- Judge model: `qwen3.6-27b:q4_k_m-tools`
- Initial thinking depth: `high`
- Maximum combined reasoning and answer tokens: `8192`
- Request timeout: `900` seconds
- Temperature: `0`
- Output: `.tmp/qwen-path-ranking/topic-107565-v1`

To overwrite an existing output:

```powershell
python -X utf8 scripts/run_qwen_path_ranking_experiment.py --force
```

To prepare and inspect the candidate set without calling Ollama:

```powershell
python -X utf8 scripts/run_qwen_path_ranking_experiment.py `
  --prepare-only `
  --force
```

## Controlled sibling comparison

The first all-prefix run mixed two decisions:

- which branch continuation is best;
- whether another post should be added at all.

Qwen ranked the shorter `#1 -> #2 -> #4` path first, so that run did not isolate the `#5` versus `#6` versus `#7` branch judgment.

Use a fixed prefix and post count for the controlled comparison:

```powershell
python -X utf8 scripts/run_qwen_path_ranking_experiment.py `
  --required-prefix 1 2 4 `
  --required-post-count 4 `
  --output-dir .tmp/qwen-path-ranking/topic-107565-v2-siblings `
  --force
```

This produces exactly three candidates:

```text
#1 -> #2 -> #4 -> #5
#1 -> #2 -> #4 -> #6
#1 -> #2 -> #4 -> #7
```

The preserved controlled run is stored at `runs/topic-107565-v2-siblings`.
It ranked `#5` first, `#7` second, and `#6` third.
This matched the GPT-OSS branch choice rather than the reviewed reference path.

## Validation

The script checks that Qwen:

- returns every candidate exactly once;
- uses no unknown candidate IDs;
- assigns unique consecutive ranks;
- makes `top_candidate_id` equal the rank-1 candidate;
- returns score values within the schema.

Invalid rankings receive two automatic retries by default.
The initial attempt uses `high` reasoning. After a timeout or unusable structured output, later attempts reduce reasoning to `medium` and then `low`.
Each request, response, parsed result, timeout, and validation result is preserved.

The script explicitly sends Ollama `num_predict=8192`. This prevents the model's 262144-token default output allowance from permitting an unbounded reasoning run.

## Comparison

After blind ranking, the script reports:

- Qwen's top-ranked path;
- the rank of the reviewed reference path `#1 -> #2 -> #4 -> #7`;
- the rank of the GPT-OSS path `#1 -> #2 -> #4 -> #5`;
- criterion scores and a deterministic weighted score for inspection.

The Qwen ranking remains a review aid rather than final acceptance authority.

## First-run result

The preserved all-prefix run is stored at:

```text
runs/topic-107565-v1-all-prefixes
```

It passed structural validation and ranked:

1. `#1 -> #2 -> #4`
2. `#1 -> #2`
3. `#1 -> #3`
4. `#1 -> #2 -> #4 -> #5`
5. `#1 -> #2 -> #4 -> #7`
6. `#1 -> #2 -> #4 -> #6`

This shows that the judge strongly rewarded shorter paths. It does not establish that Qwen prefers post `#5` over post `#7` when path length and common prefix are controlled.

The controlled sibling run removed that ambiguity and still ranked post `#5` above post `#7`.
Qwen described post `#5` as offering short, transferable certainty and historical-reasoning phrases, while treating post `#7` as more verbose and tied to software-standardization context.

Because GPT-OSS and Qwen independently favored the same branch, switching judge models alone does not reproduce the reviewed `#7` preference. Either the ranking rubric needs a more explicit target for reusable evaluation criteria, or `#5` and `#7` should be treated as different valid learning-path variants rather than one objectively correct choice.

The plain `qwen3.6-27b:q4_k_m` tag is not allowlisted in the current Ollama MCP setup and rejected the `think` option during the failed first attempt. The `qwen3.6-27b:q4_k_m-tools` tag is the active allowlisted model and accepts high reasoning effort.
