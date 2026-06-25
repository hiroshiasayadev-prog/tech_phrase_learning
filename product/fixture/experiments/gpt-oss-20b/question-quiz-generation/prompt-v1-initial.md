# Question quiz generation prompt v1

- **prompt_id**: `question-quiz-generation-v1-reconstructed`
- **status**: reconstructed
- **model**: `gpt-oss-20b`
- **reasoning**: `medium`

## Purpose

Generate one question-formulation quiz from one authentic opening post.

## Reconstructed user prompt

```text
Create one phrase-oriented question-formulation quiz from the authentic opening post below.

Requirements:
- return exactly 3 plausible generated options;
- mark exactly 1 option as preferred;
- explain each option briefly;
- provide only the minimal context needed for the exercise;
- do not answer the technical question;
- generated options are learning abstractions, not reconstructions of the source wording;
- include one useful source phrase copied exactly from the authentic opening post;
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

## Observed limitation

The three options could remain semantically equivalent.
The preferred choice could therefore become arbitrary.
