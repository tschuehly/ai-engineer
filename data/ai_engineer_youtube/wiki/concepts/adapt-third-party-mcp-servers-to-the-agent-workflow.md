# Adapt Third-Party MCP Servers to the Agent Workflow

Summary: Public MCP servers should be treated as generic integration code that may need curation before an agent uses it in production. The right tool surface depends on the workflow, not only on what the upstream server exposes.

Use when:
- Connecting a public MCP server such as Playwright to a specific agent product.
- Reviewing why adding more tools made an agent less reliable.

Details:
- Third-party agent tools may come from MCP servers, libraries, or copied integration code; the common issue is that they were written by another team without knowledge of the local architecture or workflow. 02:07-02:51
- The out-of-the-box Playwright MCP server exposed 21 browser tools with generic descriptions, which made sense for a general browser integration but not for a spec-review agent. 10:39-12:22
- A baseline run failed by navigating to a made-up route and producing poor evidence, showing that adding a generic tool catalog can degrade behavior before it improves capability. 13:13-14:12
- Curation can remove irrelevant or risky tools such as resize, drag, or browser code execution; in the demo this reduced the surface from 21 tools to 16 and gave the agent less to choose from. 15:47-18:02
- Tool curation trades context reduction against capability: some adaptations remove context, while other adaptations add longer descriptions or new tools when that improves task fit. 17:39-18:02, 39:35-40:17
- **The same adaptation problem seen from the server author's side of the boundary.** Figma could not assume any client behaviour it had not verified, so it reimplemented three spec features through tool results: server instructions became text appended to every tool call, elicitation became a returned prompt asking the user's permission, and sampling became a returned prompt telling the agent to scan the codebase and report matches "in a specified format… in bulk." Both sides end up writing adapters, and the cost is symmetrical — the server gives up a protocol guarantee in exchange for model compliance, exactly as an adapting client gives up the server's intended semantics. ([Lumarie](../sources/20260828_ZIYYsAzaLlA.md), 09:48-12:03)

- **The other thing a stable MCP surface buys: a replaceable implementation underneath it.** Adapting a third-party server is the usual reason to care about this boundary; Šteimantas' checkout stage shows the inverse benefit. Keeping Playwright MCP as the interface let a hardened remote browser replace the local one "as a drop in replacement," with the agent, prompts, and tool definitions untouched, which turned "our browser keeps getting blocked" from a rewrite into a procurement decision. See [Keep a Protocol Boundary So the Browser Backend Stays Swappable](keep-a-protocol-boundary-so-the-browser-backend-stays-swappable.md). ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 11:54-13:20)

Related topics:
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Secure MCP Servers by Shrinking the Agent-Visible Surface](secure-mcp-servers-by-shrinking-the-agent-visible-surface.md)
- [MCP Tool Surfaces Need Default Context Budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Wrap Generic Tool Descriptions With Use-Case Guidance](wrap-generic-tool-descriptions-with-use-case-guidance.md)
- [Tools Are the Only Primitive Every Client Implements](tools-are-the-only-primitive-every-client-implements.md)
- [Keep a Protocol Boundary So the Browser Backend Stays Swappable](keep-a-protocol-boundary-so-the-browser-backend-stays-swappable.md)

Sources:
- [Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz](../sources/20260408_U00AOI1eJUE.md), 02:07-18:02
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 09:48-12:03
- [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](../sources/20260826_XsvUhpnHepE.md), 11:54-13:20
