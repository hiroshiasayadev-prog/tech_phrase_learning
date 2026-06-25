# PRODUCT-ADR-LEARNING-002: Use prediction and reveal over authentic conversation segments for the first MVP

- **status**: superseded
- **date**: 2026-06-24
- **depends_on**: [PRODUCT-ADR-LEARNING-001]
- **supersedes**: []
- **migrated_to_spec**: 2026-06-24

## Context

The first MVP must test whether real technical conversations provide useful phrase exposure.

Whole discussion topics are too long for a focused learning interaction.
Isolated phrases remove the conversational situation that explains their use.

A phrase-oriented reply quiz can focus attention on tone and conversational fit.
The quiz must not claim to reconstruct the exact source reply.
Generated options require review because several responses may be reasonable.

The MVP needs a small learner-visible unit that preserves authentic interaction.
The unit must expose conversational intent without requiring the learner to read an entire topic.

## Decision

The first MVP will use an authentic conversation segment as its primary learning unit.

A conversation segment will contain:

- a concise context capsule;
- a short sequence of source conversation turns;
- one selected reply to reveal;
- useful phrase spans from the revealed reply;
- concise explanations of phrase function and nuance;
- source attribution.

The first interaction will present a generated phrase-oriented reply quiz.

The quiz will contain:

- a generated title;
- a minimal generated context summary;
- generated reply options;
- one preferred option for the represented situation;
- concise explanations for the options.

The quiz may remove or generalize technical details.
The quiz must preserve the source interaction's social situation and conversational intent.
The quiz must not add unsupported technical facts.

The product will reveal the authentic source conversation after selection.
The reveal will show the corresponding source reply and useful source phrases.

Multiple real child replies may appear as authentic alternative branches.
Generated options are learning abstractions, not claimed source reconstructions.

Every published MVP learning unit will require human review.

## Rationale

A short segment preserves the situation that gives each phrase meaning.
The segment also limits reading load and supports repeated exposure.

Choosing among phrase-oriented replies directs attention toward tone and conversational fit.
Revealing the authentic reply preserves observed native usage.

Separating generated quiz content from source content avoids false reconstruction claims.
Authentic branches show that different responses can be reasonable.

Human review protects learners from incorrect summaries, labels, or explanations during early validation.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Present whole discussion topics | Topic length and branching would obscure the phrase-learning task. |
| Present isolated phrase cards | The learner would lose the reply context and conversational intent. |
| Present generated options as source reconstructions | Generated wording would falsely imply that participants used those exact replies. |
| Ask learners to predict the exact next sentence | Many phrasings can express the same valid conversational move. |
| Publish generated annotations without review | Early model errors could teach misleading usage. |

## Consequences

- The pipeline must extract coherent conversation segments from larger topics.
- The learning model requires phrase-oriented quiz content and phrase-function annotations.
- Source replies remain unchanged in the learner-visible reveal.
- Quiz titles, context summaries, options, and explanations remain derived content.
- The MVP requires a review workflow before publication.
- Exact segment limits and annotation schemas belong to learning and pipeline specifications.
- Adaptive or unreviewed generated reply exercises remain later features.

## Evidence

- Stack Overflow answers often resolve a question without sustained conversation.
- GitHub pull requests frequently contain no meaningful human exchange.
- Python Discussions contains self-contained opening posts and threaded technical discussion.
- Real technical threads contain clarification, disagreement, concession, and alternative proposals.
- The target learner already understands the technical domain and can focus on conversational phrasing.
