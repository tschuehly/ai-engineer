# Prefer Model-Portable Agentic Prompts Before Fine-Tuning

Summary: Multi-model enterprise platforms may get more practical leverage from prompts, cached prompts, and agentic workflow structure than from fine-tuning every supported model variant.

Use when:
- Supporting multiple foundation-model providers in one enterprise AI product.
- Considering fine-tuning for a workflow that can still be improved through decomposition, prompting, verification, or model routing.

Details:
- Box supports multiple model families, including Gemini, Llama, OpenAI, and Anthropic, which makes consistent fine-tuning across all supported providers and future model versions operationally difficult.
- For Box's extraction and content-agent use cases, prompts, cached prompts, and agentic workflow design have been preferred over fine-tuning because newer base models often improve and the workflow must remain provider-portable.
- This is a use-case-specific stance rather than a general rejection of model adaptation: it applies when model portability, rapid provider evolution, and workflow orchestration dominate the optimization problem.

Related topics:
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Use Agent RFT after baseline and task optimization](use-agent-rft-after-baseline-and-task-optimization.md)
- [Train long-tail knowledge into weights with curated synthetic data](train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md)

Sources:
- [Building an Agentic Platform - Ben Kus, CTO Box](../sources/20250824_12v5S1n1eOY.md), 18:18-18:54
