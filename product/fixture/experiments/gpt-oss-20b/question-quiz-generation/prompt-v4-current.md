# Question quiz generation prompt v4

- **prompt_id**: `question-quiz-generation-v4-current`
- **status**: current experiment contract
- **model**: `gpt-oss-20b`
- **reasoning**: `medium`

## Purpose

Generate a reviewed phrase-exposure interaction under the current learning contract.

The quiz is scaffolding for exposure to natural phrases.
It is not a strict technical knowledge test.

## User prompt

```text
Create one phrase-exposure interaction from the authentic opening post below.

The interaction teaches natural ways to ask a technical question.
The learner already understands the technical domain.

Generate exactly 3 question options.

Option requirements:
- every option must sound natural to a fluent technical English speaker;
- every option must contain reusable conversational phrasing;
- the options may express different conversational or technical intents;
- the options must remain plausible within the same broad technical situation;
- do not introduce unsupported technical facts;
- do not copy or closely reconstruct the authentic source wording.

Preferred-option requirements:
- mark exactly 1 option as preferred;
- the preferred option must fit the displayed generated context best;
- preference is based on contextual fit, not on technical correctness;
- the preferred option does not need to reproduce the complete intent of the authentic post.

Explanation requirements:
- explain each option's conversational intent and contextual fit briefly;
- do not describe a natural non-preferred option as grammatically wrong;
- do not answer the underlying technical question.

Source-phrase requirements:
- copy one reusable phrase character-for-character from the authentic opening post;
- the phrase must include wording used to ask the question;
- do not select only technical vocabulary or the technical action;
- describe its conversational function briefly.

Context requirements:
- provide only the information needed to understand the broad situation;
- preserve the source interaction's social situation;
- generated context must remain distinct from authentic source text.

Return JSON only in this shape:
{
  "title": "short generated title",
  "context": "minimal generated situation",
  "options": [
    {
      "id": "A",
      "text": "natural generated question",
      "preferred": true,
      "explanation": "short intent and fit explanation"
    },
    {
      "id": "B",
      "text": "natural generated question",
      "preferred": false,
      "explanation": "short intent and fit explanation"
    },
    {
      "id": "C",
      "text": "natural generated question",
      "preferred": false,
      "explanation": "short intent and fit explanation"
    }
  ],
  "source_phrase": {
    "text": "exact source substring",
    "function": "short conversational function"
  }
}

Authentic opening post:
{{OPENING_POST_JSON}}
```

## Deterministic checks

- Output parses as JSON.
- There are exactly three options with unique IDs.
- Exactly one option is preferred.
- The source phrase occurs character-for-character in the authentic post.
- Required fields are present and non-empty.

## Human review

Reviewers judge:

- naturalness of every option;
- phrase reuse value;
- plausibility within the broad situation;
- fit of the preferred option to the generated context;
- absence of unsupported technical facts;
- usefulness of the authentic source phrase;
- separation of generated and authentic content.
