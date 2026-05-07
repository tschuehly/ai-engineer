# Start Coding Agents With Small Verifiable Chores

Summary: Coding-agent adoption should begin with small, low-risk tasks that have a clear definition of done and cheap verification. As users build intuition for the agent's strengths and failure modes, they can expand task size without turning every run into an unreviewable experiment.

Use when:
- Introducing autonomous coding agents to a team or repository.
- Choosing whether a task is ready for agent delegation.
- Looking for low-risk agent work that still improves the codebase.

Details:
- Strong starter tasks fit in a single commit and let the agent or reviewer tell whether the work is complete through passing tests, resolved merge conflicts, or similarly explicit completion signals. (07:31-07:54)
- Brennan recommends beginning with rote chores such as fixing lint errors, resolving merge conflicts, or repairing a single failing test because they are bounded and usually easy for a human to verify. (07:57-08:12)
- Database migrations, failing-test cleanup after an API change, and test coverage expansion are presented as practical examples when the expected best practices and validation path are clear. (14:48-15:45)
- The caveat is that production-facing greenfield apps should not be merged through vibe-coded output alone; low-stakes internal apps can tolerate more rapid experimentation than customer-facing production systems. (15:47-16:28)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Limit Agent Change Size by Feedback Speed](limit-agent-change-size-by-feedback-speed.md)
- [Review coding-agent work at task, plan, and code checkpoints](review-coding-agent-work-at-task-plan-and-code-checkpoints.md)
- [Keep critical code inside human understanding and review capacity](keep-critical-code-inside-human-understanding-and-review-capacity.md)

Sources:
- [Software Development Agents: What Works and What Doesn't - Robert Brennan, OpenHands](../sources/20250725_o_hhkJtlbSs.md), 07:31-08:12, 14:48-16:28
