# Building Alice's Brain: an AI Sales Rep that Learns Like a Human - Sherwood & Satwik, 11x

Source: [Building Alice's Brain: an AI Sales Rep that Learns Like a Human - Sherwood & Satwik, 11x](https://www.youtube.com/watch?v=KWmkMV0FNwQ)
Uploaded: 2025-07-29
Transcript: `raw/20250729_KWmkMV0FNwQ/KWmkMV0FNwQ.en-orig.vtt`

## Summary

11x describes how Alice, an AI sales-development representative, moved seller onboarding from manually entered product and offer fields into a RAG-backed seller knowledge base that ingests documents, websites, images, audio, and video; parses them into Markdown; chunks and embeds them; retrieves relevant chunks during email generation; and exposes retrieved evidence in the UI for operators and sales teams.

## Extracted Concepts

- [Seller Knowledge Bases Let Agents Pull Business Context at Action Time](../concepts/seller-knowledge-bases-let-agents-pull-business-context-at-action-time.md) - supports a product-specific RAG pattern where users upload source material once and the agent retrieves seller context when generating outbound messages.
- [Parse Multimodal Business Sources Into Structured Markdown](../concepts/parse-multimodal-business-sources-into-structured-markdown.md) - explains why PDFs, websites, images, audio, and video often need a parsing layer before retrieval.
- [Show Retrieved Chunks Inside Agent Workflows](../concepts/show-retrieved-chunks-inside-agent-workflows.md) - shows a visualization pattern for proving which knowledge-base chunks informed agent output.
- [Benchmark RAG Pipelines After Production Usage Exists](../concepts/benchmark-rag-pipelines-after-production-usage-exists.md) - captures a staged evaluation lesson: ship a product-requirement-satisfying baseline, then use real usage to benchmark parsing, hallucination, cost, and hybrid retrieval improvements.

## Topic Links

- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)
- [Workflows](../topics/workflows.md)

## Notes

- Alice's sales role depends on two context sets: seller context such as products, services, case studies, pain points, value props, and ICP, and lead context such as role, responsibilities, prior solutions, pain points, and company; the talk focuses on seller knowledge. (02:24-03:06)
- Manual seller libraries created onboarding friction because users had to enter detailed offer and value-prop descriptions before running campaigns, and too few or too many manually selected offers led to irrelevant or overloaded context. (03:09-04:47)
- The knowledge-base design flips seller context from push to pull: users upload seller materials, and Alice retrieves the most relevant context when generating emails. (04:49-05:09)
- The ingestion architecture stores uploaded resources in S3, creates database resources, dispatches parsing jobs by resource type and vendor, consumes parsing webhooks, stores parsed artifacts, embeds chunks into Pinecone, updates the UI, and lets the agent query the vector database. (06:36-07:31)
- The RAG pipeline is described as parsing, chunking, storage, retrieval, and visualization. (07:36-07:49)
- Parsing converts non-text resources such as PDFs, MP4s, and images into text for LLM use; the chosen output is Markdown because structure and formatting carry useful semantics. (07:52-08:51)
- 11x selected parsing vendors partly by resource-type support, Markdown output, and webhook support, but later identified accuracy, comprehensiveness, and cost as evaluation gaps. (09:48-10:56)
- The implementation used LlamaParse for documents/images, Firecrawl for websites, Cloudglue for audio/video, and Pinecone for vector storage with bundled embeddings. (10:56-16:45)
- Retrieval can enrich an LLM API call directly or appear as one or more tool-call steps inside a larger agent flow; in the latter shape the agent can decide whether more retrieval is needed. (16:54-17:51)
- The knowledge-base UI includes questions and dropdowns showing the chunks retrieved for the messaging flow, giving teams a way to inspect what Alice knows and why a message used specific evidence. (19:42-20:21)
- The stated lessons were that RAG is complex, teams should get a product-requirement-satisfying baseline into production before benchmarking, and vendors should be used as technical partners; future work included hallucination tracking, parser accuracy/completeness evaluation, hybrid RAG with a graph database, and cost reduction. (20:38-22:00)
