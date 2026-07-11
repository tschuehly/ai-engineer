# Layer AI Application Metrics From Guardrail Compliance to System Health

Summary: Evaluate a production AI application with a layered ladder of application-level metrics — input/output guardrail compliance, response quality, at least one domain metric, and system health — and keep the same metrics running after ship as online monitoring, adding implicit success indicators. This is the application-metric complement to a model-focused eval pyramid.

Use when:
- Writing the first eval plan for a RAG or agentic application and deciding which metrics to define.
- Deciding what to keep tracking in production after the offline evals pass.
- A system has guardrails but no metric on how often they fire or whether outputs are actually grounded.

Details:
- **Guardrails first, because LLM systems are probabilistic** and can produce unexpected/incorrect/harmful output (not a pre-LLM concern); you define the acceptable boundaries. *Input* guardrails detect invalid/irrelevant/harmful inputs (e.g. "write me a poem" to a claims system → reject); *output* guardrails detect invalid/incorrect/hallucinated/harmful outputs (e.g. a response with no citations is invalid). (21:12-22:16)
- **The metric ladder (four tiers):** (1) guardrail-compliance rates — input (e.g. claim-rejection rate; too high → investigate, but you can only investigate what you measured) and output (e.g. missing-citation rate); (2) **response quality**, e.g. *faithfulness* — is the decision actually rooted in the retrieved sources; (3) at least one **domain/application-specific** metric tied to the North Star (e.g. claim processing time); (4) **system-health** metrics — average token cost/usage, average turns per conversation, cost per recommendation. (22:00-24:00)
- **Monitoring continues the same metrics online** and adds *implicit* indicators of user success and system health: how often a human overrides the AI verdict (want it low; rising above a threshold → investigate) and how long a human takes to review the AI recommendation (too long can mean verbose/confusing responses). (23:59-25:10)
- Motivating principle: "you can't improve what you can't measure" — build evaluation in from the start rather than bolting metrics on after a demo. (28:14-28:22)
- Distinct from a *model* eval pyramid (serving metrics → formatting → factual accuracy → safety/bias → custom): this ladder is about the *application's* own compliance, grounding, domain outcome, and operational health, and it is explicitly designed to carry from offline eval into online monitoring.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Layer LLM evals from serving metrics to application risk](layer-llm-evals-from-serving-metrics-to-application-risk.md)
- [Design AI systems requirements-first with a four-phase framework](design-ai-systems-requirements-first-with-a-four-phase-framework.md)
- [Run eval suites in CI/CD before and during production](run-eval-suites-in-cicd-before-and-during-production.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)

Sources:
- [AI System Design: From Idea to Production - Apoorva Joshi, MongoDB](../sources/20260628_T0HhO4YtTfE.md), 21:12-25:10
