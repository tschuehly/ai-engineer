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

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)
- [Evaluate context changes with lint, task scenarios, and probabilistic budgets](evaluate-context-changes-with-lint-task-scenarios-and-probabilistic-budgets.md)

Sources:
- [Software Engineering Is Becoming Plan and Review - Louis Knight-Webb, Vibe Kanban](../sources/20260502_W76woOYHlvY.md), 03:53-07:26
