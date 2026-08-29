# When Code Stops Being the Long Pole, Approvals Become It

Summary: Governance overheads that were rounding errors against a 9-12 month build become the critical path when the build takes one to two months. Amazon's observation is that decision speed — the time to approve building a product and to approve launching it — is the bottleneck that replaces manual coding, and that frontier teams now spend more time deciding than writing code.

Use when:
- A team has demonstrably faster delivery and the overall time-to-customer has not moved.
- Prioritizing where to spend organizational-change effort after coding-agent adoption succeeds.
- Arguing for a lighter approval path for reversible decisions.

Details:
- **The arithmetic, which is the whole argument.** "When it used to take 9 to 12 months to build a new product, it didn't matter so much in the overall wash of things if it took two months to make the decision to build the product and then two months to approve the launch. But now those are the bottlenecks. Those are the long pole." Nothing about the approval process changed; the denominator did. ([Liguori](../sources/20260828_pqlWNihgdjI.md), 19:13-19:37)
- **The named replacement.** "Previously, writing code manually was the bottleneck… the speed of decision-making becomes a new bottleneck. The more that you spend reviewing the decision to actually build a new product, the slower it is to build the product now because the code only takes 1 to two months to write." (18:45-19:13)
- **The observable that tells you it has happened.** "Often I find that frontier engineering teams spend more time making decisions than they do writing code." That ratio is checkable on a real team without any instrumentation, and it inverts the ratio most engineering processes were designed around. (19:37-19:49)
- **The prescription, and its limit.** "The more that you can make fast decisions, especially ones that are easy to be reversed, the better." The qualifier is doing real work: this is not an argument for removing approval from decisions that are expensive to undo, it is an argument for sorting decisions by reversibility and refusing to pay a two-month review on the reversible ones. Liguori does not say which Amazon reviews were shortened, or by how much. (19:49-19:56)
- **Why this is a different claim from "the bottleneck moves."** The wiki already records the bottleneck migrating *inside* the engineering loop — from token generation to compute to human attention, and from code production to review capacity. This one moves *outside* it, into product approval, launch review, and legal or compliance sign-off, which are owned by people who were not part of the coding-agent rollout and who have no reason to have noticed that the constraint arrived on their desk. That is why an engineering-side adoption program can succeed completely and change nothing a customer sees.
- **What to measure instead of velocity.** If the diagnosis holds, deployment velocity and PR throughput will keep improving while time-from-idea-to-customer stays flat, which is exactly the pattern that makes engineering leaders and product leaders disagree about whether adoption worked. The useful instrument is a lead-time breakdown by stage — decide, build, approve, launch — rather than another throughput metric on the build stage.
- Provenance: an unmeasured observation. "1 to two months," "9 to 12 months," and the two-month decision and approval figures are stated as characterizations of Amazon's own experience, with no per-stage lead-time data, no before-and-after comparison, and no example of a review process that was actually changed in response. Nothing here identifies which product categories the figures describe.

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Coding-Agent Capability Tiers Change the Bottleneck](coding-agent-capability-tiers-change-the-bottleneck.md)
- [Separate the Decision Layer From the Implementation Layer](separate-the-decision-layer-from-the-implementation-layer.md)
- [Make Code Review the Bottleneck Skill for AI-Generated Code](make-code-review-the-bottleneck-skill-for-ai-generated-code.md)
- [Measure Feature Adoption, Not Shipping Velocity](measure-feature-adoption-not-shipping-velocity.md)
- [Elicit Requirements as the Non-Automatable Bottleneck](elicit-requirements-as-the-non-automatable-bottleneck.md)
- [Stage Productivity Pilots to Strip One Confound at a Time](stage-productivity-pilots-to-strip-one-confound-at-a-time.md)

Sources:
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 18:45-19:56
