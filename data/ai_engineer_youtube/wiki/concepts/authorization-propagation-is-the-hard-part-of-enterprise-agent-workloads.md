# Authorization Propagation Is the Hard Part of Enterprise Agent Workloads

Summary: Enterprise agent workloads need robust propagation of scopes, service-account permissions, and access-control context across MCP servers, asynchronous agents, and agent-to-agent delegation.

Use when:
- Designing headless or background agents that call MCP servers.
- Passing authority through MCP, A2A, service accounts, or other delegated agent workloads.

Details:
- The talk treats cloud hosting for MCP servers as mostly ordinary workload infrastructure, while authorization and access control are the hardest parts of external enterprise deployments. 06:08-06:16, 11:57-12:08
- A2A-style delegation can degrade into telling another agent what it should or should not do and relying on model alignment, which is weaker than passing enforceable scopes and access controls. 11:18-11:46
- Service accounts and asynchronous AI workloads need explicit checks that the workload has the correct access for the operation, rather than assuming inherited authority is safe. 11:46-11:56
- MCP elicitation points toward agents asking a human for missing details, but headless or background authorization remains unstable while the protocol and production patterns are still developing. 10:48-11:15

Related topics:
- [Security](../topics/security.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Preserve Authorization Chain of Custody Across Agent Hops](preserve-authorization-chain-of-custody-across-agent-hops.md)
- [Plan Asynchronous Authorization for Background Agents](plan-asynchronous-authorization-for-background-agents.md)
- [Treat Agents As Users For Authorization](treat-agents-as-users-for-authorization.md)

Sources:
- [(possible dupe but better sound) What does Enterprise Ready MCP mean? - Tobin South, WorkOS](../sources/20250627_0MqYA52iWQU.md), 06:08-06:16, 10:48-12:08
