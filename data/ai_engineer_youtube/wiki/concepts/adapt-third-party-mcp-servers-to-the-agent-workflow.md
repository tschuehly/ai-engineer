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

Related topics:
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Secure MCP Servers by Shrinking the Agent-Visible Surface](secure-mcp-servers-by-shrinking-the-agent-visible-surface.md)
- [MCP Tool Surfaces Need Default Context Budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Wrap Generic Tool Descriptions With Use-Case Guidance](wrap-generic-tool-descriptions-with-use-case-guidance.md)

Sources:
- [Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz](../sources/20260408_U00AOI1eJUE.md), 02:07-18:02
