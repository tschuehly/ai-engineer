# Match the Inference Lever to the Latency Metric It Moves

Summary: Distributed-inference optimizations are not interchangeable speedups. KV-cache-aware routing buys time-to-first-token (and throughput) by avoiding repeated prefill; prefill/decode disaggregation buys inter-token latency by stopping one request's prefill from stalling another's token stream. Agentic workloads usually need both, and picking the wrong one leaves the metric your users feel untouched.

Use when:
- A serving deployment already improved TTFT but users still report stuttering or jittery streaming.
- Deciding the order in which to adopt routing, tiering, and disaggregation.
- Writing serving SLOs and needing to say which lever defends which number.

Details:
- The mapping is stated directly: prefix and KV-cache routing "helps you solve the TTFT problem and of course you'll improve your throughput, but oftentimes for agentic workload it's not just a TTFT… it's about your inter-token latency. How do we solve that? So prefill-decode disaggregation." ([Fama](../sources/20260827_YXowceUKYJI.md), 08:53-09:19)
- Routing moves TTFT because the win is not doing prefill at all: a cached second turn on the same pod returns in about 1 second where the cold first turn took about 3, and the pod address is identical because the router scored that pod on prefix-cache availability. (07:44-08:53)
- Disaggregation moves inter-token latency because of what colocating the phases does: prefill is compute-bound and bursty while decode is memory-bandwidth-bound and latency-sensitive, so "if there's a sudden influx of a long prefill prompt, it will completely stall the ongoing decode token generation process causing massive problems and jitter in user streaming latency." The fix is structural — the interfering work is on a different pod — not a tuning parameter. ([Kamra](../sources/20260827_YXowceUKYJI.md), 10:20-11:56)
- The two levers are separable in measurement, which is the useful part of the evidence. A concurrency sweep shows three lines on the same hardware: aggregated serving under default Kubernetes scheduling, the same aggregated serving *plus* llm-d KV-cache-aware routing ("you can almost see the gains just based on the routing"), and disaggregated serving above both. Adopting routing does not require adopting disaggregation. (13:52-14:37)
- The inverse holds too, and it is the reason to not reach for disaggregation first: if the requirement is strict TTFT rather than smooth streaming, stay aggregated, "because you can actually tune them on aggregate serving." Disaggregation adds a network hop for the KV transfer, which is the wrong direction for first-token latency. (16:45-17:04)
- Ordering that follows: measure which metric is actually violated, take the routing lever first (it is cheaper, needs no special fabric, and helps the >90%-cache-hit agentic case most), and reach for disaggregation only when inter-token latency is the violated number.

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Route inference requests by KV locality and worker load](route-inference-requests-by-kv-locality-and-worker-load.md)
- [Disaggregate prefill and decode workers by workload shape](disaggregate-prefill-and-decode-workers-by-workload-shape.md)
- [Disaggregation Needs a Fabric, and Pays Off in the Middle Concurrency Band](disaggregation-needs-a-fabric-and-pays-off-in-the-middle-band.md)
- [Track Latency and Timeouts Per Model Class Per Route](track-latency-and-timeouts-per-model-class-per-route.md)
- [Tune inference to the application Pareto point](tune-inference-to-the-application-pareto-point.md)

Sources:
- [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../sources/20260827_YXowceUKYJI.md), 07:44-09:19, 10:20-11:56, 13:52-14:37, 16:45-17:04
