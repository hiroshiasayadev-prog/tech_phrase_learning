# Automated evaluation prompt v3: complete coverage

- **prompt_id**: `conversation-path-evaluation-v3-complete-coverage`
- **status**: current investigation prompt

Evaluate every generated post summary and the proposed learning path using the supplied authored source text.

Requirements:

- Return exactly one `summary_reviews` item for every supplied post.
- Preserve the same post numbers and ascending order.
- Check summary fidelity, preserved uncertainty, authored-text attribution, exact phrase-candidate fidelity, conversational continuity, reading burden, and phrase-learning value.
- Flag unsupported, reversed, overstated, or quote-contaminated claims.
- Review selected and unselected posts because any bad summary can distort path ranking.
- Use `needs_review` when uncertain.
- Do not rewrite summaries or phrase candidates.

Return one JSON object matching the supplied JSON schema.

## Input

{{EVALUATION_INPUT_JSON}}
