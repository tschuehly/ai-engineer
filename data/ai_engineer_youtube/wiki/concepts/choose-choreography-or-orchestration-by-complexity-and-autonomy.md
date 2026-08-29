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
- **A case where the choice is made for you by who owns the systems.** In a GTM stack the tools already choreograph among themselves — "usually that CRM [and] sequencer are syncing independently of your orchestration system" — so an orchestrator added on top is not choosing between the two patterns; it is a central coordinator layered over pre-existing choreography it cannot observe or pause. That hybrid is what forces explicit readiness polling into the workflow, and it is a third configuration this page's two-way choice does not cover. ([Berry](../sources/20260826_UhCY231d0FQ.md), 08:18-08:55)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Treat multi-agent systems as distributed systems](treat-multi-agent-systems-as-distributed-systems.md)
- [Wrap agent calls with circuit breakers and compensation](wrap-agent-calls-with-circuit-breakers-and-compensation.md)
- [Wait for the Background Sync Before Acting on a Record You Just Created](wait-for-the-background-sync-before-acting-on-a-record-you-just-created.md)
- [Treat Tool-to-Tool Orchestration as a Data Engineering Problem](treat-tool-to-tool-orchestration-as-a-data-engineering-problem.md)
- [Build Orchestration From a Few General-Purpose Node Types](build-orchestration-from-a-few-general-purpose-node-types.md)

Sources:
- [From Chaos to Choreography: Multi-Agent Orchestration Patterns That Actually Work - Sandipan Bhaumik](../sources/20260408_2czYyrTzILg.md), 05:29-11:12
- [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](../sources/20260618_ObTPqBGsEbA.md), 19:52-22:07
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 08:18-08:55
