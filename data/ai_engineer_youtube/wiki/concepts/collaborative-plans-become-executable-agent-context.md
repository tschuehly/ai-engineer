# Collaborative Plans Become Executable Agent Context

Summary: Agent-written plans become more reliable when teammates can inspect and edit them together before execution. The plan and surrounding discussion then become shared prompt context for the agent instead of a private local plan hidden in one developer's terminal.

Use when:
- Designing plan-mode workflows for coding agents.
- Preventing private agent plans from bypassing team review.

Details:
- The talk criticizes local plan modes that are unshared with the team, because teams may never evaluate whether an agent's plan is good before it is implemented. 04:24-04:38
- ACE demonstrates an agent-written plan that teammates open together, edit collaboratively, and evaluate against their intent before asking the agent to implement it. 12:18-13:07
- Teammates can revise requirements and interface choices inside the plan, and the agent can use the edited plan plus session conversation as execution context. 12:39-13:07
- The workflow treats planning and building as a cycle rather than separate phases, keeping alignment alongside implementation instead of after it. 05:38-05:57

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Coding agents shift engineering work toward planning and review](coding-agents-shift-engineering-work-toward-planning-and-review.md)
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)
- [Context engines select task-specific organizational context](context-engines-select-task-specific-organizational-context.md)

Sources:
- [Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment - Maggie Appleton, GitHub](../sources/20260426_ClWD8OEYgp8.md), 04:24-05:57, 12:18-13:07
