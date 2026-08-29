# Prefer Per-Request Fallback to Retries and Circuit Breakers for LLM Calls

Summary: The standard remedy for an unreliable dependency — retry with exponential backoff and jitter, then trip a circuit breaker — misfires on LLM calls for three independent reasons. Route the failing request to a second provider instead, and demote circuit breaking to a slower background job that parks a persistently failing provider in a cool-down.

Use when:
- Writing the failure-handling path for model calls in a gateway, SDK, or agent runtime.
- A retry policy copied from a microservice client is being applied to an LLM API.
- Choosing between sequential fallback and firing both providers in parallel.
- Deciding where provider health state lives in a multi-instance fleet.

Details:
- **Why the reflex is wrong, in three separable reasons.** "Retrying an LLM API eats into your latency budget really fast" — the calls are slow, so a retry is not cheap the way a retried REST call is. "Tripping over a circuit breaker when you have another perfectly fine model provider to route to doesn't make sense. You should use the second model provider" — breakers assume the dependency is irreplaceable, and here it is not. And "blind retries just multiply your cost and your tail latencies" — the calls are also expensive, so amplification shows up on the bill as well as the clock. ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 02:24-02:58)
- **The replacement is per-request, not per-provider.** "You can actually try model provider A and then in sequence try model provider B if your request to model provider A fails." The unit of failover is the individual request, so a single bad response is repaired without changing global routing state or waiting for a failure threshold to accumulate. (03:00-03:16)
- **The parallel variant, and its exact price.** "Another option to consider here is you can fire requests to both the providers in parallel. But that's only if you're highly highly obsessed with latencies because that's just going to double your cost." (03:16-03:27)
- **Circuit breaking survives in a demoted role.** "If you know that your primary has been failing for some time, it doesn't make sense to try it again. You take it out of the load balancer or your request path and put it in a cool down and then after a few minutes have passed, try putting that back again." The breaker no longer decides what happens to *this* request — the fallback does — it decides which providers are worth trying first, on a minutes timescale. (03:28-03:52)
- **Where the failure counters live is a real design choice with a stated trade.** In-memory per serving instance, or shared infrastructure across the fleet. "If you want quick failovers, then fleetwide helps" — the whole fleet learns from one instance's failures immediately — while with local counters "whenever you change your deployment size, your configuration and your expectations change," because a threshold of N failures per instance means something different at ten instances than at a hundred. (03:53-04:35)
- **The precondition this pattern rests on is that streaming has not started.** Once tokens are on the wire the fallback is gone regardless of how it is configured; see [Streaming Forecloses the Provider Fallback](streaming-forecloses-the-provider-fallback.md). (05:35-05:55)
- **Caveats.** Nothing here is measured — no failover rate, latency impact, or incident count is reported, and the three reasons are argued from the properties of LLM calls rather than from observed outcomes. The pattern also assumes the second provider can actually serve the request, which is a separate piece of work: see [Your Fallback Provider Is Under-Tested and Under-Provisioned](your-fallback-provider-is-under-tested-and-under-provisioned.md). And per-request fallback does nothing about the failure class where the provider responds successfully but slowly, which is handled by timeouts and hedging instead.


- **A product-level instance of the same pattern, with the ordering pinned per task rather than globally.** DigitalOcean's router gives each named task a model pool and a selection policy. "Manual ranking" pins a preferred model and degrades into a failover chain — "I really want to always route to GLM 5.2 unless it's down… If GLM fails, it'll fail over to GPT-5.2" — while a "fastest" policy picks "whichever one's been fastest" over a recent window, which is this page's demoted circuit breaker stated as a positive selection rule instead of a cool-down ([Kamath & Gillam](../sources/20260822_FvxY8oPoI8o.md), 07:10-07:52). The addition worth taking is that the fallback list is *per task*, so the substitute for a code-generation call is a peer coding model rather than whatever the gateway's global second provider happens to be; see [Give Each Task a Model Pool With an Explicit Selection Policy](give-each-task-a-model-pool-with-an-explicit-selection-policy.md). The addition worth distrusting is that "if GLM fails" is never defined — no timeout, no error class, no behaviour on a partially streamed response.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Your Fallback Provider Is Under-Tested and Under-Provisioned](your-fallback-provider-is-under-tested-and-under-provisioned.md)
- [Streaming Forecloses the Provider Fallback](streaming-forecloses-the-provider-fallback.md)
- [Track Latency and Timeouts Per Model Class Per Route](track-latency-and-timeouts-per-model-class-per-route.md)
- [Wrap agent calls with circuit breakers and compensation](wrap-agent-calls-with-circuit-breakers-and-compensation.md)
- [Contain Retry Amplification Before It Becomes a Compute Incident](contain-retry-amplification-in-agent-loops.md)
- [Abstract LLM Inference Behind One Routing API](abstract-llm-inference-behind-one-routing-api.md)
- [An LLM Gateway Cannot Maximize Availability, Latency, Guardrails, and Cost at Once](an-llm-gateway-cannot-maximize-availability-latency-guardrails-and-cost.md)
- [Give Each Task a Model Pool With an Explicit Selection Policy](give-each-task-a-model-pool-with-an-explicit-selection-policy.md)

Sources:
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 01:46-01:57, 02:03-04:35, 05:35-05:55
- [Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean](../sources/20260822_FvxY8oPoI8o.md), 07:10-07:52
