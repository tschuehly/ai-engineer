# Plugin Architectures Let Agent Systems Absorb Experiments

Summary: Agent systems that move volatile capabilities into plugins or extensions can absorb experiments without forcing every idea into core. This is especially useful for memory, wiki, dreaming, and other agent-substrate features whose right shape is still emerging.

Use when:
- Refactoring a fast-moving agent project from a monolith into extension points.
- Letting users or contributors test memory, retrieval, or automation ideas without growing core complexity.

Details:
- Steinberger says OpenClaw moved from a spaghetti codebase toward an architecture where capabilities are extensions or plugins, 39:51-40:00.
- The extension model lets users replace memory, add a wiki, add dreaming, or install other experiments without sending everything through overloaded core pull requests, 39:51-40:20.
- Dreaming is described as a session-log and memory-reconciliation direction: review logs, garbage-collect, promote some memories to longer-term storage, and drop others, 38:33-39:31.
- The plugin model supports an open-source "try stuff" culture where experimental agent capabilities can evolve outside the main product path, 39:31-40:20.

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Ambient agents need self-maintenance and memory hygiene](ambient-agents-need-self-maintenance-and-memory-hygiene.md)
- [Package reusable context as skills, libraries, and registries](package-reusable-context-as-skills-libraries-and-registries.md)

Sources:
- [State of the Claw - Peter Steinberger](../sources/20260417_zgNvts_2TUE.md), 38:33-40:20
