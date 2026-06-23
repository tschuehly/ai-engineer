# Stack Memory Optimizations to Train Long-Context Transformers

Summary: Fitting a multi-million-token training run onto a fixed GPU node is an incremental memory-engineering problem: no single trick is enough, so you layer fully sharded data parallelism, context parallelism, activation checkpointing, CPU offloading, and chunked sequence training, each removing one memory bottleneck the previous layer exposed.

Use when:
- Planning a long-context training or fine-tuning run that out-of-memories on the hardware you have.
- Deciding which memory optimization to add next instead of buying more GPUs.
- Reasoning about why context-length growth blows up training memory and where that memory actually goes.

Details:
- Two bottlenecks of extending a standard transformer LM's context: quadratic computation (every token interacts pairwise with every other, concentrated in the query/key/value attention step) and linear memory growth as the sequence lengthens — the second is "more insidious" and hard to handle without specific techniques. (03:56-04:46, Q&A 13:56-15:30)
- The motivating failure is sharp: a standard LLaMA 3B at a 3M-token context on a single 8×H100 node runs out of memory just placing the model parameters, before any activations exist. (05:12-05:43)
- Layer 1 — fully sharded data parallelism (FSDP): shard parameters across the 8 GPUs. Model memory drops significantly but the run still OOMs on attention activations. (05:43-06:08)
- Layer 2 — context parallelism via DeepSpeed Ulysses (Microsoft): rather than computing all multi-head attention on every GPU for the whole sequence, assign different heads to different GPUs and communicate activations as needed, so one GPU owns one head but still attends over the full sequence; this preserves the best attention kernel (Flash Attention 1/2/3/4). Utilization drops ~8×, but it still does not fit one node. (06:10-07:48)
- Layer 3 — activation checkpointing: recompute activations during the backward pass instead of storing them; available in essentially every deep-learning framework, just enable it without imposing too much recompute. Cuts activation memory another ~8×. (07:48-08:26)
- Layer 4 — CPU offloading of transformer-block inputs: keep some block inputs on CPU while idle and prefetch them when backpropagating to that layer, so the overlap hides the transfer; first implemented (to the speaker's knowledge) by Unsloth, reaching ~37 GB offloaded with low performance impact. (08:30-09:26)
- Layer 5 — chunked sequence training (Arctic Long Sequence Training): tile element-wise computations — the loss and the MLPs — across the sequence so you never materialize a buffer that is millions of tokens wide along one dimension. With this layer added, 3M tokens finally fits. (09:31-10:00)
- Operating mindset: bottlenecks appear where you least expect, so profile where memory goes (e.g. the PyTorch profiler) before optimizing; understanding memory is useful even below millions of tokens because saved memory can be reinvested to speed up training. (03:22-03:42, 13:00-13:43)

Related topics:
- [Models](../topics/models.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Untied Ulysses Reuses Attention Buffers Across Head Chunks](untied-ulysses-reuses-attention-buffers-across-head-chunks.md)
- [Local LLM training exposes the core model-building stack](local-llm-training-exposes-the-core-model-building-stack.md)
- [Interleave local and global attention to trade context for efficiency](interleave-local-and-global-attention-to-trade-context-for-efficiency.md)
- [Treat quantization as a memory-bandwidth lever](treat-quantization-as-a-memory-bandwidth-lever.md)

Sources:
- [Road to 5 Million Tokens: Breaking Barriers in Long Context Training — Max Ryabinin, Together AI](../sources/20260608_TUnPNY4E2fw.md), 03:56-10:00
