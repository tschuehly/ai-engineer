# KV-cache hit rate is a production agent SLO

Summary: Production agent platforms should treat KV-cache hit rate as an operational SLO because it connects repeated context reuse to token cost, rate limits, latency, and GPU capacity.

Use when:
- Sizing or operating inference for coding agents, agent swarms, or long-context tool loops.
- Translating agent user SLAs into platform-level cache, latency, and throughput objectives.

Details:
- The WEKA talk frames subscription tiers and token-cache rights as practical allocations of KV-cache slots in token storage, not only abstract API pricing (04:24-05:26).
- Missed cache hits force repeated prefill of the same tokens, which can cost more on usage-based APIs and consume rate-limited subscription capacity even when the user pays a flat fee (09:35-10:43).
- For agentic workflows, cache-hit bands matter to providers because low hit rates can waste GPU cluster capacity on repeated context processing rather than useful output generation (14:25-15:52).
- KV-aware routing should balance prefix match against existing worker load; cache locality alone can route too much work to the same machine and create queueing (11:03-13:01).
- The application-side version of the same SLO, with a number: Towards AI's AI tutor logs cached-token count per turn alongside cost and time-to-first-token, and their winning configuration ran at 97% cached tokens — which made the setup sending the *most* tokens the cheapest to run. Hit rate is therefore not only a platform capacity metric but the variable that decides whether an application-level context change saves money or costs it, since any rewrite of the history drops the rate toward zero. ([Context Engineering in 2026](../sources/20260817_WP3hjUXd918.md), 35:19-35:50, 52:10-53:07)

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Agent swarms create reusable KV-cache working sets](agent-swarms-create-reusable-kv-cache-working-sets.md)
- [Size KV-cache memory tiers with workload-shaped benchmarks](size-kv-cache-memory-tiers-with-workload-shaped-benchmarks.md)
- [Prompt Caching Sets the Break-Even Bar for Compaction](prompt-caching-sets-the-break-even-bar-for-compaction.md)

Sources:
- [Context Platform Engineering to Reduce Token Anxiety - Val Bercovici, WEKA](../sources/20251124_NTBX-wxUhHs.md), 01:22-03:45, 09:35-10:43, 14:25-15:52
- [Hacking the Inference Pareto Frontier - Kyle Kranen, NVIDIA](../sources/20250801_Y2qc0UhDSnc.md), 11:03-13:01
- [Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](../sources/20260817_WP3hjUXd918.md), 35:19-35:50, 52:10-53:07
