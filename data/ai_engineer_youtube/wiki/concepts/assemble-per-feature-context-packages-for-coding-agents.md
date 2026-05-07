# Assemble Per-Feature Context Packages for Coding Agents

Summary: Once planning artifacts exist, each coding-agent run should receive a curated context package for the current atomic feature rather than the full planning corpus. The goal is enough specification, dependency, validation, and implementation-plan context for autonomous work without wasting the context window.

Use when:
- Initializing a coding-agent session from a planning document or implementation plan.
- Preventing broad planning artifacts from overwhelming a model with irrelevant context.

Details:
- Gallon frames implementation as a tight loop repeated for each atomic feature, where planning artifacts guide the transformation of specifications into working, tested software (38:30-38:50).
- Context assembly transforms planning artifacts into a curated package that enables one autonomous feature implementation session (39:49-40:05).
- The context package should include only implementation-plan sections relevant to the current atomic feature, the feature specification, referenced dependencies, and validation guidance (40:50-41:05).
- Dumping entire planning documents into an agent session wastes context on irrelevant information, can still omit critical context, causes unnecessary back-and-forth, and leaves validation gaps (40:05-40:46).
- The implementation context should be assembled from source planning artifacts rather than improvised in chat, preserving traceability from the current feature back to the broader plan (21:04-21:21, 39:49-41:05).

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [Frequent intentional compaction keeps coding agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md)
- [Offload long-horizon agent state outside the context window](offload-long-horizon-agent-state-outside-the-context-window.md)

Sources:
- [The Cure for the Vibe Coding Hangover - Corey J. Gallon, Rexmore](../sources/20251124_JsKTQbT58BY.md), 38:30-41:05
