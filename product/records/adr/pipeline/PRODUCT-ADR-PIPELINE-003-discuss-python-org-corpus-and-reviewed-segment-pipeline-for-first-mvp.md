# PRODUCT-ADR-PIPELINE-003: Use discuss.python.org and a reviewed segment pipeline for the first MVP

- **status**: superseded
- **date**: 2026-06-24
- **depends_on**: [PRODUCT-ADR-LEARNING-001, PRODUCT-ADR-LEARNING-002, PRODUCT-ADR-PIPELINE-001, PRODUCT-ADR-PIPELINE-002]
- **supersedes**: []
- **migrated_to_spec**: 2026-06-24

## Context

The first MVP needs a source with sustained technical conversation.
The source must provide enough local context to understand each discussion.

Stack Overflow usually provides short problem-and-answer exchanges.
GitHub pull requests often contain summaries, review requests, bot replies, or no discussion.
Hacker News frequently depends on an external article that requires separate retrieval and summarization.

Python Discussions contains opening posts, replies, quotations, and explicit reply relationships.
The technical domain is also familiar to the initial learner audience.

The source still contains long topics, code-heavy replies, external references, and incomplete branches.
The pipeline must therefore find coherent segments before LLM augmentation.

## Decision

The first MVP will use public topics from `discuss.python.org` as its initial corpus.

Initial topic selection will prefer self-contained technical design discussions.
The Packaging category will be the first collection scope.
Other categories may be added after the first corpus is evaluated.

The first MVP pipeline will use these stages:

1. discover eligible topics;
2. fetch and retain immutable source snapshots;
3. normalize posts without changing source wording;
4. reconstruct explicit reply and reference relationships;
5. extract short conversation-segment candidates;
6. reject unsuitable candidates with deterministic rules;
7. augment retained candidates with bounded LLM tasks;
8. validate source fidelity and structured output;
9. send candidates to human review;
10. publish only accepted learning units.

Mechanical stages will own source retrieval, relationship reconstruction, cleanup, candidate identity, and rule-based filtering.

LLM stages will own semantic tasks requiring interpretation.

Examples, not exhaustive:

- context-capsule generation;
- dialogue-act classification;
- useful phrase extraction;
- phrase-function explanation;
- difficulty estimation;
- missing-context detection.

The pipeline will treat a conversation segment as a derived artifact.
The source topic and source posts will remain separate immutable records.

Each derived artifact will retain source references, pipeline version, model identity, and prompt version.
The pipeline will support regeneration without retrieving unchanged source content again.

The first MVP will target a manually reviewed corpus before automated publication.
The initial validation target will be 50 to 100 accepted conversation segments.

## Rationale

Python Discussions reduces dependency on external articles.
The opening post usually provides the discussion context directly.

A Discourse source exposes structured post and reply data.
Mechanical reconstruction is therefore more reliable than asking an LLM to infer thread structure.

Short conversation segments match the learning unit selected by PRODUCT-ADR-LEARNING-002.
The segments also bound model input and review effort.

Immutable source snapshots preserve provenance.
Versioned derived artifacts support diagnosis and reprocessing.

Human review provides evidence for later filters, prompts, schemas, and model evaluation.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Start with Stack Overflow | Most threads do not provide sustained conversational exchange. |
| Start with GitHub pull requests | Meaningful human conversations are difficult to discover reliably. |
| Start with Hacker News | Many discussions require an external article for essential context. |
| Send complete topics directly to an LLM | Cost, reproducibility, and source-relationship accuracy would be poor. |
| Store only final learning units | Lost intermediate artifacts would prevent diagnosis and regeneration. |
| Publish automatically after LLM augmentation | Early annotation quality is not yet established. |

## Consequences

- The first source adapter targets Discourse topic and post structures.
- Source-specific fields must not become the source-independent domain model.
- The implementation requires raw snapshots, normalized posts, relationships, segments, annotations, and review results.
- Exact filtering thresholds require implementation evidence and belong in pipeline specifications.
- Source licensing, attribution, retention, and redistribution require a separate explicit decision or investigation.
- The first MVP measures extraction and review quality before content-production scale.
- Adding another source requires a new adapter, not a rewrite of learning semantics.

## Evidence

- Python Discussions provides self-contained opening posts followed by technical replies.
- Discussion branches contain clarification, disagreement, revisions, and alternative proposals.
- Discourse exposes explicit reply relationships and structured post content.
- The target learner already understands Python and software-engineering concepts.
- Mechanical filtering can remove code-heavy, link-dependent, and context-incomplete candidates before model use.
