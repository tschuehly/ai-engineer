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
- **A second route to the same trust goal that keeps generated queries but shrinks the question set.** Snowflake's internal assistant answers free-form questions over a semantic layer (15 semantic views, 85 tables, 3,000 columns) rather than routing to certified reports, and buys trust by bounding what it will attempt: "we don't want to try to answer 100 questions and get them 70% right. We want to answer 50 questions, but get them 95% right," with the candidate set written from the sales process in advance and scoring 50% on its first run. Coverage was then restored incrementally — 60% of the data arrived in the six to seven months after launch. Read against this page, the discriminator is what already exists: where an ecosystem of certified assets exists, retrieving them is the cheaper trust anchor; where a governed semantic layer exists instead, scope restriction plus a process-derived question set does the same job. ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 04:08-05:31)
- **A rung below certified assets: no query at all for the common path.** Cloudflare's recurring analysis reads tables already transformed "by the dimension of time, also slice of the logical part of the business, which is manager, theater, and finally the metric," with trend detection pre-computed, which the speaker says "handles 80 or plus percent of the requests." Certified reports constrain what the agent retrieves; pre-shaped tables constrain what it can compute. Raw data and autonomous querying are kept, but pushed to the self-serve workspace where a human is driving — "you can always go down to the raw data" — rather than used in the unattended weekly artifact. ([Joyce](../sources/20260826_Qw_tC68KKes.md), 10:04-11:03)

Related topics:
- [Agents](../topics/agents.md)
- [Business Intelligence](../topics/business-intelligence.md)
- [Infrastructure](../topics/infrastructure.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Enterprise AI Asset Registries Connect Governance To Runtime Lineage](enterprise-ai-asset-registries-connect-governance-to-runtime-lineage.md)
- [Agentic Retrieval Lets Models Plan Search Steps](agentic-retrieval-lets-models-plan-search-steps.md)
- [Choose Quality Over Coverage Because the First Five Answers Decide Adoption](choose-quality-over-coverage-because-the-first-five-answers-decide-adoption.md)
- [Pre-Shape Analytics Data by Time, Slice, and Metric Before the Agent Reads It](pre-shape-analytics-data-by-time-slice-and-metric-before-the-agent-reads-it.md)

Sources:
- [Small Bets, Big Impact Building GenBI at a Fortune 100 - Asaf Bord, Northwestern Mutual](../sources/20251223_LU9KgcZDRfY.md), 08:33-17:42
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 04:08-05:31
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 10:04-11:03
