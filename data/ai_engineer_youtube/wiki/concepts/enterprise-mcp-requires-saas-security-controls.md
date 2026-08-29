# Enterprise MCP Requires SaaS Security Controls

Summary: MCP servers become enterprise-ready by inheriting the same security and operations controls expected from production SaaS, then adapting them to agent-facing tool calls.

Use when:
- Moving an MCP server beyond a local or internal demo.
- Defining the minimum enterprise controls for a public or internal MCP service.

Details:
- Local MCP servers can prove an API connection, but they are not enough for broad use because they usually lack shared authentication, access controls, and production operations. 04:19-04:46
- A production MCP server should not expose an unauthenticated external API; users need login, authorization, admin-scoped privileges, and access controls before the tool is reachable. 04:48-05:35
- Public MCP services need abuse controls around signups, free-credit usage, input validation, and the broader auth stack because AI-backed services can turn credits or tool access into direct provider cost. 06:32-07:18
- Enterprise sales add the familiar SaaS checklist: SSO, lifecycle management, provisioning, fine-grained access controls, performant authorization, audit logs, and DLP for data routed through MCP servers. 08:08-09:28
- **Local-first answers one enterprise objection and surfaces a control class this page does not name.** Figma's local server was "really great with enterprises because they kind of like the idea of our data not being sent anywhere," and file access inherits the OS permission model rather than needing a new one. But the launch checklist includes a requirement that is commercial rather than security-shaped: alongside "the highest possible bar for our security" and "respect file permissions" sits "we wanted to respect our pricing [and] packaging so we didn't have abuse vectors" — an agent-reachable surface can become a route to a paid capability outside its packaging, and entitlement enforcement belongs on the control list next to authentication and authorization. ([Lumarie](../sources/20260828_ZIYYsAzaLlA.md), 13:13-14:18)

Related topics:
- [Security](../topics/security.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Move Production MCP From API Keys to Scoped OAuth Token Flows](move-production-mcp-from-api-keys-to-scoped-oauth-token-flows.md)
- [Model MCP Servers as OAuth Resource Servers](model-mcp-servers-as-oauth-resource-servers.md)
- [Govern MCP Tool Calls With Tool-Level Policy and End-to-End Traces](govern-mcp-tool-calls-with-tool-level-policy-and-end-to-end-traces.md)
- [An Installed Desktop App Is an Auth and Filesystem Beachhead](an-installed-desktop-app-is-an-auth-and-filesystem-beachhead.md)

Sources:
- [(possible dupe but better sound) What does Enterprise Ready MCP mean? - Tobin South, WorkOS](../sources/20250627_0MqYA52iWQU.md), 04:19-09:28
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 13:13-14:18
