# Show Retrieved Chunks Inside Agent Workflows

Summary: RAG-backed agent products should expose the retrieved evidence that shaped an output, not only the final generated artifact. Showing retrieved chunks inside the work UI helps operators inspect whether the agent used relevant context and gives product teams a concrete surface for debugging retrieval and hallucination issues.

Use when:
- Designing RAG-backed workflows where users need to trust or debug the evidence behind generated messages.
- Giving sales, support, research, or operations teams a way to inspect agent knowledge without opening trace logs.
- Building product UI around retrieval rather than treating retrieval as invisible backend plumbing.

Details:
- 11x describes visualization as the fifth step in the RAG pipeline after parsing, chunking, storage, and retrieval. (07:36-07:49)
- In the Alice knowledge-base UI, users can inspect the content Alice knows, click generated questions, and see dropdowns of retrieved chunks that were used in the messaging flow. (19:42-20:21)
- This evidence surface turns "what the agent knows" into a product-visible artifact that sales teams can use to demonstrate knowledge and that builders can use to debug retrieval-driven output quality. (19:08-20:21)

Related topics:
- [Agents](../topics/agents.md)
- [Retrieval](../topics/retrieval.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Make agent work more trustworthy by making it verifiable](make-agent-work-more-trustworthy-by-making-it-verifiable.md)
- [Enterprise deep research needs trustworthy retrieval and governance controls](enterprise-deep-research-needs-trustworthy-retrieval-and-governance-controls.md)
- [Evaluate retrieval and MCP layers by task value, not only response availability](evaluate-retrieval-and-mcp-layers-by-task-value.md)

Sources:
- [Building Alice's Brain: an AI Sales Rep that Learns Like a Human - Sherwood & Satwik, 11x](../sources/20250729_KWmkMV0FNwQ.md), 07:36-07:49, 19:08-20:21
