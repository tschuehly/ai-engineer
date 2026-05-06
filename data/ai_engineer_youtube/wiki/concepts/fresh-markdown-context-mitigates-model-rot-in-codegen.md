# Fresh Markdown Context Mitigates Model Rot in Codegen

Summary: Code-generation agents fail when their model snapshot predates a fast-moving API or project. Current Markdown documentation selected at runtime can patch model knowledge without retraining.

Use when:
- An agent invents keys, APIs, configuration patterns, or setup steps for a fast-changing integration.
- A product team needs to decide whether to rely on model priors, RAG, or current docs for codegen.

Details:
- Model rot is the gap between the training snapshot and current project reality; for fast-moving software, a model trained months earlier may not know what changed. 02:15-03:07
- PostHog mitigates this by letting the agent choose from fresh Markdown documentation, load the relevant docs into context, and then apply the current integration pattern. 03:27-04:08
- The failure mode is product-facing even when the model caused it: users saw agents making up keys, patterns, and nonexistent APIs while trying to integrate PostHog. 04:09-04:48

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Agent skills should point to current docs instead of embedding every API detail](agent-skills-should-point-to-current-docs-instead-of-embedding-every-api-detail.md)
- [Do not cache context-engine answers as durable truth](do-not-cache-context-engine-answers-as-durable-truth.md)

Sources:
- [LLM codegen fails and how to stop 'em - Danilo Campos, PostHog](../sources/20260430_juoNbJiZUi0.md), 02:15-04:48
