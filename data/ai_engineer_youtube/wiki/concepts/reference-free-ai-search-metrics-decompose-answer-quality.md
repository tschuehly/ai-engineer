# Reference-Free AI Search Metrics Decompose Answer Quality

Summary: When ground-truth answers are unavailable, AI search can still be evaluated by decomposing response quality into answer completeness, document relevance, and hallucination against retrieved evidence. These metrics measure different failure modes and should be interpreted together.

Use when:
- Evaluating production AI search traces without labeled answers.
- Diagnosing whether failures come from missing retrieval, incomplete generation, or unsupported claims.

Details:
- Answer completeness checks whether all components of a question were addressed, but completeness is not the same as correctness; a complete answer can still include unsupported claims (14:03-15:44).
- Document relevance measures what share of retrieved documents are actually useful for the question, and low relevance should push systems toward "I don't know" rather than unsupported answering (14:32-17:04).
- Hallucination detection checks whether factual claims in the response are absent from the retrieved documents, making grounding documents the next-best reference when ground truth is unavailable (14:38-15:55).
- The three metrics expose tradeoffs: higher completeness can come with higher hallucination risk when a system adds reasoning or interpretation beyond the retrieved evidence (17:04-18:25).
- Evaluation should do more than rank providers; metric combinations should point to repair strategies, such as retrieving more documents when answers are incomplete despite relevant evidence and no hallucinations (18:29-19:23).

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Treat Evals as the Home of Domain Knowledge](treat-evals-as-the-home-of-domain-knowledge.md)
- [Build Scoring Systems From Inspectable Quality Signals](build-scoring-systems-from-inspectable-quality-signals.md)
- [Evaluate retrieval and MCP layers by task value, not only response availability](evaluate-retrieval-and-mcp-layers-by-task-value.md)

Sources:
- [Evaluating AI Search: A Practical Framework for Augmented AI Systems - Quotient AI + Tavily](../sources/20250729_wRJD0inpmjU.md), 14:03-19:23
