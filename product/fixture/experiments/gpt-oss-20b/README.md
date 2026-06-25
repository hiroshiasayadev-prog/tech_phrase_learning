# gpt-oss-20b experiment evidence

This directory preserves prompt contracts and observations from the first lightweight-model experiments.

## Evidence status

The original request payloads were not saved at execution time.
The prompt files are reconstructed from session notes, recorded outputs, and the constraints added between runs.

They must not be treated as byte-for-byte copies of the original prompts.
Future experiments should store the exact request payload before invocation.

Run repository prompts from their local files rather than copying them from rendered chat messages.
Rendered-chat copying may remove Markdown characters such as backticks from inline code spans.
Verify the stored request payload before attributing a source-fidelity mismatch to the model.

## Model context

| field | value |
|---|---|
| Model | `gpt-oss-20b` |
| API shape | OpenAI-compatible endpoint |
| Primary reasoning level | `medium` |
| Comparison reasoning level | `high` |
| Human review | Required |

Provider, endpoint URL, temperature, seed, and other request parameters were not recorded.
They remain unknown for these historical runs.

## Experiments

| directory | purpose |
|---|---|
| `question-candidate-filter` | Select opening posts containing reusable technical-question phrasing. |
| `question-quiz-generation` | Generate phrase-exposure interactions from reviewed opening posts. Topic-specific golden-run prompts may coexist with generic experiment prompts. |
| `conversation-path-selection` | Build a coarse tree, summarize posts, select one learning path, and create an automated evaluation through Ollama. |

## Preservation rule for later runs

Save these artifacts together for every model invocation:

1. exact system and user messages;
2. exact reduced input payload;
3. model and reasoning level;
4. all sampling and output parameters;
5. raw model response;
6. deterministic validation result;
7. human review result;
8. prompt and pipeline version identifiers.

These files are investigation fixtures.
They do not define the normative runtime package schema.
