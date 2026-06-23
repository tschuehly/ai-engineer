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

Related topics:
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Settle Agent Payments Over HTTP With 402 and Checkout Protocols](settle-agent-payments-over-http-with-402-and-checkout-protocols.md)
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Use Browser UI Control When APIs Are Absent](use-browser-ui-control-when-apis-are-absent.md)
- [AI-Native Search APIs Serve Agent Query Shapes](ai-native-search-apis-serve-agent-query-shapes.md)

Sources:
- [Machines of Buying and Selling Grace - Adam Behrens, New Generation](../sources/20250723_zlZz0mDF2eg.md), 03:17-04:31, 08:39-09:28, 12:49-13:21
