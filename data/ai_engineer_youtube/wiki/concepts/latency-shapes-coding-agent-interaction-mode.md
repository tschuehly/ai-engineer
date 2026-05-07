# Latency Shapes Coding-Agent Interaction Mode

Summary: Coding-agent latency is not only an infrastructure metric; it changes whether the human experiences the agent as a synchronous collaborator, a background delegate, or an awkward interruption-prone middle state.

Use when:
- Choosing between fast foreground coding models and slower long-running background agents.
- Evaluating whether a coding-agent product keeps developers in flow or forces context switching.

Details:
- Cursor Composer was built to be both smart and fast because early fast prototypes were liked for speed but were not reliable enough as daily coding drivers. 01:22-01:55
- A fast foreground agent can keep the developer in flow while it reads files, runs commands, edits files, and manages todos, rather than making the developer wait for a long background job. 02:31-03:16
- Robinson describes a "semi async valley" where 10-20 minute runs are slow enough to break synchronous work but not long-running or powerful enough to feel like a true background delegate. 12:26-13:08
- A practical workflow can route planning to a strongest frontier model, then route implementation to a faster specialized model when the plan is ready. 13:20-13:36

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Inference](../topics/inference.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)

Sources:
- [Building Cursor Composer - Lee Robinson, Cursor](../sources/20251202_fL1iJHtl51Q.md), 01:22-03:16, 12:26-13:36
