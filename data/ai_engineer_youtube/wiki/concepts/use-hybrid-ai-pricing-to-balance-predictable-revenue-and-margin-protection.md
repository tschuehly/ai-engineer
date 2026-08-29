# Use Hybrid AI Pricing to Balance Predictable Revenue and Margin Protection

Summary: Hybrid AI pricing combines a base fee with a scaling or usage fee so the company gets predictable revenue while heavy usage still pays for marginal compute. This pattern avoids the extremes of pure subscriptions and pure usage billing.

Use when:
- Pricing an AI feature whose power users can consume disproportionate compute.
- Designing packages that should invite experimentation without exposing the company to unlimited usage.

Details:
- Pure subscriptions create committed revenue but expose margins when a small group of power users consumes most compute; pure usage protects margins but can discourage customers from experimenting because invoices feel unpredictable.
- A hybrid model uses a base fee for the relationship and a scaling fee for additional value consumed, allowing normal users to start predictably while heavy users pay as they grow.
- Credits can keep customer-facing plans stable while internal feature-to-credit mappings change as premium capabilities become standard or new capabilities appear.
- **A worked credit architecture, and a case that is deliberately not hybrid.** Lovable's model as replicated on stage is "a credit-only pricing model where you auto-recharge on a monthly basis," with "multiple different types of credits that are scoped to different types of usage" and an invoice at period end "if you overspend" — no base subscription fee at all. The mechanism worth carrying is the scoping: separate pools for build, plan mode, cloud, and AI gateway credits stop one capability from silently consuming the budget a customer bought for another, which a single undifferentiated credit balance cannot do. Garvin also flags the administrative cost this creates — "relatively complicated to administer is the credit itself" — which is why Metronome makes the credit a first-class object rather than a balance field. ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 14:33-15:10, 15:34-15:41)
- **A second route to the same shape, from adoption rather than margin.** ChatGPT Enterprise launched at $60 per user per month, "priced according to how expensive it was for us to serve it," and was later restructured to "a license fee, a base fee to use the product, and then move to usage based." The reason given is not power-user margin exposure but the buyer's scoping decision: at $60 a seat, "organizations would come in and say, well, I'm only buying this for a subset of my team or only for my developers," and after the change "the barrier to entry went down… and then usage went up over time." Hybrid pricing is therefore two different arguments that happen to produce the same structure — protect the ceiling against heavy users, and remove the floor that caps deployment breadth. See [Price Under the Department Threshold So Adoption Can Spread](price-under-the-department-threshold-so-adoption-can-spread.md). ([Rosenthal](../sources/20260826_wdTRsfw0KG0.md), 09:06-10:19)

Related topics:
- [AI Monetization](../topics/ai-monetization.md)
- [Go To Market](../topics/go-to-market.md)

Related concepts:
- [Map AI charge metrics to customer-perceived value](map-ai-charge-metrics-to-customer-perceived-value.md)
- [Prevent AI billing surprises with caps, notifications, and rate limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md)
- [Per-Seat Pricing Loses Its Referent When One Agent Does the Work of Many Logins](per-seat-pricing-loses-its-referent-when-agents-do-the-work.md)
- [Price Under the Department Threshold So Adoption Can Spread](price-under-the-department-threshold-so-adoption-can-spread.md)

Sources:
- [Mastering AI Pricing: Flexible & Agile Monetization - Mayank Pant, Stripe](../sources/20260501_CrqPcIZOOXA.md), 01:44-02:23, 05:02-06:07, 11:36-13:03, 19:17-23:00
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 14:33-15:10, 15:34-15:41
- [Reverse-Engineering the AI Buyer — Aliisa Rosenthal, Acrew Capital](../sources/20260826_wdTRsfw0KG0.md), 09:06-10:19
