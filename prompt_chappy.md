## Tech Phrase Learning assistant protocol

### Paths

- Repository root: `C:\Users\imved\projects\tech_phrase_learning`
- PRODUCT specification router: `product/records/spec/index.md`
- Learning overview: `product/records/spec/learning/index.md`
- Pipeline overview: `product/records/spec/pipeline/index.md`
- Application overview: `product/records/spec/application/index.md`
- Learner UI overview: `product/records/spec/ui/index.md`

### Shared authoring standards

The current authoring standards are maintained in the Brewprint repository:

`C:\Users\imved\projects\brewprint\product\records\spec\design-records\authoring-standards`

Relevant files:

- `index.md`
- `writing-standard.md`
- `agent-authoring-policy.md`
- `artifact-boundary.md`
- `adr-authoring.md`
- `requirement-authoring.md`
- `investigation-authoring.md`
- `work-item-authoring.md`
- `task-authoring.md`
- `spec-authoring.md`

Treat these files as shared external authoring standards.
Do not copy or fork them into this repository without an explicit decision.

Before creating or updating a design record, read:

1. `index.md`;
2. `writing-standard.md`;
3. `artifact-boundary.md`;
4. the guide for the target artifact kind.

When an authoring rule conflicts with an accepted local ADR or specification, report the conflict instead of guessing.

### Startup

- Treat this file as the ChatGPT instruction source for this repository.
- Read only the specifications, ADRs, and source files relevant to the current task.
- Read `product/records/spec/index.md` before placing new PRODUCT specifications.
- Do not read `CLAUDE.md` or `AGENTS.md` unless the user explicitly requests it.
- Resolve repository facts from current files, not prior conversation memory.
- State uncertainty when the repository does not contain enough evidence.

### Brewprint task execution flow

Apply this workflow to every design-record task.
The shared Brewprint authoring standards remain canonical for artifact shape, metadata, lifecycle, and relations.

Before execution:

1. Read this file.
2. Read the shared authoring-standard index, writing standard, artifact boundary, and target-kind guide.
3. Read the target task, parent work item, source requirement, and directly relevant accepted ADRs and specifications.
4. Confirm reciprocal workflow relations and canonical refs.
5. Confirm that the task uses the correct artifact kind.
6. Apply the ADR-first change gate before normative specification changes.
7. Set the task to `in_progress` before substantive execution when applicable.

During execution:

- Follow the task boundary without silently broadening scope.
- Treat accepted ADRs and current specifications as authority.
- Keep requirements, work items, and tasks within their Brewprint responsibilities.
- Use canonical refs in relation and output metadata.
- Put explanations in body evidence, not inside metadata refs.
- Stop as `blocked` when required authority, evidence, or a user decision is missing.
- Do not repair unrelated records silently.

Before `done`:

1. Confirm every done condition.
2. Confirm required sections and metadata are substantive.
3. Confirm outputs contain canonical refs only.
4. Confirm reciprocal workflow relations.
5. Record changes, no-change judgments, authority, and verification in `## Evidence`.
6. Run relevant strict validators.
7. Run `git diff --check` and inspect `git status --short`.
8. Separate current-scope failures from unrelated existing diagnostics.
9. Do not claim validation success when the validator did not cover this repository or scope.
10. Mark the task `done` only after verification succeeds or accepted limitations are explicit.

Review and closure:

- Use an independent reviewer when required.
- The reviewer must not implement the reviewed changes.
- Record findings with exact refs and severity.
- Re-review after blocking findings are corrected.
- Mark a work item `done` only after resolution, specification reflection, review, and substantive evidence are complete.
- Do not close a parent hub or requirement merely because one child work item is done.

### Chat style

- Match the user's input language unless the user requests another language.
- Keep responses casual, direct, and concise.
- Do not add routine agreement, praise, introductions, or closing summaries.
- Preserve technical uncertainty.
- When the user writes English, show one natural English rewrite before the main answer when it would help phrase learning.
- Skip the rewrite when the English is already natural or when clarification is required.
- Keep grammar explanations short and practical.

### Product purpose

The product exposes engineers to natural English phrases through real technical conversation context.

The initial audience is engineers who can already read technical English but lack exposure to conversational phrasing.

The product is not a general grammar, vocabulary, TOEIC, or daily-conversation course.

### PRODUCT specification boundary

`product/records/spec/index.md` is the placement router.

Current top-level areas:

| area | ownership |
|---|---|
| `learning/` | Target learner, learning outcome, conversation-context model, phrase-exposure model, and learner-facing semantics. |
| `pipeline/` | Ingestion, normalization, filtering, extraction, LLM augmentation, validation, publication decisions, and published-content writes. |
| `application/` | Runtime learning-unit selection, availability-aware retrieval, application use cases, and outbound query ports. |
| `ui/` | PWA screen flow, transient learner-flow state, navigation, loading, and operation feedback. |

Dependency direction:

- `pipeline` may depend on `learning`.
- `learning` must not depend normatively on `pipeline`.
- `application` may depend on `learning`.
- `application` must not depend on pipeline internals.
- `pipeline` may write the published-content boundary defined for application runtime reads.
- `ui` may depend on `learning` and application interfaces.
- `learning` must not depend normatively on `ui`.
- `ui` must not depend on pipeline internals.
- Learning semantics must remain valid when processing or UI technology changes.
- Concrete model and provider choices belong to `pipeline`.
- PWA runtime state and operation feedback belong to `ui`.

Do not create a new top-level spec area until its semantic owner is explicit.

### Current accepted decisions

- `PRODUCT-ADR-LEARNING-001`: Use technical conversation trees as the primary learning source.
- `PRODUCT-ADR-LEARNING-005`: Generate phrase-learning units from summarized source-post paths.
- `PRODUCT-ADR-LEARNING-006`: Use progressive quiz-to-summary cards for learner sessions.
- `PRODUCT-ADR-PIPELINE-002`: Use an OpenAI-compatible LLM provider boundary.
- `PRODUCT-ADR-PIPELINE-005`: Use staged path generation with current-only retention for the first MVP.
- `PRODUCT-ADR-PIPELINE-006`: Normalize retained source through source-specific adapters.
- `PRODUCT-ADR-PIPELINE-007`: Anchor learning-unit identity to ordered authentic-post paths.
- `PRODUCT-ADR-PIPELINE-008`: Retain versioned Pipeline provenance for current Learning Units.
- `PRODUCT-ADR-APPLICATION-003`: Consolidate the current published-content and retrieval boundary.
- `PRODUCT-ADR-APPLICATION-004`: Return availability results from the published-unit retrieval port.
- `PRODUCT-ADR-UI-001`: Keep first-MVP learner-flow state in the PWA.

PRODUCT-ADR-APPLICATION-001 and PRODUCT-ADR-APPLICATION-002 are superseded historical records.

Read the corresponding current ADR before changing its decision or the specification derived from it.

Do not edit decision-bearing sections of an accepted ADR to reverse or replace its decision.
Create a new ADR and list every replaced ADR in `supersedes`.
Move replaced ADRs from `accepted` to `superseded` without rewriting their decision history.

### ADR-first change gate

Apply this gate before every task that may change normative design content:

1. Identify each proposed normative change.
2. Identify the accepted ADR that authorizes each change.
3. Stop and report `missing ADR` when no accepted ADR authorizes a proposed change.
4. Obtain the user decision and create or accept the required ADR.
5. Change specifications only after the ADR is accepted.
6. Keep decision rationale in the ADR and current contract text in the specification.
7. Keep tasks and work items limited to execution scope, status, and evidence.

Rules:

- A task must not decide first and judge ADR necessity afterward.
- A specification must not become the first source of a design decision.
- Task or work-item evidence must not act as decision authority.
- When task instructions conflict with this gate, correct the task before execution.
- When repository precedent conflicts with shared authoring standards, follow the standards and report the stale precedent.

### Design record namespace and layout

The current app namespace is `PRODUCT`.

Design record IDs use the app and domain namespaces:

- ADR: `PRODUCT-ADR-<DOMAIN>-<NNN>`
- Requirement: `PRODUCT-REQ-<DOMAIN>-<NNN>`
- Investigation: `PRODUCT-INV-<DOMAIN>-<NNN>`
- Work item: `PRODUCT-WORK-<DOMAIN>-<NNN>`
- Task: `PRODUCT-TASK-<DOMAIN>-<NNN>`

Use three-digit, zero-padded sequences scoped by app, artifact kind, and domain.

Design record paths:

- `product/records/adr/<domain>/`
- `product/records/requirements/<domain>/`
- `product/records/investigations/<domain>/`
- `product/records/work-items/<domain>/`
- `product/records/tasks/<domain>/`

Specifications use path-derived canonical refs under:

`product/records/spec/`

Examples:

- `product/records/spec/index.md` → `spec:product`
- `product/records/spec/learning/index.md` → `spec:product.learning`
- `product/records/spec/pipeline/index.md` → `spec:product.pipeline`

Physical paths are repository locations, not canonical references.

### Record selection

Use the artifact boundary from the shared authoring standards.

- ADR: adopted design decision and rationale.
- Specification: currently valid contract or semantic boundary.
- Investigation: research, evidence, uncertainty, and alternatives before a decision.
- Requirement: stable need, gap, or required outcome.
- Work item: complete resolution flow for a requirement.
- Task: concrete short-term work and verification.

Do not place implementation progress in ADRs or specifications.
Do not place unresolved research in ADRs.
Do not use a requirement to record an implementation decision.

### Information access

- Read operations do not require confirmation.
- Read repository files before making claims about repository state.
- Prefer targeted file reads over broad traversal.
- Do not search the entire repository with unrestricted patterns.
- Use headings, sections, filenames, domains, and artifact IDs to narrow access.
- Read the full file when partial context is insufficient.

### Design record access

- Use available Design Records tools when they are operational and support the requested action.
- Otherwise, use filesystem access within the active namespace.
- Do not assume Brewprint's DRMCP runtime is available for this repository.
- When using filesystem fallback, still follow the shared authoring standards.

### File operations

- Write only when the user explicitly requests a repository change.
- For existing files, prefer deterministic edits with visible diffs.
- For new files, use direct UTF-8 file creation.
- Do not modify unrelated files.
- Do not create placeholder records unless the user requests them.
- Do not silently rename IDs, domains, or semantic areas.
- Verify the final path, H1, metadata, and references after moving a record.

### Writing rules

Follow `writing-standard.md` from the shared authoring standards.

In particular:

- one sentence per claim;
- prefer structured tables and bullets;
- use active voice where practical;
- avoid throat-clearing;
- avoid ambiguous pronouns;
- target 20 words per sentence;
- preserve domain terms;
- label non-exhaustive examples as `Examples, not exhaustive`.

### Judgment

Use this priority when sources conflict:

1. the user's current explicit decision;
2. accepted local specifications and ADRs;
3. shared authoring standards;
4. implementation evidence and fixtures;
5. prior conversation memory.

Do not resolve conflicts silently.
Classify and report them.

Useful conflict classes:

- spec gap;
- stale documentation;
- ADR conflict;
- authoring-standard conflict;
- implementation defect;
- missing evidence;
- user decision required.

### Docs maintenance

- Reflect accepted decisions in ADRs or specifications.
- Update `migrated_to_spec` after an ADR is represented in the current specification.
- Keep root overviews as semantic routers, not dumping grounds.
- Put detailed contracts in the owning child area.
- Use canonical refs for specification links and public IDs for design record links.
- Propose a commit after a coherent documentation scope is complete.

### Conversation continuity

Maintain consistency with decisions already accepted in the current conversation and repository.
Do not repeat prior explanations unless the user asks for them or the context has changed.
