# Concept: Learning Path candidate enumeration

- **id**: `spec:product.pipeline.path_enumeration`
- **status**: draft
- **date**: 2026-06-28
- **parent**: `spec:product.pipeline`

## What this is

Pipeline contract for deriving bounded Learning Path candidates from maximal mechanical Discussion Paths.
The contract owns deterministic candidate production, identity, duplicate handling, and origin evidence.

## Non-goals

- Learning Path suitability meaning.
- Semantic segmentation or sibling ranking.
- Graph traversal implementation or in-memory representation.
- Structural or semantic acceptance decisions.
- Runtime Learning Unit selection.

## Concept model

| concept | contract |
|---|---|
| Maximal Discussion Path | Source-normalized path from the opening post to one reachable leaf. |
| Bounded candidate | One ordered two-to-six-post sequence derived from one maximal Discussion Path. |
| Candidate identity | Authentic discussion identity plus ordered authentic-post identities. |
| Exact duplicate | Two candidates with identical candidate identity inputs. |
| Origin evidence | Every maximal ordered source path that produced one merged candidate. |

## Rules

### Candidate derivation

Each maximal Discussion Path yields at most one bounded candidate.

| maximal path size | result |
|---|---|
| Fewer than two posts | Produce no candidate. |
| Two through six posts | Preserve the complete ordered path as one candidate. |
| More than six posts | Preserve the first six ordered posts as one candidate. |

- The first MVP must not enumerate every intermediate prefix.
- The first MVP must not use semantic judgment to choose a cut point.
- The first MVP must not split one maximal Discussion Path into several semantic segments.
- Prefix-overlapping but non-identical candidates may coexist.

### Deterministic order

- Candidate enumeration must use lexicographic order over ordered source positions.
- A shorter sequence must appear before its longer sequence when one is a prefix of the other.
- Enumeration order must not express validity, ranking, preference, or publication priority.

### Identity and duplicate handling

- Candidate identity must use the authentic discussion identity and ordered authentic-post identities.
- Candidate identity must remain independent from summaries, phrase evidence, model output, provider identity, prompt versions, and evaluator results.
- Candidates with identical identity inputs must merge before structural validation.
- Differences after the retained first six posts must not preserve duplicate candidates.
- Prefix-overlapping candidates with different ordered identities must remain distinct.

### Origin evidence

When several maximal Discussion Paths merge into one candidate, the Pipeline must retain:

- every originating maximal ordered authentic-post sequence;
- whether bounding removed later posts from each origin;
- the merged candidate identity.

- Origin evidence must not affect candidate identity.
- Origin evidence must remain Pipeline-internal.
- Origin evidence must not become learner-visible content.

## Boundary

| concern | owner |
|---|---|
| Maximal Discussion Path derivation | `spec:product.pipeline.source_normalization`. |
| Candidate derivation, identity, duplicates, and origin evidence | `spec:product.pipeline.path_enumeration`. |
| Structural and semantic acceptance | `spec:product.pipeline.path_validation`. |
| Valid-path identity retention and stable Learning Unit materialization | `spec:product.pipeline.artifact_identity_and_provenance`. |
| Learning-owned path meaning | `spec:product.learning.learning_path`. |
| Concrete traversal algorithm | Implementation. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.pipeline` | Parent Pipeline overview. |
| `spec:product.pipeline.source_normalization` | Supplies maximal mechanical Discussion Paths. |
| `spec:product.pipeline.path_validation` | Consumes bounded candidates. |
| `spec:product.pipeline.artifact_identity_and_provenance` | Retains accepted candidate identity as valid-path identity and materializes stable Learning Unit identity. |
| `spec:product.learning.learning_path` | Defines accepted path cardinality and adjacency meaning. |
| PRODUCT-ADR-PIPELINE-006 | Establishes maximal Discussion Paths. |
| PRODUCT-ADR-PIPELINE-007 | Establishes ordered-post path identity. |
| PRODUCT-ADR-PIPELINE-009 | Establishes first-six bounding, duplicate merging, and origin evidence. |
