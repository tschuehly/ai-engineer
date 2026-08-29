# Fractured Attention Becomes Usable With Delegated Agents

Summary: Delegated coding agents can make short gaps between meetings useful for investigation, planning, and patch preparation. This lets technical managers contribute code when they still have enough judgment to review the result.

Use when:
- Designing coding-agent workflows for managers, staff engineers, or interrupted operators.
- Explaining why asynchronous agent delegation changes the value of small attention windows.

Details:
- The source argues that managers can commit code when they have enough technical judgment because agents can perform investigation and patch preparation while the manager is doing other work. (15:08-16:15)
- Instead of needing a three- or four-hour focus block, a user can leave a meeting, ask an agent to investigate a bug, then return to a plan, root cause, or candidate fix. (15:39-16:03)
- The same pattern supports parallel agent panes where engineers productively run multiple agent tasks at once, though the talk acknowledges this can be done badly as performative multitasking. (06:11-06:49)
- **The same reclamation at a larger unit of time, and the review constraint that still binds it.** Krieger's version is a weekend rather than a gap between meetings: a "dynamic workflow setup" ported a few hundred thousand lines of Python to TypeScript, verifying and churning unattended, and he "came back Monday to a completed workflow." The limit this page names still applies at that scale and gets worse — he explicitly does not review every line of what returns, and the binding constraint becomes whether he can conceptualize the result at all. Delegating into otherwise-dead time buys throughput, not comprehension. ([Krieger](../sources/20260827_qqrk7CtkuIw.md), 04:52-05:14, 10:19-11:20)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Cloud agents turn coding work into asynchronous VM-backed queues](cloud-agents-turn-coding-work-into-asynchronous-vm-backed-queues.md)
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)
- [Treat Human Attention as the Bottleneck for Agentic Work](treat-human-attention-as-the-agentic-bottleneck.md)
- [The Review Bottleneck Is Comprehension, Not Reviewer Time](the-review-bottleneck-is-comprehension-not-reviewer-time.md)

Sources:
- [Dispatch from the Future: building an AI-native Company - Dan Shipper, Every, AI & I](../sources/20251218_MGzymaYBiss.md), 06:11-06:49, 15:08-16:15
- [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 04:52-05:14, 10:19-11:20
