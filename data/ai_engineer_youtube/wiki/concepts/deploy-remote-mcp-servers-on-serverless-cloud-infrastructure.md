# Deploy Remote MCP Servers on Serverless Cloud Infrastructure

Summary: Local stdio MCP servers can be adapted into remote streamable HTTP services by placing tool handlers behind serverless compute, API routing, authorization, and session persistence.

Use when:
- Moving an MCP tool from a local development demo to a shared cloud endpoint.
- Designing cloud MCP deployment where existing serverless services and security controls should remain usable.

Details:
- The talk starts from a local stdio MCP server using the Python SDK and FastMCP, then frames cloud scale as decoupling the client from the local process and connecting to remote MCP servers. (12:48-14:30)
- The AWS demo places an MCP Lambda handler behind API Gateway using streamable HTTP, with an authorizer, optional Cognito integration, and DynamoDB session data. (14:34-15:04)
- The Lambda handler invokes the MCP server, while the Strands client passes the API Gateway URL and bearer token, lists the available tools, and passes those tools into the agent. (15:06-16:46)
- This pattern preserves ordinary cloud operational primitives: anything that can run in Lambda can become part of the remote MCP tool implementation. (17:09-17:21)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Stateless Remote MCP Servers Rebuild Allowed Tools Per Request](stateless-remote-mcp-servers-rebuild-allowed-tools-per-request.md)
- [MCP Gateways Create an Enterprise Root of Trust](mcp-gateways-create-an-enterprise-root-of-trust.md)
- [Move production MCP from API keys to scoped OAuth token flows](move-production-mcp-from-api-keys-to-scoped-oauth-token-flows.md)

Sources:
- [Building Agents at Cloud Scale - Antje Barth, AWS](../sources/20250802_WJjInLeaJjo.md), 12:48-17:21
