# Retrieval

## Overview

Retrieval gives agents access to institutional systems such as Confluence, Jira, SharePoint, GitHub, Slack, knowledge graphs, and file-backed knowledge bases. The useful retrieval layer is not the one with the most connectors, but the one that provides accurate, task-relevant context and exposes gaps when the source knowledge is missing, stale, contradictory, or unavailable to the current user. Personal Markdown knowledge bases can play the same role at individual scale when saved links, notes, tasks, and project records are indexed, tagged, connected, and resurfaced when relevant. Read-only personal retrieval can also synthesize emails, journals, tasks, browser history, notes, and relationship records into reflection without granting mutation rights. Context engines add a reasoning layer over retrieval by personalizing results to the task, team, permissions, and source relationships. Small models can improve this layer by embedding, reranking, extracting entities, filtering inputs, or building structured knowledge targets. Omnimodal embeddings extend the retrieval target beyond text: one semantic vector can represent text, audio, video, and documents so agents can retrieve, query, and compare concepts without lossy modality handoffs. Dimension-adaptive embeddings add an infrastructure lever by letting retrieval start with cheaper coarse vectors and expand when higher expressiveness is needed.

Retrieval is also an LLM security boundary. Poisoned chunks can steer an answer when they are retrieved for the target query and ranked high enough to look useful, so retrieval systems need provenance, corpus hygiene, and safety checks before retrieved text becomes model context.

RAG systems benefit from reusable baselines, but not from a single fixed recipe. Document parsing, chunking, embedding choice, hybrid lexical/vector search, metadata filters, and query-time agent loops all need to be tuned against the actual corpus and user questions. Structure-aware ingestion is especially important for messy source formats: preserving document hierarchy, tables, images, OCR output, and modality-specific extraction gives retrieval cleaner chunks than plain text extraction. Hybrid indexes add another control point by combining vector similarity, keyword search, filters, aggregations, and embedding-model migration paths.

Private research agents can treat connectors and uploads as complementary retrieval inputs. A connector such as Notion or Microsoft 365 provides durable organizational context, while uploaded receipts, PDFs, screenshots, or task files provide local evidence for the current run. The workflow becomes more useful when the agent can compare both layers and write results back to the right internal page or record.

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
- [Hybrid retrieval should support filters and embedding migration](../concepts/hybrid-retrieval-should-support-filters-and-embedding-migration.md) - vector search should be paired with lexical search, metadata scope, and migration paths.
- [Agentic retrieval lets models plan search steps](../concepts/agentic-retrieval-lets-models-plan-search-steps.md) - retrieval tools can let the model decompose and repeat searches instead of relying on one top-k query.
- [Use connectors and uploads as private research context](../concepts/use-connectors-and-uploads-as-private-research-context.md) - internal agents can combine organizational systems and task files as source context.

## Open Questions

- How should retrieval systems route between source-of-truth systems and curated context blocks when they disagree?
- Which retrieval steps benefit from hot-swappable small models rather than a single general embedding or reranking service?
- How should Graph RAG or graph summarization systems preserve permission boundaries when summaries cross source scopes?
- How should personal retrieval distinguish durable notes from stale bookmarks and noisy saved material?
- What status metadata should retrieval systems use to demote closed PRDs and historical planning artifacts?
- When should cross-modal retrieval use one omnimodal embedding space instead of separate modality-specific indexes plus fusion?
- Which RAG pipeline changes should be exposed as user-facing filters, operator settings, or internal LangFlow-style flow edits?

## Sources

- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md)
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md)
- [I Gave an AI Agent the Keys to My Life (Here's What Happened) - Radek Sienkiewicz (@velvetshark-com)](../sources/20260502_sJ2jc7leKBk.md)
- [Full Walkthrough: Workflow for AI Coding - Matt Pocock](../sources/20260424_-QFHIoCo-Ko.md)
- [The New Application Layer - Malte Ubl, CTO Vercel](../sources/20260420_XKup1pj-34M.md)
- [How Google DeepMind is researching the next Frontier of AI for Gemini - Raia Hadsell, VP of Research](../sources/20260418_zZsTVBXcbow.md)
- [$1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs - Diego Carpentero](../sources/20260416_YZHPEkfy2kc.md)
- [OpenRAG: An open-source stack for RAG - Phil Nash](../sources/20260408_4TxOBhDRRCM.md)
- [Cognitive Exhaust Fumes, or: Read-Only AI Is Underrated - Simon Podhajsky, Head of AI, Waypoint](../sources/20260408_u0TOSBbAw7c.md)
- [Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)](../sources/20251230_xz0-brt56L8.md)
