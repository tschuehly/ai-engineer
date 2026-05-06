# Small Bets, Big Impact Building GenBI at a Fortune 100 - Asaf Bord, Northwestern Mutual

Source: [Small Bets, Big Impact Building GenBI at a Fortune 100 - Asaf Bord, Northwestern Mutual](https://www.youtube.com/watch?v=LU9KgcZDRfY)
Uploaded: 2025-12-23
Transcript: `raw/20251223_LU9KgcZDRfY/LU9KgcZDRfY.en-orig.vtt`

## Summary

Asaf Bord describes GenBI as an enterprise analytics copilot that answers business questions with data, and argues that risk-averse organizations can make this kind of AI work fundable by using real-but-controlled data, expert users, staged trust boundaries, and incremental productizable deliveries instead of one large speculative program.

## Extracted Concepts

- [Fund enterprise AI through incremental productizable bets](../concepts/fund-enterprise-ai-through-incremental-productizable-bets.md) - the source shows how six-week stages with tangible deliverables reduce sunk-cost risk and keep leadership engaged.
- [Start GenBI with certified assets before autonomous SQL](../concepts/start-genbi-with-certified-assets-before-autonomous-sql.md) - the source frames report discovery over certified dashboards as a safer first product than free-form SQL generation.
- [Evaluate BI agents with real metadata and expert feedback](../concepts/evaluate-bi-agents-with-real-metadata-and-expert-feedback.md) - the source explains why messy production-like data, BI experts, and metadata A/B tests provide stronger validation than polished demos.

## Topic Links

- [Agents](../topics/agents.md)
- [Business Intelligence](../topics/business-intelligence.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)
- [AI Monetization](../topics/ai-monetization.md)

## Notes

- GenBI is defined as an agent that helps people answer business questions with data, reducing reliance on BI teams to find reports and explain their meaning. (01:23-01:53)
- The team chose actual messy enterprise data rather than synthetic or clean data so lab results would expose production-like complexity, while still working in a sandbox and excluding actual client data. (03:31-05:29, 07:10-07:17)
- End users and BI subject-matter experts were part of the research process, providing examples, eval material, and buy-in before production packaging. (05:38-06:35)
- The release path deliberately starts with BI experts, then business managers who can detect errors, while executive-facing answers are deferred because the system is not yet accurate enough for that trust level. (07:30-08:44)
- The initial trust architecture avoids generating SQL and instead retrieves already verified reports and dashboards, because BI teams reported that much of their work is directing users to the right report. (08:53-09:49)
- The roadmap breaks work into six-week stages: natural language to SQL research, metadata/context definition, multi-context semantic search/data owner discovery, light data pivoting, role/access design, and eventually a fuller GenBI agent that can run SQL and join data. (10:05-13:37)
- The proposed architecture uses a data and metadata layer, a metadata agent, a RAG/report-finding agent, an SQL agent, a BI answer agent, orchestration, governance/trust, and contextual UI. (15:55-16:24)
- Existing certified reports can seed later SQL generation as close few-shot examples, letting the SQL agent expand from a validated query rather than starting from scratch. (17:04-17:42)
- Each agent component can be packaged as its own product with tangible business metrics, allowing the program to stop or continue after each stage. (18:06-18:30)
- Internal benchmarks from the research can be reused to evaluate vendor solutions such as Databricks Genie and to avoid being persuaded by shallow demos. (14:39-15:16, 20:12-20:24)
- The talk connects GenAI productivity gains to SaaS pricing pressure: seat-based pricing may become less aligned when one AI-augmented worker can produce much more output. (21:20-22:24)
