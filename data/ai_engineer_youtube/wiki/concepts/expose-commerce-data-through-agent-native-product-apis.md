# Expose Commerce Data Through Agent-Native Product APIs

Summary: Commerce agents need current, structured product access that is better than scraping pages or negotiating one-off product feeds with every merchant. A unified product-data API or MCP server can turn messy merchant catalogs into an agent-native interface for discovery and checkout.

Use when:
- Building merchant, marketplace, retail, procurement, or shopping-agent integrations.
- Choosing between browser automation, scraping, product feeds, APIs, and MCP for commerce workflows.

Details:
- Behrens presents two agent-shopping futures: agents can operate websites, or they can use programmatic access through MCP servers and APIs. (03:17-04:31)
- In the programmatic path, an API endpoint can reason over the request, return generated UI elements, and let the purchase hit an API endpoint instead of forcing an agent through a website checkout flow. (04:03-04:31)
- Existing product-feed infrastructure requires chat products to work individually with each merchant, while scraping repeats integration work and can clog websites with bot traffic. (08:39-09:09)
- New Generation's proposed pattern is a unified API for product data across merchants, analogous to aggregating financial institutions through a service such as Plaid. (09:12-09:28)
- The Samsung implementation example abstracts multiple product verticals and inventory representations into a consistent API with cohesive endpoints that can work across merchants. (12:49-13:21)
- **Discoverability is becoming a marketplace position, not only an API property.** Garvin reports providers queuing to be reachable from inside someone else's agent workflow: "there are a number of different providers that are onboarding every day… companies like Vercel, like Hugging Face etc are basically working in Stripe Projects environment to be able to make their own products more discoverable to agents that are operating Stripe's system." Being agent-native is necessary but no longer sufficient — the agent has to encounter you at the moment it is assembling a stack, which turns integration into a distribution decision about whose orchestrator you appear in. ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 10:17-10:26, 17:14-17:31)
- **The two largest assistant surfaces chose the feed anyway, and not for legacy reasons.** Prio reports that "both ACP and UCP right now, so Gemini and ChatGPT, does not support that search catalog call. They want you to send that feed to them," motivated by query-time fan-out ("if you have M number of merchants and N number of products, now it has to call that many") and by ranking economics ("sponsored products, retail media related things"). That qualifies this page's framing of feeds as the inferior legacy path: a unified product API is valuable to the *merchant* as the one place to fan out N aggregator schemas from, but it does not remove the feed, because the aggregator wants the index in its own hands. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 08:35-09:19)

Related topics:
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Settle Agent Payments Over HTTP With 402 and Checkout Protocols](settle-agent-payments-over-http-with-402-and-checkout-protocols.md)
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Use Browser UI Control When APIs Are Absent](use-browser-ui-control-when-apis-are-absent.md)
- [AI-Native Search APIs Serve Agent Query Shapes](ai-native-search-apis-serve-agent-query-shapes.md)
- [Separate Agent as Product, Agent as Buyer, and Agent as User](separate-agent-as-product-buyer-and-user.md)
- [Push a Product Feed, Because Per-Merchant Catalog Search Does Not Scale](push-a-product-feed-because-catalog-search-does-not-scale.md)

Sources:
- [Machines of Buying and Selling Grace - Adam Behrens, New Generation](../sources/20250723_zlZz0mDF2eg.md), 03:17-04:31, 08:39-09:28, 12:49-13:21
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 10:17-10:26, 17:14-17:31
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 08:35-09:19
