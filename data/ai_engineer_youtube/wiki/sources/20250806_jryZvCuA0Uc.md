# How to look at your data - Jeff Huber (Chroma) + Jason Liu (567)

Source: [How to look at your data - Jeff Huber (Chroma) + Jason Liu (567)](https://www.youtube.com/watch?v=jryZvCuA0Uc)
Uploaded: 2025-08-06
Transcript: `raw/20250806_jryZvCuA0Uc/jryZvCuA0Uc.en-orig.vtt`

## Summary

Jeff Huber and Jason Liu argue that AI teams should inspect their own application data before changing retrieval models, prompts, tools, or roadmaps. The talk separates input-side measurement, where fast query-document retrieval evals compare embeddings and chunking against local data, from output-side analysis, where structured extraction and clustering of conversation histories reveal user intents, frustration, tool gaps, and impact-weighted product opportunities.

## Extracted Concepts

- [Use fast query-document evals for retrieval changes](../concepts/use-fast-query-document-evals-for-retrieval-changes.md) - This source defines fast retrieval evals as cheap query-document pair checks for comparing retrieval configurations.
- [Align synthetic retrieval queries with real user specificity](../concepts/align-synthetic-retrieval-queries-with-real-user-specificity.md) - This source warns that naive generated queries can be too clean or overly specific unless calibrated against real user queries.
- [Cluster conversation outputs to prioritize AI product work](../concepts/cluster-conversation-outputs-to-prioritize-ai-product-work.md) - This source shows how conversation summaries, errors, tools, frustration, and satisfaction can be clustered to guide product and agent-tool investments.

## Topic Links

- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)
- [Workflows](../topics/workflows.md)

## Notes

- Fast retrieval evals use query/document pairs: for each query, the expected document should be returned in the chosen top-k set; this makes retrieval experiments cheap enough to run repeatedly instead of waiting on expensive judge pipelines (02:15-03:06).
- Synthetic query generation is useful before real traffic exists, but the generated query set should match the specificity and messiness of real user queries; otherwise teams can trick themselves with benchmark examples that are cleaner than production data (03:08-04:29).
- In the Weights & Biases chatbot example, local recall-at-10 testing ranked embedding models differently than public MTEB expectations: OpenAI `text-embedding-3-small` performed worst in that application and Voyage 3 Large performed best for that data (05:23-06:44).
- Conversation histories already contain product feedback such as retries, user frustration, tool calls, errors, and "try again" corrections, so teams can extract structured metadata from conversations rather than relying only on thumbs-up/down widgets (07:28-10:38).
- The output-analysis pipeline summarizes conversations, extracts metadata such as topics/tools/errors/frustration, clusters the summaries, aggregates into higher-level themes, and compares KPIs across those clusters (10:17-12:19).
- Segmenting by use case and performance lets teams decide what to build, fix, educate users about, or explicitly refuse; high-usage low-performance clusters are the most urgent product investments (14:12-15:18).
