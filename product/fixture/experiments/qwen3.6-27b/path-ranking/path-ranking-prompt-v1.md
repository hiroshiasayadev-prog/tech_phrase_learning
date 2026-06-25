# Qwen path-ranking prompt v1

- **prompt_id**: `qwen-conversation-path-ranking-v1`
- **status**: investigation
- **model_role**: independent learning-path ranker

## User prompt template

Rank every supplied candidate conversation path for an English phrase-learning session.

The candidate paths were enumerated mechanically from one coarse conversation tree. The post summaries and phrase candidates are fixed upstream evidence. You are not choosing or rewriting posts, summaries, phrases, or tree relationships.

The learner already understands software engineering. The product goal is lightweight exposure to reusable conversational English, not deep technical reading or faithful reproduction of every technical detail.

Ranking priorities, in order:

1. reusable conversational phrase value;
2. understandable conversation flow;
3. variety of conversational functions such as proposing, questioning, qualifying, disagreeing, clarifying, and evaluating;
4. low cognitive burden;
5. controlled technical-detail burden.

Important rules:

- Rank every candidate exactly once.
- Use only the supplied candidate IDs and paths.
- Do not invent another path.
- Do not assume the longest or most technically informative path is best.
- Prefer broadly reusable conversational wording over tool-specific technical explanation.
- Treat phrase candidates as the strongest evidence of learning value.
- A technically coherent path may still rank lower when its language is less reusable.
- Score each criterion from 1 to 5, where 5 is best.
- `cognitive_lightness` means 5 is easiest and lightest to follow.
- `technical_detail_control` means 5 contains the least distracting technical detail.
- Make the rank order consistent with your stated reasons.

Return one JSON object matching the supplied JSON schema.

## Input

{{RANKING_INPUT_JSON}}
