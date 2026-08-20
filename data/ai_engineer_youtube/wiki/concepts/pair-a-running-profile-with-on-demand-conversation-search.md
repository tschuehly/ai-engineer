# Pair a Running Profile With On-Demand Conversation Search

Summary: Two flagship consumer assistants started at opposite ends of the memory design space — an always-on synthesized profile versus nothing but search tools over past conversations — and after three years of independent evolution both shipped the other half. The convergent shape is a small always-present profile plus model-invoked retrieval over conversation history.

Use when:
- Deciding whether personalization should be pushed into every prompt, pulled by the model when it decides it needs it, or both.
- Reviewing a memory design that has only one of the two halves and is failing on the other's job.
- Looking for an existence proof that the chunk/embed/vector-search recipe is not the only production answer for conversational memory.

Details:
- Claude's August 2025 v1 had **no profile and no fact list**. The model was given two tools: search past conversations by keyword or topic, and search by time period, answering queries like "what did we discuss last week" or "at the start of November of 2025." Every conversation started fresh with no user context and retrieval happened on demand when the model judged it necessary (06:59-08:03).
- ChatGPT's April 2025 v2 was the mirror image: a background-synthesized running profile prepended to every conversation, with no retrieval step at conversation time (03:56-04:58).
- The speaker had assumed two products with the same surface — chat box, conversation list, new conversation — would converge on the same memory design, and found they had not (07:07-07:24). His post naming them opposites hit the Hacker News front page on 2025-09-11; Claude shipped a running profile the same day (08:03-08:20).
- ChatGPT closed the gap from the other side during 2026 by adding a tool to search past conversations, "so the model can retrieve summarized context based on queries it makes" (09:16-09:33).
- The convergent architecture, stated as the end state of three years of independent evolution: a running profile that is visible and editable, plus tools for the model to look over past conversations (10:09-10:26). The two halves do different jobs — the profile is what is always true enough to pay for on every turn; search is for the specific thing that turns out to matter now.
- What neither does: "It wasn't too long ago that everyone including me assumed that RAG was the way to go about memory" — chunk conversations, embed, vector store, semantic search on the incoming query — and "neither ChatGPT nor Claude really do this" (10:32-11:00). Retrieval here is a model-invoked tool call over conversations, not a similarity lookup over chunks.
- Gemini takes a third position on the profile half: a running profile in which each memory carries detailed timing logs for when it was created and last updated (11:12-11:22).

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Replace User-Managed Memory Lists With a Background-Synthesized Profile](replace-user-managed-memory-lists-with-a-background-profile.md)
- [Budget Memory Between Update Cost and Serving Cost](budget-memory-between-update-cost-and-serving-cost.md)
- [Do Not Outsource the Memory System](do-not-outsource-the-memory-system.md)
- [Rank Agent Memory by Outcome Utility, Not Just Similarity](rank-agent-memory-by-outcome-utility-not-just-similarity.md)
- [Explicit Context Attachments Can Outperform Opaque Agent Memory](explicit-context-attachments-can-outperform-opaque-agent-memory.md)

Sources:
- [Lessons from Studying Every Memory System — Shlok Khemani, Independent](../sources/20260812_5ZGyKWjQDr0.md), 03:56-11:22
