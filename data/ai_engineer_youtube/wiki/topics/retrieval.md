# Retrieval

## Overview

Retrieval gives agents access to institutional systems such as Confluence, Jira, SharePoint, GitHub, Slack, knowledge graphs, and file-backed knowledge bases. The useful retrieval layer is not the one with the most connectors, but the one that provides accurate, task-relevant context and exposes gaps when the source knowledge is missing, stale, contradictory, or unavailable to the current user. Personal Markdown knowledge bases can play the same role at individual scale when saved links, notes, tasks, and project records are indexed, tagged, connected, and resurfaced when relevant. Read-only personal retrieval can also synthesize emails, journals, tasks, browser history, notes, and relationship records into reflection without granting mutation rights. Context engines add a reasoning layer over retrieval by personalizing results to the task, team, permissions, and source relationships. Small models can improve this layer by embedding, reranking, extracting entities, filtering inputs, or building structured knowledge targets. Omnimodal embeddings extend the retrieval target beyond text: one semantic vector can represent text, audio, video, and documents so agents can retrieve, query, and compare concepts without lossy modality handoffs. Dimension-adaptive embeddings add an infrastructure lever by letting retrieval start with cheaper coarse vectors and expand when higher expressiveness is needed.

Retrieval is also an LLM security boundary. Poisoned chunks can steer an answer when they are retrieved for the target query and ranked high enough to look useful, so retrieval systems need provenance, corpus hygiene, and safety checks before retrieved text becomes model context. Embeddings themselves should also be protected as sensitive derived data: storing vectors without source text does not make the corpus safe to expose if a reconstruction model can recover source-like content.

RAG systems benefit from reusable baselines, but not from a single fixed recipe. Document parsing, chunking, embedding choice, hybrid lexical/vector search, metadata filters, and query-time agent loops all need to be tuned against the actual corpus and user questions. Generic embeddings can be too global for a specialized corpus, so contextual or domain-adaptive embedding approaches may improve retrieval before a team reaches for model weight updates. Structure-aware ingestion is especially important for messy source formats: preserving document hierarchy, tables, images, OCR output, and modality-specific extraction gives retrieval cleaner chunks than plain text extraction. For image-heavy or scanned PDFs, the retrieval unit itself may need to shift from extracted text chunks to page images: ColPali-style systems embed visual page patches so the retrieved evidence preserves layout, embedded text, forms, and images together. Hybrid indexes add another control point by combining vector similarity, keyword search, filters, aggregations, and embedding-model migration paths. Graph retrieval adds a distinct lever when questions depend on entity relationships: teams can combine vector retrieval with knowledge-graph traversal, but only when the ontology and extracted triplets are reliable enough to justify the extra compute and latency. Graph-backed context can also become an agent memory surface rather than only a search backend: nodes, relationships, properties, embeddings, and access overlays make long-term memory traversable and inspectable, while agentic GraphRAG can let a model inspect schema, issue graph queries, and pull related chunks iteratively when a fixed retrieval path is too shallow.

Document extraction for enterprise retrieval often needs a domain-operated template layer before chunks become trusted structured data. BlackRock's knowledge-app sandbox treats field source, type, required status, validations, dependencies, labels, embeddings, and business tags as configurable retrieval and extraction metadata, so operators can compare runs and refine evidence before downstream systems consume the output.

Private research agents can treat connectors and uploads as complementary retrieval inputs. A connector such as Notion or Microsoft 365 provides durable organizational context, while uploaded receipts, PDFs, screenshots, or task files provide local evidence for the current run. The workflow becomes more useful when the agent can compare both layers and write results back to the right internal page or record. Enterprise deep research applies the same private-context idea to larger document-heavy corpora: the agent runs multi-step or parallel investigation over internal sources, reflects on retrieved evidence, and synthesizes a cited report. That raises the retrieval bar because multimodal ingestion, hybrid search, metadata, reranking, access control, hallucination checks, deployment boundaries, and observability all affect whether the research output can be trusted.

## Key Concepts

- [Context blocks turn monolithic enterprise knowledge into reusable agent context](../concepts/context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md) - decomposed context units give retrieval systems cleaner targets than broad documentation monoliths.
- [Evaluate retrieval and MCP layers by task value, not only response availability](../concepts/evaluate-retrieval-and-mcp-layers-by-task-value.md) - retrieval must be tested against whether it helps complete work.
- [Use small models as context-management tools before agent reasoning](../concepts/use-small-models-as-context-management-tools-before-agent-reasoning.md) - embeddings, rerankers, NER, and extraction models can structure or filter retrieval inputs before agent reasoning.
- [Context engines select task-specific organizational context](../concepts/context-engines-select-task-specific-organizational-context.md) - retrieval needs task and user relevance, not just available chunks.
- [Surface unresolved context conflicts to agents and users](../concepts/surface-unresolved-context-conflicts-to-agents-and-users.md) - contradictory retrieved sources should be resolved or exposed.
- [Do not cache context-engine answers as durable truth](../concepts/do-not-cache-context-engine-answers-as-durable-truth.md) - answer reuse can preserve stale code, docs, or model mistakes.
- [Use social and expert graphs to personalize coding-agent context](../concepts/use-social-and-expert-graphs-to-personalize-coding-agent-context.md) - contribution and review signals can bias retrieval toward relevant repositories and experts.
- [Personal knowledge bases become agent context substrates](../concepts/personal-knowledge-bases-become-agent-context-substrates.md) - personal retrieval becomes more useful when ingestion adds context and links to existing notes.
- [Cognitive exhaust gains value through cross-source synthesis](../concepts/cognitive-exhaust-gains-value-through-cross-source-synthesis.md) - personal retrieval can reveal patterns no single source can see.
- [Retire completed planning docs before they become agent doc rot](../concepts/retire-completed-planning-docs-before-they-become-agent-doc-rot.md) - retrieval systems should avoid presenting stale plans as current implementation truth.
- [Surface existing company information before redesigning processes](../concepts/surface-existing-company-information-before-redesigning-processes.md) - agents can retrieve and synthesize information that already exists outside the system of record.
- [Use omnimodal embeddings for cross-modal retrieval and comparison](../concepts/use-omnimodal-embeddings-for-cross-modal-retrieval-and-comparison.md) - cross-modal retrieval needs semantic representations that preserve concepts across text, audio, video, and documents.
- [Adapt embedding dimensions with Matryoshka representation learning](../concepts/adapt-embedding-dimensions-with-matryoshka-representation-learning.md) - retrieval systems can trade index cost and expressiveness without changing embedding models.
- [LLM attack surfaces span prompts, context, retrieval, tools, and actions](../concepts/llm-attack-surfaces-span-prompts-context-retrieval-tools-and-actions.md) - RAG poisoning makes retrieved chunks part of the threat model.
- [Filter untrusted context before it reaches the agent](../concepts/filter-untrusted-context-before-it-reaches-the-agent.md) - retrieved context should be screened before it becomes agent instructions.
- [Aggregated personal context creates mosaic and exfiltration risk](../concepts/aggregated-personal-context-creates-mosaic-and-exfiltration-risk.md) - aggregating many small personal signals changes the privacy risk of retrieval.
- [RAG stacks need modular baselines instead of one fixed recipe](../concepts/rag-stacks-need-modular-baselines-instead-of-one-fixed-recipe.md) - shared RAG components should remain tunable for the source corpus and user workflow.
- [Structure-aware document parsing improves RAG chunk quality](../concepts/structure-aware-document-parsing-improves-rag-chunk-quality.md) - preserving hierarchy, tables, OCR, and images gives retrieval better chunk boundaries.
- [Agentic document extraction decomposes complex fields](../concepts/agentic-document-extraction-decomposes-complex-fields.md) - extraction pipelines should group related fields and validate OCR/image evidence before creating structured metadata.
- [Domain-expert sandboxes accelerate knowledge-app iteration](../concepts/domain-expert-sandboxes-accelerate-knowledge-app-iteration.md) - specialized retrieval and extraction metadata should be adjustable by the operators who understand the corpus.
- [Treat PDF pages as visual retrieval units](../concepts/treat-pdf-pages-as-visual-retrieval-units.md) - scanned and visual PDFs may retrieve better when each page remains an image instead of being decomposed into text, tables, and images.
- [Patch-level visual embeddings trade ingest cost for query-time retrieval](../concepts/patch-level-visual-embeddings-trade-ingest-cost-for-query-time-retrieval.md) - page-image retrieval stores many patch vectors and shifts the main cost toward ingestion and indexing.
- [Hybrid retrieval should support filters and embedding migration](../concepts/hybrid-retrieval-should-support-filters-and-embedding-migration.md) - vector search should be paired with lexical search, metadata scope, and migration paths.
- [Choose HybridRAG when relationship structure matters](../concepts/choose-hybridrag-when-relationship-structure-matters.md) - graph retrieval is most useful when questions need explicit entity relationships, not only semantic chunk similarity.
- [Knowledge graphs make agent memory traversable and explainable](../concepts/knowledge-graphs-make-agent-memory-traversable-and-explainable.md) - graph context can store relationships, embeddings, and access overlays as inspectable retrieval structure.
- [Agentic GraphRAG uses schema-aware multi-step graph queries](../concepts/agentic-graphrag-uses-schema-aware-multi-step-graph-queries.md) - agentic graph retrieval trades speed for deeper schema-guided traversal and supporting chunks.
- [Treat ontology and triplet quality as GraphRAG bottlenecks](../concepts/treat-ontology-and-triplet-quality-as-graphrag-bottlenecks.md) - noisy graph construction creates noisy graph retrieval.
- [Balance GraphRAG hop depth against production latency](../concepts/balance-graphrag-hop-depth-against-production-latency.md) - deeper traversal can improve context, but it must fit the application's latency budget.
- [Agentic retrieval lets models plan search steps](../concepts/agentic-retrieval-lets-models-plan-search-steps.md) - retrieval tools can let the model decompose and repeat searches instead of relying on one top-k query.
- [Use connectors and uploads as private research context](../concepts/use-connectors-and-uploads-as-private-research-context.md) - internal agents can combine organizational systems and task files as source context.
- [Enterprise deep research runs multi-step synthesis over private corpora](../concepts/enterprise-deep-research-runs-multi-step-synthesis-over-private-corpora.md) - private-corpus research uses multi-step retrieval, reflection, synthesis, and citations instead of a single RAG answer.
- [Enterprise deep research needs trustworthy retrieval and governance controls](../concepts/enterprise-deep-research-needs-trustworthy-retrieval-and-governance-controls.md) - internal research outputs need retrieval quality, hallucination mitigation, access control, deployment flexibility, and observability.
- [Treat embeddings as recoverable sensitive data](../concepts/treat-embeddings-as-recoverable-sensitive-data.md) - vector stores should be secured like source-derived data, not treated as anonymized storage.
- [Train long-tail knowledge into weights with curated synthetic data](../concepts/train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md) - weight updates become an alternative when RAG cannot combine or adapt niche knowledge well enough.

## Open Questions

- How should retrieval systems route between source-of-truth systems and curated context blocks when they disagree?
- Which retrieval steps benefit from hot-swappable small models rather than a single general embedding or reranking service?
- How should Graph RAG or graph summarization systems preserve permission boundaries when summaries cross source scopes?
- Which graph-traversal depths, graph-acceleration libraries, and RAG evaluation metrics produce the best relevance-latency balance for each corpus?
- How should personal retrieval distinguish durable notes from stale bookmarks and noisy saved material?
- What status metadata should retrieval systems use to demote closed PRDs and historical planning artifacts?
- When should cross-modal retrieval use one omnimodal embedding space instead of separate modality-specific indexes plus fusion?
- When should visual-document RAG preserve page images instead of extracting OCR text and structured table/image chunks?
- Which RAG pipeline changes should be exposed as user-facing filters, operator settings, or internal LangFlow-style flow edits?
- Which private corpora are too sensitive to expose through third-party or loosely protected embedding stores?

## Sources

- [How BlackRock Builds Custom Knowledge Apps at Scale — Vaibhav Page & Infant Vasanth, BlackRock](../sources/20250823_08mH36_NVos.md)
- [Building an Agentic Platform - Ben Kus, CTO Box](../sources/20250824_12v5S1n1eOY.md)

- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md)
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md)
- [I Gave an AI Agent the Keys to My Life (Here's What Happened) - Radek Sienkiewicz (@velvetshark-com)](../sources/20260502_sJ2jc7leKBk.md)
- [Full Walkthrough: Workflow for AI Coding - Matt Pocock](../sources/20260424_-QFHIoCo-Ko.md)
- [The New Application Layer - Malte Ubl, CTO Vercel](../sources/20260420_XKup1pj-34M.md)
- [How Google DeepMind is researching the next Frontier of AI for Gemini - Raia Hadsell, VP of Research](../sources/20260418_zZsTVBXcbow.md)
- [$1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs - Diego Carpentero](../sources/20260416_YZHPEkfy2kc.md)
- [OpenRAG: An open-source stack for RAG - Phil Nash](../sources/20260408_4TxOBhDRRCM.md)
- [HybridRAG: A Fusion of Graph and Vector Retrieval  - Mitesh Patel, NVIDIA](../sources/20250722_-tgQa8Fzf80.md)
- [Cognitive Exhaust Fumes, or: Read-Only AI Is Underrated - Simon Podhajsky, Head of AI, Waypoint](../sources/20260408_u0TOSBbAw7c.md)
- [Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)](../sources/20251230_xz0-brt56L8.md)
- [Jack Morris: Stuffing Context is not Memory, Updating Weights is](../sources/20251229_Jty4s9-Jb78.md)
- [VoiceVision RAG - Integrating Visual Document Intelligence with Voice Response - Suman Debnath, AWS](../sources/20251206_hwCmfThIiS4.md)
- [Context Engineering: Connecting the Dots with Graphs - Stephen Chin, Neo4j](../sources/20251124_LLuKshphGOE.md)
- [Enterprise Deep Research: The Next Killer App for Enterprise AI — Ofer Mendelevitch, Vectara](../sources/20251124_fh9LgKXBGnQ.md)
