# Prefer Model-Portable Agentic Prompts Before Fine-Tuning

Summary: Multi-model enterprise platforms may get more practical leverage from prompts, cached prompts, and agentic workflow structure than from fine-tuning every supported model variant.

Use when:
- Supporting multiple foundation-model providers in one enterprise AI product.
- Considering fine-tuning for a workflow that can still be improved through decomposition, prompting, verification, or model routing.

Details:
- Box supports multiple model families, including Gemini, Llama, OpenAI, and Anthropic, which makes consistent fine-tuning across all supported providers and future model versions operationally difficult.
- For Box's extraction and content-agent use cases, prompts, cached prompts, and agentic workflow design have been preferred over fine-tuning because newer base models often improve and the workflow must remain provider-portable.
- This is a use-case-specific stance rather than a general rejection of model adaptation: it applies when model portability, rapid provider evolution, and workflow orchestration dominate the optimization problem.
- The prompt can be the most *architecture-portable* layer, not just the most provider-portable: Witan Labs found that adding domain knowledge to the prompt "survived all of the different iterations of the tools" and "always produced improved results," and "almost the exact same prompt would work for the REPL or the individual tools or any of the other approaches" — so investment in the prompt outlasts churn in the tool/interface layer beneath it. ([Witan Labs](../sources/20260708_HEFSExa0xl0.md), 12:37-13:25, 18:01-18:16)
- The mechanism is reminding, not teaching: LLMs already "know many many things," so domain knowledge in the prompt exists to "pigeonhole them a little bit into what you want them to focus on… remind it to pay more attention to that than other things" for the specific task — a cheaper and more portable lever than baking that focus into weights. ([Witan Labs](../sources/20260708_HEFSExa0xl0.md), 12:46-13:16, 18:01-18:16)

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
- [Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs](../sources/20260708_HEFSExa0xl0.md), 12:37-13:25, 18:01-18:16
