# Control Long-Running Workflow Agents Through Run Lifecycle Operations

Summary: Long-running agent workflows need explicit run lifecycle controls: scheduling, child workflow launches, deterministic stream naming, cancellation, and version-aware deployment behavior. These controls keep recurring or waiting agents governable after they leave a single request/response loop.

Use when:
- Designing recurring, scheduled, or human-waiting agent workflows.
- Planning operational controls for workflow runs that may outlive a single deployment or user session.

Details:
- Scheduling workflows can launch agent workflows, and workflows can start other workflows; a recurring agent can sleep, call the agent, then choose the stream it writes to, 55:29-55:55.
- Stream names can be made deterministic so each recurring run has a predictable stream for clients to reconnect to, 55:59-56:13.
- Long waits can be canceled from the observability UI, API, or CLI; workflows can also race a sleep against a human approval so a human click wakes the run earlier than the timer, 56:17-57:02.
- Deployment versioning matters for in-flight runs: every deployment can be treated as a version, and operators may need to upgrade, cancel, or rerun existing workflow runs when code changes, 61:51-64:07.

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Treat long waits as logical workflow state](treat-long-waits-as-logical-workflow-state.md)
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Cloud agents turn coding work into asynchronous VM-backed queues](cloud-agents-turn-coding-work-into-asynchronous-vm-backed-queues.md)

Sources:
- [Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel](../sources/20260106_kmV-qg4uoNI.md), 55:29-57:02, 61:51-64:07
