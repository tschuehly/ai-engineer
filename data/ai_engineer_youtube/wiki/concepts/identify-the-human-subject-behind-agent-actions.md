# Identify the Human Subject Behind Agent Actions

Summary: Agent security policy needs a concrete human or enterprise subject before it can apply authentication, authorization, restrictions, or audit semantics.

Use when:
- Designing agents that act for users, employees, owners, or administrators.
- Separating anonymous model execution from user-scoped delegated authority.

Details:
- Auth0 frames "AI needs to know who I am" as the first pillar because an anonymous actor cannot receive meaningful security restrictions or authorization decisions. 05:18-05:46
- The subject is not only "the agent"; it may be the human user, employee, owner, or administrator on whose behalf the operation is performed. 07:48-08:10
- In enterprise settings, an employee's agent may represent both the user and the company, so the organization also needs control over what those delegated agents do. 07:05-07:33

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Cross-app access centralizes MCP authentication through the identity provider](cross-app-access-centralizes-mcp-authentication-through-the-identity-provider.md)
- [Scope personal and team agents by reachable authority](scope-personal-and-team-agents-by-reachable-authority.md)
- [Customize subagents by task, model, tools, and permissions](customize-subagents-by-task-model-tools-and-permissions.md)

Sources:
- [Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0](../sources/20260114_VSdV-AdSlis.md), 05:18-05:46, 07:05-08:10
