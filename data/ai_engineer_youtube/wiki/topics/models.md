# Models

## Overview

Model work in this wiki covers how AI engineers choose, train, adapt, and deploy model architectures under real constraints. The current sources show complementary views: small or edge models make deployment practical when memory, latency, privacy, and accelerator access matter; from-scratch local training exposes the tokenizer, architecture, training-loop, and inference choices that are often hidden behind high-level APIs; generative-media models need data curation, learned latent representations, denoising architectures, sampling controls, artifact-aware data, and perceptual evals suited to image and video topology; and non-language frontier models can be optimized for retrieval, weather, or interactive environments. Edge-scale and local workstation models should be treated as deployment-constrained systems: target hardware, memory capacity, memory bandwidth, runtime support, and quantization format can matter as much as parameter count. Edge-scale models should be profiled on target hardware, quantized to the device envelope, and post-trained for narrow capabilities rather than judged as miniature general-purpose chatbots. Model choice should also account for behavioral reliability: some models improve on public leaderboards while still accepting nonsensical premises, overusing reasoning, or underperforming on fuzzy expert work. Gemma 4 adds a concrete routing pattern inside one open-weight family: effective on-device variants, sparse MoE efficiency, and dense long-context reasoning variants serve different deployment and workflow shapes. Gemma also shows that open model families need ecosystem compatibility: permissive licensing, common runtimes, fine-tuning tools, multilingual tokenizers, quantized Hugging Face distribution, domain variants, and familiar client APIs can matter as much as the base model when teams adapt models for local, low-resource, safety, or medical workflows. Tiny models add another pattern: specialize and fine-tune narrow components, then compose them into a product workflow.

Encoder models add a guardrail-specific model pattern. When the job is to classify whether an input, retrieved chunk, tool description, model response, or agent plan is safe, a bidirectional encoder with a classification head can be a better production fit than a generative judge because it can inspect the full sequence in one forward pass and return a compact binary or policy label. Agent organizations add a model-routing layer: not every role needs frontier-model cost, so teams should choose models by role intelligence needs, quality bar, budget, and latency.

Long-tail knowledge adaptation adds a memory-oriented model pattern. When a domain is too private, too new, or too underrepresented for a base model, teams can choose between spending at inference time through context, RAG, or deep-research loops and spending at training time by turning source facts into a model update. The source-backed caveat is that naive fine-tuning can memorize and damage general behavior; useful weight updates need curated data generation, selective update strategies, and regression evaluation.

Long-horizon agent models add a post-training pressure: fluent next-token continuation is not the same as sustained task completion. Poolside's public demo frames reinforcement learning as the missing ingredient for moving from completions and chat toward autonomous software-development and knowledge-work agents, especially when the target behavior spans codebase inspection, translation, testing, feature addition, and iterative verification.

Code world models add an execution-aware variant of model training for software. Instead of treating code only as syntax, CWM trains around program execution traces: local variables, memory, line-by-line state, repository-level test and CI traces, and state/action/state transitions. This makes code a constrained world-modeling substrate where a model can learn to simulate program behavior, support neural-debugger interfaces, and reason about expensive execution paths before every real-world action is run.

Coding-model evaluation needs model-family progress to be measured against fresh and appropriately difficult tasks. Dynamic code benchmarks can use post-training-window problem releases and changing difficulty distributions to avoid confusing memorized or saturated task sets with genuine model improvement. As coding models move from completions to repository optimization and translation, evals should also measure whether the model's apparent improvement survives real task distributions, runtime checks, and reward-hack detection.

Coding and workplace-agent models also need training signals that look like the work they will do. MiniMax M2 adds a compact open-weight model pattern: train against scaled coding environments and verifiable goals, use expert developers as a reward/evaluation source, teach repeated reasoning-tool loops for noisy environments, perturb scaffolds so the behavior is not tied to one harness, and exploit small active-parameter cost when many parallel agent copies are useful.

Cline's RL environment factory adds a data-production pattern for that training pressure: real coding-agent sessions can be converted into portable environments with start states, prompts, solved end states, traces, and outcome verifiers. In that framing, the agent product is not only an interface around current models; it is also a source of hard tasks that can shape future model capability. Prime Intellect generalizes this environment pattern beyond RL: a product harness with tasks and rewards can become an eval, synthetic-data generator, SFT or distillation source, RL training loop, and model-customization substrate.

Applied Compute adds the enterprise specialization and systems-efficiency layer for RL. In that framing, RL turns private customer workflows into private benchmarks, then improves a specialized model through repeated use and data flywheels. Because those runs serve customer delivery rather than open-ended lab research, speed, cost, and low-variance runtime are product requirements. Asynchronous pipeline RL can improve GPU utilization by decoupling sampling from training, but it introduces stale-policy tokens and a throughput/stability tradeoff that has to be modeled before launch.

OpenAI's Agent RFT talk adds a hosted, tool-using version of that post-training pattern. It treats reinforcement fine-tuning as a late-stage lever for multi-step agents after teams have matched training and eval data to production, measured a base-model baseline, and optimized prompts, tools, and task shape. The model learns from sampled trajectories that call real tool endpoints and receive custom reward signals, so useful gains depend on objective task definitions, enough exploration variance, and graders that capture production success rather than easy-to-game proxy behavior.

Cursor Composer adds a product-owned coding-model example: reinforcement learning can specialize a model for a concrete IDE agent workflow when the training loop uses high-quality data, enough compute, and the same tools and environment the model will see at inference time. Its reported improvements are behavioral as much as benchmark-oriented: the model learned to use semantic search, read files before editing, and call tools in parallel.

GLM 4.6 adds a staged open-model training recipe for long-context coding and agent behavior. The useful pattern is not just more tokens: general pretraining is followed by code and reasoning continuation, repo-level code contexts, synthetic reasoning traces, long-context agent data, and RL systems that treat short reasoning tasks differently from slow software-engineering trajectories. Its reported post-training details also expose concrete failure modes: multistage short-to-long RL can erode long-context ability, sequence-mean loss can encourage short reward-seeking coding outputs, and mixed-quality scientific reasoning data can underperform smaller expert-verified datasets.

Brockman's research-engineering framing keeps model progress tied to executable systems. The AlexNet example combines an idea with fast GPU kernels, and current frontier work adds 100,000-GPU systems plus complex RL orchestration. Model capability should therefore be understood as the product of research direction, data, training method, runtime systems, and infrastructure rather than a research paper or parameter count alone.

Morph's Magi 1 framing pushes that idea toward branch-aware reasoning models: the model is intended to be trained from the ground up to use a branchable cloud substrate, delegate to subagents, run verified environment searches, and call external verification software. The reusable model lesson is that some capabilities may require co-designing the model objective with the execution environment rather than adding a tool after training.

Computer-vision models add a visual-fidelity caveat to multimodal model selection. Caption-aligned VLMs can look semantically competent while missing fine details that captions never supervised, such as object part pose, direction, clock hands, or domain-specific visual classes. Vision-only self-supervised backbones such as DINOv2 can preserve richer visual feature structure, but the useful engineering target is aligning those features with language and object-detection heads without reducing them to caption-level semantics.

Robot foundation models add action as another model output modality. GR00T N1's vision-language-action framing combines image observations, robot state, and language prompts, then outputs action trajectories through a dual-system architecture and embodiment-specific decoder. The model lesson is that physical AI needs scarce action data, sim-to-real strategy, realtime control, and body-specific output adaptation in addition to ordinary foundation-model pretraining.

Mechanistic interpretability adds a model-internal engineering surface. Instead of treating the model as only a prompt-response box, feature attribution can show which learned concepts contributed to a token, activation steering can adjust a behavior at inference time, dynamic prompting can trigger instructions when internal features fire, and model diffs can inspect post-training changes. These controls should be evaluated like any other model intervention because they can be powerful, hidden from users, and narrower than ordinary prompt or fine-tuning changes.

## Key Concepts

- [Use Eagle 3 Speculative Decoding With Matched Draft Models](../concepts/use-eagle-3-speculative-decoding-with-matched-draft-models.md) - speculative decoding draft models need to be matched to the target model rather than treated as arbitrary smaller substitutes.
- [SGLang Serves Models Through Configured OpenAI-Compatible Servers](../concepts/sglang-serves-models-through-configured-openai-compatible-servers.md) - model availability depends on serving-framework support, hardware settings, and API-compatible deployment paths.
- [AI Engineering Practice Is Heterogeneous and Fast Moving](../concepts/ai-engineering-practice-is-heterogeneous-and-fast-moving.md) - model strategy must tolerate frequent updates and multiple concurrent use cases.
- [Multimodal Models Have a Production Adoption Gap](../concepts/multimodal-models-have-a-production-adoption-gap.md) - image, video, and audio capabilities still trail text in workplace production use.
- [Research engineering partnership](../concepts/research-engineering-partnership.md) - model progress requires ideas and engineering systems to land together.
- [Train Reasoning Models For Verified Environment Branching](../concepts/train-reasoning-models-for-verified-environment-branching.md) - branch-aware reasoning depends on model training and execution substrate co-design.
- [Compare models by task, thinking budget, cost, and latency](../concepts/compare-models-by-task-thinking-budget-cost-and-latency.md) - model choice should be routed by workload constraints rather than by size alone.
- [Update coding eval sets dynamically as model capability changes](../concepts/update-coding-eval-sets-dynamically-as-model-capability-changes.md) - coding-model comparisons need fresh tasks and calibrated difficulty to stay meaningful.
- [Grow Agent Organizations Incrementally By Role Quality and Cost](../concepts/grow-agent-organizations-incrementally-by-role-quality-and-cost.md) - agent roles should use models whose quality and price fit the work.
- [Curate generative-media data before tuning model internals](../concepts/curate-generative-media-data-before-tuning-model-internals.md) - data quality can be a stronger lever than model or optimizer changes for image and video models.
- [Account for compression artifacts in media model data and evals](../concepts/account-for-compression-artifacts-in-media-model-data-and-evals.md) - internet-scale media data may already encode perceptual compression assumptions.
- [Personalize aesthetic evals with preference classifiers](../concepts/personalize-aesthetic-evals-with-preference-classifiers.md) - learned preference models can make subjective media quality usable as a product signal.
- [Train image and video diffusion models in learned latent spaces](../concepts/train-image-and-video-diffusion-models-in-learned-latent-spaces.md) - learned latents reduce media tensor size while preserving spatial or temporal topology.
- [Use guidance to trade diffusion sample diversity for conditional quality](../concepts/use-guidance-to-trade-diffusion-sample-diversity-for-conditional-quality.md) - diffusion sampling settings are part of model behavior, not a cosmetic afterthought.
- [Distill diffusion models to reduce sampling steps](../concepts/distill-diffusion-models-to-reduce-sampling-steps.md) - diffusion distillation targets latency by shortening the denoising path.
- [Expose explicit control signals for generative media models](../concepts/expose-explicit-control-signals-for-generative-media-models.md) - text prompts should be complemented by structured controls when users need predictable media outputs.
- [Ground generated media with current search context](../concepts/ground-generated-media-with-current-search-context.md) - grounded image models combine retrieval, text rendering, localization, and generation.
- [Use vision-only features when captions erase visual distinctions](../concepts/use-vision-only-features-when-captions-erase-visual-distinctions.md) - caption supervision can miss visual distinctions that self-supervised visual features preserve.
- [Evaluate vision models on domain adaptability and few-shot grounding](../concepts/evaluate-vision-models-on-domain-adaptability-and-few-shot-grounding.md) - object-detection models should be compared on specialized domains and few-shot grounding, not only common-class benchmarks.
- [Mechanistic Interpretability Turns Model Internals Into Engineering Surfaces](../concepts/mechanistic-interpretability-turns-model-internals-into-engineering-surfaces.md) - model features and activations can become inspectable controls for debugging and steering.
- [Activation Steering Can Patch Specific Runtime Behaviors](../concepts/activation-steering-can-patch-specific-runtime-behaviors.md) - raising or lowering specific features can change targeted model behavior at inference time.
- [Use Activation Triggers for Dynamic Prompting](../concepts/use-activation-triggers-for-dynamic-prompting.md) - internal feature activations can decide when runtime prompts or context should be injected.
- [Model Diffs Inspect Post-Training Feature Changes](../concepts/model-diffs-inspect-post-training-feature-changes.md) - feature-level diffs can reveal behavioral shifts after post-training.
- [Interpretability-Native Interfaces Expose Concept-Level Model Controls](../concepts/interpretability-native-interfaces-expose-concept-level-model-controls.md) - learned concepts can become direct UI controls for generative models.
- [Evaluate whether models reject impossible or nonsensical premises](../concepts/evaluate-whether-models-reject-impossible-or-nonsensical-premises.md) - model reliability includes knowing when not to answer a malformed request.
- [Benchmark narrow slices separately from real expert work](../concepts/benchmark-narrow-slices-separately-from-real-expert-work.md) - public benchmark progress should be interpreted alongside real prompt distributions and expert dissatisfaction.
- [Route Gemma 4 model variants by deployment and workflow shape](../concepts/route-gemma-4-model-variants-by-deployment-and-workflow-shape.md) - Gemma 4's effective, MoE, and dense variants map to different local, hosted, reasoning, coding, and agentic workloads.
- [Open model families need ecosystem-compatible tooling](../concepts/open-model-families-need-ecosystem-compatible-tooling.md) - open models need licensing and toolchain support that fits how developers already run and fine-tune models.
- [Expose local and open-source models through familiar API clients](../concepts/expose-local-and-open-source-models-through-familiar-api-clients.md) - local model adoption improves when application code can keep a hosted-API-shaped interface.
- [Use MLX Swift LM for Apple local model integration](../concepts/use-mlx-swift-lm-for-apple-local-model-integration.md) - model availability for Apple apps depends on MLX-compatible weights and native runtime support.
- [Multilingual tokenizers improve low-resource fine-tuning paths](../concepts/multilingual-tokenizers-improve-low-resource-fine-tuning-paths.md) - tokenizer design can determine whether low-resource or sovereign-language adaptation works well.
- [Domain Gemma variants package specialized policy and task behavior](../concepts/domain-gemma-variants-package-specialized-policy-and-task-behavior.md) - specialized variants give safety and domain workflows a better starting point than generic chat behavior.
- [Treat edge models as their own architecture class](../concepts/treat-edge-models-as-their-own-architecture-class.md) - memory-bound edge models need architecture and training choices optimized for local latency and limited effective parameters.
- [Interleave local and global attention to trade context for efficiency](../concepts/interleave-local-and-global-attention-to-trade-context-for-efficiency.md) - attention placement and grouped query attention can reduce context cost without removing global context flow.
- [Per-layer embeddings move effective-model capacity out of VRAM](../concepts/per-layer-embeddings-move-effective-model-capacity-out-of-vram.md) - PLE shows one way to add representational depth while respecting on-device memory constraints.
- [Tune multimodal token budgets by visual or audio task](../concepts/tune-multimodal-token-budgets-by-visual-or-audio-task.md) - image and audio inputs should spend tokens according to the modality's actual task value.
- [Robotics Data Pyramids Combine Scarce Real Trajectories With Synthetic Data](../concepts/robotics-data-pyramids-combine-scarce-real-trajectories-with-synthetic-data.md) - robot foundation models need data strategies beyond scraping because action traces are scarce.
- [Dual-System VLA Architectures Separate Planning From Realtime Control](../concepts/dual-system-vla-architectures-separate-planning-from-realtime-control.md) - VLA models can split slow task planning from high-frequency motor execution.
- [Embodiment-Specific Action Decoders Make Robot Foundation Models Adaptable](../concepts/embodiment-specific-action-decoders-make-robot-foundation-models-adaptable.md) - shared robot-model knowledge becomes deployable through body-specific action decoding.
- [Profile small-model architectures on target hardware](../concepts/profile-small-model-architectures-on-target-hardware.md) - operator choices should be validated on the CPUs, phones, GPUs, and accelerators that will run the model.
- [Treat quantization as a memory-bandwidth lever](../concepts/treat-quantization-as-a-memory-bandwidth-lever.md) - precision choices affect throughput and time to first token, not only whether a model fits.
- [Post-train small models for narrow capabilities](../concepts/post-train-small-models-for-narrow-capabilities.md) - data extraction, tool use, and other focused tasks are better targets than average performance across every benchmark.
- [Build RL environments as software artifacts](../concepts/build-rl-environments-as-software-artifacts.md) - interactive post-training tasks need runnable environments, parsers, state, and rewards rather than only static examples.
- [Treat environments as eval, data, and training substrates](../concepts/treat-environments-as-eval-data-and-training-substrates.md) - environments preserve optionality across evals, synthetic data, SFT, distillation, and RL.
- [Product harnesses can become model customization environments](../concepts/product-harnesses-can-become-model-customization-environments.md) - product-specific behavior can be trained inside the same harness that defines the user experience.
- [Environment registries make AI research more accessible](../concepts/environment-registries-make-ai-research-more-accessible.md) - packaged environments make model research easier to share and run.
- [Pair next-token prediction with reinforcement learning for long-horizon work](../concepts/pair-next-token-prediction-with-reinforcement-learning-for-long-horizon-work.md) - long-horizon model behavior needs task-completion feedback beyond fluent continuations.
- [Train code models on execution traces, not only syntax](../concepts/train-code-models-on-execution-traces-not-only-syntax.md) - execution traces expose program dynamics that token-only source modeling can miss.
- [Use neural debugging to fill code by simulated execution](../concepts/use-neural-debugging-to-fill-code-by-simulated-execution.md) - execution-aware code models can complete partial code from simulated state and surrounding structure.
- [Train coding-agent models with environments and expert developer reward](../concepts/train-coding-agent-models-with-environments-and-expert-developer-reward.md) - coding-agent model quality should be shaped by verifiable environments and developer trust judgments.
- [Production-Matched RL Environments Train Coding Agents on Real Tool Surfaces](../concepts/production-matched-rl-environments-train-coding-agents-on-real-tool-surfaces.md) - production-like tool loops make specialized coding-model training more likely to transfer.
- [Train coding models on repo-level contexts](../concepts/train-coding-models-on-repo-level-contexts.md) - coding-model data should expose project structure, linked files, issues, pull requests, and execution traces.
- [Use hybrid RL system design for agent trajectories](../concepts/use-hybrid-rl-system-design-for-agent-trajectories.md) - short reasoning RL and long agent trajectories need different training/inference coupling.
- [Preserve long-context ability with single-stage RL](../concepts/preserve-long-context-ability-with-single-stage-rl.md) - long-context post-training can regress when RL ramps through shorter context windows.
- [Use token-weighted loss for long coding outputs](../concepts/use-token-weighted-loss-for-long-coding-outputs.md) - token-averaged loss can reduce short-template reward seeking in varied-length coding outputs.
- [Keep visual inputs at native shape for GUI and video agents](../concepts/keep-visual-inputs-at-native-shape-for-gui-and-video-agents.md) - multimodal models need layout and temporal cues for screenshots, slides, video, and GUI action.
- [Turn real coding sessions into RL environments](../concepts/turn-real-coding-sessions-into-rl-environments.md) - real coding traces can become training environments when reconstructed and verified.
- [Interleave reasoning and tool calls for long-horizon agents](../concepts/interleave-reasoning-and-tool-calls-for-long-horizon-agents.md) - long-horizon model behavior needs repeated think-act-observe cycles in noisy tool environments.
- [Perturb agent scaffolds during training for generalization](../concepts/perturb-agent-scaffolds-during-training-for-generalization.md) - robust agent models should tolerate variation in tools, prompts, templates, environments, and responses.
- [Small agentic models make parallel workplace agents economical](../concepts/small-agentic-models-make-parallel-workplace-agents-economical.md) - small active-parameter models can make multi-copy agent workflows affordable.
- [Use verifiable rewards for language-model RL](../concepts/use-verifiable-rewards-for-language-model-rl.md) - automatic outcome checks can turn task success, format compliance, and action validity into training signals.
- [Specialize models against private benchmarks with RL](../concepts/specialize-models-against-private-benchmarks-with-rl.md) - enterprise RL should target measurable private workflows, not only public leaderboards.
- [Pipeline RL trades policy staleness for GPU throughput](../concepts/pipeline-rl-trades-policy-staleness-for-gpu-throughput.md) - async RL improves utilization only when the algorithm can tolerate stale-policy data.
- [Simulate RL run layouts before spending GPU budget](../concepts/simulate-rl-run-layouts-before-spending-gpu-budget.md) - GPU allocation, response lengths, KV-cache limits, and staleness should be modeled before expensive runs.
- [Use Agent RFT after baseline and task optimization](../concepts/use-agent-rft-after-baseline-and-task-optimization.md) - reinforcement fine-tuning should follow data matching, baselining, prompt optimization, and task/tool simplification.
- [Prefer model-portable agentic prompts before fine-tuning](../concepts/prefer-model-portable-agentic-prompts-before-fine-tuning.md) - provider-portable workflow improvements can be cheaper than repeated fine-tunes across model families.
- [Preserve rollout trajectory context for agent RFT grading](../concepts/preserve-rollout-trajectory-context-for-agent-rft-grading.md) - tool-calling training needs rollout IDs and trace context so graders can judge behavior, not only final text.
- [Design Agent RFT rewards for production match and anti-hacking](../concepts/design-agent-rft-rewards-for-production-match-and-anti-hacking.md) - reward functions should mirror production, provide learning signal, and block metric gaming.
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
- Which private workflow benchmarks have enough measurable ROI and repeated use to justify enterprise RL instead of prompting, RAG, or ordinary fine-tuning?
- How much policy staleness can a given language-model RL algorithm tolerate before asynchronous throughput gains stop improving useful learning?
- How should teams evaluate sparse MoE, effective on-device, and dense long-context models against the same agent workflow without hiding deployment cost differences?
- When should a team fine-tune an open model directly, start from a domain variant, or rely on a hosted API model for maximum raw capability?
- What evaluation suite is sufficient before promoting a weight-updated long-tail model over RAG or full-context prompting?
- When does adding reasoning effort improve model judgment, and when does it simply make accommodation of a bad premise longer?
- Which media-generation failures should be fixed through data curation, latent representation design, sampling settings, distillation, or explicit controls?
- How should media model training account for codec artifacts that are invisible to some users but visible to metrics or downstream models?
- Which non-language tasks should be handled by specialized frontier models instead of routed through a general LLM?
- Which quantization formats preserve enough quality while improving local model responsiveness for each hardware class?
- Which coding-eval time windows best separate memorized benchmark behavior from genuine current model capability?
- Which scaffold perturbations best predict whether a coding-agent model will transfer across real harnesses and tool APIs?
- Which model advances are blocked by research ideas versus the engineering systems needed to test and scale them?
- How can VLMs use high-fidelity vision-only features while preserving language alignment and real-time detection performance?
- Which interpretability-derived feature controls are stable enough across prompts, model versions, and deployment environments to use as production levers?

## Sources

- [#define AI Engineer - Greg Brockman, OpenAI (ft. Jensen Huang)](../sources/20250810_avWhreBUYF0.md)

- [Building an Agentic Platform - Ben Kus, CTO Box](../sources/20250824_12v5S1n1eOY.md)
- [Vision AI in 2025 - Peter Robicheaux, Roboflow](../sources/20250803_IQc05eCvNYE.md)
- [What Is a Humanoid Foundation Model? An Introduction to GR00T N1 - Annika & Aastha](../sources/20250728_mWKYvT9Lc50.md)
- [Why you should care about AI interpretability - Mark Bissell, Goodfire AI](../sources/20250727_6AVMHZPjpTQ.md)
- [Introduction to LLM serving with SGLang - Philip Kiely and Yineng Zhang, Baseten](../sources/20250726_Ahtaha9fEM0.md)

- [Build & deploy AI-powered apps - Paige Bailey, Google DeepMind](../sources/20260429_G_bHFmEAarM.md)
- [Compilers in the Age of LLMs - Yusuf Olokoba, Muna](../sources/20251124_q2nHsJVy4FE.md)
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
- [Perceptual Evaluations: Evals for Aesthetics - Diego Rodriguez, Krea.ai](../sources/20250823_h5ItAJuB3Fc.md)
- [Coding Evals: From Code Snippets to Codebases - Naman Jain, Cursor](../sources/20251215_tHN44yJoeS8.md)
- [Minimax M2: Building the #1 Open Model - Olive Song, MiniMax](../sources/20251213_lY1iFbDPRlw.md)
- [Hard Won Lessons from Building Effective AI Coding Agents - Nik Pash, Cline](../sources/20251212_I8fs4omN1no.md)
- [The 2025 AI Engineering Report - Barr Yaron, Amplify](../sources/20250801_mQ7_Zje7WKE.md)
- [Infrastructure for the Singularity - Jesse Han, Morph](../sources/20250801_2goSS66XRBk.md)
- [RL Environments at Scale - Will Brown, Prime Intellect](../sources/20251209__IzZWeuTx7I.md)
- [Efficient Reinforcement Learning - Rhythm Garg & Linden Li, Applied Compute](../sources/20251209_o15AaYl7Wu0.md)
- [Agent Reinforcement Fine Tuning - Will Hang & Cathy Zhou, OpenAI](../sources/20251209_p1CmPZ2j6Lk.md)
- [Building Cursor Composer - Lee Robinson, Cursor](../sources/20251202_fL1iJHtl51Q.md)
- [Z.ai GLM 4.6: What We Learned From 100 Million Open Source Downloads - Yuxuan Zhang, Z.ai](../sources/20251122_m6MF1OR_9kM.md)
