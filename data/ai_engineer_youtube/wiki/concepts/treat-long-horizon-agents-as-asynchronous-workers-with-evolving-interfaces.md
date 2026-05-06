# Treat long-horizon agents as asynchronous workers with evolving interfaces

Summary: As agent tasks stretch from minutes to hours and eventually days, interfaces should treat agents as asynchronous workers whose progress, diffs, tests, and handoffs need visible control surfaces rather than assuming a synchronous chat loop.

Use when:
- Designing UX for coding or knowledge-work agents that may run longer than a human wants to watch.
- Choosing between IDE, web, local agent, queue, and status surfaces for long-running agent work.

Details:
- Poolside describes the demoed VS Code assistant as one interface into its platform and says other interfaces include web and downloadable local agents for adopters. (08:20-08:35)
- The speakers say current agents already run tasks for hours and expect future agents to run tasks for days, making asynchronous operation and changing form factors central interface concerns. (10:30-10:47)
- The demo's live diff pane, generated test commands, Bash test scripts, summaries, and manual reruns are concrete progress and verification surfaces for work that would be hard to supervise through final chat output alone. (03:27-07:59)
- This supports designing agent products around resumable task state, inspectable artifacts, and reviewable execution traces as model capability lengthens the work horizon.

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Treat agent APIs as asynchronous task lifecycles](treat-agent-apis-as-asynchronous-task-lifecycles.md)
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)
- [Use durable execution for production agent loops](use-durable-execution-for-production-agent-loops.md)

Sources:
- [AGI: The Path Forward - Jason Warner & Eiso Kant, Poolside](../sources/20251227_OGCG_QkCcZo.md), 03:27-07:59, 08:20-08:35, 10:30-10:47
