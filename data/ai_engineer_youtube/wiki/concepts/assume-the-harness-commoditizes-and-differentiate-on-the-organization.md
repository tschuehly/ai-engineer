# Assume the Harness Commoditizes and Differentiate on the Organization

Summary: A planning premise worth testing against your roadmap: harnesses and loops become commodity — plausibly sold as a service by a frontier lab — so the work of assembling them is table stakes rather than advantage. What does not commoditize is the organization around them and the knowledge captured in context, skills, and constraints.

Use when:
- Deciding how much of a multi-year plan to stake on a proprietary internal harness.
- Weighing an investment in harness engineering against an investment in captured domain knowledge.
- A vendor or a frontier lab ships something that replaces six months of your internal loop work.
- Explaining why an enablement program should be scoped to the organization rather than the tooling.

Details:
- **The premise, stated at the top of the talk as its foundation.** "There's been a lot of conference talks here about optimizing agents with loops and harnesses… and I think that's great. But eventually, we'll get there… one day, this will kind of become commodity. Somewhere maybe even going into one of the frontier labs that just offers this as a service… And that's not going to be the differentiator for your organization. So, I'm starting from there up." ([Debois](../sources/20260822_zCJtYuqwm7E.md), 00:56-01:38)
- **What is left when the harness is commodity.** "Assume we're heading towards the dark factory, some kind of form of autonomous working within an organization… it changes dynamic of the way you collaborate around us… today, I'm not talking about how do you become better with your agent, but how it will change your team dynamics, your platform, and your organization." (01:38-02:17) The rest of the talk is that argument: team rituals, a platform registry, an ownership mandate, hiring, and spend policy.
- **And the asset.** "I think your moat is capturing the knowledge. The knowledge you're putting now into skills, in your context, and maybe in your harness, the way you restrain this, your business context." (20:24-20:43) Note that the harness appears on *both* sides — the machinery commoditizes, the constraints encoded in it do not. The distinction is between the loop and what the loop knows about your business.
- **This is in direct tension with the wiki's harness-investment position, and the tension is real.** [Harness Engineering Shifts Scarcity From Code Production to Control Surfaces](harness-engineering-shifts-scarcity-from-code-production-to-control-surfaces.md) collects several sources — including Anthropic's own applied team — arguing the harness is the binding constraint on what models can achieve. Debois does not dispute that; he disputes its durability. The reconciling reading is that harness work is necessary and non-durable: it is worth doing now because nothing else unblocks the model today, and it is a bad thing to plan to *own* in three years. The wiki already holds the mechanism that makes non-durability concrete — [A Harness Fix Becomes Overhead When the Model Outgrows It](a-harness-fix-becomes-overhead-when-the-model-outgrows-it.md) and [Keep the Harness Thick Early and Thin It as the Model Improves](keep-the-harness-thick-early-and-thin-it-as-the-model-improves.md) describe the same depreciation from inside a single team's codebase.
- **Read as a commoditization argument, it matches a pattern the wiki has recorded elsewhere.** [Commoditize the Layer You Do Not Win On](commoditize-the-layer-you-do-not-win-on.md) records that commoditization relocates competition one layer up rather than ending it — hyperscalers stopped competing on raw compute and started competing on databases and serverless. Debois is naming where he expects the relocation to land for coding agents: the organization and its captured knowledge. That page's caution applies here too, that standardization is path-dependent, which would make an internally-built harness costly to leave once the commodity arrives.
- **The premise also carries the talk's own risk.** If harnesses do not commoditize, or commoditize slowly and unevenly, then organizations that treated harness work as table stakes will have under-invested in the thing that was actually differentiating. Nothing in the talk hedges this, and see [Building the Harness Is the Engineering Path That Prompting Took Away](building-the-harness-is-the-engineering-path-that-prompting-took-away.md) for a second-order cost: harness work is also what re-engaged the developers who rejected prompting, so declaring it commodity removes the answer to an adoption problem the same talk describes.
- **Caveats.**
  - The premise is a prediction with no evidence behind it beyond an analogy to continuous delivery in 2009. No timeline, no mechanism, and no account of which parts commoditize first.
  - Debois works at Tessl, whose position is in spec- and context-driven development. "Harnesses are commodity, captured knowledge is the moat" is the argument that favours that position, and the talk does not flag the interest.
  - "Capturing the knowledge" is asserted as a moat without any account of what protects it. Context, skills, and business constraints are files; they leave with people and with repositories at least as easily as any other artifact.

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Harness Engineering Shifts Scarcity From Code Production to Control Surfaces](harness-engineering-shifts-scarcity-from-code-production-to-control-surfaces.md)
- [Commoditize the Layer You Do Not Win On](commoditize-the-layer-you-do-not-win-on.md)
- [A Harness Fix Becomes Overhead When the Model Outgrows It](a-harness-fix-becomes-overhead-when-the-model-outgrows-it.md)
- [Keep the Harness Thick Early and Thin It as the Model Improves](keep-the-harness-thick-early-and-thin-it-as-the-model-improves.md)
- [Skills Are the Residual Where Organizational Know-How Lands](skills-are-the-residual-where-organizational-know-how-lands.md)
- [Target Swap Speed, Not Stability, as the Reliability Goal](target-swap-speed-not-stability-as-the-reliability-goal.md)
- [Building the Harness Is the Engineering Path That Prompting Took Away](building-the-harness-is-the-engineering-path-that-prompting-took-away.md)

Sources:
- [Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl](../sources/20260822_zCJtYuqwm7E.md), 00:56-02:17, 20:24-20:43
