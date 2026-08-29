# Gateway Platform Primitives Let Teams Focus on MCP Business Logic

Summary: Shared gateway primitives let domain teams create MCP servers without reimplementing auth, routing, deployment, observability, credentials, and scaling. The domain server can focus on workflow policy and business logic while the platform enforces common enterprise controls.

Use when:
- Legal, finance, observability, or other domain teams need to build MCP workflows without owning platform security.
- Standardizing MCP server creation with a CLI, subregistry, proxy, tunnel, and role-based access controls.

Details:
- A gateway can give new MCP servers auth, role-based access control, proxy routing, secure tunnels, an internal subregistry, and a developer CLI. (08:28-09:33)
- Once these primitives exist, a legal-team MCP server can focus on contract review, redlining, and escalation behavior rather than who can access it, how often it is used, whether it scales, or whether new agents can connect. (07:37-08:26)
- A gateway CLI can make MCP server creation understandable to the coding agent a team is using, so teams integrate with shared primitives and focus on the server-specific workflow. (09:14-09:48)
- Standard primitives can encode enterprise operating procedures by defining expected tools, forbidden tools, and required behavior for agents and MCP servers. (13:30-14:03)
- Anthropic's gateway pattern frames the platform primitive as a pit of success: if engineers get a simple `connect to MCP` call that handles internal and external routing, stored credentials, authentication flows, rate limits, and observability, teams can build integrations once and reuse them across products instead of reimplementing custom endpoints and OAuth flows. 01:24-02:37, 07:50-08:51, 11:18-12:09
- **The same primitive set at DoorDash, with eval added as a peer rather than a downstream concern.** Their platform is an LLM gateway "where you can easily switch between different models," an agent gateway "where you can connect to tools and other agents" that solves "authentication, agent identity and other things in a central place which our security team can bless," open-weights model hosting paired with the LLM gateway because "cost is a number one concern these days" — and then "the fourth pillar is eval." Filing evaluation alongside routing and auth rather than beneath them is the structural claim: the same argument that centralizes credentials centralizes traces, scores, and judges. ([AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 01:20-02:11)
- **The primitives arrive with a dependency attached, and it is worth pricing.** Manuja's reminder is that after a platform absorbs auth, routing, rate limits, and fallback, "we are actually adding another dependency in the request path itself." His stronger version is that one deployment serving an entire company "is a single point of failure," and that what organizations usually want from it is governance rather than shared traffic — "do not try to centralize your traffic, but you can have plugins, you can have custom code that can centralize your governance." Shared *primitives* and a shared *deployment* are separable, and the argument for the first does not carry the second. ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 12:58-15:42)

Related topics:
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [MCP gateways create an enterprise root of trust](mcp-gateways-create-an-enterprise-root-of-trust.md)
- [Carry MCP JSON-RPC Over Internal Transports](carry-mcp-json-rpc-over-internal-transports.md)
- [Move the Platform's Primary Surface as Its Users Gain Tools](move-the-platforms-primary-surface-as-its-users-gain-tools.md)
- [Decentralize the Gateway, Centralize the Governance](decentralize-the-gateway-centralize-the-governance.md)

Sources:
- [Gateways are All You Need - Karan Sampath, Anthropic](../sources/20260427_CD6R4Wf3jnY.md), 07:37-14:03
- [Remote MCPs: What we learned from shipping - John Welsh, Anthropic](../sources/20250619_0NHCyq8bBcM.md), 01:24-02:37, 07:50-08:51, 11:18-12:09
- [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 01:20-02:11
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 12:58-15:42
