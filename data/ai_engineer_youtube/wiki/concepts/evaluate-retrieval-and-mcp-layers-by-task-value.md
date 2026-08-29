# Evaluate Retrieval And MCP Layers By Task Value

Summary: Retrieval and MCP layers should be evaluated by whether their outputs help agents solve the target work, not merely by whether connectors return data.

Use when:
- Testing RAG, MCP, or knowledge-graph integrations for enterprise agents.
- Avoiding a connector-count mindset when institutional knowledge quality is the real constraint.

Details:
- The source warns that MCP and RAG outputs can be nondeterministic, unreliable, and untested when teams only check whether output is returned, 08:41-09:18.
- A connector layer over Confluence, Jira, SharePoint, GitHub, and similar stores only helps when the underlying knowledge is accurate enough and the retrieved result is valuable for the work item, 07:03-09:18.
- The speaker's early attempts with many MCP servers produced useful results only part of the time and left humans doing the gap-filling and question-answering work, 09:23-10:07.
- **Task value becomes measurable rather than argued when you run the without arm.** Sourcegraph's CodeScaleBench runs hundreds of software-lifecycle tasks with and without its code-navigation MCP tool, which turns "does this layer add task value" into a comparison instead of a claim, and produces the diagnostic material as a by-product: thousands of traces read for where the tool got in the agent's way. Jarmak states both halves as the purpose — "how is our tool helping the agent do the work," and "when it isn't working well, why isn't it working well." See [Benchmark Your Own Tool by Running Agents With and Without It](benchmark-your-tool-by-running-agents-with-and-without-it.md). ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 05:36-06:33)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Enterprise agent failures often expose missing institutional knowledge](enterprise-agent-failures-expose-missing-institutional-knowledge.md)
- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](demand-driven-context-pulls-knowledge-from-failed-work.md)
- [Benchmark Your Own Tool by Running Agents With and Without It](benchmark-your-tool-by-running-agents-with-and-without-it.md)

Sources:
- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md), 07:03-10:07
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 05:36-06:33
