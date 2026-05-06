# Enterprise AI Asset Registries Connect Governance To Runtime Lineage

Summary: Enterprise AI registries should connect business use cases to the agents, MCP servers, models, owners, environments, authentication methods, costs, and lifecycle states they depend on. This turns discovery catalogs into operational lineage for governance, impact analysis, and maintenance.

Use when:
- Scaling AI tools and agents across many teams that would otherwise reinvent infrastructure and security models.
- Needing to answer which use cases are affected by a model disruption, tool outage, auth change, or compliance review.

Details:
- Amplifon's platform separates an MCP registry, A2A registry, and use-case registry, then links them so governance can see deployed MCP servers, agents, models, and use cases across teams. (07:41-08:52)
- MCP registry entries are enriched with enterprise metadata such as owner, environment, authentication model, cost attribution, and use-case linkage rather than only tool identity. (09:20-11:17)
- Use-case linkage is the governance layer: it enables impact analysis, auditability, and a trail of which AI tooling exists and how developers use it. (11:17-11:43)
- A use-case registry should capture status, version, description, ownership, linked assets, model usage, and lifecycle history so teams can trace outages or model disruptions back to affected business deployments. (12:51-17:47)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [MCP Gateways Create an Enterprise Root of Trust](mcp-gateways-create-an-enterprise-root-of-trust.md)
- [Build Internal AI Engineering Platforms When Off-the-Shelf Tools Lack Enterprise Context](build-internal-ai-engineering-platforms-when-off-the-shelf-tools-lack-enterprise-context.md)
- [A2A agent registries make deployed agents discoverable through agent cards](a2a-agent-registries-make-deployed-agents-discoverable-through-agent-cards.md)

Sources:
- [One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca](../sources/20260410_VXfRt_H-V08.md), 07:41-17:47
