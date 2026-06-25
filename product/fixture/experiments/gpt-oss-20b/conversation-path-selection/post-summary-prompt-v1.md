# Post summary prompt v1

- **prompt_id**: `conversation-post-summary-v1`
- **status**: preserved experiment prompt
- **model_role**: post summarizer

## User prompt template

Summarize one authentic technical-discussion post for an English phrase-learning pipeline.

The learner already understands software engineering.
The summary should make the conversational movement easy to follow without requiring the learner to read long code blocks, link lists, or implementation details.

Requirements:

- Write one or two short natural-English sentences.
- Keep the summary at 55 words or fewer.
- Preserve the author's stance, uncertainty, qualification, and conversational intent.
- Do not invent technical facts, motives, adoption claims, or conclusions.
- Omit code and detailed examples unless they are essential to the author's main point.
- Describe what the author is doing conversationally, not every technical detail they mention.
- Treat the summary as generated text, not as a quotation.
- Use the supplied parent and quote summaries only as context. The authentic current post is the authority.

Return one JSON object matching the supplied JSON schema.

## Input

{{POST_INPUT_JSON}}
