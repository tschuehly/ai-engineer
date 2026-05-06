# Blueprint Repositories Standardize MCP and A2A Service Delivery

Summary: Template repositories can turn MCP and A2A service development into a standardized delivery path by packaging boilerplate infrastructure, required interfaces, auth, cost tracking, observability, and registry publication. This lets teams focus on business logic while still meeting enterprise deployment conventions.

Use when:
- Many teams need to build MCP servers or A2A agents without reimplementing platform concerns.
- Linking DevOps pipelines to AI asset registries so production deployment also updates discoverability and governance metadata.

Details:
- Amplifon created separate GitHub template repositories for MCP and A2A development so teams can start from a standard path toward production. (17:49-18:27)
- The blueprints include Docker files, package management, FastAPI server exposure, authentication, cost tracking, Langfuse observability, and evaluation support. (18:31-19:17)
- The A2A blueprint is framework-agnostic, using interfaces and ports so teams can implement in LangChain, Agno, or another framework while preserving the same outer contract. (19:20-19:56)
- Deployment tags trigger GitHub Actions that publish Docker images plus metadata such as A2A agent cards and MCP `server.json` into the registry backend. (20:01-20:50)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Enterprise AI asset registries connect governance to runtime lineage](enterprise-ai-asset-registries-connect-governance-to-runtime-lineage.md)
- [A2A agent registries make deployed agents discoverable through agent cards](a2a-agent-registries-make-deployed-agents-discoverable-through-agent-cards.md)
- [Gateway Platform Primitives Let Teams Focus on MCP Business Logic](gateway-platform-primitives-let-teams-focus-on-mcp-business-logic.md)

Sources:
- [One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca](../sources/20260410_VXfRt_H-V08.md), 17:49-20:50
