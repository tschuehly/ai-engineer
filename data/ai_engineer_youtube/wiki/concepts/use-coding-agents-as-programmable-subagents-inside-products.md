# Use coding agents as programmable subagents inside products

Summary: A coding agent can be exposed as a programmable subagent or tool inside another product, not only as a standalone IDE or CLI. This lets a product call the agent through SDKs, CI/CD, GitHub Actions, MCP connectors, or custom workflows while keeping the outer product focused on domain experience.

Use when:
- Embedding code-writing or code-maintenance ability into an application workflow.
- Deciding whether a product agent should call a maintained coding agent instead of reimplementing one.

Details:
- Codex is described as usable from VS Code, CLI, cloud, ChatGPT, Slack, GitHub PR review, a TypeScript library, Python exec, GitHub Actions, CI/CD, and the Agents SDK. 08:31-13:24
- The source frames this as putting "the agent inside of your own agent": an outer product can call Codex programmatically and connect it back to the product through MCP connectors. 11:24-13:24
- One proposed product pattern is software that writes customer-specific plugin connectors at the API level, shifting work that previously required professional services into an agent-executed workflow. 13:24-13:57
- IDE products can wrap the coding agent in their own interaction layer while delegating model/harness maintenance to the agent provider; the user-facing differentiation remains the editor integration and coding experience. 14:08-14:28

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Agent connectivity stack combines skills, MCP, CLIs, and computer use](agent-connectivity-stack-combines-skills-mcp-clis-and-computer-use.md)
- [Embed agent tools in existing work surfaces](embed-agent-tools-in-existing-work-surfaces.md)

Sources:
- [Future-Proof Coding Agents - Bill Chen & Brian Fioca, OpenAI](../sources/20251205_wVl6ZjELpBk.md), 08:31-15:28
