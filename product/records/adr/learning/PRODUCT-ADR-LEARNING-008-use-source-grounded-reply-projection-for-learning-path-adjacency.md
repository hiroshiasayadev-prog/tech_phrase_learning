# PRODUCT-ADR-LEARNING-008: Use source-grounded reply projection for learning-path adjacency

- **status**: accepted
- **date**: 2026-06-27
- **depends_on**: [PRODUCT-ADR-LEARNING-001, PRODUCT-ADR-LEARNING-005]
- **supersedes**: []
- **migrated_to_spec**: null

## Context

PRODUCT-ADR-LEARNING-001 establishes authentic technical conversation trees as the primary learning source.

PRODUCT-ADR-LEARNING-005 defines one learning path as an ordered sequence of connected source posts.
The accepted ADR does not define which source relationship makes adjacent posts connected.

Discourse exposes an explicit `reply_to_post_number` for some replies.
Other visible topic responses do not carry an explicit reply target.

The investigation script `scripts/fetch_post_tree.py` builds a coarse traversal tree.
The script connects an explicit reply to its referenced source post.
The script connects a response without an explicit target to the discussion opening post.

The script also falls back to the opening post when an explicit target is unavailable in the fetched set.
That fallback case must remain distinguishable from a genuine topic-level response.

The script is implementation evidence, not decision authority.
Learning requires an explicit source-independent adjacency rule before Pipeline and specification work rely on that projection.

## Decision

A valid first-MVP learning path will use source-grounded reply projection for adjacent source posts.

An adjacent post after the opening post is valid when either condition holds:

1. the source exposes an explicit reply relation to the preceding path post;
2. the source presents the post as a topic-level response, and the projection connects it to the discussion opening post.

An unavailable explicit reply target is not equivalent to a topic-level response.
The Pipeline must preserve that distinction and must not treat the unavailable-target fallback as accepted Learning adjacency without separate evidence.

A missing explicit reply target does not authorize arbitrary semantic-parent inference.

The first MVP will not create a learning-path edge solely because generated analysis considers two posts contextually related.

Quote relations, textual references, and semantic inference may remain supplemental evidence.
They do not independently establish first-MVP path adjacency under this decision.

The Learning domain owns the accepted meaning of connected adjacency.
The Pipeline owns source-specific extraction, projection, validation, and materialization mechanics.

## Rationale

Explicit reply relations preserve source-observed conversational structure.

Treating a source-level topic response as a response to the opening post supports platforms where top-level replies omit an explicit parent.
The projection retains useful discussion structure without inventing a semantic parent among later posts.

Distinguishing an unavailable explicit target prevents a data-access fallback from becoming false Learning meaning.

Rejecting content-only inferred edges reduces the risk of presenting unrelated posts as one authentic exchange.
The restriction also keeps learning-path validity reproducible from source relationships.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Require an explicit direct reply relation for every adjacent pair | Source-level topic responses without explicit targets could not form valid opening-post branches. |
| Treat an unavailable explicit target as a topic-level response | The fallback would erase a meaningful source-evidence distinction. |
| Allow Pipeline to infer arbitrary parent relations from content | Semantic inference could invent conversation structure that the source does not support. |
| Allow any posts from one discussion when the sequence reads coherently | Discussion membership alone does not preserve authentic conversational relationships. |
| Treat quote and textual-reference relations as first-MVP adjacency authorities | Their extraction and conversational meaning are not yet complete enough for the initial contract. |

## Consequences

- `spec:product.learning.learning_path` must define connected adjacency using explicit replies and topic-level opening-post projection.
- The specification must distinguish a genuine topic-level response from an unavailable explicit target.
- The specification must not depend on the concrete Discourse field name or Python implementation.
- Pipeline source adapters may map source-specific relationship fields into this semantic rule.
- Pipeline validation must reject content-only inferred adjacency for first-MVP valid paths.
- The current `fetch_post_tree.py` fallback may remain investigation code, but production projection must preserve the unavailable-target distinction.
- Quote and reference evidence may support later summarization, review, or an expanded adjacency decision.
- The accepted projection does not require an exact reconstruction of every conversational dependency.

## Evidence

- `scripts/fetch_post_tree.py` preserves explicit `reply_to_post_number` relations when the referenced post exists.
- The script projects posts without an explicit target under the opening post.
- The script currently uses the same fallback when an explicit target is unavailable in the fetched set.
- PRODUCT-INV-PIPELINE-002 identified that conflation and required the cases to remain distinguishable.
- PRODUCT-INV-PIPELINE-002 found the coarse reply projection sufficient for bounded path discovery when source-native relations remain distinguishable.
- The user adopted the source-grounded projection as the first-MVP adjacency rule and requested an explicit Learning ADR.
