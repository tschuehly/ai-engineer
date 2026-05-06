# Local-First Platform Workflows Shorten Agent Feedback Loops

Summary: Agent-ready platforms should let agents validate work locally and fail early before pushing changes into slow remote pipelines.

Use when:
- Designing developer-platform workflows for coding agents that run on a local machine or isolated workspace.
- Reducing agent iteration time caused by delayed CI, deployment, or provisioning failures.

Details:
- The source notes that even when the model runs elsewhere, coding-agent work is often local to the developer's machine or agent workspace. (10:04-10:25)
- Platform workflows should shift left: if something will fail, it should fail as soon as possible instead of requiring a version-control push followed by a remote workflow failure minutes later. (10:29-10:44)
- If validation can run locally through APIs or wrappers around platform APIs, agents can loop faster and correct their own work before involving shared infrastructure. (10:44-11:14)
- Local-first loops still need precise task instructions and explicit success criteria so the agent knows when to stop iterating. (11:14-11:32)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent software factories need runnable, contextual, and verifiable primitives](agent-software-factories-need-runnable-contextual-and-verifiable-primitives.md)
- [Limit agent change size by feedback speed](limit-agent-change-size-by-feedback-speed.md)
- [Cloud agents turn coding work into asynchronous VM-backed queues](cloud-agents-turn-coding-work-into-asynchronous-vm-backed-queues.md)

Sources:
- [Platforms for Humans and Machines: Engineering for the Age of Agents - Juan Herreros Elorza](../sources/20260408_cCRO3ChaYhM.md), 10:04-11:32
