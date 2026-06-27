# PRODUCT-TASK-PIPELINE-001-02: Resolve source, normalization, identity, and provenance decisions

- **id**: PRODUCT-TASK-PIPELINE-001-02
- **status**: not_started
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PIPELINE-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 2.5d
- **depends_on**:
  - PRODUCT-TASK-PIPELINE-001-01
- **outputs**: []

## Goal

Resolve Pipeline-owned source, normalization, artifact identity, generated-content versioning, and provenance decisions through accepted ADRs.

## Work

1. Read the T01 decision register and current accepted Pipeline ADRs.
2. Resolve the source acquisition boundary, including discovery input, fetch result, retained reuse, refresh, replacement, and acquisition failure outcomes.
3. Resolve authentic source identity and current retained-source identity without selecting a storage schema.
4. Define the source-independent authentic-post model and conversation normalization decisions.
5. Preserve authored text separately from quoted material and generated text.
6. Preserve explicit reply targets, genuine topic-level responses, unavailable explicit targets, source order, metadata, and author identity.
7. Resolve normalized artifact identity and its route to authentic source evidence.
8. Resolve stable valid-path and learning-unit identity inputs without changing Learning semantics.
9. Resolve current generated-content versioning and replacement meaning.
10. Resolve provider, prompt, validator, and publication-decision provenance ownership.
11. Define which provenance remains Pipeline-internal and opaque to Application readers.
12. Present each unsupported normative choice to the user before adoption.
13. Create focused Pipeline ADRs for every adopted decision lacking current authority.
14. Keep physical schemas, identifier encodings, databases, provider deployments, and exact prompt text outside the decisions.
15. Update `outputs` and Evidence with every accepted ADR.
16. Do not change normative specifications before the required ADRs are accepted.

## Done condition

- Source acquisition, reuse, refresh, replacement, and failure meanings have accepted authority.
- Authentic source and normalized artifact identity have accepted authority.
- Authored text, quoted material, source relationships, metadata, and author identity have clear ownership.
- Valid-path and stable learning-unit identity inputs are consistent with Learning contracts.
- Generated-content replacement and current version meaning are explicit.
- Provider, prompt, validator, and publication-decision provenance have explicit ownership.
- The opaque provenance boundary outside Pipeline is explicit.
- Every adopted decision is recorded in an accepted Pipeline ADR.
- No implementation schema or technology is adopted.
- T03 through T07 have complete decision inputs.

## Verification

- Trace every adopted normative claim to one accepted Pipeline ADR.
- Confirm no task or investigation evidence acts as authority.
- Confirm source-specific fields do not become the source-independent model.
- Confirm unavailable explicit targets remain distinct from genuine topic-level responses.
- Confirm stable learning-unit identity remains anchored to valid-path identity.
- Confirm provenance does not leak through `LearningUnitRef` or complete learner-visible content.
- Run relevant record validation, strict specification validation, `git diff --check`, and `git status --short`.

## Evidence

TBD
