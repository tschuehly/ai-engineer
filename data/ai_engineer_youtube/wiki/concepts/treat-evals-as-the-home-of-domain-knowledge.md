# Treat Evals as the Home of Domain Knowledge

Summary: AI product judgment should be encoded in evals and scoring systems, not only in prompts or one-off review notes. Once the scorer captures the domain's definition of goodness, it can guide prompt optimization, synthetic-data filtering, fine-tuning, reinforcement learning, and online candidate selection.

Use when:
- Deciding where to put product-specific judgment for an AI application.
- Explaining why eval work is a core development activity rather than post-demo QA.

Details:
- The workshop frames evals as an ongoing quality methodology: set benchmarks, find metrics, calibrate against humans and user data, and keep improving them as the product changes, 06:43-07:18.
- The presenters argue that evals are where domain knowledge will live because other layers can work from those evals once the scoring system is reliable, 12:29-12:50.
- Good evals enable downstream automation: prompt optimizers such as DSPy, synthetic-data filtering for fine-tuning, reinforcement learning, and online scoring all depend on the scorer representing the intended behavior, 12:54-13:15.
- Generic helpfulness, harmlessness, and hallucination checks can be useful guardrails, but they do not capture nuanced application quality such as whether a generated travel plan is compelling for the user, 14:10-15:04.
- **If evals are where domain knowledge lives, the people who hold it need write access.** DoorDash draws the organizational consequence directly: "we needed to empower the people who are the domain experts, and in our case that was strategy and operations folks, it was product managers, it was even labeling partners, and not only engineers," because evals are "a cross functional effort… that actually helps us add all the domain specific knowledge into the quality of the AI itself." A scoring system that only engineers can author houses whatever domain knowledge the engineers happen to have, which is the failure this page's argument is meant to prevent. ([AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 02:50-03:07, 04:01-04:33)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Write custom scorers as product specifications](write-custom-scorers-as-product-specifications.md)
- [Use evals as durable AI system specifications](use-evals-as-durable-ai-system-specifications.md)
- [Optimize LLM programs with metrics and teacher feedback](optimize-llm-programs-with-metrics-and-teacher-feedback.md)
- [Keep Judge-Prompt Ownership Configurable While the Org Is Still Learning](keep-judge-prompt-ownership-configurable-while-the-org-is-still-learning.md)

Sources:
- [[Full Workshop] Building Metrics that actually work - David Karam, Pi Labs (fmr Google Search)](../sources/20250729_jxrGodnopHo.md), 06:43-07:18, 12:29-15:04
- [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 02:50-03:07, 04:01-04:33
