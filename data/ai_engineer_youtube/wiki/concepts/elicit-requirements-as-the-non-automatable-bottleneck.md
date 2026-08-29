# Elicit Requirements as the Non-Automatable Bottleneck

Summary: When AI makes code, specs, and tests cheap to produce, the scarce, still-human work moves upstream to eliciting the real requirements — getting the right stakeholders in the room and naming what is actually worth building. You can prompt your AI, but "you can't prompt the room."

Use when:
- Deciding where to invest scarce senior/expert attention now that implementation is cheap.
- Diagnosing why AI-accelerated teams ship fast but build low-value or unused things.
- Justifying discovery/requirements work against pressure to jump straight to prompting.

Details:
- The delivery bottleneck shifted: getting access to code and being able to build is no longer the constraint; the constraint is accessing stakeholders and decision-makers and spending time eliciting requirements — figuring out what should be built. You can prompt code, AI, and a whole specification, but not the room. (02:15-03:00)
- Evidence: a VisualLabs internal hackathon generated ~21 agent ideas and abandoned 17 — not for technology reasons but because they created no business value (no data access, no clear business owner, or it just didn't make sense). The 4 that survived run in production and materially changed how the team works. (00:37-01:30)
- Naive AI use replicates what already exists because a model "by definition is coded to give you the most common answers" — the Henry Ford "faster horse" trap. A human must read the room and name the problem precisely to move AI off the average and toward a step-change ("a car a magnitude shift better"). (03:10-04:20)
- The remedy is an old trade with new economics: "isn't this just good old product management?" — yes; everyone has the same models and tools, so the differentiator is who understands the business need better. (10:50-11:40)
- Operational consequence: move upstream. Pre-boom the smartest people wrote code; now shift subject-matter experts toward customers and business problems and spend more time deciding what to build, "because that's the expensive part. Building it has actually become very cheap." Don't require everyone to become a PM — just include their experience in the decision of what to build. (12:35-14:00)
- **The same boundary drawn from the agent's side, as a rule about what is left to say.** "Anything that's in code, any fact that's in code, the agents can figure out by reading the code. What's left are the things that are not in code" — the political constraints, the vendor deal that forces a database choice, the preference nobody wrote down. That is a sharper statement of this page's claim than "requirements are hard": it says the non-automatable input is defined by exclusion, and it shrinks as retrieval improves. It also gives elicitation a concrete output format, since the residue is what belongs in the shared session or document rather than in a spec that restates the codebase. See [tell the agent only what is not recoverable from the code](tell-the-agent-only-what-is-not-recoverable-from-the-code.md). ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 14:01-14:30)

- **The organizational scale-up of the same claim: not just requirements, but the approvals around them.** Once "the code only takes 1 to two months to write," Amazon finds "the speed of decision-making becomes a new bottleneck," and the arithmetic is the argument: "when it used to take 9 to 12 months to build a new product, it didn't matter so much in the overall wash of things if it took two months to make the decision to build the product and then two months to approve the launch. But now those are the bottlenecks. Those are the long pole." The observable Liguori offers is a ratio anyone can check — "frontier engineering teams spend more time making decisions than they do writing code" — and her prescription sorts by reversibility rather than removing review: "the more that you can make fast decisions, especially ones that are easy to be reversed, the better." See [When Code Stops Being the Long Pole, Approvals Become It](when-code-stops-being-the-long-pole-approvals-become-it.md). Unmeasured; no per-stage lead-time data is given. ([Liguori](../sources/20260828_pqlWNihgdjI.md), 18:45-19:56)

Related topics:
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Capture AI-Build Requirements With Story Maps and User Stories](capture-ai-build-requirements-with-story-maps-and-user-stories.md)
- [Measure Feature Adoption, Not Shipping Velocity](measure-feature-adoption-not-shipping-velocity.md)
- [AI-amplified shipping speed needs stronger product taste](ai-amplified-shipping-speed-needs-stronger-product-taste.md)
- [Product Engineers Need Direct Customer Context](product-engineers-need-direct-customer-context.md)
- [Tell the Agent Only What Is Not Recoverable From the Code](tell-the-agent-only-what-is-not-recoverable-from-the-code.md)
- [When Code Stops Being the Long Pole, Approvals Become It](when-code-stops-being-the-long-pole-approvals-become-it.md)

Sources:
- [You Can't Prompt the Room: The Last Skill AI Won't Replace - Balázs Horváth, VisualLabs](../sources/20260629_6bmM45jkMDY.md), 00:37-14:00
- [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../sources/20260808_iQ5xldZ9StU.md), 14:01-14:30
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 18:45-19:56
