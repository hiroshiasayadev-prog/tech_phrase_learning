# PRODUCT-TASK-APPLICATION-003-05: Review complete-shuffle selection design

- **id**: PRODUCT-TASK-APPLICATION-003-05
- **status**: done
- **date**: 2026-06-26
- **work_item**: PRODUCT-WORK-APPLICATION-003
- **source_requirement**: PRODUCT-REQ-APPLICATION-001
- **estimate**: 0.5d
- **depends_on**:
  - PRODUCT-TASK-APPLICATION-003-04
- **outputs**:

## Goal

Independently verify that the complete-shuffle selection design is consistent and implementation-ready.

## Work

1. Use a reviewer who did not implement PRODUCT-TASK-APPLICATION-003-02 through PRODUCT-TASK-APPLICATION-003-04.
2. Review every impact ref from PRODUCT-WORK-APPLICATION-003.
3. Verify `SelectionScope`, the first-MVP `all` scope, and the maximum of 100 references.
4. Verify within-queue uniqueness, later repetition, and fewer-than-maximum behavior.
5. Verify the absence of reservation, backend queue identity, queue position, and queue history.
6. Verify bounded random selection semantics and database-side execution compatibility.
7. Verify adapter obligations for availability, scope, maximum count, uniqueness, and ordering.
8. Verify domain validation and invalid-result handling.
9. Verify extension boundaries for source, topic, discussion, difficulty, and learner history.
10. Check application, published-content, and UI ownership for contradictions or duplication.
11. Check that no concrete persistence, transport, algorithm, or framework decision entered the design scope.
12. Record findings by severity and give a final `PASS` or `NEEDS REVISION` verdict.
13. Re-run the review after any blocking finding is corrected.

Do not implement fixes during the independent review.

## Done condition

- The review covers every completion condition in PRODUCT-WORK-APPLICATION-003.
- Findings identify exact refs and conflicting claims.
- The review confirms that `all` does not require every eligible reference in one queue.
- The review confirms that database-side bounded selection remains possible.
- The review confirms that selection rules remain adapter-independent.
- Blocking findings are corrected and independently re-reviewed.
- The final verdict is `PASS`.
- The evidence states whether implementation planning may begin for this module.

## Verification

- Confirm reviewer independence from T02 through T04 implementation.
- Trace every reviewed claim to a current ADR or specification.
- Confirm validation results for every modified specification.
- Confirm the final verdict and remaining non-blocking advisories are explicit.

## Evidence

### Initial provisional review

- **Verdict**: NEEDS REVISION.
- **Reviewer**: `qwen3.6-27b:q4_k_m-tools` through the local Ollama review boundary.
- The reviewer did not implement PRODUCT-TASK-APPLICATION-003-02 through PRODUCT-TASK-APPLICATION-003-04.
- One blocking finding and one non-blocking advisory were reported.
- The blocking finding was corrected before the final independent re-review.

### Findings

| severity | ref | section | finding | required action |
|---|---|---|---|---|
| Blocking | `spec:product.ui.learning_flow` | `### Main screen` and `### Learning queue` | The application may validly return an empty reference array, but the UI contract defines no terminal or stable transition for an empty initial queue. Queue exhaustion always triggers another queue request, so repeated empty results can create an undefined reacquisition loop. | Define the PWA behavior for an empty initial queue and for an empty replacement queue after exhaustion. Keep the decision in the UI flow contract. |
| Non-blocking | PRODUCT-ADR-UI-001 | `## Consequences` | The statement that backend selection, queue production, availability, API, and repository contracts remain undecided is historically stale after PRODUCT-ADR-APPLICATION-001 and the application specifications established those boundaries. | Judge whether to add a narrow historical clarification. Do not change the accepted UI ownership decision. |

### Completion-condition coverage

| condition | result | evidence |
|---|---|---|
| `SelectionScope` has an implementation-independent meaning. | PASS | `spec:product.application.learning_unit_selection` defines `All` and `Constrained(non_empty_constraints)`. |
| `All` includes every currently available candidate without requiring a full-corpus queue. | PASS | `spec:product.application` and `spec:product.application.learning_unit_selection`. |
| Maximum, exact smaller results, uniqueness, ordering, and later repetition are explicit. | PASS | `spec:product.application.learning_unit_selection`. |
| Queue issuance creates no reservation or backend queue state. | PASS | PRODUCT-ADR-APPLICATION-001 and `spec:product.application.learning_unit_selection`. |
| Bounded randomized selection remains database-compatible and adapter-independent. | PASS | PRODUCT-ADR-APPLICATION-001 and `spec:product.application.learning_unit_selection`. |
| Adapter obligations cover availability, scope, exact cardinality, uniqueness, and randomized ordering. | PASS | `spec:product.application.learning_unit_selection`. |
| Observable validation and invalid-result handling are transport-independent. | PASS | `spec:product.application.learning_unit_selection`. |
| Selection-time and retrieval-time availability are distinct. | PASS | `spec:product.application.learning_unit_selection` and `spec:product.application.published_content`. |
| Future non-history constraints intersect without moving queue state. | PASS | `spec:product.application.learning_unit_selection`. |
| Learner-history selection remains deferred. | PASS | `spec:product.application.learning_unit_selection`. |
| Availability, selection, and PWA state ownership are separated. | PASS | Application, published-content, and UI specifications. |
| No concrete persistence, transport, framework, or exact algorithm entered the contract. | PASS | All reviewed impact refs. |
| A valid empty queue has a complete UI transition. | FAIL | `spec:product.ui.learning_flow` defines reacquisition on exhaustion but no empty-result state or termination rule. |

### Reviewer-output verification

- The blocking finding is supported by two current contracts.
- `spec:product.application.learning_unit_selection` accepts a zero-length result as valid.
- `spec:product.ui.learning_flow` keeps the main screen visible until a first unit loads and always reacquires after queue exhaustion.
- No rule handles a valid empty initial result or repeated empty replacement results.
- The missing transition prevents deterministic PWA implementation and can cause unbounded reacquisition.
- The ADR advisory does not change the review verdict and does not require changing the accepted UI ownership decision.

### Correction applied

- The blocking empty-result transition gap was corrected in `spec:product.ui.learning_flow`.
- A successful empty initial queue now shows `Quiz list was empty.` with `Back to main`.
- A successful empty replacement queue ends the current learning flow and shows the same empty-queue screen.
- Successful empty results trigger no automatic or manual queue retry.
- Queue-acquisition request failures continue to use the existing retry behavior.
- The blocking finding is corrected but not yet independently re-reviewed.
- The PRODUCT-ADR-UI-001 advisory remains non-blocking and unresolved.

### Final independent re-review

- **Verdict**: PASS.
- **Reviewer**: Codex.
- **Blocking findings**: None.
- **Non-blocking findings**: One stale historical statement in PRODUCT-ADR-UI-001 `## Consequences`.
- Every PRODUCT-WORK-APPLICATION-003 impact ref and completion condition passed.
- The previous empty-result blocking finding is closed.
- Implementation planning may begin for this module.

### Final coverage

- `SelectionScope`, first-MVP `All`, future intersection semantics, and learner-history deferral are complete.
- Queue cardinality, zero-result behavior, uniqueness, later repetition, randomized ordering, and absence of `eligible_count` in results are complete.
- Queue issuance creates no reservation, backend queue identity, backend position, backend history, or durable learner progress.
- Database-side bounded selection and adapter-independent domain rules remain possible.
- Adapter obligations and application-observable validation are explicit.
- Invalid observable arrays are rejected without normalization.
- Selection-time and retrieval-time availability are distinct.
- Successful empty initial and replacement queues show the empty-queue screen without queue retry.
- Queue-acquisition request failures continue to use retry behavior.
- Application, published-content, and UI ownership are consistent and not duplicated.
- No persistence, transport, framework, SQL, or exact randomization decision entered the contract.

### Remaining advisory

- PRODUCT-ADR-UI-001 `## Consequences` still states that backend selection, queue production, availability, API, and repository contracts remain undecided.
- The statement is stale historical wording only.
- The statement does not contradict the accepted UI ownership decision.
- The advisory does not block implementation planning or work-item closure.

### Validation status

- Design Records MCP does not index the target application and UI refs.
- Filesystem rereads confirmed the corrected current text and canonical references.
- No CLI validator result is available in this tool environment.
- Final independent review evidence supplied by Codex records `PASS` with no blocking findings.
