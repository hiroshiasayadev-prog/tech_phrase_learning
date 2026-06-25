# Post summary prompt v3: authored text

- **prompt_id**: `conversation-post-summary-v3-authored-text`
- **status**: current investigation prompt
- **model_role**: post summarizer

## User prompt template

Summarize one technical-discussion post for an English phrase-learning pipeline.

The supplied `authored_text` contains only the current author's own contribution. Quoted blocks from earlier posts were removed mechanically. Use parent and quote-target summaries only as conversational context; never attribute them to the current author.

The learner already understands software engineering. Make the conversational movement easy to follow without requiring long code, link lists, or implementation detail.

Requirements:

- Write one or two short natural-English sentences.
- Keep the summary at 55 words or fewer.
- Preserve the author's stance, uncertainty, qualification, and conversational intent.
- Do not invent technical facts, motives, adoption claims, or conclusions.
- Omit code and detailed examples unless essential to the main conversational point.
- Distinguish challenging, evaluating, clarifying, proposing, qualifying, and seeking feedback.
- Treat the summary as generated text, not as a quotation.
- Extract one to three short reusable phrase candidates copied exactly from `authored_text`.
- Each phrase candidate must contain reusable conversational wording, not only technical terms.
- Preserve every source character in each phrase candidate.
- Prefer short candidates without Markdown links.
- If a candidate includes a Markdown link, copy the complete source syntax.
- Explain each candidate's conversational function without answering the technical issue.

Return one JSON object matching the supplied JSON schema.

## Input

{{POST_INPUT_JSON}}
