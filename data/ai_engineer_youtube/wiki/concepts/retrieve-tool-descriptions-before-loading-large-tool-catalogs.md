# Retrieve Tool Descriptions Before Loading Large Tool Catalogs

Summary: When an agent has access to thousands of tools, store tool descriptions in a searchable knowledge base and retrieve a small relevant set before loading executable tool schemas into model context.

Use when:
- A product or platform has too many tools to expose in one model context window.
- The agent needs broad capability discovery without paying the context and selection cost of every tool on every run.

Details:
- AWS describes an internal agent with over 6,000 tools, which is too many descriptions and schemas to place in one model context for selection. (10:57-11:13)
- The described mitigation stores tool descriptions in a knowledge base and uses a `retrieve` tool for semantic search over that catalog. (10:47-11:18)
- The agent pulls only the relevant tools back into model context, then lets the model choose among that narrowed set. (11:18-11:30)
- Prosodica frames the same pattern as a **Semantic Tool Router** — "RAG for tools": each tool has a clear description; the descriptions are embedded offline into a vector index (Chroma, Pinecone, Qdrant) when the catalog is created or updated; at runtime the user query is embedded with the same model, a nearest-neighbor / cosine search returns the top-K (K≈3–5) closest tool descriptions, and only those schemas are injected into the model call. If you already have an embedding model and vector DB, the infrastructure is familiar. (vh2VGuQ3zhY 09:20-16:40)
- The retrieval step does more than narrow — it *removes* the wrong tools from the model's choice set, cutting cross-tool confusion, not only adding the right one. (vh2VGuQ3zhY 18:30-20:00)
- Community signal for the same move: Anthropic's on-demand tool loading via MCP reported token usage dropping from 150k to 2,000 (98.7% reduction), and MCP Zero explores routing across thousands of tools spanning many servers. (vh2VGuQ3zhY 12:10-12:40, 26:10-26:20)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [MCP Tool Surfaces Need Default Context Budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Discover Large API Tool Surfaces Progressively](discover-large-api-tool-surfaces-progressively.md)
- [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [The Fat-Agent Tool Overload Collapses Accuracy and Inflates Latency](fat-agent-tool-overload-collapses-accuracy-and-latency.md)
- [Tune a tool router with a K-sweep and guard its failure modes](tune-a-tool-router-with-k-sweep-and-guard-its-failure-modes.md)

Sources:
- [Building Agents at Cloud Scale - Antje Barth, AWS](../sources/20250802_WJjInLeaJjo.md), 10:47-11:30
- [The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica](../sources/20260628_vh2VGuQ3zhY.md), 09:20-16:40, 18:30-20:00
