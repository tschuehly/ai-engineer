# AI Engineer YouTube Topical Wiki

This wiki is compiled from local AI Engineer YouTube transcripts. Start with a topic, follow concept links for source-backed detail, and use source notes when you need the original video context.

## Current Emphasis

- [Context development lifecycle treats context as an engineered artifact](concepts/context-development-lifecycle-treats-context-as-an-engineered-artifact.md) - context should move through generate, evaluate, distribute, observe, and adapt loops.
- [Route high-impact agent actions through explicit human approval gates](concepts/route-high-impact-agent-actions-through-explicit-human-approval-gates.md) - sensitive automations should pause at review boundaries the model cannot bypass.
- [Use hybrid AI pricing to balance predictable revenue and margin protection](concepts/use-hybrid-ai-pricing-to-balance-predictable-revenue-and-margin-protection.md) - AI products often need base fees plus scaling fees because pure subscription and pure usage models each fail under AI cost dynamics.
- [Grow personal-agent permissions incrementally from recurring pain](concepts/grow-personal-agent-permissions-incrementally-from-recurring-pain.md) - high-access personal agents should earn autonomy through small reversible workflows.
- [Purpose-built agent workspaces make orchestration visible](concepts/purpose-built-agent-workspaces-make-orchestration-visible.md) - personal-agent UIs should expose topics, tool calls, scheduled messages, active agents, and capabilities instead of hiding orchestration in generic chat.
- [Explicit context attachments can outperform opaque agent memory](concepts/explicit-context-attachments-can-outperform-opaque-agent-memory.md) - nested topic descriptions and selected documents, skills, and knowledge bases make personal-agent context inspectable.
- [Choose plan-heavy or review-heavy agent workflows by task shape](concepts/choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md) - coding-agent workflow depth should match the task's specifiability and review needs.
- [Evaluate context changes with lint, task scenarios, and probabilistic budgets](concepts/evaluate-context-changes-with-lint-task-scenarios-and-probabilistic-budgets.md) - context updates need validation because instruction changes can alter downstream agent behavior.
- [Use tool names and descriptions as operational prompts](concepts/use-tool-names-and-descriptions-as-operational-prompts.md) - tool metadata shapes tool selection and should be tuned like prompt context.
- [Non-technical collaborators can steer agents with natural work artifacts](concepts/non-technical-collaborators-can-steer-agents-with-natural-work-artifacts.md) - agents can extend operational workflows when collaborators can prompt with Figma pages, redlines, notes, screenshots, and emails.
- [Canvas-native agents turn spatial work surfaces into prompt context](concepts/canvas-native-agents-turn-spatial-work-surfaces-into-prompt-context.md) - whiteboards and design canvases can become agent interfaces when drawings, annotations, selections, and generated artifacts are readable context.
- [Prompt-coded product behavior reduces code but weakens hard guarantees](concepts/prompt-coded-product-behavior-reduces-code-but-weakens-hard-guarantees.md) - advanced agent workflows can move into skill-like prompts, but runtime guarantees may become model-compliance problems.
- [Server-side interaction state simplifies branching conversational agents](concepts/server-side-interaction-state-simplifies-branching-conversational-agents.md) - interaction IDs can simplify continuation, retrieval, and branching without making context unlimited.
- [Realtime multimodal agents use stateful streams for audio, vision, and tools](concepts/realtime-multimodal-agents-use-stateful-streams-for-audio-vision-and-tools.md) - live agents can combine audio, screen frames, transcriptions, and tools in one stateful session.
- [Evaluate voice agents with traces, transcripts, audio checks, and simulations](concepts/evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md) - voice systems need both transcript-level task checks and audio-specific validation for tone, pacing, and guardrail timing.
- [Replay production failures before promoting prompt fixes](concepts/replay-production-failures-before-promoting-prompt-fixes.md) - prompt changes should be validated against the triggering trace and the broader regression suite before release.
- [Connect production observability to offline eval loops](concepts/connect-production-observability-to-offline-eval-loops.md) - production traces should reveal failure modes and become replayable offline regression examples.
- [Fresh Markdown context mitigates model rot in codegen](concepts/fresh-markdown-context-mitigates-model-rot-in-codegen.md) - productized coding agents need current docs when model training snapshots lag fast-moving APIs.
- [Agent software factories need runnable, contextual, and verifiable primitives](concepts/agent-software-factories-need-runnable-contextual-and-verifiable-primitives.md) - parallel coding agents need navigable repositories, runnable environments, accessible context, and self-checking paths.
- [Cloud agents turn coding work into asynchronous VM-backed queues](concepts/cloud-agents-turn-coding-work-into-asynchronous-vm-backed-queues.md) - humans can plan synchronously and dispatch isolated background execution when review handoffs and setup are controlled.
- [Cross-app access centralizes MCP authentication through the identity provider](concepts/cross-app-access-centralizes-mcp-authentication-through-the-identity-provider.md) - enterprise MCP clients and servers can share SSO-backed trust instead of repeating per-tool consent.
- [MCP gateways create an enterprise root of trust](concepts/mcp-gateways-create-an-enterprise-root-of-trust.md) - gateway infrastructure centralizes MCP auth, authorization, observability, secure connectivity, routing, and deployment controls.
- [MCP tool surfaces need default context budgets](concepts/mcp-tool-surfaces-need-default-context-budgets.md) - production MCP servers need defaults, outputs, and discovery paths that keep broad tool catalogs from overwhelming agents.
- [Agent connectivity stack combines skills, MCP, CLIs, and computer use](concepts/agent-connectivity-stack-combines-skills-mcp-clis-and-computer-use.md) - production agents should choose the right connectivity surface for local execution, remote semantics, governance, and domain guidance.
- [Discover large API tool surfaces progressively](concepts/discover-large-api-tool-surfaces-progressively.md) - broad API surfaces should be discovered on demand instead of eagerly loading every endpoint as MCP context.
- [Run agent-written API code inside programmable sandboxes](concepts/run-agent-written-api-code-inside-programmable-sandboxes.md) - code-mode tools need isolation, network controls, secret boundaries, and rate limits.
- [MCP applications ship UI and tools together](concepts/mcp-applications-ship-ui-and-tools-together.md) - an MCP server can provide both a human-rendered interface and model-callable tools when clients support richer protocol semantics.
- [Capability-based sandboxes start with no authority](concepts/capability-based-sandboxes-start-with-no-authority.md) - code-mode runtimes should grant explicit task-scoped APIs and network access rather than broad ambient authority.
- [Compare models by task, thinking budget, cost, and latency](concepts/compare-models-by-task-thinking-budget-cost-and-latency.md) - model routing should account for task fit, reasoning depth, speed, and cost instead of defaulting to the largest model.
- [Train image and video diffusion models in learned latent spaces](concepts/train-image-and-video-diffusion-models-in-learned-latent-spaces.md) - learned autoencoder latents make high-resolution and video diffusion tractable while preserving useful media topology.
- [Use guidance to trade diffusion sample diversity for conditional quality](concepts/use-guidance-to-trade-diffusion-sample-diversity-for-conditional-quality.md) - diffusion sampling settings can improve conditional adherence and perceived quality at the cost of diversity and artifact risk.
- [Evaluate whether models reject impossible or nonsensical premises](concepts/evaluate-whether-models-reject-impossible-or-nonsensical-premises.md) - reliable models and agents should stop or reframe invalid requests instead of confidently accommodating them.
- [Track user dissatisfaction alongside pairwise model preference](concepts/track-user-dissatisfaction-alongside-pairwise-model-preference.md) - "both bad" feedback reveals absolute model failure rates that leaderboards can hide.
- [Route Gemma 4 model variants by deployment and workflow shape](concepts/route-gemma-4-model-variants-by-deployment-and-workflow-shape.md) - Gemma 4's effective, MoE, and dense variants map to different local, hosted, reasoning, coding, and agentic workloads.
- [Open model families need ecosystem-compatible tooling](concepts/open-model-families-need-ecosystem-compatible-tooling.md) - open-weight adoption depends on licensing, runtimes, fine-tuning tools, and community integrations, not only base-model capability.
- [Use MLX Swift LM for Apple local model integration](concepts/use-mlx-swift-lm-for-apple-local-model-integration.md) - Apple-device local inference can be integrated through native MLX runtimes and curated Hugging Face model IDs.
- [Treat edge models as their own architecture class](concepts/treat-edge-models-as-their-own-architecture-class.md) - edge-scale models need memory, latency, architecture, and post-training choices that differ from scaled-down large-model defaults.
- [Per-layer embeddings move effective-model capacity out of VRAM](concepts/per-layer-embeddings-move-effective-model-capacity-out-of-vram.md) - Gemma 4 effective models use PLE to add representational capacity while reducing on-device VRAM pressure.
- [Customize subagents by task, model, tools, and permissions](concepts/customize-subagents-by-task-model-tools-and-permissions.md) - subagents should be scoped to their role instead of inheriting unnecessary authority.
- [Align teams before agents implement](concepts/align-teams-before-agents-implement.md) - fast coding agents make shared direction the scarce resource.
- [Shared cloud workspaces make agent sessions collaborative](concepts/shared-cloud-workspaces-make-agent-sessions-collaborative.md) - cloud-backed sessions let teammates and agents share prompts, code, terminals, previews, and PR context.
- [Spatial agent maps expose filesystem-level lineage and collisions](concepts/spatial-agent-maps-expose-filesystem-level-lineage-and-collisions.md) - parallel agent work becomes easier to supervise when file activity, changelists, and likely collisions are visible.
- [Use PRDs to align agents on the design concept](concepts/use-prds-to-align-agents-on-the-design-concept.md) - planning artifacts should capture shared intent, implementation decisions, and testing decisions before agent coding.
- [Limit agent change size by feedback speed](concepts/limit-agent-change-size-by-feedback-speed.md) - generated code volume should stay inside the available test, type-check, and review loop.
- [Use deep modules to make agent work testable](concepts/use-deep-modules-to-make-agent-work-testable.md) - simple module interfaces help humans validate agent-written internals from outside.
- [Retire completed planning docs before they become agent doc rot](concepts/retire-completed-planning-docs-before-they-become-agent-doc-rot.md) - historical PRDs can mislead agents after code and requirements diverge.
- [Collaborate with complex agents through high-bandwidth artifacts](concepts/collaborate-with-complex-agents-through-high-bandwidth-artifacts.md) - vertical agents often need documents, tables, comments, and review primitives as their main collaboration surface.
- [Use decision logs to keep uncertain agents moving](concepts/use-decision-logs-to-keep-uncertain-agents-moving.md) - reversible assumptions can preserve progress while keeping human review targeted.
- [Do not use token volume as a developer productivity metric](concepts/do-not-use-token-volume-as-a-developer-productivity-metric.md) - token spend and leaderboard metrics can push engineers toward visible usage instead of useful work.
- [AI-amplified shipping speed needs stronger product taste](concepts/ai-amplified-shipping-speed-needs-stronger-product-taste.md) - when implementation gets cheap, product teams need stronger discipline about what not to ship.
- [Zero-bug policies turn bug inflow into immediate work](concepts/zero-bug-policies-turn-bug-inflow-into-immediate-work.md) - AI-assisted bug routing works best when reports become immediate triage instead of passive backlog.
- [Build internal AI engineering platforms when off-the-shelf tools lack enterprise context](concepts/build-internal-ai-engineering-platforms-when-off-the-shelf-tools-lack-enterprise-context.md) - large organizations may need monorepo, service-discovery, review, and on-call integration around agents.
- [Choose autonomy level by task uncertainty and control needs](concepts/choose-autonomy-level-by-task-uncertainty-and-control-needs.md) - many requested agents should remain workflows when the steps are knowable and control matters.
- [Compressed research agents preserve human decision points](concepts/compressed-research-agents-preserve-human-decision-points.md) - agents can accelerate repeated research without changing the final decision owner.
- [Calibrate LLM judges like binary classifiers](concepts/calibrate-llm-judges-like-binary-classifiers.md) - judge prompts need domain labels, dev/test splits, and precision/recall-aware validation before they gate quality.
- [AI output speed can overwhelm review capacity](concepts/ai-output-speed-can-overwhelm-review-capacity.md) - generated-code volume should be constrained by responsible review, not only by agent throughput.
- [Agent-legible codebases reduce generated-code entropy](concepts/agent-legible-codebases-reduce-generated-code-entropy.md) - modular flow, explicit primitives, and lint-enforced rules make codebases easier for agents to modify safely.
- [Use human judgment gates for high-risk agent code changes](concepts/use-human-judgment-gates-for-high-risk-agent-code-changes.md) - migrations, permissions, dependencies, architecture, and reliability work need explicit human review friction.

## Topics

- [Agents](topics/agents.md) - agent workflows that combine reasoning, tools, APIs, and local state.
- [AI Monetization](topics/ai-monetization.md) - pricing, charge metrics, billing guardrails, and monetization infrastructure for AI products.
- [Coding Agents](topics/coding-agents.md) - coding-agent loops, tickets, validation, and feedback-driven prompt or skill improvement.
- [Context Engineering](topics/context-engineering.md) - engineering prompts, skills, memory, retrieval, and documentation into reusable task context.
- [Edge Inference](topics/edge-inference.md) - on-device inference decisions, model sizing, deployment, and fleet validation.
- [Evaluation](topics/evaluation.md) - task-level validation of models, tools, retrieval, and agent workflows.
- [Generative Media](topics/generative-media.md) - image and video generation models, latent representations, diffusion sampling, distillation, and controls.
- [Inference](topics/inference.md) - production serving patterns for model runtimes, batching, routing, autoscaling, and resource use.
- [Infrastructure](topics/infrastructure.md) - deployment runtimes, conversion paths, compilation choices, and operational validation.
- [Models](topics/models.md) - model architecture, tokenizer, training, adaptation, and sizing choices under practical constraints.
- [Retrieval](topics/retrieval.md) - bringing accurate, task-relevant knowledge from enterprise systems and curated context blocks into agent work.
- [Tools](topics/tools.md) - MCP integrations, scripts, skills, and tool-use guidance for agent workflows.
- [Voice Agents](topics/voice-agents.md) - realtime audio-agent architecture, tool delegation, persona prompting, and voice-specific evaluation.
- [Workflows](topics/workflows.md) - repeatable loops for agent execution, failure discovery, and context improvement.

## Indexes

- [Concept Index](indexes/concept-index.md)
- [Processed Sources](indexes/processed-sources.md)
- [Activity Log](log.md)
