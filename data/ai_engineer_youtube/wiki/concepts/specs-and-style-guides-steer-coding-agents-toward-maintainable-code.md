# Specs and Style Guides Steer Coding Agents Toward Maintainable Code

Summary: Specs, docs, and strict style guides are coding-agent context, not optional process overhead. They prevent mistakes by making intent, constraints, and preferred implementation patterns visible before code is generated.

Use when:
- Preparing a codebase or agent environment for maintainable generated changes.
- Encoding architecture, product, or style expectations as reusable agent context.

Details:
- A plan-first coding workflow can force the agent to propose a plan before implementation, then switch to an implementation prompt after the plan is accepted (05:15-06:05).
- Agents do not automatically know the Slack, email, or planning context behind a codebase, so specs and docs need to be first-class workflow inputs rather than separate artifacts humans remember manually (06:08-06:43).
- Sculptor is described as detecting when docs and code are out of sync and when specs conflict, so the agent can see stale or contradictory intent before it codes against the wrong source (06:43-07:10).
- Style guides can be tailored to agent failure modes; Albrecht gives the example of preferring immutable data patterns to reduce race-condition risk (07:12-08:00).

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use repository instructions to ground coding agents](use-repository-instructions-to-ground-coding-agents.md)
- [Model-shaped codebase architecture for coding agents](model-shaped-codebase-architecture-for-coding-agents.md)
- [Treat prompts as distributed harness surfaces](treat-prompts-as-distributed-harness-surfaces.md)

Sources:
- [Beyond the Prototype: Using AI to Write High-Quality Code - Josh Albrecht, Imbue](../sources/20250725_x_1EumTaXeE.md), 05:15-08:00
