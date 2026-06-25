# Automated evaluation prompt v1

- **prompt_id**: `conversation-path-evaluation-v1`
- **status**: preserved experiment prompt

Evaluate generated post summaries and a proposed learning sequence using the supplied source posts.

Check summary fidelity, preserved uncertainty, conversational continuity, reading burden, and likely phrase-learning value. Flag unsupported or overstated claims. Use `needs_review` when uncertain. Do not rewrite the summaries. Return one JSON object matching the supplied JSON schema.

## Input

{{EVALUATION_INPUT_JSON}}
