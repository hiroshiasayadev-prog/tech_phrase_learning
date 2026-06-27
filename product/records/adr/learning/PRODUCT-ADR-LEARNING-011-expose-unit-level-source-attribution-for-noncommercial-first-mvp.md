# PRODUCT-ADR-LEARNING-011: Expose unit-level source attribution for the noncommercial first MVP

- **status**: accepted
- **date**: 2026-06-27
- **depends_on**: [PRODUCT-ADR-LEARNING-001, PRODUCT-ADR-LEARNING-005, PRODUCT-ADR-LEARNING-009]
- **supersedes**: []
- **migrated_to_spec**: 2026-06-27

## Context

The accepted first-MVP corpus uses discussions from `discuss.python.org`.

PRODUCT-INV-LEARNING-002 found that current user contributions on that source use CC BY-NC-SA 3.0.
The license imposes attribution, noncommercial, and share-alike conditions.

A global legal-notices surface can explain common corpus and license terms.
A global notice alone does not identify the source discussion and authors for one learning unit.

Repeating complete attribution text on every quiz card would create unnecessary visual noise.
The product needs unit-specific attribution without making it the primary learning content.

## Decision

The accepted `discuss.python.org` corpus will be used only for a noncommercial first-MVP release.

Commercial release using that corpus remains blocked until at least one condition holds:

- the relevant rights holders grant separate permission;
- the corpus is replaced with commercially compatible source material;
- qualified legal review confirms another lawful basis for the intended use.

Every first-MVP learning unit will retain one learner-accessible source-attribution record.

The unit-level attribution will contain:

- the original source discussion title;
- `Discussions on Python.org` as the source platform;
- one direct URL to the original discussion;
- the displayed usernames of every selected source-post author;
- `CC BY-NC-SA 3.0` and a link to the license;
- a clear statement that the summaries, quiz options, and other learner-visible material were generated, summarized, or adapted from the linked discussion;
- a statement that attribution does not imply endorsement by the source authors, the Python Software Foundation, or the source platform.

The first MVP does not require a separate direct URL for every selected post.
The discussion URL and complete selected-author list form the minimum unit-specific attribution contract.

The product will also expose one global legal-notices surface containing common corpus, license, adaptation, noncommercial-use, share-alike, and no-endorsement information.

Learners must be able to open:

- the global legal notices from the main page;
- the current learning unit's source and license details from that unit.

The Learning contract requires both notice surfaces to remain learner-accessible.
The UI domain owns the presentation mechanism, interaction pattern, prominence, and accessibility behavior.

The accepted user direction is a low-prominence anchor-style action that opens a modal.
That direction requires separate UI authority before UI specification reflection.

## Rationale

Unit-specific attribution makes the source discussion and contributing authors identifiable without filling every learning card with legal text.

One discussion URL is sufficient for the first-MVP attribution model because all selected posts belong to that discussion.
The complete selected-author list preserves contributor attribution at the learning-unit level.

A global notice avoids repeating common license terms while unit-level access preserves the relationship between one unit and its source.

A downstream UI design can keep attribution accessible without distracting from the learning flow.

The noncommercial boundary prevents the product from treating attribution as permission for commercial use.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Put all attribution only in a global legal-notices page | The learner could not determine which source discussion and authors produced the current unit. |
| Display complete attribution inline on every interaction card | The repeated legal text would add visual noise and distract from phrase learning. |
| Display only the source platform and license | The current discussion and contributing authors would remain unidentified. |
| Require one direct URL for every selected post | The first MVP can identify all selected contributions through one discussion URL and the selected-author list. |
| Permit commercial use when attribution is present | CC BY-NC-SA 3.0 includes conditions beyond attribution. |

## Consequences

- `spec:product.learning.learning_unit` must require unit-specific attribution content.
- The attribution must cover every selected source-post author in the learning path.
- The source discussion title adopted by PRODUCT-ADR-LEARNING-009 may also serve as the attributed work title.
- `spec:product.learning.quiz_session` must keep unit attribution accessible during the learning-unit session.
- Application complete-content contracts must preserve the unit attribution record.
- Pipeline publication must materialize the required title, discussion URL, selected-author usernames, license identity, and adaptation statement.
- UI specifications must define the main-page legal-notices action and learning-unit source-and-license action.
- The accepted anchor-style action and modal direction must be authorized by a UI-owned decision before UI specification reflection.
- Product governance must prevent commercial release with this corpus until the commercial-source boundary is resolved.
- This ADR records a product-design decision and does not replace qualified legal advice.

## Evidence

- PRODUCT-INV-LEARNING-002 records the current source-license evidence and attribution analysis.
- PRODUCT-ADR-LEARNING-009 requires the original source discussion title in every learning unit.
- The user adopted a noncommercial first-MVP boundary.
- The user selected low-prominence anchor-style actions on the main page and beneath each learning unit, with modal presentation for details.
- The presentation decision remains a downstream UI-authority input and is not owned by this Learning ADR.
