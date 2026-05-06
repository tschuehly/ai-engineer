# A2A Agent Registries Make Deployed Agents Discoverable Through Agent Cards

Summary: An A2A registry uses agent cards as a standard metadata contract so deployed agents can be discovered, inspected, and reused by other agents or developers. CI/CD should publish the card as part of deployment so the registry stays current.

Use when:
- Building an internal marketplace or discovery layer for agent-to-agent services.
- Standardizing how agents publish their endpoint, capabilities, modalities, and authentication requirements.

Details:
- The A2A registry is described as a catalog of available agents that lets developers connect to already developed agents. (08:05-08:31)
- The registry is based on agent cards that describe an agent's identity, endpoint, capabilities, supported modalities, and authentication requirements. (11:43-12:01)
- Deployment can make agent development self-documenting by publishing the agent card into the registry through CI/CD, allowing other agents and developers to discover and interact with the new service. (12:03-12:36)
- Inspector pages and form-based widgets can help developers validate A2A compatibility and generate agent-card metadata without hand-editing raw JSON first. (15:41-16:50)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Enterprise AI asset registries connect governance to runtime lineage](enterprise-ai-asset-registries-connect-governance-to-runtime-lineage.md)
- [Blueprint repositories standardize MCP and A2A service delivery](blueprint-repositories-standardize-mcp-and-a2a-service-delivery.md)
- [Agent Connectivity Stack Combines Skills, MCP, CLIs, and Computer Use](agent-connectivity-stack-combines-skills-mcp-clis-and-computer-use.md)

Sources:
- [One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca](../sources/20260410_VXfRt_H-V08.md), 08:05-16:50
