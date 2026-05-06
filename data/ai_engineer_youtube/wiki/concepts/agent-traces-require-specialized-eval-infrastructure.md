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

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Apply online scoring to production traces with cost-aware sampling](apply-online-scoring-to-production-traces-with-cost-aware-sampling.md)

Sources:
- [Why building eval platforms is hard - Phil Hetzel, Braintrust](../sources/20260428__fQ7Z_Wfouk.md), 15:58-18:00
