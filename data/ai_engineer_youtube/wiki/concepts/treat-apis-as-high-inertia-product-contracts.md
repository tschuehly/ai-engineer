# Treat APIs as High-Inertia Product Contracts

Summary: APIs and data structures become external product contracts once shipped, so early platform iteration needs especially trusted users and careful contract design.

Use when:
- Designing developer-platform APIs or agent-facing tool contracts.
- Deciding whether a platform abstraction is ready for broad release.

Details:
- Auchenberg argues APIs are harder than UI because moving a button is easier than changing a shipped API or data structure that customer systems depend on. 10:54-11:24
- Platform teams should work with a small discerning user set before broad release so the contract can be tested with people who can provide detailed integration feedback. 11:14-11:38
- A provider-side afternoon API change can become a six-month customer migration, which makes early feedback and contract caution more important for platforms than for many UI changes. 11:38-11:51

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent Experience Prioritizes APIs, CLIs, and MCP Over Dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Avoid Premature Low-Level AI System Coupling](avoid-premature-low-level-ai-system-coupling.md)

Sources:
- [Shipping something to someone always wins - Kenneth Auchenberg (ex. Stripe, VSCode)](../sources/20250728_mHzJhXppwUA.md), 10:54-11:51
