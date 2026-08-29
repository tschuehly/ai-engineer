# Agent Traces Require Specialized Eval Infrastructure

Summary: Agent traces differ from ordinary application traces because they are text-heavy, semi-structured, large, and high velocity, so eval platforms need storage and query designs built for that shape.

Use when:
- Designing trace storage for agent observability or online evaluation.
- Deciding whether a simple relational table is enough for AI trace data.

Details:
- Adding production observability expands an eval platform into tracing and logging infrastructure, not just offline test execution, 15:58-16:07.
- Agent traces are described as unlike normal application traces: they are often semi-structured or unstructured and contain a large amount of text inherent to LLM workflows, 17:18-17:37.
- Very large traces can create performance problems when naively stored as a single database row, such as trying to cram a one-gigabyte trace into Postgres, 17:37-17:53.
- Production agent usage can be high velocity, so trace infrastructure must handle both complicated records and numerous events, 17:53-18:00.
- **The read path has its own two constraints, and solving storage does not solve them.** LangChain gives the cost as a product you can compute in advance — "you can like literally multiply the input token cost times the number of traces times like how big each trace is on average" — and the capacity limit as a hard stop: "if I have a super long interaction with a coding agent like Claude Code or Codex or like deep agents, I can't even read that trace with another agent because that context like doesn't fit in memory." A trace store therefore needs a query interface a mining agent can use, not just durable retrieval of whole records ([Mine Trace Corpora With Agents Because They Do Not Fit in Context](mine-trace-corpora-with-agents-because-they-do-not-fit-in-context.md)). ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 06:35-07:36)
- **The access layer is part of the specialization, not a wrapper on it.** DoorDash exposes the same trace store through MCP, an SDK, and REST — "all your API access including SDK access is basically powered by this single plane" — with "table APIs" over scores and datasets that both first-party screens and operator-generated apps are built on. Storage shape is the well-known half of the problem; the less obvious half is that annotation, judging, and sampling are all reads and writes against the same corpus by very different clients, so a trace store designed only for an engineer's query path forces every other workflow into a copy. ([AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 06:12-06:35, 07:10-07:44)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Apply online scoring to production traces with cost-aware sampling](apply-online-scoring-to-production-traces-with-cost-aware-sampling.md)
- [Mine Trace Corpora With Agents Because They Do Not Fit in Context](mine-trace-corpora-with-agents-because-they-do-not-fit-in-context.md)
- [Ship Stable APIs and Let Users Vibe-Code the Interface](ship-stable-apis-and-let-users-vibe-code-the-interface.md)

Sources:
- [Why building eval platforms is hard - Phil Hetzel, Braintrust](../sources/20260428__fQ7Z_Wfouk.md), 15:58-18:00
- [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../sources/20260812_CvRngaQZQ3Y.md), 06:35-07:36
- [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 06:12-06:35, 07:10-07:44
