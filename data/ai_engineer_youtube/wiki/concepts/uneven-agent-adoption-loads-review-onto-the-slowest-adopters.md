# Uneven Agent Adoption Loads Review Onto the Slowest Adopters

Summary: When agent adoption is left to individuals, the engineers who adopt fastest generate the diffs the engineers who adopt slowest must read. The laggards lose shipping time to review, and the code they spend that time reading is the worst code on the team — so the experience that was supposed to persuade them does the opposite.

Use when:
- Deciding whether "let people figure agents out for themselves" is an acceptable rollout policy.
- Diagnosing why the engineers furthest behind on agent adoption are also the most hostile to agents.
- Assigning review load on a team with a wide spread in agent throughput.

Details:
- The mechanism, stated in full: "If we live in this figure it out for yourself paradigm… people are going to get outsized productivity, some people aren't, and… the people who are generating like 10 PRs a day are going to like look like, you know, gods compared to people who are shipping like one to two. And the one to two PR people are actually going to get left with the review burden. And that's actually a really, really bad thing. Cuz now not only can they not ship, they're going to actually see bad code and then curse the agents and hence not be able to get on to the let's ship 10 PRs." ([Khandelwal](../sources/20260811_aeTb5BdmTTc.md), 06:06-06:36)
- The loop is self-reinforcing in two directions at once. Review time is time not spent shipping, so the throughput gap widens mechanically; and the sample of agent output the laggard sees is biased toward the unreviewed and the hastily generated, so the belief gap widens too. Neither half requires anyone to behave badly.
- The distinction worth holding onto is *distribution*, not volume. [AI Output Speed Can Overwhelm Review Capacity](ai-output-speed-can-overwhelm-review-capacity.md) already establishes that aggregate generated-code output can outrun aggregate review capacity. This page is about what happens *inside* a team whose average is fine: the load lands on whoever is not producing, and that is exactly the person whose opinion of agents is still being formed.
- This is the argument that makes adoption an org-level responsibility rather than a personal one: the cost of one engineer's non-adoption is paid by that engineer in review hours and by the team in a growing skeptic. See [Own Agent Adoption at the Leadership Layer Because the Fixes Are Shared](own-agent-adoption-at-the-leadership-layer-because-the-fixes-are-shared.md).
- Practical implication for review assignment: if review load is distributed by availability, it will concentrate on the slowest adopters, because they are the most available. That is the opposite of what the rollout needs. The existing guidance to assign review explicitly, with SLOs and turn-taking, applies here with an extra criterion — do not let the reviewer roster become a proxy for the non-adopter roster.
- Caveat on evidence: the 10-versus-1-to-2 PR contrast is an illustration of a pattern from one team of about ten, not a reported measurement. Khandelwal gives no throughput or review-latency numbers anywhere in the talk. The mechanism is plausible and checkable locally (compare review load against PR authorship per engineer); the magnitudes are not established.
- **Figma reports the same unevenness with the identity of the slow adopters filled in, and it is not the low-throughput engineer.** "It's actually our best engineer, the one that hold all their [context] in their brain… they are like holding together with their mental duct tape all the places that agents are not working well… So, they actually end up being slowest to adopt because they see all the problem[s] first hand." That is a different population from the one this page describes — not the engineer shipping one to two PRs, but the engineer the codebase depends on. Both mechanisms can run in the same org at once, and if they do, the review load concentrates on exactly the person whose objections are most worth acting on. ([Blum](../sources/20260828_5Bn0xro2ol8.md), 03:25-04:07)

- **A third axis the load can fall along: career stage, independent of throughput.** "We do see that reviewing AI output is often harder for some than actually writing it, especially early in career. Senior engineers have already spent a large portion of their career reviewing others code. But early career engineers don't have that muscle yet and so reviewing it can feel like a lot more cognitive load than they're used to and actually writing it." This is not the same population as the low-throughput engineer or as Figma's indispensable senior: it is the person whose review skill has not been built yet, and the mechanism is skill formation rather than time displacement or accumulated context. The three axes can coincide — an early-career engineer is often also slower to adopt and more available for review — which would concentrate the load on the reader least equipped to catch what matters. Stated as an observation with no review-latency, defect-escape, or survey data. ([Liguori](../sources/20260828_pqlWNihgdjI.md), 16:17-16:44)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Own Agent Adoption at the Leadership Layer Because the Fixes Are Shared](own-agent-adoption-at-the-leadership-layer-because-the-fixes-are-shared.md)
- [Map Agent Adoption on Fear and Utilization Axes](map-agent-adoption-on-fear-and-utilization-axes.md)
- [AI Output Speed Can Overwhelm Review Capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Make Code Review the Bottleneck Skill for AI-Generated Code](make-code-review-the-bottleneck-skill-for-ai-generated-code.md)
- [Drive Org-Wide Agentic Adoption Through Champions and AI-Ready Repos](drive-org-wide-agentic-adoption-through-champions-and-ai-ready-repos.md)
- [Create Psychological Safety for AI Adoption](create-psychological-safety-for-ai-adoption.md)
- [The Best Engineers Adopt Agents Last, and Their Objections Are the Roadmap](the-best-engineers-adopt-agents-last-and-their-objections-are-the-roadmap.md)
- [Budget the Productivity Dip That Precedes the Agent Speedup](budget-the-productivity-dip-that-precedes-the-agent-speedup.md)

Sources:
- [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../sources/20260811_aeTb5BdmTTc.md), 06:06-06:36
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 03:25-04:07
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 16:17-16:44
