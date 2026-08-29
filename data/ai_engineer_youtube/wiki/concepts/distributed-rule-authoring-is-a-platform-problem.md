# Distributed Rule Authoring Is a Platform Problem, Not an Authoring Problem

Summary: When hundreds of teams write their own review rules, the authoring step turns out to be trivial — a team asks a model to read its past PR reviews and produce a skill. What is hard is running hundreds of team-authored skills at consistent quality and low cost, which is a platform obligation: bind rules to the existing ownership model, co-locate them with the code, route deterministically, and return per-rule observability to the author so bad rules get retired by the people who wrote them.

Use when:
- Standing up team-customizable agent behaviour — review rules, lint agents, or skills — across an org too large to curate centrally.
- Estimating the work in a "let teams write their own rules" proposal, and finding the estimate concentrated in the wrong place.
- Deciding which checks must be centrally mandated and which may be team-owned.
- Designing the feedback path that stops a rule library from accumulating rules nobody wants.

Details:
- **The claim, stated as the lesson.** "One thing that we learned is that actually writing the skill was very easy. Like teams just very quickly wrote a skill by asking Claude to write one, go over my previous PR reviews and write me a skill. But the hard part was how to run these skills at scale with consistent quality and low cost. And that required a lot of iterations not only from the uReview team side, but also like for each team who was trying to write these rules." ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 09:43-10:12)
- **The constraint that forces distribution.** "With hundreds of teams across the company, we can't have centralized management of our code reviews, our customizations, and our rules, and even the knowledge that goes into those code reviews. We need to distribute that." Note the third item — the *knowledge* behind a rule cannot be centralized either, which is why the platform's job is routing and operating rules rather than owning them. (02:04-02:25)
- **Obligation one: bind to the ownership model you already have.** "We have a need for plugging into existing team ownership system rather than trying to replicate that externally," and later, "we had to actually piggyback on our ownership model which is at Uber so that we can like very logically roll out to all the teams." A parallel rule registry with its own notion of who owns what drifts from the real one; reusing the existing mapping is what makes rollout a routing question instead of a migration. (02:04-02:25, 08:41-08:53)
- **Obligation two: co-locate the rule with the code.** "Co-locate the customizations next to where the developers write their code so that they can like quickly keep updating these customizations." The editing cost of a rule sets its refresh rate; a rule that lives in a separate console gets written once and never revised.
- **Obligation three: deterministic routing.** "We had to implement a smart deterministic routing so that we could route which team gets what kind of review with which model, what kind of generators, and so on." Two things are worth separating here: the *selection* of rules is deterministic and ownership-derived, while the *execution* is a model. Making the selection layer deterministic is what keeps the cost and latency of a review predictable across hundreds of configurations. (09:05-09:16)
- **Obligation four: return the observability to the rule's author.** "The hard thing was like we had to actually surface all of this observability… like the agent trajectory, addressal rate, sentiment analysis back to the teams. So that the teams could actually understand that 'Oh, I wrote this rule, but maybe not a lot of developers are liking it in my team, so let me go and update it.'" This is the garbage-collection mechanism a distributed rule library otherwise lacks: nobody centrally reviews rules for value, so the author has to be shown their own rule's reception. The same view goes to "all the people who are contributing to the platform." (09:16-09:43)
- **The counter-force, which bounds how much may be delegated.** Some checks cannot be optional: "we need to make sure that we have security and compliance reviews run across everything. We can't rely on teams hoping to run the code review skill that happens. We need reliability there." This is the argument for putting mandatory checks in the review platform rather than in each team's agent configuration — a rule that lives only in the harness is advisory, because whether it runs depends on how someone invoked the agent. (02:43-02:57)
- The customization surface is a ladder rather than one format, and teams pick a rung by how much structure their check has: general-purpose per-file logic-bug review; a deep multi-file review carrying each monorepo's anti-pattern style guides; few-shot "AI linters" where "developers can basically kind of deterministically get more context and then run rules with that context and like a file and find some systematic and mechanical issues"; and at the top, a custom agent "link[ed] to like a knowledge base… link[ed] to their past PRs, [with] a skill to do the review." (07:37-08:41)
- Relation to the mining pattern this wiki already carries: [Mine Recurring Review Comments Into an Invariant Registry](mine-recurring-review-comments-into-an-invariant-registry.md) says the corpus of past review comments already contains the rules. Uber's teams did exactly that ("go over my previous PR reviews and write me a skill") and found it took minutes. This page is the next problem in that sequence — the mining is not the bottleneck, operating the result is — and the two compose directly.
- Limits. No figures are given for how many teams authored rules, how many rules exist, what any of them cost to run, or how often a rule is retired after its author sees the feedback. The four obligations are described as things they had to build, not as an evaluated design. ([Provenance and Limits](../sources/20260828_EL123UNokkI.md))

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Mine Recurring Review Comments Into an Invariant Registry](mine-recurring-review-comments-into-an-invariant-registry.md)
- [Govern Agent Rules Through Feedback Gatekeepers](govern-agent-rules-through-feedback-gatekeepers.md)
- [AI Review Gates Turn Standards Into Executable Feedback](ai-review-gates-turn-standards-into-executable-feedback.md)
- [Use Reviewer Agents and Lints to Turn Review Lessons Into Guardrails](use-reviewer-agents-and-lints-to-turn-review-lessons-into-guardrails.md)
- [Build Internal AI Engineering Platforms When Off-the-Shelf Tools Lack Enterprise Context](build-internal-ai-engineering-platforms-when-off-the-shelf-tools-lack-enterprise-context.md)
- [Measure a Review Bot by Whether the Comment Changed the Code](measure-a-review-bot-by-whether-the-comment-changed-the-code.md)

Sources:
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 02:04-02:57, 07:37-10:12
