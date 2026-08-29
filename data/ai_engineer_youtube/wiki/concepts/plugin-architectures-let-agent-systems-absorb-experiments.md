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
- **What it costs when the architecture does not absorb new primitives, priced as a share of capacity.** Izmit's team runs "60-70% of the work… adding new features, improving quality" against "30-40% of the work is that we are constantly re-architecting with the new technology," and reports that 80% of the current architecture does not match the original PRD after adding CI/CD, eval infrastructure, a skill library, MCP orchestration, progressive disclosure, memory, and scheduling post-launch. That is the number a plugin boundary is trying to buy down. His conclusion is not to design harder up front but to stop over-investing in any architecture — "you should be okay to pivot very easily" — which is the same bet from the other side: absorb experiments by keeping the cost of replacement low rather than by anticipating the extension points. ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 12:35-13:40, 17:33-17:57)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Ambient agents need self-maintenance and memory hygiene](ambient-agents-need-self-maintenance-and-memory-hygiene.md)
- [Package reusable context as skills, libraries, and registries](package-reusable-context-as-skills-libraries-and-registries.md)
- [Budget a Third of Sprint Capacity for Re-Architecture](budget-a-third-of-sprint-capacity-for-re-architecture.md)

Sources:
- [State of the Claw - Peter Steinberger](../sources/20260417_zgNvts_2TUE.md), 38:33-40:20
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 12:35-13:40, 17:33-17:57
