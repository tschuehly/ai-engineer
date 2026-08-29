# Fresh Markdown Context Mitigates Model Rot in Codegen

Summary: Code-generation agents fail when their model snapshot predates a fast-moving API or project. Current Markdown documentation selected at runtime can patch model knowledge without retraining.

Use when:
- An agent invents keys, APIs, configuration patterns, or setup steps for a fast-changing integration.
- A product team needs to decide whether to rely on model priors, RAG, or current docs for codegen.

Details:
- Model rot is the gap between the training snapshot and current project reality; for fast-moving software, a model trained months earlier may not know what changed. 02:15-03:07
- PostHog mitigates this by letting the agent choose from fresh Markdown documentation, load the relevant docs into context, and then apply the current integration pattern. 03:27-04:08
- The failure mode is product-facing even when the model caused it: users saw agents making up keys, patterns, and nonexistent APIs while trying to integrate PostHog. 04:09-04:48

- **Freshness cuts both ways, and the removal half is the one teams skip.** Amazon's context habit has an addition trigger and a subtraction trigger running together: "every time the agent makes a mistake or does something not the way that you would have done it, what am I missing in my skills files? What am I missing in my steering files that the agent needed?" — and, as models improve, "do I still need this in my steering files or is this just bloating context?" The material being pruned is specifically compensation for a superseded model's quirks ("a lot of do nots" written for Sonnet 3.7, largely unnecessary by Opus 4.5). A context file kept fresh only by addition drifts toward being a record of models that no longer exist. ([Liguori](../sources/20260828_pqlWNihgdjI.md), 08:47-09:39)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Agent skills should point to current docs instead of embedding every API detail](agent-skills-should-point-to-current-docs-instead-of-embedding-every-api-detail.md)
- [Do not cache context-engine answers as durable truth](do-not-cache-context-engine-answers-as-durable-truth.md)
- [A Harness Fix Becomes Overhead When the Model Outgrows It](a-harness-fix-becomes-overhead-when-the-model-outgrows-it.md)

Sources:
- [LLM codegen fails and how to stop 'em - Danilo Campos, PostHog](../sources/20260430_juoNbJiZUi0.md), 02:15-04:48
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 08:47-09:39
