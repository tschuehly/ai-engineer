# Branchable Cloud Workspaces Make Agent Actions Reversible

Summary: Agent infrastructure can make exploratory software actions less brittle when full VM or container workspaces can be snapshotted, branched, replicated, moved, and rehydrated cheaply. This turns irreversible browser, shell, and environment mutations into branches that can be abandoned or promoted.

Use when:
- Designing cloud workspaces for agents that need to try risky or stateful actions.
- Choosing whether a workflow needs snapshots, branches, and replayable environment state rather than only logs.

Details:
- Han describes Infinibranch as virtualization, storage, and networking infrastructure for agents that need to interact with complex software environments at very low latency. 04:11-04:30
- The workflow premise is that browser navigation, clicks, and other computer-use actions are normally irreversible, while branchable snapshots let the agent backtrack or explore multiple possible paths. 04:48-05:52
- Morph Liquid Metal is presented as improving performance, latency, and storage efficiency, adding first-class container runtime support, millisecond branching, autoscale-to-zero, autoscale-to-infinity, and planned GPU support. 06:11-06:42
- Snapshot semantics are compared to Docker layer caching and "git for compute": side effects can mutate container state while chained workflows remain idempotent on top of snapshots. 08:25-08:48

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Cloud Agents Turn Coding Work Into Asynchronous VM-Backed Queues](cloud-agents-turn-coding-work-into-asynchronous-vm-backed-queues.md)
- [Treat agents as embodied action systems](treat-agents-as-embodied-action-systems.md)
- [Use immutable versioned state for agent handoffs](use-immutable-versioned-state-for-agent-handoffs.md)

Sources:
- [Infrastructure for the Singularity - Jesse Han, Morph](../sources/20250801_2goSS66XRBk.md), 04:11-08:48
