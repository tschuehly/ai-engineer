# Coding Agents Shift Engineering Work Toward Planning and Review

Summary: As coding agents generate more of the implementation, the scarce human work moves into deciding what should be done, checking whether the result is right, and carrying the change through delivery. Treat agent adoption as work displacement into planning and review rather than assuming code-generation time becomes free time.

Use when:
- Designing team workflows around coding agents.
- Explaining why review load can rise even when agents write more code.
- Deciding what parts of software engineering tooling should be optimized for humans.

Details:
- The talk breaks software engineering work into planning, writing code, reviewing generated code, and reviewing other people's code, then argues that Copilot, ChatGPT, Cursor, and Claude Code progressively shrink the direct code-writing portion. (02:04-02:51)
- The displaced time moves into planning and reviewing; the speaker describes AI as an accelerant that increases daily throughput but still leaves humans responsible for higher-leverage planning and review work. (02:52-03:30)
- Mature coding-agent interfaces should optimize task writing, QA, code review, and change shepherding because those are the human responsibilities that remain visible when agents handle more implementation. (12:14-14:01)

- Matt Dailey (Ref) sharpens the displacement in two ways. First, the phases are not one new job but two gears with different requirements — planning is "creative and collaborative," polish is evaluative and local — so "the skill now is what gear am I in? Am I using the appropriate tools for the gear that I'm… trying to accomplish right now." Second, the displaced work inherits the wrong tools: "all our history of coding tools were built for this style of work. Um our IDE, our workhorse… it was built for implementation and polish to be done by an individual, to be heads down." The cheap diagnostic is drift inside a single session — notice "when you drift from the planning phase into the polish phase," and whether the tool still fits. ([Dailey](../sources/20260809_Kz4QJmNrVXU.md), 07:03-09:55, 18:43-19:16)
- **The unit of input changed, and the shift can be dated.** Denys Linkov contrasts "back in 2025… you would use models to generate snippets of code, small functions" with today's "well-constructed spec that you give to a model." His own six-month monorepo consolidation shows the adoption happening mid-project rather than up front: plan mode was picked up partway through and became the default entry point for each batch of work, alongside all-human PR review. The planning displacement is therefore something a team can observe arriving during a single project, not a posture adopted in advance. ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 01:39-02:16, 16:36-17:00)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Ralph loops process one ticket at a time with fresh context](ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md)
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Separate the Decision Layer From the Implementation Layer](separate-the-decision-layer-from-the-implementation-layer.md)
- [Read the Task-Length Curve at the Success Rate You Would Actually Delegate At](read-the-task-length-curve-at-the-success-rate-you-would-delegate-at.md)

Sources:
- [Software Engineering Is Becoming Plan and Review - Louis Knight-Webb, Vibe Kanban](../sources/20260502_W76woOYHlvY.md), 02:04-03:30, 12:14-14:01
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../sources/20260809_Kz4QJmNrVXU.md), 07:03-09:55, 18:43-19:16
- [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](../sources/20260808_7vn4WpqNpck.md), 01:39-02:16, 16:36-17:00
