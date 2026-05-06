# Agents

## Overview

Agent workflows depend on both model capability and the context substrate around the model. On-device agents can keep core inference local while invoking selected tools, APIs, and structured outputs; enterprise agents also need institutional knowledge that is accurate enough to move real work through delivery systems. Context engines can supply that knowledge by selecting task-specific organizational context, resolving or surfacing conflicts, and using team or expert signals to personalize what the agent sees. Small models can sit in front of the main agent as retrieval, extraction, classification, or reranking tools that reduce context rot. For coding work, simple loops can give agents enough structure to process one ticket at a time while avoiding the coordination failure modes of large multi-agent plans. Skills add another packaging layer: they can expose product-specific workflow guidance through progressive disclosure while leaving service integrations to tools such as MCP.

## Key Concepts

- [On-device agents can combine local reasoning with tool and API calls](../concepts/on-device-agents-can-combine-local-reasoning-with-tool-and-api-calls.md) - local inference can still support function calling, JSON output, and selected API-backed skills.
- [Enterprise agent failures often expose missing institutional knowledge](../concepts/enterprise-agent-failures-expose-missing-institutional-knowledge.md) - task failures can reveal missing enterprise knowledge rather than insufficient model capability.
- [Use small models as context-management tools before agent reasoning](../concepts/use-small-models-as-context-management-tools-before-agent-reasoning.md) - narrow models can filter, classify, retrieve, or extract context before the main agent reasons.
- [Ralph loops process one ticket at a time with fresh context](../concepts/ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md) - coding agents can be constrained to one work item, one validation cycle, and a clean handoff.
- [Use independent validation contexts to reduce agent confirmation bias](../concepts/use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md) - separate review contexts can catch failures the producing agent rationalizes away.
- [Agent skills package progressive-disclosure context for repeatable workflows](../concepts/agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md) - skills can make domain workflows available without loading all instructions upfront.
- [Use skills for workflow guidance and MCP for integrations](../concepts/use-skills-for-workflow-guidance-and-mcp-for-integrations.md) - agents often need both a reliable tool surface and context that explains how to use it.
- [Evaluate agent skills with task scenarios and comparative conditions](../concepts/evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md) - skill usefulness should be measured against real task behavior.
- [Context engines select task-specific organizational context](../concepts/context-engines-select-task-specific-organizational-context.md) - agents need the right organizational context before they can produce code that fits the system.
- [Use social and expert graphs to personalize coding-agent context](../concepts/use-social-and-expert-graphs-to-personalize-coding-agent-context.md) - agent context can be shaped by who owns, reviews, and works near the relevant code.

## Open Questions

- Which classes of tool calls are reliable enough for small on-device models without cloud fallback?
- How should agents distinguish missing institutional knowledge from ambiguous task instructions?
- When is a small-model preprocessing step worth its latency and operational complexity compared with giving the main agent more raw context?
- How much autonomy should coding agents receive before independent validation and permission boundaries become mandatory?
- Which product workflows should become reusable skills rather than prompt snippets, documentation pages, or MCP tool descriptions?
- When should a coding agent ask a context engine for more organizational context instead of exploring the repository itself?

## Sources

- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md)
- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md)
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
- [Ralph Loops: Build Dumb AI Loops That Ship - Chris Parsons, Cherrypick](../sources/20260504_2TLXsxkz0zI.md)
- [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](../sources/20260504_GmAQKINjv1E.md)
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md)
