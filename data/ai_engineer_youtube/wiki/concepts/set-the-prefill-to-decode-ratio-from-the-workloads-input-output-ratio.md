# Set the Prefill-to-Decode Ratio From the Workload's Input-to-Output Ratio

Summary: Once prefill and decode run in separate pools, the pool ratio becomes a tuning parameter with an obvious source: the workload's measured input-to-output sequence-length ratio tells you which phase is the constraint. Derive the starting ratio from it, size each pool for its own objective (prefill for throughput, decode for latency), and let an autoscaler re-derive the ratio as traffic shifts rather than freezing it at deploy time.

Use when:
- Choosing an initial prefill:decode worker split for a disaggregated deployment.
- A disaggregated deployment underperforms and you suspect the split, not the technique.
- Planning capacity for agentic traffic, where input-to-output ratios routinely exceed 100:1.

Details:
- The diagnosis comes before the ratio: on an agentic dataset with a 45:1 input-to-output ratio, "prefill is really the constraint." A high ISL:OSL ratio means most of the compute is prompt processing, so decode-side capacity is not the thing to buy. ([Fama](../sources/20260827_YXowceUKYJI.md), 19:52-20:20)
- The two pools are tuned for different objectives, which is the reason to separate their sizing at all: a prefill pool of "up to three workers optimized for high throughput" against "one dedicated worker" for decode "optimized for low latency." (18:30-19:10)
- The architectural payoff is that the ratio becomes cheap to change: "you can actually scale the throughput by simply adding prefill workers without reconfiguring the decode." A prefill-bound workload is then a scaling action, not a redesign. (19:10-19:28)
- The reported result on that setup — GLM 5.2 served on H200s rather than the B200s its published numbers use — is "4x faster TTFT and also 60% more requests," with the work stated to be in progress and the next step being more prefill replicas. Note the internal inconsistency: the architecture is described as up to three prefill workers to one decode, while the quoted result is "with 2P… 1D." (18:01-18:30, 19:52-20:20)
- Supporting configuration, for shape rather than as a recipe: NIXL carries the KV transfer between pools, and each worker is a LeaderWorkerSet group at TP1 with DP8 and EP8 — expert parallelism because the model is a mixture of experts, with data parallelism doing the work tensor parallelism usually does. (18:45-19:28)
- The static ratio is explicitly a starting point, not an answer: the design space needs "dynamic PD rate matching… because you can start with a static PD ratio but it needs to evolve with the autoscaler as the traffic changes," alongside independent autoscaling of each pool and continual TP/DP tuning against SLOs. A ratio derived from last quarter's ISL:OSL is wrong as soon as the application changes its prompt shape. (17:35-17:55)
- Adjacent unexplained finding from the same deployment, offered as days-old and still being explored: BF16 KV cache "actually is faster than using FP8 KV cache for longer prefill." No workload definition or measurement accompanies it, so treat it as a reason to benchmark KV-cache precision on a prefill-heavy workload rather than assume the quantized path is faster. (19:28-19:52)

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Autoscale specialized inference workers as traffic mix changes](autoscale-specialized-inference-workers-as-traffic-mix-changes.md)
- [Disaggregation Needs a Fabric, and Pays Off in the Middle Concurrency Band](disaggregation-needs-a-fabric-and-pays-off-in-the-middle-band.md)
- [Disaggregate prefill and decode workers by workload shape](disaggregate-prefill-and-decode-workers-by-workload-shape.md)
- [Replay Agentic Traces, Because Steady-State Benchmarks Hide the Workload](replay-agentic-traces-because-steady-state-benchmarks-hide-the-workload.md)
- [Treat Quantization as a Memory-Bandwidth Lever](treat-quantization-as-a-memory-bandwidth-lever.md)

Sources:
- [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../sources/20260827_YXowceUKYJI.md), 17:35-17:55, 18:01-20:20
