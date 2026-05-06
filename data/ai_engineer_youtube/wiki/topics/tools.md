# Tools

## Overview

Agent tools are most useful when their execution surface is paired with clear context about when and how to use them. MCP can expose service-backed integrations and remote actions, while skills can package the workflow guidance, domain instructions, references, and scripts that help an agent choose and use those integrations correctly. A context engine can be exposed through MCP, CLI, API, dashboard, or messaging surfaces; the tool surface is the access path, while the engine still needs source relationships, personalization, permissions, and conflict handling behind it.

## Key Concepts

- [Use skills for workflow guidance and MCP for integrations](../concepts/use-skills-for-workflow-guidance-and-mcp-for-integrations.md) - separates the integration layer from the contextual guidance layer.
- [Context engines select task-specific organizational context](../concepts/context-engines-select-task-specific-organizational-context.md) - a tool surface alone does not make a context engine useful.

## Open Questions

- When should a workflow be encoded as an MCP tool description, a skill, a local script, or a combination of these?
- What telemetry is needed to decide that a skill or tool is unused, stale, or actively harmful?
- When should a context engine expose the same capability through MCP, CLI, API, or a messaging integration?

## Sources

- [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](../sources/20260504_GmAQKINjv1E.md)
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md)
