# Scaling Enterprise-Grade RAG: Lessons from Legal Frontier - Calvin Qi (Harvey), Chang She (Lance)

Source: [Scaling Enterprise-Grade RAG: Lessons from Legal Frontier - Calvin Qi (Harvey), Chang She (Lance)](https://www.youtube.com/watch?v=W1MiZChnkfA)
Uploaded: 2025-07-29
Transcript: `raw/20250729_W1MiZChnkfA/W1MiZChnkfA.en-orig.vtt`

## Summary

Harvey and LanceDB frame enterprise legal RAG as a domain-specific, large-scale retrieval problem that needs corpus-aware indexing, expert-grounded evaluation, hybrid sparse/dense retrieval, reranking, privacy-aware infrastructure, and AI-data storage that serves both low-latency online queries and offline ingestion, analytics, preprocessing, and training.

## Extracted Concepts

- [Decompose Domain RAG by Query Structure and Corpus Scale](../concepts/decompose-domain-rag-by-query-structure-and-corpus-scale.md) - this source shows how legal RAG differs across uploads, project vaults, and global corpora, and how queries combine semantic, lexical, temporal, and domain-specific constraints.
- [Layer Domain RAG Evals by Fidelity, Cost, and Speed](../concepts/layer-domain-rag-evals-by-fidelity-cost-and-speed.md) - this source distinguishes expert review, expert-labeled criteria, and fast automated retrieval metrics.
- [AI Data Lakehouses Need Online Retrieval and Offline Iteration Paths](../concepts/ai-data-lakehouses-need-online-retrieval-and-offline-iteration-paths.md) - this source describes a LanceDB/Lance architecture for shared multimodal AI data, online serving, and offline experimentation.

## Topic Links

- [Retrieval](../topics/retrieval.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

## Notes

- Harvey separates legal data into on-demand uploads, project vaults, and large legal corpora such as legislation, case law, tax, and regulation data; each corpus level creates different retrieval scale and organization requirements. (01:23-02:22)
- Legal retrieval challenges include long dense documents, sparse versus dense representation choices, expert query complexity, domain-specific jargon, and privacy or security constraints. (02:22-03:23)
- A representative legal query can include jurisdiction, applicability before a date, a specialized dataset such as EU laws and directives, explicit regulation IDs, multiple provisions, and abbreviations that require legal context. (03:42-04:37)
- The talk recommends eval-driven development with a range of evals: expensive expert reviews, expert-labeled criteria for more automated checks, and fast quantitative retrieval metrics such as precision, recall, right folder, right section, and keyword checks. (04:39-06:08)
- Harvey and LanceDB both emphasize that domain experts should guide data structure, use cases, explicit and implicit query patterns, and evaluation procedures so teams can iterate as tools and context windows change. (06:11-06:44, 15:02-16:05)
- LanceDB positions its architecture as supporting search, analytics, training, preprocessing, vector search, full-text search, reranking, and multimodal storage over object-store-backed data with separated compute, memory, and storage. (09:58-14:55)
