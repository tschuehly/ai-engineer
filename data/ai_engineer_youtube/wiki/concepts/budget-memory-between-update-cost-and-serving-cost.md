# Budget Memory Between Update Cost and Serving Cost

Summary: "Memory is a function of compute." A running profile costs to maintain (update frequency × compute per update) and costs again on every conversation it enters (profile length × traffic), and those two costs trade against each other under one GPU budget — which is why a large profile updated rarely and a small profile updated daily are two answers to the same question, not one right and one wrong design.

Use when:
- Sizing a personalization profile, or justifying why it is not larger.
- Choosing an update cadence for a memory system and needing the argument for cheap-but-frequent versus rich-but-rare.
- Explaining why a memory design that looks obviously better in isolation was not shipped.

Details:
- The two cost centres, stated plainly: maintenance "depends on how frequently you update it and how much compute you apply to each update," and serving exists because "these profiles are part of the context window for every single conversation," so "the longer the profile the more it costs to serve" (12:08-12:37).
- The unconstrained design is easy to name and is the tell that the constraint is doing the work: update every hour or after every conversation, spend a strong model with subagents on each update, and store 400,000 tokens instead of 4,000. "Unfortunately we live in a GPU constrained world and trade-offs have to be made" (12:37-13:14).
- The two flagship consumer products sit at opposite corners of that budget as of the talk. ChatGPT: ~4,000 tokens, updated every few days — higher serving cost, lower update cost. Claude: ~1,000 tokens, updated every 24 hours — the exact opposite trade (13:14-13:37).
- The serving cost is per-conversation and unavoidable for the always-on half of a memory system, which is what makes profile length a product-wide inference bill rather than a storage decision. The retrieval half has the inverse profile: it costs nothing on turns where the model does not call it.
- Compression style is part of the same budget. ChatGPT's dense keyword clues buy more content per served token than Claude's complete sentences; the bet is that the model reconstructs the meaning at conversation time (04:58-05:47, 08:20-08:46).
- **The read half of the budget has its own cost law, and it is not about length.** Where the serving cost of an always-on profile scales with tokens × traffic, the cost of *retrieved* memory scales with how wrong it is: "bad memory is expensive because it spends more token and it can send the agent the wrong way," and in a controlled ablation the most accurate recall policy was also the cheapest — "it's not just that it gives you better recall, it actually costs less." That breaks the tradeoff framing on the retrieval side: you do not buy accuracy with tokens there, you buy both together by ranking better. The corollary for this page's budget is that the on-demand half is not simply the cheap half — a noisy retriever can cost more than a long profile, because misdirection is charged in extra turns rather than in prompt size. See [Bad Recall Costs More Than No Recall](bad-recall-costs-more-than-no-recall.md). ([Memory Harnesses for Long-Running Research Agents](../sources/20260812_R3-anFK1YM8.md), 09:36-10:02)
- Corollary for anyone benchmarking their own memory system against a vendor's: the observable numbers (profile size, refresh interval) are the output of someone else's traffic and margin, so copying the operating point copies their economics, not their quality.

Related topics:
- [Inference](../topics/inference.md)
- [Context Engineering](../topics/context-engineering.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Replace User-Managed Memory Lists With a Background-Synthesized Profile](replace-user-managed-memory-lists-with-a-background-profile.md)
- [Pair a Running Profile With On-Demand Conversation Search](pair-a-running-profile-with-on-demand-conversation-search.md)
- [Do not treat long context as durable model memory](do-not-treat-long-context-as-durable-model-memory.md)
- [Frequency, Not Volume, Drives Web-Context Cost](frequency-not-volume-drives-web-context-cost.md)
- [Profile Synthesis Is Continual Learning Outside the Weights](profile-synthesis-is-continual-learning-outside-the-weights.md)
- [Bad Recall Costs More Than No Recall](bad-recall-costs-more-than-no-recall.md)
- [Treat Memory as a Write–Manage–Read Control Loop, Not a Store](treat-memory-as-a-write-manage-read-control-loop.md)

Sources:
- [Lessons from Studying Every Memory System — Shlok Khemani, Independent](../sources/20260812_5ZGyKWjQDr0.md), 04:58-05:47, 08:20-08:46, 12:08-13:37
- [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](../sources/20260812_R3-anFK1YM8.md), 09:36-10:02
