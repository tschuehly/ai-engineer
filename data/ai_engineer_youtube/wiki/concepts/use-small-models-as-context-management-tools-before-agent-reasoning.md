# Use Small Models as Context-Management Tools Before Agent Reasoning

Summary: Small models can act as preprocessing and retrieval tools that reduce context rot before a larger agent reasons over the task. This is useful when embeddings, rerankers, named entity recognition, classification, or extraction can shrink or structure the input better than sending raw context to the main model.

Use when:
- An agent workflow is losing quality because the context window is growing with low-value or poorly structured input.
- The task can be decomposed into search, reranking, classification, extraction, ontology construction, or other narrow preprocessing steps.

Details:
- Context rot is presented as quality degradation as context increases; small models can preprocess data so the agent sees more useful context. (04:42-05:17)
- Small models can complement code search or grep by making the underlying file system or knowledge base more structured before deterministic search runs. (05:27-05:44)
- Examples include named entity recognition for ontology or knowledge graph generation, Chroma-style context filtering, token reduction, and e-commerce taxonomy classification. (05:51-06:59)

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md)
- [Evaluate retrieval and MCP layers by task value, not only response availability](evaluate-retrieval-and-mcp-layers-by-task-value.md)

Sources:
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md), 04:42-06:59
