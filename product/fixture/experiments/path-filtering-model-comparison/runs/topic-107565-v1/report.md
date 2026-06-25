# Path-filtering model comparison

Each case was judged independently. Expected labels were not sent to either model.

## Summary

| model | accuracy | valid recall | invalid rejection | target met |
|---|---:|---:|---:|---|
| gpt-oss:20b | 1.000 | 1.000 | 1.000 | True |
| qwen3.6-27b:q4_k_m-tools | 1.000 | 1.000 | 1.000 | True |

## Case decisions

| case | expected | class | gpt-oss:20b | qwen3.6-27b:q4_k_m-tools |
|---|---|---|---|---|
| T001 | accept | real_valid_path | accept | accept |
| T002 | accept | real_valid_path | accept | accept |
| T003 | accept | real_valid_path | accept | accept |
| T004 | accept | real_valid_path | accept | accept |
| T005 | accept | real_valid_path | accept | accept |
| T006 | accept | real_valid_path | accept | accept |
| T007 | reject | invalid_disconnected_structure | reject | reject |
| T008 | reject | invalid_no_phrase_evidence | reject | reject |
| T009 | reject | invalid_technical_only_phrase_evidence | reject | reject |

## Agreement

- Cases compared: `9`
- Same decision: `9`
- Agreement rate: `1.000`
- Disagreements: `[]`

## gpt-oss:20b

- False rejections: `[]`
- False acceptances: `[]`

### T001 — accept

Expected: `accept`

Learning focus: `['expressing proposals and concerns about standardization', 'expressing uncertainty about adoption']`

Evidence: `['I want to standardize hatchling targets.', 'I feel like this overcomplicates the pyproject.toml']`

Exclusion reasons: `[]`

The path contains two posts, mechanically valid, and includes source‑verified phrase candidates that are conversational in nature (e.g., "I want to standardize hatchling targets." and "I feel like this overcomplicates the pyproject.toml"). The technical detail is moderate but does not overwhelm the conversational learning value, and the session length is within the allowed 2–6 posts. Therefore the path meets all validity criteria.

### T002 — accept

Expected: `accept`

Learning focus: `['expressing uncertainty', 'seeking feedback']`

Evidence: `["I can't definitively say this one way of the other", 'I would love to get some feedback from any of these frontend developers if this is something they can see being standardized.']`

Exclusion reasons: `[]`

The path contains three posts, each with source‑verified phrase candidates. At least one candidate, "I can't definitively say this one way of the other", is a reusable conversational phrase that is not purely technical. The conversation remains coherent, stays within the 2–6 post limit, and the technical detail is moderate, allowing learners to focus on conversational patterns such as expressing uncertainty and seeking feedback.

### T003 — accept

Expected: `accept`

Learning focus: `['expressing uncertainty about adoption', 'seeking feedback']`

Evidence: `['I want to standardize hatchling targets.']`

Exclusion reasons: `[]`

The path contains four posts, mechanically valid, and includes source‑verified phrase candidates that are conversational in nature (e.g., "I want to standardize hatchling targets."). The technical content is moderate and does not overwhelm the conversational learning value. All criteria for a valid quiz path are satisfied.

### T004 — accept

Expected: `accept`

Learning focus: `['expressing uncertainty about adoption', 'seeking feedback']`

Evidence: `['I want to standardize hatchling targets.', 'I feel like this overcomplicates the pyproject.toml', "I don't expect pip to", 'I would love to get some feedback from any of these frontend developers if this is something they can see being standardized.']`

Exclusion reasons: `[]`

The path contains four posts, each with at least one source‑verified conversational phrase. The technical content is moderate and does not overwhelm the conversational learning value. The conversation is coherent, the structure is mechanically valid, and the post count falls within the allowed range. Therefore the path is valid for a lightweight English phrase‑learning quiz session.

### T005 — accept

Expected: `accept`

Learning focus: `['seeking feedback on standardization', 'expressing uncertainty about adoption']`

Evidence: `['I would love to get some feedback from any of these frontend developers if this is something they can see being standardized.']`

Exclusion reasons: `[]`

The path contains four posts, which is within the allowed range of 2–6. The structure is mechanically valid and the conversation flows coherently. At least one phrase candidate is a reusable conversational expression: "I would love to get some feedback from any of these frontend developers if this is something they can see being standardized." Technical detail is present but not overwhelming, and the overall reading and technical burdens are moderate. Therefore the path satisfies all validity criteria.

### T006 — accept

Expected: `accept`

Learning focus: `['expressing proposals and concerns', 'communicating availability of options']`

Evidence: `['I want to standardize hatchling targets.', 'I feel like this overcomplicates the pyproject.toml', 'I have a couple of these options', 'you can use the CLI directly']`

Exclusion reasons: `[]`

The path contains two posts, each with clear conversational intent and at least one source‑verified phrase that is reusable conversational wording. The technical detail is moderate and does not overwhelm the conversational learning value. The conversation is coherent and within the allowed length, satisfying all validity criteria.

### T007 — reject

Expected: `reject`

Learning focus: `[]`

Evidence: `["I'm pretty certain"]`

Exclusion reasons: `['invalid_structure']`

The supplied path is marked as mechanically invalid, which disqualifies it from being a valid quiz path regardless of other criteria.

### T008 — reject

Expected: `reject`

Learning focus: `[]`

Evidence: `[]`

Exclusion reasons: `['no_reusable_phrase']`

The supplied path contains no phrase candidates, so it fails the requirement that at least one reusable conversational wording be present. Without such evidence, the path cannot be considered valid for a quiz session.

### T009 — reject

Expected: `reject`

Learning focus: `[]`

Evidence: `[]`

Exclusion reasons: `['no_reusable_phrase']`

All phrase candidates in the supplied posts are technical terms only and none represent reusable conversational wording. Therefore the path fails the requirement for at least one reusable phrase candidate.

## qwen3.6-27b:q4_k_m-tools

- False rejections: `[]`
- False acceptances: `[]`

### T001 — accept

Expected: `accept`

Learning focus: `['expressing proposals and concerns', 'questioning feasibility and adoption', 'indicating uncertainty']`

Evidence: `['I feel like this overcomplicates the pyproject.toml', "I'm not sure whether or not the build frontend should support building targets that are not listed in the `targets` table.", "I don't expect pip to", "I don't *know* if that's the case"]`

Exclusion reasons: `[]`

The path meets all validity criteria. It contains exactly two posts forming a coherent proposal-and-response sequence. The supplied phrase candidates are source-verified and clearly reusable in general conversational contexts (e.g., expressing concern about complexity, questioning adoption, indicating uncertainty). While the topic involves software build tools, the technical context does not overwhelm the conversational learning value, and the reading/technical burden remains within acceptable limits.

### T002 — accept

Expected: `accept`

Learning focus: `['expressing proposals and concerns', 'seeking feedback and clarification', 'expressing uncertainty and doubt']`

Evidence: `['I feel like this overcomplicates the pyproject.toml', "I don't expect pip to", 'I would love to get some feedback from any of these frontend developers if this is something they can see being standardized.', "I can't definitively say this one way of the other"]`

Exclusion reasons: `[]`

The path meets all validity criteria: it is mechanically valid, contains exactly 3 posts (within the 2-6 limit), and forms a coherent conversational sequence about standardizing build targets. It supplies multiple source-verified, reusable conversational phrases focused on proposing ideas, expressing concern/uncertainty, and requesting feedback. The technical context is present but does not overwhelm the conversational learning value, making it fully suitable for a lightweight English phrase-learning quiz.

### T003 — accept

Expected: `accept`

Learning focus: `['expressing proposals and concerns', 'seeking feedback', 'expressing uncertainty', 'clarifying context']`

Evidence: `['I feel like this overcomplicates the pyproject.toml', 'I would love to get some feedback from any of these frontend developers if this is something they can see being standardized.', "I don't *know* if that's the case", "I'm pretty certain", "I can't definitively say this one way of the other"]`

Exclusion reasons: `[]`

The path satisfies all validity conditions: it is mechanically valid, presents a coherent conversational sequence regarding tool standardization and adoption, contains multiple source-verified reusable conversational phrases focused on proposing, questioning, seeking feedback, and clarifying, maintains a medium technical burden that does not overwhelm the conversational learning value, and contains exactly four posts. No exclusion criteria are triggered.

### T004 — accept

Expected: `accept`

Learning focus: `['expressing uncertainty', 'seeking feedback', 'clarifying technical points', 'expressing concern about complexity']`

Evidence: `['I feel like this overcomplicates the pyproject.toml', "I don't *know* if that's the case", 'I would love to get some feedback from any of these frontend developers if this is something they can see being standardized.', "They aren't implemented like that, of course"]`

Exclusion reasons: `[]`

The path satisfies all five validity conditions: it is mechanically valid, forms a coherent four-post discussion about Python build tool standardization, and falls within the required 2-6 post range. The technical context is present but manageable (low to medium burden) and does not obscure the conversational language. Multiple source-verified phrase candidates clearly demonstrate reusable conversational functions such as expressing uncertainty, seeking feedback, and clarifying, making the path suitable for a lightweight English learning quiz.

### T005 — accept

Expected: `accept`

Learning focus: `['expressing uncertainty', 'seeking feedback', 'stating conditions for action', 'proposing and evaluating ideas']`

Evidence: `['I feel like this overcomplicates the pyproject.toml', "I don't *know* if that's the case", 'I would love to get some feedback from any of these frontend developers if this is something they can see being standardized.', 'I want to see more than one tool implementing something with significant adoption before trying to standardize it.', "I can't definitively say this one way of the other"]`

Exclusion reasons: `[]`

The path satisfies all five validity conditions: it is mechanically valid with exactly four posts (within the 2–6 limit), presents a coherent back-and-forth sequence about standardization and adoption, includes multiple source-verified phrases that function as reusable conversational language rather than isolated technical terms, and maintains a medium technical burden that does not overshadow the practical phrasing. No exclusion criteria are triggered.

### T006 — accept

Expected: `accept`

Learning focus: `['expressing proposals and concerns', 'expressing reluctance and preferences', 'suggesting alternatives']`

Evidence: `['I feel like this overcomplicates the pyproject.toml', 'I have no desire to see them formalised', 'you can use the CLI directly']`

Exclusion reasons: `[]`

The path satisfies all validity criteria: it is mechanically valid with exactly two posts, forms a coherent proposal-response sequence, provides multiple source-verified reusable conversational phrases, and maintains a medium technical burden that does not overwhelm the conversational learning value.

### T007 — reject

Expected: `reject`

Learning focus: `[]`

Evidence: `[]`

Exclusion reasons: `['invalid_structure']`

The supplied metadata explicitly marks the path as mechanically invalid ('mechanically_valid': false), which directly violates the first validity criterion. Although the post count falls within the acceptable range and reusable conversational phrases are present, the structural failure alone mandates rejection.

### T008 — reject

Expected: `reject`

Learning focus: `[]`

Evidence: `[]`

Exclusion reasons: `['no_reusable_phrase']`

The path satisfies structural, length, and coherence requirements, and the technical burden is manageable. However, every post contains an empty 'phrase_candidates' array. The validity criteria explicitly require at least one supplied source-verified phrase candidate that functions as reusable conversational wording. Since no candidates were provided, the path cannot support phrase-learning and is rejected.

### T009 — reject

Expected: `reject`

Learning focus: `[]`

Evidence: `[]`

Exclusion reasons: `['no_reusable_phrase']`

The path fails criterion 3: all supplied phrase candidates are explicitly marked as 'technical term only' (e.g., 'pyproject.toml', 'build_wheel', 'pip', 'uv', 'PEP 517'). None qualify as reusable conversational wording. While the structure is valid, the sequence is coherent, and the post count is within limits, the complete absence of conversational phrase evidence makes it unsuitable for the stated phrase-learning goal.

