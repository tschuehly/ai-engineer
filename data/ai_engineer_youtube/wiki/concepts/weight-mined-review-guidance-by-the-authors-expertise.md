# Weight Mined Review Guidance by the Author's Expertise

Summary: Mining a team's PR history into agent-facing best practices treats every past comment as equally authoritative. Weighting by who wrote it — seniority, or measured expertise in that area of the codebase — makes the surfaced guidance match what the team's most trusted reviewers actually say. The expertise signal can come from the same review graph that already tells you where review coverage is thin.

Use when:
- Turning years of review comments into rules, skills, or reviewer prompts, and needing a ranking.
- An AI reviewer's comments are technically defensible but do not sound like your team.
- You already build an ownership or review graph and are looking for a second use for it.
- Deciding what to do when mined comments conflict with each other.

Details:
- The mining step: the system "looks at pull request data — and there are other data sources for this — and it generates a series of best practices that help align agents to your codebase," then surfaces the same material through the code review agent rather than only to coding agents. ([Werry](../sources/20260827_qdAkxLoYNI8.md), 12:44-13:10)
- The weighting step, stated as policy: "Richie's one of the senior engineers, and we use the sort of seniority or expertise as a signal to boost comments that are important." (13:24-13:40)
- The validation anecdote, and what it is worth: the senior engineer's reaction to a surfaced comment was "Oh, that's cool. That's something I would say" — "and that's because that actually was something he said." That is a provenance check, not a correctness check. It confirms the mining recovered his voice; it says nothing about whether the comment helped on this PR. For the harder signal, see [Measure a Review Bot by Whether the Comment Changed the Code](measure-a-review-bot-by-whether-the-comment-changed-the-code.md). (13:10-13:28)
- Where the expertise score can come from without a new system: the engineering social graph built from review relationships — who reviews whose code — clustered into teams and projected onto the codebase as a coverage map, "and that's exactly what we use within the context engine itself." One graph, two outputs: a staffing risk map, and a per-area authority weight for mined guidance. (16:04-16:44)
- Why the weighting is worth the complexity. A flat mine of review history conflates settled conventions with one-off opinions, and conflicts within it have no tiebreak. Authority-weighting supplies the tiebreak the corpus lacks, and does it with a signal the organization already produces.
- The failure mode to design against: seniority is a proxy for correctness, and proxies calcify. A boosted corpus reproduces the tenured reviewers' preferences, including the outdated ones, and suppresses a newer engineer who was right — the same "do not" that a better model no longer needs, kept alive because a principal engineer wrote it in 2024. Pair the weighting with a decay or review pass over the boosted set.
- Composition with the retrospective-mining pattern this wiki already holds: mine the backlog in bulk for what repeats, then rank what repeats by who said it, and keep appending. See [Mine Recurring Review Comments Into an Invariant Registry](mine-recurring-review-comments-into-an-invariant-registry.md).
- Limit: demonstrated by one reaction from one engineer in a vendor demo. No measurement of whether boosted comments are more often correct, more often acted on, or better received than unweighted ones.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Mine Recurring Review Comments Into an Invariant Registry](mine-recurring-review-comments-into-an-invariant-registry.md)
- [Use Social and Expert Graphs to Personalize Coding-Agent Context](use-social-and-expert-graphs-to-personalize-coding-agent-context.md)
- [Measure a Review Bot by Whether the Comment Changed the Code](measure-a-review-bot-by-whether-the-comment-changed-the-code.md)
- [Code Review Carries Alignment, Not Just Correctness](code-review-carries-alignment-not-just-correctness.md)
- [Comment Volume Is a Property of the Review Pipeline, Not the Model](comment-volume-is-a-property-of-the-review-pipeline.md)

Sources:
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 12:44-13:40, 16:04-16:44
