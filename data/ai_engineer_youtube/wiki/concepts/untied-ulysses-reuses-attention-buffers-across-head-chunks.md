# Untied Ulysses Reuses Attention Buffers Across Head Chunks

Summary: Once the known long-context training stack is exhausted, the next memory win is inside context parallelism itself: because one attention head-group already saturates a GPU's compute, you can chunk the heads and iterate over them, reusing one smaller activation buffer across iterations instead of allocating a huge per-head-group buffer — cutting activation memory with negligible throughput impact.

Use when:
- A long-context training run already uses FSDP, context parallelism, checkpointing, offloading, and chunked sequences but still cannot reach the target sequence length.
- Looking for an activation-memory optimization that does not trade away throughput.
- Evaluating context-parallelism implementations beyond stock DeepSpeed Ulysses for very long sequences.

Details:
- Together AI's "Untied Ulysses" is a deeper analysis and expansion of the DeepSpeed Ulysses context-parallelism step, motivated by reaching 5M tokens when the rest of the stack tops out near 3M. (10:04-10:26)
- Key observation: computing even one set of attention heads at a time already saturates the GPU's compute within a single iteration — so scheduling multiple heads on one GPU does not need them computed simultaneously. (10:26-10:42)
- Mechanism: divide the heads assigned to a GPU into chunks and iterate over time — recompute one head group, compute attention over it, store the partial result, then run the next stage which reuses the buffers the previous stage allocated. A smaller buffer reused across two or more iterations replaces one huge buffer per head group, saving activation memory with no significant throughput impact at small scales. (10:42-11:40)
- Results: at both 8B and 32B scale, Untied Ulysses closely matches the most memory-optimized transformer-training implementations while scaling further to 5M tokens (~25% past prior Ulysses per the talk's description) and is sometimes more performant at shorter context lengths. (11:40-12:10)
- Chunk-size tradeoff is straightforward: a larger chunk (more heads per iteration) uses more memory but runs the model a bit faster; a smaller chunk saves memory at a small throughput cost — a tunable knob, not a fixed setting. (12:10-12:29)
- U-Pipe is layered on top: it frees additional memory that can be reinvested elsewhere (for example among pipeline stages), and for 3-5M context lengths it is "the technique that will save you" relative to the other layers. (12:29-13:00)
- Why one trick is never enough: in a vanilla implementation the query/key/value attention step would allocate a single tensor millions of tokens long on one axis, so a range of approaches (not just U-Pipe) is needed to execute the computation without running out of memory. (Q&A 13:56-15:30)

Related topics:
- [Models](../topics/models.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Stack Memory Optimizations to Train Long-Context Transformers](stack-memory-optimizations-to-train-long-context-transformers.md)
- [Interleave local and global attention to trade context for efficiency](interleave-local-and-global-attention-to-trade-context-for-efficiency.md)
- [Preserve long-context ability with single-stage RL](preserve-long-context-ability-with-single-stage-rl.md)

Sources:
- [Road to 5 Million Tokens: Breaking Barriers in Long Context Training — Max Ryabinin, Together AI](../sources/20260608_TUnPNY4E2fw.md), 10:04-15:30
