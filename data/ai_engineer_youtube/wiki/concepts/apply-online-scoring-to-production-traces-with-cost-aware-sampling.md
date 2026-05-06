# Apply Online Scoring to Production Traces With Cost-Aware Sampling

Summary: Production AI monitoring should score live traces, but the sampling strategy should distinguish cheap deterministic checks from expensive judge-model evaluations.

Use when:
- Moving AI evaluations from offline test sets into production monitoring.
- Deciding how much live traffic to score with LLM-as-judge checks.

Details:
- The workshop states that offline test cases provide confidence, but production data has no substitute; online scoring applies evaluation logic to live application logs, 01:13:58-01:14:39.
- For LLM-as-judge scoring, teams should start with a higher sampling rate to establish a baseline, then reduce sampling, for example to 5-10%, once the output is acceptable and costs need control, 01:14:39-01:15:14.
- Deterministic scores are cheap enough to run continuously, unlike more sophisticated model-based checks that may require stronger reasoning models and higher cost, 01:15:16-01:15:20.
- Metadata matters because online scoring may execute against individual spans, whole traces, or selected failure categories rather than every event, 01:17:18-01:17:44.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)
- [Prevent AI billing surprises with caps, notifications, and rate limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md)

Sources:
- [Shipping complex AI applications - Braintrust & Trainline](../sources/20260501_ZdheJTfLu-s.md), 01:13:58-01:15:20, 01:17:18-01:17:44
