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

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Disaggregate prefill and decode workers by workload shape](disaggregate-prefill-and-decode-workers-by-workload-shape.md)
- [Production inference combines model support with cluster operations](production-inference-combines-model-support-with-cluster-operations.md)
- [Match GPU Commitments To Workload Lifecycle](match-gpu-commitments-to-workload-lifecycle.md)

Sources:
- [Hacking the Inference Pareto Frontier - Kyle Kranen, NVIDIA](../sources/20250801_Y2qc0UhDSnc.md), 17:45-19:58
