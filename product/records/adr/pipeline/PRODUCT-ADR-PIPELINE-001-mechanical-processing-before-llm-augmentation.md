# PRODUCT-ADR-PIPELINE-001: Prefer mechanical processing before LLM augmentation

- **status**: superseded
- **date**: 2026-06-24
- **depends_on**: [PRODUCT-ADR-LEARNING-001]
- **supersedes**: []
- **migrated_to_spec**: 2026-06-24

## Context

Technical conversation sources contain structured and unstructured data.

Thread relationships, author identifiers, timestamps, scores, links, and code blocks are mechanically observable.
Phrase usefulness, nuance, and learning difficulty require semantic judgment.

Sending complete source threads directly to an LLM would increase cost and reduce reproducibility.
The approach would also make deterministic failures difficult to diagnose.

Small local models and cheap hosted APIs may be sufficient for bounded semantic tasks.
Their output quality and structured-output reliability will vary.

## Decision

The content pipeline will use deterministic processing before LLM augmentation.

Mechanical processing will own tasks with explicit rules or source structure.

Examples, not exhaustive:

- parse source records;
- preserve reply-tree relationships;
- remove markup and redundant quoting;
- detect code blocks and links;
- normalize whitespace;
- enforce length and score thresholds;
- remove duplicates;
- apply source and language filters;
- produce stable candidate identifiers.

LLM processing will own bounded tasks that require semantic interpretation.

Examples, not exhaustive:

- classify phrase usefulness;
- identify reusable phrase patterns;
- explain conversational nuance;
- estimate learning difficulty;
- draft distractors and quiz explanations;
- perform limited readability cleanup.

Each LLM task will receive the smallest sufficient context.
Each task will define a structured output contract when practical.

Application code will validate LLM output.
Invalid output will be retried, rejected, or sent to review.

The pipeline must retain intermediate mechanical and LLM-derived artifacts.
The retained artifacts must support diagnosis and later reprocessing.

## Rationale

Mechanical processing is cheaper, faster, reproducible, and easy to test.
It should handle every task that does not require semantic judgment.

Bounded LLM tasks reduce token use and model requirements.
The boundary makes small local models and cheap hosted APIs practical.

Intermediate artifacts make pipeline behavior observable.
They also allow new models or prompts to reprocess existing candidates without re-ingestion.

Structured validation prevents model output from becoming an implicit source of truth.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Send complete threads to one large prompt | Cost, reproducibility, and failure diagnosis would be poor. |
| Use only deterministic rules | Rules cannot reliably judge nuance, phrase usefulness, or plausible distractors. |
| Use an LLM for parsing and normalization | Source structure and text cleanup do not require model inference. |
| Publish LLM output without validation | Model variance would create malformed or misleading learning content. |
| Require human authoring for every item | Manual-only production would prevent useful content scale. |

## Consequences

- The pipeline requires explicit stages and persisted intermediate forms.
- Deterministic stages require unit and fixture tests.
- LLM stages require schemas, prompts, and quality evaluation.
- Content can be reprocessed after model or prompt changes.
- Human review may remain necessary for uncertain or high-impact items.
- Pipeline complexity is higher than a single-prompt prototype.
- The separation supports later comparison between local and hosted models.

## Evidence

- Conversation sources expose reply structure without semantic inference.
- Text cleanup and candidate filtering can be expressed with deterministic rules.
- Phrase usefulness and nuance depend on conversational meaning.
- Bounded classification and generation tasks fit smaller models better than complete pipeline execution.
- Retained intermediate artifacts allow failures to be attributed to a specific stage.
