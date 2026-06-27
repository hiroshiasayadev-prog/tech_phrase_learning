# PRODUCT-ADR-LEARNING-009: Use the source discussion title for first-MVP learning units

- **status**: accepted
- **date**: 2026-06-27
- **depends_on**: [PRODUCT-ADR-LEARNING-001, PRODUCT-ADR-LEARNING-005]
- **supersedes**: []
- **migrated_to_spec**: 2026-06-27

## Context

The first-MVP learning page requires a discussion title for the current learning unit.

Current Learning contracts do not define the title's meaning, origin, or required presence.

A generated learner-facing title could summarize one selected learning path more directly than the original discussion title.
However, generated titles introduce another generation task, validation criteria, and prompt-quality concern.

The first MVP does not need that additional complexity to identify the source discussion.

## Decision

Every first-MVP learning unit will include the original source discussion title.

The source discussion title will be the learner-visible discussion title for the learning unit.

The first MVP will not require a generated or path-specific learner-facing title.

The title must remain associated with the source discussion referenced by the learning path.

The Learning domain owns the title's learner-visible meaning and required presence.
The Pipeline owns source-specific extraction and materialization.
The UI owns placement, truncation, and presentation behavior.

A later generated or path-specific title requires a new Learning decision.

## Rationale

The original source title provides a deterministic and source-grounded identifier for the current discussion.

Using the source title avoids a new generation and validation workflow.
The simpler rule is sufficient for the first MVP.

The decision also prevents generated text from being mistaken for the original discussion title.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Generate one learner-facing title per learning path | The first MVP would require another prompt, quality contract, validation flow, and investigation. |
| Store both source and generated titles | The additional field and generation process do not provide enough first-MVP value. |
| Omit the discussion title | The learning page requires a stable identifier for the current source discussion. |

## Consequences

- `spec:product.learning.learning_unit` must require one source discussion title per learning unit.
- The title must identify the source discussion used by the learning path.
- `spec:product.application.pwa_interface` must preserve the title inside available complete content.
- `spec:product.ui.components.top_bar` must use the learning unit's source discussion title.
- Pipeline generation does not require a title-generation stage for the first MVP.
- UI truncation and responsive presentation remain implementation concerns.
- Learner-visible attribution remains a separate decision under PRODUCT-INV-LEARNING-002.

## Evidence

- `spec:product.ui.learning_flow` requires the top bar to show the current discussion title.
- `spec:product.ui.components.top_bar` leaves the title source unresolved.
- The accepted first-MVP content source is an authentic technical discussion.
- The user selected the original source discussion title to avoid new generation-quality and prompt-design work.
