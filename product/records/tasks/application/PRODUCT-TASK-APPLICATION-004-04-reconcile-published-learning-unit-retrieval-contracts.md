# PRODUCT-TASK-APPLICATION-004-04: Reconcile published learning-unit retrieval contracts

- **id**: PRODUCT-TASK-APPLICATION-004-04
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-004
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 0.5d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-004-03
- **outputs**:
  - spec:product
  - spec:product.application
  - spec:product.application.published_content
  - spec:product.application.learning_unit_selection
  - spec:product.pipeline
  - PRODUCT-ADR-APPLICATION-003
  - PRODUCT-ADR-APPLICATION-004

## Goal

Reflect accepted APPLICATION ADRs into current specifications without introducing or changing a design decision.

## Work

1. Read PRODUCT-ADR-APPLICATION-003 and PRODUCT-ADR-APPLICATION-004.
2. Stop as blocked when any required retrieval decision lacks an accepted ADR.
3. Reflect `Available(complete_learning_unit) | Unavailable` in the owning application specification.
4. Reflect transactional current-state publication without previous or new runtime revision language.
5. Reflect the accepted outbound retrieval-port shape.
6. Define the current meaning of `LearningUnitRef`, application use case, outbound retrieval port, persistence adapter, current published state, `Available`, and `Unavailable`.
7. Keep every definition limited to meaning already authorized by PRODUCT-ADR-APPLICATION-003 or PRODUCT-ADR-APPLICATION-004.
8. Keep complete learning-unit composition and attribution owned by `spec:product.learning.learning_unit`.
9. Keep publication validation and published-content writes owned by `spec:product.pipeline`.
10. Keep provenance out of normal PWA retrieval results.
11. Keep queue, loaded content, session, retry, and unavailable-reference skipping owned by `spec:product.ui.learning_flow`.
12. Remove stale `Found`, previous-publication, new-publication, and concurrent-revision wording.
13. Do not edit decision-bearing sections of accepted or superseded ADRs.
14. Update only permitted ADR lifecycle or migration metadata when reflection is complete.
15. Record changed refs, no-change judgments, and validation evidence in `## Evidence`.

Do not adopt a new design decision in this task.

## Done condition

- Every normative specification change traces to an accepted ADR.
- No normative specification change relies only on task or work-item evidence.
- Retrieval results use `Available` and `Unavailable`.
- Specifications describe one committed current published state.
- Specifications contain no runtime previous or new publication model.
- The accepted outbound retrieval-port shape is reflected once in its owning specification.
- `LearningUnitRef`, application use case, outbound retrieval port, persistence adapter, current published state, `Available`, and `Unavailable` have explicit meanings.
- The definitions introduce no decision beyond PRODUCT-ADR-APPLICATION-003 and PRODUCT-ADR-APPLICATION-004.
- Pipeline, application, learning, and UI ownership remain distinct.
- Provenance does not reach the normal PWA retrieval result.
- No decision-bearing ADR body is edited.
- ADR migration metadata matches completed specification reflection.
- Validation passes for every changed record.

## Verification

- Trace each changed normative statement and term definition to PRODUCT-ADR-APPLICATION-003 or PRODUCT-ADR-APPLICATION-004.
- Confirm PRODUCT-ADR-APPLICATION-001 and PRODUCT-ADR-APPLICATION-002 remain historical superseded records.
- Confirm no task evidence acts as decision authority.
- Search affected specifications for `Found`, previous publication, new publication, before switch, and after switch.
- Confirm pipeline publication-integrity ownership is not duplicated in application specifications.
- Confirm no SQL, table, ORM, transport, retry timing, or framework decision enters the specifications.
- Run available record and specification validation.
- Record working-tree evidence in `## Evidence`.

## Evidence

### Semantic verdict

All normative specification changes trace to PRODUCT-ADR-APPLICATION-003 or PRODUCT-ADR-APPLICATION-004.
No new design decisions were introduced.
No decision-bearing ADR body was modified.
ADR-003 and ADR-004 `migrated_to_spec` fields were set to `2026-06-26`; no other ADR content was changed.

### Changed specs

| spec | change summary |
|---|---|
| `spec:product` | Replaced deferred TASK-004-03 note with PRODUCT-ADR-APPLICATION-004 reference. Added ADR-004 to related specs. |
| `spec:product.application` | Added `## Definitions` for `application use case` and `persistence adapter`. Updated dependency diagram label "DB adapter" → "Persistence adapter". Updated Topics table summary "atomic replacement" → "transactional current-state publication". Replaced ADR-001 with ADR-003 and ADR-004 in related specs. |
| `spec:product.application.published_content` | Added `current published state` to concept model table. Replaced "Atomic replacement" section with "Transactional current-state publication" section, removing Before switch / After switch table and previous/new publication language. Replaced ADR-001 with ADR-003 in related specs. |
| `spec:product.application.learning_unit_selection` | Replaced `Found(complete_learning_unit)` with `Available(complete_learning_unit)`. Added `LearningUnitRef` annotation on port input. Added `## Definitions` for `LearningUnitRef`, `outbound retrieval port`, `Available`, `Unavailable`. Split layer table row into separate "Outbound selection operation" and "Outbound retrieval port" rows. Renamed "Database adapter" → "Persistence adapter" in layer table. Renamed "Database adapters" → "Persistence adapters" in domain-and-adapter-separation section. Added `### Outbound retrieval port` rules section reflecting ADR-004 adapter obligations. Replaced ADR-001 with ADR-003 and ADR-004 in related specs. |
| `spec:product.pipeline` | Added transactional commit obligations to Writer obligations: `PublicationHandoff` and `AvailabilityChange` each commit in one transaction; failed transaction leaves committed state unchanged; transaction syntax and technology are implementation details. |

### Explicit no-change judgments

| spec | reason |
|---|---|
| `spec:product.learning.learning_unit` | Owns learner-visible content and attribution. No stale application language. No change needed. |
| `spec:product.ui.learning_flow` | Owns transient queue and session state. No stale application language. No change needed. |

### ADR-to-spec trace table

| ADR decision | reflected in |
|---|---|
| ADR-003: one committed current published state | `spec:product.application.published_content` — `current published state` definition, transactional publication section |
| ADR-003: pipeline commits each published-content change in one transaction | `spec:product.pipeline` — Writer obligations transactional commit bullets |
| ADR-003: failed transaction leaves committed state unchanged | `spec:product.pipeline` — Writer obligations; `spec:product.application.published_content` — transactional publication section |
| ADR-003: `Available(complete_learning_unit) \| Unavailable` | `spec:product.application.learning_unit_selection` — concept model, definitions, outbound retrieval port section |
| ADR-003: `Available` and `Unavailable` semantics | `spec:product.application.learning_unit_selection` — definitions table |
| ADR-003: no runtime revision model | `spec:product.application.published_content` — removed Before switch / After switch table and previous/new publication language |
| ADR-003: pipeline owns validation and writes | `spec:product.application.published_content` — ownership rules; not duplicated in application |
| ADR-003: application use cases | `spec:product.application` — definitions table |
| ADR-004: application owns semantic outbound retrieval port | `spec:product.application.learning_unit_selection` — definitions, layer table, port rules section |
| ADR-004: outbound retrieval port is separate from bounded selection operation | `spec:product.application.learning_unit_selection` — layer table split into "Outbound selection operation" and "Outbound retrieval port" rows |
| ADR-004: persistence adapter implements port | `spec:product.application` — definitions table; `spec:product.application.learning_unit_selection` — layer table, port rules section |
| ADR-004: adapter returns result, not projection | `spec:product.application.learning_unit_selection` — port rules section |
| ADR-004: mapping/infrastructure failures propagate as technical failures | `spec:product.application.learning_unit_selection` — port rules section |
| ADR-004: persistence adapter does not decide availability | `spec:product.application.learning_unit_selection` — port rules section |

### Removed stale terminology

| stale term | location | replacement |
|---|---|---|
| `Found(complete_learning_unit)` | `spec:product.application.learning_unit_selection` concept model | `Available(complete_learning_unit)` |
| Before switch / After switch table rows | `spec:product.application.published_content` atomic replacement section | Transactional current-state publication table |
| "previous publication" / "new publication" observable-state model | `spec:product.application.published_content` | "one committed current published state" |
| "Database adapter" in layer table | `spec:product.application.learning_unit_selection` | "Persistence adapter" |
| "Database adapters" in domain-and-adapter-separation | `spec:product.application.learning_unit_selection` | "Persistence adapters" |
| "DB adapter" in dependency diagram | `spec:product.application` | "Persistence adapter" |
| "atomic replacement" in Topics table summary | `spec:product.application` | "transactional current-state publication" |
| Deferred TASK-004-03 reference in root diagram note | `spec:product` | PRODUCT-ADR-APPLICATION-004 reference |
| PRODUCT-ADR-APPLICATION-001 as current authority | `spec:product.application`, `spec:product.application.published_content`, `spec:product.application.learning_unit_selection` | PRODUCT-ADR-APPLICATION-003 and PRODUCT-ADR-APPLICATION-004 |

Stale-language scoped search results (active application and pipeline specs):

| search term | result |
|---|---|
| `Database adapter` | No matches |
| `Database adapters` | No matches |
| `DB adapter` | No matches |
| `DB adapters` | No matches |
| `atomic replacement` | No matches |
| `Found(` | No matches |
| `Before switch` | No matches |
| `After switch` | No matches |
| `previous complete projection` | No matches |
| `new complete projection` | No matches |
| `PRODUCT-ADR-APPLICATION-001` | No matches in active specs |
| `PRODUCT-ADR-APPLICATION-002` | No matches in active specs |
| `previous publication` | One match in `spec:product.pipeline` — valid non-goals statement: "The first MVP does not require … previous publications …". Classified: unrelated occurrence. |

### Terminology ownership

| term | canonical owner |
|---|---|
| `LearningUnitRef` | `spec:product.application.learning_unit_selection` |
| `application use case` | `spec:product.application` |
| `outbound selection operation` | `spec:product.application.learning_unit_selection` (layer table; bounded selection distinct from retrieval port) |
| `outbound retrieval port` | `spec:product.application.learning_unit_selection` |
| `persistence adapter` | `spec:product.application` |
| `current published state` | `spec:product.application.published_content` |
| `Available` | `spec:product.application.learning_unit_selection` |
| `Unavailable` | `spec:product.application.learning_unit_selection` |

### Validation results

```
[strict]  All 20 file(s) OK.
```

### git diff --check

No whitespace errors. LF/CRLF conversion warnings are pre-existing in the repository.

### git status --short

Modified specs: `product/records/spec/application/index.md`, `product/records/spec/application/learning-unit-selection.md`, `product/records/spec/application/published-content.md`, `product/records/spec/index.md`, `product/records/spec/pipeline/index.md`.
ADR migration metadata updated: `PRODUCT-ADR-APPLICATION-003`, `PRODUCT-ADR-APPLICATION-004` (untracked new files; only `migrated_to_spec` field changed).

### Blockers

None.
