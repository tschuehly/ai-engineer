# Coding Agents

## Overview

Coding agents work best when their autonomy is constrained by small work items, visible checks, and explicit handoff rules. The Ralph loop pattern favors a simple repeated cycle over elaborate orchestration: pick one ticket, implement it, validate it, update status, and let the next run continue with the improved prompt, skill, or work queue. This reduces the coordination burden that appears when many agents attempt a large dependency graph at once. As agents write more of the implementation, human effort shifts toward planning, reviewing, QA, and shepherding changes. The right balance depends on task shape: specifiable back-end, refactor, migration, and maintenance work can be plan-heavy and test-driven, while exploratory front-end work may require tighter review loops. Context engines add another reliability layer by giving the agent system-specific decisions, reviewers, owners, and expert signals before it spends tokens rediscovering them from the repository.

## Key Concepts

- [Ralph loops process one ticket at a time with fresh context](../concepts/ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md) - simple repeated ticket execution can ship more reliably than broad multi-agent plans.
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](../concepts/feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md) - review outputs, tests, and generated critiques become inputs to the next run.
- [Use independent validation contexts to reduce agent confirmation bias](../concepts/use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md) - separate validation contexts can catch defects the producing agent misses.
- [Coding agents shift engineering work toward planning and review](../concepts/coding-agents-shift-engineering-work-toward-planning-and-review.md) - agent-written code increases the importance of task definition, review, QA, and change shepherding.
- [Choose plan-heavy or review-heavy agent workflows by task shape](../concepts/choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md) - task type should determine whether humans invest more in upfront specification or iterative review.
- [Parallel coding-agent queues need focus-preserving review interfaces](../concepts/parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md) - long-running agent work benefits from queueing, diffs, previews, and focused review handoffs.
- [Use social and expert graphs to personalize coding-agent context](../concepts/use-social-and-expert-graphs-to-personalize-coding-agent-context.md) - reviewer and ownership graphs can tell agents whose conventions and decisions matter for a change.
- [Context engines select task-specific organizational context](../concepts/context-engines-select-task-specific-organizational-context.md) - context engines reduce irrelevant exploration before a coding task.

## Open Questions

- What ticket sizes and dependency patterns are small enough for unattended coding-agent loops?
- Which validation responsibilities should stay in deterministic tests versus independent review agents?
- What repository activity signals are reliable enough to infer code ownership or expertise for agent context?
- Which front-end QA capabilities are strong enough to move visual and interaction review out of human back-and-forth?

## Sources

- [Ralph Loops: Build Dumb AI Loops That Ship - Chris Parsons, Cherrypick](../sources/20260504_2TLXsxkz0zI.md)
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md)
- [Software Engineering Is Becoming Plan and Review - Louis Knight-Webb, Vibe Kanban](../sources/20260502_W76woOYHlvY.md)
