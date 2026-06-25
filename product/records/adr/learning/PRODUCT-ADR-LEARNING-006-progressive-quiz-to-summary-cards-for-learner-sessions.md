# PRODUCT-ADR-LEARNING-006: Use progressive quiz-to-summary cards for learner sessions

- **status**: accepted
- **date**: 2026-06-25
- **depends_on**: [PRODUCT-ADR-LEARNING-005]
- **supersedes**: []
- **migrated_to_spec**: 2026-06-25

## Context

The first MVP needs to present one source-post path as a sequence of phrase-learning interactions.

The learner must answer one quiz before seeing the corresponding source-post summary.
Earlier answered turns must remain available as conversation context without occupying the full screen.

The current specifications require progressive reveal and one interaction per selected source turn.
They do not define the learner-facing card transition or the default summarized-post presentation.

The product focuses on phrase learning.
Raw source posts may contain long technical explanations, code blocks, links, and other details that distract from phrase exposure.

## Decision

The learner session will use progressive quiz-to-summary cards.

The session will show:

- zero or more answered cards for completed source turns;
- one active quiz card for the current source turn;
- no later quiz card before the current quiz is completed.

The active quiz card will contain:

- a short English prompt that states what the source author intends to communicate;
- three English answer options;
- one option that best expresses the intended conversational move;
- a control to skip the current discussion.

Each answer option will minimize source-specific technical detail.
Each option will preserve enough situation detail to show how the phrase is used.

After the learner answers, the active quiz card will be replaced by an answered card.
The new answered card will initially remain open.
The answered card will contain:

- the English summary of the corresponding source post;
- the answer result;
- the quiz prompt;
- the correct quiz phrase;
- a control to continue to the next source post or discussion.

Only an answered card's answer-detail region may be collapsed.
The source-post summary remains visible while the answer detail is closed.
The most recently answered card keeps its answer detail open until the learner continues.

The default learner-visible representation of a source post is its validated summary.
The first MVP does not require raw source-post display.
Raw source access may be added later without changing the session progression model.

All learner-facing text will be English.

### Screen model before answering

```text
+------------------------------------------------------------+
| Answered card: Post 1                                [open] |
|------------------------------------------------------------|
| Source-post summary                                       |
|                                                            |
|  +------------------------------------------------------+  |
|  | ✓ Correct                                            |  |
|  |                                                      |  |
|  | Question                                             |  |
|  | The author wants to express uncertainty.             |  |
|  |                                                      |  |
|  | Correct phrase                                       |  |
|  | I don't know if that's the case.                     |  |
|  +------------------------------------------------------+  |
+------------------------------------------------------------+

+------------------------------------------------------------+
| Answered card: Post 2                                      |
|------------------------------------------------------------|
| The author asks whether the existing behavior is still     |
| required for compatibility.                                |
|                                                            |
| [Answer detail: closed]                                    |
+------------------------------------------------------------+

+------------------------------------------------------------+
| Quiz: Post 3                                               |
|------------------------------------------------------------|
| Question                                                   |
| The author wants to explain that the earlier behavior was  |
| probably kept because people still depended on it.         |
|                                                            |
| [A] I'm pretty certain this remained because people        |
|     relied on the previous behavior.                       |
|                                                            |
| [B] I have no idea why this remained, but changing it      |
|     should be harmless.                                    |
|                                                            |
| [C] It no longer matters why this remained because nobody  |
|     depends on it.                                         |
|                                                            |
| [Skip this discussion]                                     |
+------------------------------------------------------------+
```

### Screen model immediately after answering

```text
+------------------------------------------------------------+
| Answered card: Post 3                                [open] |
|------------------------------------------------------------|
| The author believes the behavior remained because older    |
| tools depended on the existing arrangement.                |
|                                                            |
|  +------------------------------------------------------+  |
|  | ✓ Correct                                            |  |
|  |                                                      |  |
|  | Question                                             |  |
|  | The author wants to explain that the earlier         |  |
|  | behavior was probably kept because people still      |  |
|  | depended on it.                                      |  |
|  |                                                      |  |
|  | Correct phrase                                       |  |
|  | I'm pretty certain this remained because people      |  |
|  | relied on the previous behavior.                     |  |
|  +------------------------------------------------------+  |
|                                                            |
|                                      [Next post]            |
+------------------------------------------------------------+
```

### Transition model

```text
answered cards
    +
active quiz card
    |
    | learner answers
    v
active quiz card becomes an answered card
with open answer detail
    |
    | learner continues
    v
answer detail becomes collapsible
    +
next quiz card appears
```

## Rationale

A quiz-first card preserves the phrase-choice interaction before the source-post summary is revealed.

Replacing the quiz card with an answered card keeps one source turn represented by one stable screen element.
The card stack also shows conversation progression without exposing later replies.

Summaries reduce technical reading burden while retaining the conversational movement needed for phrase learning.
Collapsible answer details preserve prior context without hiding source-post summaries.

English-only learner-facing content keeps the product focused on English exposure.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Show the source-post summary before answering | The summary may reveal the intended response before the learner chooses a phrase. |
| Keep the quiz and answer as separate permanent cards | Two cards for one source turn would duplicate structure and weaken conversation continuity. |
| Show raw source posts by default | Long technical detail and code would distract from phrase learning. |
| Collapse the newest answered card immediately | The learner would lose the result and correct phrase before choosing to continue. |
| Show all quizzes at once | Later quizzes would expose future conversational intent and break progressive reveal. |
| Mix Japanese guidance into the learner session | Mixed-language presentation would reduce English exposure. |

## Consequences

- Each selected source turn requires one active quiz state and one answered state.
- The UI must replace the active quiz card after answer submission.
- The UI must keep completed source-post summaries visible and make only answer details collapsible.
- Source-post summaries become required learner-facing content for the first MVP.
- Raw source-post display remains optional and deferred.
- Quiz prompts, options, labels, summaries, and controls require English learner-facing copy.
- The learning specifications must define the semantic content of quiz and answered cards.
- Concrete styling, spacing, responsive behavior, and component technology remain implementation decisions.

## Evidence

- PRODUCT-ADR-LEARNING-005 requires progressive presentation and one interaction per selected source post.
- The agreed session sketch uses answered cards followed by one active quiz card.
- Source topics may contain code blocks and long technical explanations that are not central to phrase learning.
- The product goal is phrase exposure through technical conversation context, not full technical-reading practice.
