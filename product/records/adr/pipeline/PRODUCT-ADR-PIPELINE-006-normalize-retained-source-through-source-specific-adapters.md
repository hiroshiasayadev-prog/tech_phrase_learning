# PRODUCT-ADR-PIPELINE-006: Normalize retained source through source-specific adapters

- **status**: accepted
- **date**: 2026-06-27
- **depends_on**:
  - PRODUCT-ADR-PIPELINE-005
  - PRODUCT-ADR-LEARNING-008
- **supersedes**:
- **migrated_to_spec**: 2026-06-28

## Context

PRODUCT-ADR-PIPELINE-005 establishes retained-source reuse and deterministic source processing.

Source platforms expose different identifiers, reply fields, quote formats, and retrieval shapes.
The common Pipeline must not depend on Discourse-specific fields.

PRODUCT-ADR-LEARNING-008 requires source-grounded adjacency.
The Pipeline must distinguish a genuine topic-level response from an unavailable explicit reply target.

The first MVP also needs clear outcomes for incomplete fetches, normalization failures, and conversations without usable paths.

## Decision

The Pipeline will use source-specific adapters before common processing.

The first-MVP adapter will support eligible Packaging discussions from `discuss.python.org`.
Future adapters may support other technical-discussion platforms without changing the common authentic-conversation model.

### Source acquisition and retention

The first MVP will periodically crawl eligible discussion listings to discover canonical discussion URLs.

The canonical discussion URL identifies one retained authentic discussion.

| acquisition condition | outcome |
|---|---|
| No retained source exists and the complete discussion fetch succeeds | Establish retained authentic source and continue to normalization. |
| Retained source already exists for the canonical URL | Reuse the retained source without refetching. |
| The initial fetch is partial, unavailable, or failed | Do not establish retained source and do not continue to normalization. |

The first MVP will not provide an explicit source-refresh operation.
The first MVP will not detect later source changes.
Source freshness is not part of the learning-content contract.

### Source-independent normalized model

A source adapter will map retained source records into one source-independent authentic conversation.

The normalized conversation will contain:

- the authentic discussion identity;
- the authentic discussion title;
- a source reference;
- source metadata required for attribution and current diagnosis;
- authentic posts;
- one adapter-materialized identity for each authentic post;
- authored text separated from quoted material;
- author identity;
- source order;
- source-observed relationship evidence;
- mechanically derived maximal Discussion Paths;
- routes from normalized posts to retained source evidence.

Each authentic-post identity must be unique within its retained discussion.
Each authentic-post identity must resolve to current retained source evidence.

A source-native post identifier is preferred when available.
The common Pipeline contract will not require a source-native identifier, numeric identifier, post URL, or post number.

The adapter must preserve the distinction between:

- an explicit source reply relation;
- a genuine topic-level response;
- an explicit reply target that is unavailable in retained source evidence.

An unavailable explicit target must not become a topic-level response through fallback projection.

Generated summaries, prompts, target phrases, and quiz content remain outside the authentic-conversation model.

### Discussion Path boundary

A Discussion Path is a mechanically derived source-structure path.
A Discussion Path is not a Learning Path.

The source adapter will derive maximal paths from the opening post to each reachable leaf.
The adapter will not use LLM judgment to discover source structure.

Posts that are not reachable from the opening post will not enter the normalized authentic-conversation model.
The retained authentic source may preserve those posts for diagnosis.

The common Pipeline will derive bounded Learning Path candidates from Discussion Paths.
The common Pipeline may derive prefixes without changing the adapter output contract.

### Current normalized artifact

One retained authentic discussion has at most one current normalized authentic-conversation artifact.

Re-normalization replaces the current normalized artifact under the same authentic discussion identity.
Source Adapter Version and normalization implementation are not normalized-artifact identity inputs.
The first MVP will not retain historical normalized revisions.

A normalization failure will preserve the complete retained authentic source.
A normalization failure will create no normalized artifact and no Learning Unit candidate.
A later Source Adapter Version may re-normalize the retained source without refetching.

Successful normalization may produce zero Discussion Paths or zero Learning Path candidates.
That outcome is valid and creates no Learning Unit.

## Rationale

Source-specific adapters isolate platform fields and parsing behavior from common Pipeline semantics.

Canonical URL retention prevents unnecessary source requests.
The first MVP does not gain learning value from tracking later source edits.

Best-effort post identity supports platforms without stable source-native post identifiers.
The required uniqueness and evidence route remain sufficient for current processing.

Mechanical Discussion Path derivation keeps source structure deterministic.
It also prevents LLM context limits from defining conversation topology.

Separating acquisition success from normalization success preserves reusable authentic source after adapter defects.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Require one source-native post ID contract for every platform | Some platforms may not expose a stable post identifier in the required form. |
| Expose Discourse fields to the common Pipeline | Source-specific representation would become common Pipeline semantics. |
| Refetch every known discussion | Repeated requests consume source capacity without improving first-MVP learning value. |
| Treat partial fetches as retained source | Missing posts or relations could create false Discussion Paths. |
| Use LLMs to discover conversation structure | Structural discovery must remain deterministic and independent of model context limits. |
| Collapse unavailable reply targets into topic-level responses | The fallback would violate accepted source-grounded adjacency. |
| Discard retained source after normalization failure | Adapter fixes would require unnecessary source refetching. |
| Treat zero candidates as normalization failure | A valid authentic conversation may contain no first-MVP learning opportunity. |

## Consequences

- Source adapters own source-specific fetching interpretation, quote parsing, relationship extraction, and normalized post identity materialization.
- The common Pipeline consumes the source-independent authentic-conversation model.
- Source adapters do not create Learning Paths or Learning Unit candidates.
- T03 may define bounded prefix enumeration and duplicate handling from maximal Discussion Paths.
- T06 may define acquisition retry and orchestration policy.
- T07 must reflect source acquisition and normalization contracts into focused Pipeline specifications.
- Exact schemas, identifier encodings, parsing libraries, storage technology, and network clients remain implementation choices.

## Evidence

- PRODUCT-TASK-PIPELINE-001-01 identified source acquisition and normalization as missing Pipeline authority.
- `scripts/fetch_post_tree.py` demonstrates deterministic tree projection but conflates unavailable targets with topic-level responses.
- PRODUCT-ADR-LEARNING-008 requires the unavailable-target distinction.
- The user selected canonical-URL retention without refetch or explicit refresh.
- The user selected source-specific adapters and best-effort authentic-post identity.
- The user selected maximal mechanical Discussion Paths and common-Pipeline prefix derivation.
- The user selected complete-fetch-only retention and retained-source preservation after normalization failure.
