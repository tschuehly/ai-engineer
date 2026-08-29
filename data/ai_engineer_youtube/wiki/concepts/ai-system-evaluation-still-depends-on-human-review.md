# AI System Evaluation Still Depends on Human Review

Summary: AI system evaluation in practice remains a layered mix of observability, offline evals, user data, benchmarks, internal metrics, and human review. Human review remains the most common quality check in the survey, while evaluation itself is reported as the top pain point.

Use when:
- Designing an eval plan for an AI system already in production.
- Explaining why observability or benchmarks alone do not replace human quality review.

Details:
- Respondents used multiple monitoring methods: 60% reported standard observability and over 50% relied on offline evals. (08:52-09:12)
- For model and system quality, respondents combined methods including user data collection and benchmarks, but human review was still the most popular method. (09:14-09:28)
- Most respondents relied on internal metrics for monitoring their own model usage. (09:28-09:33)
- Evaluation topped the survey's list of the most painful things about AI engineering. (11:16-11:31)
- **Human review is not only the most common method, it is a standing per-unit bill.** DoorDash's platform team describes the volume plainly — "we do have thousands of rows that need to get annotated every week and it can get pretty expensive at DoorDash scale" — with the spend going to external annotators rather than to engineering time. That reframes the survey finding: human review persisting as the top quality method is also a recurring operating cost that scales with traffic, which is why the platform improvements they report are measured as "reduction in the spend at per annotation cost" rather than as better scores. No figure is given for the reduction. ([AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 13:58-14:33)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Monitor whole agent systems, not single models](monitor-whole-agent-systems-not-single-models.md)
- [Use evals as durable AI system specifications](use-evals-as-durable-ai-system-specifications.md)
- [Ship Stable APIs and Let Users Vibe-Code the Interface](ship-stable-apis-and-let-users-vibe-code-the-interface.md)

Sources:
- [The 2025 AI Engineering Report - Barr Yaron, Amplify](../sources/20250801_mQ7_Zje7WKE.md), 08:52-11:31
- [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 13:58-14:33
