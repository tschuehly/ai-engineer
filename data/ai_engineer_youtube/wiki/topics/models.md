# Models

## Overview

Model work in this wiki covers how AI engineers choose, train, adapt, and deploy model architectures under real constraints. The current sources show complementary views: small or edge models make deployment practical when memory, latency, privacy, and accelerator access matter; from-scratch local training exposes the tokenizer, architecture, training-loop, and inference choices that are often hidden behind high-level APIs; generative-media models need data curation, learned latent representations, denoising architectures, and sampling controls suited to image and video topology; and non-language frontier models can be optimized for retrieval, weather, or interactive environments. Edge-scale and local workstation models should be treated as deployment-constrained systems: target hardware, memory capacity, memory bandwidth, runtime support, and quantization format can matter as much as parameter count. Edge-scale models should be profiled on target hardware, quantized to the device envelope, and post-trained for narrow capabilities rather than judged as miniature general-purpose chatbots. Model choice should also account for behavioral reliability: some models improve on public leaderboards while still accepting nonsensical premises, overusing reasoning, or underperforming on fuzzy expert work. Gemma 4 adds a concrete routing pattern inside one open-weight family: effective on-device variants, sparse MoE efficiency, and dense long-context reasoning variants serve different deployment and workflow shapes. Gemma also shows that open model families need ecosystem compatibility: permissive licensing, common runtimes, fine-tuning tools, multilingual tokenizers, quantized Hugging Face distribution, and domain variants can matter as much as the base model when teams adapt models for local, low-resource, safety, or medical workflows. Tiny models add another pattern: specialize and fine-tune narrow components, then compose them into a product workflow.

Encoder models add a guardrail-specific model pattern. When the job is to classify whether an input, retrieved chunk, tool description, model response, or agent plan is safe, a bidirectional encoder with a classification head can be a better production fit than a generative judge because it can inspect the full sequence in one forward pass and return a compact binary or policy label. Agent organizations add a model-routing layer: not every role needs frontier-model cost, so teams should choose models by role intelligence needs, quality bar, budget, and latency.

Long-tail knowledge adaptation adds a memory-oriented model pattern. When a domain is too private, too new, or too underrepresented for a base model, teams can choose between spending at inference time through context, RAG, or deep-research loops and spending at training time by turning source facts into a model update. The source-backed caveat is that naive fine-tuning can memorize and damage general behavior; useful weight updates need curated data generation, selective update strategies, and regression evaluation.

Long-horizon agent models add a post-training pressure: fluent next-token continuation is not the same as sustained task completion. Poolside's public demo frames reinforcement learning as the missing ingredient for moving from completions and chat toward autonomous software-development and knowledge-work agents, especially when the target behavior spans codebase inspection, translation, testing, feature addition, and iterative verification.

Code world models add an execution-aware variant of model training for software. Instead of treating code only as syntax, CWM trains around program execution traces: local variables, memory, line-by-line state, repository-level test and CI traces, and state/action/state transitions. This makes code a constrained world-modeling substrate where a model can learn to simulate program behavior, support neural-debugger interfaces, and reason about expensive execution paths before every real-world action is run.

Coding-model evaluation needs model-family progress to be measured against fresh and appropriately difficult tasks. Dynamic code benchmarks can use post-training-window problem releases and changing difficulty distributions to avoid confusing memorized or saturated task sets with genuine model improvement. As coding models move from completions to repository optimization and translation, evals should also measure whether the model's apparent improvement survives real task distributions, runtime checks, and reward-hack detection.

## Key Concepts

- [Compare models by task, thinking budget, cost, and latency](../concepts/compare-models-by-task-thinking-budget-cost-and-latency.md) - model choice should be routed by workload constraints rather than by size alone.
- [Update coding eval sets dynamically as model capability changes](../concepts/update-coding-eval-sets-dynamically-as-model-capability-changes.md) - coding-model comparisons need fresh tasks and calibrated difficulty to stay meaningful.
- [Grow Agent Organizations Incrementally By Role Quality and Cost](../concepts/grow-agent-organizations-incrementally-by-role-quality-and-cost.md) - agent roles should use models whose quality and price fit the work.
- [Curate generative-media data before tuning model internals](../concepts/curate-generative-media-data-before-tuning-model-internals.md) - data quality can be a stronger lever than model or optimizer changes for image and video models.
- [Train image and video diffusion models in learned latent spaces](../concepts/train-image-and-video-diffusion-models-in-learned-latent-spaces.md) - learned latents reduce media tensor size while preserving spatial or temporal topology.
- [Use guidance to trade diffusion sample diversity for conditional quality](../concepts/use-guidance-to-trade-diffusion-sample-diversity-for-conditional-quality.md) - diffusion sampling settings are part of model behavior, not a cosmetic afterthought.
- [Distill diffusion models to reduce sampling steps](../concepts/distill-diffusion-models-to-reduce-sampling-steps.md) - diffusion distillation targets latency by shortening the denoising path.
- [Expose explicit control signals for generative media models](../concepts/expose-explicit-control-signals-for-generative-media-models.md) - text prompts should be complemented by structured controls when users need predictable media outputs.
- [Ground generated media with current search context](../concepts/ground-generated-media-with-current-search-context.md) - grounded image models combine retrieval, text rendering, localization, and generation.
- [Evaluate whether models reject impossible or nonsensical premises](../concepts/evaluate-whether-models-reject-impossible-or-nonsensical-premises.md) - model reliability includes knowing when not to answer a malformed request.
- [Benchmark narrow slices separately from real expert work](../concepts/benchmark-narrow-slices-separately-from-real-expert-work.md) - public benchmark progress should be interpreted alongside real prompt distributions and expert dissatisfaction.
- [Route Gemma 4 model variants by deployment and workflow shape](../concepts/route-gemma-4-model-variants-by-deployment-and-workflow-shape.md) - Gemma 4's effective, MoE, and dense variants map to different local, hosted, reasoning, coding, and agentic workloads.
- [Open model families need ecosystem-compatible tooling](../concepts/open-model-families-need-ecosystem-compatible-tooling.md) - open models need licensing and toolchain support that fits how developers already run and fine-tune models.
- [Use MLX Swift LM for Apple local model integration](../concepts/use-mlx-swift-lm-for-apple-local-model-integration.md) - model availability for Apple apps depends on MLX-compatible weights and native runtime support.
- [Multilingual tokenizers improve low-resource fine-tuning paths](../concepts/multilingual-tokenizers-improve-low-resource-fine-tuning-paths.md) - tokenizer design can determine whether low-resource or sovereign-language adaptation works well.
- [Domain Gemma variants package specialized policy and task behavior](../concepts/domain-gemma-variants-package-specialized-policy-and-task-behavior.md) - specialized variants give safety and domain workflows a better starting point than generic chat behavior.
- [Treat edge models as their own architecture class](../concepts/treat-edge-models-as-their-own-architecture-class.md) - memory-bound edge models need architecture and training choices optimized for local latency and limited effective parameters.
- [Interleave local and global attention to trade context for efficiency](../concepts/interleave-local-and-global-attention-to-trade-context-for-efficiency.md) - attention placement and grouped query attention can reduce context cost without removing global context flow.
- [Per-layer embeddings move effective-model capacity out of VRAM](../concepts/per-layer-embeddings-move-effective-model-capacity-out-of-vram.md) - PLE shows one way to add representational depth while respecting on-device memory constraints.
- [Tune multimodal token budgets by visual or audio task](../concepts/tune-multimodal-token-budgets-by-visual-or-audio-task.md) - image and audio inputs should spend tokens according to the modality's actual task value.
- [Profile small-model architectures on target hardware](../concepts/profile-small-model-architectures-on-target-hardware.md) - operator choices should be validated on the CPUs, phones, GPUs, and accelerators that will run the model.
- [Treat quantization as a memory-bandwidth lever](../concepts/treat-quantization-as-a-memory-bandwidth-lever.md) - precision choices affect throughput and time to first token, not only whether a model fits.
- [Post-train small models for narrow capabilities](../concepts/post-train-small-models-for-narrow-capabilities.md) - data extraction, tool use, and other focused tasks are better targets than average performance across every benchmark.
- [Build RL environments as software artifacts](../concepts/build-rl-environments-as-software-artifacts.md) - interactive post-training tasks need runnable environments, parsers, state, and rewards rather than only static examples.
- [Pair next-token prediction with reinforcement learning for long-horizon work](../concepts/pair-next-token-prediction-with-reinforcement-learning-for-long-horizon-work.md) - long-horizon model behavior needs task-completion feedback beyond fluent continuations.
- [Train code models on execution traces, not only syntax](../concepts/train-code-models-on-execution-traces-not-only-syntax.md) - execution traces expose program dynamics that token-only source modeling can miss.
- [Use neural debugging to fill code by simulated execution](../concepts/use-neural-debugging-to-fill-code-by-simulated-execution.md) - execution-aware code models can complete partial code from simulated state and surrounding structure.
- [Use verifiable rewards for language-model RL](../concepts/use-verifiable-rewards-for-language-model-rl.md) - automatic outcome checks can turn task success, format compliance, and action validity into training signals.
- [Bootstrap RL with targeted SFT before reinforcement learning](../concepts/bootstrap-rl-with-targeted-sft-before-reinforcement-learning.md) - small models may need a syntax and valid-action warm-up before RL can improve strategy.
- [Control environment noise for group-based RL](../concepts/control-environment-noise-for-group-based-rl.md) - grouped rollout methods need comparable environments, controlled difficulty, and stable batch sizing.
- [Mitigate small-model doom loops during preference alignment and RL](../concepts/mitigate-small-model-doom-loops-during-preference-alignment-and-rl.md) - tiny reasoning models need post-training checks for repetitive loops that SFT may not remove.
- [Match Gemma edge model size to device memory and interaction class](../concepts/match-gemma-edge-model-size-to-device-memory-and-interaction-class.md) - model size is an engineering decision tied to device capability and product interaction.
- [Use small models as context-management tools before agent reasoning](../concepts/use-small-models-as-context-management-tools-before-agent-reasoning.md) - specialized small models can prepare context before a larger reasoning model is invoked.
- [Fine-tuned encoder discriminators make low-latency guardrails practical](../concepts/fine-tuned-encoder-discriminators-make-low-latency-guardrails-practical.md) - encoder classifiers can specialize safety checks without invoking a generative model.
- [Local LLM training exposes the core model-building stack](../concepts/local-llm-training-exposes-the-core-model-building-stack.md) - local from-scratch training clarifies the core pieces behind model behavior.
- [Tokenizer size must match data and compute budget](../concepts/tokenizer-size-must-match-data-and-compute-budget.md) - tokenizer capacity should fit the data, domain, modality, and training budget.
- [Use loss curves to debug local model training](../concepts/use-loss-curves-to-debug-local-model-training.md) - train and validation loss patterns reveal learning, overfitting, and instability.
- [Modular tiny-model pipelines reuse specialized models across mobile app workflows](../concepts/modular-tiny-model-pipelines-reuse-specialized-models-across-mobile-app-workflows.md) - narrow fine-tuned models can be composed into mobile app pipelines and reused across features.
- [Use omnimodal embeddings for cross-modal retrieval and comparison](../concepts/use-omnimodal-embeddings-for-cross-modal-retrieval-and-comparison.md) - embedding models are companion models for retrieval, recognition, and comparison across modalities.
- [Adapt embedding dimensions with Matryoshka representation learning](../concepts/adapt-embedding-dimensions-with-matryoshka-representation-learning.md) - one embedding model can expose different dimensionalities for cost and quality tradeoffs.
- [Do not treat long context as durable model memory](../concepts/do-not-treat-long-context-as-durable-model-memory.md) - model memory should not be conflated with transient prompt activations.
- [Train long-tail knowledge into weights with curated synthetic data](../concepts/train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md) - specialized knowledge can be trained into weights when raw fine-tuning is converted into a safer data and update process.
- [Neural weather models can target operational forecast variables directly](../concepts/neural-weather-models-can-target-operational-forecast-variables-directly.md) - forecasting models should match architecture and target variables to operational use.
- [Interactive world models need memory, control, and live prompting](../concepts/interactive-world-models-need-memory-control-and-live-prompting.md) - generated environments need stateful interaction, not only plausible frames.

## Open Questions

- How should tokenizer decisions change when a model must support mixed modalities or mixed domains rather than a single constrained corpus?
- Which lightweight generated-sample checks complement train/validation loss for tiny local model runs?
- When is a modular set of fine-tuned tiny models preferable to one larger model with prompting or skills?
- Which small-model failures should be fixed with architecture, post-training data, runtime tools, or product task narrowing?
- Which interactive tasks have reward signals clear enough to justify building an RL environment rather than collecting more SFT examples?
- How should teams evaluate sparse MoE, effective on-device, and dense long-context models against the same agent workflow without hiding deployment cost differences?
- When should a team fine-tune an open model directly, start from a domain variant, or rely on a hosted API model for maximum raw capability?
- What evaluation suite is sufficient before promoting a weight-updated long-tail model over RAG or full-context prompting?
- When does adding reasoning effort improve model judgment, and when does it simply make accommodation of a bad premise longer?
- Which media-generation failures should be fixed through data curation, latent representation design, sampling settings, distillation, or explicit controls?
- Which non-language tasks should be handled by specialized frontier models instead of routed through a general LLM?
- Which quantization formats preserve enough quality while improving local model responsiveness for each hardware class?
- Which coding-eval time windows best separate memorized benchmark behavior from genuine current model capability?

## Sources

- [Build & deploy AI-powered apps - Paige Bailey, Google DeepMind](../sources/20260429_G_bHFmEAarM.md)
- [Gemma 4 Deep Dive - Cassidy Hardin, Researcher, Google DeepMind](../sources/20260427__A367W_qvc8.md)
- [Everything I Learned Training Frontier Small Models - Maxime Labonne, Liquid AI](../sources/20260429_fLUtUkqYHnQ.md)
- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md)
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
- [Training an LLM from Scratch, Locally - Angelos Perivolaropoulos, ElevenLabs](../sources/20260504_UsB70Tf5zcE.md)
- [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM - Cormac Brick, Google](../sources/20260503_BKWpYIWvAo4.md)
- [What Do Models Still Suck At? - Peter Gostev, Arena.ai, BullshitBench](../sources/20260424_R7A8rX-09Zw.md)
- [Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind](../sources/20260421_xOP1PM8fwnk.md)
- [Gemma, DeepMind's Family of Open Models - Omar Sanseviero, Google DeepMind](../sources/20260420__gVFUEdhCyI.md)
- [Running LLMs on your iPhone: 40 tok/s Gemma 4 with MLX - Adrien Grondin, Locally AI](../sources/20260420_a2muGkT4WD4.md)
- [How Google DeepMind is researching the next Frontier of AI for Gemini - Raia Hadsell, VP of Research](../sources/20260418_zZsTVBXcbow.md)
- [$1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs - Diego Carpentero](../sources/20260416_YZHPEkfy2kc.md)
- [Paperclip: Open Source Human Control Plane for AI Labor - Dotta Bippa](../sources/20260415_h403btjldDQ.md)
- [Running LLMs locally: Practical LLM Performance on DGX Spark - Mozhgan Kabiri chimeh, NVIDIA](../sources/20260410_c5-kx2bwoCk.md)
- [Let LLMs Wander: Engineering RL Environments - Stefano Fiorucci](../sources/20260408_71V3fTaUp2Q.md)
- [Jack Morris: Stuffing Context is not Memory, Updating Weights is](../sources/20251229_Jty4s9-Jb78.md)
- [AGI: The Path Forward - Jason Warner & Eiso Kant, Poolside](../sources/20251227_OGCG_QkCcZo.md)
- [Code World Model: Building World Models for Computation - Jacob Kahn, FAIR Meta](../sources/20251217_sYgE4ppDFOQ.md)
- [Building in the Gemini Era - Kat Kampf & Ammaar Reshi, Google DeepMind](../sources/20251215_fgkXEIbZpGc.md)
- [Coding Evals: From Code Snippets to Codebases - Naman Jain, Cursor](../sources/20251215_tHN44yJoeS8.md)
