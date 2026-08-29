# Ship Self-Serve Before the Enterprise Tier

Summary: Build the self-serve product first, learn from what it fails to cover, and derive the enterprise tier from that evidence. Shipping enterprise first means specifying it from the segment that happened to be loud enough to reach you, and the self-serve product that follows will compete with it rather than feed it.

Use when:
- Deciding what to build first for a product that has both individual and organizational buyers.
- Enterprise inbound is arriving before you have a paid product, and it is telling you what to build.
- A self-serve launch is being deferred until "after enterprise is stable."
- Sales reps are competing with a cheaper tier of the same product.

Details:
- **The worked failure.** ChatGPT launched at the end of 2022 "with no enterprise features whatsoever." The inbound was specific — "Can I get SSO? Can I get an NDA? Can I get an invoice?" — and approval to build came "9 months later." ([Rosenthal](../sources/20260826_wdTRsfw0KG0.md), 01:49-02:25)
- **The sampling bias is the mechanism, and it generalizes past sales.** "Over that 9-month time, the companies that had been the loudest, the companies that had gotten to me, were the bigger companies, were the large enterprises. So, I thought, 'Okay, we should go out and build a really high-end product for all these enterprises that want to use us.'" The requirements set was drawn from whoever had the org chart, the persistence, and the introductions to reach one person — a sample selected by ability to reach you, not by size of opportunity. The result: "We added every bell and whistle. We made it lightning fast. It was a very expensive product… We went way up market right out the gate." (02:25-02:59)
- **What the self-serve launch revealed four months later.** "We released our self-serve motion in January of 2024, so about 4 months after our enterprise version, and it just completely cannibalized our enterprise business. It grew so much faster. It turns out most people just didn't want to talk to a salesperson." The demand the loud segment had masked was a preference for *no sales contact at all*, which no amount of listening to enterprise inbound could have surfaced. (02:59-03:37)
- **The organizational damage is separate from the revenue damage.** "It frustrated the sales reps cuz now they had to compete with self-serve. It sort of cannibalized the customer base. They sometimes preferred to just move into the cheaper self-serve option." Launching in the wrong order does not just misprioritize engineering; it puts two of your own motions into competition after you have already hired against one of them. (03:20-03:37)
- **The corrected sequence, which became policy.** "We should have launched with self-serve first, listen to feedback from our customers and what they weren't getting from the self-serve product, and then figured out how to build a more expensive enterprise offering, and then hire the team to sell it… For every other product we launched at OpenAI, we made sure to do it self-serve first, learn where we needed to tack on humans and add them." Four ordered steps: self-serve, observed gaps, enterprise tier, sales team. (03:37-04:14)
- **This is the sourced resolution to a tension the wiki previously marked as inference.** [Self-Serve Onboarding Is a Precondition for Agent Recommendation](self-serve-onboarding-is-a-precondition-for-agent-recommendation.md) argues that demo-gated evaluation removes you from an agent's answer set, and explicitly flags that its proposed resolution — keep the sales motion but ensure a complete self-serve path exists alongside it — was not sourced. This page supplies it from the other direction, and adds an ordering the earlier page did not have: not merely *alongside*, but *first*, with the enterprise tier specified from what self-serve usage reveals.
- **The counter-case this does not cover.** OpenAI's self-serve motion grew into consumer-scale inbound demand for a product people had already heard of. A company with no brand may get nothing from a self-serve launch to learn from, in which case the enterprise conversations are the only signal available. The talk does not address this, and the recommendation is a counterfactual asserted rather than tested — the enterprise launch plausibly contributed to the awareness that made self-serve grow. Treat the transferable part as the diagnosis (requirements sampled from who can reach you are biased upmarket) rather than the universal rule.
- **The related trap named in the same talk.** "Avoid the pull upmarket as long as you can resist it because once you get a big customer, they'll come and they'll say, 'I can spend a million dollars, 10 million dollars with you.' And it's very tempting to want to orient your whole business around that. They will take so many of your legal, security, product, engineering, sales resources. So, you want to be really, really picky about who those first big enterprise partners are." The pull upmarket and the enterprise-first launch are the same error at different times. (11:25-11:57)

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Go To Market](../topics/go-to-market.md)
- [AI Monetization](../topics/ai-monetization.md)

Related concepts:
- [Self-Serve Onboarding Is a Precondition for Agent Recommendation](self-serve-onboarding-is-a-precondition-for-agent-recommendation.md)
- [Build the Automated Motion First and Hire Into Its Bottlenecks](build-the-automated-motion-first-and-hire-into-its-bottlenecks.md)
- [Price Under the Department Threshold So Adoption Can Spread](price-under-the-department-threshold-so-adoption-can-spread.md)
- [Reply to Every Inbound and Over-Capture at Signup](reply-to-every-inbound-and-over-capture-at-signup.md)
- [Treat a Pilot as a Second Sales Process You Run for Free](treat-a-pilot-as-a-second-sales-process-you-run-for-free.md)
- [Ship Continuously Viable Product Shapes](ship-continuously-viable-product-shapes.md)
- [Gate Each Rollout Phase on a Different Question](gate-each-rollout-phase-on-a-different-question.md)
- [Scarce Human Contact Appreciates as the Funnel Automates](scarce-human-contact-appreciates-as-the-funnel-automates.md)
- [Layer Ask, Push, and Self-Serve Because Teams Interface Differently](layer-ask-push-and-self-serve-because-teams-interface-differently.md)
- [Use Design Partner Evidence To Support Early AI Startup Scale](use-design-partner-evidence-to-support-early-ai-startup-scale.md)

Sources:
- [Reverse-Engineering the AI Buyer — Aliisa Rosenthal, Acrew Capital](../sources/20260826_wdTRsfw0KG0.md), 01:49-04:14, 11:25-11:57
