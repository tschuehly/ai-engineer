# Replay Agentic Traces, Because Steady-State Benchmarks Hide the Workload

Summary: Public inference benchmarks report steady-state numbers from one sanitized run, which is the opposite of what an agentic workload does. Plan capacity from replayed traces of real agent sessions instead, and read them as distributions — turn counts spanning three orders of magnitude, cache hit rates above 90%, and input-to-output ratios past 100:1 are the normal case, not the tail.

Use when:
- Sizing GPUs, KV-cache tiers, or routing policy for a coding-agent or tool-loop workload.
- Deciding whether a published tokens-per-second or throughput figure predicts anything about your traffic.
- Explaining why a deployment that benchmarked well degrades once real agent sessions arrive.

Details:
- The critique is precise about what is missing, not just that benchmarks are optimistic: public results are "very steady state isolated highly sanitized numbers," and what they omit is "the chaotic reality of multi-turn interactions, massive context fluctuations which are very typical of agentic workloads." ([Kamra](../sources/20260827_YXowceUKYJI.md), 00:43-01:10)
- The replacement evidence comes from SWE-bench-style agentic workloads and traces of real Claude Code sessions, which "fundamentally break many assumptions we made with classic LLM serving." Three facts carry most of the weight: turn counts run "from a few turns all the way to 3,000 turns"; cache hit rate is "oftentimes well exceeding 90%" because agents reuse the system prompt and tool definitions across every turn; and the input-to-output token ratio is "oftentimes over a 100 ratio and even higher." ([Fama](../sources/20260827_YXowceUKYJI.md), 03:16-04:12)
- The statistical instruction is explicit and is the part most easily skipped: "we can't just simply take the average and oftentimes we need to look at the distributions and the P90 numbers especially when you do capacity planning." A workload whose turn count spans 1 to 3,000 has a mean that describes no session. (04:12-04:34)
- The tooling exists rather than being left as an exercise: Red Hat contributed a trace-replay tool to `inference-perf` with Google and IBM specifically so the community can study these patterns against its own traces. (04:34-04:58)
- Note what a 100:1 input-to-output ratio implies before any optimization is chosen — the workload is prefill-bound, so decode-side throughput tuning is aimed at the smaller half of the problem, and the >90% cache hit rate means most of that prefill is *repeated* work that a serving system can decline to redo.
- Scope caveat: the profile is given as ranges and "oftentimes," with no distribution, sample size, or split between the benchmark-derived and the production-derived traces, and no P90 figure is shown despite the advice to plan on P90. It is a strong argument for measuring your own traces, not a table to plan against directly.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Inference](../topics/inference.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Benchmark inference with use-case-shaped token loads](benchmark-inference-with-use-case-shaped-token-loads.md)
- [Client-Controlled Context Makes the Server's KV Cache Volatile](client-controlled-context-makes-the-servers-kv-cache-volatile.md)
- [Agent swarms create reusable KV-cache working sets](agent-swarms-create-reusable-kv-cache-working-sets.md)
- [KV-cache hit rate is a production agent SLO](kv-cache-hit-rate-is-a-production-agent-slo.md)
- [Set the Prefill-to-Decode Ratio From the Workload's Input-to-Output Ratio](set-the-prefill-to-decode-ratio-from-the-workloads-input-output-ratio.md)

Sources:
- [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../sources/20260827_YXowceUKYJI.md), 00:43-01:10, 03:16-04:58
