# PRODUCT-TASK-PIPELINE-001-02: Resolve source, normalization, identity, and provenance decisions

- **id**: PRODUCT-TASK-PIPELINE-001-02
- **status**: done
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PIPELINE-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 2.5d
- **depends_on**:
  - PRODUCT-TASK-PIPELINE-001-01
- **outputs**:
  - PRODUCT-ADR-PIPELINE-006
  - PRODUCT-ADR-PIPELINE-007
  - PRODUCT-ADR-PIPELINE-008

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

### Accepted ADR authority

| ADR | authority established |
|---|---|
| PRODUCT-ADR-PIPELINE-006 | Source acquisition, retained-source reuse, Adapter normalization, authentic-post identity, Discussion Paths, and normalization outcomes. |
| PRODUCT-ADR-PIPELINE-007 | Valid-path identity inputs, stable Learning Unit identity, current-only generated content, and atomic replacement. |
| PRODUCT-ADR-PIPELINE-008 | Pipeline-owned opaque provenance, Source Adapter Version, Common Pipeline Version, publication outcome, and version-targeted withdrawal selection. |

### Decision register

The register preserves the user-approved choices materialized in accepted Pipeline ADRs.
Task Evidence is not normative authority.

| sequence | decision | status | accepted ADR |
|---|---|---|---|
| D01 | Pipeline core consumes a source-independent authentic-conversation model. A source-specific adapter maps source-system records into that model. The first MVP uses an adapter for eligible `discuss.python.org` Packaging topics. | materialized | PRODUCT-ADR-PIPELINE-006 |
| D02 | The source-independent input is one authentic conversation containing conversation identity, title, source reference, authentic posts, post identity, authored text, author identity, source order, source-observed relationships, mechanically derived discussion paths, and a route to source evidence. Source adapters do not create learning paths or learning-unit candidates. | materialized | PRODUCT-ADR-PIPELINE-006 |
| D03 | Each source adapter interprets source-specific quote representation and emits authored text separately from quoted material. Generated summaries, prompts, phrases, and quiz content remain outside the authentic-conversation model. | materialized | PRODUCT-ADR-PIPELINE-006 |
| D04 | A source adapter derives discussion paths mechanically from source-platform conversation structure. The common Pipeline derives bounded learning-path candidates from those discussion paths and uses LLMs only for semantic suitability and generation, not structural path discovery. | materialized | PRODUCT-ADR-PIPELINE-006 |
| D05 | A source adapter emits maximal discussion paths from the opening post to each reachable leaf. The common Pipeline derives bounded prefix candidates and duplicate handling without changing the adapter contract. | materialized | PRODUCT-ADR-PIPELINE-006 |
| D06 | Posts that are not reachable from the opening post through mechanically derived discussion paths are excluded from the normalized authentic-conversation model. Retained authentic-source evidence may preserve those posts for current-source diagnosis. | materialized | PRODUCT-ADR-PIPELINE-006 |
| D07 | The first MVP periodically crawls eligible discussion listings to discover discussion URLs. Retained-source lookup uses the canonical discussion URL. A URL with established retained source is reused without refetch or later source-change detection. Source freshness is not part of the learning-content contract. Initial-acquisition retry policy remains outside T02. | materialized | PRODUCT-ADR-PIPELINE-006 |
| D08 | The first MVP provides no explicit source refresh operation. Regeneration may replace current generated content from retained source, but it does not replace the retained authentic source. | materialized | PRODUCT-ADR-PIPELINE-006 |
| D09 | The canonical discussion URL identifies the retained authentic discussion. Each source adapter materializes an authentic-post identity on a best-effort basis. That identity must be unique within the retained discussion and resolve to current source evidence. Source-native post IDs are preferred when available but are not required by the common Pipeline contract. | materialized | PRODUCT-ADR-PIPELINE-006 |
| D10 | One retained authentic discussion has at most one current normalized authentic-conversation artifact. Successful re-normalization replaces that current artifact under the same discussion identity. Adapter version and normalization implementation are not identity inputs, and historical normalized revisions are not required. | materialized | PRODUCT-ADR-PIPELINE-006 |
| D11 | Valid learning-path identity is anchored to the authentic discussion identity plus the ordered authentic-post identities in that path. Path-scoped summaries, target phrases, quiz content, provider identity, prompt provenance, and validator provenance are not identity inputs. | materialized | PRODUCT-ADR-PIPELINE-007 |
| D12 | Each valid learning path materializes exactly one stable learning-unit identity. Regeneration replaces current generated content under that identity and does not create a sibling learning unit or runtime revision identity. | materialized | PRODUCT-ADR-PIPELINE-007 |
| D13 | The Pipeline does not expose or require a separate generated-content instance identity. Replacement updates the complete current generated content and matching current provenance as one atomic semantic change. Partial replacement is invalid. Concrete transaction syntax and persistence mechanics remain implementation concerns. | materialized | PRODUCT-ADR-PIPELINE-007 |
| D14 | Each current learning unit has one Pipeline-owned provenance bundle that links its authentic source, current normalized conversation, valid path, stage-specific provider and prompt provenance, validation results, Common Pipeline Version, and resulting publication outcome. Application receives only an opaque reference to that bundle. | materialized | PRODUCT-ADR-PIPELINE-008 |
| D15 | Successful completion of the approved Common Pipeline publishes the complete current learning unit without a separate per-unit publication-decision layer. Common Pipeline Version is retained in current provenance and may select all current units produced by that version for an availability-only bulk withdrawal. Exact version syntax and bulk-operation implementation remain outside T02. | materialized | PRODUCT-ADR-PIPELINE-008 |
| D16 | Provenance records Source Adapter Version separately from Common Pipeline Version. Source Adapter Version identifies the source-specific normalization and discussion-path behavior. Common Pipeline Version identifies shared learning-path processing, generation, validation, and publication behavior. Both versions represent release-level behavior rather than individual executions. | materialized | PRODUCT-ADR-PIPELINE-008 |
| D17 | Current provenance may select learning units by either Source Adapter Version or Common Pipeline Version for an availability-only bulk withdrawal. The selection and mutation mechanics belong to later publication design. | materialized | PRODUCT-ADR-PIPELINE-008 |
| D18 | Only a complete initial discussion fetch establishes retained authentic source and may proceed to normalization. Partial, unavailable, or failed fetch results do not establish retained source and do not enter learning-unit generation. Retry policy and orchestration remain outside T02. | materialized | PRODUCT-ADR-PIPELINE-006 |
| D19 | A normalization failure does not discard a complete retained authentic source. It produces no normalized artifact and does not enter learning-unit generation. A later Source Adapter Version may re-normalize the retained source without refetching it. | materialized | PRODUCT-ADR-PIPELINE-006 |
| D20 | A successfully normalized authentic conversation may validly produce zero discussion paths or zero learning-path candidates. The normalized artifact remains current, no learning unit is created, and the outcome is not a normalization failure. | materialized | PRODUCT-ADR-PIPELINE-006 |

### Independent review

The initial independent review returned `NEEDS REVISION` with no blocking or major finding.

Two minor Task Evidence findings were corrected:

- D07 now limits no-refetch semantics to URLs with established retained source and leaves initial-acquisition retry policy to T06.
- D10 now states that one retained discussion has at most one current normalized artifact and requires successful re-normalization for replacement.

The focused re-review returned `PASS`.
Both previous findings are closed, no regression finding remains, and no ADR change is required.
The reviewer confirmed that T02 decision authority is ready.
The final validation results satisfied the remaining closure conditions.

### Verification status

- Manual readback confirmed each ADR H1, required metadata fields, required body sections, and dependency direction.
- Manual readback confirmed T02 outputs and parent Work Item impact references for PRODUCT-ADR-PIPELINE-006 through PRODUCT-ADR-PIPELINE-008.
- No normative specification changed.
- Design Records MCP validation was unavailable because the validation call was blocked before execution. Manual record-shape and relation checks remain the recorded limitation.
- `git diff --check` completed without reported output.
- Strict specification validation returned `[strict]  All 34 file(s) OK.`
- `git status --short` showed only the three new Pipeline ADRs, T02, its parent Work Item, and `prompt_chappy.md` in the T02 change scope.
- Every T02 done condition is satisfied.
- T02 is `done`. T03 may consume PRODUCT-ADR-PIPELINE-006 through PRODUCT-ADR-PIPELINE-008.
