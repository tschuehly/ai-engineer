# Treat multi-agent systems as distributed systems

Summary: Adding agents turns a single-agent feature into a distributed system with coordination, shared-state, failure propagation, and observability problems. Teams should debug multi-agent failures as architecture failures before blaming prompts or model quality.

Use when:
- A working single-agent prototype starts failing after more agents are added.
- Agent outputs depend on other agents, shared caches, shared databases, or partial workflow completion.

Details:
- A one-agent system can demo well with an LLM, prompts, retrieval, and tool calls, but adding agents creates dependencies where one agent produces data another needs, agents wait on each other, shared state changes underneath readers, and one crash can take down the workflow.
- Coordination complexity grows through pairwise relationships: five agents can create at least ten potential coordination paths, and each path can become a failure point, race condition, or state synchronization problem.
- In the credit-decisioning example, a credit-score agent wrote an updated score, but a downstream risk agent read stale cached data and produced incorrect risk ratings; the root problem was cache invalidation and architecture, not prompt quality.
- Multi-agent production work should include distributed-systems practices such as explicit coordination patterns, state lineage, handoff contracts, failure isolation, retries, and observability.

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Choose choreography or orchestration by complexity and autonomy](choose-choreography-or-orchestration-by-complexity-and-autonomy.md)
- [Use immutable versioned state for agent handoffs](use-immutable-versioned-state-for-agent-handoffs.md)
- [Wrap agent calls with circuit breakers and compensation](wrap-agent-calls-with-circuit-breakers-and-compensation.md)

Sources:
- [From Chaos to Choreography: Multi-Agent Orchestration Patterns That Actually Work - Sandipan Bhaumik](../sources/20260408_2czYyrTzILg.md), 01:32-05:28
