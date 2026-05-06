# Cross-App Access Centralizes MCP Authentication Through the Identity Provider

Summary: Cross-App Access lets an organizational identity provider act as the trust bridge between an MCP client and MCP server, reducing repeated per-tool consent while giving IT a central policy point for which app may request access to another.

Use when:
- Designing enterprise MCP authentication for many agent tools.
- Reducing repeated OAuth consent screens without bypassing SSO governance.

Details:
- Ordinary MCP OAuth setup can force users to authenticate and consent separately for every connected MCP server, which becomes expensive and low-signal across large engineering teams. 01:19-02:39
- XAA assumes the MCP client, MCP server, and identity provider already have trust relationships through SSO; the IdP can then validate that the user belongs to both applications and that the client is allowed to request access to the server. 06:37-07:33, 10:52-11:08
- The admin-side setup is a managed connection policy: for example, the IdP can record that Cursor is allowed to request access to Figma, while normal app membership still controls whether the user belongs to both applications. 13:17-14:15
- The MCP client identifies the target resource with an audience URL such as an MCP server URL, and the identity provider maps that audience to the managed application policy. 18:11-19:07

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Use skills for workflow guidance and MCP for integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Short-lived IdP-derived tokens reduce standing MCP access](short-lived-idp-derived-tokens-reduce-standing-mcp-access.md)

Sources:
- [One Login to Rule Them All: Cross-App Access for MCP - Garrett Galow, WorkOS](../sources/20260428_EmhRyw6xeT0.md), 01:19-02:39, 06:37-07:33, 10:52-11:08, 13:17-14:15, 18:11-19:07
