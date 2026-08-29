# Streaming Forecloses the Provider Fallback

Summary: The moment the first token reaches the client, you are committed to the provider that produced it. Tokens already sent cannot be recalled, so the multi-provider fallback you carefully built is unavailable exactly when the request fails mid-generation — which is why "something went wrong, please try again" exists as a product surface rather than as a bug.

Use when:
- Deciding whether an endpoint should stream, and what that decision costs in reliability.
- Explaining to product or design why a partial answer cannot be silently rescued by a second provider.
- Designing the error UX for a streaming AI feature, or auditing one that just shows a generic failure.
- Choosing where guardrails run, since the parallel placement has the same conflict with streaming.

Details:
- **The commitment is irreversible and mid-stream.** "Once you have decided to go with provider A, you have to continue going with provider A. You cannot mid-stream change the providers. Whatever has been sent to the client, it's done." ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 05:35-05:50)
- **The generic error message is the visible price.** "And that's where the something went wrong message, that's the one that you see. It's not because of laziness. It's by design… and it's one of the trade-offs." Reading it as an unimplemented feature is the mistake; it is the only honest thing a committed stream can say. (05:47-05:55, 00:20-00:48)
- **Streaming is still correct for some use cases, and the reason is stated plainly.** "Nobody wants to wait for 30 seconds to have a wall of text appear in front of them. So there are use cases where streaming is absolutely required. But it comes at a cost. You trade away your levers." The decision is perceived latency against retained control, not good against bad. (05:16-05:35)
- **The same conflict decides guardrail placement.** Running guardrails concurrently with generation is the low-latency option, but "streaming wouldn't work well here with parallel. So if you're specially producing structured output, please don't stream them… run these guardrails concurrently for your structured outputs." Structured output is the case where streaming buys the user nothing anyway, since a half-parsed JSON object is not a partial answer. (12:28-12:47)
- **A practical decision rule falls out.** Endpoints whose output a human reads as it arrives should stream and accept an unrescuable failure class; endpoints whose output is consumed whole — structured output, tool arguments, anything a program parses — should not stream, and in exchange keep per-request fallback, parallel guardrails, and post-hoc validation available. See [Prefer Per-Request Fallback to Retries and Circuit Breakers for LLM Calls](prefer-per-request-fallback-to-retries-and-circuit-breakers-for-llm-calls.md) for what is being preserved.
- **What the talk does not address.** Buffering the first N tokens before releasing them — trading a small amount of time-to-first-token for a rescuable window — is an obvious middle path and is not discussed. Nor is resuming a failed stream on a second provider by replaying the partial output as context, which some products do at the cost of a visible seam. Treat the binary framing as the default, not as proof no middle exists.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Prefer Per-Request Fallback to Retries and Circuit Breakers for LLM Calls](prefer-per-request-fallback-to-retries-and-circuit-breakers-for-llm-calls.md)
- [An LLM Gateway Cannot Maximize Availability, Latency, Guardrails, and Cost at Once](an-llm-gateway-cannot-maximize-availability-latency-guardrails-and-cost.md)
- [Treat Guardrails as a Failable Dependency With Its Own Time Budget](treat-guardrails-as-a-failable-dependency-with-a-time-budget.md)
- [Use Resumable Streams as the UI Boundary for Durable Agents](use-resumable-streams-as-the-ui-boundary-for-durable-agents.md)
- [Sort Failures by Whether the User Can Retry](sort-failures-by-whether-the-user-can-retry.md)
- [Read the Stop Reason Before You Read the Answer](read-the-stop-reason-before-you-read-the-answer.md)

Sources:
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 00:20-00:48, 05:16-05:55, 12:28-12:47
