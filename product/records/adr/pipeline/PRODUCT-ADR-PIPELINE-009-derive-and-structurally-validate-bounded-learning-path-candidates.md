# PRODUCT-ADR-PIPELINE-009: Derive and structurally validate bounded Learning Path candidates

- **status**: accepted
- **date**: 2026-06-28
- **depends_on**:
  - PRODUCT-ADR-PIPELINE-006
  - PRODUCT-ADR-PIPELINE-007
  - PRODUCT-ADR-PIPELINE-008
  - PRODUCT-ADR-LEARNING-005
  - PRODUCT-ADR-LEARNING-007
  - PRODUCT-ADR-LEARNING-008
- **supersedes**:
- **migrated_to_spec**: 2026-06-28

## Context

PRODUCT-ADR-PIPELINE-006 requires each Source Adapter to emit maximal mechanical Discussion Paths.
The common Pipeline must derive bounded Learning Path candidates without redefining source structure.

The Learning contract requires each valid path to:

- contain two to six posts;
- begin with the discussion opening post;
- preserve source order;
- use source-grounded adjacency;
- remain distinct from sibling paths without canonical-path selection.

The Pipeline still needs deterministic candidate derivation, duplicate handling, structural rejection outcomes, and retained derivation evidence.

## Decision

### Bounded candidate derivation

Each maximal Discussion Path will yield at most one bounded Learning Path candidate.

| maximal Discussion Path size | derivation outcome |
|---|---|
| Fewer than two posts | Produce no candidate. |
| Two through six posts | Preserve the complete ordered path as one candidate. |
| More than six posts | Preserve only the first six ordered posts as one candidate. |

The first MVP will not enumerate every intermediate prefix.
It will not use semantic judgment to split one Discussion Path into shorter candidates.

Candidate enumeration will use lexicographic order over ordered source positions.
When a prefix relation exists, the shorter sequence will appear first.
Enumeration order will not express validity, ranking, preference, or publication priority.

### Candidate identity and duplicate handling

Candidate identity will use:

- the authentic discussion identity;
- the ordered authentic-post identities in the bounded candidate.

Candidates with identical identity inputs will merge before structural validation and semantic processing.
Differences that occur only after the retained first six posts will not preserve duplicate candidates.

Prefix-overlapping but non-identical ordered sequences will remain distinct candidates.
Summaries, phrase evidence, evaluator output, model identity, and prompt version will not affect candidate or valid-path identity.

When several maximal Discussion Paths collapse into one candidate, the Pipeline will retain every originating maximal ordered authentic-post sequence.
It will also retain whether bounding removed later posts from each origin.
Origin evidence will not affect identity and will not become learner-facing content.

### Structural validation

Every candidate will receive deterministic structural validation before semantic processing.

Validation will establish all of these conditions:

- all posts belong to one authentic discussion;
- the first post is the authentic discussion opening post;
- the candidate contains two through six posts;
- source order is preserved;
- each authentic-post identity resolves to retained source evidence;
- no authentic-post identity appears more than once;
- every adjacent pair has retained source relationship evidence;
- every adjacent pair satisfies the accepted source-grounded adjacency contract.

The Pipeline will not repair a repeated-post candidate by deleting posts.

Each adjacent pair will retain:

- the ordered endpoint identities;
- whether the edge is an explicit reply or a genuine topic-level response projected to the opening post;
- the authentic explicit target identity when an explicit target exists.

A genuine topic-level response may project to the opening post.
An unavailable explicit reply target will not fall back to opening-post projection.

### Structural rejection evidence

A candidate with any structural failure will become a structural rejection and will not enter semantic processing.

Structural rejection will use these controlled reasons:

| reason | meaning |
|---|---|
| `invalid_discussion_scope` | Candidate posts do not belong to one authentic discussion. |
| `invalid_opening_post_start` | The candidate does not begin with the authentic opening post. |
| `invalid_cardinality` | The candidate reaching validation does not contain two through six posts. |
| `invalid_source_order` | Candidate order does not preserve source conversation order. |
| `invalid_adjacency` | An adjacent pair lacks an accepted source-grounded relation. |
| `unavailable_explicit_reply_target` | An explicit target cannot resolve and cannot use opening-post fallback. |
| `unresolved_post_identity` | A candidate post identity does not resolve to retained source evidence. |
| `missing_relationship_evidence` | Required source relationship evidence is absent. |
| `repeated_post` | One authentic-post identity appears more than once. |

The Pipeline will retain all detected structural reasons.
Each structural rejection will retain candidate identity and the relevant authentic-post identities.
Run-level counts may be derived from candidate-level outcomes.

Concrete graph algorithms, data structures, identifier encodings, and persistence layouts remain implementation choices.

## Rationale

One bounded candidate per maximal Discussion Path avoids redundant prefix expansion.
It also keeps the first-MVP candidate set understandable and deterministic.

Truncating after the sixth post preserves the Learning-owned cardinality without discarding the complete source discussion evidence.

Identity based on authentic ordered posts keeps duplicate handling stable across model and prompt changes.
Origin evidence explains why several source branches produced one bounded candidate without changing its logical identity.

Deterministic structural validation prevents a model verdict from inventing or repairing source topology.
Distinct relationship evidence preserves the accepted boundary between explicit replies, genuine topic-level responses, and unavailable targets.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Enumerate every two-to-six-post prefix | It creates redundant candidates and was not the intended first-MVP path derivation. |
| Drop every Discussion Path longer than six posts | The first six posts may still provide a bounded candidate. |
| Use semantic judgment to choose a cut point | Semantic segmentation requires separate fixtures and is deferred beyond the first MVP. |
| Preserve duplicates when later leaves differ | Candidate inputs and resulting path identity are identical after bounding. |
| Repair repeated posts by deletion | Repair would create a sequence not emitted by source derivation. |
| Infer adjacency from content similarity | Learning requires source-grounded adjacency rather than model-created edges. |
| Fall back to the opening post for unavailable explicit targets | This would misclassify an unresolved explicit reply as a genuine topic-level response. |
| Include generated evidence in path identity | Regeneration would create new logical paths from unchanged source structure. |

## Consequences

- Source Adapters continue to emit maximal mechanical Discussion Paths.
- The common Pipeline owns bounded derivation, duplicate merging, and structural validation.
- Semantic filtering consumes only structurally valid candidates.
- PRODUCT-ADR-PIPELINE-007 remains the authority for valid-path and Learning Unit identity.
- PRODUCT-ADR-PIPELINE-008 remains the authority for versioned current provenance.
- T04 may consume retained candidates without reconstructing path bounds or adjacency.
- T06 may define execution, batching, and operational retry behavior without changing structural outcomes.
- T07 must reflect candidate derivation, structural reasons, edge evidence, and origin provenance into focused Pipeline specifications.
- Exact graph traversal, in-memory representation, storage schema, and implementation technology remain deferred.

## Evidence

- PRODUCT-ADR-PIPELINE-006 establishes maximal mechanical Discussion Paths and the common-Pipeline candidate boundary.
- PRODUCT-ADR-LEARNING-007 establishes the two-to-six-post first-MVP cardinality.
- PRODUCT-ADR-LEARNING-008 establishes source-grounded adjacency and unavailable-target semantics.
- PRODUCT-ADR-PIPELINE-007 establishes source-only ordered path identity.
- PRODUCT-ADR-PIPELINE-008 establishes retained Pipeline provenance.
- PRODUCT-INV-PIPELINE-002 provides reviewed path and invalid-control fixtures as non-normative evidence.
- The user selected one candidate per maximal Discussion Path, first-six-post bounding, exact duplicate merging, deterministic structural rejection, and retained origin and edge evidence.
