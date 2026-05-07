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

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Monitor whole agent systems, not single models](monitor-whole-agent-systems-not-single-models.md)

Sources:
- [How to look at your data - Jeff Huber (Chroma) + Jason Liu (567)](../sources/20250806_jryZvCuA0Uc.md), 07:28-17:57
