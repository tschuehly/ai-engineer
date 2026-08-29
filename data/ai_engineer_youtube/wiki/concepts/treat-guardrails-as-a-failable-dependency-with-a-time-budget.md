# Treat Guardrails as a Failable Dependency With Its Own Time Budget

Summary: Guardrails are usually designed as policy and operated as if they were free and always up. They are services: they go down, they add latency, and their placement in the request path is a design decision. Decide fail-open versus fail-closed in advance, bound their time so the model stays the rate-determining step, give them their own fallbacks, and pick their position knowingly.

Use when:
- Adding prompt-injection, PII, toxicity, or policy checks to a production request path.
- A guardrail provider outage is about to decide, by default, whether your product stays up.
- Latency work has stalled and the checks around the model turn out to be part of the budget.
- Choosing between pre-hook, parallel, and post-hook placement for a safety check.

Details:
- **The reframe.** Guardrails exist for "preventing your services from prompt injection attacks, keeping PII filters in place, having toxicity filters, keeping the LLMs to stop swearing at your customers" — but "just like a model provider, there are trade-offs, too. Guardrails are just like another service that can go down that can be unreliable." ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 09:45-10:20)
- **Fail open or fail closed is a decision you make once, deliberately.** "When I say fail open, you can still serve the request even if your guardrails are down. Fail close, you block the request and say, hey, I'm not available. That's the trade-off between availability and security." There is "no universal answer. It really depends on your use case" — a toxicity filter that is down may still allow serving; a PII filter arguably may not. (10:20-10:54)
- **The default rule.** "The default choice should be the worst case that you can live with." Whatever the system does when nobody is watching should be the outcome you would accept, with the better outcome reached by explicit configuration rather than by luck. (10:54-11:00)
- **Time budget: the model, not the check, sets the pace.** "Your request should never be bound by your guardrail timing. It should always be the LLM that is the rate determining step. So make sure that you have timeouts in place and those guardrails run with a specific time budget." A guardrail without its own timeout can turn a safety feature into the slowest thing in the request. (11:03-11:38)
- **Guardrails need fallbacks for the same reason models do.** "We always discuss fallbacks with regards to model providers, but guardrails are critical services too where you can consider fallbacks, have secondary provider, secondary checks, cache decisions, to keep your service available when a guardrail provider is down." Cached decisions are the cheap one — a previously-rendered verdict on the same input costs nothing to reuse. (11:38-12:02)
- **Three placements with three different costs.** *Pre-hook* runs on the input before the model — "probably the safest, but it does add serial latency to your requests." *Parallel* runs concurrently with generation and is the latency-preserving option, but "streaming wouldn't work well here with parallel. So if you're specially producing structured output, please don't stream them… run these guardrails concurrently for your structured outputs." *Post-hook* is "best for output monitoring, auditing your outputs." Note that the parallel option is only genuinely safe when the output is not already reaching the user — the same commitment problem as [Streaming Forecloses the Provider Fallback](streaming-forecloses-the-provider-fallback.md). (12:04-12:47)
- **How this relates to the coverage question.** Where [LLM Guardrails Need Checkpoints at Every Untrusted Boundary](llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md) argues about *how many* checkpoints and *where* the untrusted input enters, this page is about the operational properties of each checkpoint once it exists. Adding checkpoints multiplies the failure surface and the serial latency, so the two arguments pull against each other and should be resolved explicitly.
- **Caveat.** No incident, latency figure, or availability number for any guardrail is reported, and the fail-open/fail-closed guidance is worked through for exactly one example (toxicity). The talk also does not address the case that makes the decision hardest: a guardrail that is up but degraded, returning verdicts of unknown quality, which neither a timeout nor a fail-open switch detects.

Related topics:
- [Security](../topics/security.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [LLM Guardrails Need Checkpoints at Every Untrusted Boundary](llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md)
- [Fine-Tuned Encoder Discriminators Make Low-Latency Guardrails Practical](fine-tuned-encoder-discriminators-make-low-latency-guardrails-practical.md)
- [Enforce Deterministic Guardrails Around Sensitive Tool Calls](enforce-deterministic-guardrails-around-sensitive-tool-calls.md)
- [An LLM Gateway Cannot Maximize Availability, Latency, Guardrails, and Cost at Once](an-llm-gateway-cannot-maximize-availability-latency-guardrails-and-cost.md)
- [Streaming Forecloses the Provider Fallback](streaming-forecloses-the-provider-fallback.md)
- [Layer AI Application Metrics From Guardrail Compliance to System Health](layer-ai-application-metrics-from-guardrail-compliance-to-system-health.md)
- [Fail Loudly and Bill Only for Successful Results](fail-loudly-and-bill-only-for-successful-results.md)

Sources:
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 09:45-12:47
