# PRODUCT-ADR-LEARNING-004: Use mixed question-and-reply phrase-exposure sessions for the first MVP

- **status**: superseded
- **date**: 2026-06-25
- **depends_on**: [PRODUCT-ADR-LEARNING-001]
- **supersedes**: [PRODUCT-ADR-LEARNING-002, PRODUCT-ADR-LEARNING-003]
- **migrated_to_spec**: 2026-06-25

## Context

The first learning model treated reply formulation as the primary quiz interaction.
That scope excludes how engineers initiate technical conversations.

Engineers need to ask questions, request clarification, seek recommendations, and describe uncertainty.
Question formulation can be more useful than a later reply in the same source discussion.
A reply-only session therefore misrepresents normal technical participation.

PRODUCT-INV-LEARNING-001 tested authentic opening questions and generated question-formulation quizzes.
The investigation found useful patterns for possibility, clarification, recommendation, and evaluation questions.

The experiment also showed that quiz precision is not the primary learning value.
Exposure to several natural phrases within a familiar technical situation provides value by itself.

The first MVP still needs authentic source reveal, progressive ordering, and clear separation between generated and source content.

## Decision

The first MVP will use mixed question-and-reply phrase-exposure sessions.

Every learning session must contain:

- at least one question-formulation interaction;
- at least one reply-formulation interaction;
- one coherent authentic source conversation branch;
- progressive reveal in source order;
- source attribution at the terminal state.

A session must begin from an opening post with useful question-formulation value.
The session must continue into at least one authentic reply with useful conversational phrasing.

A question-formulation interaction will:

1. show minimal generated context for initiating the discussion;
2. show generated question options;
3. wait for the learner's selection;
4. show concise option explanations;
5. reveal the authentic opening post;
6. highlight useful source phrases from the opening post.

A reply-formulation interaction will:

1. show the accumulated authentic conversation;
2. show generated response options;
3. wait for the learner's selection;
4. show concise option explanations;
5. reveal the corresponding authentic reply;
6. highlight useful source phrases from the reply.

Generated options are phrase-exposure material.
Every option should sound natural and contain useful conversational language.
Options may express different conversational or technical intents.

One option will be marked preferred for the displayed context.
The preferred option does not claim to reconstruct the authentic source turn.
Quiz correctness remains secondary to exposure to natural phrasing.

Generated context, options, and explanations must remain distinct from authentic source text.
Authentic source turns must preserve source wording.
Highlighted source phrases must occur verbatim in their revealed turns.

Later interactions must remain hidden until earlier interactions finish.
Every source turn selected for a learning session must have a corresponding learner interaction.

The first MVP will retain a minimal introduction page with a random-start action.
Every published session will require human review.

## Rationale

Technical participation includes both initiating and responding.
A session that teaches only replies leaves a major learner need uncovered.

Requiring both interaction types gives each session a complete conversational shape.
The learner sees how a technical concern is raised and how another engineer responds.

Authentic opening-post reveal extends the existing source-first learning principle without replacing it.
Progressive reveal preserves the information available at each conversational moment.

Treating quizzes as phrase-exposure scaffolding avoids false precision.
Several natural formulations can be valuable even when they express different intentions.

A preferred option still gives the learner a clear interaction path.
Human review protects naturalness, source fidelity, and contextual suitability.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Keep reply-only sessions | Reply-only sessions omit how engineers initiate technical conversations. |
| Create separate question-only and reply-only sessions | Separate sessions would not show the complete flow from question to response. |
| Allow sessions to contain either interaction type | Some sessions would still omit a fundamental form of technical participation. |
| Require every option to preserve the same technical intent | The constraint would reduce useful exposure to varied natural phrases. |
| Treat the quiz as a strict knowledge test | Technical correctness is not the primary learning objective. |
| Reveal generated wording as source reconstruction | Generated text would be falsely attributed to source participants. |
| Reveal the authentic turn before selection | Early reveal would remove the phrase-choice interaction. |

## Consequences

- PRODUCT-ADR-LEARNING-002 and PRODUCT-ADR-LEARNING-003 are superseded.
- The learning specs must define question-formulation and reply-formulation interactions.
- The learning specs must define mixed interaction sessions as mandatory for the first MVP.
- Candidate selection must find opening posts and replies with useful conversational phrasing.
- A source topic without a suitable opening question cannot produce a complete first-MVP session.
- The pipeline must retain authentic opening posts as reveal targets.
- The future package contract must distinguish generated interactions from authentic turns.
- The future package contract must distinguish question and reply interaction types.
- Every selected source turn requires one corresponding interaction before publication.
- Mechanical validation can verify exact source phrase spans.
- Human review must assess naturalness, phrase usefulness, context fit, and source fidelity.
- PRODUCT-INV-PIPELINE-001 can resume after the learning specs reflect this decision.
- The accepted Packaging corpus remains unchanged by this ADR.

## Evidence

- PRODUCT-INV-LEARNING-001 concluded that question formulation is a distinct and useful learning interaction.
- The learner reports more opportunities to ask technical questions than to answer them.
- Topic `107763` provides a compact possibility question followed by authentic replies.
- Topic `107844` provides reusable recommendation patterns and later discussion.
- `gpt-oss-20b` produced useful question-formulation options with bounded prompts and human review.
- Medium-reasoning generation provided sufficient draft quality without the latency cost of high reasoning.
- Exact phrase-span validation detected model outputs that did not occur verbatim in the source.
