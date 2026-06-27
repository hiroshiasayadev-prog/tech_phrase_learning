# PRODUCT-TASK-LEARNING-001-02: Resolve missing learning decisions

- **id**: PRODUCT-TASK-LEARNING-001-02
- **status**: done
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-LEARNING-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 1d
- **depends_on**:
  - PRODUCT-TASK-LEARNING-001-01
- **outputs**:
  - PRODUCT-INV-LEARNING-002
  - PRODUCT-ADR-LEARNING-007
  - PRODUCT-ADR-LEARNING-008
  - PRODUCT-ADR-LEARNING-009
  - PRODUCT-ADR-LEARNING-010
  - PRODUCT-ADR-LEARNING-011
  - PRODUCT-ADR-LEARNING-012

## Goal

Resolve every missing normative learning decision identified by the baseline through accepted Learning ADRs.

## Work

1. Read PRODUCT-TASK-LEARNING-001-01 Evidence and every identified authority gap.
2. Separate decisions from specification elaboration and implementation choices.
3. Present each unresolved learning judgment to the user before adoption.
4. Create focused Learning ADRs for adopted decisions that lack accepted authority.
5. Cover, when unresolved by current authority:
   - the learner-visible meaning and source of a discussion title;
   - stable option identity required for learner-answer state;
   - minimum learner-visible attribution composition;
   - learning-owned publication-readiness criteria;
   - any missing field, invariant, interaction, progression, or terminal semantic.
6. Keep option wire representation, identifier encoding, pipeline validation mechanics, and UI state outside the ADR decisions.
7. Mark each new ADR `accepted` only after the user adopts its decision.
8. Record supersession and `migrated_to_spec` state accurately.
9. Update this task's `outputs` and Evidence with every created or changed ADR.
10. Stop as `blocked` when a required user decision remains unavailable.

Do not change normative specifications before the required ADRs are accepted.

### Decision register

Resolve the following items one at a time.
Record each result in this table immediately after the user adopts or rejects the candidate direction.

| no. | decision | current gap | status | result | authority action |
|---:|---|---|---|---|---|
| 1 | First-MVP maximum learning-path length | `spec:product.learning.learning_path` sets six posts, but no accepted Learning ADR authorizes that number. | resolved | Retain a Learning-owned range of two to six selected source posts for the first MVP. | PRODUCT-ADR-LEARNING-007 accepted. T03 must retain two-to-six path cardinality and align unit interaction cardinality. T04 must preserve the same session interaction range. |
| 2 | Learning-path adjacency semantics | The current spec requires an `accepted conversation projection` without defining whether projected adjacency is valid Learning meaning. | resolved | Use source-grounded reply projection: explicit reply relations plus genuine topic-level responses projected to the opening post. Content-only inferred edges and unavailable-target fallbacks are invalid adjacency authority. | PRODUCT-ADR-LEARNING-008 accepted. T03 must define source-independent adjacency semantics and preserve the unavailable-target distinction. Pipeline keeps source-specific extraction and projection mechanics. |
| 3 | Discussion-title semantics | UI requires a current discussion title, but Learning does not define its meaning, origin, or required presence. | resolved | Require the original source discussion title as the learner-visible title for every first-MVP learning unit. Do not generate a path-specific title. | PRODUCT-ADR-LEARNING-009 accepted. T03 must add the source discussion title to complete learning-unit content. T04 must route the title to the UI top bar. |
| 4 | Answer-option identity and correct-option reference | UI stores a selected option identifier, while Learning defines option values without stable semantic identity. | resolved | Give every option an interaction-local semantic identity. Reference the correct option by identity. Shuffle learner-visible order once per interaction and keep that permutation stable for the current session. | PRODUCT-ADR-LEARNING-010 accepted. T03 must define identity and correct-option reference. T04 must preserve the stable shuffled-presentation constraint and route UI-owned state follow-up to the UI owner. |
| 5 | Minimum learner-visible attribution and first-MVP source-use boundary | PRODUCT-INV-LEARNING-002 found that `discuss.python.org` contributions use CC BY-NC-SA 3.0. Attribution alone does not resolve noncommercial and share-alike restrictions. | resolved | Limit the accepted corpus to noncommercial first-MVP use. Require global legal notices from the main page and unit-specific attribution access from each learning unit. | PRODUCT-ADR-LEARNING-011 accepted. T03 must define unit-level attribution content. T04 must preserve the access requirements and route the accepted anchor-style modal direction to UI authority. Commercial-source compatibility remains a Product-governance follow-up. |
| 6 | Publication-readiness decision gate | Investigation evidence defines concrete structural and semantic failure classes, but those findings were not yet adopted as normative Learning authority. | resolved | Require structural readiness plus non-compensating semantic dimensions for path coherence, per-post quiz suitability, source grounding, summary fidelity, phrase usefulness, option naturalness, contextual fit, and generated-source separation. Use approved automated per-unit gating with human approval at the criteria and fixture level. | PRODUCT-ADR-LEARNING-012 accepted. T03 must consolidate the Learning-owned readiness contract. Pipeline must define and validate the concrete gate implementation with representative harder fixtures. |

Decision order:

1. maximum learning-path length;
2. learning-path adjacency semantics;
3. discussion-title semantics;
4. answer-option identity and correct-option reference;
5. minimum learner-visible attribution;
6. publication-readiness decision gate.

For each resolved item, record:

- the adopted result;
- rejected alternatives when rationale matters;
- the accepted ADR that authorizes the result, or `no new ADR required` with the existing authority;
- the exact T03 or T04 specification-reflection input.

## Done condition

- Every missing normative learning decision from T01 is accepted, deferred without blocking completeness, or explicitly blocks the task.
- Every adopted decision has one focused Learning ADR.
- Existing accepted Learning ADRs remain unchanged unless a new ADR explicitly supersedes them.
- Decision rationale appears only in ADRs.
- No implementation mechanism or downstream-owner behavior is adopted as a Learning decision.
- T03 and T04 have complete accepted authority for specification reflection.

## Verification

- Trace every adopted decision to one accepted Learning ADR.
- Confirm each ADR uses the correct status, dependencies, supersession, and target specification refs.
- Confirm no specification became the first source of a design decision.
- Confirm option identity remains semantic and transport-independent.
- Confirm publication-readiness meaning remains separate from pipeline gate implementation.
- Run relevant record validation, `git diff --check`, and `git status --short`.

## Evidence

### Execution protocol

- T02 started with six numbered decision items.
- Resolve one item per user discussion.
- Update the Decision register immediately after each result.
- Create or accept the required ADR before any normative specification reflection.
- PRODUCT-INV-LEARNING-002 concluded before Decision 5 judgment.

### Resolved decision 1

- **Decision**: A valid first-MVP learning path contains two to six ordered source-post references.
- **Reason**: Six posts allow a multi-turn exchange while limiting fatigue and keeping one discussion focused.
- **Rejected direction**: Leaving the maximum to Pipeline policy would allow processing choices to change learner-session length.
- **Authority**: PRODUCT-ADR-LEARNING-007.
- **T03 input**: Retain the two-to-six path cardinality and state that one selected post produces one interaction.
- **T04 input**: Preserve two to six ordered interactions per session without introducing a UI-specific limit.
- **Specification status**: No specification was changed in T02. `migrated_to_spec` remains `null` until T03 and T04 reflection.

### Decision progress

| no. | status |
|---:|---|
| 1 | resolved by PRODUCT-ADR-LEARNING-007 |
| 2 | resolved by PRODUCT-ADR-LEARNING-008 |
| 3 | resolved by PRODUCT-ADR-LEARNING-009 |
| 4 | resolved by PRODUCT-ADR-LEARNING-010 |
| 5 | resolved by PRODUCT-ADR-LEARNING-011 |
| 6 | resolved by PRODUCT-ADR-LEARNING-012 |

### Decision 2 result

- **Adopted result**: Adjacent posts use explicit reply relations or genuine source-level topic responses projected to the opening post.
- **Rejected direction**: Content-only inference must not create a first-MVP learning-path edge.
- **Fallback distinction**: An unavailable explicit reply target must not be treated as a genuine topic-level response.
- **Authority**: PRODUCT-ADR-LEARNING-008.
- **T03 input**: Define source-independent connected adjacency and preserve the unavailable-target distinction without naming Discourse fields or Python code.
- **Pipeline input**: Preserve source-native relations and implement source-specific projection and validation.
- **Specification state**: No Learning specification changed in T02.

### Closure verification

- **Decision coverage**: All six decision-register items are resolved through PRODUCT-ADR-LEARNING-007 through PRODUCT-ADR-LEARNING-012.
- **ADR lifecycle**: All six new ADRs are `accepted`.
- **Specification migration**: All six new ADRs retain `migrated_to_spec: null` because T03 and T04 have not reflected them yet.
- **Dependency check**: Every ADR dependency resolves to an existing accepted Learning ADR. No new supersession relation is required.
- **Workflow relation check**: PRODUCT-WORK-LEARNING-001 lists this task, and both records use PRODUCT-REQ-PRODUCT-001.
- **Investigation check**: PRODUCT-INV-LEARNING-002 is `concluded` and records PRODUCT-ADR-LEARNING-011 in `follow_up_results`.
- **Artifact-boundary check**: Learning ADRs own learner-visible meaning and constraints. UI state and presentation mechanisms are routed as downstream inputs.
- **Specification check**: T02 changed no normative specification.
- **Manual shape check**: T02, PRODUCT-INV-LEARNING-002, and PRODUCT-ADR-LEARNING-007 through PRODUCT-ADR-LEARNING-012 contain their required canonical sections and substantive content.
- **DRMCP limitation**: DRMCP is unavailable for this repository. `validate_records` was not run and no success is claimed.
- **Strict specification validation**: `validate_spec.py product/records/spec --strict --no-color` returned `[strict]  All 34 file(s) OK.`
- **Whitespace validation**: `git diff --check` produced no output.
- **Repository state**: `git status --short` showed the expected PRODUCT coordination changes and new Learning records.
- **Closure state**: All done conditions are satisfied. T02 is complete and ready for commit.

### Decision 6 result

- **Adopted result**: Publication readiness requires both structural readiness and every required semantic quality dimension.
- **Structural scope**: Validate path validity, complete fields and cardinalities, option identity and correct-option references, source routes, generated-source separation, attribution completeness, evaluation coverage, and internal consistency.
- **Semantic scope**: Evaluate path coherence, per-post quiz suitability, source grounding, summary fidelity, phrase usefulness, option naturalness, contextual fit, and generated-source separation.
- **Non-compensation rule**: Failure of one required dimension blocks publication regardless of aggregate quality.
- **Human boundary**: Humans approve criteria, representative fixtures, material criteria changes, and unresolved borderline policy judgments.
- **Automation boundary**: Routine units may pass an approved automated gate. Model-only success is insufficient without deterministic validation.
- **Production-evidence boundary**: Existing local-model results support provisional bounded use but do not prove unattended production-grade accuracy across unseen content.
- **Authority**: PRODUCT-ADR-LEARNING-012.
- **Investigation evidence**: PRODUCT-INV-LEARNING-001, PRODUCT-INV-PIPELINE-001, and PRODUCT-INV-PIPELINE-002.
- **T03 input**: Consolidate the Learning-owned publication-readiness contract without prescribing Pipeline algorithms.
- **T04 input**: Preserve generated-source separation and downstream availability semantics.
- **Pipeline input**: Define deterministic checks, semantic evaluator contracts, coverage validation, retries, thresholds, and representative harder-fixture approval evidence.
- **Specification state**: No Learning specification changed in T02.

### Decision 3 result

- **Adopted result**: Every first-MVP learning unit uses the original source discussion title as its learner-visible discussion title.
- **Rejected direction**: The first MVP will not generate a path-specific learner-facing title.
- **Reason**: Generated titles would add prompt design, quality validation, and investigation work without enough first-MVP value.
- **Authority**: PRODUCT-ADR-LEARNING-009.
- **T03 input**: Require one source discussion title in complete learning-unit content.
- **T04 input**: Route the immutable learning-unit title to the persistent UI top bar.
- **Attribution boundary**: The source title also serves as the attributed work title under PRODUCT-ADR-LEARNING-011.
- **Specification state**: No Learning specification changed in T02.

### Decision 4 result

- **Adopted result**: Every option has one stable semantic identity within its interaction in the current published content.
- **Correctness rule**: Each interaction references the correct option by semantic identity.
- **Display rule**: The learner-visible option order is shuffled once when the interaction first becomes active.
- **Stability rule**: The chosen permutation remains stable until the current learning-unit session ends.
- **Label rule**: `A`, `B`, and `C` identify display positions after shuffling and are not semantic identities.
- **Reason**: Recorded experiments place the preferred option first, so preserving generated order would expose a correctness-position pattern.
- **Authority**: PRODUCT-ADR-LEARNING-010.
- **T03 input**: Require interaction-local unique option identities and one correct-option reference.
- **T04 input**: Preserve one stable shuffled permutation per interaction and route selected-identity and permutation-state handling to the UI owner.
- **Implementation boundary**: Identifier encoding, wire representation, shuffle algorithm, and state storage remain deferred.
- **Specification state**: No Learning specification changed in T02.

### Decision 5 result

- **Adopted source-use boundary**: The accepted `discuss.python.org` corpus is limited to noncommercial first-MVP use.
- **Commercial boundary**: Commercial release remains blocked pending separate permission, corpus replacement, or qualified legal confirmation.
- **Unit attribution**: Require the source discussion title, source platform, discussion URL, every selected source-post author's displayed username, license identity and link, adaptation statement, and no-endorsement statement.
- **URL scope**: One discussion URL is sufficient for the first MVP. Separate direct URLs for every selected post are not required.
- **Global access**: Global legal notices must remain accessible from the main page.
- **Unit access**: Unit-specific source and license details must remain accessible from the current learning unit.
- **Accepted UI direction**: Use low-prominence anchor-style actions that open modal dialogs.
- **Authority boundary**: The presentation direction requires UI-owned authority before UI specification reflection.
- **Authority**: PRODUCT-ADR-LEARNING-011.
- **Investigation evidence**: PRODUCT-INV-LEARNING-002.
- **T03 input**: Require complete unit-level attribution content and author coverage.
- **T04 input**: Preserve the main-page and unit-level access constraints and record the accepted presentation direction for UI follow-up.
- **Implementation boundary**: Link semantics, modal behavior, typography, spacing, focus management, and responsive behavior remain UI concerns.
- **Specification state**: No Learning specification changed in T02.
