# Simulate AI Pricing Against Usage Data Before Launch

Summary: AI pricing should be tested against real or beta usage before launch so teams can compare revenue, customer impact, and packaging risk. Simulations turn pricing from guesswork into a measured product decision.

Use when:
- Preparing to launch a new AI agent or AI feature with uncertain usage patterns.
- Comparing add-on, token, tiered, included-usage, or hybrid pricing scenarios before customers are billed.

Details:
- Closed-beta "shell" pricing can instrument usage and model alternate charges without actually billing customers, giving teams evidence before launch. (12:19-13:23)
- A pricing simulation should run over a defined time window and customer cohort, such as beta users or existing customers moving from an older package. (13:29-13:58)
- Useful simulation outputs include top-line revenue impact, average change for existing customers, revenue mix, scatter plots of percentage change versus revenue impact, and exportable per-customer impact data. (14:54-16:25)
- Pricing simulation is especially relevant for AI agent products because their usage distribution and outcome value may not be visible from a static price page. (12:40-13:23)
- **A cheaper predecessor step, and the boundary between the two.** Before simulating against historical volumes, an agent can stand up a populated sandbox in minutes: provisioned customer, seeded usage, and a rendered draft invoice, from one natural-language instruction. That answers whether the model was *built* as intended — the right pools, the right drawdown, the right overage behaviour. It does not answer what the model earns, because the usage is invented: "you can see the usage that we plopped in. All obviously in a production environment, you would be seeing this against real usage that you have." Structure check first against synthetic data, economics second against real data; conflating them is how a correct-looking invoice becomes a revenue forecast. ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 07:53-08:19, 15:14-15:32)

Related topics:
- [AI Monetization](../topics/ai-monetization.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Treat AI pricing as a fast-moving product hypothesis](treat-ai-pricing-as-a-fast-moving-product-hypothesis.md)
- [Map AI charge metrics to customer-perceived value](map-ai-charge-metrics-to-customer-perceived-value.md)
- [Seed the Agent-Built Sandbox With Usage, Not Just Objects](seed-the-agent-built-sandbox-with-usage-not-just-objects.md)

Sources:
- [Monetizing AI - Alvaro Morales, Orb](../sources/20250723_6WQYLQB0odc.md), 11:19-16:43
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 07:53-08:19, 15:14-15:32
