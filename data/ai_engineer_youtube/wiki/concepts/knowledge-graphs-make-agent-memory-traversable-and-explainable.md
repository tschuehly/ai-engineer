# Knowledge Graphs Make Agent Memory Traversable And Explainable

Summary: Knowledge graphs can turn agent memory and enterprise context into explicit nodes, relationships, properties, embeddings, and access overlays. This gives agents structured context they can traverse while giving humans an inspectable view of what evidence shaped an answer.

Use when:
- Designing long-term agent memory that needs relationship-aware retrieval rather than only conversation summaries.
- Building enterprise context layers where provenance, access control, and explainability matter.

Details:
- Context engineering should act more like information architecture than prompt phrasing: curate domain-relevant context, structure inputs, and put high-signal evidence where the model will attend to it. 00:58-02:11
- Short-term memory needs relevant current evidence plus selected tool results, but previous tool dumps can fill the window and degrade attention. 04:17-04:43
- Long-term memory should extract semantic and structural meaning from prior conversations into instructions, procedures, and planning guidance rather than replaying raw history. 04:45-05:26
- Knowledge graphs model facts as nodes, relationships, and properties, and can also store embeddings for vector lookup alongside relationship traversal. 06:59-09:04
- Graph context can be explained because the system can inspect which graph nodes and relationships were passed to the model. 10:22-10:30
- Graph overlays can encode role-based access rules before context reaches the model, such as separating clinical diagnosis access from administrative patient information. 10:30-11:05

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Choose HybridRAG when relationship structure matters](choose-hybridrag-when-relationship-structure-matters.md)
- [Do not treat long context as durable model memory](do-not-treat-long-context-as-durable-model-memory.md)
- [Context window editing clears stale tool results](context-window-editing-clears-stale-tool-results.md)

Sources:
- [Context Engineering: Connecting the Dots with Graphs - Stephen Chin, Neo4j](../sources/20251124_LLuKshphGOE.md), 00:58-11:05
