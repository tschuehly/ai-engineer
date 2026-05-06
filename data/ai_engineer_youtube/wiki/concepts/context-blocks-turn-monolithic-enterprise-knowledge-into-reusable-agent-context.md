# Context Blocks Turn Monolithic Enterprise Knowledge Into Reusable Agent Context

Summary: Context blocks are reusable units of institutional knowledge extracted from messy enterprise sources so agents can retrieve focused, task-relevant context instead of consuming an undifferentiated knowledge monolith.

Use when:
- Refactoring broad enterprise documentation into agent-usable retrieval units.
- Designing persistent knowledge that multiple agents can reuse after one failure-driven discovery cycle.

Details:
- The talk compares institutional knowledge transformation to decomposing a legacy monolith into microservices: a monolithic knowledge base should be transformed into smaller context blocks through an explicit process, 12:02-12:31.
- After a task is solved, the newly discovered knowledge should be curated in a specific place so the same or other agents can reuse it, 15:22-15:45.
- The persistence layer can be a file system for a demo, but the same pattern can live behind MCP servers, RAG, Confluence, Slack, or other enterprise stores, 22:48-23:10.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](demand-driven-context-pulls-knowledge-from-failed-work.md)
- [Enterprise agent failures often expose missing institutional knowledge](enterprise-agent-failures-expose-missing-institutional-knowledge.md)

Sources:
- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md), 12:02-15:45, 22:48-23:10
