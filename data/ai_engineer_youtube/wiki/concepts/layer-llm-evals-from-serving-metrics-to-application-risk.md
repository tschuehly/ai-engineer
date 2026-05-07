# Layer LLM evals from serving metrics to application risk

Summary: Production LLM evaluation should be layered from hard serving constraints up to application-specific risk checks. A model that scores well on factual tasks can still be unusable if it is too slow, too expensive, badly formatted, unsafe, biased, or untested against the product's own failure modes.

Use when:
- Designing the first eval plan for a production LLM application.
- Deciding which eval layer to add next when time and compute budget are limited.

Details:
- The talk distinguishes broad evaluation from benchmarking: benchmarks are controlled data and task comparisons, while evaluation is the wider end-to-end assessment of model and system behavior. (09:26-10:24)
- Smith recommends an incremental approach: start with a component such as RAG chunk retrieval or latency/throughput, then expand into integration, UI, and end-to-end tests by priority. (12:12-13:26)
- The eval pyramid starts with system performance, then adds formatting checks, factual accuracy benchmarks, safety and bias checks, and finally application-specific custom evaluations. (13:30-14:52)
- Safety and bias evals are treated as release-prevention work, not only post-incident mitigation, because failures such as satire retrieval or skewed training data can damage customers and company credibility. (07:13-09:25)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Map application evals to the product court](map-application-evals-to-the-product-court.md)
- [Prefer simple debuggable eval scores](prefer-simple-debuggable-eval-scores.md)
- [Guardrail evaluation is part of production AI evaluation](llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md)

Sources:
- [Strategies for LLM Evals (GuideLLM, lm-eval-harness, OpenAI Evals Workshop) - Taylor Jordan Smith](../sources/20250727_89NuzmKokIk.md), 07:13-14:52
