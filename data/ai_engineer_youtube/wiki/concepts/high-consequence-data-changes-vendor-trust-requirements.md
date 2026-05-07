# High-Consequence Data Changes Vendor Trust Requirements

Summary: Vendors serving high-consequence public-sector agent workloads must satisfy trust requirements beyond ordinary SaaS security posture. The more sensitive the data and actions, the more customers need continuous monitoring, explicit control mappings, deployment locality, and partnership around governance.

Use when:
- Evaluating whether a SaaS, model, or agent platform is appropriate for regulated or classified work.
- Planning customer trust evidence for high-consequence AI deployments.

Details:
- Los Alamos distinguishes open, public, unrestricted data from controlled, classified, DOE, restricted, formerly restricted, PII, mission, operational, and finance data; the latter categories change what agent services can touch. (07:24-09:32)
- A SOC 2 report is not enough for these workloads; the talk points to NIST SP 800-53, FedRAMP, DoD security requirements, CNSSI 1253, and continuous monitoring as part of the trust conversation. (08:13-09:43)
- Regulated customers may need AI governance definitions for pilots, risk levels, and agency-specific implementation strategies while formal policy is still being shaped. (09:48-10:23)
- The trust burden is reciprocal: national labs need commercial and academic partners, but partners need to design for the data and outcome responsibility that comes with government access. (03:50-05:14, 05:53-06:09)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Cross-app access does not replace authorization policy](cross-app-access-does-not-replace-authorization-policy.md)
- [Govern MCP tool calls with tool-level policy and end-to-end traces](govern-mcp-tool-calls-with-tool-level-policy-and-end-to-end-traces.md)
- [Scope personal and team agents by reachable authority](scope-personal-and-team-agents-by-reachable-authority.md)

Sources:
- [Government Agents: AI Agents Meet Tough Regulations - Mark Myshatyn, Los Alamos National Lab](../sources/20251206_TnSGx36Ly0Q.md), 03:50-10:23
