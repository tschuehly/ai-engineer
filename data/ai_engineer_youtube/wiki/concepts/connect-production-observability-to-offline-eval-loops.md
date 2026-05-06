# Connect Production Observability to Offline Eval Loops

Summary: Production traces should feed offline evals because real user behavior exposes failure modes that pre-production examples often miss.

Use when:
- Turning production agent failures into regression cases.
- Designing an eval platform that also collects observability data.

Details:
- Braintrust frames evals and observability as adjacent agent-quality problems: evals build pre-production confidence, while observability checks whether the same behavior holds under real usage, 03:33-04:20.
- The talk argues that the best way to identify agent failure modes is access to production trace data from real users, then scoring those failure modes explicitly, 14:00-14:21.
- A durable eval loop observes production behavior, analyzes traces, pulls actual examples into an offline environment, and improves the agent through offline evals for the lifetime of the production agent, 14:21-15:49.
- Online evals can point scoring functions at observability traffic and trigger alerting, while offline evals can replay production-like behavior in a safer environment, 16:20-16:48.
- Traces are useful product artifacts because they preserve input, output, metadata, and agent actions; PMs can inspect those traces, pull a traced prompt and variables into a playground, and turn observed behavior into an eval data set. 19:43-25:21

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Apply online scoring to production traces with cost-aware sampling](apply-online-scoring-to-production-traces-with-cost-aware-sampling.md)
- [Replay production failures before promoting prompt fixes](replay-production-failures-before-promoting-prompt-fixes.md)
- [Label LLM Judge Outputs Before Mapping Them to Scores](label-llm-judge-outputs-before-mapping-them-to-scores.md)

Sources:
- [Why building eval platforms is hard - Phil Hetzel, Braintrust](../sources/20260428__fQ7Z_Wfouk.md), 03:33-04:20, 14:00-16:48
- [Shipping AI That Works: An Evaluation Framework for PMs - Aman Khan, Arize](../sources/20251226_2HNSG990Ew8.md), 19:43-25:21
