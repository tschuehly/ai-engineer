# AI Engineer YouTube Topical Wiki

This wiki is compiled from local AI Engineer YouTube transcripts. Start with a topic, follow concept links for source-backed detail, and use source notes when you need the original video context.

## Current Emphasis

- [Context development lifecycle treats context as an engineered artifact](concepts/context-development-lifecycle-treats-context-as-an-engineered-artifact.md) - context should move through generate, evaluate, distribute, observe, and adapt loops.
- [Route high-impact agent actions through explicit human approval gates](concepts/route-high-impact-agent-actions-through-explicit-human-approval-gates.md) - sensitive automations should pause at review boundaries the model cannot bypass.
- [Use hybrid AI pricing to balance predictable revenue and margin protection](concepts/use-hybrid-ai-pricing-to-balance-predictable-revenue-and-margin-protection.md) - AI products often need base fees plus scaling fees because pure subscription and pure usage models each fail under AI cost dynamics.
- [Grow personal-agent permissions incrementally from recurring pain](concepts/grow-personal-agent-permissions-incrementally-from-recurring-pain.md) - high-access personal agents should earn autonomy through small reversible workflows.
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
- [Discover large API tool surfaces progressively](concepts/discover-large-api-tool-surfaces-progressively.md) - broad API surfaces should be discovered on demand instead of eagerly loading every endpoint as MCP context.
- [Run agent-written API code inside programmable sandboxes](concepts/run-agent-written-api-code-inside-programmable-sandboxes.md) - code-mode tools need isolation, network controls, secret boundaries, and rate limits.
- [Compare models by task, thinking budget, cost, and latency](concepts/compare-models-by-task-thinking-budget-cost-and-latency.md) - model routing should account for task fit, reasoning depth, speed, and cost instead of defaulting to the largest model.
- [Route Gemma 4 model variants by deployment and workflow shape](concepts/route-gemma-4-model-variants-by-deployment-and-workflow-shape.md) - Gemma 4's effective, MoE, and dense variants map to different local, hosted, reasoning, coding, and agentic workloads.
- [Treat edge models as their own architecture class](concepts/treat-edge-models-as-their-own-architecture-class.md) - edge-scale models need memory, latency, architecture, and post-training choices that differ from scaled-down large-model defaults.
- [Per-layer embeddings move effective-model capacity out of VRAM](concepts/per-layer-embeddings-move-effective-model-capacity-out-of-vram.md) - Gemma 4 effective models use PLE to add representational capacity while reducing on-device VRAM pressure.
- [Customize subagents by task, model, tools, and permissions](concepts/customize-subagents-by-task-model-tools-and-permissions.md) - subagents should be scoped to their role instead of inheriting unnecessary authority.
- [Align teams before agents implement](concepts/align-teams-before-agents-implement.md) - fast coding agents make shared direction the scarce resource.
- [Shared cloud workspaces make agent sessions collaborative](concepts/shared-cloud-workspaces-make-agent-sessions-collaborative.md) - cloud-backed sessions let teammates and agents share prompts, code, terminals, previews, and PR context.
- [Spatial agent maps expose filesystem-level lineage and collisions](concepts/spatial-agent-maps-expose-filesystem-level-lineage-and-collisions.md) - parallel agent work becomes easier to supervise when file activity, changelists, and likely collisions are visible.

## Topics

- [Agents](topics/agents.md) - agent workflows that combine reasoning, tools, APIs, and local state.
- [AI Monetization](topics/ai-monetization.md) - pricing, charge metrics, billing guardrails, and monetization infrastructure for AI products.
- [Coding Agents](topics/coding-agents.md) - coding-agent loops, tickets, validation, and feedback-driven prompt or skill improvement.
- [Context Engineering](topics/context-engineering.md) - engineering prompts, skills, memory, retrieval, and documentation into reusable task context.
- [Edge Inference](topics/edge-inference.md) - on-device inference decisions, model sizing, deployment, and fleet validation.
- [Evaluation](topics/evaluation.md) - task-level validation of models, tools, retrieval, and agent workflows.
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
