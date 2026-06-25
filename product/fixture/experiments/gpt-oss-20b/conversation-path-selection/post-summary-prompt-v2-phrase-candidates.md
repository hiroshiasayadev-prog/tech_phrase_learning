# Post summary prompt v2: phrase candidates

- **prompt_id**: `conversation-post-summary-v2-phrase-candidates`
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
- Distinguish challenging, evaluating, clarifying, proposing, qualifying, and seeking feedback. Do not label a challenge as merely seeking feedback.
- Treat the summary as generated text, not as a quotation.
- Use the supplied parent and quote summaries only as context. The authentic current post is the authority.
- Extract one to three short reusable phrase candidates copied exactly from the authentic current post.
- Each phrase candidate must contain reusable conversational wording, not only technical terms.
- Preserve every source character in each phrase candidate.
- Explain the conversational function of each phrase candidate without answering the technical issue.

Return one JSON object matching the supplied JSON schema.

## Input

{{POST_INPUT_JSON}}
