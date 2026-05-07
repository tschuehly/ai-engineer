# Context Engineering: Connecting the Dots with Graphs - Stephen Chin, Neo4j

Source: [Context Engineering: Connecting the Dots with Graphs - Stephen Chin, Neo4j](https://www.youtube.com/watch?v=LLuKshphGOE)
Uploaded: 2025-11-24
Transcript: `raw/20251124_LLuKshphGOE/LLuKshphGOE.en-orig.vtt`

## Summary

Stephen Chin frames context engineering as information architecture for AI systems, where prompts, retrieval, state, memory, structured outputs, and tools work together to put relevant information near the top of the model context. The talk emphasizes knowledge graphs as a way to make context more structured, explainable, permission-aware, and traversable, including both two-pass GraphRAG pipelines and agentic MCP workflows where Claude Code uses the Neo4j Cypher MCP server to inspect graph schema and issue multi-step queries.

## Extracted Concepts

- [Knowledge graphs make agent memory traversable and explainable](../concepts/knowledge-graphs-make-agent-memory-traversable-and-explainable.md) - this source explains how graph structure can store facts, relationships, embeddings, access overlays, and interaction learnings as inspectable context.
- [Agentic GraphRAG uses schema-aware multi-step graph queries](../concepts/agentic-graphrag-uses-schema-aware-multi-step-graph-queries.md) - this source demonstrates an agent retrieving a graph schema, issuing Cypher queries, and pulling related text chunks for a richer answer.
- [Choose HybridRAG when relationship structure matters](../concepts/choose-hybridrag-when-relationship-structure-matters.md) - this source reinforces that graphs add relationship, community, and domain structure beyond vector similarity.
- [Context window editing clears stale tool results](../concepts/context-window-editing-clears-stale-tool-results.md) - this source adds a GraphRAG-adjacent reminder that past tool dumps can crowd out useful current context.

## Topic Links

- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)
- [Tools](../topics/tools.md)

## Notes

- Context engineering shifts AI work from one-shot prompt phrasing toward dynamically curating domain-relevant information, especially in enterprise and business contexts where large windows can still fail to focus attention on the right evidence. 00:58-02:11
- The talk scopes context engineering across prompt instructions, RAG, state/history, short-term and long-term memory, structured outputs, applications, and tools. 02:46-04:03
- Short-term memory should prioritize relevant results high in the active context window while avoiding excessive previous tool outputs that fill the window with stale information. 04:17-04:43
- Long-term memory should capture semantic and structural meaning from past conversations and turn it into instructions, procedures, and planning guidance that can fill context gaps without adding noise. 04:45-05:26
- Knowledge graphs represent people, places, events, things, relationships, properties, and embeddings; this makes them readable by humans and LLMs and useful as organizational or process digital twins. 06:59-09:04
- GraphRAG is any retrieval pipeline that uses graph retrieval as part of answer construction, adding relationships, nodes, community grouping, domain facts, and inspectable evidence beyond vector similarity. 09:23-10:30
- Graph overlays can express role-based access constraints, such as separating clinical diagnosis access from administrative patient data, and then instruct the model on what it may answer with. 10:30-11:05
- A two-pass GraphRAG demo first performs vector lookup to find related graph nodes, then expands to related nodes and passes those graph facts to the LLM as context. 14:02-14:43
- In the Claude Code demo, the Neo4j Cypher MCP server lets the agent retrieve the graph schema, generate multiple Cypher queries, retrieve vulnerability context and text chunks, and produce a more detailed remediation answer than the faster fixed retrieval flow. 21:33-24:36
