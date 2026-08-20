# Cluster Conversation Outputs to Prioritize AI Product Work

Summary: AI application logs can be turned into product intelligence by extracting structured metadata from conversations, clustering similar outputs, and comparing quality or usage KPIs across clusters. This reveals which capabilities need tools, routing, prompts, education, or refusal behavior.

Use when:
- Conversation histories are too large or detailed for manual product review.
- Agent or chatbot teams need to decide what tools, prompts, routers, or product affordances to build next.
- Aggregate eval scores are too generic to explain where the system is succeeding or failing.

Details:
- Conversation histories contain implicit feedback such as retries, corrections, frustration, tool calls, chain steps, and errors; teams do not need to rely only on explicit feedback widgets (07:28-09:04).
- A useful pipeline summarizes conversations, extracts fields such as topics, tools used, errors, satisfaction, and frustration, embeds those summaries, clusters them, and aggregates them into higher-level segments for analysis (10:08-12:19).
- Comparing KPIs across clusters turns a vague score into an actionable diagnosis, such as finding that factuality is low for time-filter queries but high for contract-search queries (11:20-11:48).
- Usage and performance should be interpreted together: high-usage low-performance segments deserve fixes, high-usage high-performance segments are healthy, low-usage high-performance segments may need product education, and low-usage low-performance segments may only need refusal or a small prompt change (14:12-15:18).
- Impact-weighted cluster analysis can justify roadmap changes, such as adding plotting tools when a large share of conversations ask for data visualization and the current code execution path handles it poorly (17:07-17:57).
- **Scope limit: this is a periodic analysis pass, not an issue tracker.** Ben Hylak's objection is that clustering "is useful for one-off analysis, but it just doesn't really scale well" as a monitoring layer — boundaries are emergent rather than declared, temporal tracking across re-runs is unreliable, and what counts as the same issue "is actually very, very unique to every company," so a bucket like "price issues" can merge a wrong quote and a wrong refund with unrelated root causes. Everything on this page is about allocating roadmap attention from a snapshot, which is exactly the use he concedes; the failure begins when a cluster label is treated as a durable work item with a trend line ([Clusters Are Not Issues](clusters-are-not-issues.md)). ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 16:16-18:08)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Monitor whole agent systems, not single models](monitor-whole-agent-systems-not-single-models.md)
- [Clusters Are Not Issues](clusters-are-not-issues.md)
- [Promote Validated Live-Trace Failure Clusters Into the Golden Dataset](promote-validated-live-trace-failure-clusters-into-the-golden-dataset.md)

Sources:
- [How to look at your data - Jeff Huber (Chroma) + Jason Liu (567)](../sources/20250806_jryZvCuA0Uc.md), 07:28-17:57
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 16:16-18:08
