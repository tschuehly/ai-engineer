# Inference

## Overview

Inference is the production discipline of turning trained models into reliable, efficient services. For small models, the main constraint is often not raw compute alone but orchestration across many specialized models: dynamic loading, routing, batching, model-specific runtime support, observability, and autoscaling determine whether the system wastes GPU capacity or becomes a reusable agent and retrieval substrate. At the architecture level, inference cost is also shaped by attention and memory choices: sparse expert activation, local/global attention mixes, grouped query attention, quantization, flash-backed embedding tables, and hardware-specific kernels can change the practical serving envelope before cluster operations even begin. Long-context serving adds the same lesson from another angle: every extra prompt token can increase cost and latency, and large windows do not guarantee stable reasoning over the added material. Agentic long-context serving adds a KV-cache layer to that problem: orchestrators, subagents, tool calls, and tool responses create repeated token regions, so cache hit rate, time-to-live, prefill/decode behavior, and memory-tier throughput can determine cost, rate limits, and useful concurrency. Local workstation inference adds a prototyping path between laptop demos and shared cloud infrastructure: it can improve iteration speed, privacy, cost predictability, and latency when the local runtime matches the production stack, but it still needs reproducible benchmarks and careful precision choices because fitting a model in memory is not the same as serving it responsively. Compiler-based inference adds another portability path: plain Python model code can be traced into an IR, type-propagated, lowered to C++ or Rust, compiled into a native library, and hidden behind an API-compatible client so local, edge, desktop, mobile, and cloud deployment targets do not all force different application code. On-device inference adds another serving shape: native runtimes such as MLX Swift LM can stream local tokens directly in an app, but teams still need target-device throughput checks, curated model catalogs, and download-size planning. AI-generated kernels add a specialized optimization path for agentic inference pipelines: agents can search over known tricks such as fusion, tiling, operation rewrites, and hardware ports, but the loop only matters when verified on real target hardware. For image and video diffusion, inference behavior is also the sampler: guidance, denoising step count, and distillation affect quality, diversity, artifacts, and latency.

Open frontier-scale models add an adoption constraint to inference: availability of weights is not enough when a model is too large for ordinary local hardware. GLM 4.6 is described as a 355B-parameter model that can be served through open-source inference stacks such as SGLang and vLLM when enough GPUs are available, while hosted/API access and coding-assistant integrations provide easier adoption paths for teams without large accelerator pools. Model marketplaces add a different adoption layer: one routing API can hide provider-specific edge cases, caching, tool-calling differences, regional routing, privacy controls, and observability while preserving the ability to compare and switch models.

Application builders should treat that routing layer as a strategic default, not only an operational convenience. A competitive model market means last year's strong model can become cheap enough for broad use while newer providers or open-source releases change the quality frontier, so products should keep room to choose the right model at the right time.

Brockman's infrastructure view adds a serving-shape warning: realtime AI interfaces and long compute-heavy jobs are different workloads. Inference platforms need to account for both low-latency interaction and longer test-time or agentic compute, because a fleet balanced for the wrong mix can waste scarce accelerator capacity.

Compute marketplaces add a lower-level routing problem beneath model marketplaces: the same product may need long training runs, temporary experiment bursts, online inference, and offline batch inference at different times. A GPU aggregation layer can reduce over-reservation only if the platform exposes workload-shaped commitments and verifies heterogeneous supplier performance well enough for the inference or training job being routed.

Morph's reasoning-time branching pattern adds another long-running inference shape: instead of one model call consuming more hidden thinking tokens, the system can branch the external environment, run parallel agents against the same state, and choose verifier-passing branches. Capacity planning then has to include workspace snapshot overhead, branch fanout, verifier cost, and the wall-clock goal of finding a good branch faster than a single linear run.

NVIDIA Dynamo's inference-frontier framing adds a data-center serving lens: the useful target is an application's operating point across quality, latency, and cost, not a single benchmark metric. Distributed inference can move that point by disaggregating compute-bound prefill from often memory-bound decode, routing requests by both KV locality and worker load, exploiting agent structure such as re-query loops and tool-call waits to preserve KV state, and dynamically shifting specialized worker pools as input and output sequence distributions change.

Realtime voice serving adds an audio-token variant of the same discipline. A TTS model that emits codec tokens has to generate fast enough for playback, not just fast enough for text UX; leading generated silence, adapter loading, batch shape, and quantization choices all affect whether the first useful audio arrives inside the conversation window.

## Key Concepts

- [Dual-mode AI infrastructure](../concepts/dual-mode-ai-infrastructure.md) - inference fleets should distinguish realtime latency needs from long compute-heavy workloads.
- [Scale Test-Time Search Through Parallel Verifier-Checked Branches](../concepts/scale-test-time-search-through-parallel-verifier-checked-branches.md) - test-time compute can fan out into external branch attempts scored by verifiers.
- [Tune inference to the application Pareto point](../concepts/tune-inference-to-the-application-pareto-point.md) - model-serving choices should target the application's quality, latency, and cost operating point.
- [Serve Realtime TTS By Audio-Token Throughput](../concepts/serve-realtime-tts-by-audio-token-throughput.md) - streaming voice inference needs generated codec-token throughput that stays ahead of playback.
- [Remove Head-Of-Line Silence From Voice Models](../concepts/remove-head-of-line-silence-from-voice-models.md) - generated leading silence burns inference time before useful audio exists.
- [Route LoRA Voice Clones With Sticky GPU Affinity](../concepts/route-lora-voice-clones-with-sticky-gpu-affinity.md) - adapter-aware routing keeps sessions near the GPU state needed for realtime voice clones.
- [Disaggregate prefill and decode workers by workload shape](../concepts/disaggregate-prefill-and-decode-workers-by-workload-shape.md) - prefill and decode stress hardware differently and can benefit from separate worker pools.
- [Route inference requests by KV locality and worker load](../concepts/route-inference-requests-by-kv-locality-and-worker-load.md) - KV-friendly routing should still account for queue depth and worker load.
- [Exploit structured agent waits for KV-cache manipulation](../concepts/exploit-structured-agent-waits-for-kv-cache-manipulation.md) - tool-call and re-query structure can tell the serving layer when to offload or restore KV state.
- [Autoscale specialized inference workers as traffic mix changes](../concepts/autoscale-specialized-inference-workers-as-traffic-mix-changes.md) - worker mix should adapt as input and output sequence length distributions shift.
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
- [Compile Python inference functions into portable native binaries](../concepts/compile-python-inference-functions-into-portable-native-binaries.md) - Python inference can be packaged as native libraries when portability and low-latency deployment matter.
- [Expose local and open-source models through familiar API clients](../concepts/expose-local-and-open-source-models-through-familiar-api-clients.md) - API compatibility can hide whether a model runs through a hosted service, local runtime, or compiled binary.
- [Abstract LLM inference behind one routing API](../concepts/abstract-llm-inference-behind-one-routing-api.md) - routing layers can normalize model access, provider differences, observability, privacy, and tool-calling support.
- [Plan AI products for a multimodel market](../concepts/plan-ai-products-for-a-multimodel-market.md) - application infrastructure should assume model choice, pricing, and capability will keep changing.
- [Match GPU Commitments To Workload Lifecycle](../concepts/match-gpu-commitments-to-workload-lifecycle.md) - compute access should match training, experiment, online inference, and offline inference phases.
- [Aggregate Idle GPU Supply Through Compute Marketplaces](../concepts/aggregate-idle-gpu-supply-through-compute-marketplaces.md) - pooled accelerator supply can change the cost envelope for model training and serving.
- [Open model families need ecosystem-compatible tooling](../concepts/open-model-families-need-ecosystem-compatible-tooling.md) - open-weight models need serving, fine-tuning, and integration support before developers can use them.
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
- Which provider differences should model-routing APIs normalize, and which should remain visible because they affect quality or risk?
- Which inference metrics distinguish realtime user interaction from long-running agentic compute in capacity plans?
- Which workloads are safe to route through lower-cost marketplace GPUs, and which require reserved, benchmarked, or reliability-backed capacity?
- How should inference platforms expose prefill/decode, KV-routing, and worker-specialization controls without making every application team become serving-infrastructure experts?

## Sources

- [#define AI Engineer - Greg Brockman, OpenAI (ft. Jensen Huang)](../sources/20250810_avWhreBUYF0.md)
- [Context Platform Engineering to Reduce Token Anxiety - Val Bercovici, WEKA](../sources/20251124_NTBX-wxUhHs.md)
- [Compilers in the Age of LLMs - Yusuf Olokoba, Muna](../sources/20251124_q2nHsJVy4FE.md)
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
- [Gemma 4 Deep Dive - Cassidy Hardin, Researcher, Google DeepMind](../sources/20260427__A367W_qvc8.md)
- [Everything I Learned Training Frontier Small Models - Maxime Labonne, Liquid AI](../sources/20260429_fLUtUkqYHnQ.md)
- [Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind](../sources/20260421_xOP1PM8fwnk.md)
- [Running LLMs on your iPhone: 40 tok/s Gemma 4 with MLX - Adrien Grondin, Locally AI](../sources/20260420_a2muGkT4WD4.md)
- [Running LLMs locally: Practical LLM Performance on DGX Spark - Mozhgan Kabiri chimeh, NVIDIA](../sources/20260410_c5-kx2bwoCk.md)
- [Jack Morris: Stuffing Context is not Memory, Updating Weights is](../sources/20251229_Jty4s9-Jb78.md)
- [AI Kernel Generation: What's working, what's not, what's next - Natalie Serrino, Gimlet Labs](../sources/20251217_6guQG_tGt0o.md)
- [Minimax M2: Building the #1 Open Model - Olive Song, MiniMax](../sources/20251213_lY1iFbDPRlw.md)
- [Z.ai GLM 4.6: What We Learned From 100 Million Open Source Downloads - Yuxuan Zhang, Z.ai](../sources/20251122_m6MF1OR_9kM.md)
- [The Next Unicorns: 7 Top AI startups from the HF0 Residency](../sources/20250821_L8-5ezsoI5A.md)
- [State of Startups and AI 2025 - Sarah Guo, Conviction](../sources/20250802_3MZS5gNElZM.md)
- [Infrastructure for the Singularity - Jesse Han, Morph](../sources/20250801_2goSS66XRBk.md)
- [Why We Don't Need More Data Centers - Dr. Jasper Zhang, Hyperbolic](../sources/20250801_M6Vbaig1TsM.md)
- [Hacking the Inference Pareto Frontier - Kyle Kranen, NVIDIA](../sources/20250801_Y2qc0UhDSnc.md)
- [Serving Voice AI at $1/hr: Open-source, LoRAs, Latency, Load Balancing - Neil Dwyer, Gabber](../sources/20250731_rD23-VZZHOo.md)
