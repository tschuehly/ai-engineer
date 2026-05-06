# Let the Core Agent Loop Orchestrate Parallel Subtasks

Summary: Parallel coding agents should be orchestrated by the main agent loop when users cannot decompose work or resolve merge conflicts. The loop can decide subtasks on the fly, run testing or alternative trajectories in parallel, and shape work to reduce collisions.

Use when:
- Designing parallel coding-agent systems for non-technical or low-supervision users.
- Evaluating whether parallelism improves UX or only shifts decomposition and merge work onto the user.

Details:
- Parallelism trades extra compute for time and user experience rather than directly making a single agent more capable. 20:00-21:03
- Running many agents in parallel duplicates shared context across context windows, so compute cost rises even when subtasks share most of their background. 21:03-21:23
- Manual parallel-agent workflows leave users to decide task decomposition, dispatch threads, and reconcile outputs; for Replit's users, even the concept of merge conflicts is not an acceptable requirement. 21:23-23:13
- Useful parallelism includes running testing alongside code creation, injecting asynchronous observations into the main loop, and sampling multiple trajectories when budget permits. 22:03-22:39
- Replit's proposed direction is to make the core loop the orchestrator: it decomposes tasks on behalf of the user, chooses parallelism dynamically, and shapes subtasks to reduce merge-conflict risk. 23:14-24:16

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use parent agents to compare and merge parallel subagent outputs](use-parent-agents-to-compare-and-merge-parallel-subagent-outputs.md)
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)
- [Review bundles compress parallel agent output into evidence](review-bundles-compress-parallel-agent-output-into-evidence.md)

Sources:
- [The 3 Pillars of Autonomy - Michele Catasta, Replit](../sources/20251222_MLhAA9yguwM.md), 20:00-24:16
