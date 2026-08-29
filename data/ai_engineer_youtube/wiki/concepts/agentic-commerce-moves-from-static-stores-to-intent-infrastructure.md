# Agentic Commerce Moves From Static Stores to Intent Infrastructure

Summary: Agentic commerce treats buyers, sellers, and the transaction protocol as AI-mediated participants rather than assuming users browse static product pages. The durable design shift is from page navigation toward explicit buying and selling intent that agents can reason over.

Use when:
- Designing shopping, procurement, marketplace, or checkout workflows for AI agents.
- Deciding whether a commerce agent should browse a website, call a product API, or negotiate against higher-level intent.

Details:
- Behrens defines a store as both a location and a protocol for facilitating transactions among merchants and buyers, then argues that AI digitizes the participants and their interactions rather than only the merchandise and distribution. (01:58-02:47)
- The agentic commerce stack changes static websites into merchant agents, consumer browsing into consumer agents, and low-level payment infrastructure into higher-level intent infrastructure while still optimizing for transactions. (02:21-02:47)
- Buyer intent can be explicitly captured from conversations or by asking a user agent, rather than inferred only from keyword searches, click data, and site metrics. (06:23-06:50)
- The hard product problem is resolving fuzzy intent such as "running shoes" into SKU-level inventory and transaction-ready options without forcing the user to provide a product-detail-page URL first. (06:57-07:18)
- Seller intent also becomes dynamic: merchants may expose realtime availability, contextual pricing, inline discounts, and bundles across merchants instead of only static product detail pages. (07:49-08:20)
- **The B2B mirror, where the agent procures infrastructure rather than goods.** Garvin separates the two markets explicitly — B2C is "agentic commerce," while in the Metronome case "we're talking about in a B2B context" — and the B2B transaction shown is an agent "literally procuring their initial Stripe instance as well as additional backend services" through a CLI. The seller-side obligation is the same discoverability problem in a different medium: "make your services discoverable to agents that may be building an application or working in the open web," with Vercel and Hugging Face named as providers onboarding into that environment. ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 10:07-10:33, 17:14-17:31)

Related topics:
- [Agents](../topics/agents.md)
- [Product Strategy](../topics/product-strategy.md)
- [AI Monetization](../topics/ai-monetization.md)

Related concepts:
- [Measure AI intensity by human input to valuable output](measure-ai-intensity-by-human-input-to-valuable-output.md)
- [Agent Experience Means Autonomous Access, Understanding, and Operation](agent-experience-means-autonomous-access-understanding-and-operation.md)
- [Turn AI Product Intents Into Contained Workflows](turn-ai-product-intents-into-contained-workflows.md)
- [Separate Agent as Product, Agent as Buyer, and Agent as User](separate-agent-as-product-buyer-and-user.md)

Sources:
- [Machines of Buying and Selling Grace - Adam Behrens, New Generation](../sources/20250723_zlZz0mDF2eg.md), 01:58-02:47, 06:23-08:20
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 10:07-10:33, 17:14-17:31
