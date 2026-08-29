# Evaluate BI Agents With Real Metadata and Expert Feedback

Summary: BI-agent evaluation should use production-like data complexity, subject-matter experts, and metadata quality experiments, because clean demos can hide the schema, context, and governance failures that block enterprise use.

Use when:
- Validating a natural-language analytics or semantic-layer agent.
- Deciding whether metadata enrichment improves LLM performance on enterprise data questions.

Details:
- The GenBI team chose actual messy enterprise data rather than synthetic or cleansed data to expose the complexities that would matter before production. (04:53-05:29)
- Working with people who use the data daily supplied subject-matter expertise, real examples of questions and answers, and eval material while also creating business buy-in. (05:38-06:35)
- Early rollout is staged by evaluator skill: BI experts first, then business managers who know enough to catch wrong answers, while executives are deferred until accuracy and trust improve. (07:30-08:44)
- The metadata effort is evaluated by running a battery of questions against databases with and without good metadata, then comparing how much better the LLM performs when the right metadata is present. (19:08-19:53)
- Internal benchmarks created during research become useful for evaluating third-party GenBI tools and detecting shallow vendor demos. (14:39-15:16, 20:12-20:24)
- **The cheapest version of expert grounding: take the questions from the documented business process, before the data is connected.** Izmit wrote 150 questions from Snowflake's sales process into a spreadsheet before trying the agent, over engineering's objection that the data was not wired up — "it doesn't matter. These are the questions your sellers are going to ask" — and the first run scored 50%. Two properties make it worth copying: it needs no traffic, annotation tool, or labeling budget, and the questions the system *cannot* answer become the data-connection backlog ranked by the job rather than by availability. What it does not supply is a rubric; "accuracy" over 150 free-form business questions is never defined in the source. ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 04:08-04:42)

Related topics:
- [Business Intelligence](../topics/business-intelligence.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [RAG Stacks Need Modular Baselines Instead of One Fixed Recipe](rag-stacks-need-modular-baselines-instead-of-one-fixed-recipe.md)
- [Mature eval platforms from spreadsheets into experiment systems](mature-eval-platforms-from-spreadsheets-into-experiment-systems.md)
- [Write the Question Set From the Business Process Before the Data Is Connected](write-the-question-set-from-the-business-process-before-the-data-is-connected.md)

Sources:
- [Small Bets, Big Impact Building GenBI at a Fortune 100 - Asaf Bord, Northwestern Mutual](../sources/20251223_LU9KgcZDRfY.md), 04:53-20:24
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 04:08-04:42
