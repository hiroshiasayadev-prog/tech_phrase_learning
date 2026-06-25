# Question candidate filter prompt

- **prompt_id**: `question-candidate-filter-v1-reconstructed`
- **status**: reconstructed
- **model**: `gpt-oss-20b`
- **reasoning**: `medium`
- **batch_size**: 8
- **maximum_selected**: 2

## Purpose

Select opening posts that expose reusable natural English for asking technical questions.

The model receives reduced opening-post records.
Each record contains only:

- `topic_id`;
- `title`;
- `text`.

The reduced `text` keeps question-bearing paragraphs, nearby context, and the final paragraph.
Code blocks may be replaced with `[code omitted]`.

## Reconstructed user prompt

```text
You are reviewing opening posts from technical discussions.

Select posts that contain useful, reusable natural English for asking a technical question.
The learner already understands the technical domain and is learning conversational phrasing.

Select no more than 2 posts from this batch.
Return fewer than 2 when the remaining posts do not contain a useful question phrase.

For each selected post:
- copy one exact phrase from the supplied text;
- the phrase must contain wording used to ask the question;
- do not select only technical vocabulary, a code fragment, or a topic label;
- classify the conversational move;
- explain briefly why the phrase is reusable.

Useful move labels include:
- possibility;
- clarification;
- recommendation;
- evaluation;
- troubleshooting;
- how_to.

Reject:
- text that is not actually a question phrase;
- search-query-style fragments with little conversational value;
- release announcements and informational notices;
- phrases useful only because of their technical subject matter.

Return JSON only in this shape:
[
  {
    "topic_id": 123,
    "exact_phrase": "exact substring from text",
    "move": "possibility",
    "reason": "short reason"
  }
]

Opening posts:
{{OPENING_POST_RECORDS_JSON}}
```

## Deterministic checks

- Output parses as JSON.
- Output contains at most two selections.
- Every `topic_id` exists in the input batch.
- Every `exact_phrase` occurs character-for-character in that record's `text`.
- Required fields are present and non-empty.

## Human review

Reviewers judge:

- whether the selected span is genuinely a question phrase;
- naturalness and reuse value;
- whether the move label is informative;
- whether the item is strong, useful, weak, or a false positive.
