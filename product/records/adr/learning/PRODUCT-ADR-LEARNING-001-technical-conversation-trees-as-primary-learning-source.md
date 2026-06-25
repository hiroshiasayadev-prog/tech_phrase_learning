# PRODUCT-ADR-LEARNING-001: Use technical conversation trees as the primary learning source

- **status**: accepted
- **date**: 2026-06-24
- **depends_on**: []
- **supersedes**: []
- **migrated_to_spec**: 2026-06-24

## Context

The product targets engineers who can already read technical English.

The main learning gap is not basic vocabulary or grammar.
The gap is repeated exposure to natural phrases in realistic context.

General native content can impose high cognitive load.
Users must understand unfamiliar culture, plot, humor, and language at the same time.

Technical discussions reduce that load.
Engineers already understand the domain, goals, and common argument patterns.

Flat phrase lists remove the context that gives a phrase its meaning.
A conversation tree preserves the relationship between a post and its replies.

## Decision

The product will use real technical conversation trees as its primary learning source.

A learning unit will preserve enough thread structure to show:

- the root post or parent comment;
- the selected reply;
- relevant ancestor context;
- sibling replies when they aid comparison;
- the phrase or response pattern under study.

The product will prioritize technical discussions about:

- software engineering;
- architecture and design;
- debugging and implementation;
- code review;
- project and team communication;
- engineering careers and workplace situations.

The product may transform source material for readability.
Transformation must preserve the original conversational intent.

The product is not a general-purpose English course.
The initial audience is engineers learning natural conversational English through familiar technical contexts.

## Rationale

Technical context lets learners focus on language instead of learning the subject at the same time.

Conversation trees expose phrases as responses to concrete situations.
The structure shows why a phrase is appropriate, not only what the phrase means.

Repeated exposure to technical conversation can provide a bridge toward broader native content.
Many useful discussion phrases also occur outside engineering contexts.

A focused audience gives the product a clear content-selection boundary.
The focus also differentiates the product from general vocabulary and grammar applications.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Use isolated phrase lists | Isolated phrases do not show conversational intent or reply relationships. |
| Start with general native media | Unfamiliar culture, plot, and slang increase cognitive load. |
| Build a general English-learning application | Broad scope would weaken content selection and product differentiation. |
| Use only technical documentation | Documentation provides limited exposure to natural conversational replies. |
| Generate all conversations with an LLM | Generated conversations would not provide direct exposure to observed native usage. |

## Consequences

- Source ingestion must preserve parent-child reply relationships.
- Content selection must favor useful technical conversations.
- Learning screens must present phrases with sufficient conversational context.
- Source licensing and attribution require explicit investigation.
- The product may later expand beyond technical content after validating the initial learning model.
- Generated content can supplement source material but cannot replace real conversation as the primary source.

## Evidence

- Engineers can understand technical situations before they know the natural English phrasing.
- Technical discussions contain reusable agreement, disagreement, clarification, and evaluation phrases.
- Conversation context explains phrase intent more effectively than isolated definitions.
- The initial product idea emerged from difficulty consuming native media despite comfortable technical reading.
