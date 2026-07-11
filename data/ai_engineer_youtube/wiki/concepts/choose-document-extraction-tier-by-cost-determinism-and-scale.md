# Choose a Document-Extraction Tier by Cost, Determinism, and Scale

Summary: Converting unstructured documents (PDFs, scans, tables, images) into LLM-ready text is a tiered decision, not a single tool choice: a naive parser, a frontier vision-language model, and a local structure-aware library trade quality against cost, determinism, and how well they scale to thousands of documents.

Use when:
- Choosing how to ingest a large PDF/scan/mixed-format corpus for RAG or fine-tuning.
- Deciding whether to send documents to a frontier VLM API or run local extraction.
- Justifying document-extraction cost at scale to a team that assumes "just send it to the model."

Details:
- Extraction quality is the determining factor for downstream answer correctness; a compounding failure example is ~20 scientific papers that now cite a nonsensical nonexistent term because an old scanned article was OCR'd and two words from two PDF columns got merged, then propagated by researchers writing with LLMs. (03:07)
- Tier 1 — naive PDF parser: fast and cheap, runs on CPU, but linearizes and truncates tables, leaks page headers, and drops image content, producing text a human and a model cannot decipher; unfit for question-answering or validation over tables. (05:26)
- Tier 2 — frontier VLM: good quality but expensive (~$30 per million output tokens), which balloons across dozens/hundreds/thousands of documents; it is non-deterministic (hallucination risk at scale) and brittle to model deprecations, where a version change (e.g. 5.1→5.2) breaks previously consistent structured output. (05:26)
- Tier 3 — local structure-aware library (Docling): the "middle ground" — fast, cheap, deterministic, open-source, air-gappable, GPU-optional — that emits Markdown/JSON/Pydantic while preserving layout, tables, and images. (05:44)
- Scale datapoint: Hugging Face's Leandro built the FinePDFs training corpus with OCR + Docling on CPU at ~50× cost savings versus using VLMs/OCR naively — evidence that local structure-aware extraction is the scalable tier, not just the cheap one. (08:15)

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Structure-aware document parsing improves RAG chunk quality](structure-aware-document-parsing-improves-rag-chunk-quality.md)
- [Use a document outline as the retrieval index for chunkless agentic RAG](use-a-document-outline-as-the-retrieval-index-for-chunkless-agentic-rag.md)
- [Right-size models with prototype big, deploy small](right-size-models-with-prototype-big-deploy-small.md)
- [Treat PDF pages as visual retrieval units](treat-pdf-pages-as-visual-retrieval-units.md)

Sources:
- [Structuring the Unstructured - Cedric Clyburn, Red Hat](../sources/20260628_-x5GEVnkuRw.md), 03:07-08:30
