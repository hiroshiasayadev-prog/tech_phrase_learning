# Question quiz generation prompt v2

- **prompt_id**: `question-quiz-generation-v2-reconstructed`
- **status**: reconstructed
- **model**: `gpt-oss-20b`
- **reasoning**: `medium`

## Purpose

Create visible formulation contrast between generated options.

## Reconstructed user prompt

```text
Create one phrase-oriented question-formulation quiz from the authentic opening post below.

Generate exactly 3 grammatically plausible question options:
- one option must be clear, direct, and appropriately specific;
- one option must be too vague for the situation;
- one option must be unnecessarily tied to implementation details.

Mark the clear, direct, appropriately specific option as preferred.
Its advantage must come from question formulation, not from answering the technical issue.

Additional requirements:
- provide only the minimal context needed for the exercise;
- do not answer the technical question;
- generated options are learning abstractions, not source reconstructions;
- explain each option briefly;
- select one short reusable source phrase;
- the source phrase must include wording used to ask the question;
- do not select only the technical action or subject;
- return JSON only.

Return this shape:
{
  "title": "short generated title",
  "context": "minimal generated situation",
  "options": [
    {
      "id": "A",
      "text": "generated question",
      "preferred": true,
      "explanation": "short explanation"
    },
    {
      "id": "B",
      "text": "generated question",
      "preferred": false,
      "explanation": "short explanation"
    },
    {
      "id": "C",
      "text": "generated question",
      "preferred": false,
      "explanation": "short explanation"
    }
  ],
  "source_phrase": {
    "text": "source phrase",
    "function": "short phrase function"
  }
}

Authentic opening post:
{{OPENING_POST_JSON}}
```

## Observed improvement

The option roles became easier to distinguish.

## Observed limitations

- The source phrase could still be a generated paraphrase rather than an exact source span.
- The implementation-specific option could introduce details absent from the source.
