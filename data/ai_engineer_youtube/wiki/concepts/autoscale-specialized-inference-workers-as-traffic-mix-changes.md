# Autoscale specialized inference workers as traffic mix changes

Summary: Specialized inference deployments need dynamic load balancing because the right mix of aggregated, disaggregated, prefill, decode, tensor-parallel, and context-parallel workers changes with input and output sequence length distributions.

Use when:
- Operating an inference platform with multiple traffic classes or changing user/application mix.
- Deciding whether worker specialization has become an autoscaling problem rather than a static deployment setting.

Details:
- Worker specialization can match different input sequence length and output sequence length regions: short-input/long-output cases may prefer aggregated workers with higher tensor parallelism, middle ranges may prefer disaggregation, and long-context regimes may need disaggregation with context parallelism (17:45-18:25).
- Specialization can improve speed and cost while keeping quality constant because it changes where and how work runs, not the model's math (18:25-18:40).
- Static histograms can become wrong when app or user mix shifts; increases in input sequence length can raise prefill demand relative to decode demand and break the original worker balance (18:43-19:28).
- Real-time autoscaling across prefill and decode instance types is needed to account for changes in platform usage distribution and to make disaggregation reach its potential (19:28-19:58).
- **Independent corroboration, with the failure mode named as a ratio rather than a histogram.** Red Hat reaches the same conclusion from a different stack: the PD design space needs "dynamic PD rate matching… because you can start with a static PD ratio but it needs to evolve with the autoscaler as the traffic changes," plus autoscaling that "scale[s] PD pools independently" and continual tuning of tensor and data parallelism against SLOs. llm-d supplies the mechanism as workload APIs — LeaderWorkerSet and DisaggregatedSet orchestrating multi-node model execution — with autoscalers that "monitor capacity bounds and real-time traffic mixes." The scheduler's full input list is worth copying as a checklist: "SLO targets, QPS, KV cache locality metrics, PD ratios and network topologies." ([Kamra](../sources/20260827_YXowceUKYJI.md), 09:28-10:20, 17:04-17:55)

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Disaggregate prefill and decode workers by workload shape](disaggregate-prefill-and-decode-workers-by-workload-shape.md)
- [Production inference combines model support with cluster operations](production-inference-combines-model-support-with-cluster-operations.md)
- [Match GPU Commitments To Workload Lifecycle](match-gpu-commitments-to-workload-lifecycle.md)
- [Set the Prefill-to-Decode Ratio From the Workload's Input-to-Output Ratio](set-the-prefill-to-decode-ratio-from-the-workloads-input-output-ratio.md)

Sources:
- [Hacking the Inference Pareto Frontier - Kyle Kranen, NVIDIA](../sources/20250801_Y2qc0UhDSnc.md), 17:45-19:58
- [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../sources/20260827_YXowceUKYJI.md), 09:28-10:20, 17:04-17:55
