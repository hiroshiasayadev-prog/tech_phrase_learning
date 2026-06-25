# PRODUCT-INV-LEARNING-001: Question-formulation quiz model

- **status**: concluded
- **date**: 2026-06-24
- **trigger**: The first golden-session investigation exposed a learner need to practice asking technical questions, not only replying to them.
- **scope**: Investigate whether question formulation should become a first-class learning interaction and how it relates to reply-oriented quizzes.
- **non_scope**: Excludes adoption of a revised learning model, changes to accepted ADRs, final package schema, fixture authoring, UI implementation, and source-category expansion.
- **source_refs**:
  - PRODUCT-INV-PIPELINE-001
  - spec:product.learning.learning_model
  - spec:product.learning.learning_unit
  - spec:product.learning.quiz_session
  - PRODUCT-ADR-LEARNING-002
  - PRODUCT-ADR-LEARNING-003
  - PRODUCT-ADR-PIPELINE-003
- **follow_up_candidates**:
  - A new learning ADR that supersedes or extends PRODUCT-ADR-LEARNING-002, if required.
  - Updates to `spec:product.learning.learning_model`.
  - Updates to `spec:product.learning.learning_unit`.
  - Updates to `spec:product.learning.quiz_session`.
  - Resumption of PRODUCT-INV-PIPELINE-001 after the learning-model boundary is resolved.
- **follow_up_results**:
  - PRODUCT-ADR-LEARNING-004
  - spec:product.learning
  - spec:product.learning.learning_model
  - spec:product.learning.learning_unit
  - spec:product.learning.quiz_session

## Investigation scope

This investigation examines question formulation as a learner-facing interaction.

The investigation must determine whether the product should teach two distinct conversational moves:

- initiating a technical conversation;
- responding within an existing technical conversation.

The investigation must also determine whether one learning session may contain both moves.

The result will provide evidence for later ADR and specification work.
The investigation will not change the accepted learning contract directly.

## Out of scope

- Final adoption of question-formulation quizzes.
- Direct modification of PRODUCT-ADR-LEARNING-002 or PRODUCT-ADR-LEARNING-003.
- Final normative learning-unit package schema.
- Golden fixture creation.
- Automated question generation.
- Concrete UI design.
- Expansion of the accepted initial source category.
- Final licensing or redistribution decisions.

## Background

The current learning contract is primarily reply-oriented.

`spec:product.learning.learning_unit` defines generated reply options.
`spec:product.learning.quiz_session` defines a generated reply-choice interaction.
PRODUCT-ADR-LEARNING-002 establishes phrase-oriented reply quizzes followed by authentic source reveal.

The learner identified a broader and more frequent need: asking technical questions.
Typical opportunities include opening discussions, requesting clarification, describing problems, and asking reviewers for guidance.

Question formulation may require different learner-visible semantics from reply formulation.
The authentic turn may be an opening post rather than a reply.
The generated context may represent a problem state before any source conversation exists.

## What was investigated

The investigation will answer these questions:

1. Should question formulation become a first-class learning interaction?
2. Are question formulation and reply formulation separate learning-unit step types?
3. May one session contain both question and reply steps?
4. Should question formulation precede reply formulation in the first MVP?
5. What information must generated context provide before an opening-question quiz?
6. What generated options produce useful comparison without claiming source reconstruction?
7. Should the authentic opening post be revealed after selection?
8. Which phrase functions should be highlighted in authentic questions?
9. How should question clarity, directness, politeness, and technical sufficiency be reviewed?
10. Which current ADRs or learning specs require revision?
11. Does the golden-session investigation need to pause until this boundary is resolved?

### Initial motivating example

Source topic:

`https://discuss.python.org/t/passing-a-keyword-argument-containing-a/107763`

Category shown by the source:

`Python Help`

Authentic opening post supplied as investigation evidence:

> Is there some way I can use a hyphen in the name of a keyword argument as in the example below?
>
> `set_cookie("cookieName", "cookieValue", Max-Age=0, Expires="")`

Observed reusable question structure:

1. Ask whether the desired operation is possible.
2. Name the operation directly.
3. Provide a minimal example.

Observed phrase candidates:

- `Is there some way I can ...?`
- `as in the example below`

The example is evidence for the learning-model question.
It is not yet an accepted golden-fixture candidate.
The topic is outside the Packaging category selected by PRODUCT-ADR-PIPELINE-003.

## Findings

### Learning interaction boundary

- Question formulation is a distinct and useful learning interaction.
- The learner expects more opportunities to ask technical questions than to answer them.
- Question formulation targets an authentic opening post rather than an authentic reply.
- Question and reply formulation require different generated contexts and reveal targets.
- A progressive session can support both interaction types.
- The first golden fixture does not need to demonstrate both types at once.

### Quiz purpose

- The quiz primarily delivers exposure to natural conversational phrases.
- Strict assessment accuracy is secondary to phrase exposure.
- Every generated option should sound natural and provide reusable language.
- Generated options may express different conversational or technical intents.
- The preferred option only needs to fit the generated context best.
- Generated options remain abstractions and must not be presented as source reconstructions.

### Authentic reveal and phrase spans

- An authentic opening post can be revealed after a question-formulation selection.
- The reveal should preserve the same generated-versus-authentic separation used for replies.
- A highlighted source phrase must occur verbatim in the authentic post.
- The highlighted span should include question-formulation wording, not only technical vocabulary.
- Exact source-span validation can be mechanical.

### Source examples

| topic | move | evidence | assessment |
|---|---|---|---|
| `107763` | Possibility | `Is there some way I can use a hyphen` | Strong minimal candidate with a direct question and small example. |
| `107844` | Recommendation | `what's the most Pythonic approach these days?` and `What do you all use in production?` | Strong richer candidate with several reusable recommendation patterns. |
| `107650` | Clarification | The useful question appears in the title, while the body is dominated by console output. | Weak candidate for the first fixture. |

Topic `107763` appears preferable for the first minimal question-formulation fixture.
Topic `107844` appears useful as a later richer comparison fixture.

### Lightweight-model experiment

- A title-only pass returned 38 candidates and did not filter strictly enough.
- Opening-post evaluation produced a smaller and more useful shortlist.
- Reduced model input retained question paragraphs and removed irrelevant payload fields.
- Eight reduced posts consumed about 25 percent of the model context window.
- The opening-post filter selected ten examples across the tested batches.
- Manual review classified five as strong, two as useful, two as weak, and one as a false positive.
- The false positive selected technical text instead of a question phrase.
- Medium-reasoning quiz generation consumed about 18 percent of the context window.
- Medium reasoning produced sufficient draft quality for reviewed generation.
- High reasoning took about three minutes and showed no consistent quality improvement.
- Human review remains necessary for naturalness, phrase usefulness, and option quality.
- Reconstructed prompts, recorded outputs, and review notes are preserved under `product/fixture/experiments/gpt-oss-20b`.
- The prompt files are marked reconstructed because the exact original request payloads were not saved.

### Current-contract gaps

- PRODUCT-ADR-LEARNING-002 defines the interaction in reply-oriented terms.
- `spec:product.learning.learning_unit` defines generated reply options.
- `spec:product.learning.quiz_session` defines a reply-choice interaction.
- The current records do not define authentic opening-post reveal.
- Implementing question-formulation quizzes before follow-up decisions would exceed the accepted contract.

## Cross-cutting observations

- Conversation initiation and response belong to the same broader technical-participation learning goal.
- Source-category suitability and learning-pattern usefulness are separate judgments.
- A source outside the accepted corpus can provide investigation evidence without changing corpus scope.
- Lightweight models benefit from deterministic input reduction and bounded output contracts.
- Mechanical fidelity checks and human semantic review address different failure classes.
- Quiz-option diversity can increase phrase exposure even when the options express different intents.

## Follow-up judgment candidates

- Candidate: Expand the learning model from reply choice to technical-conversation participation.
- Candidate: Define question formulation and reply formulation as separate interaction types.
- Candidate: Allow progressive sessions to contain either or both interaction types.
- Candidate: Define quiz options as phrase-exposure material rather than strict answer alternatives.
- Candidate: Supersede or extend PRODUCT-ADR-LEARNING-002 because its reply-only wording is too narrow.
- Candidate: Keep Python Help examples as investigation evidence without expanding the accepted initial corpus.
- Candidate: Use medium-reasoning `gpt-oss-20b` for reviewed candidate filtering and draft generation.

## Recommendation

Question formulation appears suitable as a first-class learning interaction.

A follow-up ADR should broaden the learning model from reply selection to technical-conversation phrase exposure.
The ADR should define question formulation and reply formulation as distinct interaction types.
The ADR should preserve generated-versus-authentic separation for both types.

The learner-facing contract should treat quizzes as phrase-exposure scaffolding.
Generated options should be natural and useful even when their intents differ.
The preferred option should represent the best fit for the displayed context.

After the ADR and learning specs are updated, PRODUCT-INV-PIPELINE-001 should resume.
Topic `107763` appears preferable for the first minimal golden fixture.

## Follow-up artifact candidates

- A new learning ADR that supersedes or extends PRODUCT-ADR-LEARNING-002.
- `spec:product.learning.learning_model` update.
- `spec:product.learning.learning_unit` update.
- `spec:product.learning.quiz_session` update.
- PRODUCT-INV-PIPELINE-001 update after the learning-model decision.
- A later pipeline contract for reviewed lightweight-model candidate filtering.

## Open questions

- Must the first MVP mix question and reply interactions within one session?
- Does the accepted Packaging corpus contain enough useful opening-question examples?
- Should a second golden fixture test the richer recommendation-question shape before package specification?
- What review-result contract should record naturalness, source fidelity, and publication readiness?
