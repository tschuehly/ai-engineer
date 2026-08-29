# MCP Gateways Create an Enterprise Root of Trust

Summary: An MCP gateway is a shared middle layer between MCP clients and many MCP servers that centralizes authentication, authorization, observability, secure connectivity, and deployment. Use it when decentralized MCP development is blocked by security review, opaque usage, or inconsistent access control.

Use when:
- Scaling MCP beyond a few approved servers across many enterprise teams.
- Giving security teams one trusted control point while letting domain teams build business-specific MCP servers.

Details:
- Enterprises struggle with MCP table stakes such as knowing who uses each tool, which tools are failing, which users should have access, and whether servers prevent data exfiltration or harmful tool use. (01:42-03:20)
- Registries help discovery but do not provide the enterprise layer for authentication, access control, observability, and credential management. (03:20-04:07)
- A gateway acts as a middle layer between many MCP servers and any MCP client, supplying authorization, authentication, observability, secure connectivity, and deployment support. (06:52-07:49)
- Security teams can bless one platform as the root of trust while MCP servers treat the gateway as the only trusted endpoint. (06:01-06:31, 08:51-09:08)
- Anthropic's remote-MCP gateway example adds an internal adoption pattern: make `connect to MCP` the easy path, route by URL to internal or external servers, centralize credential management, rate limiting, and observability, and return a normal MCP SDK client session so protocol features roll out through ordinary package updates. 07:50-09:43
- A gateway also becomes a central inspection point for model-bound context: standardized MCP messages let teams hook policy, malicious-server blocking, content classification, audit, tool-execution processors, tool-definition processors, and resource management into one stream. 12:39-14:05
- **Where the gateway sits in one org-scale stack sketch.** Touil's enablement layer places an MCP gateway "to manage and simplify all of the MCP tools across your organization" beside a model gateway that manages and optimizes across locally run open-source and frontier models, an environment sandbox, a knowledge graph abstracting "your IT core systems, your codebase, your skills registry," and a workflow marketplace. ([Touil](../sources/20260828_M05vON8i0aI.md), 01:22-02:06) The sketch is useful mainly for what it puts *next to* the gateway: a skills registry as a peer control point rather than something the gateway covers, which matches his later argument that skills carry scripts and need their own checking pipeline. A slide taxonomy, not a deployed architecture.
- **A root of trust is also a blast radius, and the two roles can be split.** Manuja's position is that a company-wide gateway "is a single point of failure," and that most teams asking for one "want centralized governance" rather than centralized traffic — a distinction that maps cleanly onto this page, since trust anchoring, policy, and audit are governance concerns while request forwarding is not. His prescription — plugins or shared code enforcing common policy across many deployments, "managed by a single team" but not "a single deployment for the entire company" — preserves the root of trust while removing the shared failure domain, at the cost of policy-version drift across the fleet. ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 14:34-15:42)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Cross-app access centralizes MCP authentication through the identity provider](cross-app-access-centralizes-mcp-authentication-through-the-identity-provider.md)
- [Filter MCP tools by scopes and step-up authorization](filter-mcp-tools-by-scopes-and-step-up-authorization.md)
- [Stateless remote MCP servers rebuild allowed tools per request](stateless-remote-mcp-servers-rebuild-allowed-tools-per-request.md)
- [Carry MCP JSON-RPC Over Internal Transports](carry-mcp-json-rpc-over-internal-transports.md)
- [Skills Are the Residual Where Organizational Know-How Lands](skills-are-the-residual-where-organizational-know-how-lands.md)
- [Decentralize the Gateway, Centralize the Governance](decentralize-the-gateway-centralize-the-governance.md)

Sources:
- [Gateways are All You Need - Karan Sampath, Anthropic](../sources/20260427_CD6R4Wf3jnY.md), 01:42-09:08
- [Remote MCPs: What we learned from shipping - John Welsh, Anthropic](../sources/20250619_0NHCyq8bBcM.md), 07:50-09:43, 12:39-14:05
- [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../sources/20260828_M05vON8i0aI.md), 01:22-02:06
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 14:34-15:42
