# Agents

## Overview

Agent workflows depend on both model capability and the context substrate around the model. On-device agents can keep core inference local while invoking selected tools, APIs, and structured outputs; because small edge models are context-sensitive, tool and skill systems should expose compact descriptions first and load details only when needed. Voice agents add realtime audio constraints: architecture choice, latency, spoken persona, interruption behavior, and audio-specific evaluation matter alongside ordinary model, instruction, tool, and runtime design. Personal agents need the same restraint at a permission level: broad access to email, files, calendars, operating-system automation, and memory should grow from small reversible workflows rather than from an immediate all-access launch. Visual workflow builders add another control layer by making triggers, model calls, memory, tools, approval waits, and execution state inspectable and adjustable. Enterprise agents also need institutional knowledge that is accurate enough to move real work through delivery systems. Context engines can supply that knowledge by selecting task-specific organizational context, resolving or surfacing conflicts, and using team or expert signals to personalize what the agent sees. Small models can sit in front of the main agent as retrieval, extraction, classification, or reranking tools that reduce context rot. For coding work, simple loops can give agents enough structure to process one ticket at a time while avoiding the coordination failure modes of large multi-agent plans. As agents take on longer implementation runs, human leverage shifts toward planning, review, QA, and change shepherding, so agent interfaces need to preserve focus across multiple streams rather than constantly interrupting the developer. Always-on agents add an operational layer: indexing, backups, update checks, memory hygiene, and cleanup keep the agent substrate reliable while scripts handle deterministic cases that do not need LLM judgment. Skills add another packaging layer: they can expose product-specific workflow guidance through progressive disclosure while leaving service integrations to tools such as MCP. As context becomes packageable, agents also need filters and provenance checks because unsafe instructions may be loaded before execution sandboxes can constrain behavior.

## Key Concepts

- [On-device agents can combine local reasoning with tool and API calls](../concepts/on-device-agents-can-combine-local-reasoning-with-tool-and-api-calls.md) - local inference can still support function calling, JSON output, and selected API-backed skills.
- [Enterprise agent failures often expose missing institutional knowledge](../concepts/enterprise-agent-failures-expose-missing-institutional-knowledge.md) - task failures can reveal missing enterprise knowledge rather than insufficient model capability.
- [Use small models as context-management tools before agent reasoning](../concepts/use-small-models-as-context-management-tools-before-agent-reasoning.md) - narrow models can filter, classify, retrieve, or extract context before the main agent reasons.
- [Ralph loops process one ticket at a time with fresh context](../concepts/ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md) - coding agents can be constrained to one work item, one validation cycle, and a clean handoff.
- [Use independent validation contexts to reduce agent confirmation bias](../concepts/use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md) - separate review contexts can catch failures the producing agent rationalizes away.
- [Coding agents shift engineering work toward planning and review](../concepts/coding-agents-shift-engineering-work-toward-planning-and-review.md) - code generation moves human leverage toward task definition, QA, review, and deployment follow-through.
- [Parallel coding-agent queues need focus-preserving review interfaces](../concepts/parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md) - longer agent runs need interfaces that batch human attention around completed work.
- [Agent skills package progressive-disclosure context for repeatable workflows](../concepts/agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md) - skills can make domain workflows available without loading all instructions upfront.
- [Use skills for workflow guidance and MCP for integrations](../concepts/use-skills-for-workflow-guidance-and-mcp-for-integrations.md) - agents often need both a reliable tool surface and context that explains how to use it.
- [Evaluate agent skills with task scenarios and comparative conditions](../concepts/evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md) - skill usefulness should be measured against real task behavior.
- [Context engines select task-specific organizational context](../concepts/context-engines-select-task-specific-organizational-context.md) - agents need the right organizational context before they can produce code that fits the system.
- [Use social and expert graphs to personalize coding-agent context](../concepts/use-social-and-expert-graphs-to-personalize-coding-agent-context.md) - agent context can be shaped by who owns, reviews, and works near the relevant code.
- [Edge agent skills need progressive disclosure to preserve small-model reliability](../concepts/edge-agent-skills-need-progressive-disclosure-to-preserve-small-model-reliability.md) - on-device agents need compressed skill context to keep small-model tool use reliable.
- [Constrained decoding makes small-model tool calls production-usable](../concepts/constrained-decoding-makes-small-model-tool-calls-production-usable.md) - runtime constraints can make local function calling less dependent on open-ended generation.
- [Filter untrusted context before it reaches the agent](../concepts/filter-untrusted-context-before-it-reaches-the-agent.md) - agents need context-layer security in addition to execution sandboxes.
- [Grow personal-agent permissions incrementally from recurring pain](../concepts/grow-personal-agent-permissions-incrementally-from-recurring-pain.md) - personal-agent autonomy should expand through small trusted workflows with rollback paths.
- [Ambient agents need self-maintenance and memory hygiene](../concepts/ambient-agents-need-self-maintenance-and-memory-hygiene.md) - always-on agents need indexing, backups, update checks, memory cleanup, and guardrails.
- [Visual agent workflows make tool use observable and adjustable](../concepts/visual-agent-workflows-make-tool-use-observable-and-adjustable.md) - explicit workflow nodes make agent behavior easier to inspect, debug, and tune.
- [Route high-impact agent actions through explicit human approval gates](../concepts/route-high-impact-agent-actions-through-explicit-human-approval-gates.md) - sensitive actions should pause for review that the model cannot bypass.
- [Use tool names and descriptions as operational prompts](../concepts/use-tool-names-and-descriptions-as-operational-prompts.md) - tool metadata is prompt context that shapes tool selection.
- [Split large automation surfaces into specialized subagents and subworkflows](../concepts/split-large-automation-surfaces-into-specialized-subagents-and-subworkflows.md) - broad automation domains can be decomposed into routed specialists.
- [Choose voice-agent architecture by latency, accuracy, and semantics](../concepts/choose-voice-agent-architecture-by-latency-accuracy-and-semantics.md) - voice agents need architecture choices that account for audio latency and semantic loss.
- [Delegate complex voice-agent tasks through specialist tools and handoffs](../concepts/delegate-complex-voice-agent-tasks-through-specialist-tools-and-handoffs.md) - realtime voice agents can stay responsive by delegating harder work to specialist tools or agents.

## Open Questions

- Which classes of tool calls are reliable enough for small on-device models without cloud fallback?
- How should agents distinguish missing institutional knowledge from ambiguous task instructions?
- When is a small-model preprocessing step worth its latency and operational complexity compared with giving the main agent more raw context?
- How much autonomy should coding agents receive before independent validation and permission boundaries become mandatory?
- How should agent tools balance parallelism against the human cost of switching between unfinished work streams?
- Which product workflows should become reusable skills rather than prompt snippets, documentation pages, or MCP tool descriptions?
- When should a coding agent ask a context engine for more organizational context instead of exploring the repository itself?
- Which context sources should be trusted enough to auto-load, and which should require filtering, provenance checks, or user approval?
- Which personal-agent permissions should require explicit review even after adjacent workflows have become reliable?
- Which workflow events should be captured for auditability when an agent waits for or resumes after human approval?
- Which voice-agent actions should run in the realtime conversational layer, and which should be delegated to slower specialist agents?

## Sources

- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md)
- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md)
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
- [Ralph Loops: Build Dumb AI Loops That Ship - Chris Parsons, Cherrypick](../sources/20260504_2TLXsxkz0zI.md)
- [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](../sources/20260504_GmAQKINjv1E.md)
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md)
- [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM - Cormac Brick, Google](../sources/20260503_BKWpYIWvAo4.md)
- [Context Is the New Code - Patrick Debois, Tessl](../sources/20260503_bSG9wUYaHWU.md)
- [Software Engineering Is Becoming Plan and Review - Louis Knight-Webb, Vibe Kanban](../sources/20260502_W76woOYHlvY.md)
- [I Gave an AI Agent the Keys to My Life (Here's What Happened) - Radek Sienkiewicz (@velvetshark-com)](../sources/20260502_sJ2jc7leKBk.md)
- [Human-in-the-Loop Automation with n8n - Liam McGarrigle](../sources/20260502_tDArkCqjA-c.md)
- [Building Effective Voice Agents - Toki Sherbakov + Anoop Kotha, OpenAI](../sources/20250720_-OXiljTJxQU.md)
