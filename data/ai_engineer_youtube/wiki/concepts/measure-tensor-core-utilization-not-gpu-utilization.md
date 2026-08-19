# GPU Utilization Is a Lie: Instrument Tensor Cores and the Fabric

Summary: For large-scale training, the two metrics most teams already have — GPU utilization and node health — are the two that hide the problem. GPU utilization measures how much of the time a GPU is doing *some* work, not how much useful arithmetic it is doing, so it can read 100% through an entire pre-training run that is nowhere near well used; tensor core utilization is the honest proxy. And because most failures at scale happen in cross-node communication, the metrics that matter most are InfiniBand counters, which no vendor exporter provides by default and which you have to collect yourself.

Use when:
- Standing up observability for a multi-node training run and deciding which metrics are load-bearing.
- A cluster's dashboards look healthy while runs crash, stall, or lose throughput.
- Judging whether a change to batch size, resolution, or parallelism actually improved hardware efficiency.
- Deciding whether DCGM plus node exporters is a sufficient starting point (it is not).

Details:
- The framing claim, from Krea's infra lead running Krea 2 pre-training on thousands of GPUs: "metrics are everything. That's how I can support my researchers. That's how I have visibility in the system… invest heavily on metrics. Don't go blind because you're going to go crazy." He describes the specific metrics as "quite silly but like extremely effective" — the value is in collecting them at all, not in their sophistication. ([Menezes](../sources/20260818_byn9PURoBNY.md), 04:22-04:46)
- GPU utilization is rejected outright: "there is GPU utilization which is a lie. Don't trust this. This is dumb… this is amount of time GPU's doing work but like not good work. Not how efficient the GPU's working." During their pre-training the metric read 100% and "this is not true. We are not fully utilizing the GPU." (05:26-05:45)
- Tensor core utilization is the replacement because it reports "how much of a tensor core you're using and like how effective they are being." The validating observation is a natural experiment already present in a diffusion training schedule: as the resolution curriculum stepped 128 → 256 → 512 → 1024 pixels through pre-training, mid-training, and post-training, tensor core utilization climbed with it, "cuz now you're doing more work on images" — a metric that moves with real arithmetic intensity while the utilization number stays pinned at 100%. (05:46-06:18)
- The fabric is where the failures actually were: "most of our failures were like related to like cross-node communication," and the silent class is the expensive one — NCCL timeouts and crashes where "the metrics are all good." (03:25-03:34, 06:38-06:47)
- Nothing ships those counters. "InfiniBand and NVLink metrics… by default [are] not exported by… the NVIDIA metrics, that DCGM stuff. Some NVLink stuff, yes, but no InfiniBand." His stated bar: "if you're doing large-scale pre-training with a bunch of GPUs talking to each other between machines and you have no InfiniBand metrics, you're doing something wrong." Building the collection is not the hard part — "We had to build custom stuff to get this. It was not hard. You can figure it out." (06:18-07:12)
- The dashboard contents are worth copying: beyond throughput, they track how long a message waits after being sent on the fabric, error counts broken out by error type, and packet counts. Wait time and typed error counts are what turn a green throughput graph into a diagnosis. (06:47-07:08)
- NVLink is the intra-node counterpart and NVIDIA does not export its error counters either. Its diagnostic value is specific: "sometimes a single node would have a weird failure where the GPUs seem to be fine, but like some weird error happens and then you can look at NVLink errors and like you see errors happening. And then replace that machine." He rates InfiniBand "extremely important" and NVLink "a little bit less." (07:12-07:45)
- Temperature belongs in the same set and is the cheapest of all: one GPU running warmer than its neighbors "is going to start throttling and slow down and… the training's going to be unstable and you have weird problems" — a single card degrading a synchronous collective run. Their rule is to pull anything above 78 °C rather than investigate it. (04:46-05:17)
- Overall verdict on the metric set: "without this we would not be able to to train at all." (07:45-07:52)
- Caveat on transfer: these are single-cluster observations from an image-diffusion pre-training workload on an all-InfiniBand fabric, and the speaker allows that the crash rate itself may be "maybe skill issue on our part, maybe our cluster." The metric argument is about instrumentation defaults, not about a universal failure profile.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)

Related concepts:
- [Let Training Crash and Checkpoint Against a Fast Filesystem](let-training-crash-and-checkpoint-against-a-fast-filesystem.md)
- [Give Training Priority Over Production on a Shared GPU Cluster](give-training-priority-over-production-on-a-shared-gpu-cluster.md)
- [Simulate RL run layouts before spending GPU budget](simulate-rl-run-layouts-before-spending-gpu-budget.md)
- [Pipeline RL trades policy staleness for GPU throughput](pipeline-rl-trades-policy-staleness-for-gpu-throughput.md)
- [Layer AI application metrics from guardrail compliance to system health](layer-ai-application-metrics-from-guardrail-compliance-to-system-health.md)
- [Run the LLM Post-Training Ladder on Diffusion Models](run-the-llm-post-training-ladder-on-diffusion-models.md)

Sources:
- [Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai](../sources/20260818_byn9PURoBNY.md), 03:25-07:52
