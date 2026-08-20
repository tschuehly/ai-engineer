# Last-Mile Domain Context Beats Model Chasing

Summary: In vertical AI applications, stronger models can establish a useful baseline, but the final performance gap often depends on customer-specific domain context and workflow interpretation. The durable advantage is a system that keeps translating expert insight into model-usable context.

Use when:
- Deciding whether a specialized AI product needs more model work or more domain-context infrastructure.
- Explaining why vertical AI products need workflow-specific context and expert iteration after general reasoning is good enough.

Details:
- Anterior frames the core bottleneck as whether the model understands the specific industry, customer, and workflow, not merely whether the base model can reason, 01:19-01:55.
- The clinical example shows that a seemingly simple policy question hides domain ambiguity around what qualifies as conservative therapy, what counts as unsuccessful treatment, and how much documentation can be inferred, 02:25-05:02.
- The talk reports that model and pipeline work reached a strong baseline around 95%, while the adaptive domain-intelligence loop pushed performance toward 99% by adding customer and domain context, 05:29-06:33.
- The structural reason this gap keeps appearing, from a different source: digital work is "millions of these micro worlds," each with "its unique local physics, like different structures, constraints, affordances, and dynamics that you have to learn," and "even if you're using the same software, every company configure it differently" ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 05:25-06:24). On that account Anterior's last five points are not a property of clinical review — they are what a general model structurally cannot hold, so the same gap should be expected in any vertical.
- The complementary framing for what the domain loop is actually supplying: intelligence "solves the problem through the context" it was handed, while expertise "will bring you the right context. Given any problem, we know what context [to] bring in are important" ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 09:20-09:49). Anterior's expert loop is a mechanism for acquiring that selection policy, which is why it keeps paying after the base model improves.

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Build Domain-Specific Workflow Wrappers Around Models](build-domain-specific-workflow-wrappers-around-models.md)
- [Resolve AI Capability Risk Before Product Surface Commitment](resolve-ai-capability-risk-before-product-surface-commitment.md)
- [Digital Work Is Millions of Microworlds With Local Physics](digital-work-is-millions-of-microworlds-with-local-physics.md)
- [Expertise Compresses the Search; Intelligence Expands It](expertise-compresses-the-search-intelligence-expands-it.md)

Sources:
- [Make your LLM app a Domain Expert: How to Build an Expert System - Christopher Lovejoy, Anterior](../sources/20250728_MRM7oA3JsFs.md), 01:19-06:33
- [Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 05:25-06:24, 09:20-09:49
