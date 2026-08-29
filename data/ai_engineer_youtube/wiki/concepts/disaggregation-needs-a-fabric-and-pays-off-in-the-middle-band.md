# Disaggregation Needs a Fabric, and Pays Off in the Middle Concurrency Band

Summary: Prefill/decode disaggregation has one hard prerequisite and one non-obvious payoff shape. The prerequisite is an RDMA or RoCE class fabric, because the decode worker pulls the KV cache across the network; without it, stay aggregated. The payoff, in the configuration measured, is concentrated in the middle of the concurrency curve and roughly ties aggregated serving at both ends.

Use when:
- Deciding whether to adopt disaggregated serving, or explaining to a platform team why you cannot.
- Interpreting a disaggregation benchmark that shows no win, and checking whether it was run at the wrong concurrency.
- Writing hardware requirements for an inference cluster before the model is chosen.

Details:
- The prerequisite is stated as a possession, not a preference: disaggregation "requires transfer of KV caches from your prefill workers to your decode workers, so you must possess an advanced high-speed network fabric like RDMA or RoCE." Absence of that fabric is called "the biggest point" in the stay-aggregated column. ([Kamra](../sources/20260827_YXowceUKYJI.md), 16:22-17:04)
- The mechanism that makes the fabric load-bearing: the prefill worker "processes the prompt, constructs the initial KV cache of the prompt and outputs the standard KV transfer metadata," and "the target decode worker actually pulls the computed KV caches across the network fabric utilizing the KV transfer metadata." Every request pays a cache-sized network transfer that aggregated serving does not. (11:56-12:55)
- Use disaggregation for: long context with high input-to-output sequence-length ratios; large models where rich model-parallelism techniques apply; the middle concurrency regime; and "strict ITL streaming requirements." Stay aggregated for: short-to-moderate context, any model size, low concurrency, strict TTFT requirements — and no fabric. (15:39-17:04)
- The payoff shape is the surprise. On 16 H100s (aggregated 4 replicas at TP4 versus 2 prefill + 2 decode at TP4), the PD curve "is very similar to the aggregated config at the lower concurrency regimes and very similar at the higher concurrency regimes, but it's actually the middle part of the concurrency regime that PD actually shines." A benchmark run at idle or at saturation will show the technique doing nothing. (13:52-15:07)
- At a single operating point in that band the difference is large: P99 inter-token latency falls from "roughly around 900 milliseconds" with visible fluctuation to "almost nine times better at 100 milliseconds," and the curve is "much smoother" — on a multi-turn workload with a 10,000-token prefix and 128 tokens per turn. Smoothness is a separate deliverable from the median; streaming jitter is what phase interference produces. (12:59-13:52)
- The middle-band rule does not survive a change of configuration, and the talk does not reconcile this. On 64 H100s (aggregated 8 replicas at TP8 versus 3 prefill + 5 decode at TP8) with a prefill-heavy 5,000-token input and 500-token output, the PD Pareto curve "dominates… across the entire interactivity spectrum." Two variables moved at once — the prefill:decode ratio and the workload shape — so read the middle-band claim as one configuration's shape rather than a property of disaggregation. (15:07-15:35)
- The honest framing offered with the matrix: "I don't want to leave you guys that PD is the answer to everything and it's a magic bullet… it's essentially a phase separation trade-off." (15:39-15:53)
- All figures are the vendor's internal results for its own project, reported without error bars, run counts, or axis values on the concurrency sweep.

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Disaggregate prefill and decode workers by workload shape](disaggregate-prefill-and-decode-workers-by-workload-shape.md)
- [Match the Inference Lever to the Latency Metric It Moves](match-the-inference-lever-to-the-latency-metric-it-moves.md)
- [Set the Prefill-to-Decode Ratio From the Workload's Input-to-Output Ratio](set-the-prefill-to-decode-ratio-from-the-workloads-input-output-ratio.md)
- [Autoscale specialized inference workers as traffic mix changes](autoscale-specialized-inference-workers-as-traffic-mix-changes.md)
- [GPU Utilization Is a Lie: Instrument Tensor Cores and the Fabric](measure-tensor-core-utilization-not-gpu-utilization.md)

Sources:
- [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../sources/20260827_YXowceUKYJI.md), 11:56-15:35, 15:39-17:04
