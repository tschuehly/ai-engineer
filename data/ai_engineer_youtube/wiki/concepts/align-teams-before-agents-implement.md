# Align Teams Before Agents Implement

Summary: Cheap agentic implementation shifts the bottleneck from writing code to deciding what should be built. Teams need shared alignment before and during agent work because unaligned agents can create duplicate work, wrong features, merge conflicts, and PR review overload.

Use when:
- Designing team workflows around parallel coding agents.
- Deciding whether an agent task needs shared planning before implementation.

Details:
- Single-player coding-agent interfaces scale individual output, but the source argues software remains a team activity where people must agree on what they are building and why. 01:04-01:38
- When implementation is cheap, opportunity cost becomes the real cost because every agent-built feature displaces another possible investment. 02:20-02:30
- Agentic workflows can remove early planning touchpoints and push alignment into PR review, where rejecting a direction means throwing away already-generated work. 03:52-05:18
- Alignment failures show up as unrequested features, late critical feedback, duplicated work, same-file conflicts, and stacks of PRs that reviewers lack context to evaluate. 05:02-05:34
- **The same team's lead restates it as a qualification of "understanding is the bottleneck," and adds a meter.** Responding to Geoffrey Litt's talk, Gazit accepts the diagnosis at one scale and rejects its scope: "that's very true at a me level. But my personal understanding was never sufficient for shipping code inside a team. Our understanding at an us level can't only happen at the end of the process, when the process happens so much faster." The consequence is now priced rather than merely regretted: "going faster means that a small misalignment can snowball into a ton of wasted work, and that work costs tokens, and tokens cost real money now" — on top of the time. Note also that abundance does not dissolve the prior question: "even if you're a token billionaire, even if you have 10 terminals running Fable night and day, then opportunity cost is still there. It's everything." ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 01:34-01:43, 03:51-04:30)

- **The same argument scaled to an org, with the cost term named.** Mohamed's version is structural rather than workflow-level: per-person AI tooling raises the linear term while "the more people you have, the quadratic term of communication between them and alignment them keep growing," until "your throughput actually is not what you [are] getting." His domain evidence is a time split — roughly 15 chip-design practitioners reporting "we spend 70% of our time doing alignment" — and the inversion he draws from it is the sharpest form of this page's claim: "the most successful chip organization are not the one with the best engineers, but they are the most aligned organizations." Neither the literature behind the quadratic claim nor the 70% figure is sourced or instrumented. ([Mohamed](../sources/20260822_0I6aoPSRzVc.md), 02:37-04:40)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Coding agents shift engineering work toward planning and review](coding-agents-shift-engineering-work-toward-planning-and-review.md)
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)
- [Tell the Agent Only What Is Not Recoverable From the Code](tell-the-agent-only-what-is-not-recoverable-from-the-code.md)
- [Alignment Is the Quadratic Term That Per-Person Tooling Does Not Touch](alignment-is-the-quadratic-term-that-per-person-tooling-does-not-touch.md)

Sources:
- [Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment - Maggie Appleton, GitHub](../sources/20260426_ClWD8OEYgp8.md), 01:04-05:34
- [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../sources/20260808_iQ5xldZ9StU.md), 01:34-01:43, 03:51-04:30
- [What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 02:37-04:40
