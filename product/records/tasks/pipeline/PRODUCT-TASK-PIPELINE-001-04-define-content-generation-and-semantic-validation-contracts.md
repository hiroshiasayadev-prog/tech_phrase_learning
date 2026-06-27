# PRODUCT-TASK-PIPELINE-001-04: Define content generation and semantic-validation contracts

- **id**: PRODUCT-TASK-PIPELINE-001-04
- **status**: done
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PIPELINE-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 2.5d
- **depends_on**:
  - PRODUCT-TASK-PIPELINE-001-03
- **outputs**:
  - PRODUCT-ADR-PIPELINE-011
  - PRODUCT-ADR-PIPELINE-012
  - PRODUCT-ADR-PIPELINE-013
  - PRODUCT-ADR-PIPELINE-014
  - PRODUCT-ADR-PIPELINE-015
  - PRODUCT-ADR-PIPELINE-016

## Goal

Define bounded summary, target-phrase, intent-prompt, quiz-generation, and semantic-validation stage contracts.

## Work

1. Read accepted Pipeline ADRs, T03 path outputs, and the fixed Learning unit contract.
2. Define reusable source-post summary inputs, outputs, grounding evidence, and validation obligations.
3. Define path-specific summary revision inputs, outputs, and continuity constraints.
4. Require summaries to preserve position, certainty, response meaning, and source grounding.
5. Define unsupported-claim rejection and generated-versus-source-authored separation.
6. Define target-phrase selection as a distinct bounded stage.
7. Define concise intent-prompt generation as a distinct bounded stage.
8. Define exactly-three-option quiz generation as a distinct bounded stage.
9. Require generated option identity to be semantic and independent from array position.
10. Require one correct-option reference that resolves within the interaction.
11. Define naturalness, contextual fit, target-phrase realization, and incorrect-option usefulness evaluation.
12. Define per-stage input completeness, structured-output validation, source-grounding checks, and semantic evaluation results.
13. Define invalid provider output as untrusted stage output without selecting a retry policy.
14. Define how contradictory or incomplete stage results are reported to orchestration.
15. Preserve provider isolation and smallest-sufficient-context requirements from current ADRs.
16. Create or update Pipeline ADRs when current authority does not determine observable generation or validation semantics.
17. Keep exact prompts, model names, thresholds, schemas, and provider assignments outside the contract.
18. Update `outputs` and Evidence with accepted ADRs or specification inputs.

## Done condition

- Reusable and path-specific summary stages have explicit inputs, outputs, and grounding obligations.
- Conversational continuity and unsupported-claim rejection are explicit.
- Generated and source-authored content remain distinguishable.
- Target-phrase selection, prompt generation, and quiz generation are separate bounded stages.
- Every interaction produces exactly three semantically identified options and one correct-option reference.
- Naturalness, contextual fit, phrase realization, and distractor usefulness have explicit evaluation outcomes.
- Every model-produced structure has mechanical validation and semantic evaluation obligations.
- Invalid, incomplete, and contradictory stage results have explicit orchestration-facing outcomes.
- Every new normative decision has accepted Pipeline ADR authority.
- Concrete model, prompt, threshold, and serialized schema choices remain deferred.

## Verification

- Trace each output obligation to `spec:product.learning.learning_unit` or accepted Pipeline authority.
- Confirm the stage contracts do not redefine learner-visible meaning.
- Confirm option identity never derives from generated array position, labels, display order, or option text.
- Confirm source grounding does not rely only on model assertion.
- Confirm a model-only success result cannot establish publication readiness.
- Check the reviewed golden fixture and harder experiment findings as evidence, not authority.
- Run relevant record validation, strict specification validation, `git diff --check`, and `git status --short`.

## Evidence

### Decision register

Task Evidence traces user-approved choices to accepted ADR authority.
The accepted ADRs remain the normative decision records.

| sequence | decision | status | accepted ADR |
|---|---|---|---|
| D01 | Reusable-summary generation receives the target post's complete authored text and source binding. An opening post receives no prior-post summary context. A later post receives every validated reusable summary on its mechanically derived ancestor chain, ordered from the opening post through the immediate predecessor. Sibling, later, and unrelated posts are excluded. Quoted material remains separated from authored text. Resolved quote identity and exact quote evidence may be supplied as context but cannot establish the target author's position or phrase evidence. Silent truncation is invalid; a reusable summary may proceed to path filtering only when complete authored-text coverage is established. | accepted | PRODUCT-ADR-PIPELINE-011 |
| D02 | Reusable-summary output contains the target authentic-post identity, reusable summary text, source-author position, source-author certainty or qualification, and conversational response meaning. These fields remain distinct so semantic validation can detect position reversal, lost uncertainty, and changed response meaning even when the prose appears natural. Technical-burden and phrase-learning-potential labels are not required reusable-summary contract fields. Concrete serialized field names and controlled vocabularies remain deferred. | accepted | PRODUCT-ADR-PIPELINE-011 |
| D03 | Reusable-summary semantic validation uses four independent evaluation units: position fidelity, certainty or qualification fidelity, conversational response-meaning fidelity, and unsupported-claim or attribution detection. Every unit executes. Each valid PASS identifies the target post, evaluated dimension, non-empty explanation, and exact authored-text evidence. Mechanical validation verifies complete unique dimension coverage, target identity, evidence membership in the target authored text, quote separation, and non-contradictory verdicts. Any valid semantic failure rejects the generated summary as a grounding failure. Invalid evaluator output remains distinct from content rejection. | accepted | PRODUCT-ADR-PIPELINE-011 |
| D04 | Source-grounded phrase-evidence extraction is a bounded stage separate from reusable-summary generation. The stage receives the target authentic-post identity, complete authored text, interaction role, validated reusable summary, ordered validated ancestor summaries, and quote-boundary evidence. Candidate text must come only from the target post's authored text. Summary failure and phrase-evidence failure remain independently observable. T03 filtering consumes only phrase evidence that passes mechanical and semantic validation. | accepted | PRODUCT-ADR-PIPELINE-012 |
| D05 | Source-grounded phrase-evidence extraction returns zero to three candidates per post. Zero candidates is a valid semantic result meaning that complete processing found no usable conversational phrase. It is distinct from invalid output, grounding failure, or extraction failure. Each candidate identifies the target post, exact authored-text span, source location, required question or reply role, and conversational function. A candidate may contain technical terms, but it is rejected when no reusable conversational English remains beyond technical vocabulary. A path containing a post with zero validated candidates fails that post's T03 suitability requirement rather than becoming a Pipeline execution failure. | accepted | PRODUCT-ADR-PIPELINE-012 |
| D06 | Phrase-evidence validation separates deterministic grounding checks from two independent semantic evaluation units: conversational-function fit and phrase usefulness. Both evaluations run for every mechanically valid candidate. Only candidates that pass both remain validated phrase evidence; valid candidates may survive when sibling candidates fail. An extraction result with zero candidates requires a separate semantic confirmation that the complete post contains no usable conversational phrase. Mechanical validation covers target identity, exact authored-text membership, source location, quote exclusion, interaction role, cardinality, and duplicate spans. | accepted | PRODUCT-ADR-PIPELINE-012 |
| D07 | Path-specific summary revision runs only after a candidate path has passed T03 filtering. Posts are revised in source order. Each revision unit receives the valid path identity, target post identity, the target post's validated reusable summary and structured position, certainty, and response-meaning fields, plus every preceding path-specific summary already accepted for that path. Later-post context is excluded. Revision may improve references, omitted-topic clarity, continuity, repetition, and technical compression, but must preserve source-author position, certainty, response meaning, technical claims, phrase evidence, path identity, and attribution. An unchanged result is valid. Output identifies the target post, revised summary or unchanged result, and the reason for any change. | accepted | PRODUCT-ADR-PIPELINE-013 |
| D08 | Path-specific summary validation uses two independent semantic evaluation units: semantic preservation and path continuity. Semantic preservation checks position, certainty or qualification, response meaning, technical claims, attribution, and unsupported additions against the validated reusable summary and source evidence. Path continuity checks reference clarity, conversational relation, required topic retention, and excessive repetition against preceding accepted path-specific summaries. Both evaluations run for revised and unchanged results. Mechanical validation verifies path and target identities, exactly one result per path post, source-order processing, mutually exclusive revised or unchanged outcomes, exclusion of later-post context, and reference to validated reusable-summary inputs. | accepted | PRODUCT-ADR-PIPELINE-013 |
| D09 | Target-phrase selection is a bounded stage after path-specific summary acceptance. For each interaction, the stage receives the valid path and target-post identities, interaction type, one to three validated phrase-evidence candidates from the target post, the accepted path-specific summary and structured position, certainty, and response meaning, every preceding accepted path-specific summary, and the target post's authored text. Later-post context is excluded. The stage selects exactly one validated phrase-evidence candidate and produces exactly one target phrase as a grounded unchanged or generalized transformation. Permitted changes include technical-noun replacement, reusable-span extraction, minimal contextual completion, and minor grammatical adjustment. The transformation must preserve conversational function, position, certainty, and source-post grounding. Output identifies the selected evidence, target phrase, conversational function, transformation kind, and explanation. | accepted | PRODUCT-ADR-PIPELINE-014 |
| D10 | Target-phrase validation uses three independent semantic evaluation units: grounded transformation, phrase usefulness, and contextual sufficiency. Grounded-transformation evaluation checks traceability to the selected phrase evidence, exclusion of other-post wording, preserved position, certainty, conversational function, and valid technical generalization. Phrase-usefulness evaluation checks natural reusable conversational English rather than technical vocabulary alone. Contextual-sufficiency evaluation checks that the phrase preserves enough wording to demonstrate its usage and remains suitable for the interaction type and preceding path context. All three must pass. Mechanical validation verifies exactly one target phrase per interaction, resolvable same-post evidence, matching path and post identities, non-empty text, exclusive unchanged or generalized classification, excluded later-post context, complete evaluation coverage, and generated-source separation. | accepted | PRODUCT-ADR-PIPELINE-014 |
| D11 | Quiz-prompt generation is a bounded stage after target-phrase acceptance. The generator does not receive the target phrase text, selected phrase-evidence wording, current authored text, answer options, or later-post context. It receives the valid path and target-post identities, interaction type, accepted path-specific summary, structured position, certainty or qualification, conversational response meaning, target phrase conversational function, and preceding accepted path-specific summaries. Existing validated semantic fields supply the required intent representation; no additional intent-extraction stage is required. The generated English prompt states the intended communicative situation concisely, preserves position and certainty, minimizes source-specific technical detail, and includes only enough context to judge options without revealing the target phrase or its near-verbatim wording. | accepted | PRODUCT-ADR-PIPELINE-014 |
| D12 | Quiz-prompt validation uses three independent semantic evaluation units: intent fidelity, answer leakage, and prompt usability. Intent-fidelity evaluation checks that the prompt preserves the source author's communicative intent, position, certainty, and interaction role. Answer-leakage evaluation checks both direct phrase disclosure and semantic near-disclosure of the accepted target phrase. Prompt-usability evaluation checks that the prompt contains enough situation detail to distinguish options while remaining concise and minimizing source-specific technical detail. All three must pass. Mechanical validation verifies exactly one non-empty prompt per interaction, matching path and post identities, absence of exact target-phrase text, exclusion of later-post context, complete unique evaluation coverage, and generated-source separation. | accepted | PRODUCT-ADR-PIPELINE-014 |
| D13 | Exactly-three-option generation uses three bounded sequential model tasks rather than one combined generation call. The first task generates one correct option from the accepted quiz prompt, target phrase, interaction type, conversational function, position, certainty, and minimum preceding context. The second task generates one distractor with the prompt and accepted correct option visible. The third task generates another distractor with the prompt and both accepted earlier options visible. Each distractor must remain natural and useful English, clearly unsuitable for the prompt, and semantically distinct from the other options. Deterministic orchestration assigns semantic option identities independent from array position, labels, display order, and option text, then creates one correct-option reference resolving to the correct option identity. | accepted | PRODUCT-ADR-PIPELINE-015 |
| D14 | Option validation is staged. The correct option must independently pass naturalness, target-phrase realization, prompt fit, and meaning-preservation evaluations before distractor generation proceeds. Each distractor must independently pass naturalness and usefulness, prompt mismatch, and unsupported-claim avoidance before the next option proceeds. After all three options exist, set-level evaluation independently checks exactly one best fit, pairwise semantic distinction, and absence of trivial answer cues. Deterministic validation verifies exactly three non-empty options, unique semantic option identities, no exact duplicate text, one same-interaction correct-option reference, complete required evaluation coverage, and identity independence from array position, labels, display order, and option text. | accepted | PRODUCT-ADR-PIPELINE-015 |
| D15 | Every generation and semantic-evaluation stage reports one orchestration-facing outcome from: accepted, incomplete input, provider failure, invalid provider output, semantic rejection, incomplete evaluation, or contradictory evaluation. Invalid provider output means the model response cannot be trusted structurally or by identity. Semantic rejection means a structurally valid result fails accepted meaning criteria. Incomplete and contradictory evaluation remain distinct from both. Retry count, provider switching, and rerun scope remain outside this decision. No non-accepted model output or evaluation result may become input to a downstream stage. | accepted | PRODUCT-ADR-PIPELINE-016 |
| D16 | One interaction remains incomplete until every required summary, target-phrase, prompt, option, identity, reference, and evaluation result for that selected post is accepted. One incomplete interaction prevents materialization of the whole Learning Unit for its valid path. The Pipeline must not skip the failed post, shorten or mutate the valid path, or publish a partial unit. Accepted intermediate artifacts may be retained and reused so reruns can resume from the failed stage. Failure remains localized to the affected path, post, and stage and does not invalidate shared source artifacts, validated reusable artifacts, or Learning Units derived from other valid paths. | accepted | PRODUCT-ADR-PIPELINE-016 |
| D17 | Content-validation completion is determined by deterministic, non-compensating aggregation of accepted stage and evaluation results. The Pipeline does not add one universal model judgment over the completed Learning Unit. Every valid-path post must have one complete interaction, every required structural and semantic result must be present and accepted, identities and ordering must agree, source routes and generated-source separation must remain intact, and no rejection, incompleteness, or contradiction may be present. A pass in one dimension cannot compensate for a failure in another. This completion result establishes readiness to enter the later publication gate; it does not itself authorize publication. | accepted | PRODUCT-ADR-PIPELINE-016 |

### ADR materialization

Six accepted Pipeline ADRs now provide normative authority for every T04 decision.
No normative specification changed during ADR authoring.

### Verification state

Filesystem review confirmed unique ADR sequences, matching file-name prefixes, matching H1 IDs, required metadata fields, and canonical dependency refs.

Final repository verification completed successfully:

- `git diff --check` completed without reported output;
- strict specification validation returned `[strict]  All 34 file(s) OK.`;
- `git status --short` showed only the T04 change scope;
- the change scope contained this Task, its parent Work Item, and PRODUCT-ADR-PIPELINE-011 through PRODUCT-ADR-PIPELINE-016.

Every T04 decision now traces to accepted Pipeline ADR authority.
No normative specification changed during T04.
PRODUCT-TASK-PIPELINE-001-04 is `done` and commit-ready.
