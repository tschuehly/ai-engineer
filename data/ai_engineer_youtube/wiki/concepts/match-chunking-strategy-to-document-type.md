# Match Chunking Strategy to Document Type

Summary: Chunking is one of the highest-leverage parts of a RAG system, and no single chunker fits every document. Pick a chunking strategy per document shape — heading, paragraph, fixed-size-with-overlap, or sentence — and handle ad-hoc images by converting them to text first, because naive whole-file chunking leaves meaningless fragments that reduce accuracy and increase hallucination.

Use when:
- Ingesting mixed documents (FAQs, policy handbooks, unstructured notes, screenshots, emails) into a retrieval store.
- Deciding how to split a parsed document before embedding it.
- Debugging retrieval that returns irrelevant fragments (signatures, dates, acknowledgements) or untrackable references.

Details:
- Heading-based chunking: the parser (Docling) finds each heading and makes each heading-plus-content a chunk. Best for FAQ/Q&A material — chunks stay clean, and each answer references a single traceable heading-and-answer unit. (Matini 13:52-17:57)
- Paragraph-based chunking: each paragraph becomes its own chunk regardless of headings — useful when content is prose without a clear heading hierarchy. (Matini 17:57-19:36)
- Fixed-size chunking: split every 512 characters with a 64-character overlap (32 before + 32 after each boundary) so context is not lost across cuts; a best-practice fallback for unorganized or random data you cannot clean, at the cost of sometimes breaking mid-thought. (Matini 19:36-21:40)
- Sentence-based chunking: chunk by a count of sentences — a good fit for short, unstructured messages. (Matini 21:40-21:47)
- Ad-hoc images/screenshots (e.g. an emailed maintenance-window notice) are handled by an image→text model → `.md` → sentence-group chunking, then indexed; no manual data cleanup is needed for a quick drag-and-drop, and the answer cites the uploaded screenshot. (Matini 21:47-25:32)
- Turning FAQ source data into explicit question/answer pairs is the easiest form for the system to digest and gives the cleanest references. (Matini 11:44-14:04)
- The failure mode chunking prevents: dumping a whole 28-page handbook produces meaningless chunks (acknowledgement, signature, date) that slow answers, reduce accuracy, and increase hallucination — so split into relevant files and clean the data before uploading. (Matini 12:32-13:20, 25:28-26:05)

Related topics:
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Structure-aware document parsing improves RAG chunk quality](structure-aware-document-parsing-improves-rag-chunk-quality.md)
- [Structure Documents Offline to Avoid the Multimodal Token Tax](structure-documents-offline-to-avoid-the-multimodal-token-tax.md)
- [Hybrid Retrieval Combines Lexical, Sparse, Dense, and Reranking Signals](hybrid-retrieval-combines-lexical-sparse-dense-and-reranking-signals.md)

Sources:
- [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry - Abed Matini, Ogilvy](../sources/20260628_Akm1sqvWG4A.md), 10:46-26:05
