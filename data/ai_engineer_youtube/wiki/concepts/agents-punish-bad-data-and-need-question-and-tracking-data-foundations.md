# Agents Punish Bad Data and Need Question and Tracking Data Foundations

Summary: Data quality dominates production agent effort because agents, unlike forgiving humans, return wrong answers confidently when fed wrong data. A durable data foundation separates question data (what the agent answers from) from tracking data (the traces), and gives the tracking data its own schema and centralized collection strategy.

Use when:
- Estimating where production-agent effort actually goes before model work.
- Designing how trace and observability data is stored, governed, and served.

Details:
- The speaker spends roughly 60% of project time on the data foundation, because data was historically built for forgiving humans who can correct a wrong report, while agents find the wrong value, answer confidently, and give no signal that anything went wrong. (14:45-15:42)
- The foundation has two halves: question data (pre-training, post-training, and API-reachable data the agent answers from) and tracking data (the trace/observability data). Tracking data needs a deliberate schema and serving plan to support auditors, regulators, online monitoring, and LLM-as-judge runs, especially when hundreds of agents run across the org. (15:42-16:38)
- Metadata is what lets agents use enterprise data: cataloging tables with descriptions, column descriptions, and PII tags (the speaker cites Unity Catalog over a Delta Lake layer) gives the model context when it queries those tables, with governance centralized at one layer. (16:38-18:28)
- Enterprises run multiple frameworks (CrewAI, LangChain) and clouds, so trace data should flow into one centralized collection layer that can serve operational dashboards, first-line health monitoring, text-to-SQL, custom apps, and automated judges from a shared location. (18:28-19:52)
- Stale data is a concrete failure mode: when a bank changed its interest-rate policy, the new policy document was not re-embedded into the vector database, so the agent served stale answers and CSAT dropped until tracing exposed the cause. (29:33-30:29)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Retrieval](../topics/retrieval.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [AI Data Lakehouses Need Online Retrieval and Offline Iteration Paths](ai-data-lakehouses-need-online-retrieval-and-offline-iteration-paths.md)
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Run a Production AI Incident Playbook](run-a-production-ai-incident-playbook.md)
- [Sequence Production AI by Pillars and Choose the Model Last](sequence-production-ai-by-pillars-and-choose-the-model-last.md)

Sources:
- [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](../sources/20260618_ObTPqBGsEbA.md), 14:45-19:52, 29:33-30:29
