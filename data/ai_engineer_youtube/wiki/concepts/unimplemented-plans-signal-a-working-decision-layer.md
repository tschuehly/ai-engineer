# Unimplemented Plans Signal a Working Decision Layer

Summary: When a team moves its work into durable plan documents, the first reported effect is that people write plans they never build — and that is the success signal, not waste. It means ideas are being prioritized *after* exploration instead of before, which is the shift from code velocity to idea velocity and the escape from prototype gravity.

Use when:
- Judging whether a planning-first workflow is working, without a throughput metric to point at.
- Answering the objection that time spent on plans that never ship is time wasted.
- Deciding whether to prototype an idea or explore it in writing first.

Details:
- The observation: "the first thing we see happen actually is that people start to plan and then not implement their plan. Uh and this is actually like a really good sign. Because what that means is they're thinking through ideas… 'I have this vague thought. Don't just give me some code. Don't go off and… build it for me, but let… me understand the idea that I'm talking about.'" ([Dailey](../sources/20260809_Kz4QJmNrVXU.md), 14:33-14:57)
- Why it counts as prioritization rather than abandonment: "then they have a bunch of these and then some of them are getting built and some of them aren't. So, that means they're prioritizing the ideas that after they've explored them are the ones that are worth building." The selection happens with exploration already paid for, which is the only point at which the comparison is informed. (14:57-15:10)
- The reframe: "you're shifting from code velocity to idea velocity." The velocity metric does not disappear; the unit it counts changes from shipped code to explored ideas, which is what makes an unbuilt plan legible as output. (15:12-15:18)
- **Prototype gravity** is the named failure it avoids: "rather than… getting stuck in prototype gravity where we build something and we're so excited to just ship that thing and we're going down like one path of the idea maze, we can now… more effectively explore that whole maze and find that gold that's around the corner." The mechanism is commitment, not sunk cost in the accounting sense — a built thing is shippable, and shippable things get shipped. (15:18-15:48)
- The tension worth holding with the wiki's prototyping thread. [Parallel Agent Prototypes Turn Design Choices Into Measurements](parallel-agent-prototypes-turn-design-choices-into-measurements.md) argues the opposite direction: build several options cheaply and let real metrics decide. Both are exploration strategies for the same moment, and they differ on what the artifact is for. A prototype answers questions writing cannot ("does this actually work / how does it feel"); a plan avoids acquiring an artifact you will feel obliged to ship. The reconcilable version: prototype in parallel *when* the open question is empirical, plan when the open question is what matters — and keep prototypes explicitly disposable so gravity does not attach.
- A second-order effect on cost, implied but not priced by the talk: exploring an idea to the point of a decision costs a document rather than a day of agent implementation, and it is the discarded ones that make the difference. The talk offers no numbers on either side.
- Timing argument for why this must happen early: realignment is cheap "before someone has spent even a day in AI going deep on some idea building a prototype, we can talk about it early and make sure we're aligned on where we [are] actually taking the system." Once a person has invested, the conversation is no longer about the idea. (16:38-16:54)
- Caveat: this is a vendor's observation of its own users with no denominator — no count of plans written versus built, no team sizes, no comparison against a team that did not adopt the workflow. Read the signal as a qualitative tell to look for, and be alert to its failure mode: plans nobody implements can also mean plans nobody trusts, or a team that has moved its procrastination upstream.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Separate the Decision Layer From the Implementation Layer](separate-the-decision-layer-from-the-implementation-layer.md)
- [Make the Doc the State and the Agent the Action](make-the-doc-the-state-and-the-agent-the-action.md)
- [Parallel Agent Prototypes Turn Design Choices Into Measurements](parallel-agent-prototypes-turn-design-choices-into-measurements.md)
- [Measure Feature Adoption, Not Shipping Velocity](measure-feature-adoption-not-shipping-velocity.md)
- [Review research and plans before they multiply into code](review-research-and-plans-before-they-multiply-into-code.md)

Sources:
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../sources/20260809_Kz4QJmNrVXU.md), 14:33-15:48, 16:38-16:54
