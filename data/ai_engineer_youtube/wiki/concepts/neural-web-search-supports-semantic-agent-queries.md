# Neural Web Search Supports Semantic Agent Queries

Summary: Neural web search embeds documents and queries so retrieval can match meaning, negation, and long-form intent instead of only overlapping keywords.

Use when:
- Choosing between keyword search and embedding-backed web retrieval for agent RAG.
- Debugging failures where exact words match but the requested semantics do not.

Details:
- Exa frames traditional web search as an inverted keyword index plus ranking, while neural search represents documents and queries as embeddings that can capture meaning, ideas, and how documents are referred to on the web.
- The talk uses "shirts without stripes" as a simple failure mode for keyword search: a keyword engine can overmatch the word "stripes," while a semantic system can represent the negation and retrieve non-striped shirts.
- Web-scale neural search still needs high-quality data and transformer training; the claim is not that vector search is automatically sufficient, but that learned representations give a broader substrate than keyword matching for paragraph-length or semantic queries.

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Choose Lexical, Vector, and Reranking Retrieval by Query Shape](choose-lexical-vector-and-reranking-retrieval-by-query-shape.md)
- [Agentic Retrieval Lets Models Plan Search Steps](agentic-retrieval-lets-models-plan-search-steps.md)

Sources:
- [Building a Smarter AI Agent with Neural RAG - Will Bryk, Exa.ai](../sources/20250729_xnXqpUW_Kp8.md), 01:48-05:18
