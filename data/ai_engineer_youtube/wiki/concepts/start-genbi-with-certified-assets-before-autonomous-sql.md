# Start GenBI With Certified Assets Before Autonomous SQL

Summary: A governed GenBI agent can earn trust by first retrieving certified reports and dashboards, then using those validated assets as context or query seeds before attempting autonomous SQL over enterprise data.

Use when:
- Designing an analytics copilot for messy enterprise BI systems.
- Choosing how much autonomy to give an agent that answers business questions from governed data.

Details:
- The source argues against starting with free-form SQL because query generation is difficult even for humans and because executive-grade answers need higher accuracy than the system currently provides. (08:33-09:05)
- The safer first step is to retrieve already verified reports and dashboards from the existing ecosystem and deliver the same trusted asset in a faster, more interactive way. (09:06-09:49)
- The architecture separates a metadata agent for context understanding, a RAG agent for finding certified reports, an SQL agent for additional data pulls, and a BI answer agent for translating results into business language. (15:55-17:04)
- When a certified report is not enough, it can still provide a close query seed or few-shot example for SQL expansion rather than forcing the model to build a query from scratch. (17:04-17:42)

Related topics:
- [Agents](../topics/agents.md)
- [Business Intelligence](../topics/business-intelligence.md)
- [Infrastructure](../topics/infrastructure.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Enterprise AI Asset Registries Connect Governance To Runtime Lineage](enterprise-ai-asset-registries-connect-governance-to-runtime-lineage.md)
- [Agentic Retrieval Lets Models Plan Search Steps](agentic-retrieval-lets-models-plan-search-steps.md)

Sources:
- [Small Bets, Big Impact Building GenBI at a Fortune 100 - Asaf Bord, Northwestern Mutual](../sources/20251223_LU9KgcZDRfY.md), 08:33-17:42
