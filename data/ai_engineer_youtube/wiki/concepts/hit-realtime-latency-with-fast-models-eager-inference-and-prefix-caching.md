# Hit Soft-Realtime Latency With a Fast Model, Eager Inference, and Prefix Caching

Summary: To keep a voice-driven experience responsive within a ~1 s envelope, combine three techniques: a latency-prioritized fast model (with heavier work handed off asynchronously to a larger thinking model), eager short-interval inference that fires as the user talks instead of waiting for end-of-speech silence, and a stable prefix-caching regimen that keeps most of the context identical across requests.

Use when:
- Building a soft-realtime voice-in/visuals-out agent that must respond within ~1 s.
- Diagnosing why a small, cheap model still misses realtime latency targets.
- Reducing per-turn cost and latency for a long-running or frequently-running agent.

Details:
- Fast model on a latency-prioritized *platform*, not just a small model: GPT-5 mini was cheaper but showed 5,000 ms latencies, 7,000 ms P95, sometimes 10,000 ms — too slow to ever respond in time; Haiku is much better on P95, so pick a Haiku-class (or small open-source) model and feed it short context so it can respond in a few hundred milliseconds. 08:55-10:25
- Async handoff for heavy work: when a larger chunk of work is needed, the fast real-time model sends an asynchronous message to a larger model that can think, then the soft-realtime model re-interleaves that result into its ongoing responses — keeping the interactive loop fast while still doing deep work. 09:57-10:14
- Eager short-interval inference: traditional voice apps wait for ~1 s of silence to confirm the user stopped, blowing the latency budget; instead fire inference every 1-2 s as the person talks, even when unsure they've finished, so output keeps pace with a multi-clause spoken request ("change this, and also list that"). 10:30-11:35
- Stable prefix-caching regimen: lean into platform prefix caching (up to ~90% cheaper/faster) by keeping the first ~90% of the context window identical from request to request and varying only the final ~10%, and minimize output tokens for fast, affordable turns. The same principle applies whether the agent is long-running or frequently-running. 11:35-12:40
- **Hedging is the lever for the tail these techniques do not reach.** Once the per-route budget exists, "you can fire another request if your primary request actually consumed let's say P90 of your latency budget. This can really hedge the P99 tail." It buys tail latency with duplicate spend rather than with model choice or caching, which makes it complementary to everything on this page — and it presupposes a budget defined per model per route, since a gateway-wide number would fire the hedge at the wrong moment for every route. ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 07:15-07:40, 09:24-09:43)
- **What the stable-prefix regimen buys on a self-hosted cluster: the pod, not just the cache entry.** With KV-cache-aware routing, holding the system prompt fixed keeps requests landing on the pod that already holds the prefix — measured in a four-turn demo at ~1 second on the cached pod against ~3 seconds cold, with "exactly the same" pod address on the cached turns. Change the system prompt and the request is routed to a *different* pod and pays full prefill again. So the discipline this page recommends for a hosted prefix-caching discount has a stronger form on your own fleet: the varying tail of the prompt costs a cache miss, but varying the head costs a relocation. ([Fama](../sources/20260827_YXowceUKYJI.md), 07:44-08:53)

Related topics:
- [Inference](../topics/inference.md)
- [Voice Agents](../topics/voice-agents.md)

Related concepts:
- [Relax the latency budget by choosing voice-in, visuals-out over voice-out](relax-the-latency-budget-with-voice-in-visuals-out.md)
- [Size the Voice-Agent LLM to the Time-to-First-Token Budget](size-the-voice-agent-llm-to-the-time-to-first-token-budget.md)
- [KV cache hit rate is a production agent SLO](kv-cache-hit-rate-is-a-production-agent-slo.md)
- [Track Latency and Timeouts Per Model Class Per Route](track-latency-and-timeouts-per-model-class-per-route.md)
- [Client-Controlled Context Makes the Server's KV Cache Volatile](client-controlled-context-makes-the-servers-kv-cache-volatile.md)

Sources:
- [Voice In, Visuals Out: The Agony and the Ecstasy - Allen Pike, Forestwalk Labs](../sources/20260628_65X0pQ6Lmbg.md), 08:55-12:40
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 07:15-07:40, 09:24-09:43
- [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../sources/20260827_YXowceUKYJI.md), 07:44-08:53
