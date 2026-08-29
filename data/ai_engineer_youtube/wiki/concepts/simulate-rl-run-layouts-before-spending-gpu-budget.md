# Simulate RL Run Layouts Before Spending GPU Budget

Summary: Expensive RL runs should be modeled before launch by estimating sampling throughput, training throughput, response-length distribution, KV-cache limits, GPU allocation, and maximum staleness. The goal is to find a layout whose sample production and training consumption rates match under the algorithm's staleness tolerance.

Use when:
- Planning how many GPUs to allocate to sampling versus training in an async RL run.
- Setting performance targets before optimizing inference or training kernels.

Details:
- Applied Compute models the end-to-end RL system from GPU budget, training batch size, sampling forward-pass latency, response-length distribution, and per-GPU training throughput. (09:00-12:53)
- Sampling throughput is estimated from forward-pass latency as a function of batch size, with KV-cache memory limits constraining how large the steady-state generation batch can be. (10:16-12:28)
- Synchronous simulations need both the generation batch size and response-length distribution because the longest request controls the number of forward passes before an optimization step can run. (13:20-14:56)
- Async simulations should balance sample production and training consumption rates; too many training GPUs drain the queue and sit idle, while too many sampling GPUs create samples faster than trainers can consume and raise staleness. (15:01-17:17)
- Candidate layouts are pruned when simulated staleness exceeds what the ML method can tolerate, then swept to choose high-throughput allocation before paying for real GPU runs. (17:17-19:31)
- The source reports a roughly 60% simulated speedup over the synchronous baseline when compute is optimally allocated between training and sampling under their assumptions. (18:58-19:12)

- **The simulator assumes one budget of homogeneous, co-located GPUs to allocate between training and sampling; a cross-datacenter design breaks that assumption in a useful direction.** If rollout engines can autoscale globally at other providers, sampling capacity stops being drawn from the same fixed pool as training capacity, and the allocation sweep this page describes becomes a sweep over trainer size against an elastic — and differently priced — sampling tier ([The Rollout Serving Island Is the Movable Unit of an RL Run](the-rollout-serving-island-is-the-movable-unit-of-an-rl-run.md)). Two model inputs change with it: weight-sync latency stops being negligible, and per-GPU sampling cost stops being a single number. Modal reports no simulation of its own, so this is a stated implication rather than a modeled result. ([Modal](../sources/20260810_maRzp4kImJ4.md), 03:37-04:18, 17:26-18:43)
- **Why the layout space is large enough to need a method at all.** Arora enumerates it: "a standard transformer layer can be parallelized across data, sequence, tensor, context, layer, pipeline and expert dimensions, and each composition induces a different communication pattern," so the space "expands combinatorially beyond single GPU cases." Each composition is a different communication pattern, not just a different memory split — which is the part a layout simulator has to model if its prediction is to hold, and the reason these patterns recur "from inference to RL to post-training." ([Arora](../sources/20260827_pOvWgX7IJsc.md), 22:37-23:20)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)

Related concepts:
- [Pipeline RL trades policy staleness for GPU throughput](pipeline-rl-trades-policy-staleness-for-gpu-throughput.md)
- [The Rollout Serving Island Is the Movable Unit of an RL Run](the-rollout-serving-island-is-the-movable-unit-of-an-rl-run.md)
- [Make local inference benchmarks reproducible artifacts](make-local-inference-benchmarks-reproducible-artifacts.md)
- [Use hardware-in-the-loop search for AI kernel generation](use-hardware-in-the-loop-search-for-ai-kernel-generation.md)
- [Overlap Communication With Compute Intra-SM or Inter-SM by Data Alignment](overlap-communication-with-compute-intra-sm-or-inter-sm.md)

Sources:
- [Efficient Reinforcement Learning - Rhythm Garg & Linden Li, Applied Compute](../sources/20251209_o15AaYl7Wu0.md), 09:00-19:57
- [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](../sources/20260810_maRzp4kImJ4.md), 03:37-04:18, 17:26-18:43
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 22:37-23:20
