# Qwen path-ranking experiment

- Judge model: `qwen3.6-27b:q4_k_m-tools`
- Fixed upstream run: `C:\Users\imved\projects\tech_phrase_learning\product\fixture\experiments\gpt-oss-20b\conversation-path-selection\runs\topic-107565-v3`
- Candidate count: `3`
- Ranking validation: `True`
- Qwen top path: `#1 -> #2 -> #4 -> #5`
- Reviewed reference path: `#1 -> #2 -> #4 -> #7`
- Reference rank: `2`
- GPT-OSS path: `#1 -> #2 -> #4 -> #5`
- GPT-OSS path rank: `1`

## Ranking

| rank | candidate | path | phrase | coherence | lightness | detail control | function variety | weighted |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | P001 | #1 -> #2 -> #4 -> #5 | 5 | 5 | 5 | 4 | 5 | 4.9 |
| 2 | P003 | #1 -> #2 -> #4 -> #7 | 4 | 4 | 4 | 4 | 4 | 4.0 |
| 3 | P002 | #1 -> #2 -> #4 -> #6 | 4 | 4 | 3 | 3 | 4 | 3.75 |

## Top-choice reason

P001 offers the highest density of broadly reusable conversational phrases (expressing certainty, explaining historical reasons, seeking feedback) while maintaining the lowest cognitive and technical burden. Its flow naturally models a collaborative discussion without getting bogged down in implementation specifics.

## Candidate notes

### Rank 1: P001 — #1 -> #2 -> #4 -> #5

P001 best balances reusable phrase value with low cognitive load. The final post adds clear expressions of certainty and historical context without heavy jargon, making it ideal for lightweight phrase acquisition.

Strengths:
- Highest variety of everyday conversational functions (certainty, historical reasoning, seeking feedback)
- Phrases are short, natural, and highly transferable to non-technical contexts
- Technical context is present but does not obscure the language learning value

Weaknesses:
- Slight repetition of uncertainty expressions across posts 1 and 4

### Rank 2: P003 — #1 -> #2 -> #4 -> #7

P003 is a solid second choice due to its clear argumentative structure and useful stance expression, though the phrasing is slightly less versatile and more verbose than P001.

Strengths:
- Introduces a clear stance expression useful for debates and evaluations
- Maintains a logical discussion flow with familiar technical terms
- Good mix of proposing, questioning, and evaluating functions

Weaknesses:
- The stance phrase is quite long and somewhat context-bound to software standardization
- Fewer distinct conversational functions compared to P001

### Rank 3: P002 — #1 -> #2 -> #4 -> #6

P002 ranks last because the technical explanation distracts from the conversational phrases, reducing cognitive lightness and technical detail control despite having good clarification wording.

Strengths:
- Excellent phrases for correcting misconceptions and clarifying definitions
- Natural conversational pivot that models how to politely correct a premise

Weaknesses:
- Higher technical burden (PEP 517, wheel intermediates, implementation details) increases cognitive load
- Clarification is tightly coupled to specific technical explanations, reducing phrase reusability

## Interpretation boundary

The ranking is an independent model judgment over fixed upstream summaries and phrase candidates. It does not replace human acceptance of the final learning path.

