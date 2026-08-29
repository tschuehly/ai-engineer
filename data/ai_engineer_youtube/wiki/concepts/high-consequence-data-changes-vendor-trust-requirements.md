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
- **The vendor's side of the same conversation, and where it can be automated.** Rosenthal reports that security review is "where deals tend to stall out and die over time" and recommends removing the seller from the loop: a trust portal with an auto-signed NDA, self-serve pen-test and security documentation, machine-filled questionnaires, and an inverted default in which the buyer must justify a call by naming "what I couldn't find." Read from this page's side, that is a claim about which parts of a trust requirement are document retrieval — those automate — and which are the buyer's own judgment about consequence, which do not. For AI products specifically, the second category has grown: training-data use, subprocessor model providers, retention of prompts and outputs, and what an agent may act on are not answered by a pen-test report. See [Automate the Security Review Path Because Deals Stall There](automate-the-security-review-path-because-deals-stall-there.md). ([Rosenthal](../sources/20260826_wdTRsfw0KG0.md), 08:15-09:06)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Cross-app access does not replace authorization policy](cross-app-access-does-not-replace-authorization-policy.md)
- [Govern MCP tool calls with tool-level policy and end-to-end traces](govern-mcp-tool-calls-with-tool-level-policy-and-end-to-end-traces.md)
- [Scope personal and team agents by reachable authority](scope-personal-and-team-agents-by-reachable-authority.md)
- [Automate the Security Review Path Because Deals Stall There](automate-the-security-review-path-because-deals-stall-there.md)

Sources:
- [Government Agents: AI Agents Meet Tough Regulations - Mark Myshatyn, Los Alamos National Lab](../sources/20251206_TnSGx36Ly0Q.md), 03:50-10:23
- [Reverse-Engineering the AI Buyer — Aliisa Rosenthal, Acrew Capital](../sources/20260826_wdTRsfw0KG0.md), 08:15-09:06
