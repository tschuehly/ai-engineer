# Evaluate Retrieval And MCP Layers By Task Value

Summary: Retrieval and MCP layers should be evaluated by whether their outputs help agents solve the target work, not merely by whether connectors return data.

Use when:
- Testing RAG, MCP, or knowledge-graph integrations for enterprise agents.
- Avoiding a connector-count mindset when institutional knowledge quality is the real constraint.

Details:
- The source warns that MCP and RAG outputs can be nondeterministic, unreliable, and untested when teams only check whether output is returned, 08:41-09:18.
- A connector layer over Confluence, Jira, SharePoint, GitHub, and similar stores only helps when the underlying knowledge is accurate enough and the retrieved result is valuable for the work item, 07:03-09:18.
- The speaker's early attempts with many MCP servers produced useful results only part of the time and left humans doing the gap-filling and question-answering work, 09:23-10:07.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Enterprise agent failures often expose missing institutional knowledge](enterprise-agent-failures-expose-missing-institutional-knowledge.md)
- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](demand-driven-context-pulls-knowledge-from-failed-work.md)

Sources:
- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md), 07:03-10:07
