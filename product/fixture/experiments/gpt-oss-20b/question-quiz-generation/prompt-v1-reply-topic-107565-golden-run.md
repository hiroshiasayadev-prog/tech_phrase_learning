# Reply quiz generation prompt v1: Topic 107565 golden run

- **prompt_id**: `reply-quiz-generation-v1-topic-107565-golden-run`
- **status**: current golden-run prompt
- **model**: `gpt-oss-20b`
- **reasoning**: `medium`
- **topic_id**: `107565`
- **source_post_number**: `2`

## Purpose

Generate the reply-formulation interaction for the first golden learning session.

This prompt uses the accepted generated question as the only visible prior turn.
It does not include the full authentic opening post.

This prompt is topic-specific investigation evidence.
It does not define a normative runtime prompt or package schema.

## Invocation instructions

1. Read this prompt directly from the repository file.
2. Preserve all source characters in the request payload.
3. Use `medium` reasoning.
4. Use API-level JSON enforcement when supported.
5. Save the exact request payload and raw response before review.

## User prompt

```text
RETURN ONE JSON OBJECT ONLY.
THE FIRST CHARACTER OF YOUR RESPONSE MUST BE `{`.
THE LAST CHARACTER OF YOUR RESPONSE MUST BE `}`.
DO NOT RETURN MARKDOWN, HEADINGS, TABLES, CODE FENCES, NOTES, OR TEXT OUTSIDE THE JSON OBJECT.

Create one phrase-exposure interaction that teaches natural ways to reply to a technical proposal.

Visible prior turn:
Should the frontend attempt to call a conventionally named build_XXX hook if the requested target isn't listed in the targets table?

Authentic reply:
What *frontend* tools do you expect to support this new interface? I don't expect pip to - pip currently only uses `build_wheel` and the associated methods, we don't even have a need for `build_sdist`.

Without a frontend using these new APIs, I don't see a good reason for standardising anything.

There's also the fact that I've seen almost no demand for building "non-standard targets" of the form you're describing, but that may simply because I don't work on tools that would see such demand. I note that the examples you found are *plugins* for hatch, and therefore could easily have been created to satisfy one person's nice use case (I don't *know* if that's the case, though, so I'm not claiming there's no demand, just that I'm not aware of any).

Generate:
- one short declarative context;
- exactly three natural direct replies;
- exactly one preferred reply;
- one short explanation inside each option;
- the exact source phrase and function supplied below.

Context requirement:
The context must express uncertainty about whether standardisation is justified because expected frontend adoption is unclear.
Do not say or imply that no frontend plans to adopt the interface.
The context must make exactly one reply fit best.
The preferred reply and both non-preferred replies must address different concerns.
The two non-preferred replies must not restate the preferred reply using different wording.

Reply requirements:
- every option must directly reply to the visible prior turn;
- every option must sound natural and expose reusable conversational phrasing;
- the three options must express different intents;
- each option must address a different concern in the discussion;
- the two non-preferred options must not be paraphrases of the preferred option or of each other;
- do not introduce unsupported technical facts;
- do not claim that demand does not exist;
- do not claim whether any packaging tool requires non-standard targets;
- do not paraphrase the authentic question about which frontend tools would support the interface;
- do not closely reconstruct any sentence from the authentic reply;
- generated options must differ from the authentic reply in both wording and sentence structure;
- do not reuse both `Without/If there is no frontend...` and `I don't see a good reason...` in one generated option.

Required source phrase:
Without a frontend using these new APIs, I don't see a good reason for standardising anything.

Required source function:
Challenges whether standardization is justified without expected adoption.

Return exactly this JSON shape:
{
  "title": "short title",
  "context": "short declarative situation",
  "options": [
    {
      "id": "A",
      "text": "natural direct reply",
      "preferred": true,
      "explanation": "short explanation of intent and fit"
    },
    {
      "id": "B",
      "text": "natural direct reply",
      "preferred": false,
      "explanation": "short explanation of intent and fit"
    },
    {
      "id": "C",
      "text": "natural direct reply",
      "preferred": false,
      "explanation": "short explanation of intent and fit"
    }
  ],
  "source_phrase": {
    "text": "Without a frontend using these new APIs, I don't see a good reason for standardising anything.",
    "function": "Challenges whether standardization is justified without expected adoption."
  }
}

Before responding, verify:
- the response parses as JSON;
- the first character is `{` and the last character is `}`;
- no text exists outside the JSON object;
- there are exactly three options with IDs A, B, and C;
- every option contains `id`, `text`, `preferred`, and `explanation`;
- exactly one option has `"preferred": true`;
- all three options express distinct intents and address different concerns;
- neither non-preferred option restates the preferred reply in different wording;
- `source_phrase.text` and `source_phrase.function` match the required strings exactly.

RETURN ONE JSON OBJECT ONLY.
```

## Deterministic checks

- The response begins with `{` and ends with `}`.
- The complete response parses as one JSON object.
- No text exists outside the JSON object.
- The output contains exactly three options with IDs `A`, `B`, and `C`.
- Every option contains a non-empty explanation.
- Every option works as a direct reply to the supplied generated question.
- Exactly one option is preferred.
- The source phrase occurs character-for-character in the authentic reply.

## Human review

Reviewers judge:

- naturalness and reuse value of every reply;
- coherence with the visible prior question;
- whether exactly one option best fits the context;
- whether all three options express distinct intents and address different concerns;
- whether the non-preferred replies avoid restating the preferred reply;
- whether adoption uncertainty remains qualified;
- whether generated replies avoid close reconstruction of authentic sentences;
- absence of unsupported technical claims;
- source-phrase fidelity.
