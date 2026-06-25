# Coarse tree, summary, and learning-path experiment

This experiment tests whether one Discourse topic can be reduced into a lightweight learning path without reconstructing every conversational dependency.

## Flow

1. Load one immutable Discourse topic snapshot.
2. Preserve explicit reply and quote references.
3. Build one coarse rooted traversal tree.
4. Ask `gpt-oss-20b` to summarize each post separately.
5. Ask `gpt-oss-20b` to select one path from the summarized tree.
6. Compare the proposal with a reviewed reference path.
7. Run an automated source-fidelity and learning-burden evaluation.
8. Leave the final verdict to human review.

The generated summaries are candidate learner-facing text. They are not authentic quotations.
The raw source posts remain authoritative for provenance.
Quoted blocks are removed mechanically before summarization and phrase extraction so phrase attribution applies to the current author's own text.

## Script

From the repository root:

```powershell
python -X utf8 scripts/run_path_selection_experiment.py `
  --output-dir .tmp/conversation-path-selection/topic-107565-v3
```

Default configuration:

- Ollama base URL: `http://192.168.11.22:11434`
- Model: `gpt-oss:20b`
- Source: `product/fixture/golden/topic-107565/source-topic.raw.json`
- Reference path: `1 2 4 7`
- Temporary output: `.tmp/conversation-path-selection/topic-107565`

Override values through CLI options or environment variables:

```powershell
$env:OLLAMA_BASE_URL = 'http://192.168.11.22:11434'
$env:OLLAMA_MODEL = 'gpt-oss:20b'

python -X utf8 scripts/run_path_selection_experiment.py `
  --model gpt-oss:20b `
  --expected-path 1 2 4 7 `
  --force
```

Use `--prepare-only` to generate the coarse tree and exact request payload previews without calling Ollama.

Post-summary outputs receive two automatic retries by default when deterministic validation fails. Each attempt preserves its request, response, parsed output, and validation result. Override this with `--summary-retries`.

After an interrupted or failed run, rerun the same output directory with `--force`. The script removes the incomplete directory before starting again.

## Experiment versions

| version | purpose | preserved prompt files |
|---|---|---|
| v1 | Summary-only path selection. | `*-v1.md` and unversioned original schemas. |
| v2 | Added exact phrase candidates and selected/rejected consistency checks. | `*-v2-*.md` and `post-summary-v2.schema.json`. |
| v3 | Removes quoted blocks before attribution and validates complete automated-review coverage. | `*-v3-*.md` and `*-v3.schema.json`. |

The script currently runs v3.
Preserved evidence runs are stored under `runs/topic-107565-v1`, `runs/topic-107565-v2`, and `runs/topic-107565-v3`.

## Preserved artifacts

The script writes:

- source identity and run configuration;
- coarse tree and projection reasons;
- exact request and raw response for every model call;
- validated post summaries;
- summarized tree in JSON and Markdown;
- proposed path and deterministic validation;
- comparison with the reference path;
- automated evaluation and deterministic review-coverage validation;
- one human-readable report.

These artifacts are investigation evidence. They do not define the final runtime schema.

## Human verdict for topic 107565

The v3 run passed deterministic source-attribution, path-consistency, and automated-review coverage checks.
Its proposed path `#1 -> #2 -> #4 -> #5` is coherent but was not accepted as the preferred learning path.

The reviewed path remains `#1 -> #2 -> #4 -> #7` because post `#7` provides a stronger reusable evaluation pattern about requiring multiple adopted implementations before standardization.
Post `#5` is technically relevant, but most of its extracted wording is historical or tool-specific rather than broadly reusable conversation language.

The model-proposed path is therefore treated as a candidate, not a final selection.
