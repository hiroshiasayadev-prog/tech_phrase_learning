# Question quiz generation prompt v5: Topic 107565 golden run

- **prompt_id**: `question-quiz-generation-v5-topic-107565-golden-run`
- **status**: current golden-run prompt
- **model**: `gpt-oss-20b`
- **reasoning**: `medium`
- **topic_id**: `107565`

## Purpose

Generate the question-formulation interaction for the first golden learning session.

This prompt is topic-specific investigation evidence.
It does not define a normative runtime prompt or package schema.

## Invocation instructions

1. Read this prompt directly from the repository file.
2. Do not copy the prompt from a rendered ChatGPT message.
3. Replace `{{OPENING_POST_JSON}}` with the exact opening-post record for topic `107565`.
4. Preserve Markdown backticks and all other source characters in the request payload.
5. Use `medium` reasoning.
6. Use API-level JSON enforcement when the endpoint supports it.
7. Save the exact request payload and raw model response before review.

Rendered-chat copying may remove Markdown backticks from inline code spans.
A character removed before invocation is a transport or copying error, not a model source-fidelity failure.
Verify the locally stored request payload before evaluating exact copying.

## User prompt

```text
Create one phrase-exposure interaction from the authentic opening post below.

The interaction teaches natural ways to ask a technical question.
The learner already understands the technical domain.

## Authentic social situation

The author is proposing a possible standard for custom build targets and is asking the packaging community to evaluate the proposal.

Preserve that social situation.

Do not transform it into:

- personal implementation support;
- configuration instructions;
- a step-by-step setup request;
- a personal “how do I” question.

## Generated context

Create a short declarative situation focused on this concern:

The author is unsure whether a frontend should attempt to call a conventionally named build hook when a requested custom target is not listed in the `targets` table.

The generated context must be a statement, not a question.

The context must establish one specific concern that exactly one option addresses directly.
The other two options may remain relevant to the proposal, but they must address different concerns.

Keep the context distinct from the authentic source wording.

## Question options

Generate exactly three question options.

Every option must:

- sound natural to a fluent technical English speaker;
- contain reusable conversational phrasing;
- remain plausible within the same broad technical discussion;
- express a meaningful conversational or technical intent;
- avoid unsupported technical facts;
- avoid copying or closely reconstructing the authentic source wording;
- use ordinary, natural wording for system behavior.

Avoid unnatural combinations such as `refuse silently`.
Do not use `silent` or `silently` to describe rejecting a request.

Do not introduce:

- fallback behavior;
- default builds;
- automatic recovery behavior;
- error-handling mechanisms;
- configuration rules;

unless they appear explicitly in the authentic opening post.

Exactly one option must be marked as preferred.

The preferred option must fit the generated context best.

Preference is based on contextual fit, not technical correctness.

## Explanations

Each option must contain a short explanation.

The explanation must describe:

- the option’s conversational intent;
- why it fits or fits less well than the preferred option.

Do not describe a natural non-preferred option as grammatically wrong.

Do not answer the underlying technical question.

## Required authentic source phrase

Set `source_phrase.text` to this exact string:

Does including the `targets` as a key confuse users that lack a thorough understanding of their backend?

Set `source_phrase.function` to this exact string:

Asks whether a proposed configuration choice could confuse users.

The two backtick characters around `targets` are required source characters.

Do not remove, replace, escape, normalize, or reinterpret them.

The exact JSON field must appear as:

"source_phrase": {
  "text": "Does including the `targets` as a key confuse users that lack a thorough understanding of their backend?",
  "function": "Asks whether a proposed configuration choice could confuse users."
}

## Output format

Return exactly one valid JSON object and nothing else.

Do not use Markdown.
Do not use code fences.
Do not write commentary before or after the JSON.
Do not place explanations outside the option objects.
Do not omit any required field.

Return this shape:

{
  "title": "short generated title",
  "context": "short generated situation focused on one specific concern",
  "options": [
    {
      "id": "A",
      "text": "natural generated question",
      "preferred": true,
      "explanation": "short explanation of intent and contextual fit"
    },
    {
      "id": "B",
      "text": "natural generated question",
      "preferred": false,
      "explanation": "short explanation of intent and contextual fit"
    },
    {
      "id": "C",
      "text": "natural generated question",
      "preferred": false,
      "explanation": "short explanation of intent and contextual fit"
    }
  ],
  "source_phrase": {
    "text": "Does including the `targets` as a key confuse users that lack a thorough understanding of their backend?",
    "function": "Asks whether a proposed configuration choice could confuse users."
  }
}

## Final validation

Before responding, verify all of the following:

- the response contains exactly one JSON object;
- no text appears outside the JSON object;
- there are exactly three options;
- the option IDs are A, B, and C;
- every option contains `id`, `text`, `preferred`, and `explanation`;
- every explanation is inside its option object;
- exactly one option has `"preferred": true`;
- the generated context is declarative rather than interrogative;
- exactly one option directly addresses the specific context concern;
- no option uses an unnatural system-action phrase such as `refuse silently`;
- no unsupported fallback or default behavior was introduced;
- `source_phrase.text` matches the required string character-for-character;
- the backticks around `targets` are present;
- `source_phrase.function` matches the required string exactly.

## Authentic opening post

{{OPENING_POST_JSON}}
```

## Deterministic checks

- The output parses as one JSON object.
- The output contains exactly three options with IDs `A`, `B`, and `C`.
- Every option contains a non-empty explanation.
- Exactly one option is preferred.
- The source phrase occurs character-for-character in the locally stored request source.
- The source phrase retains the backticks around `targets`.
- No text occurs outside the JSON object.

## Human review

Reviewers judge:

- naturalness of every option;
- phrase reuse value;
- plausibility within the proposal-feedback situation;
- whether the context is declarative and focused on one specific concern;
- whether exactly one option directly addresses and best fits that concern;
- whether system-action wording sounds natural;
- absence of unsupported technical facts;
- usefulness of the authentic source phrase;
- separation of generated and authentic content.
