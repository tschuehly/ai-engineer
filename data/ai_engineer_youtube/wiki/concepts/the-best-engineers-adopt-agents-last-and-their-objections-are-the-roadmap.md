# The Best Engineers Adopt Agents Last, and Their Objections Are the Roadmap

Summary: In at least one large engineering org, agent adoption is slowest among the strongest engineers — the people holding undocumented institutional context, who see every agent failure first and are already paying for it. Read that as calibrated skepticism rather than resistance: their complaints are a sorted list of the places where verification is missing. Put them in charge of that list instead of trying to persuade them, and they arrive on their own once the fixes lighten their own load.

Use when:
- The loudest agent skeptics on a team are also its most senior or most load-bearing engineers.
- Choosing between an enablement push and a verification-infrastructure push, with budget for one.
- Deciding what to do with a backlog of "the agent got this wrong" complaints.
- Writing an adoption plan and looking for something to sequence it by.

Details:
- **The observation, and the mechanism inside it.** "It's actually our best engineer, the one that hold all their [context] in their brain… they know where all the pitfalls are. They are like holding together with their mental duct tape all the places that agents are not working well and they're preventing all the really bad stuff from coming in… they have all the institutional [context] that ha[s] never [been] written down in their head and they get so much burden and become bottlenecks and get[] really frustrated. So, they actually end up being slowest to adopt because they see all the problem[s] first hand." ([Blum](../sources/20260828_5Bn0xro2ol8.md), 03:25-04:07)
- **Why this inverts the usual reading.** Late adoption is normally treated as a fluency or fear problem, to be met with training or demonstrations. Here the causal arrow runs the other way: these engineers are late *because* they have the most evidence, and the evidence is real. An enablement program aimed at them is answering a question they did not ask.
- **The move is delegation, not persuasion.** "Just make sure to bring them in rather than trying to figure out how to make them use the AI. Just… let's have them be in charge of the road map to make AI safe [in] your organization, and they will come along once they see that the improvement that they're making [is] actually making their life better." The incentive is self-interest rather than conversion: the fixes they specify are fixes to the failures they are personally absorbing. (11:45-12:33)
- **Their complaints are already prioritized.** "They're skeptic[al] because they're seeing the way you are lacking validation, where your tools fail. So… their feedback is basically the road map of how to improve your agent[s] interacting with the code base." The ordering comes for free — the failures they raise first are the ones costing them most, which is a reasonable proxy for what is costing the codebase most. And they are not reticent: "They'll not be shy about telling you what you need to fix." (11:57-12:45)
- **The undocumented-context detail is the load-bearing one.** These engineers are the same population the wiki's context material keeps pointing at: the institutional knowledge nobody wrote down lives in their heads, which is exactly what an agent lacks. That makes them simultaneously the best source of agent context and the people with the least reason to volunteer it, since writing it down dissolves the position that makes them a bottleneck. Nothing in the talk addresses that conflict; see [Demand-Driven Context Pulls Knowledge From Failed Work](demand-driven-context-pulls-knowledge-from-failed-work.md) for a loop that extracts the same knowledge from failures rather than from goodwill.
- **How this relates to the wiki's existing adoption pages.** [Uneven Agent Adoption Loads Review Onto the Slowest Adopters](uneven-agent-adoption-loads-review-onto-the-slowest-adopters.md) explains why the slowest adopters end up hostile — they absorb the review load and see the worst code. This page says something stronger and independent about *who* they are: not the least capable, but the most context-rich, which makes their hostility informative rather than merely understandable. Read together, the two form a full loop: the highest-context engineers absorb the failures, the failures make them skeptics, and the skepticism is the specification for the fix.
- **Against a mandate.** [Map Agent Adoption on Fear and Utilization Axes](map-agent-adoption-on-fear-and-utilization-axes.md) records that mandates raise utilization without raising confidence. This page supplies the reason a mandate is worse than useless on this specific population: it overrides the exact signal you would most want to keep, from the people best positioned to produce it.
- **Caveats, and they matter.**
  - This is one org's observation with no distribution behind it, and "best" is not defined independently of the property being explained — the engineers holding the most undocumented context are called the best engineers, and the claim is that they adopt last. The tautology risk is real.
  - No count, rate, or timeline is given for how many skeptics "came along," or how long it took, or whether any did not.
  - The strategy assumes the complaints are addressable. A skeptic whose objection is that the work fundamentally requires taste has produced a roadmap item nobody can close, and the talk does not cover the case where the roadmap does not converge.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Uneven Agent Adoption Loads Review Onto the Slowest Adopters](uneven-agent-adoption-loads-review-onto-the-slowest-adopters.md)
- [Map Agent Adoption on Fear and Utilization Axes](map-agent-adoption-on-fear-and-utilization-axes.md)
- [Invest in One High-Value Skill to Convert Agent Skeptics](invest-in-one-high-value-skill-to-convert-agent-skeptics.md)
- [Own Agent Adoption at the Leadership Layer Because the Fixes Are Shared](own-agent-adoption-at-the-leadership-layer-because-the-fixes-are-shared.md)
- [Create Psychological Safety for AI Adoption](create-psychological-safety-for-ai-adoption.md)
- [Treat Agent Readiness as Verification Infrastructure](treat-agent-readiness-as-verification-infrastructure.md)
- [Demand-Driven Context Pulls Knowledge From Failed Work](demand-driven-context-pulls-knowledge-from-failed-work.md)
- [Reduced Developer Agency Is an Adoption Cost, and Planning Is Its Remedy](reduced-developer-agency-is-an-adoption-cost-and-planning-is-its-remedy.md)

Sources:
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 03:25-04:07, 11:45-12:45
