# Independent quiz-path filter prompt v1

- **prompt_id**: `quiz-path-filter-v1`
- **status**: investigation
- **model_role**: independent absolute filter

## User prompt template

Decide whether the supplied conversation path is usable as one English phrase-learning quiz session.

Judge this path independently. Do not compare it with any alternative path, and do not reject it merely because a shorter, richer, or more interesting path might exist.

The learner already understands software engineering. The product goal is lightweight exposure to reusable conversational English, not deep technical reading.

A path is valid when all of these are true:

1. its supplied structure is mechanically valid;
2. the summarized conversation is understandable as one sequence;
3. at least one supplied source-verified phrase candidate is reusable conversational wording rather than only a technical term;
4. technical detail does not overwhelm the available conversational learning value;
5. the path contains between two and six posts.

Important rules:

- Use only the supplied phrase candidates as exact phrase evidence.
- Do not invent a phrase from a summary.
- A path may be valid with only one narrow learning focus.
- A path may be valid even when it is not the best candidate in the topic.
- Medium reading burden is not by itself a rejection reason.
- Technical context is allowed when reusable conversational language remains visible.
- Reject only for an actual validity failure, not relative inferiority.
- For a valid path, return at least one learning focus and at least one exact phrase candidate as evidence.
- For an invalid path, return one or more controlled exclusion reasons.

Controlled exclusion reasons:

- `invalid_structure`
- `incoherent_conversation`
- `no_reusable_phrase`
- `excessive_session_length`
- `excessive_technical_burden`
- `insufficient_context`

Return one JSON object matching the supplied schema.

## Input

{{FILTER_INPUT_JSON}}
