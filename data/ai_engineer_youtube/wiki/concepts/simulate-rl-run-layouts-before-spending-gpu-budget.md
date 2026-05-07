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

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)

Related concepts:
- [Pipeline RL trades policy staleness for GPU throughput](pipeline-rl-trades-policy-staleness-for-gpu-throughput.md)
- [Make local inference benchmarks reproducible artifacts](make-local-inference-benchmarks-reproducible-artifacts.md)
- [Use hardware-in-the-loop search for AI kernel generation](use-hardware-in-the-loop-search-for-ai-kernel-generation.md)

Sources:
- [Efficient Reinforcement Learning - Rhythm Garg & Linden Li, Applied Compute](../sources/20251209_o15AaYl7Wu0.md), 09:00-19:57
