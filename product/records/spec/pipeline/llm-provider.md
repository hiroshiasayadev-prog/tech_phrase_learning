# Concept: LLM provider boundary

- **id**: `spec:product.pipeline.llm_provider`
- **status**: draft
- **date**: 2026-06-28
- **parent**: `spec:product.pipeline`

## What this is

Pipeline boundary for invoking hosted, local, fake, or test language-model providers through one internal interface.
The boundary isolates provider-specific transport and capability differences from Pipeline stage semantics.

## Non-goals

- Permanent provider or model selection.
- Equivalent behavior or quality across compatible providers.
- Exact prompts, inference parameters, or token budgets.
- Retry counts, fallback order, or provider-switching policy.
- Vendor-specific SDK use outside provider adapters.

## Concept model

| concept | contract |
|---|---|
| Internal provider boundary | Pipeline-facing interface used by generation and semantic-evaluation stages. |
| OpenAI-compatible baseline | Chat-completion transport shape used as the initial adapter baseline. |
| Provider adapter | Boundary component that translates between internal requests and one concrete backend. |
| Logical model role | Pipeline role mapped by configuration to a provider-specific model identifier. |
| Provider capability | Optional provider behavior that must be supported, adapted, or rejected explicitly. |
| Untrusted provider output | Provider result that requires deterministic validation before semantic acceptance. |

## Rules

### Internal boundary

- Pipeline generation and evaluation stages must call the internal provider boundary.
- Pipeline stage semantics must not call vendor SDKs directly.
- Hosted OpenAI-compatible APIs, local compatible endpoints, test providers, and fake providers may implement the boundary.
- The baseline adapter contract must use an OpenAI-compatible chat-completion request and response shape.
- API compatibility means transport compatibility only.
- The Pipeline must not assume equivalent quality, capability, or behavior across compatible providers.

### Provider adapter responsibilities

| concern | adapter responsibility |
|---|---|
| Endpoint | Select the concrete hosted or local base URL. |
| Authentication | Supply provider-specific credentials or omit them when supported. |
| Model mapping | Map logical model roles to provider-specific model identifiers. |
| Request translation | Convert internal messages and options into provider requests. |
| Response translation | Convert provider responses into the internal response representation. |
| Capability handling | Reject or adapt unsupported structured output, tool use, or optional features. |
| Error mapping | Convert provider failures into stable Pipeline-facing failure categories. |

- Vendor-specific credentials, model names, and SDK types must remain inside adapters or implementation configuration.
- Provider capability differences must be handled explicitly.
- Logical model roles must remain independent from concrete model names.

### Output trust and failure boundary

- Every provider-produced structure is untrusted input.
- Deterministic validation must occur before semantic acceptance.
- Structurally unusable, malformed, or identity-invalid output must become `invalid_provider_output` under `spec:product.pipeline.validation`.
- Provider inability to complete the requested operation must become `provider_failure` under `spec:product.pipeline.validation`.
- A valid semantic rejection must not be mapped to provider failure.
- Retryability, finite exhaustion, fallback, and provider switching belong to `spec:product.pipeline.orchestration`.

## Boundary

| concern | owner |
|---|---|
| Provider-neutral invocation and adapter isolation | `spec:product.pipeline.llm_provider`. |
| Stage input, output, and semantic meaning | The owning Pipeline stage specification. |
| Deterministic and semantic result classification | `spec:product.pipeline.validation`. |
| Retry, fallback, and exhaustion | `spec:product.pipeline.orchestration`. |
| Provider, prompt, and behavior evidence | `spec:product.pipeline.artifact_identity_and_provenance`. |
| Concrete SDK, endpoint, model, and credentials | Implementation and configuration. |

## Related specs

| ref | relation |
|---|---|
| `spec:product.pipeline` | Parent Pipeline overview. |
| `spec:product.pipeline.content_generation` | Uses the provider boundary for bounded generation tasks. |
| `spec:product.pipeline.path_validation` | Uses the provider boundary for semantic path evaluations. |
| `spec:product.pipeline.validation` | Classifies provider results and validates untrusted output. |
| `spec:product.pipeline.orchestration` | Owns retry, fallback, and exhaustion. |
| `spec:product.pipeline.artifact_identity_and_provenance` | Retains stage-specific provider and behavior evidence. |
| PRODUCT-ADR-PIPELINE-002 | Establishes the internal OpenAI-compatible provider boundary. |
| PRODUCT-ADR-PIPELINE-022 | Establishes provider-failure retry and exhaustion semantics. |
| PRODUCT-ADR-PIPELINE-024 | Establishes generation-provider and evaluator-provider rerun boundaries. |
