# PRODUCT-INV-LEARNING-002: Source attribution requirements

- **status**: concluded
- **date**: 2026-06-27
- **trigger**: PRODUCT-ADR-LEARNING-001 requires explicit attribution investigation, while current learning contracts do not define a minimum learner-visible attribution.
- **scope**: Determine the minimum learner-visible source attribution for one first-MVP learning unit and the authoritative source-policy evidence that constrains it.
- **non_scope**: Excludes source ingestion mechanics, provenance storage, transport schemas, UI layout, and adoption of the final attribution contract.
- **source_refs**:
  - PRODUCT-ADR-LEARNING-001
  - PRODUCT-ADR-LEARNING-005
  - PRODUCT-REQ-PRODUCT-001
  - spec:product.learning.learning_unit
  - spec:product.learning.quiz_session
  - spec:product.pipeline
  - spec:product.application.pwa_interface
- **follow_up_candidates**:
  - A Learning ADR defining first-MVP learner-visible attribution minimums.
  - spec:product.learning.learning_unit
  - spec:product.learning.quiz_session
- **related_work_items**:
  - PRODUCT-WORK-LEARNING-001
- **related_adrs**:
  - PRODUCT-ADR-LEARNING-001
  - PRODUCT-ADR-LEARNING-005
  - PRODUCT-ADR-LEARNING-011
- **related_specs**:
  - spec:product.learning.learning_unit
  - spec:product.learning.quiz_session
  - spec:product.pipeline
  - spec:product.application.pwa_interface
- **follow_up_results**:
  - PRODUCT-ADR-LEARNING-011

## Investigation scope

Determine which source facts must remain learner-visible at the final state of one first-MVP learning unit.

Distinguish learner-visible attribution from pipeline provenance and internal source evidence.

Use authoritative source-policy evidence for the accepted initial corpus.

## Out of scope

- Source acquisition, parsing, normalization, and retention mechanics.
- Internal provenance identifiers and storage schemas.
- HTTP, JSON, serialization, and route design.
- Attribution layout, truncation, icons, and styling.
- Adoption of the final attribution decision.

## Background

PRODUCT-ADR-LEARNING-001 requires explicit investigation of source attribution.

PRODUCT-ADR-LEARNING-005 requires source attribution for every first-MVP learning unit.

`spec:product.learning.learning_unit` currently requires attribution to identify the source discussion and original location.
The specification does not define the minimum learner-visible composition.

The initial pipeline corpus uses public `discuss.python.org` Packaging topics.
Relevant source-policy evidence has not been recorded in the Learning design records.

## What was investigated

The investigation must answer:

1. Which authoritative source-policy materials apply to the accepted initial corpus?
2. Must attribution identify the source platform?
3. Must attribution include the original discussion title?
4. Must attribution include a direct original-location reference?
5. Must attribution identify individual source authors?
6. Must transformed summaries be identified as transformed content?
7. Is one unit-level attribution sufficient for all interactions in one path?
8. Which source references remain internal grounding evidence?
9. Which requirements belong to Learning and which belong to Pipeline?

## Findings

### Applicable source license

The current `discuss.python.org` Terms of Service states that user contributions use Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported.

Authoritative evidence:

- `https://discuss.python.org/tos` identifies the user-content license as CC BY-NC-SA 3.0.
- `https://creativecommons.org/licenses/by-nc-sa/3.0/` provides the license deed.
- `https://creativecommons.org/licenses/by-nc-sa/3.0/legalcode` provides the legal code.

The license permits sharing and adaptation only under its conditions.
The conditions include attribution, noncommercial use, and share-alike distribution for adaptations.

This investigation records product-design evidence and is not legal advice.
A legal review remains appropriate before public or commercial release.

### Attribution elements

CC BY-NC-SA 3.0 requires reasonable attribution for distributed or publicly performed source works and adaptations.

The applicable minimum evidence includes:

- the original author or supplied pseudonym;
- the supplied work title;
- a source URI when reasonably practicable;
- the applicable license or license URI;
- an indication that changes were made for an adaptation.

Creative Commons attribution guidance summarizes the normal attribution components as title, author, source, and license.
Version 3.0 also requires the supplied title.

### Learning-unit attribution mapping

One first-MVP learning unit derives content from several selected source posts in one discussion.

The minimum learner-visible attribution should therefore contain:

- the original source discussion title;
- `Discussions on Python.org` as the source platform;
- a direct link to the original discussion;
- the displayed usernames of every selected source-post author;
- `CC BY-NC-SA 3.0` with a link to the license;
- a statement that the learner-visible summaries and quiz material are summarized, adapted, or generated from the linked discussion.

The attribution must not imply endorsement by the authors, the Python Software Foundation, or the source platform.

One unit-level attribution is sufficient when it covers every selected post author and remains available at the final session state.
Repeating full attribution on every interaction is not required by the Learning contract.

The Learning unit must retain interaction-to-source-post grounding internally.
Internal post identifiers, source snapshots, prompt versions, and pipeline provenance are not learner-visible attribution elements.

### Noncommercial and share-alike constraints

The accepted initial corpus has constraints beyond attribution.

- **NonCommercial**: The licensed material may not be used for a purpose primarily intended for commercial advantage or monetary compensation under the license grant.
- **ShareAlike**: Adaptations distributed to learners must use the same or an allowed compatible license.
- **Change indication**: Adapted or summarized material must identify that changes were made.

Whether a particular generated summary, quiz, product distribution, or business model is legally an adaptation or commercial use depends on facts and applicable law.
The repository does not contain authority to resolve those legal judgments.

The first-MVP design must not assume that attribution alone permits commercial use of this corpus.
A commercial release requires separate permission, a compatible alternative corpus, or qualified legal confirmation of another lawful basis.

### Ownership boundary

| concern | owner |
|---|---|
| Required learner-visible attribution meaning | Learning. |
| Source-specific license detection and metadata extraction | Pipeline. |
| Author and discussion metadata materialization | Pipeline. |
| Preservation in complete published content | Pipeline and Application publication boundary. |
| Final-card placement and interaction | UI. |
| Commercial-use and share-alike release approval | Product governance with qualified legal review. |
| Internal source evidence and provenance | Pipeline. |

## Cross-cutting observations

- Learner-visible attribution and internal provenance serve different purposes.
- Discussion-title semantics overlap with attribution and current-context identification.
- Selected source-post authors matter because one learning unit derives from several individual contributions.
- A final-card attribution block can satisfy the Learning presentation boundary when it covers the complete unit.
- Attribution does not resolve the source license's noncommercial and share-alike restrictions.
- Source-specific constraints must not become generic Learning semantics without an explicit decision.
- The product needs an explicit source-use gate before any commercial release.

## Follow-up judgment candidates

- Candidate: Require source title, source platform, direct discussion link, selected author usernames, license identification, and change indication.
- Candidate: Keep full attribution at the learning-unit final state rather than repeating it on every interaction.
- Candidate: Keep source-specific provenance outside learner-visible attribution.
- Candidate: Permit the accepted initial corpus only within a noncommercial first-MVP release boundary until separate permission or legal confirmation exists.
- Candidate: Replace the initial corpus before a commercial release when compatible permission is unavailable.

## Recommendation

The minimum attribution described in this investigation appears appropriate for the current first MVP.

The final answered card should provide one complete unit-level attribution block.
The source discussion title may serve both the current discussion identifier and the required supplied title.

The product should treat commercial use of the accepted corpus as blocked pending separate permission, corpus replacement, or qualified legal confirmation.
Attribution alone is not sufficient to remove the noncommercial and share-alike constraints.

## Follow-up artifact candidates

- A focused Learning ADR for the adopted attribution minimum and first-MVP source-use boundary.
- `spec:product.learning.learning_unit` reflection.
- `spec:product.learning.quiz_session` reflection.
- Downstream Pipeline, Application, and UI follow-up inputs when owner contracts require alignment.
- A Product requirement or work item for commercial-source compatibility before commercial release.

## Open questions

- Will the first MVP be distributed only for noncommercial evaluation?
- Will learner-visible adapted material be explicitly offered under CC BY-NC-SA 3.0?
- Does the intended future business model require replacing the corpus or obtaining separate permission?
- What qualified legal review is required before public release?
- Which generated fields legally constitute an adaptation under the intended deployment and jurisdiction?
