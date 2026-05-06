# Treat Long Waits as Logical Workflow State

Summary: Long-running agent workflows should model waits as logical durable state rather than keeping a physical process alive. This is especially important for human-in-the-loop flows where a response may arrive hours, days, or weeks later.

Use when:
- Building agent approval, clarification, or review workflows that pause for human input.
- Designing infrastructure for agent runs that include long waits, parallel branches, or resumable handoffs.

Details:
- Human-in-the-loop agent workflows often need to wait far longer than a live process should be pinned; Temporal lets the developer code the wait while the worker can remove inactive state from memory and later reconstitute it when input arrives, 58:24-60:02.
- Temporal workflows can express ordinary code patterns such as parallel branches, awaits, long waits, and loops while preserving the workflow as durable execution state, 61:35-62:19.
- The talk presents OpenAI Agents SDK orchestration as many small agents with independent loops that can be orchestrated together; durable workflows provide a place to coordinate those loops and non-agent steps like human input, 60:37-61:40.

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Use immutable versioned state for agent handoffs](use-immutable-versioned-state-for-agent-handoffs.md)
- [Choose choreography or orchestration by complexity and autonomy](choose-choreography-or-orchestration-by-complexity-and-autonomy.md)

Sources:
- [OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal](../sources/20260112_k8cnVCMYmNc.md), 58:24-62:19
