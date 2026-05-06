# Tools

## Overview

Agent tools are most useful when their execution surface is paired with clear context about when and how to use them. MCP can expose service-backed integrations and remote actions, while skills can package the workflow guidance, domain instructions, references, and scripts that help an agent choose and use those integrations correctly. Visual automation tools can expose service nodes such as Gmail or calendar actions directly as agent tools, but the tool names and descriptions become part of the prompt surface and need the same care as any other instruction. Voice agents are another place where tool restraint matters: a realtime conversational agent should start with a small tool surface and delegate complex work through specialist handoffs that preserve conversation state. Some workflows should bypass LLM judgment entirely: deterministic scripts, explicit approval gates, and subworkflows are a better fit for known conditional actions, while the LLM handles judgment-heavy interpretation and connection-making. On edge devices, guidance must be especially compact: a skill registry can expose short descriptions first, then load full instructions, JavaScript, native intents, or API calls only when needed. Context packages can also be distributed through libraries and registries, which makes tool guidance reusable across projects but requires evaluation, provenance, dependency management, and context filtering before installation. A context engine can be exposed through MCP, CLI, API, dashboard, or messaging surfaces; the tool surface is the access path, while the engine still needs source relationships, personalization, permissions, and conflict handling behind it. Product teams should also treat APIs, CLIs, and MCP servers as first-class user interfaces when agents or bots are the callers; dashboards alone are insufficient for agent experience.

## Key Concepts

- [Use skills for workflow guidance and MCP for integrations](../concepts/use-skills-for-workflow-guidance-and-mcp-for-integrations.md) - separates the integration layer from the contextual guidance layer.
- [Context engines select task-specific organizational context](../concepts/context-engines-select-task-specific-organizational-context.md) - a tool surface alone does not make a context engine useful.
- [Edge agent skills need progressive disclosure to preserve small-model reliability](../concepts/edge-agent-skills-need-progressive-disclosure-to-preserve-small-model-reliability.md) - small local models need tool context to be discoverable without all details being preloaded.
- [Constrained decoding makes small-model tool calls production-usable](../concepts/constrained-decoding-makes-small-model-tool-calls-production-usable.md) - tool runtimes can improve small-model reliability by constraining calls to valid tools.
- [Package reusable context as skills, libraries, and registries](../concepts/package-reusable-context-as-skills-libraries-and-registries.md) - tool guidance can be shared as installable context packages.
- [Filter untrusted context before it reaches the agent](../concepts/filter-untrusted-context-before-it-reaches-the-agent.md) - tool and skill ecosystems need controls for unsafe context before execution sandboxes apply.
- [Ambient agents need self-maintenance and memory hygiene](../concepts/ambient-agents-need-self-maintenance-and-memory-hygiene.md) - operational jobs and deterministic scripts keep always-on agent systems reliable.
- [Personal knowledge bases become agent context substrates](../concepts/personal-knowledge-bases-become-agent-context-substrates.md) - note search, memory, tagging, and link ingestion are tool surfaces for personal context.
- [Visual agent workflows make tool use observable and adjustable](../concepts/visual-agent-workflows-make-tool-use-observable-and-adjustable.md) - visual nodes expose the trigger, memory, model, tool, and approval surfaces behind an agent.
- [Route high-impact agent actions through explicit human approval gates](../concepts/route-high-impact-agent-actions-through-explicit-human-approval-gates.md) - approval steps keep sensitive tool execution outside model-only control.
- [Use tool names and descriptions as operational prompts](../concepts/use-tool-names-and-descriptions-as-operational-prompts.md) - clear tool metadata improves selection and enables local tool-specific guidance.
- [Split large automation surfaces into specialized subagents and subworkflows](../concepts/split-large-automation-surfaces-into-specialized-subagents-and-subworkflows.md) - subworkflows and specialist agents keep large tool surfaces manageable.
- [Delegate complex voice-agent tasks through specialist tools and handoffs](../concepts/delegate-complex-voice-agent-tasks-through-specialist-tools-and-handoffs.md) - voice systems should route harder tool or policy decisions to specialists while preserving context.
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](../concepts/agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md) - agent-facing products need machine-friendly control surfaces, not only human dashboards.

## Open Questions

- When should a workflow be encoded as an MCP tool description, a skill, a local script, or a combination of these?
- What telemetry is needed to decide that a skill or tool is unused, stale, or actively harmful?
- When should a context engine expose the same capability through MCP, CLI, API, or a messaging integration?
- What security checks should run before a registry skill or context package is loaded by an agent?
- Which agent operations should be implemented as deterministic scripts rather than LLM tool calls?
- How should tool descriptions be tested when they act as prompts for high-risk actions?
- How small should a realtime voice agent's tool surface be before handoff delegation becomes necessary?
- How should product teams test APIs, CLIs, and MCP servers as user interfaces for agents rather than just integrations for humans?

## Sources

- [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](../sources/20260504_GmAQKINjv1E.md)
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md)
- [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM - Cormac Brick, Google](../sources/20260503_BKWpYIWvAo4.md)
- [Context Is the New Code - Patrick Debois, Tessl](../sources/20260503_bSG9wUYaHWU.md)
- [I Gave an AI Agent the Keys to My Life (Here's What Happened) - Radek Sienkiewicz (@velvetshark-com)](../sources/20260502_sJ2jc7leKBk.md)
- [Human-in-the-Loop Automation with n8n - Liam McGarrigle](../sources/20260502_tDArkCqjA-c.md)
- [Building Effective Voice Agents - Toki Sherbakov + Anoop Kotha, OpenAI](../sources/20250720_-OXiljTJxQU.md)
- [Agents for Everything Else - swyx](../sources/20260501_zepu8Kk6FBQ.md)
