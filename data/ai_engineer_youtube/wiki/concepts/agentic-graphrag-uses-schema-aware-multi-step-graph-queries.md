# Agentic GraphRAG Uses Schema-Aware Multi-Step Graph Queries

Summary: Agentic GraphRAG lets an agent inspect a graph schema, generate graph queries, traverse relationships, and retrieve supporting chunks iteratively. This is slower than a fixed retrieval pass, but can produce richer answers when the task needs detailed relationship context.

Use when:
- Exposing a graph database to a coding or research agent through MCP or another tool interface.
- Choosing between a fast fixed GraphRAG flow and a slower agentic graph-exploration workflow.

Details:
- A simple GraphRAG pipeline can run as a two-pass process: vector lookup finds related graph nodes, then related nodes are expanded and passed to the LLM as answer context. 14:02-14:43
- In the demo, Claude Code connects to a Neo4j Cypher MCP server configured with database settings and query keywords. 21:33-22:13
- The agent first retrieves the graph schema so it can understand node labels, relationships, and graph structure before querying for the requested vulnerability. 22:21-22:46
- After schema inspection, the agent issues multiple Cypher queries, retrieves vulnerability nodes, and pulls related text chunks attached to those nodes. 22:46-23:24
- The agentic MCP retrieval flow is slower than the earlier fixed retrieval path, but it returns a more detailed vulnerability answer including CVE, affected component, attack type, severity, technical description, remediation versions, and advisory context. 23:24-24:36

Related topics:
- [Agents](../topics/agents.md)
- [Retrieval](../topics/retrieval.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Agentic retrieval lets models plan search steps](agentic-retrieval-lets-models-plan-search-steps.md)
- [Choose HybridRAG when relationship structure matters](choose-hybridrag-when-relationship-structure-matters.md)
- [MCP tool surfaces need default context budgets](mcp-tool-surfaces-need-default-context-budgets.md)

Sources:
- [Context Engineering: Connecting the Dots with Graphs - Stephen Chin, Neo4j](../sources/20251124_LLuKshphGOE.md), 14:02-14:43, 21:33-24:36
