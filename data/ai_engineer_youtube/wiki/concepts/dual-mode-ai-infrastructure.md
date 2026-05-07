# Dual-Mode AI Infrastructure

Summary: AI infrastructure has to serve at least two different workload modes: long compute-heavy jobs and low-latency realtime interactions. Designing accelerators or fleets for one mode without understanding the ratio can leave expensive capacity idle or mismatched.

Use when:
- Planning accelerator, GPU, or inference fleet capacity for mixed AI products.
- Comparing infrastructure needs for agentic test-time scaling versus realtime AI interfaces.

Details:
- Brockman separates compute-intensive workloads that may run for a long time from realtime workloads that need very low latency. 32:25-32:41
- The naive hardware answer is two accelerator shapes: one compute-optimized and one latency-optimized, with different HBM and compute tradeoffs. 33:43-33:54
- The hard planning problem is predicting ratios; if the balance is wrong, part of the fleet can become useless. 33:57-34:06
- The same discussion frames AGI-scale software work as requiring massive physical infrastructure projects, not only writing model software. 33:15-33:38

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Size KV-cache memory tiers with workload-shaped benchmarks](size-kv-cache-memory-tiers-with-workload-shaped-benchmarks.md)
- [Pipeline RL trades policy staleness for GPU throughput](pipeline-rl-trades-policy-staleness-for-gpu-throughput.md)

Sources:
- [#define AI Engineer - Greg Brockman, OpenAI (ft. Jensen Huang)](../sources/20250810_avWhreBUYF0.md), 32:25-34:06
