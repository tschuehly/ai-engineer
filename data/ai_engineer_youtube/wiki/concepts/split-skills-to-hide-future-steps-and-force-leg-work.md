# Split skills to hide future steps and force more leg work per step

Summary: An agent under-invests in an early step when it can see the ultimate goal, so splitting a multi-step skill into separate skills that each expose only the current step forces the agent to do more "leg work" on that step instead of rushing toward a visible finish line.

Use when:
- A skill's exploratory or clarifying step (ask questions, explore the codebase) is being rushed.
- You want to deepen one phase of a workflow without rewriting the instructions to be more insistent.

Details:
- The failure mode: on a step like "ask clarifying questions" or "explore the codebase," the agent just doesn't put in enough effort. 14:56-15:25
- Root cause via plan mode: plan mode has two steps — ask clarifying questions, then create a plan. In every implementation Matt Pocock has tried, the clarifying-questions step is rushed because the agent sees its ultimate goal is to create the plan, so it asks a couple of things and eagerly produces the plan. 15:25-16:05
- Fix: split the phases into separate skills so the agent sees only one step at a time. His `grill with docs` skill *is* the clarifying-questions phase as its own skill; only after it completes does the separate `to PRD` skill run. The agent sees step one, finishes it, and only then sees step two. 16:05-16:40
- Why it works: hiding the future goal removes the agent's incentive to shortcut the current step, so it does an extra chunk of leg work exactly where you want depth — "there's no technique like it," though it's not always necessary. 16:40-16:47
- This is the inverse pressure to progressive disclosure's token savings: here you deliberately split a workflow across skills to change *behavior* (more effort per phase), not just to shrink `SKILL.md`.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Steer agents with leading words that surface in reasoning traces](steer-agents-with-leading-words-that-surface-in-reasoning-traces.md)
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Use subagents to isolate context-heavy subtasks](use-subagents-to-isolate-context-heavy-subtasks.md)
- [Use PRDs to align agents on the design concept](use-prds-to-align-agents-on-the-design-concept.md)

Sources:
- [Building Great Agent Skills: The Missing Manual - Matt Pocock](../sources/20260629_UNzCG3lw6O0.md), 14:56-16:47
