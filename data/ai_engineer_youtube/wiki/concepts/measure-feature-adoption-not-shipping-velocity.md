# Measure Feature Adoption, Not Shipping Velocity

Summary: When AI makes shipping cheap, "features shipped" stops being a useful success metric. Track whether shipped features are actually reused — features used more than twice, and the frequency of a target activity — and treat demos-as-deliverables and untested PRDs as anti-patterns.

Use when:
- Choosing delivery KPIs for an AI-accelerated team.
- Auditing whether high shipping velocity is producing real adoption or just feature sprawl.
- Reviewing whether an agent/feature is ready to count as a win.

Details:
- Replace "number of features shipped last quarter" with "number of features shipped that is actually used more than twice" — a better KPI once implementation is cheap and shipping is no longer scarce. (13:20-14:00)
- Building-the-wrong-thing looks like high shipping velocity with poor adoption: people log into the newest thing but don't reuse it. Watch the frequency of a certain activity, not time-of-usage or time-on-site (those can look healthy while nothing is being reused). (11:40-12:20)
- Anti-pattern — "the demo is the deliverable": a demo is fast to build and looks nice, but "the demo system is not a live system"; the goal is production usage, not a good-looking demo. (12:20-12:35)
- Anti-pattern — a PRD with no real user testers: shipping into a live environment without gathering proper end-user testing tends to produce features people won't use. (12:00-12:20)
- Root-cause evidence: a VisualLabs hackathon abandoned 17 of 21 agent ideas for lack of business value (no data access, no owner, no measurable value); the surviving 4 earned production use — the same value/adoption filter applied before and after building. (00:37-01:30)

Related topics:
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Elicit Requirements as the Non-Automatable Bottleneck](elicit-requirements-as-the-non-automatable-bottleneck.md)
- [Capture AI-Build Requirements With Story Maps and User Stories](capture-ai-build-requirements-with-story-maps-and-user-stories.md)
- [AI-amplified shipping speed needs stronger product taste](ai-amplified-shipping-speed-needs-stronger-product-taste.md)
- [Optimize Onboarding Around One Aha Moment](optimize-onboarding-around-one-aha-moment.md)

Sources:
- [You Can't Prompt the Room: The Last Skill AI Won't Replace - Balázs Horváth, VisualLabs](../sources/20260629_6bmM45jkMDY.md), 00:37-14:00
