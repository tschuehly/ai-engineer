# Workflow Search Retrieves Enterprise Practice at Runtime

Summary: Workflow search maps a new task to similar prior task-workflow examples and feeds those workflow representations to the agent as runtime guidance. It gives enterprise agents company-specific process context without forcing every changing workflow into model weights.

Use when:
- An agent needs to follow internal practices, protocols, or metrics that are not obvious from the task text.
- A workflow library exists or can be mined from successful agent traces, documents, or user-authored process descriptions.

Details:
- A task-to-golden-workflow dataset can be searched at runtime so the LLM sees examples of how similar work is done inside the company (13:18-13:51).
- The retrieval result can steer behavior along a determinism-to-creativity spectrum: no close workflow match leaves room for agent invention, while a high-confidence match should make the model produce a workflow close to known practice (13:51-14:20).
- Workflow search resembles document search but needs enterprise ranking signals beyond textual similarity; when many workflows look similar, authoritativeness can depend on creator proximity, historical success rate, and workplace discussion signals such as Slack posts (16:24-18:18).

Related topics:
- [Agents](../topics/agents.md)
- [Retrieval](../topics/retrieval.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Context Engines Select Task-Specific Organizational Context](context-engines-select-task-specific-organizational-context.md)
- [Use Social and Expert Graphs to Personalize Coding-Agent Context](use-social-and-expert-graphs-to-personalize-coding-agent-context.md)

Sources:
- [How to build Enterprise Aware Agents - Chau Tran, Glean](../sources/20250724_hxFpUcvWPcU.md), 13:18-18:18
