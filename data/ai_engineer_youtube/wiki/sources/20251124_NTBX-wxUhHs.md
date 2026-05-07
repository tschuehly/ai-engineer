# Context Platform Engineering to Reduce Token Anxiety - Val Bercovici, WEKA

Source: [Context Platform Engineering to Reduce Token Anxiety - Val Bercovici, WEKA](https://www.youtube.com/watch?v=NTBX-wxUhHs)
Uploaded: 2025-11-24
Transcript: `raw/20251124_NTBX-wxUhHs/NTBX-wxUhHs.en-orig.vtt`

## Summary

Val Bercovici and Callan Fox frame production agent context as an inference-platform storage problem: agent and subagent loops repeatedly send large shared prompt, tool-call, and tool-response regions, so KV-cache hit rate, cache time-to-live, working-set sizing, and memory-tier throughput determine cost, rate limits, latency, and usable concurrency.

## Extracted Concepts

- [KV-cache hit rate is a production agent SLO](../concepts/kv-cache-hit-rate-is-a-production-agent-slo.md) - this source treats cache hits as the core metric linking context reuse to user-visible throughput and provider economics.
- [Agent swarms create reusable KV-cache working sets](../concepts/agent-swarms-create-reusable-kv-cache-working-sets.md) - this source shows that orchestrators, subagents, tool calls, and tool responses create repeated token regions that can be cached across fast agent loops and slower human pauses.
- [Size KV-cache memory tiers with workload-shaped benchmarks](../concepts/size-kv-cache-memory-tiers-with-workload-shaped-benchmarks.md) - this source describes load generation, SLOs, cache TTL, prefill/decode modes, and memory-tier comparisons for context-platform sizing.

## Topic Links

- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

## Notes

- The talk introduces WEKA's open-source context platform engineering toolkit as a load generator for configurable agent swarms and subtasks, with deterministic or random prompt cycles, model parallelism options, aggregated or disaggregated prefill/decode options, and memory-tier configuration (00:20-01:04).
- The speakers cite Manus's context engineering claim that KV-cache hit rate is the most important metric for production-grade AI agents, because higher hit rates reduce token anxiety and make agent workloads less dependent on prompt-cache price arbitrage (01:22-03:45).
- Agentic coding prompts contain relatively little direct user text; most token volume can come from system prompts, tool calls, and tool responses, making repeated regions visible in cache analysis (07:04-07:48).
- Human feedback loops can be minutes or hours, while agent and subagent requests can arrive every 10-15 seconds, so cache time-to-live must account for both fast tool loops and slow human pauses (07:48-08:17).
- Cache TTL changes working-set behavior: a one-minute TTL can thrash when request gaps exceed a minute, while five-minute or one-hour TTLs can improve hit rates at the cost of holding more tokens in cache (11:07-12:49).
- KV-cache hit rate has direct cost and capacity effects: missed hits can re-prefill the same tokens many times, increase input token costs or rate-limit pressure, and waste GPU cluster capacity for agentic workflows (10:07-10:43, 13:02-15:52).
- Memory-tier design needs capacity plus fast write/read paths; tiers that can store many tokens but cannot fetch them into the GPU quickly enough do not help the active inference path (16:05-18:40, 22:40-22:58).
- The benchmark workflow can ramp coding-agent user pools, compare HBM, DRAM, and storage-backed tiers, and track whether the system maintains output tokens and concurrency under prefill- or decode-focused loads (18:46-22:58).
