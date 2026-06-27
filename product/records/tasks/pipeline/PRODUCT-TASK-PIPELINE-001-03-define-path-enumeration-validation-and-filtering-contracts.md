# PRODUCT-TASK-PIPELINE-001-03: Define path enumeration, validation, and filtering contracts

- **id**: PRODUCT-TASK-PIPELINE-001-03
- **status**: not_started
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PIPELINE-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 2d
- **depends_on**:
  - PRODUCT-TASK-PIPELINE-001-02
- **outputs**: []

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

TBD
