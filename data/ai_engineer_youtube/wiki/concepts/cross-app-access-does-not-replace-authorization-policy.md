# Cross-App Access Does Not Replace Authorization Policy

Summary: XAA centralizes authentication across MCP clients and servers, but it does not by default solve fine-grained authorization, scope reduction, or policy-specific permission caveats.

Use when:
- Separating identity proof from authorization scope in MCP security design.
- Reviewing whether an SSO-backed MCP connection is enough for sensitive tools.

Details:
- In Q&A, Galow states that XAA solves the authentication problem by default, not authorization; the user is still logging into the resource application as themselves. 17:00-17:35
- The permissions granted are the user's existing permissions in the resource application, such as Figma permissions in the example. 17:31-17:35
- Future work could let the IdP grant cross-app access with scoped caveats, but that is not part of the described spec at the time of the talk. 17:35-17:56
- The audience value helps the IdP and resource server identify the target MCP server, but it is not a mechanism for escalating or "hacking" OAuth scopes. 18:11-19:13

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Cross-app access centralizes MCP authentication through the identity provider](cross-app-access-centralizes-mcp-authentication-through-the-identity-provider.md)
- [Customize subagents by task, model, tools, and permissions](customize-subagents-by-task-model-tools-and-permissions.md)
- [Filter untrusted context before it reaches the agent](filter-untrusted-context-before-it-reaches-the-agent.md)

Sources:
- [One Login to Rule Them All: Cross-App Access for MCP - Garrett Galow, WorkOS](../sources/20260428_EmhRyw6xeT0.md), 17:00-17:56, 18:11-19:13
