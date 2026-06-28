# Concept: Source normalization

- **id**: `spec:product.pipeline.source_normalization`
- **status**: draft
- **date**: 2026-06-28
- **parent**: `spec:product.pipeline`

## What this is

Pipeline contract for converting accepted retained source into one source-independent authentic conversation.
The contract preserves authored content and source-observed relationships without creating Learning Paths or generated learning content.

## Non-goals

- Source-specific serialized fields as common Pipeline semantics.
- Learning Path suitability or candidate filtering.
- Generated summaries, phrases, prompts, options, or quizzes.
- Concrete parsing libraries, schemas, or identifier encodings.
- Historical normalized revisions.

## Concept model

| concept | contract |
|---|---|
| Authentic discussion | One retained technical discussion identified by the source acquisition contract. |
| Authentic post | One source-authored post with source-independent identity and evidence routing. |
| Authored text | Text attributable to the target post author after quote separation. |
| Quoted material | Referenced source material kept distinct from the target author's authored text. |
| Relationship evidence | Source-observed evidence for explicit replies, genuine topic-level responses, or unavailable explicit targets. |
| Discussion Path | A mechanically derived maximal source-structure path from the opening post to one reachable leaf. |
| Normalized authentic conversation | The current source-independent representation consumed by the Common Pipeline. |

## Rules

### Source Adapter normalization

- A Source Adapter must normalize only accepted complete retained authentic source.
- The Source Adapter must isolate source-specific fields and interpretation from the Common Pipeline.
- The normalized conversation must identify the authentic discussion and original discussion title.
- The normalized conversation must retain a source reference and attribution-relevant source metadata.
- The normalized conversation must retain routes from normalized posts to retained source evidence.

### Authentic post contract

Each normalized authentic post must contain or retain access to:

- one adapter-materialized authentic-post identity;
- complete authored text separated from quoted material;
- author identity;
- source order;
- source-observed relationship evidence;
- current retained source evidence.

- Each authentic-post identity must be unique within its authentic discussion.
- Each authentic-post identity must resolve to current retained source evidence.
- A source-native post identifier is preferred when available.
- The Common Pipeline must not require a numeric identifier, post URL, post number, or other source-native identifier form.
- Generated content must not enter the authentic-conversation model.

### Relationship distinctions

The normalized conversation must preserve these distinct source states:

| state | meaning |
|---|---|
| Explicit reply | The source records one explicit reply target. |
| Genuine topic-level response | The source records a response without an explicit reply target. |
| Unavailable explicit reply target | The source records an explicit target that retained source evidence cannot resolve. |

- A genuine topic-level response may project to the opening post for source-grounded adjacency.
- An unavailable explicit reply target must not become a topic-level response through fallback projection.
- Quote relations, textual references, and semantic similarity must not create source structure by themselves.

### Discussion Path derivation

- The Source Adapter must derive Discussion Paths mechanically.
- The Source Adapter must derive one maximal path from the opening post to each reachable leaf.
- LLM judgment must not discover or alter source topology.
- A Discussion Path is not a Learning Path.
- The Source Adapter must not create bounded Learning Path candidates.
- Posts unreachable from the opening post must not enter the normalized authentic conversation.
- Retained authentic source may preserve unreachable posts for diagnosis.

### Current normalized artifact

- One retained authentic discussion has at most one current normalized authentic-conversation artifact.
- Re-normalization replaces the current normalized artifact under the same authentic discussion identity.
- Source Adapter Version and normalization implementation are not normalized-artifact identity inputs.
- A normalization failure must preserve the complete retained authentic source.
- A normalization failure must create no normalized artifact and no candidate.
- A later compatible Source Adapter may re-normalize retained source without refetching.
- Successful normalization may produce zero Discussion Paths.
- A valid zero-path result is not a normalization failure.
- The first MVP does not retain historical normalized revisions.

## Boundary

| concern | owner |
|---|---|
| Source acquisition and retained-source acceptance | `spec:product.pipeline.source_acquisition`. |
| Source-specific normalization and authentic-conversation projection | `spec:product.pipeline.source_normalization`. |
| Bounded candidate derivation | `spec:product.pipeline.path_enumeration`. |
| Learning Path meaning and adjacency criteria | `spec:product.learning.learning_path`. |
| Identity, versions, and provenance | `spec:product.pipeline.artifact_identity_and_provenance`. |
| Retry and rerun progression | `spec:product.pipeline.orchestration`. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.pipeline` | Parent Pipeline overview. |
| `spec:product.pipeline.source_acquisition` | Supplies accepted complete retained source. |
| `spec:product.pipeline.path_enumeration` | Derives bounded candidates from maximal Discussion Paths. |
| `spec:product.pipeline.artifact_identity_and_provenance` | Defines current normalized artifact identity and behavior evidence. |
| `spec:product.learning.learning_path` | Defines Learning-owned source-grounded adjacency meaning. |
| PRODUCT-ADR-PIPELINE-006 | Establishes the source-independent normalized model and mechanical Discussion Paths. |
| PRODUCT-ADR-PIPELINE-009 | Establishes the bounded candidate boundary after normalization. |
| PRODUCT-ADR-PIPELINE-024 | Establishes normalization rerun and compatibility rules. |
