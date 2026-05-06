# From Chaos to Choreography: Multi-Agent Orchestration Patterns That Actually Work - Sandipan Bhaumik

Source: [From Chaos to Choreography: Multi-Agent Orchestration Patterns That Actually Work - Sandipan Bhaumik](https://www.youtube.com/watch?v=2czYyrTzILg)
Uploaded: 2026-04-08
Transcript: `raw/20260408_2czYyrTzILg/2czYyrTzILg.en-orig.vtt`

## Summary

Sandipan Bhaumik frames multi-agent production systems as distributed systems: adding agents creates coordination, state, observability, and recovery problems that are not solved by better prompts alone. The talk recommends choosing choreography or orchestration by workflow complexity and autonomy needs, using immutable versioned state and data contracts at handoffs, and applying circuit breakers plus saga-style compensation so agent failures do not collapse the full workflow.

## Extracted Concepts

- [Treat multi-agent systems as distributed systems](../concepts/treat-multi-agent-systems-as-distributed-systems.md) - this source explains why coordination complexity, stale data, and race conditions appear when teams scale from one agent to many.
- [Choose choreography or orchestration by complexity and autonomy](../concepts/choose-choreography-or-orchestration-by-complexity-and-autonomy.md) - this source gives a decision frame for event-driven agent choreography versus central workflow orchestration.
- [Use immutable versioned state for agent handoffs](../concepts/use-immutable-versioned-state-for-agent-handoffs.md) - this source recommends append-only state snapshots, schema validation, and data contracts to avoid shared mutable state failures.
- [Wrap agent calls with circuit breakers and compensation](../concepts/wrap-agent-calls-with-circuit-breakers-and-compensation.md) - this source applies circuit breaker and saga patterns to multi-agent failure recovery.

## Topic Links

- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

## Notes

- Scaling from one agent to five agents creates dependency, shared-state, and crash-propagation problems; the speaker calls this a distributed-system problem rather than an AI or prompt problem (01:32-02:26).
- In a credit decisioning example, a risk agent read stale cached customer data after a score update, causing incorrect risk ratings and approvals; the root cause was cache invalidation and architecture, not the model (02:31-04:30).
- Choreography coordinates agents through events on a message bus, supports loose coupling and frequent agent addition, but requires strong event observability and delivery guarantees because debugging failures is otherwise difficult (05:55-08:16).
- Orchestration centralizes the workflow graph, state, retries, logging, and parallelism; the speaker recommends it for complex dependencies, rollback, regulated workflows, and stable flows where traceability matters more than autonomy (08:21-10:16).
- The state-management recommendation is immutable append-only snapshots with versions, schema validation, and creator metadata; each agent receives a sealed input state and produces a new version rather than mutating shared records (11:24-15:18).
- Data contracts should validate handoffs at agent boundaries, including fields such as findings, confidence, sources, and timestamps, so low-quality or malformed output is rejected immediately rather than several agents downstream (15:20-16:24).
- Circuit breakers should track failure counts and open/half-open/closed state around agent calls so repeated timeouts, crashes, or rate limits fail fast and prevent cascading workflow failure (16:36-18:58).
- Saga-style compensation gives each agent an execute and compensate method so an orchestrator can walk backward through successful steps and undo partial work after a later failure (19:02-20:56).
