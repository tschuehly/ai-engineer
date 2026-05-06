# Translate API Endpoints Into Agent Stories

Summary: MCP tools should collapse low-level API operations into agent stories: specific outcomes a programmatic agent can recognize and complete with limited context. Generated endpoint mirrors can bootstrap experiments, but should be curated before production use.

Use when:
- Turning a REST or OpenAPI surface into MCP tools.
- Debugging agents that over-orchestrate many low-level tools for a simple business action.

Details:
- Atomic REST operations are good API design but poor MCP design when the agent needs a business outcome such as tracking an order; the server should expose the outcome instead of making the model choreograph every step. 14:47-15:43
- Agents can orchestrate tool sequences, but using an LLM as glue is slow, expensive, stochastic, and hard to debug when the algorithm is already known. 15:46-16:21
- The proposed design unit is "one tool equals one agent story": something an autonomous agent with an objective and limited context window is trying to achieve. 16:21-16:42
- Tool names should be written for agent selection, not for future API maintainers; explanatory names help the model pick the right tool at the right time. 16:43-17:04
- Auto-converting a few endpoints can be a useful bootstrap to see whether an agent can use a tool at all, but the REST-shaped parts should then be stripped and curated instead of shipped to production as the MCP server. 38:20-39:59

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Design MCP Servers as Agent Products](design-mcp-servers-as-agent-products.md)
- [Encode Agent Intent Into Server-Side Tools](encode-agent-intent-into-server-side-tools.md)
- [Adapt Third-Party MCP Servers to the Agent Workflow](adapt-third-party-mcp-servers-to-the-agent-workflow.md)

Sources:
- [Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect](../sources/20260112_96G7FLab8xc.md), 14:47-17:04, 38:20-39:59
