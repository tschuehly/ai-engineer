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
- [Evaluate voice agents with traces, transcripts, audio checks, and simulations](concepts/evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md) - voice systems need both transcript-level task checks and audio-specific validation for tone, pacing, and guardrail timing.

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
