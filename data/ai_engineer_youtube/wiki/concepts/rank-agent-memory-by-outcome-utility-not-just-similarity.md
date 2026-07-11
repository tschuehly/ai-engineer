# Rank Agent Memory by Outcome Utility, Not Just Similarity

Summary: Retrieve agent memories by semantic similarity *weighted by whether each memory historically helped or hurt the run's outcome* — a utility score that rises when a retrieved memory precedes a pass and falls when it precedes a fail, like a credit score — so outcome becomes a first-class re-ranking signal instead of embedding similarity alone.

Use when:
- Designing agent memory and deciding which past traces/lessons to surface for the current task.
- An agent keeps repeating the same failure even though a "similar" memory is being retrieved.
- Choosing between a preference/conversation-history memory store and an outcome-aware one.

Details:
- Current memory systems (LangChain, Mem0) store user preferences, profile, and conversation history and retrieve by embedding similarity; they do not learn from outcome, so they behave like a chat experience rather than a self-improving production learning system, 03:36-04:32.
- The **utility score** = similarity weighted by how useful a memory was for executing the task, carrying the history of past pieces and past outcomes; retrieve by semantic similarity to the current task **weighted by whether those memories have historically helped or hurt the execution/outcome**, so the outcome is a first-class signal in re-ranking, not just retrieval, 04:32-05:40.
- Credit-score analogy (from the talk description): a retrieved memory that precedes a passing run gains utility; one that precedes a failing run loses it; the ranking formula combines semantic similarity with outcome history.
- **Treat memory as reasoning, not as facts** — not "user prefers dark theme," but "if someone asks for a refund, check the settlement before refunding so the customer isn't paid twice." Acting on usefulness (not static preferences) also combats context stuffing, 05:40-06:44.
- Reported lift: on tau-bench (policy adherence) 66% → 76% from utility-ranked memory, and 80% once stabilized reasoning is baked into skills; a similar trend on other agentic benchmarks (agentic figures ASR-uncertain in the source), 06:44-08:50.
- Failure modes: **cold start** (pure semantic search until enough reviews accumulate), **utility drift** (near-duplicate memories collide), **noisy review labels** making utility noisy, and a credit/re-ranking hyperparameter `lambda` to tune, 08:50-09:45.

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Close the Eval-to-Action Loop So Signal Survives the Dashboard](close-the-eval-to-action-loop-so-signal-survives-the-dashboard.md)
- [Rank RAG Results With Domain and Product Signals Beyond Relevance](rank-rag-results-with-domain-and-product-signals-beyond-relevance.md)
- [Skills Turn Procedural Feedback Into Transferable Agent Memory](skills-turn-procedural-feedback-into-transferable-agent-memory.md)
- [Explicit Context Attachments Can Outperform Opaque Agent Memory](explicit-context-attachments-can-outperform-opaque-agent-memory.md)

Sources:
- [User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch](../sources/20260628_Jx4ZFEAq6bY.md), 03:36-09:45
