# Use immutable versioned state for agent handoffs

Summary: Agent handoffs are safer when each step receives a sealed state snapshot, validates the input contract, and appends a new state version instead of mutating shared records.

Use when:
- Agents pass intermediate outputs, customer data, recommendations, or research between workflow steps.
- A system has stale reads, lost updates, or hard-to-reproduce shared-state bugs.

Details:
- Shared mutable state lets multiple agents read and write the same database records concurrently, which can cause stale reads, lost updates, and last-write-wins behavior unless transactions, isolation levels, and locks are used correctly.
- Immutable state snapshots create an append-only lineage: each agent receives one version, validates it, produces a new version, and never updates the prior version.
- State snapshots should include a version number, payload, and creator metadata, with each handoff validating schema and data-contract expectations before the next agent runs.
- The append-only history supports rollback and debugging: operators can trace or binary-search state evolution to find where bad output first entered the workflow.
- Data contracts should be enforced at agent boundaries, for example rejecting low-confidence or malformed research output before it reaches downstream analysis and report generation.

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Treat multi-agent systems as distributed systems](treat-multi-agent-systems-as-distributed-systems.md)
- [Choose choreography or orchestration by complexity and autonomy](choose-choreography-or-orchestration-by-complexity-and-autonomy.md)

Sources:
- [From Chaos to Choreography: Multi-Agent Orchestration Patterns That Actually Work - Sandipan Bhaumik](../sources/20260408_2czYyrTzILg.md), 11:24-16:24
