# Vet MCP Servers As Action-Capable Extensions

Summary: MCP servers should be reviewed as action-capable extensions of the agent, not as passive context feeds. In Copilot workflows they can expose external data, create issues, search systems, inspect schemas, or perform other tasks on the user's behalf.

Use when:
- Adding an MCP server to GitHub Copilot or another coding-agent environment.
- Deciding whether a third-party MCP server is safe enough for developer workflows.

Details:
- Harrison describes MCP as the way Copilot can reach external data sources and services that the base LLM does not know directly. 23:48-24:19
- The request path is Copilot to MCP server to external resource, with examples such as GitHub issue creation, search, and database schema or data access. 24:31-25:16
- The trust caveat is explicit: MCP servers can access data and perform tasks on the user's behalf, so third-party servers should be used only when trusted or built internally. 25:18-25:58
- **Vetting a server is a point-in-time check on code that gets replaced.** The trust question here is "should this server be allowed to act on my behalf?"; the supply-chain question is whether the code answering to that name today is the code you reviewed. LiteLLM, at "three and a half million downloads a day," shipped a poisoned release for three hours after attackers stole its PyPI publishing tokens through a GitHub app; the package installed a harvester for API, SSH, and crypto keys plus a remote-command-execution backdoor. Detection was accidental — the malware crashed Cursor when the LiteLLM MCP server ran, and a researcher chased the crash. An MCP-server package is the worst case for this because it is installed *and* then run as a persistent local process with tool authority, so pin versions with hashes and treat an unexplained client crash after a dependency update as a possible security signal. See [An AI-Infrastructure Package Is a High-Yield Credential Target](an-ai-infrastructure-package-is-a-high-yield-credential-target.md). ([Rizwan](../sources/20260807_CoEIs6Xm8m8.md), 04:17-05:19)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Security](../topics/security.md)

Related concepts:
- [Harden Third-Party MCP Tools Against Silent Failure and Endpoint Risk](harden-third-party-mcp-tools-against-silent-failure-and-endpoint-risk.md)
- [Secure MCP servers by shrinking the agent-visible surface](secure-mcp-servers-by-shrinking-the-agent-visible-surface.md)
- [Treat Code-Executing Agents as RCE-Risk Surfaces](treat-code-executing-agents-as-rce-risk-surfaces.md)
- [An AI-Infrastructure Package Is a High-Yield Credential Target](an-ai-infrastructure-package-is-a-high-yield-credential-target.md)

Sources:
- [Piloting agents in GitHub Copilot - Christopher Harrison, Microsoft](../sources/20250726_DdaAABdAqZY.md), 23:48-25:58
- [Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline](../sources/20260807_CoEIs6Xm8m8.md), 04:17-05:19
