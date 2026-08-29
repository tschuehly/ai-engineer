# Track Latency and Timeouts Per Model Class Per Route

Summary: A gateway serving embeddings, classification, chat, and reasoning in one fleet has no meaningful aggregate latency — the number averages workloads whose normal operating ranges differ by an order of magnitude or more. Track P99 per model per route, set timeouts at the same granularity, and treat a missing timeout as the most likely cause of a silent outage.

Use when:
- Defining SLOs, dashboards, or alerts for a service that fronts multiple model classes.
- A latency regression is invisible in aggregate but users on one route are complaining.
- Setting timeout values for model calls, or discovering there are none.
- Planning for reasoning-model or router-model traffic whose duration you cannot predict.

Details:
- **Latency failures are the quiet class.** "Availability failures are right in your face. They fail. You get alarmed. You get paged. But high latencies can be the quiet ones. And they need to receive more love than tuning your services for just availability." ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 06:30-06:52)
- **The mixed-workload problem is what makes the aggregate meaningless.** One gateway carries embedding requests "that take just less than a second," classification "less than a second," "chat requests taking 3 seconds and reasoning requests taking a long time." Asked whether the audience measures aggregate service latency, Manuja calls it a trick question: "You shouldn't. It doesn't make sense. It's a lie. You should be tracking your P99 per model per route, not a gateway wide number." (06:54-07:40)
- **The line that makes it memorable and portable.** "A reasoning model's normal is actually a chat model's outage." Any threshold that is correct for one is wrong for the other in a way no percentile over the combined population can fix. (08:02-08:16)
- **Timeouts get the same granularity, and their absence is named as the top cause of silent failure.** "Set timeouts on per model class per route… that's the number one root cause of your silent outage. If you don't have a timeout, your gateway thinks your request is being happily served while it is not." A missing timeout is worse than a wrong one because the system reports health while a caller waits indefinitely. (07:41-08:02)
- **Reasoning and router models are where this gets genuinely hard, and the talk is honest that there is no fix.** They are nondeterministic — "you cannot set the temperature to zero in many cases and the same prompt can take somewhere from 2 seconds to 60 seconds and we've seen that in production where P99 suddenly popped to 60 seconds for no good reason." Router models add a second layer, since "they hide that abstraction behind you. Like they pick which models to run." Two partial answers: "at least start with fixing the reasoning level per route," and pin down whatever the router leaves free, making "requests as deterministic as possible with an undeterministic system." (08:17-09:22)
- **Hedging is the tail mitigation, and it is priced in duplicate requests.** "You can fire another request if your primary request actually consumed let's say P90 of your latency budget. This can really hedge the P99 tail." The trigger is a fraction of the budget you have already defined per route — which is another reason the per-route budget has to exist first. (09:24-09:43)
- **Caveats.** The 2-to-60-second range and the P99 spike are a symptom report with no root cause identified, and "number one root cause of your silent outage" is a ranking asserted from memory without a sample, period, or organization. "Fix the reasoning level per route" is the entire method offered for reasoning-latency variance, with no guidance on choosing the level, and hedging is proposed with no measurement of the extra spend it creates.
- **Inter-token latency is the percentile an agentic route needs, and it is not TTFT.** Red Hat separates the two by which lever moves them: KV-cache-aware routing "helps you solve the TTFT problem," but "for agentic workload it's not just a TTFT… it's about your inter-token latency," which is what prefill/decode disaggregation defends — measured at P99 ITL of ~900 ms aggregated versus ~100 ms disaggregated, with the aggregated curve also visibly noisier. The reason a P99 on the wrong metric hides the problem is mechanical: a long prefill arriving on a shared pod "will completely stall the ongoing decode token generation process causing… jitter in user streaming latency," which a first-token percentile never sees. ([Kamra](../sources/20260827_YXowceUKYJI.md), 08:53-09:19, 11:25-11:56, 12:59-13:52)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [An LLM Gateway Cannot Maximize Availability, Latency, Guardrails, and Cost at Once](an-llm-gateway-cannot-maximize-availability-latency-guardrails-and-cost.md)
- [Prefer Per-Request Fallback to Retries and Circuit Breakers for LLM Calls](prefer-per-request-fallback-to-retries-and-circuit-breakers-for-llm-calls.md)
- [KV-cache hit rate is a production agent SLO](kv-cache-hit-rate-is-a-production-agent-slo.md)
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Hit Soft-Realtime Latency With a Fast Model, Eager Inference, and Prefix Caching](hit-realtime-latency-with-fast-models-eager-inference-and-prefix-caching.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Decentralize the Gateway, Centralize the Governance](decentralize-the-gateway-centralize-the-governance.md)
- [Match the Inference Lever to the Latency Metric It Moves](match-the-inference-lever-to-the-latency-metric-it-moves.md)

Sources:
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 06:30-09:43
- [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../sources/20260827_YXowceUKYJI.md), 08:53-09:19, 11:25-13:52
