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
- **An ordering argument for doing this second.** Figma shipped a local server first and only then built the remote one, because before the March 2025 spec revision "there wasn't this [auth] spec to to build from and we could easily relay [auth] from our web app to our desktop app." Local was "our fastest path to getting something into the hands of users to understand product market fit and what kind of tools and use cases folks had," and it suited enterprises "because they kind of like the idea of our data not being sent anywhere." The remote server followed in September, both reached general availability in October 2025, and both are maintained — the two are a sequence, not a choice. ([Lumarie](../sources/20260828_ZIYYsAzaLlA.md), 13:28-15:18)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Stateless Remote MCP Servers Rebuild Allowed Tools Per Request](stateless-remote-mcp-servers-rebuild-allowed-tools-per-request.md)
- [MCP Gateways Create an Enterprise Root of Trust](mcp-gateways-create-an-enterprise-root-of-trust.md)
- [Move production MCP from API keys to scoped OAuth token flows](move-production-mcp-from-api-keys-to-scoped-oauth-token-flows.md)
- [An Installed Desktop App Is an Auth and Filesystem Beachhead](an-installed-desktop-app-is-an-auth-and-filesystem-beachhead.md)

Sources:
- [Building Agents at Cloud Scale - Antje Barth, AWS](../sources/20250802_WJjInLeaJjo.md), 12:48-17:21
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 13:28-15:18
