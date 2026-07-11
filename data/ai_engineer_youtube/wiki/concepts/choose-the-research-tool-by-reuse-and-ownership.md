# Choose the Research Tool by Reuse and Ownership, Not Just Speed

Summary: Pick a research/knowledge tool by how durable the output must be and how much you must own it — not only by how fast it answers. The ladder runs from ad-hoc chat (Google/ChatGPT) for throwaway answers, to a coding agent (Codex/Claude Code) for one-off changes, to NotebookLM/RAG for revisiting content or production scale, to a self-owned file-based research memory when you want a personalized, inspectable store that compounds over time.

Use when:
- Deciding whether a question deserves a quick chat, a coding-agent session, a RAG pipeline, or a purpose-built personal knowledge base.
- Justifying (or avoiding) the setup cost of building your own research/memory system versus using an off-the-shelf tool.
- Weighing ownership, personalization, and agent-nativeness against convenience.

Details:
- Fast one-off answer → just Google it or ask ChatGPT/Claude. The catch: for a long-context or repeatable project you become "fully dependent on the architecture that OpenAI/ChatGPT's team built," and each session loses its context. (03:42-04:20)
- One-off change or a single article you won't repeat → use Codex/Claude Code or an agent you trust. But when you keep digging to improve/optimize, "you want your research sources to stick and to be able to refer to them in the future," and to avoid re-pasting links/PDFs and rebuilding on-the-fly scripts every new session. (04:20-05:30, 07:57-08:39)
- NotebookLM is powerful for digesting and revisiting content, but you don't own it, can't fully personalize it, it's "not agent-native," and it's weak for coding because it's browser-based. (05:32-06:05)
- A retrieval/RAG pipeline with a vector DB is the production answer and is "super powerful at scale," but it needs infrastructure, is not human-friendly to inspect/edit by hand, and is overkill for a personal system you want to use lightly. (06:24-07:07)
- Build your own when you want "everything there but more personalization" — a personalized research assistant that builds a Wikipedia-like store that compounds over time, is easily inspectable, and holds sources/comparisons/implementations you keep adding. The downside is more setup than opening Claude Code. (07:08-07:57)
- Underlying principle: the bottleneck is not how much context you feed the model but how you *reuse* it later. With an agent "the context window becomes everything… and when you stop the conversation, it loses everything," so the real need is memory + context management (and, for the authors' video work, some persistent personality). (08:39-09:16)

Related topics:
- [Workflows](../topics/workflows.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Build a File-Based Research Wiki With Progressive-Disclosure Retrieval](file-based-research-wiki-with-progressive-disclosure-retrieval.md)
- [Do Not Treat Long Context as Durable Model Memory](do-not-treat-long-context-as-durable-model-memory.md)
- [Enterprise Deep Research Runs Multi-Step Synthesis Over Private Corpora](enterprise-deep-research-runs-multi-step-synthesis-over-private-corpora.md)
- [Treat Embeddings as Cached Compute Decided by Query Volume](treat-embeddings-as-cached-compute-decided-by-query-volume.md)

Sources:
- [Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI](../sources/20260626_ZRM_TfEZcIo.md), 03:42-09:16
