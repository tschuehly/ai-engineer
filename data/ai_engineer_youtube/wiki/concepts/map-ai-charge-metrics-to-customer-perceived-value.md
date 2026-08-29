# Map AI Charge Metrics to Customer-Perceived Value

Summary: AI pricing should expose charge metrics that customers understand as value, not only technical units such as tokens or API calls. The right billable unit depends on whether the product automates work, augments quality, provides enhanced access, or produces business outcomes.

Use when:
- Choosing between token/API pricing, workflow units, credits, and outcome-based pricing.
- Translating product capabilities into packaging that sales, finance, and customers can reason about.

Details:
- Technical units are easiest for infrastructure providers but can overwhelm product customers; a presentation tool customer may care about decks or slides produced, not underlying API calls.
- Charge metrics can be consumption-based, workflow-based, or outcome-based: API calls align with provider cost, generated images or summarized documents align with product use, and hires or qualified leads align with customer ROI.
- Outcome-based pricing is easier to sell but harder to attribute; consumption pricing is easier to implement but farther from customer value, so teams need data to justify where they land.
- Credits can abstract multiple features into a customer-facing currency while allowing internal mappings to evolve as model costs and feature value change.
- GenAI productivity can weaken seat count as a proxy for value: if one employee can do far more work with AI, pricing by employees may diverge from the work or business value produced. (21:20-22:24)
- Agent pricing can be placed on a spectrum from resource units such as tokens, through workflow steps and whole workflows, to labor-replacement units and measured outcomes. Outcome pricing is strongest when both parties agree on the outcome definition and can measure it objectively. (05:54-09:35)
- **A metric can stop referring to anything, which is worse than being misaligned.** Seats are a proxy: they count humans as a stand-in for how much work a customer extracts. Garvin's argument is that an agent operating the whole system severs the proxy from the thing it stood for — "paying for a seat level access to the product to perform your work is no longer important in some sense" — with value "accruing to essentially one user of your platform, which in this case would be an agent." The diagnostic that separates this from ordinary misalignment: usage grows while the metric stays flat, so no amount of re-pricing the seat recovers the relationship. ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 10:59-11:52)

Related topics:
- [AI Monetization](../topics/ai-monetization.md)

Related concepts:
- [Treat AI pricing as a fast-moving product hypothesis](treat-ai-pricing-as-a-fast-moving-product-hypothesis.md)
- [Use hybrid AI pricing to balance predictable revenue and margin protection](use-hybrid-ai-pricing-to-balance-predictable-revenue-and-margin-protection.md)
- [Choose direct or indirect AI monetization](choose-direct-or-indirect-ai-monetization.md)
- [Per-Seat Pricing Loses Its Referent When One Agent Does the Work of Many Logins](per-seat-pricing-loses-its-referent-when-agents-do-the-work.md)

Sources:
- [Mastering AI Pricing: Flexible & Agile Monetization - Mayank Pant, Stripe](../sources/20260501_CrqPcIZOOXA.md), 02:32-03:17, 06:24-11:34
- [Small Bets, Big Impact Building GenBI at a Fortune 100 - Asaf Bord, Northwestern Mutual](../sources/20251223_LU9KgcZDRfY.md), 21:20-22:24
- [Monetizing AI - Alvaro Morales, Orb](../sources/20250723_6WQYLQB0odc.md), 05:54-09:35
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 10:59-11:52
