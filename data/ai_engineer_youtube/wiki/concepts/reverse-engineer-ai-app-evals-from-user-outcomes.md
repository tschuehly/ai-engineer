# Reverse-engineer AI app evals from user outcomes

Summary: AI application evals should begin with the user-visible or business outcome the product must achieve, then derive task-specific checks from that outcome. Generic scores can be useful diagnostics, but they are weak release gates when they do not measure the real job.

Use when:
- Choosing success metrics for a production AI app instead of relying on groundedness, factuality, bias, or average quality scores alone.
- Translating product requirements into scenario-level eval criteria.

Details:
- A support bot can be grounded and factual yet still fail if it does not give the answer the user expects or escalates cases that the product should resolve automatically, 02:49-04:17.
- Metrics should be reverse-engineered from product experience and business outcomes; in the support-bot example, the relevant measure was the rate of escalation from the AI bot to human support, 03:31-04:17.
- Scenario evals should specify the exact information that must appear in the answer, such as SMS validation and alternate support paths for a password-reset flow, 05:24-06:40.
- Personas and wording variants matter because different users can ask for the same outcome in different ways while the expected answer criteria remain the same, 06:55-08:22.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use golden data sets and mixed scoring functions for AI application confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)
- [Split LLM Judges Into Narrow Binary Metrics](split-llm-judges-into-narrow-binary-metrics.md)

Sources:
- [Practical tactics to build reliable AI apps — Dmitry Kuchin, Multinear](../sources/20250803_-T6uZYYzkWw.md), 02:49-08:22
