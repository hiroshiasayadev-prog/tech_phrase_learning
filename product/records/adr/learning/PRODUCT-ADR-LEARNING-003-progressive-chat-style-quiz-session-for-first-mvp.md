# PRODUCT-ADR-LEARNING-003: Use a progressive chat-style quiz session for the first MVP

- **status**: superseded
- **date**: 2026-06-24
- **depends_on**: [PRODUCT-ADR-LEARNING-001, PRODUCT-ADR-LEARNING-002]
- **supersedes**: []
- **migrated_to_spec**: 2026-06-24

## Context

The first MVP needs a simple path from entry to repeated phrase exposure.

A single isolated quiz would not preserve conversation progression.
Showing every quiz upfront would expose later context before earlier replies are revealed.

The product uses reply relationships as learning context.
A chat-style presentation can make that progression visible without showing an entire source topic.

The introduction also needs a minimal starting action.
Source selection would add controls without value while the MVP uses one initial corpus.

## Decision

The first MVP will use two learner-facing pages:

1. an introduction page;
2. a chat-style learning session page.

The introduction page will provide one random-start action.
The first MVP will not provide source selection.

The learning session will follow one coherent source conversation branch.
The session will reveal the branch progressively.

Each quiz step will use this sequence:

1. show the accumulated context and revealed conversation turns;
2. show one generated phrase-oriented reply quiz;
3. wait for the learner's selection;
4. show the result and concise option explanations;
5. reveal the corresponding authentic source turn;
6. append the source turn to the visible chat;
7. unlock the next quiz step.

A later quiz must remain hidden until the previous quiz step is complete.
The revealed source turn becomes context for the next quiz.

Not every source turn must become a quiz.
A source turn may provide context without requiring learner input.

The chat-style UI represents a guided source conversation.
The first MVP will not simulate unrestricted live chat with generated participants.

The session will finish with source attribution and a next-random-conversation action.

## Rationale

Progressive reveal preserves the causal order of the conversation.
The learner can judge each reply using only the context available at that moment.

Appending authentic turns lets the visible chat gradually become the real source conversation.
The separation keeps generated quiz abstractions distinct from authentic source text.

A chat-style presentation matches the reply-based learning model.
The presentation also avoids exposing the complexity of the complete source thread.

A random-start introduction keeps the MVP entry flow small.
The product can add source selection after multiple useful corpora exist.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Show one isolated quiz per session | The learner would not experience conversational progression. |
| Show all quizzes when the page opens | Later prompts would reveal context and weaken sequential judgment. |
| Show the complete source conversation before quizzing | The authentic replies would disclose the quiz answers. |
| Start with source selection | One initial corpus does not justify the added interaction and state. |
| Simulate unrestricted generated chat | Generated conversation would replace the authentic source branch. |
| Make every source turn a quiz | Some turns only provide context and do not offer a useful phrase decision. |

## Consequences

- A learning unit must preserve the ordered quiz and reveal sequence.
- Each quiz step must reference the source turn revealed after selection.
- The UI must retain accumulated chat state during a session.
- Later quiz steps depend on completion of earlier steps.
- The package schema must distinguish generated quiz content from authentic source turns.
- The package schema must mark context-only and quiz-bearing turns.
- Account, progress history, source filters, and difficulty filters remain outside the first MVP.
- Exact layout, styling, and component technology remain implementation decisions.

## Evidence

- Reply meaning depends on the conversation state that precedes it.
- Later source replies often respond directly to earlier revealed turns.
- The learner intends to see authentic content after selecting a generated phrase-oriented option.
- A chat-style sequence can present several related quizzes without exposing later replies early.
