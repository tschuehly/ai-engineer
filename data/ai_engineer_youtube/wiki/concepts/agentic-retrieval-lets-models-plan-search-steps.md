# Agentic Retrieval Lets Models Plan Search Steps

Summary: Agentic retrieval gives a model retrieval tools and lets it decide which searches to run and how to use the results. This is useful when one embedded query and a fixed top-k result set are too brittle for exploratory or multi-hop questions.

Use when:
- Building a RAG agent that may need query decomposition, repeated search, or tool choice before answering.
- Comparing deterministic retrieval pipelines with agent-controlled retrieval loops.

Details:
- The talk contrasts traditional RAG generation, where the user query is embedded once and top-k chunks are passed to an LLM, with agentic retrieval, where the model receives the query, instructions, and search tools.
- In OpenRAG, LangFlow hosts the agentic retrieval flow and can use model providers such as OpenAI, Anthropic, Ollama, and watsonx.ai.
- The demo shows the agent performing tool calls when needed, using prompt-level knowledge filters, and exposing retrieval as a reusable flow.
- Agentic retrieval increases flexibility but makes retrieval behavior part of the agent workflow, so tool traces and evaluation should inspect search decisions as well as final answers.
- Turbopuffer corroborates the pattern with a concrete definition: agentic search is "giving the agent a set of tools to progressively and iteratively find and reason over context" — grep, read, assess, repeat until the agent reaches a happy state. Sophisticated customers no longer do simple one-shot RAG; they make many calls, reason across several steps, search semantically or full-text as needed, and fetch only what each step requires, so the loop is "search to understand, understand to search."

- **Handing the model the stopping decision is the cost of handing it the search plan.** Fixed top-k is brittle, but it terminates predictably. A planning agent decides for itself when it has enough, and the radiology analogy names how that goes wrong: it "finds something that it thinks is correct and then stops." So agentic retrieval trades a recall ceiling you can measure for a coverage decision you cannot observe from inside the loop. Two mitigations keep the flexibility without the blind spot: return multiple sources with each answer so continuation does not require a fresh search, and score trajectories against the targets the agent should have read. See [Satisfaction of Search Stops Agents at the First Plausible Hit](satisfaction-of-search-stops-agents-at-the-first-plausible-hit.md). ([Werry](../sources/20260827_qdAkxLoYNI8.md), 04:16-05:12)

Related topics:
- [Agents](../topics/agents.md)
- [Retrieval](../topics/retrieval.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Deep research agents need planning, grounded evidence, and pivot loops](deep-research-agents-need-planning-grounded-evidence-and-pivot-loops.md)
- [Redefine RAG as Iterative Multi-Tool Retrieval, Not Vector Search](redefine-rag-as-iterative-multi-tool-retrieval.md)
- [Treat Embeddings as Cached Compute Decided by Query Volume](treat-embeddings-as-cached-compute-decided-by-query-volume.md)
- [Satisfaction of Search Stops Agents at the First Plausible Hit](satisfaction-of-search-stops-agents-at-the-first-plausible-hit.md)

Sources:
- [OpenRAG: An open-source stack for RAG - Phil Nash](../sources/20260408_4TxOBhDRRCM.md), 07:24-08:15, 12:20-13:04
- [RAG is dead, right?? - Kuba Rogut, Turbopuffer](../sources/20260609_UM6sFg_jdlE.md), 02:46-09:42
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 04:16-05:12
