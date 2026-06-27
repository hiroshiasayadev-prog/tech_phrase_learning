# PRODUCT-TASK-LEARNING-001-01: Establish learning contract completeness baseline

- **id**: PRODUCT-TASK-LEARNING-001-01
- **status**: done
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-LEARNING-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 1d
- **depends_on**: []
- **outputs**:
  - PRODUCT-INV-LEARNING-002

## Goal

Establish the accepted learning-contract baseline and the exact unresolved gap set for later decision and specification work.

## Work

1. Read every current and superseded Learning ADR and the concluded Learning investigation.
2. Read `spec:product.learning` and every child learning specification.
3. Read the downstream pipeline, application-interface, and UI impact refs from PRODUCT-WORK-LEARNING-001.
4. Classify each work-item concern as:
   - accepted current contract;
   - missing normative decision;
   - missing specification detail;
   - downstream contract mismatch;
   - implementation-only choice.
5. Verify target learner, learning gap, participation model, and intended learning outcome consistency.
6. Verify valid-path meaning, composition, cardinality, coherence, suitability, and grounding criteria.
7. Inventory required learning-unit elements, identities, cardinalities, and invariants.
8. Verify question-formulation and reply-formulation interaction composition.
9. Verify target phrase, prompt, option, correct-option, summary, grounding, discussion-title, and attribution semantics.
10. Verify quiz-session progression, reveal order, skip behavior, final-card behavior, and terminal behavior.
11. Verify learning-owned publication-readiness criteria against downstream pipeline needs.
12. Identify every learning-owned constraint consumed by the application interface and UI.
13. Create a focused Learning investigation only when repository evidence cannot resolve a required judgment.
14. Record exact downstream inputs for T02 through T04 in `## Evidence`.

Do not adopt a new design decision or change a normative specification in this task.

## Done condition

- Every PRODUCT-WORK-LEARNING-001 completion concern has one explicit classification.
- Accepted authority and unresolved normative decisions are distinguishable.
- Discussion-title, option-identity, attribution, and publication-readiness gaps have explicit classifications.
- Pipeline and UI consumer needs are separated from learning-owned meaning.
- Processing mechanics, provider choices, runtime selection, and PWA state remain implementation or downstream concerns.
- Any evidence gap that blocks a decision has a focused investigation record.
- T02 through T04 can proceed without reconstructing repository context.

## Verification

- Compare the inventory with PRODUCT-WORK-LEARNING-001 `## Boundary` and `## Completion Condition`.
- Confirm superseded ADRs are historical evidence rather than current authority.
- Confirm no task or work-item evidence is used as normative authority.
- Confirm every proposed normative correction names accepted authority or a missing-ADR follow-up.
- Confirm no pipeline algorithm, provider, runtime-selection, or PWA-state decision enters the Learning scope.
- Run relevant record validation, `git diff --check`, and `git status --short`.

## Evidence

### Result

- **Verdict**: READY FOR LEARNING DECISIONS.
- Current Learning authority supports the first-MVP learning model, path-based unit identity, mixed interactions, and progressive quiz-to-summary sessions.
- Five authority or evidence gaps require follow-up before Learning specifications are implementation-planning complete.
- Remaining gaps route to T02, T03, or T04 without changing normative specifications in this task.
- PRODUCT-INV-LEARNING-002 was created for the unresolved source-attribution evidence boundary.

### Reviewed authority

Current decision authority:

- PRODUCT-ADR-LEARNING-001;
- PRODUCT-ADR-LEARNING-005;
- PRODUCT-ADR-LEARNING-006.

Current Learning specifications:

- `spec:product.learning`;
- `spec:product.learning.learning_model`;
- `spec:product.learning.learning_path`;
- `spec:product.learning.learning_unit`;
- `spec:product.learning.quiz_session`.

Downstream consumers and implementers:

- `spec:product.pipeline`;
- `spec:product.application.pwa_interface`;
- `spec:product.ui.learning_flow`;
- `spec:product.ui.components.top_bar`;
- `spec:product.ui.components.quiz_card`;
- `spec:product.ui.components.answered_card`.

Historical and investigative evidence:

- PRODUCT-ADR-LEARNING-002;
- PRODUCT-ADR-LEARNING-003;
- PRODUCT-ADR-LEARNING-004;
- PRODUCT-INV-LEARNING-001;
- PRODUCT-INV-PIPELINE-002;
- PRODUCT-ADR-PIPELINE-005.

Superseded ADRs and investigations do not authorize current normative changes.

### Concern classification

| id | concern | classification | current authority or gap | downstream input |
|---|---|---|---|---|
| LM-01 | Initial audience and learning gap | accepted current contract | PRODUCT-ADR-LEARNING-001 and `spec:product.learning.learning_model` target engineers who read technical English but lack conversational exposure. | Preserve in T03. |
| LM-02 | Intended learning outcome | accepted current contract | Learning focuses on reusable question and reply phrasing in familiar technical situations. The quiz supports exposure rather than strict knowledge assessment. | T03 must keep outcome wording consistent across the overview and learning model. |
| LM-03 | Mixed participation model | accepted current contract | PRODUCT-ADR-LEARNING-005 requires one opening-question interaction and at least one reply interaction. | Preserve in T03 and T04. |
| LP-01 | Path meaning and path-to-unit cardinality | accepted current contract | One valid connected source-post path defines exactly one logical learning unit. | Preserve in T03. |
| LP-02 | Minimum path length | accepted current contract | An opening post plus at least one authentic reply entails a minimum of two selected posts. | Preserve in T03. |
| LP-03 | Maximum path length of six posts | missing normative decision | `spec:product.learning.learning_path` defines six as the maximum. Current accepted Learning ADRs define bounded paths but do not authorize the number six. | T02 must retain, replace, or remove the maximum through accepted Learning authority. |
| LP-04 | Adjacent-post connection meaning | missing specification detail | The Learning spec refers to an `accepted conversation projection` without defining source-independent connection semantics. Pipeline evidence defines a coarse projection, but Learning must not depend normatively on that mechanism. | T03 must define Learning-owned connected-path meaning. T02 is required if direct-parent versus projected adjacency requires a new choice. |
| LP-05 | Path coherence and suitability | missing specification detail | Current rules require one coherent exchange and one useful quiz per post. The criteria remain too broad to constrain independent pipeline judgment consistently. | T03 must state checkable Learning-owned suitability dimensions without defining filtering algorithms or thresholds. |
| LP-06 | Multiple valid and prefix-overlapping paths | accepted current contract | PRODUCT-ADR-LEARNING-005 permits zero or more independently valid paths and rejects ingestion-time canonicalization. | Preserve in T03. |
| LP-07 | Source grounding and source-reference ownership | accepted current contract | Paths reference authentic source posts and retain a route from each selected turn to its source evidence. | T03 must preserve source-independent semantics. Pipeline materialization remains downstream. |
| LU-01 | Required interaction composition | accepted current contract | Every selected post has one interaction, one summary, one prompt, three options, one correct option, and one target phrase. | Preserve and consolidate in T03. |
| LU-02 | Discussion title | missing normative decision and downstream contract mismatch | UI requires a current discussion title. The Learning unit does not define its meaning, origin, or required presence. Superseded PRODUCT-ADR-LEARNING-002 cannot authorize a generated title. | T02 must decide source-preserved versus derived title semantics and unit-level ownership. |
| LU-03 | Stable answer-option identity | missing normative decision and downstream contract mismatch | UI records selected option identifiers. Learning defines three option values and one correct option but no stable semantic identity or identity scope. | T02 must define option identity and correct-option reference semantics without choosing an encoding. |
| LU-04 | Prompt, option, and target-phrase meaning | accepted current contract | Current Learning contracts define intent prompts, natural options, one best-fitting option, reusable target phrases, and source grounding. | Preserve in T03. |
| LU-05 | Summary meaning | accepted current contract | Summaries are English, source-grounded, technically faithful, conversationally coherent, and distinct from source quotations. | Preserve in T03. |
| LU-06 | Learner-visible attribution minimum | missing evidence and missing normative decision | Current contracts require attribution for the source discussion and original location. They do not define minimum composition or record authoritative source-policy evidence. | PRODUCT-INV-LEARNING-002 must conclude before T02 adopts an attribution minimum. |
| LU-07 | Learner-visible content versus internal source evidence | missing specification detail | The Learning unit includes authentic source references for grounding. The application interface excludes pipeline provenance. The current Learning contract does not clearly separate visible attribution from non-visible evidence. | T03 must separate learner-visible fields from grounding obligations without defining transport shape. |
| LU-08 | Publication quality dimensions | accepted current contract | Source grounding, summary fidelity, phrase usefulness, option naturalness, and contextual fit are current Learning-owned quality dimensions. | Preserve unless T02 accepts changed or additional criteria. |
| LU-09 | Publication-readiness completeness | missing specification detail | Structural completeness, language rules, path validity, attribution, and quality dimensions are spread across sections. The complete Learning-owned readiness set is not stated in one boundary. | T03 must consolidate required outcomes. Pipeline keeps validation mechanics, retries, models, and thresholds. |
| QS-01 | Progressive quiz-to-summary flow | accepted current contract | PRODUCT-ADR-LEARNING-006 defines one active quiz, answered summary cards, progressive reveal, continue, skip, and final-card behavior. | Preserve in T04. |
| QS-02 | Correctness derivation | downstream contract mismatch tied to LU-03 | UI derives correctness from immutable content and selected option identity. Learning lacks option identity and a correct-option reference mechanism. | T04 must reconcile session semantics after T02 and T03 resolve LU-03. |
| QS-03 | Final-card and terminal behavior | accepted current contract | The final answered card shows attribution and `Next discussion`. No separate completion screen is required. | Preserve in T04. |
| QS-04 | Introduction page ownership | downstream contract mismatch and stale ownership | `spec:product.learning.quiz_session` defines an Introduction page. Current PRODUCT routing assigns PWA pages and start flow to UI. The page wording originated in superseded PRODUCT-ADR-LEARNING-003. | T04 must remove or reroute the stale Learning-owned page claim without adding a new Learning decision. |
| DS-01 | Pipeline production constraints | missing specification detail | Pipeline can identify required summaries, phrases, options, grounding, attribution, and publication gating. Path suitability and readiness remain insufficiently explicit. | T03 and T04 must produce an explicit Learning-owned constraint map. |
| DS-02 | Application complete-content boundary | accepted current contract with verification follow-up | The application returns one complete unit satisfying `spec:product.learning.learning_unit` and preserves attribution. | Later application or integration review may add explicit checks for newly required title and option identity. |
| DS-03 | UI discussion-title source | downstream contract mismatch | `spec:product.ui.components.top_bar` leaves the source as published content or a future application contract. Learning must first own title meaning. | T04 must record a UI-owner follow-up after T02 decides LU-02. |
| DS-04 | UI selected-option state | downstream contract mismatch | UI correctly owns selected-answer state. Learning must provide stable option identity inside immutable content. | T04 must record a UI-owner follow-up after T02 decides LU-03. |

### Missing normative decisions

T02 must resolve these decisions through accepted Learning ADRs:

1. whether the first-MVP valid-path maximum remains six posts;
2. the required discussion-title meaning, origin, and unit-level presence;
3. the semantic scope of answer-option identity and correct-option reference;
4. the minimum learner-visible source attribution after PRODUCT-INV-LEARNING-002 concludes;
5. direct or projected path-adjacency semantics only when T03 cannot elaborate `connected` without choosing new behavior.

T02 must also create an ADR before adding or changing publication quality criteria.

### Missing specification detail

T03 must reconcile:

- target learner, learning gap, participation model, and learning outcome wording;
- source-independent connected-path meaning;
- checkable path-coherence and phrase-learning suitability dimensions;
- required learning-unit fields and cardinalities;
- discussion-title and option-identity semantics after T02;
- learner-visible content versus internal grounding evidence;
- one consolidated Learning-owned publication-readiness boundary.

T04 must reconcile:

- question and reply session composition;
- correctness derivation after stable option identity exists;
- progressive reveal, continue, skip, final-card, and next-discussion semantics;
- final-state attribution after T02;
- removal or rerouting of the stale Introduction-page ownership;
- explicit downstream constraints and owner follow-ups for Pipeline, Application, and UI.

### Investigation routing

PRODUCT-INV-LEARNING-002 was created with `status: investigating`.

The investigation covers:

- authoritative source-policy evidence for the accepted initial corpus;
- source platform, discussion title, original location, and author-level attribution candidates;
- transformed-summary disclosure;
- unit-level versus interaction-level attribution;
- learner-visible attribution versus internal grounding and provenance.

The investigation records evidence and recommendations only.
A later Learning ADR must adopt the attribution decision.

### Implementation-only choices

The following choices do not block Learning semantic completion:

- option identifier encoding, wire type, and serialization;
- source-reference storage and database schema;
- exact title-generation prompt or model;
- path enumeration and coarse-projection algorithm;
- suitability scoring, thresholds, filters, and model assignment;
- publication-gate retry, timeout, sampling, and operational policy;
- component files, layout, icons, truncation, and accessibility implementation;
- HTTP routes, JSON shape, transport mapping, persistence, and deployment.

A concrete choice requires Learning authority only when it changes learner-visible meaning or required outcomes.

### Authority verification

- PRODUCT-ADR-LEARNING-001, PRODUCT-ADR-LEARNING-005, and PRODUCT-ADR-LEARNING-006 remain current authority.
- PRODUCT-ADR-LEARNING-002 through PRODUCT-ADR-LEARNING-004 remain superseded historical records.
- PRODUCT-INV-LEARNING-001 and PRODUCT-INV-PIPELINE-002 remain evidence rather than decision authority.
- No task or work-item Evidence is used as normative authority.
- No Learning specification changed during this task.
- Processing mechanics, provider choices, runtime selection, and PWA state remain outside the Learning boundary.

### Workflow verification

- PRODUCT-WORK-LEARNING-001 lists PRODUCT-TASK-LEARNING-001-01.
- This task references PRODUCT-WORK-LEARNING-001 and PRODUCT-REQ-PRODUCT-001.
- PRODUCT-WORK-LEARNING-001 and this task share PRODUCT-REQ-PRODUCT-001.
- PRODUCT-WORK-LEARNING-001 is now `in_progress`.
- PRODUCT-INV-LEARNING-002 references PRODUCT-WORK-LEARNING-001 and the relevant current authority.
- T02 through T04 can proceed from this Evidence and the linked investigation without reconstructing repository context.

### Validation limitation

- Filesystem reread covered the task, parent work item, source requirement, current Learning ADRs, all Learning specifications, superseded Learning ADRs, relevant investigations, and downstream impact refs.
- The active filesystem toolset cannot execute the repository validator, `git diff --check`, or `git status --short`.
- No CLI validation or working-tree cleanliness claim is made.
- The limitation is explicit and does not change the baseline-classification done conditions.

### Closure

- Every PRODUCT-WORK-LEARNING-001 completion concern has an explicit classification or downstream route.
- Accepted authority and missing decisions are separated.
- Attribution evidence has a focused investigation.
- T02 through T04 have exact decision and reflection inputs.
- PRODUCT-TASK-LEARNING-001-01 is complete.
