# Per-Seat Pricing Loses Its Referent When One Agent Does the Work of Many Logins

Summary: A seat price works because headcount is a usable proxy for how much work a customer extracts from a product. When one agent login performs the work of many humans, the proxy stops tracking value — not because seats are priced wrongly, but because the thing being counted no longer corresponds to the thing being sold.

Use when:
- Your product is being operated by an agent on a customer's behalf and seat counts have flattened or fallen while usage has not.
- Deciding whether to defend a per-seat model, add a usage or credit component, or move the metric entirely.
- Evaluating a competitor's price cut that appears irrational until you notice what they added alongside it.

Details:
- The named case: HubSpot, a Metronome customer "for the past couple of years," is "on a path to transform their entire business from a seat-based model to a credits-based model," beginning in EMEA, where "they have dramatically lowered their seats-based price and added on a credits-based model." The seat price falling and the credit model arriving are one move, not two. ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 10:42-10:59)
- The reasoning is about the metric's referent, not about margin: "what they need to be concerned about is a world in which an agent can operate their entire system. And in that world essentially paying for a seat level access to the product to perform your work is no longer important in some sense." (10:59-11:14)
- The industry term offered is "headlessness" — the product is still doing the work, but no human is sitting at it. Garvin notes Salesforce and others have used it and reports it as observed rather than forecast: "this is what Metronome is literally seeing today." (11:14-11:23)
- The structural consequence is concentration: "you have the possibility of essentially all of the value accruing to essentially one user of your platform, which in this case would be an agent." A seat model is a way of charging for distributed access, and it degrades exactly as access concentrates. (11:40-11:52)
- The supporting evidence is thin and should be labelled as such: at one demo day "all five of the demoing companies were sales-led agents meant to operate platforms like SAP or… invoicing platforms." Demo-day cohorts are selected for a thesis; this shows the pattern exists, not that it dominates. (11:23-11:40)
- What the market has converged on instead: a credits-based model, "dominant on the market since OpenAI launched their prepaid credit auto recharge model a couple of years ago." The concrete shape shown is credit-only with monthly auto-recharge, several credit pools each scoped to a different class of usage (build, plan mode, cloud, AI gateway), and overage invoiced at the end of the period. Scoping the pools is what stops one capability from silently consuming the budget for another. (12:03-12:15, 14:33-14:52, 15:34-15:41)
- Enterprise contracts are following the cloud-provider playbook rather than inventing one: "Cognition or Cursor or OpenAI, Anthropic themselves… are starting to adopt more commit structures like the CSPs have done for the past 10 years. Think having prepaid commitments, postpaid commitments, and specific types of offers for specific types of customers." (12:22-12:44)
- Counter-reading worth holding, which the source does not raise: an agent acts on behalf of some accountable party, so seats may be relocating to a different unit — an operator, a workflow, a team — rather than disappearing. The honest claim is that the *human login* has stopped being the right unit, not that consumption is the only remaining candidate. A hybrid base-plus-usage structure is the wiki's existing answer to the same pressure.
- Limit: the HubSpot transition is second-hand, in progress, geographically scoped ("starting in EMEA"), and reported with no revenue, retention, or customer-reaction outcome. It is a strategic direction chosen by a company with the same information you have, not a validated result.
- **An earlier and simpler way seats fail, recorded here so the two are not conflated.** Before any agent was operating anything, ChatGPT Enterprise's $60 per user per month broke for a purely human reason: the price sat above what a buyer would authorize company-wide, so "organizations would come in and say, well, I'm only buying this for a subset of my team or only for my developers… It's too expensive," and "once we lowered the threshold, it spread like wildfire" (09:56-10:19). That is a level problem, fixable by lowering the number; the headlessness argument on this page is a referent problem, which lowering the number does not fix. Rosenthal also reports the next objection already arriving — "usage is also getting pushed back on as companies are seeing cost of usage skyrocket" — with caps as the answer, which matches this page's credit-and-commit direction rather than contradicting it. See [Price Under the Department Threshold So Adoption Can Spread](price-under-the-department-threshold-so-adoption-can-spread.md). ([Rosenthal](../sources/20260826_wdTRsfw0KG0.md), 09:56-10:51)

Related topics:
- [AI Monetization](../topics/ai-monetization.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Separate Agent as Product, Agent as Buyer, and Agent as User](separate-agent-as-product-buyer-and-user.md)
- [Map AI Charge Metrics to Customer-Perceived Value](map-ai-charge-metrics-to-customer-perceived-value.md)
- [Use Hybrid AI Pricing to Balance Predictable Revenue and Margin Protection](use-hybrid-ai-pricing-to-balance-predictable-revenue-and-margin-protection.md)
- [Treat AI Pricing as a Fast-Moving Product Hypothesis](treat-ai-pricing-as-a-fast-moving-product-hypothesis.md)
- [Prevent AI Billing Surprises With Caps, Notifications, and Rate Limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md)
- [Price Under the Department Threshold So Adoption Can Spread](price-under-the-department-threshold-so-adoption-can-spread.md)

Sources:
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 10:36-11:52, 12:03-12:44, 14:33-15:41
- [Reverse-Engineering the AI Buyer — Aliisa Rosenthal, Acrew Capital](../sources/20260826_wdTRsfw0KG0.md), 09:56-10:51
