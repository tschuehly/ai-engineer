# Use Fast Query-Document Evals for Retrieval Changes

Summary: Retrieval changes should be tested with cheap query-document pair evals before teams swap embedding models, chunking strategies, or retrieval parameters. The useful check is whether expected documents appear in the retrieved top-k set for the application's own data.

Use when:
- Comparing embedding models, chunking strategies, or top-k settings for a RAG system.
- A public benchmark looks compelling but may not match the application's corpus or query shape.
- Retrieval experiments are too slow or expensive to run often.

Details:
- A fast retrieval eval is a set of query/document pairs where each query has an expected document; the retrieval system is run over the queries and scored by whether the expected documents appear in the chosen result set, such as top 5, top 10, or top 20 (02:15-02:45).
- The goal is cheap iteration: if a metric takes hours and hundreds of dollars, teams will experiment less; fast retrieval evals should run quickly and cheaply enough to compare many configurations (02:45-03:06).
- Public leaderboards such as MTEB can be useful background, but local evals can rank models differently. In the Weights & Biases chatbot example, `text-embedding-3-small` performed worst among the tested models and Voyage 3 Large performed best for that local data (05:23-06:44).
- Retrieval quality should be considered before fine-tuning the LLM or changing higher-level behavior, because a better model will not fix missing or wrong retrieved context (16:34-16:55).

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [RAG stacks need modular baselines instead of one fixed recipe](rag-stacks-need-modular-baselines-instead-of-one-fixed-recipe.md)
- [Keep eval data constant and task logic variable](keep-eval-data-constant-and-task-logic-variable.md)

Sources:
- [How to look at your data - Jeff Huber (Chroma) + Jason Liu (567)](../sources/20250806_jryZvCuA0Uc.md), 02:15-06:44
