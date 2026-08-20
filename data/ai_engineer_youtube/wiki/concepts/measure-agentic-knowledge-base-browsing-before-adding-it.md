# Measure Agentic Knowledge-Base Browsing Before Adding It

Summary: Letting an agent browse a knowledge base with shell commands — the pattern coding agents made popular — is not automatically better than a tuned retrieval tool. Towards AI built one over a generated wiki, measured it against their existing hybrid search, and found identical recall at 50% higher latency, because the extra tool calls bought nothing their retriever had not already found.

Use when:
- Considering replacing or augmenting a RAG pipeline with agentic file browsing.
- Justifying whether a new tool earns its latency and token budget.
- Designing the sandbox for an agent that gets shell access to a document store.

Details:
- The build: three folders created offline — `raw` (all markdown lessons and public docs), `generated` (an automatic index of file titles), and `wiki` (topic and framework pages that Claude Code wrote by reading the raw folder, e.g. a fine-tuning page pointing at every related raw file). Regenerated whenever a course is added. This is Karpathy's LLM-wiki idea applied to a product knowledge base. ([Context Engineering in 2026](../sources/20260817_WP3hjUXd918.md), 24:00-24:26, 28:00-29:20, 30:33-30:57)
- The sandbox is the reusable part even if the tool is not: read-only bash commands only (nothing that can modify the filesystem), scoped to the knowledge-base folder, an 8-second per-command timeout that returns an error so the agent can try something else, tool output capped at 40,000 characters with the agent expected to issue a follow-up command for the remainder, and a ceiling of 20 commands per turn that they have never observed being hit. (29:20-30:33)
- The motivating case was real: questions spanning several documents ("how do I best use Codex *and* Claude Code together"), where a top-5 chunk set may not cover the answer, and a paper they cite argues browsing helps. (27:07-28:00)
- The measured result: with the tool turned off, recall was *the same*; with it on, the system was 50% slower because the agent made more tool calls. "It was fun to add, but we didn't see any benefit." (31:15-32:01)
- Usage was not the problem — with their system prompt the agent invoked the browse tool on about 90% of turns, so the null result is not an under-triggering artifact. They did not tune the trigger rate in either direction. (30:57-31:14)
- The presenter's explanation is that the evaluation used real student questions, which may not be hard enough to require multi-document browsing. (The captions here are garbled and read "were complex enough" where the argument requires "were *not* complex enough.") That is the condition to check before generalizing the null result: browsing may still win on genuinely cross-document questions, which is an argument for measuring on *your* question mix rather than on the demo case. (31:58-32:18)
- The comparison was against a retriever that had itself been tuned — hybrid Cohere embeddings plus BM25 to top 30 each, merged and reranked to top 5, with the configuration chosen by a separate recall sweep. A fair verdict is "agentic browsing did not beat a *tuned* retriever," which is a different claim from "browsing does not beat RAG." (25:30-27:05)
- The same source reports a second negative result on a fashionable technique from the same evaluation discipline: GraphRAG was "way costlier to set up and just tie[d] on the results" against plain RAG on their real-user evaluations, with the caveat that a large dataset of genuinely interconnected topics might change the answer. (11:55-12:58)

- Scope the null result to its consumer. A third build from the same Karpathy LLM-wiki idea — Ben Holmes' personal note pipeline — generates an entity layer (people, concepts, organizations, sources) whose readers are a *human* clicking backlinks and a "bird's eye" graph view, not an agent answering questions. Nothing here refutes that use, and nothing there rescues agentic browsing: the two cases share a structure but not a benefit, so "the generated wiki did not help our retriever" and "the generated wiki is worth generating" can both hold. What Holmes offers is a demonstration and no measurement of any kind, which is the gap this page exists to close. See [Generate an Entity Wiki Over Your Own Notes](generate-an-entity-wiki-over-your-own-notes.md). ([LLM Knowledge Bases](../sources/20260812_I3bpdgFJCUY.md), 09:20-13:24, 17:52-19:20)

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Tools](../topics/tools.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Generate an Entity Wiki Over Your Own Notes](generate-an-entity-wiki-over-your-own-notes.md)
- [Agentic Retrieval Lets Models Plan Search Steps](agentic-retrieval-lets-models-plan-search-steps.md)
- [Redefine RAG as Iterative Multi-Tool Retrieval, Not Vector Search](redefine-rag-as-iterative-multi-tool-retrieval.md)
- [Build a File-Based Research Wiki With Progressive-Disclosure Retrieval](file-based-research-wiki-with-progressive-disclosure-retrieval.md)
- [Choose HybridRAG When Relationship Structure Matters](choose-hybridrag-when-relationship-structure-matters.md)
- [Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md)
- [Hybrid Retrieval Combines Lexical, Sparse, Dense, and Reranking Signals](hybrid-retrieval-combines-lexical-sparse-dense-and-reranking-signals.md)

Sources:
- [Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](../sources/20260817_WP3hjUXd918.md), 11:55-12:58, 24:00-32:18
- [LLM Knowledge Bases: a practical guide — Ben Holmes, Warp](../sources/20260812_I3bpdgFJCUY.md), 09:20-13:24, 17:52-19:20
