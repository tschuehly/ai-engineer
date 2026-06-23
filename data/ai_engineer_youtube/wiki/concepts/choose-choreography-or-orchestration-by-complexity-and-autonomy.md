# Choose choreography or orchestration by complexity and autonomy

Summary: Multi-agent coordination should be selected deliberately: choreography fits simple, event-driven, high-autonomy flows with strong observability, while orchestration fits complex, auditable, rollback-sensitive workflows.

Use when:
- Designing how multiple agents should coordinate work.
- Deciding whether agents should communicate through events or through a central workflow graph.

Details:
- Choreography lets agents publish and subscribe to events through a message bus. It is loosely coupled, scales agent addition well, and works when workflows are naturally event-driven and agents need to operate independently.
- Choreography becomes dangerous when event propagation cannot be traced: teams need to know whether an event was published, consumed, consumed twice, or lost.
- Orchestration uses a central coordinator to call agents, manage parallelism, hold the execution graph and state, handle retries, and log each step. Agents do not call each other directly.
- Regulated or high-impact workflows often favor orchestration because teams need to know exactly which agent acted, in what order, with what data, and how to roll back.
- A useful decision frame is workflow complexity versus autonomy requirement: simple/high-autonomy flows can use choreography; complex/low-autonomy-tolerance flows should use orchestration; complex/high-autonomy cases may need hybrid choreography with saga compensation.
- A production-playbook recap by the same speaker adds human-in-the-loop as a third coordination pattern alongside orchestrator-worker and choreography: when an agent crosses or falls below a confidence threshold, the workflow routes the case to a human to inspect and act before continuing. The same talk notes orchestration is unneeded for one agent but becomes important around five agents, where coordination complexity rises sharply. (`ObTPqBGsEbA`, 19:52-22:07)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Treat multi-agent systems as distributed systems](treat-multi-agent-systems-as-distributed-systems.md)
- [Wrap agent calls with circuit breakers and compensation](wrap-agent-calls-with-circuit-breakers-and-compensation.md)

Sources:
- [From Chaos to Choreography: Multi-Agent Orchestration Patterns That Actually Work - Sandipan Bhaumik](../sources/20260408_2czYyrTzILg.md), 05:29-11:12
- [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](../sources/20260618_ObTPqBGsEbA.md), 19:52-22:07
