# Human review: topic 107565 golden question-and-reply fixture

## Verdict

Accepted as the first reviewed question-and-reply fixture for `PRODUCT-INV-PIPELINE-001`.

The fixture contains:

- one question-formulation interaction;
- one reply-formulation interaction;
- one coherent selected source sequence;
- progressive reveal;
- authentic source attribution;
- human review.

## Source selection review

Selected source sequence:

`#1 MattP -> #2 pf_moore -> #4 MattP -> #7 cjames23`

The sequence is selected source ordering, not a claim that every edge is an explicit Discourse reply.

Source-native relationships:

| post | API `reply_to_post_number` |
|---|---:|
| `#1` | `null` |
| `#2` | `null` |
| `#4` | `2` |
| `#7` | `4` |

Post `#2` is a topic-level response. The earlier tree builder projected topic-level responses under root post `#1`. That projection supported traversal but did not preserve source-native relationship semantics.

Selection reasons:

- the opening post contains reusable technical-question phrasing;
- post `#2` provides a direct challenge to the proposal;
- posts `#4` and `#7` continue the same adoption and standardisation discussion;
- the branch remains understandable without reading linked documents;
- code and external examples are not required to understand the selected interaction points;
- both the opening post and reply contain reusable conversational phrasing.

Interaction coverage:

| post | judgment |
|---|---|
| `#1` | Question interaction generated and reviewed. |
| `#2` | Reply interaction generated and reviewed. |
| `#4` | Retained in the source sequence; quiz generation not investigated. |
| `#7` | Retained in the source sequence; quiz generation not investigated. |

The review does not establish a no-quiz source-turn type.

## Question-formulation interaction

File:

`question-interaction.json`

Prompt:

`product/fixture/experiments/gpt-oss-20b/question-quiz-generation/prompt-v5-topic-107565-golden-run.md`

Model configuration:

| field | value |
|---|---|
| Model | `gpt-oss-20b` |
| Reasoning | `medium` |
| Observed latency | Approximately 37 seconds for an early topic `107565` run. |

Deterministic review:

- output parses as one JSON object;
- exactly three options exist;
- option IDs are `A`, `B`, and `C`;
- exactly one option is preferred;
- every option contains a non-empty explanation;
- the source phrase occurs verbatim in post `#1`;
- the source phrase retains the backticks around `targets`.

Human review:

- the context is declarative and focused;
- option A directly addresses the displayed concern;
- options B and C expose distinct question intents;
- all options sound natural;
- no unsupported technical facts were introduced;
- the interaction preserves the proposal-feedback social situation.

Verdict:

Accepted.

## Reply-formulation interaction

File:

`reply-interaction.json`

Prompt:

`product/fixture/experiments/gpt-oss-20b/question-quiz-generation/prompt-v1-reply-topic-107565-golden-run.md`

Model configuration:

| field | value |
|---|---|
| Model | `gpt-oss-20b` |
| Reasoning | `medium` |
| Observed latency | Not recorded. |

The visible prior turn was the accepted generated question from the first interaction.
The full raw opening post was not included because it consumed too much of the local model context window.
The authentic post `#2` remained the source turn for phrase extraction and semantic grounding.

Deterministic review:

- output parses as one JSON object;
- exactly three options exist;
- option IDs are `A`, `B`, and `C`;
- exactly one option is preferred;
- every option contains a non-empty explanation;
- every option works as a direct reply to the visible prior question;
- the source phrase occurs verbatim in post `#2`.

Human review:

- option A best fits the adoption-uncertainty context;
- options A, B, and C address distinct concerns;
- no option closely reconstructs an authentic reply sentence;
- uncertainty about adoption remains qualified;
- all replies sound natural and reusable;
- no unsupported factual claim was introduced.

Verdict:

Accepted.

## Model comparison observation

`Qwen3.6-27B` was tested on the reply prompt before fixture materialisation.

| run | observed result |
|---|---|
| Deeper reasoning | Approximately 2 minutes 19 seconds on an RTX 3090; fluent output introduced unsupported fallback, skipping, and error-policy details. |
| Low effort | Faster than the deeper run; output still introduced unsupported ecosystem-readiness, compatibility, and tool-requirement claims. |

Comparison judgment:

- Qwen produced fluent and polished text;
- Qwen expanded into technical design beyond the supplied evidence;
- the added VRAM and latency cost did not improve acceptance quality for this bounded task;
- `gpt-oss-20b` medium reasoning remains the preferred first-MVP generation configuration;
- human review remains mandatory.

The Qwen comparison is model-evaluation evidence only.
It does not change the accepted learning model or pipeline decisions.

## Source-capture correction

A fresh Discourse API capture was saved in `source-topic.raw.json`.
`source-capture.json` records the request URL, timestamp, HTTP status, and SHA-256 digest.

The API-derived selected posts replaced the earlier whitespace-normalized `source-posts.json`.
The superseded file remains as `source-posts.pre-api-normalized.json` for comparison evidence.

Comparison results:

- all four post bodies were content-equivalent after whitespace normalization;
- all accepted source phrases still matched exactly;
- usernames matched;
- posts `#4` and `#7` retained their explicit reply targets;
- post `#2` changed from projected parent `#1` to source-native `null`.

No generated interaction required regeneration.

## Transport-fidelity observation

A copied prompt initially appeared to lose Markdown backticks around `targets`.
The ChatGPT application removed those characters during copying from rendered text.
The omission was not a model exact-copy failure.

Operational rule:

- run prompts from repository files;
- preserve the exact request payload before invocation;
- verify transport fidelity before judging model source fidelity;
- preserve raw model responses without manual repair.

## Acceptance summary

The fixture demonstrates that one reviewed Packaging source sequence can support:

- reusable question exposure from an authentic opening post;
- reusable reply exposure from an authentic response;
- a compact generated prior turn for constrained local-model context;
- exact source-phrase attribution;
- progressive reveal for one reviewed question-and-reply pair;
- retention of later source turns without claiming their quiz behavior was tested;
- separate representation of source-native replies, projected tree parents, and selected source-sequence order.

Package fields and boundaries must be derived from fixture evidence later.
This review does not define the package schema or permit selected source turns without quizzes.
