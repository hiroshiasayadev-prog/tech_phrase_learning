# PRODUCT-TASK-PIPELINE-001-03: Define path enumeration, validation, and filtering contracts

- **id**: PRODUCT-TASK-PIPELINE-001-03
- **status**: done
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PIPELINE-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 2d
- **depends_on**:
  - PRODUCT-TASK-PIPELINE-001-02
- **outputs**:
  - PRODUCT-ADR-PIPELINE-009
  - PRODUCT-ADR-PIPELINE-010

## Goal

Define deterministic path enumeration, structural validation, independent suitability filtering, and retained rejection evidence.

## Work

1. Read T01 gaps, accepted T02 ADRs, and the fixed Learning path contract.
2. Define enumeration inputs from normalized posts and preserved relationship evidence.
3. Define deterministic adjacency handling for explicit replies and genuine topic-level response projection.
4. Reject opening-post fallback when an explicit target is unavailable.
5. Define two-to-six path bounds without re-deciding their Learning meaning.
6. Define deterministic enumeration order, path identity, duplicate handling, and prefix-overlap coexistence.
7. Define enumeration outputs and the distinction between candidates, structurally valid paths, and retained valid paths.
8. Define structural checks for discussion scope, opening-post start, order, adjacency, cardinality, identity, and required evidence.
9. Define semantic suitability-filter inputs for coherence and per-post quiz suitability.
10. Require absolute candidate judgment without sibling ranking or canonical-path selection.
11. Define rejection outcomes and retained rejected evidence for diagnosis and gate development.
12. Separate deterministic checks from model-based semantic evaluation.
13. Create or update Pipeline ADRs when current accepted authority does not determine observable semantics.
14. Keep graph algorithms, data structures, thresholds, and model choices outside the contract.
15. Update `outputs` and Evidence with accepted ADRs or specification inputs.

## Done condition

- Enumeration inputs and outputs are explicit.
- Explicit replies, topic-level responses, and unavailable-target cases remain distinguishable.
- Enumeration is deterministic and bounded to Learning-owned cardinality.
- Stable path identity, duplicates, and prefix-overlap behavior are explicit.
- Structural validation is separate from semantic suitability filtering.
- Coherence and per-post quiz suitability consume Learning meaning without redefining it.
- Each candidate is judged independently.
- Rejection outcomes and retained evidence are explicit.
- Every new normative decision has accepted Pipeline ADR authority.
- T04 through T07 can consume the resulting path contracts without algorithm reconstruction.

## Verification

- Test the contract against the reviewed topic `107565` path variants and invalid controls as evidence.
- Confirm no canonical path is selected during ingestion.
- Confirm a shorter or higher-ranked sibling is not a rejection reason.
- Confirm path identity does not depend on generated phrase, quiz, summary, or model output.
- Confirm deterministic validation cannot be replaced by a model-only result.
- Confirm no concrete graph implementation or threshold enters the design contract.
- Run relevant record validation, strict specification validation, `git diff --check`, and `git status --short`.

## Evidence

### Execution boundary

- T03 is `done`.
- User-approved decisions are materialized in accepted Pipeline ADRs.
- Task Evidence is not normative authority.
- No normative specification changed in T03.
- T04 through T06 ownership remains unchanged.

### Accepted ADR authority

| ADR | authority established |
|---|---|
| PRODUCT-ADR-PIPELINE-009 | One-candidate bounding, deterministic ordering, duplicate merging, source-only identity, structural validation, edge evidence, origin provenance, and structural rejection reasons. |
| PRODUCT-ADR-PIPELINE-010 | Independent semantic evaluation units, minimal context, positive evidence, bounded invalid-output retry, full evaluation, terminal outcomes, and deterministic aggregation. |

### Decision register

The register preserves the user-approved choices materialized in accepted Pipeline ADRs.
Task Evidence is not normative authority.

| sequence | decision | status | accepted ADR |
|---|---|---|---|
| D01 | Each maximal Discussion Path yields at most one bounded candidate. Paths with fewer than two posts yield no candidate. Paths with two to six posts remain unchanged. For longer paths, the candidate retains the first six ordered posts and excludes the seventh and later posts. Intermediate prefixes are not enumerated. | materialized | PRODUCT-ADR-PIPELINE-009 |
| D02 | Candidate enumeration uses lexicographic order over ordered source positions. When one candidate is a prefix of another, the shorter candidate appears first. Enumeration order carries no validity, ranking, or priority meaning. | materialized | PRODUCT-ADR-PIPELINE-009 |
| D03 | The first MVP does not semantically segment one bounded candidate into shorter candidates. It evaluates the complete candidate after required summaries and phrase evidence exist. An incoherent candidate is rejected as a whole. Semantic boundary detection and prefix salvage are deferred. | materialized | PRODUCT-ADR-PIPELINE-010 |
| D04 | Candidates with the same authentic discussion identity and identical ordered authentic-post identities are merged before structural validation and semantic processing. Candidate-external leaf differences do not preserve duplicates. Prefix-overlapping but non-identical candidates remain distinct. | materialized | PRODUCT-ADR-PIPELINE-009 |
| D05 | A candidate containing the same authentic-post identity more than once is structurally rejected. The Pipeline does not repair the candidate by deleting repeated posts. The rejection records the repeated post identity and does not enter semantic processing. | materialized | PRODUCT-ADR-PIPELINE-009 |
| D06 | Final path-filtering outcomes distinguish structural rejection, semantic suitability rejection, semantic evaluation failure, and retained valid Learning Path. Enumerated and structurally valid candidates are observable processing states rather than retained final outcomes. | materialized | PRODUCT-ADR-PIPELINE-010 |
| D07 | Each non-retained candidate retains candidate-level evidence consisting of candidate identity, outcome stage, controlled reason or failure category, and relevant authentic-post identities. Run-level counts are derived from candidate records. Raw model requests and responses are not required. | materialized | PRODUCT-ADR-PIPELINE-009, PRODUCT-ADR-PIPELINE-010 |
| D08 | Structural rejection uses controlled reason codes for distinct contract failures. All detected structural reasons are retained, and any structural rejection prevents semantic processing. | materialized | PRODUCT-ADR-PIPELINE-009 |
| D09 | Semantic suitability rejection uses `incoherent_path`, `unsuitable_opening_post`, and `unsuitable_reply_post`. Evaluator instructions explain these meanings and independent absolute judgment, while concrete prompt wording remains outside the ADR. | materialized | PRODUCT-ADR-PIPELINE-010 |
| D10 | Invalid, incomplete, contradictory, or uncovered evaluator output is evaluation failure rather than semantic rejection. Each independent unit has one initial attempt and at most two invalid-output retries. Valid pass or rejection is not retried. | materialized | PRODUCT-ADR-PIPELINE-010 |
| D11 | Semantic suitability uses one path-coherence evaluation, one opening-post question-suitability evaluation, and one reply-suitability evaluation for each later post. Deterministic aggregation requires every unit to pass. | materialized | PRODUCT-ADR-PIPELINE-010 |
| D12 | Every required semantic unit executes after structural success, even after another unit returns a valid failure. All semantic failures and relevant post identities are retained. | materialized | PRODUCT-ADR-PIPELINE-010 |
| D13 | Each semantic evaluation receives only its required context. Coherence sees the complete summaries, opening suitability sees the opening evidence, and each reply sees summaries through itself plus its own phrase evidence. | materialized | PRODUCT-ADR-PIPELINE-010 |
| D14 | Every semantic pass retains positive evidence. Deterministic validation rejects missing coverage, foreign posts, wrong roles, invented phrase evidence, and contradictory output as evaluation failure. Positive phrase evidence does not select final learner-facing content. | materialized | PRODUCT-ADR-PIPELINE-010 |
| D15 | Learning Path identity depends only on authentic discussion identity and ordered authentic-post identities. Generated and evaluation output does not create a new path identity. | materialized | PRODUCT-ADR-PIPELINE-009 |
| D16 | When bounding and duplicate merging collapse several maximal Discussion Paths, every origin sequence and truncation fact remains internal provenance without affecting identity or semantic input. | materialized | PRODUCT-ADR-PIPELINE-009 |
| D17 | Every adjacent pair retains explicit-reply or genuine topic-level-response evidence. An unavailable explicit target is structurally rejected and cannot fall back to opening-post projection. | materialized | PRODUCT-ADR-PIPELINE-009 |
| D18 | Structural rejection takes precedence. Otherwise valid semantic failures produce semantic rejection, exhausted evaluator failures remain supplemental when mixed, evaluation failure is terminal when no semantic failure exists, and complete passes retain a valid path. | materialized | PRODUCT-ADR-PIPELINE-010 |

### Authoring verification

- Manual readback confirmed unique ADR IDs, matching H1 identifiers, required metadata, required body sections, and forward-only dependency direction.
- PRODUCT-ADR-PIPELINE-009 preserves PRODUCT-ADR-PIPELINE-006 through PRODUCT-ADR-PIPELINE-008 and the fixed Learning path contract.
- PRODUCT-ADR-PIPELINE-010 preserves the untrusted-provider boundary and the non-compensating Learning readiness dimensions.
- No normative specification file changed.
- The available Design Records MCP indexes the Brewprint repository rather than this repository. It rejected the T03 ID range and its repository-wide validation returned unrelated Brewprint diagnostics, so it could not validate these records.
- `git diff --check` completed without reported output.
- Strict specification validation returned `[strict]  All 34 file(s) OK.`
- `git status --short` showed only the two new Pipeline ADRs, T03, and its parent Work Item in the T03 change scope.
- Every T03 done condition is satisfied.
- T03 is `done`. T04 may consume PRODUCT-ADR-PIPELINE-009 and PRODUCT-ADR-PIPELINE-010.
