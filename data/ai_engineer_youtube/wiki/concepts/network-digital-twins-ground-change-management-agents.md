# Network Digital Twins Ground Change-management Agents

Summary: Network-change agents need a current, executable representation of the production network before they can safely assess impact or validate a proposed change. A digital twin can combine a network knowledge graph with testing tools so agents work against modeled state instead of only ticket prose.

Use when:
- Designing AI support for ITSM, change advisory, or network operations workflows.
- Deciding what context an agent needs before it can recommend or run network validation tests.

Details:
- Cisco's application combines ITSM ticket intent, role-specific agents, and a network knowledge graph/digital twin for change-management workflows. 02:37-03:36
- The demo flow summarizes a ServiceNow ticket, creates an impact assessment, writes it back to the ticket, generates a test plan, and later attaches execution results for approval-board review. 12:37-15:06
- The execution agent pulls a GitHub PR for a firewall configuration change, snapshots the latest network state from the knowledge graph, computes against the proposed change, and runs test cases one by one. 15:11-16:31
- The digital twin is a combination of the knowledge graph plus network-testing tools such as Batfish or RouteNet, not only a passive graph database. 16:33-16:49

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Live architecture digital twins ground architecture copilots](live-architecture-digital-twins-ground-architecture-copilots.md)
- [Make agent work more trustworthy by making it verifiable](make-agent-work-more-trustworthy-by-making-it-verifiable.md)

Sources:
- [Multi Agent AI and Network Knowledge Graphs for Change — Ola Mabadeje, Cisco](../sources/20250822_m0dxZ-NDKHo.md), 02:37-03:36, 12:37-17:32
