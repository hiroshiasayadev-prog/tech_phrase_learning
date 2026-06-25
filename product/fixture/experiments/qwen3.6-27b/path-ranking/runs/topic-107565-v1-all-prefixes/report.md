# Qwen path-ranking experiment

- Judge model: `qwen3.6-27b:q4_k_m-tools`
- Fixed upstream run: `C:\Users\imved\projects\tech_phrase_learning\product\fixture\experiments\gpt-oss-20b\conversation-path-selection\runs\topic-107565-v3`
- Candidate count: `6`
- Ranking validation: `True`
- Qwen top path: `#1 -> #2 -> #4`
- Reviewed reference path: `#1 -> #2 -> #4 -> #7`
- Reference rank: `5`
- GPT-OSS path: `#1 -> #2 -> #4 -> #5`
- GPT-OSS path rank: `4`

## Ranking

| rank | candidate | path | phrase | coherence | lightness | detail control | function variety | weighted |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | P002 | #1 -> #2 -> #4 | 5 | 5 | 4 | 5 | 5 | 4.85 |
| 2 | P001 | #1 -> #2 | 5 | 5 | 5 | 4 | 4 | 4.75 |
| 3 | P006 | #1 -> #3 | 4 | 5 | 5 | 5 | 3 | 4.35 |
| 4 | P003 | #1 -> #2 -> #4 -> #5 | 4 | 4 | 3 | 4 | 5 | 4.0 |
| 5 | P005 | #1 -> #2 -> #4 -> #7 | 4 | 4 | 3 | 4 | 5 | 4.0 |
| 6 | P004 | #1 -> #2 -> #4 -> #6 | 3 | 4 | 3 | 3 | 4 | 3.4 |

## Top-choice reason

P002 maximizes reusable conversational phrase value and functional variety while maintaining a highly coherent flow and minimal technical distraction. It strikes the optimal balance for lightweight English learning by extending the core exchange with practical functions like seeking feedback and expressing nuanced uncertainty.

## Candidate notes

### Rank 1: P002 — #1 -> #2 -> #4

P002 offers the best balance of conversational variety and reusable phrasing. It naturally extends the initial exchange with clear functions for seeking feedback and expressing nuanced uncertainty, all while keeping technical details minimal and the flow highly coherent.

Strengths:
- Excellent flow from proposal to questioning to seeking feedback
- Highly reusable phrases for uncertainty and soliciting opinions
- Maintains low technical burden while expanding conversational functions

Weaknesses:
- Slightly longer than the shortest paths, marginally increasing cognitive load

### Rank 2: P001 — #1 -> #2

P001 is a tight, highly coherent two-post exchange with excellent reusable phrases for proposals and doubt. It ranks second due to slightly lower functional variety compared to P002, though it excels in cognitive lightness.

Strengths:
- Extremely concise and direct exchange
- Strong foundational phrases for proposing and expressing doubt
- Very low cognitive burden

Weaknesses:
- Fewer conversational functions compared to extended paths
- Lacks explicit feedback-seeking or stance-taking phrases

### Rank 3: P006 — #1 -> #3

P006 is exceptionally light and coherent, featuring clear phrases for reluctance and alternatives. It ranks third because its conversational function variety is narrower than the top contenders, making it less comprehensive for phrase learning.

Strengths:
- Very short and easy to follow
- Useful phrases for expressing reluctance and offering alternatives
- Minimal technical distraction

Weaknesses:
- Limited variety of conversational functions
- Less interactive back-and-forth compared to other paths

### Rank 4: P003 — #1 -> #2 -> #4 -> #5

P003 introduces excellent phrases for certainty and historical explanation, boosting functional variety. It ranks fourth because the added context and length increase cognitive load, slightly detracting from the lightweight learning goal.

Strengths:
- Adds valuable functions for expressing certainty and explaining historical context
- Rich variety of conversational moves
- Maintains reasonable technical control

Weaknesses:
- Increased length and historical context raise cognitive burden
- Slightly more complex flow due to multiple speakers and topics

### Rank 5: P005 — #1 -> #2 -> #4 -> #7

P005 provides robust phrases for debate and conditional stances, offering high variety. It ranks fifth because the assertive and conditional language increases cognitive effort compared to the more straightforward exchanges in higher-ranked paths.

Strengths:
- Strong phrases for asserting stance and setting conditions
- Good variety of conversational functions
- Clear argumentative flow

Weaknesses:
- Higher cognitive burden due to conditional reasoning and stance-taking
- Slightly more abstract phrasing may require more parsing

### Rank 6: P004 — #1 -> #2 -> #4 -> #6

P004 focuses on technical clarification and implementation details, which reduces the broad conversational reusability of its phrases. It ranks last because the technical focus conflicts with the priority of lightweight, broadly applicable English learning.

Strengths:
- Useful clarification phrases
- Clear informative stance
- Maintains logical flow

Weaknesses:
- Leans heavily into technical implementation details
- Phrases are less broadly reusable outside technical contexts
- Higher technical detail burden

## Interpretation boundary

The ranking is an independent model judgment over fixed upstream summaries and phrase candidates. It does not replace human acceptance of the final learning path.

