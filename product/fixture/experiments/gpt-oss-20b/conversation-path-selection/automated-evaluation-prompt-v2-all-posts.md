# Automated evaluation prompt v2: all posts

- **prompt_id**: `conversation-path-evaluation-v2-all-posts`
- **status**: preserved experiment prompt

Evaluate all generated post summaries and the proposed learning sequence using the supplied source posts.

Check summary fidelity, preserved uncertainty, conversational continuity, reading burden, exact phrase-candidate fidelity, and likely phrase-learning value. Flag unsupported, reversed, or overstated claims. Review unselected posts as well as selected posts, because a bad summary can distort path ranking. Use `needs_review` when uncertain. Do not rewrite the summaries. Return one JSON object matching the supplied JSON schema.

## Input

{{EVALUATION_INPUT_JSON}}
