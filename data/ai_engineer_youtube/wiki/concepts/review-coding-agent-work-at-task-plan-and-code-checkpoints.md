# Review coding-agent work at task, plan, and code checkpoints

Summary: Coding-agent review has more leverage when it happens before implementation as well as after it. A practical workflow reviews the created task, the implementation plan, and the final code so wrong intent or direction is caught before it expands into a diff.

Use when:
- Designing review gates for coding-agent task execution.
- Deciding where humans should inspect agent work before code is generated.
- Recovering from agents that implement plausible but wrong requirements.

Details:
- The first review checkpoint is after task creation: the human checks the description and acceptance criteria to confirm the agent understood intent. (04:04-04:35, 12:15-12:29)
- The second checkpoint is the implementation plan: after the agent reads documentation and existing code, a senior engineer can inspect architecture, steps, target files, and direction before implementation starts. (04:38-05:08, 07:36-08:12, 12:29-12:36)
- The final checkpoint is code review against the task's acceptance criteria and definition of done. (08:21-08:49, 12:36-12:41)
- The transcript presents acceptance criteria as testable and easily verifiable so unit tests and review can check the intended behavior rather than merely whether the agent produced code. (04:04-04:22, 12:08-12:20)
- Multiple tasks can run in parallel using Git worktrees when they have no dependencies, but this assumes the task and plan checkpoints have made the independent work boundaries explicit. (12:41-12:48)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Review research and plans before they multiply into code](review-research-and-plans-before-they-multiply-into-code.md)
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)
- [Translate structured requirements into property-based tests](translate-structured-requirements-into-property-based-tests.md)

Sources:
- [Backlog.md: Terminal Kanban Board for Managing Tasks with AI Agents - Alex Gavrilescu, Funstage](../sources/20251124_zMXKhhwiCIc.md), 04:04-05:08, 07:36-08:49, 12:08-12:48
