# AI Search Providers Should Return Grounding Documents

Summary: AI search providers should expose the retrieved documents used to produce an answer, not only final citations. Grounding-document visibility enables reference-free metrics, hallucination checks, and scalable debugging of why an answer was incomplete, unsupported, or overconfident.

Use when:
- Designing AI search APIs, RAG observability, or provider evaluation harnesses.
- Debugging generated answers where citations alone do not show the evidence actually used.

Details:
- Quotient and Tavily's eval workflow generates answer context for each question-answer pair so reviewers can trace which sources and evidence produced the pair (08:02-08:29).
- In their provider comparison, only three evaluated providers returned the retrieved documents used to generate answers; most returned citations only, which the speakers described as largely unhelpful for debugging at scale (15:56-16:14).
- Document relevance and hallucination metrics depend on seeing grounding documents, because they compare the response and retrieved evidence rather than a separate labeled answer (14:32-15:55).
- Grounding-document visibility helps distinguish retrieval failures from generation failures: irrelevant documents with an answer suggest unsupported generation, while relevant documents with incomplete answers suggest synthesis or coverage issues (16:18-19:23).

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Show Retrieved Chunks Inside Agent Workflows](show-retrieved-chunks-inside-agent-workflows.md)
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Benchmark RAG Pipelines After Production Usage Exists](benchmark-rag-pipelines-after-production-usage-exists.md)

Sources:
- [Evaluating AI Search: A Practical Framework for Augmented AI Systems - Quotient AI + Tavily](../sources/20250729_wRJD0inpmjU.md), 08:02-19:23
