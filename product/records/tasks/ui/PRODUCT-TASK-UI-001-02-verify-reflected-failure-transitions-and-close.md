# PRODUCT-TASK-UI-001-02: Verify reflected failure transitions and close

- **id**: PRODUCT-TASK-UI-001-02
- **status**: done
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-UI-001
- **source_requirement**: PRODUCT-REQ-UI-001
- **estimate**: 0.5d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-006-05
- **outputs**:
  - PRODUCT-WORK-UI-001
  - PRODUCT-REQ-UI-001

## Goal

Verify that coordinated PWA-interface specification work reflects PRODUCT-ADR-UI-002 and close the UI resolution flow.

## Work

1. Read the final evidence from PRODUCT-TASK-APPLICATION-006-04 and PRODUCT-TASK-APPLICATION-006-05.
2. Verify `spec:product.ui` and `spec:product.ui.learning_flow` against PRODUCT-ADR-UI-002.
3. Verify page specifications only where the coordinated reflection changed owning failure surfaces.
4. Confirm application failure meanings remain owned by PRODUCT-ADR-APPLICATION-005.
5. Confirm no unsupported retry, transport, or implementation behavior was introduced.
6. Record closure evidence in PRODUCT-WORK-UI-001.
7. Mark PRODUCT-WORK-UI-001 done only when reflection and review are complete.

## Done condition

- Current UI specifications reflect PRODUCT-ADR-UI-002.
- PRODUCT-TASK-APPLICATION-006-05 records no blocking UI-transition finding.
- PRODUCT-ADR-UI-002 has the correct `migrated_to_spec` date.
- PRODUCT-WORK-UI-001 contains substantive closure evidence.
- Reciprocal requirement, work-item, and task relations remain correct.

## Verification

- Trace every category-specific UI transition to PRODUCT-ADR-UI-002.
- Confirm retry counts still come from existing UI authority.
- Confirm `Unavailable` remains a normal skip transition.
- Confirm no UI specification redefines application failure categories.
- Run relevant design-record validation.
- Run `git diff --check` and inspect `git status --short`.

## Evidence

### Result

- **Verdict**: PASS.
- Current UI specifications reflect PRODUCT-ADR-UI-002 without redefining application failure semantics.
- No blocking ADR-to-spec mismatch remains.

### Authority traceability

| operation | outcome | accepted authority | reflected behavior |
|---|---|---|---|
| Initial queue creation | `InfrastructureFailure` | PRODUCT-ADR-UI-002 | Remain on main and use the existing retry flow. |
| Initial queue creation | `MappingFailure` | PRODUCT-ADR-UI-002 | Remain on main, show safe diagnostic information, and do not retry automatically. |
| Initial queue creation | `InvalidSelectionResult` | PRODUCT-ADR-UI-002 | Remain on main, show safe diagnostic information, and do not retry automatically. |
| Initial queue creation | `Success([])` | PRODUCT-ADR-UI-002 and existing UI authority | Show the empty-queue screen as a normal success. |
| Replacement queue creation | `InfrastructureFailure` | PRODUCT-ADR-UI-002 | Preserve the learning page and state and use automatic or manual retry. |
| Replacement queue creation | `MappingFailure` | PRODUCT-ADR-UI-002 | Preserve the learning page and state, show safe diagnostic information and `Back to main`, and do not retry. |
| Replacement queue creation | `InvalidSelectionResult` | PRODUCT-ADR-UI-002 | Preserve the learning page and state, show safe diagnostic information and `Back to main`, and do not retry. |
| Replacement queue creation | `Success([])` | PRODUCT-ADR-UI-002 and existing UI authority | End the flow and show the empty-queue screen without retry. |
| Learning-unit retrieval | `InfrastructureFailure` | PRODUCT-ADR-UI-002 | Preserve the current screen and state and use the existing retry flow. |
| Learning-unit retrieval | `MappingFailure` | PRODUCT-ADR-UI-002 | End the flow, discard queue and session, return to main, and show the safe diagnostic there. |
| Learning-unit retrieval | `Unavailable` | PRODUCT-ADR-UI-002 | Remove only the affected pending reference and continue without technical-failure handling. |

### Specification reflection

| spec | result |
|---|---|
| `spec:product.ui` | PASS. The overview preserves PWA state ownership and routes category-specific transitions to UI authority. |
| `spec:product.ui.learning_flow` | PASS. Initial, replacement, retrieval, empty-result, retry, preservation, and disposal rules match PRODUCT-ADR-UI-002. |
| `spec:product.ui.pages.main_page` | PASS. Initial non-retryable failures remain on main with safe diagnostics and no retry action. |
| `spec:product.ui.pages.learning_page` | PASS. Replacement failures preserve state and retrieval mapping failure terminates the flow. |

### Ownership

- PRODUCT-ADR-APPLICATION-005 remains the authority for failure meaning, safe diagnostic content, and application-classified retryability.
- UI specifications own retry entry, retry attempt state, screen preservation, navigation, queue and session lifecycle, and failure-surface placement.
- Application interface specifications do not decide screen transitions or state disposal.
- UI authority does not define HTTP, JSON, routes, framework behavior, component layout, or exact diagnostic wording.

### Coordinated review

- PRODUCT-TASK-APPLICATION-006-05 records an independent Opus review.
- The review verdict is PASS.
- The review records no blocking findings and no major findings.
- The review evidence is used only as coordinated review completion evidence.

### Requirement consistency

- PRODUCT-REQ-UI-001 was aligned with accepted PRODUCT-ADR-UI-002 authority.
- Generic queue-creation wording was limited to initial queue creation.
- Replacement queue behavior and `Back to main` disposal were added to Required Outcome.
- Stale present-tense Evidence was changed to historical wording.
- The correction records no new decision and leaves the requirement `accepted`.

### Validation

| check | result |
|---|---|
| Dependency status reread | PASS. PRODUCT-TASK-APPLICATION-006-05 and PRODUCT-WORK-APPLICATION-006 are `done`. |
| Filesystem reread | PASS for the requirement, work item, task, accepted ADRs, coordinated review evidence, and owning specifications. |
| Design Records MCP | `validate_records(kind=requirement)` and `validate_records(kind=task)` returned diagnostics for Brewprint and other indexed records. The calls did not cover the Tech Phrase Learning UI records and are not treated as validation authority. |
| Last commit evidence | `.git/logs/HEAD` records `553b3a0 design(application): complete PWA-facing interface contracts`. |
| `git diff --check` | Not executable through the active filesystem-only repository toolset. No success is claimed. |
| `git status --short` | Not executable through the active filesystem-only repository toolset. Current working-tree status is not claimed. |
