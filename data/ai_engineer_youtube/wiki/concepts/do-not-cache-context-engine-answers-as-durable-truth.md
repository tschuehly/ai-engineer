# Do Not Cache Context-Engine Answers as Durable Truth

Summary: Cache source-derived structures or retrieval aids carefully, but do not treat a context-engine answer as durable truth for future tasks. Code, docs, and rationale change, and reusing prior answers can pollute later context.

Use when:
- Designing persistence, memory, or caching for context engines and agent retrieval systems.
- Debugging stale or self-reinforcing answers in coding-agent workflows.

Details:
- The speaker calls answer caching a bad idea: similar future questions should not automatically receive the same prior context-engine answer. (24:42-24:57)
- Complete answers go stale because code changes, docs change, and the reasons behind decisions change. (24:58-25:08)
- Feeding prior answers into later answers can regress behavior toward previous mistakes; if a model was misbehaving, repeatedly adding its old output pollutes context. (25:10-25:28)
- A safer pattern is to recompute from current sources and use durable source-backed memories, graphs, and retrieval tools as inputs rather than treating generated conclusions as canonical. (19:10-19:41, 38:26-39:19)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md)
- [Use small models as context-management tools before agent reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)

Sources:
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md), 19:10-19:41, 24:42-25:28, 38:26-39:19
