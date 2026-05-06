# Make Internal Platforms Self-Service for Agent Users

Summary: Internal developer platforms should expose self-service workflows that agents can complete without person-dependent deployment, provisioning, or troubleshooting handoffs.

Use when:
- Evaluating whether a platform can be used directly by coding agents.
- Replacing tribal platform operations with self-service APIs, CLIs, MCP servers, or automated flows.

Details:
- The source's onboarding story shows a developer copying pipelines, hitting non-application deployment errors, asking teammates, waiting on infrastructure specialists, and discovering additional resource dependencies such as databases or blob storage. Those human workarounds are especially brittle for agents. (02:54-05:20)
- The talk argues that when agents face the same pain points, they become a limiting factor on the productivity of both the coding agent and the developer using it. (05:26-06:24)
- Self-service means the developer or agent can trigger required platform actions without talking to a specific person or waiting for a specific person to do something. (07:06-07:45)
- A platform is not truly self-service if the user or agent must fetch building blocks from many places and assemble a hidden flow manually; automate the flow and make the intended path easy. (07:53-08:24)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Build internal AI engineering platforms when off-the-shelf tools lack enterprise context](build-internal-ai-engineering-platforms-when-off-the-shelf-tools-lack-enterprise-context.md)
- [MCP tool surfaces need default context budgets](mcp-tool-surfaces-need-default-context-budgets.md)

Sources:
- [Platforms for Humans and Machines: Engineering for the Age of Agents - Juan Herreros Elorza](../sources/20260408_cCRO3ChaYhM.md), 02:54-08:24
