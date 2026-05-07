# Ground Regulated Explanations in Deterministic Engines

Summary: In regulated domains, LLMs can explain outcomes without owning the authoritative calculation. Keep exact numbers and eligibility outputs in deterministic systems, then constrain the model to explain those outputs with guardrails that detect invented values.

Use when:
- Building LLM explanations for taxes, finance, healthcare, compliance, or other high-liability workflows.
- Deciding which parts of a user-facing answer should come from deterministic engines versus generative text.

Details:
- TurboTax uses LLMs to help users understand tax summaries, deductions, credits, withholding, and tax outcomes, but the underlying numbers come from Intuit's proprietary tax knowledge engine rather than model arithmetic, 03:04-03:29, 15:37-15:58.
- The speaker explicitly says they are not having LLMs do the calculations; the LLM consumes existing ground-truth numbers from internal systems, 15:49-15:58.
- Safety guardrails check raw LLM responses before user delivery so generated explanations do not hallucinate numbers, 15:58-16:36.
- Expert-crafted prompts and per-piece evals are used because wrong tax answers carry legal and privacy risk, 18:16-18:47.

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Security](../topics/security.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Keep Fixed Business Logic Outside the Model](keep-fixed-business-logic-outside-the-model.md)
- [Regulated Agents Need Explainability, Isolation, Governance, and Speed](regulated-agents-need-explainability-isolation-governance-and-speed.md)
- [Build Domain-Specific Workflow Wrappers Around Models](build-domain-specific-workflow-wrappers-around-models.md)

Sources:
- [How Intuit uses LLMs to explain taxes to millions of taxpayers - Jaspreet Singh, Intuit](../sources/20250723__zl_zimMRak.md), 03:04-03:29, 15:37-16:36, 18:16-18:47
