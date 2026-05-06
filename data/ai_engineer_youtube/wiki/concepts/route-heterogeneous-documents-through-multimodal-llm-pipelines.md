# Route Heterogeneous Documents Through Multimodal LLM Pipelines

Summary: Complex document workflows can use an early multimodal classification step to route files into specialized downstream modules instead of applying one generic summarizer or extractor to every file.

Use when:
- Processing mixed corpora such as SEC filings, contracts, patents, images, and city infrastructure documents.
- Building document workflows where visual layout or page images carry routing or segmentation signal.

Details:
- The DSPy walkthrough classifies a file from page images and branches into different processing paths for SEC filings, contracts, city infrastructure images, and catchall "other" documents. 51:17-53:10
- The file classifier uses document images as typed inputs and returns a document type, making visual structure part of the workflow instead of relying only on extracted text. 52:00-52:58
- A boundary-detection example classifies pages asynchronously, then feeds page-classification tuples into another signature to identify document boundaries. 58:20-58:58
- The boundary detector can call a page-image tool to inspect candidate boundary pages and use visual evidence before constructing the final answer. 59:19-60:07

Related topics:
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Structure-aware document parsing improves RAG chunk quality](structure-aware-document-parsing-improves-rag-chunk-quality.md)
- [Train image and video diffusion models in learned latent spaces](train-image-and-video-diffusion-models-in-learned-latent-spaces.md)

Sources:
- [DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners](../sources/20260108_-cKUW6n8hBU.md), 51:17-53:10, 58:20-60:07
