# A Faster Team Relocates the Bottleneck Downstream

Summary: Speeding up engineering with agents does not end at engineering. The people downstream — go-to-market, support, and users themselves — cannot absorb the new rate, and the upstream side stops supplying requirements fast enough. The harness has to extend past coding in both directions, or the local gain is consumed by a queue somewhere else.

Use when:
- Engineering throughput is visibly up and shipped-value is not.
- Planning an agent rollout scoped to the engineering org, and deciding whether that scope is defensible.
- Deciding where the next automation investment goes after the coding loop is working.
- A product function is complaining that engineering is "shipping too fast."

Details:
- **The claim.** "One of the impacts of that is that if you start producing as a team more, the people downstream — GTM, people like that — they have a hard time keeping up. Even users have a hard time keeping up. So, you need to help them also with automation. So, your harness doesn't stop at your coding. It also is extended to those people as well." ([Debois](../sources/20260822_zCJtYuqwm7E.md), 08:27-08:55)
- **The upstream half is the easier one to miss.** "And the same thing with gathering requirements: the input might not come fast enough for your team. So, that's another piece that you need to tap into that workflow as well." (08:55-09:09) An engineering team that has removed its own implementation constraint becomes starved rather than saturated — the queue that was always full is now empty, and the constraint is a product manager's writing speed.
- **"Even users have a hard time keeping up" is the strangest item on the list and the one worth keeping.** It is not a staffing problem that automation obviously fixes. Shipping faster than users can absorb change is a product-side cost — release notes nobody reads, retraining, churn — and Debois names it without offering a remedy beyond automation generally.
- **This is Theory-of-Constraints reasoning applied to an agent rollout, and it has a direct planning consequence.** If the bottleneck moves as soon as you relieve it, an enablement program scoped to "engineering" is scoped to one station on the line. The wiki's [Target AI Rollouts at SDLC Bottlenecks](target-ai-rollouts-at-sdlc-bottlenecks.md) and [Shape AI Teams Around the Bottleneck](shape-ai-teams-around-the-bottleneck.md) both say to find the constraint first; this page adds the second step, that finding it once is not enough, because your own success invalidates the answer.
- **It also reframes what "harness" means.** In most of the wiki the harness is a coding-agent construct — tools, context, checks, loops around a code-writing model. Debois uses it as the general name for the machinery around any agent-assisted workflow, and the practical claim is that the same investment discipline transfers: the GTM team's intake and the requirements pipeline get automated the way the build did. The wiki's non-coding agent material ([Agents for Everything Else](../sources/20260501_zepu8Kk6FBQ.md)) is the closest thing to a catalogue of what that looks like in practice.
- **Caveats.**
  - No evidence at all. This is asserted as something Debois has seen, with no organization named, no measurement of the downstream queue, and no case where the extension was actually built.
  - It assumes the downstream work is automatable in the same way coding is. GTM approvals, contractual review, and user retraining are not obviously the same kind of problem, and the talk does not distinguish them.
  - "Users have a hard time keeping up" could equally be an argument for shipping *less* often rather than automating around it. Nothing in the talk considers that reading.

Related topics:
- [Workflows](../topics/workflows.md)

Related concepts:
- [Target AI Rollouts at SDLC Bottlenecks](target-ai-rollouts-at-sdlc-bottlenecks.md)
- [Shape AI Teams Around the Bottleneck](shape-ai-teams-around-the-bottleneck.md)
- [Measure Enablement by Human Touches and Share of Fixes Reused](measure-enablement-by-human-touches-and-share-of-fixes-reused.md)
- [Run the Retro Against the System and Split Planning by Scopedness](run-the-retro-against-the-system-and-split-planning-by-scopedness.md)
- [Agent Enablement Falls Between Platform and Developer Experience, So Name an Owner](agent-enablement-falls-between-platform-and-developer-experience-so-name-an-owner.md)

Sources:
- [Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl](../sources/20260822_zCJtYuqwm7E.md), 08:27-09:09
