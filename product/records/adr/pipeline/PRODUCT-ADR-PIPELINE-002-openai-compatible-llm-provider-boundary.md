# PRODUCT-ADR-PIPELINE-002: Use an OpenAI-compatible LLM provider boundary

- **status**: accepted
- **date**: 2026-06-24
- **depends_on**: [PRODUCT-ADR-PIPELINE-005]
- **supersedes**: []
- **migrated_to_spec**: 2026-06-24

## Context

The product will use LLMs for bounded content-processing tasks.

Expected tasks include:

- phrase candidate classification;
- phrase extraction;
- explanation generation;
- quiz draft generation;
- lightweight cleanup and formatting.

The product may use hosted APIs during early development.
Hosted APIs can reduce setup cost and may be cheaper at low volume.

The product may also use local inference.
Local inference can support offline operation, privacy, and cost control.

Hosted and local providers expose different model names, authentication methods, capabilities, and operational limits.
Direct vendor integration would couple product logic to one provider.

## Decision

The product will define an internal LLM provider boundary.

Application services will call the internal boundary instead of vendor SDKs.
Provider adapters will translate internal requests to concrete backends.

The baseline adapter contract will use an OpenAI-compatible chat-completion request and response shape.

The initial provider set may include:

- hosted OpenAI-compatible APIs;
- a local OpenAI-compatible endpoint;
- test and fake providers.

Provider adapters own:

| concern | responsibility |
|---|---|
| Base URL | Select the concrete hosted or local endpoint. |
| Authentication | Supply provider-specific credentials or omit credentials for local endpoints. |
| Model identifier | Map logical model roles to provider-specific model names. |
| Request translation | Convert internal messages and options to the provider request. |
| Response translation | Convert provider responses to the internal response type. |
| Capability handling | Reject or adapt unsupported structured output, tool use, or other optional features. |
| Error mapping | Convert provider errors into stable application error categories. |

Vendor-specific SDK calls must remain inside provider adapters.

API compatibility means transport compatibility only.
The product will not assume equivalent output quality or behavior across models.

LLM output is untrusted input.
Application code will validate structured output against explicit schemas.
Invalid output may be retried, rejected, or sent to review.

## Rationale

One provider boundary allows the product to change backends without changing learning-domain logic.

An OpenAI-compatible shape has broad support across hosted and local inference servers.
The shape reduces adapter complexity for the initial product.

Logical model roles separate product behavior from concrete model names.
The separation supports cost and quality experiments without broad code changes.

Schema validation contains model variance at the application boundary.
The validation also prevents transport compatibility from being mistaken for behavioral compatibility.

## Rejected alternatives

| alternative | rejection reason |
|---|---|
| Integrate one hosted provider directly | Product logic would depend on one vendor's SDK and model naming. |
| Use local inference only | Local setup and hardware constraints would slow early validation. |
| Use hosted APIs only | The product would lose offline, privacy, and local-cost options. |
| Define a provider contract around every vendor feature | The initial product does not need a complete cross-vendor capability model. |
| Assume all OpenAI-compatible models behave the same | Request compatibility does not guarantee equivalent output or feature support. |

## Consequences

- Application services depend on an internal LLM provider interface.
- Hosted and local backends can be selected by configuration.
- Concrete model names remain outside learning-domain logic.
- Provider capability differences require explicit handling.
- Structured outputs require schema validation.
- Provider-specific integration tests remain necessary.
- Cost, latency, and quality benchmarks can compare providers through one application path.
- A later spec may define the stable provider contract after implementation evidence exists.

## Evidence

- Early product operation is expected to have low and variable LLM volume.
- Cheap hosted APIs may cost less than maintaining local inference at that stage.
- Local inference remains relevant for offline operation, privacy, and deployment control.
- Hosted and local inference servers can expose OpenAI-compatible chat-completion endpoints.
- Phrase-processing tasks are bounded and suitable for provider-level comparison.
