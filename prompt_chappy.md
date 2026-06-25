## Tech Phrase Learning assistant protocol

### Paths

- Repository root: `C:\Users\imved\projects\tech_phrase_learning`
- PRODUCT specification router: `product/records/spec/index.md`
- Learning overview: `product/records/spec/learning/index.md`
- Pipeline overview: `product/records/spec/pipeline/index.md`

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
| `pipeline/` | Ingestion, normalization, filtering, extraction, LLM augmentation, validation, and provider integration. |

Dependency direction:

- `pipeline` may depend on `learning`.
- `learning` must not depend normatively on `pipeline`.
- Learning semantics must remain valid when processing technology changes.
- Concrete model and provider choices belong to `pipeline`.

Do not create a new top-level spec area until its semantic owner is explicit.

### Current accepted decisions

- `PRODUCT-ADR-LEARNING-001`: Use technical conversation trees as the primary learning source.
- `PRODUCT-ADR-LEARNING-005`: Generate phrase-learning units from summarized source-post paths.
- `PRODUCT-ADR-LEARNING-006`: Use progressive quiz-to-summary cards for learner sessions.
- `PRODUCT-ADR-PIPELINE-001`: Prefer mechanical processing before LLM augmentation.
- `PRODUCT-ADR-PIPELINE-002`: Use an OpenAI-compatible LLM provider boundary.
- `PRODUCT-ADR-PIPELINE-004`: Use path-based generation and automated publication gating for the first MVP.

Read the corresponding ADR before changing its decision or the specification derived from it.

Do not rewrite an accepted ADR to reverse its decision.
Create a new ADR and supersede the old ADR.

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
