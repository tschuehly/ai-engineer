# Dynamic Workflow Prompting Fits Changing Enterprise Behavior

Summary: Dynamic workflow prompting retrieves current workflow examples at runtime, making it better suited than fine-tuning for fast-changing enterprise practices and personalized team behavior. Fine-tuning remains useful when a stable behavior should generalize across many examples.

Use when:
- Tools, business priorities, or team-specific procedures change often enough that retraining would lag practice.
- The behavior is a last-mile enterprise quality issue rather than a stable universal capability.

Details:
- Fine-tuning with SFT or RLHF can learn well from many task/workflow examples, but it creates a fork from the frontier model and requires retraining when tools, priorities, or processes change (11:18-13:02).
- Fine-tuning is less flexible for personalization because different teams or employees may have different optimal workflows for the same nominal task (13:02-13:16).
- Dynamic prompting through search is more interpretable because operators can inspect the exact workflow examples that influenced the output (15:15-15:28).
- The talk frames fine-tuning as custom hardware for stable requirements and dynamic prompting as software that is less optimized but much easier to change (15:28-16:24).

Related topics:
- [Agents](../topics/agents.md)
- [Retrieval](../topics/retrieval.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Workflow Search Retrieves Enterprise Practice at Runtime](workflow-search-retrieves-enterprise-practice-at-runtime.md)
- [Prefer Model-Portable Agentic Prompts Before Fine-Tuning](prefer-model-portable-agentic-prompts-before-fine-tuning.md)

Sources:
- [How to build Enterprise Aware Agents - Chau Tran, Glean](../sources/20250724_hxFpUcvWPcU.md), 11:18-16:24
