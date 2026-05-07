# Cloud Agents Turn Coding Work Into Asynchronous VM-Backed Queues

Summary: Cloud coding agents let humans plan synchronously, then hand execution to isolated background environments that can run in parallel. This increases throughput only when context, setup, cost, and review handoffs are managed.

Use when:
- Designing parallel coding-agent execution beyond a local single-agent session.
- Choosing between local agent runs, cloud VMs, and queue-based coding workflows.

Details:
- Cloud agents are described as running on separate VMs with their own development environment, allowing multiple tasks to proceed in parallel without requiring the human to keep the local workspace active (15:26-17:24).
- A practical workflow is to plan synchronously, write or refine a spec, dispatch execution asynchronously, and later review the finished cloud-agent output (01:01:30-01:02:14).
- VM-backed execution depends on the same factory primitives as local work: agents need runnable setup, accessible context, and enough environment capability to start the project and run checks (09:00-09:24, 15:26-21:52).
- The talk notes cost and wrong-context risks around cloud agents; spawning them in the wrong repo or without the right setup wastes work, and cloud agents can be expensive enough to require intentional routing (01:11:27-01:11:29, 01:21:03-01:21:47).
- Cursor's cloud-agent VMs also illustrate a training-infrastructure reuse pattern: secure sandboxes that load user code, run tools, and edit files can double as production-matched RL environments for coding models. 08:31-09:05

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)
- [Isolate parallel coding work with project worktrees](isolate-parallel-coding-work-with-project-worktrees.md)
- [Use parent agents to compare and merge parallel subagent outputs](use-parent-agents-to-compare-and-merge-parallel-subagent-outputs.md)
- [Production-Matched RL Environments Train Coding Agents on Real Tool Surfaces](production-matched-rl-environments-train-coding-agents-on-real-tool-surfaces.md)

Sources:
- [Building your own software factory — Eric Zakariasson, Cursor](../sources/20260428_rnDm57Py54A.md), 15:26-21:52, 01:01:30-01:02:14
- [Building Cursor Composer - Lee Robinson, Cursor](../sources/20251202_fL1iJHtl51Q.md), 08:31-09:05
