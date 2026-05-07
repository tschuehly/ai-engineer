# Train Graph-query Agents With Schemas And Example Queries

Summary: When a graph-query agent repeatedly burns tokens exploring schema layers, schema-aware fine-tuning or equivalent training data can move graph access from broad ReAct exploration toward faster targeted queries.

Use when:
- An agent repeatedly queries a large operational graph with high token use or latency.
- Deciding whether to keep graph schema purely in prompt/RAG context or train a specialized query agent.

Details:
- Cisco's application includes an assistant/planner plus specialized ReAct-style agents, with a query agent responsible for regular interaction with the knowledge graph. 11:12-11:42
- The team first attempted graph querying through ReAct-style reasoning, but AQL queries traversed too many graph layers and consumed many tokens and time. 11:42-12:18
- Fine-tuning the query agent with schema information and example queries reduced token consumption and result latency. 11:53-12:25
- This is a narrower alternative to unbounded agentic GraphRAG: the query behavior is optimized around a known operational schema and recurring query workload. 11:42-12:25

Related topics:
- [Agents](../topics/agents.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Agentic GraphRAG uses schema-aware multi-step graph queries](agentic-graphrag-uses-schema-aware-multi-step-graph-queries.md)
- [Train long-tail knowledge into weights with curated synthetic data](train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md)

Sources:
- [Multi Agent AI and Network Knowledge Graphs for Change — Ola Mabadeje, Cisco](../sources/20250822_m0dxZ-NDKHo.md), 11:12-12:25
