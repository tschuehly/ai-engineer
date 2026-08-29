# Neural Web Search Supports Semantic Agent Queries

Summary: Neural web search embeds documents and queries so retrieval can match meaning, negation, and long-form intent instead of only overlapping keywords.

Use when:
- Choosing between keyword search and embedding-backed web retrieval for agent RAG.
- Debugging failures where exact words match but the requested semantics do not.

Details:
- Exa frames traditional web search as an inverted keyword index plus ranking, while neural search represents documents and queries as embeddings that can capture meaning, ideas, and how documents are referred to on the web.
- The talk uses "shirts without stripes" as a simple failure mode for keyword search: a keyword engine can overmatch the word "stripes," while a semantic system can represent the negation and retrieve non-striped shirts.
- Web-scale neural search still needs high-quality data and transformer training; the claim is not that vector search is automatically sufficient, but that learned representations give a broader substrate than keyword matching for paragraph-length or semantic queries.
- **The same substrate used for exhaustive classification rather than for query answering.** Exa's own go-to-market team turns the neural index inward: "we take the internet, we crawl it, we train embeddings to do web search really well… you can think about Exa as like embeddings over the internet. And when you have embeddings over the internet you have this like arbitrarily powerful semantic filtering and slicing and dicing of any type of data that you want," which is used to classify "basically like every possible company that is inside of our total addressable market." Retrieval returns the top matches for a query; the same representation supports partitioning the whole corpus, and that second use is what makes an ICP dashboard rather than an account lookup. No accuracy figure is given for the classification. ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 05:22-06:58)

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Choose Lexical, Vector, and Reranking Retrieval by Query Shape](choose-lexical-vector-and-reranking-retrieval-by-query-shape.md)
- [Agentic Retrieval Lets Models Plan Search Steps](agentic-retrieval-lets-models-plan-search-steps.md)
- [Classify the Whole Addressable Market Instead of Searching It Account by Account](classify-the-whole-addressable-market-instead-of-searching-it.md)

Sources:
- [Building a Smarter AI Agent with Neural RAG - Will Bryk, Exa.ai](../sources/20250729_xnXqpUW_Kp8.md), 01:48-05:18
- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md), 05:22-06:58
