# Parse Multimodal Business Sources Into Structured Markdown

Summary: Business RAG systems often need a parsing stage that turns PDFs, websites, images, audio, and video into structured text before chunking and retrieval. Markdown is a useful intermediate format because headings, lists, and formatting preserve some semantic structure without requiring the downstream LLM to consume raw binary or visual material.

Use when:
- Building a knowledge base over mixed source material such as decks, websites, screenshots, call recordings, and videos.
- Choosing whether to build parsing in-house or integrate resource-specific parsing vendors.
- Defining parser output requirements before chunking and embedding.

Details:
- 11x bucketed seller source material into documents/images, websites, and media such as audio and video, then built parsing jobs by resource type and selected vendor. (06:14-06:36, 06:51-07:05)
- Parsing is framed as making non-text information legible to LLMs: PDFs, MP4s, and images still need conversion even when multimodal models exist, because practical restrictions keep parsing relevant. (07:52-08:35)
- The pipeline uses Markdown as parser output because it is text with useful structural information and formatting. (08:35-08:51)
- The team chose vendors instead of building parsing from scratch because supporting many file/resource types would require specialized work, slow time to market, and uncertain quality. (08:53-09:37)
- Vendor selection requirements included support for required resource types, Markdown output, and webhooks for asynchronous parsing completion. (09:48-10:06)

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Structure-aware document parsing improves RAG chunk quality](structure-aware-document-parsing-improves-rag-chunk-quality.md)
- [Treat PDF pages as visual retrieval units](treat-pdf-pages-as-visual-retrieval-units.md)
- [Use omnimodal embeddings for cross-modal retrieval and comparison](use-omnimodal-embeddings-for-cross-modal-retrieval-and-comparison.md)

Sources:
- [Building Alice's Brain: an AI Sales Rep that Learns Like a Human - Sherwood & Satwik, 11x](../sources/20250729_KWmkMV0FNwQ.md), 06:14-10:06
