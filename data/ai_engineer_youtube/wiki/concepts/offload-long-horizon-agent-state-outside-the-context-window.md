# Offload Long-Horizon Agent State Outside the Context Window

Summary: Long-horizon agents do not need to keep every state detail in the model context window. They can preserve coherence by writing state into code, documentation, plans, task lists, file-system memory, and scoped subagents that return compact results.

Use when:
- Designing agents that must run for long trajectories without relying on extremely large context windows.
- Deciding what state belongs in files, plans, task lists, memory stores, or specialist subagents.

Details:
- Replit's talk argues that long context models are not required for coherent long trajectories; even ambitious tasks can often fit inside roughly 200K tokens when context is managed deliberately. 15:13-15:49
- The codebase itself can maintain state through documentation written while new code is created. 15:52-16:08
- Plans, task lists, and memories can be persisted on the file system and reloaded when relevant rather than continuously included in the active prompt. 16:08-16:35
- Subagents provide separation of concerns: each starts from fresh context, receives only the subset needed for its task, runs to completion, and returns compact results to the main loop. 17:00-17:41
- Replit reported fewer context recompressions after moving work into subagent orchestration because less context pollution stayed in the main loop. 17:41-18:16

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Use subagents to isolate context-heavy subtasks](use-subagents-to-isolate-context-heavy-subtasks.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [Do not treat long context as durable model memory](do-not-treat-long-context-as-durable-model-memory.md)

Sources:
- [The 3 Pillars of Autonomy - Michele Catasta, Replit](../sources/20251222_MLhAA9yguwM.md), 15:13-18:16

