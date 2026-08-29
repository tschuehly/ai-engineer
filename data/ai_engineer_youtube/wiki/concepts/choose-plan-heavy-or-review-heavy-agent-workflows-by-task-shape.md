# Choose Plan-Heavy or Review-Heavy Agent Workflows by Task Shape

Summary: Coding-agent workflow depth should match the work type. Upfront planning reduces review churn when a task can be specified and tested, while review-heavy iteration may be appropriate for stateful, visual, or exploratory work that is hard to fully specify.

Use when:
- Deciding how much detail to put into a coding-agent prompt or spec.
- Splitting work between human planning and human review.
- Choosing agent workflows for feature development, refactors, migrations, or maintenance.

Details:
- A plan-heavy workflow uses plan documents, spec frameworks, and repeated clarification so the agent has more task context, misses fewer edge cases, and needs fewer review rounds. (03:53-04:56)
- A review-heavy workflow starts with a lighter request and expects multiple correction rounds, which lowers upfront planning effort but can consume more human time in review. (05:02-05:33)
- The speaker's rule of thumb is that five minutes of planning can save thirty minutes of reviewing AI-generated code, especially when the task is specifiable. (07:09-07:26)
- Front-end feature development can favor interactive review because state, interactions, animations, styles, and functionality create many hard-to-specify details. Back-end feature work, refactors, migrations, and maintenance can often be more plan-heavy and test-driven. (06:02-07:09)
- **The plan-heavy end runs much further than the five-minutes-saves-thirty ratio suggests.** Blum reports spending a week writing a detailed plan and a second week aligning three other teams on it, then sending it to an agent overnight: "there are probably 20 PRs here. Some of them would be maybe 10 lines, and some of them would be 100 lines," self-estimated at six weeks of pre-AI work delivered in one, "if I include the review cycle at the end that we always have to remember." The ratio survives at that scale but the tradeoff changes character: not planning time against review time, but planning time against the risk that an unattended overnight run builds four phases on an unvalidated first one. Both figures are self-estimates against self-estimated baselines. ([Blum](../sources/20260828_5Bn0xro2ol8.md), 08:07-08:26, 11:00-11:45)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)
- [Evaluate context changes with lint, task scenarios, and probabilistic budgets](evaluate-context-changes-with-lint-task-scenarios-and-probabilistic-budgets.md)
- [Structure an Agent Plan With a Frozen Why and Reviewer-Sized Phases](structure-an-agent-plan-with-a-frozen-why-and-reviewer-sized-phases.md)

Sources:
- [Software Engineering Is Becoming Plan and Review - Louis Knight-Webb, Vibe Kanban](../sources/20260502_W76woOYHlvY.md), 03:53-07:26
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 08:07-08:26, 11:00-11:45
