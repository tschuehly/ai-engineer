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
- **Checkpoints have to be per phase rather than per plan, or the later phases inherit unchecked assumptions.** "What I don't want to have is… five stages and then the first one is written but not validated, and then everything else is built on top of all the assumptions. So, having… a validation gate or an ex[it] criteria for each phase really helps and make[s] the plan resilient to drift." The failure is compounding rather than local: one unvalidated phase does not produce one bad phase, it produces every phase after it resting on something nobody checked — which is why a single review at the end of a multi-phase agent run is the wrong checkpoint even when the reviewer is thorough. ([Blum](../sources/20260828_5Bn0xro2ol8.md), 09:27-09:52)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Review research and plans before they multiply into code](review-research-and-plans-before-they-multiply-into-code.md)
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)
- [Translate structured requirements into property-based tests](translate-structured-requirements-into-property-based-tests.md)
- [Structure an Agent Plan With a Frozen Why and Reviewer-Sized Phases](structure-an-agent-plan-with-a-frozen-why-and-reviewer-sized-phases.md)

Sources:
- [Backlog.md: Terminal Kanban Board for Managing Tasks with AI Agents - Alex Gavrilescu, Funstage](../sources/20251124_zMXKhhwiCIc.md), 04:04-05:08, 07:36-08:49, 12:08-12:48
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 09:27-09:52
