# Own Agent Adoption at the Leadership Layer Because the Fixes Are Shared

Summary: Agent adoption cannot be delegated to individual engineers, because the changes that actually raise agent performance — reorganizing the codebase for progressive disclosure, converging everyone onto one shared setup, funding standing iteration on it — are not changes an IC has the authority or the scope to make.

Use when:
- Deciding who owns making coding agents work on a team: the enthusiastic IC, a platform group, or engineering leadership.
- Justifying budget for harness work that produces no shippable PRs in the near term.
- Explaining why a per-engineer enablement program plateaus.

Details:
- The claim and its reason: "It isn't really an IC's job. It's a job for leadership. It's a job for the company. Making engineers work well with their agents is truly the most impactful thing you could do as an organization." The structural reason follows a minute later: "The most impactful things that you can do to set up your code base to like make it work well require team buy-in. You can't just like if you want to change the way your code base is organized, you can't do that as an IC." ([Khandelwal](../sources/20260811_aeTb5BdmTTc.md), 05:44-06:06, 06:43-06:56)
- The cost of not owning it is not slow adoption, it is negative adoption: uneven adoption redistributes review onto the people who have not adopted, who then form their opinion of agents from the worst code on the team. See [Uneven Agent Adoption Loads Review Onto the Slowest Adopters](uneven-agent-adoption-loads-review-onto-the-slowest-adopters.md).
- The hardest part of converging on a shared setup is not technical. The method is to "find your best ICs and find… how they are making the code base work for them. Take those practices and pass them or guide. People can't live in their own practices." Khandelwal names the resistance precisely: "this is really hard for engineers to do it. It's basically accepting that my setup is imperfect." (09:14-09:37)
- He makes the ownership shift a rhetorical move as well as a structural one. On the slide, the possessive is struck through: instead of "the model is so dumb," ask "how can I make it smarter or how can I edit… This is where I have like crossed out the my. It's not a personal setup. It's the shared setup that you have to invest in." (13:34-13:51)
- The buy-in test is behavioral, not attitudinal: "You have to get them to be able to edit and play with the shared setup cuz that's the true way you know that they're actually invested." Editing the shared configuration is a stronger adoption signal than usage telemetry, because it requires both permission and belief. (10:56-11:15)
- The work never finishes, so it needs a standing line rather than a project: "you can't assume that you do this for a month and you're done. Like, things are going to change constantly underneath." His budgeting shape is "X% of your IC time is probably going to be spent on… iterating on this thing, which is not going to lead to like meaningful PRs like up front, but it's useful and it's worth it." The percentage is deliberately left unspecified. (08:19-08:33, 11:22-11:42)
- Mandates are ruled out on the same grounds as in the wiki's earlier adoption material: "people will figure it out. Let's just mandate our way through life. Like, that's just not going to work… Fear is real. Human emotions are real." His own account of the industry arc has mandates and "token maxing" raising usage without raising confidence, followed by shipped slop and SEV-2s. (01:04-02:01, 08:33-08:50)
- Relationship to the champions pattern: [Drive Org-Wide Agentic Adoption Through Champions and AI-Ready Repos](drive-org-wide-agentic-adoption-through-champions-and-ai-ready-repos.md) is a rollout *mechanism* built on the same premise — the repo is the leverage point because it is shared. Khandelwal adds the constraint that mechanism has to satisfy: the champions' practices must actually replace personal setups, not sit alongside them, or the codebase never converges.
- Caveat on evidence: this is one leader's account of one team of about ten over a few months, with no measurements of any kind. The ownership argument is structural and holds on its own logic; the claim that this is "the most impactful thing you could do as an organization" is an assertion.
- **Coexistence is what makes this an org-level problem rather than a team-by-team one.** Figma's teams sit in different acts simultaneously — "very AI forward and have already transformed their entire workflows" beside teams "still experimenting in the earlier act and/or have lost confidence" — and "they all need to work together in order to ship our product." The scope limit matters as much as the mandate: Blum finds "diminishing return[s] in trying to centralize everybody on one thing, but as long as it works for their flow and other people can iterate with them, I find that it generally works very well." Leadership owns the shared substrate (verification, encoded criteria, deterministic flows) because every team's agents hit it; the personal loop stays personal. ([Blum](../sources/20260828_5Bn0xro2ol8.md), 02:09-02:44, 10:26-11:00)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Uneven Agent Adoption Loads Review Onto the Slowest Adopters](uneven-agent-adoption-loads-review-onto-the-slowest-adopters.md)
- [Map Agent Adoption on Fear and Utilization Axes](map-agent-adoption-on-fear-and-utilization-axes.md)
- [Invest in One High-Value Skill to Convert Agent Skeptics](invest-in-one-high-value-skill-to-convert-agent-skeptics.md)
- [Drive Org-Wide Agentic Adoption Through Champions and AI-Ready Repos](drive-org-wide-agentic-adoption-through-champions-and-ai-ready-repos.md)
- [Create Psychological Safety for AI Adoption](create-psychological-safety-for-ai-adoption.md)
- [AI adoption depends on incentive design as much as tool access](ai-adoption-depends-on-incentive-design-as-much-as-tool-access.md)
- [Institutionalize Knowledge Infrastructure for AI Adoption](institutionalize-knowledge-infrastructure-for-ai-adoption.md)
- [Harness Engineering Shifts Scarcity From Code Production to Control Surfaces](harness-engineering-shifts-scarcity-from-code-production-to-control-surfaces.md)
- [The Best Engineers Adopt Agents Last, and Their Objections Are the Roadmap](the-best-engineers-adopt-agents-last-and-their-objections-are-the-roadmap.md)

Sources:
- [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../sources/20260811_aeTb5BdmTTc.md), 01:04-02:01, 05:44-06:56, 08:19-08:50, 09:14-09:37, 10:56-11:42, 13:34-13:51
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 02:09-02:44, 10:26-11:00
