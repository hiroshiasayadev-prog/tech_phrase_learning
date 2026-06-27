# PRODUCT-TASK-PIPELINE-001-06: Define orchestration, retry, and completion contracts

- **id**: PRODUCT-TASK-PIPELINE-001-06
- **status**: not_started
- **date**: 2026-06-27
- **work_item**: PRODUCT-WORK-PIPELINE-001
- **source_requirement**: PRODUCT-REQ-PRODUCT-001
- **estimate**: 2.5d
- **depends_on**:
  - PRODUCT-TASK-PIPELINE-001-05
- **outputs**: []

## Goal

Define stage orchestration, dependency order, retry, rejection, rerun, reuse, partial failure, batch continuation, and completion semantics.

## Work

1. Read T02 through T05 accepted decisions and stage contracts.
2. Define orchestration inputs and outputs for one source discussion and one processing batch.
3. Define stage dependency order from acquisition through publication.
4. Distinguish deterministic stages from model stages and publication-decision stages.
5. Define reusable retained-source and reusable summary boundaries.
6. Define rerun boundaries after source replacement, prompt change, provider change, validator change, gate change, and failed publication.
7. Define which current intermediate artifacts must be retained and which may be transient or overwritten.
8. Define retryable and non-retryable outcomes for acquisition, provider output, validation, and publication stages.
9. Define bounded retry without selecting retry count, delay, timeout, or backoff algorithms.
10. Define invalid provider output, exhausted retry, incomplete unit, contradictory result, and rejected unit outcomes.
11. Define partial failure behavior and the boundary between one unit failure and batch continuation.
12. Define whether later independent units may continue after a source, path, generation, validation, or publication failure.
13. Define completion semantics for source processing, path processing, unit generation, gate evaluation, and publication.
14. Require no partial published-content mutation after any failed precondition or write.
15. Define current-run diagnostics without requiring historical intermediate retention.
16. Create or update Pipeline ADRs when current authority does not determine observable orchestration semantics.
17. Keep workflow engines, queues, concurrency models, scheduling, logging stacks, and deployment outside the contract.
18. Update `outputs` and Evidence with accepted ADRs or specification inputs.

## Done condition

- Orchestration inputs, outputs, and stage dependency order are explicit.
- Deterministic, model, validation, gate, and publication stages remain distinct.
- Rerun and reuse boundaries are explicit for every material change or failure class.
- Required current intermediates and transient artifacts are explicit.
- Retryable and non-retryable outcomes are explicit without concrete retry timing.
- Bounded retry, exhaustion, rejection, and incomplete-unit handling are explicit.
- Contradictory validation results cannot continue to publication.
- One unit failure and batch continuation have an explicit boundary.
- Completion semantics are explicit for each processing scope.
- Current-run diagnostics remain available without historical replay requirements.
- Every new normative decision has accepted Pipeline ADR authority.
- Concrete orchestration technology remains deferred.

## Verification

- Confirm each stage consumes only declared upstream outputs.
- Confirm rerun does not silently change stable valid-path or learning-unit identity.
- Confirm source reuse and current-only retention remain consistent with PRODUCT-ADR-PIPELINE-005.
- Confirm bounded retry cannot become unbounded processing.
- Confirm one failed unit cannot produce incomplete published state.
- Confirm batch continuation never bypasses required gate dimensions.
- Confirm no workflow engine, queue technology, or concurrency implementation enters the contract.
- Run relevant record validation, strict specification validation, `git diff --check`, and `git status --short`.

## Evidence

TBD
