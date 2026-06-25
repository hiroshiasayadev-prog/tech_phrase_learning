# Question quiz generation prompt v3

- **prompt_id**: `question-quiz-generation-v3-reconstructed`
- **status**: reconstructed
- **model**: `gpt-oss-20b`
- **reasoning**: `medium`

## Purpose

Harden source-span fidelity and prevent unsupported technical assumptions.

## Reconstructed user prompt

```text
Create one phrase-oriented question-formulation quiz from the authentic opening post below.

Generate exactly 3 grammatically plausible question options:
- one option must be clear, direct, and appropriately specific;
- one option must be too vague for the situation;
- one option must be unnecessarily tied to implementation details.

Mark the clear, direct, appropriately specific option as preferred.
Its advantage must come from question formulation, not from answering the technical issue.

Every generated option must preserve the same technical intent.
A weaker option may be vague or less reusable, but it must not introduce a new technical assumption.

Additional requirements:
- provide only the minimal context needed for the exercise;
- do not answer the technical question;
- generated options are learning abstractions, not source reconstructions;
- explain each option briefly;
- the source phrase must include wording used to ask the question;
- do not select only the technical action or subject;
- copy the source phrase character-for-character from the authentic post;
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
    "text": "exact source substring",
    "function": "short phrase function"
  }
}

Authentic opening post:
{{OPENING_POST_JSON}}
```

## Observed improvement

Exact source-span selection became reliable enough for mechanical validation.

## Observed limitation

The same-intent constraint was later judged too strict for the product goal.
It optimizes quiz precision rather than broad exposure to natural phrases.
