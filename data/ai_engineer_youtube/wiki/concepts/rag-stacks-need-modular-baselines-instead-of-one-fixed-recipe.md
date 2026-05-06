# RAG Stacks Need Modular Baselines Instead Of One Fixed Recipe

Summary: RAG applications share common components, but each corpus, user population, question style, and quality expectation changes which pipeline choices work. A good RAG stack should provide a strong baseline while leaving parsing, chunking, embedding, retrieval, model, guardrail, and orchestration choices tunable.

Use when:
- Designing a RAG system and deciding whether to start from a framework baseline or build every component from scratch.
- Evaluating claims that large context windows or simple top-k vector search make RAG "solved."

Details:
- The talk rejects the idea that RAG is dead simply because context windows are large; repeatedly paying for huge prompt inputs is still unattractive, and many businesses have more than a convenient prompt-sized data set.
- RAG remains hard because PDFs, chunking strategies, embedding upgrades, search techniques, chunk summaries, chunk expansion, query rewriting, and reranking can all affect quality.
- OpenRAG's intended shape is opinionated but customizable: Docling, OpenSearch, and LangFlow provide a baseline while still allowing changes for each data set and user workflow.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Evaluate retrieval and MCP layers by task value, not only response availability](evaluate-retrieval-and-mcp-layers-by-task-value.md)
- [Context engines select task-specific organizational context](context-engines-select-task-specific-organizational-context.md)

Sources:
- [OpenRAG: An open-source stack for RAG - Phil Nash](../sources/20260408_4TxOBhDRRCM.md), 00:20-02:08, 14:17-14:46
