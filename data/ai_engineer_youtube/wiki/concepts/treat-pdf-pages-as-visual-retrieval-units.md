# Treat PDF pages as visual retrieval units

Summary: Visual-document RAG can treat each PDF page as an image instead of first decomposing the document into OCR text, tables, and extracted images. Use this when page layout, screenshots, scans, forms, or embedded visual text carry the answer.

Use when:
- A PDF corpus contains scanned pages, forms, licenses, policy documents, screenshots, or visually embedded text.
- OCR and table extraction work only partly because layout and visual context matter to retrieval.

Details:
- A traditional multimodal RAG path extracts images, tables, and text separately, embeds those units, retrieves one of them, and sends the result to a multimodal LLM.
- ColPali-style visual retrieval changes the unit of retrieval: a 100-page PDF becomes 100 page images rather than one document decomposed into text/table/image chunks, 20:33-20:51.
- This approach is especially relevant when PDFs were created from images or contain mixed visual and textual evidence that should stay together as a page, 14:32-15:16.
- Debnath describes an insurance use case with driver-license and insurance-policy images where OCR worked, but ColPali-style visual retrieval also performed well on the image-heavy documents, 01:12:23-01:12:47.

Related topics:
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Structure-aware document parsing improves RAG chunk quality](structure-aware-document-parsing-improves-rag-chunk-quality.md)
- [Use omnimodal embeddings for cross-modal retrieval and comparison](use-omnimodal-embeddings-for-cross-modal-retrieval-and-comparison.md)

Sources:
- [VoiceVision RAG - Integrating Visual Document Intelligence with Voice Response - Suman Debnath, AWS](../sources/20251206_hwCmfThIiS4.md), 07:35-10:03, 14:32-15:16, 20:33-20:51, 01:12:23-01:12:47
