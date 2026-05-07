# Prompt Management Lags Prompt Iteration

Summary: Prompt iteration can be frequent even when prompt management is absent. That gap turns prompts into operational artifacts that need versioning, ownership, evaluation, and deployment hygiene.

Use when:
- Auditing whether an AI product treats prompts as managed production assets.
- Justifying prompt registries, diff review, eval gates, or ownership around shared prompt changes.

Details:
- Amplify's survey found that 70% of respondents updated prompts at least monthly and one in ten updated prompts daily. (05:40-05:49)
- Despite that iteration rate, 31% of respondents reported no way of managing prompts. (06:07-06:20)
- The operational risk is not simply untidy files: prompt updates can change product behavior more often than model updates, so unmanaged prompts weaken reproducibility and regression diagnosis.

Related topics:
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Context development lifecycle treats context as an engineered artifact](context-development-lifecycle-treats-context-as-an-engineered-artifact.md)
- [Treat prompts as distributed harness surfaces](treat-prompts-as-distributed-harness-surfaces.md)
- [Use evals as durable AI system specifications](use-evals-as-durable-ai-system-specifications.md)

Sources:
- [The 2025 AI Engineering Report - Barr Yaron, Amplify](../sources/20250801_mQ7_Zje7WKE.md), 05:40-06:20
