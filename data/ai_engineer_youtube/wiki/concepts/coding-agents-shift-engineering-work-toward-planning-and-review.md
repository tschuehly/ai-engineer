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
- **The shift carries a morale term, and its sign is not automatic.** The same movement can land as loss: "reduced developer agency causes engineers to lose some of their job satisfaction… getting into more of a prompt cycle where they just wait on output from AI… not as much fun as they used to have and they're getting burned out." Blum's claim is that planning is what makes it land the other way — "finding a replacement to the craft of writing code" — because the human is making the decisions in advance rather than reacting to output. Whether the shift reads as deskilling or as craft therefore depends on which end of it a given engineer occupies, which is a distribution question no productivity metric surfaces. ([Blum](../sources/20260828_5Bn0xro2ol8.md), 02:53-03:25, 07:34-08:07)

- **The same shift reported by the platform team that has to serve the resulting workload, with a tension left standing inside one talk.** Bond describes engineers "interacting with the code less… often times not as involved in authoring the code," with humans still approving today but "a short path in the near future to a percentage of our code landing automatically, having automatic approvals." Alongside that he argues the human role expands upward into architecture, domain expertise, and product thinking. Both are presented as the destination, and no criterion is given for which changes fall into the automatically-landed population and which get the expanded review — which is the question the plan turns on. ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 11:11-11:56, 13:44-14:34)
- **The displacement described from the inside, as a change in what you write down.** Krieger's account of his own shift: from "I have an idea, I'm going to break it down in my head much more how I would do engineering normally, and then iterate through these different steps" to "I'm going to describe the goal, like go off and work on it," with tradeoffs and questions surfaced along the way — summarized as "moving from that task delegation to express the end state and then have it go and cook on it." The review half then lands on comprehension rather than time, so the freed capacity is not free: it is spent building a model of work you did not decompose yourself. ([Krieger](../sources/20260827_qqrk7CtkuIw.md), 01:55-02:39, 10:19-10:30)

- **The triage step upstream of the plan, and where the residue goes.** Debois reports teams splitting planning by scopedness rather than by importance: "things that were sufficiently scoped enough were easy to pick up by agents because they were well-defined, and what still was left for the humans were the things that weren't scoped out well… these things can straight go into agents, well-defined, and the harness is getting better, and this is conversational things that we need to decide as a team." That names the human residue as genuinely undecided work rather than as under-specified tickets to be fixed, and makes the boundary a property of the current harness — it moves every cycle, which is why he pairs it with a retro pointed at the system instead of the code. See [Run the Retro Against the System and Split Planning by Scopedness](run-the-retro-against-the-system-and-split-planning-by-scopedness.md). ([Debois](../sources/20260822_zCJtYuqwm7E.md), 06:54-08:00)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Ralph loops process one ticket at a time with fresh context](ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md)
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Separate the Decision Layer From the Implementation Layer](separate-the-decision-layer-from-the-implementation-layer.md)
- [Read the Task-Length Curve at the Success Rate You Would Actually Delegate At](read-the-task-length-curve-at-the-success-rate-you-would-delegate-at.md)
- [Reduced Developer Agency Is an Adoption Cost, and Planning Is Its Remedy](reduced-developer-agency-is-an-adoption-cost-and-planning-is-its-remedy.md)
- [Review Comments Have Two Audiences With Inverted Error Costs](review-comments-have-two-audiences-with-inverted-error-costs.md)
- [The Review Bottleneck Is Comprehension, Not Reviewer Time](the-review-bottleneck-is-comprehension-not-reviewer-time.md)
- [Run the Retro Against the System and Split Planning by Scopedness](run-the-retro-against-the-system-and-split-planning-by-scopedness.md)
- [A Faster Team Relocates the Bottleneck Downstream](a-faster-team-relocates-the-bottleneck-downstream.md)

Sources:
- [Software Engineering Is Becoming Plan and Review - Louis Knight-Webb, Vibe Kanban](../sources/20260502_W76woOYHlvY.md), 02:04-03:30, 12:14-14:01
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../sources/20260809_Kz4QJmNrVXU.md), 07:03-09:55, 18:43-19:16
- [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](../sources/20260808_7vn4WpqNpck.md), 01:39-02:16, 16:36-17:00
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 02:53-03:25, 07:34-08:07
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 11:11-11:56, 13:44-14:34
- [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 01:55-02:39, 10:19-10:30
- [Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl](../sources/20260822_zCJtYuqwm7E.md), 06:54-08:00
