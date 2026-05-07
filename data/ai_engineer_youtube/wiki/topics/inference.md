# Inference

## Overview

Inference is the production discipline of turning trained models into reliable, efficient services. For small models, the main constraint is often not raw compute alone but orchestration across many specialized models: dynamic loading, routing, batching, model-specific runtime support, observability, and autoscaling determine whether the system wastes GPU capacity or becomes a reusable agent and retrieval substrate. At the architecture level, inference cost is also shaped by attention and memory choices: sparse expert activation, local/global attention mixes, grouped query attention, quantization, flash-backed embedding tables, and hardware-specific kernels can change the practical serving envelope before cluster operations even begin. Long-context serving adds the same lesson from another angle: every extra prompt token can increase cost and latency, and large windows do not guarantee stable reasoning over the added material. Agentic long-context serving adds a KV-cache layer to that problem: orchestrators, subagents, tool calls, and tool responses create repeated token regions, so cache hit rate, time-to-live, prefill/decode behavior, and memory-tier throughput can determine cost, rate limits, and useful concurrency. Local workstation inference adds a prototyping path between laptop demos and shared cloud infrastructure: it can improve iteration speed, privacy, cost predictability, and latency when the local runtime matches the production stack, but it still needs reproducible benchmarks and careful precision choices because fitting a model in memory is not the same as serving it responsively. On-device inference adds another serving shape: native runtimes such as MLX Swift LM can stream local tokens directly in an app, but teams still need target-device throughput checks, curated model catalogs, and download-size planning. AI-generated kernels add a specialized optimization path for agentic inference pipelines: agents can search over known tricks such as fusion, tiling, operation rewrites, and hardware ports, but the loop only matters when verified on real target hardware. For image and video diffusion, inference behavior is also the sampler: guidance, denoising step count, and distillation affect quality, diversity, artifacts, and latency.

## Key Concepts

- [Profile small-model architectures on target hardware](../concepts/profile-small-model-architectures-on-target-hardware.md) - local inference performance should be measured on the intended hardware, not inferred from architecture alone.
- [Use local AI workstations when iteration, privacy, or latency dominate](../concepts/use-local-ai-workstations-when-iteration-privacy-or-latency-dominate.md) - local serving can complement cloud infrastructure when queueing, data residency, or deterministic latency drive the workflow.
- [Make local inference benchmarks reproducible artifacts](../concepts/make-local-inference-benchmarks-reproducible-artifacts.md) - benchmark runs should capture environment, responses, timing, and hardware metrics for later verification.
- [Use hardware-in-the-loop search for AI kernel generation](../concepts/use-hardware-in-the-loop-search-for-ai-kernel-generation.md) - generated kernel variants need target-hardware execution and profiling feedback.
- [Use AI kernel generation for known optimization patterns, not expert-level breakthroughs](../concepts/use-ai-kernel-generation-for-known-optimization-patterns-not-expert-level-breakthroughs.md) - agents are useful for searching known optimization spaces and ports, not replacing deeply hand-tuned primitives.
- [Evaluate generated kernels for correctness, performance, and benchmark gaming](../concepts/evaluate-generated-kernels-for-correctness-performance-and-benchmark-gaming.md) - speedups only count when numerical correctness and benchmark methodology hold up.
- [Treat quantization as a memory-bandwidth lever](../concepts/treat-quantization-as-a-memory-bandwidth-lever.md) - precision format can determine whether a locally loaded model is actually interactive.
- [Use MLX Swift LM for Apple local model integration](../concepts/use-mlx-swift-lm-for-apple-local-model-integration.md) - Apple local inference can be integrated as a native app runtime instead of only as a remote service.
- [Interleave local and global attention to trade context for efficiency](../concepts/interleave-local-and-global-attention-to-trade-context-for-efficiency.md) - local windows, periodic global layers, and grouped query attention shape memory and serving cost.
- [Do not treat long context as durable model memory](../concepts/do-not-treat-long-context-as-durable-model-memory.md) - context length changes serving cost and does not by itself guarantee reliable reasoning.
- [KV-cache hit rate is a production agent SLO](../concepts/kv-cache-hit-rate-is-a-production-agent-slo.md) - repeated context reuse should be operated as a latency, cost, and capacity objective.
- [Agent swarms create reusable KV-cache working sets](../concepts/agent-swarms-create-reusable-kv-cache-working-sets.md) - orchestrators, subagents, and tool loops create repeated token regions that inference platforms can cache.
- [Size KV-cache memory tiers with workload-shaped benchmarks](../concepts/size-kv-cache-memory-tiers-with-workload-shaped-benchmarks.md) - cache tiers need benchmarks shaped by agent working sets, TTLs, prefill/decode behavior, and concurrency.
- [Per-layer embeddings move effective-model capacity out of VRAM](../concepts/per-layer-embeddings-move-effective-model-capacity-out-of-vram.md) - flash-backed PLE changes the memory profile of effective on-device models.
- [Hot-swap small models to avoid one-model-per-GPU waste](../concepts/hot-swap-small-models-to-avoid-one-model-per-gpu-waste.md) - many small models can share accelerator capacity when the runtime supports dynamic loading and eviction.
- [Production inference combines model support with cluster operations](../concepts/production-inference-combines-model-support-with-cluster-operations.md) - serving many model families requires both architecture-specific adaptation and production operations.
- [Use small models as context-management tools before agent reasoning](../concepts/use-small-models-as-context-management-tools-before-agent-reasoning.md) - inference infrastructure can expose narrow models as preprocessing and retrieval tools for agent workflows.
- [Small agentic models make parallel workplace agents economical](../concepts/small-agentic-models-make-parallel-workplace-agents-economical.md) - low per-agent cost changes whether multiple concurrent agent copies are practical.
- [Train image and video diffusion models in learned latent spaces](../concepts/train-image-and-video-diffusion-models-in-learned-latent-spaces.md) - latent media representations shrink inference tensors while keeping useful topology.
- [Use guidance to trade diffusion sample diversity for conditional quality](../concepts/use-guidance-to-trade-diffusion-sample-diversity-for-conditional-quality.md) - sampling parameters shape output quality and failure modes.
- [Distill diffusion models to reduce sampling steps](../concepts/distill-diffusion-models-to-reduce-sampling-steps.md) - step reduction is a direct latency lever for diffusion serving.

## Open Questions

- How should teams evaluate the latency and quality tradeoff between preprocessing with small models and sending broader raw context to a larger agent model?
- When should a workload pay inference-time cost for retrieval or deep research versus training-time cost for model adaptation?
- When do local/global attention and grouped query attention provide enough serving efficiency to justify architecture-specific runtime support?
- How should diffusion serving expose guidance, step count, and distillation choices without letting users create predictable artifacts or unacceptable latency?
- Which local workstation benchmarks are strong enough to predict production serving behavior after scaling to cloud or data-center infrastructure?
- Which AI-generated kernel optimizations should be promoted into production once hardware-in-the-loop benchmarks show a speedup?
- Which workplace-agent subtasks are cheap and independent enough to route to many small model copies instead of one larger agent?
- Which KV-cache hit-rate bands are needed before agent swarms stop wasting prefill capacity on repeated prompt, tool-call, and tool-response tokens?

## Sources

- [Context Platform Engineering to Reduce Token Anxiety - Val Bercovici, WEKA](../sources/20251124_NTBX-wxUhHs.md)
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
- [Gemma 4 Deep Dive - Cassidy Hardin, Researcher, Google DeepMind](../sources/20260427__A367W_qvc8.md)
- [Everything I Learned Training Frontier Small Models - Maxime Labonne, Liquid AI](../sources/20260429_fLUtUkqYHnQ.md)
- [Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind](../sources/20260421_xOP1PM8fwnk.md)
- [Running LLMs on your iPhone: 40 tok/s Gemma 4 with MLX - Adrien Grondin, Locally AI](../sources/20260420_a2muGkT4WD4.md)
- [Running LLMs locally: Practical LLM Performance on DGX Spark - Mozhgan Kabiri chimeh, NVIDIA](../sources/20260410_c5-kx2bwoCk.md)
- [Jack Morris: Stuffing Context is not Memory, Updating Weights is](../sources/20251229_Jty4s9-Jb78.md)
- [AI Kernel Generation: What's working, what's not, what's next - Natalie Serrino, Gimlet Labs](../sources/20251217_6guQG_tGt0o.md)
- [Minimax M2: Building the #1 Open Model - Olive Song, MiniMax](../sources/20251213_lY1iFbDPRlw.md)
