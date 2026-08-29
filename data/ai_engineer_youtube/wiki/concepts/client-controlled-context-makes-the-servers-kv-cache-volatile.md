# Client-Controlled Context Makes the Server's KV Cache Volatile

Summary: In agentic serving the client owns the prompt structure, so the server no longer controls its own cache lifecycle. That single shift is what turns KV cache management into a scheduling problem: the server cannot predict which prefixes will be reused, so it has to route for locality, tier storage beneath GPU memory, and pin sessions instead of relying on a steady working set.

Use when:
- Explaining why a serving stack that was fine for chat traffic thrashes its cache under agent traffic.
- Deciding where cache policy belongs — engine, router, or storage tier.
- Justifying investment in cache-aware infrastructure with a cost number rather than a latency graph.

Details:
- The regime statement: "We're no longer chasing this raw throughput in a steady state," because the context is "highly volatile and client-driven… user and client define the prompt structure." ([Fama](../sources/20260827_YXowceUKYJI.md), 05:04-05:32)
- Three consequences follow directly. KV cache management "becomes super volatile because the context is client determined," producing "frequent evictions and rewrites." The engine (vLLM) and the upper scheduling and routing layer now need coordination such as prefix routing, "especially when latency becomes a primary scheduling metric rather than a secondary or afterthought." And the metric set changes: "we need to measure cache throughput separately" from raw throughput. (05:32-06:00)
- The economic case is made in one line rather than with a latency graph, using Anthropic's public API pricing: "there's 10x cost difference between cached and non-cached tokens… 10x difference on your token balance sheet is pretty serious impact on your business." That is the number that makes routing a cheaper lever than adding GPUs. (06:00-06:28)
- Because reuse cannot be predicted, it has to be *preserved*: the cache management layer offloads across hot/warm/cold tiers to NVMe SSD and the XFS filesystem, uses KV-centric stores such as Mooncake, and applies "smarter and session-aware eviction policies such as priority and also session pinning to ensure this really important context persists exactly when and where it's needed." Session pinning is the direct answer to a client-owned lifecycle — the server cannot know when the session resumes, so it holds the state rather than betting on recomputation. (07:12-07:44)
- The demo shows how sharp the client's control is: keeping the system prompt fixed and varying only the user prompt returns to the same pod and the cached path (~1 s), while changing the system prompt lands on a different pod with no cache hit and pays full prefill (~3 s). An application-side prompt edit therefore relocates the request, not just the cache entry. (07:44-08:53)
- The application-side corollary is that anything which rewrites conversation history — reordering context, injecting a timestamp, compacting — is a serving decision made by the client, and the server has no way to object.
- Caveat: the 10x figure is one vendor's published API pricing used to motivate self-hosted work, not a measurement of self-hosted serving economics, and no cost-per-token figure for the self-hosted path appears in the talk.

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [KV-cache hit rate is a production agent SLO](kv-cache-hit-rate-is-a-production-agent-slo.md)
- [Route inference requests by KV locality and worker load](route-inference-requests-by-kv-locality-and-worker-load.md)
- [Size KV-cache memory tiers with workload-shaped benchmarks](size-kv-cache-memory-tiers-with-workload-shaped-benchmarks.md)
- [Exploit structured agent waits for KV-cache manipulation](exploit-structured-agent-waits-for-kv-cache-manipulation.md)
- [Replay Agentic Traces, Because Steady-State Benchmarks Hide the Workload](replay-agentic-traces-because-steady-state-benchmarks-hide-the-workload.md)

Sources:
- [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../sources/20260827_YXowceUKYJI.md), 05:04-08:53
