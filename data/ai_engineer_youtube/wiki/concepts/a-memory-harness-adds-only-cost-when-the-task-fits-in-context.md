# A Memory Harness Adds Only Cost When the Task Fits in Context

Summary: If everything the task needs already fits inside the context window, a memory harness buys nothing — measured as identical accuracy at higher cost. The harness earns its complexity only once the relevant context provably does not fit, which makes "does it fit?" the first question to answer before designing memory at all.

Use when:
- Scoping a memory or retrieval layer and needing a reason not to build one yet.
- A memory system shows no quality gain in eval and you are looking for the explanation before tuning it.
- Justifying a memory harness to reviewers, or being asked to justify one.

Details:
- The measured null result. On a literature-review task over a paper corpus: "because for these tasks, all the papers and all the information fit into the context, the memory actually didn't add more capability. It was the same performance with memory and without memory, and it only added more cost. So when your task fits in context, the harness doesn't add much." ([Memory Harnesses for Long-Running Research Agents](../sources/20260812_R3-anFK1YM8.md), 06:14-06:39)
- The task was not trivially easy — it was designed as a needle problem. The corpus contained a Nature paper claiming the discovery of 742,000 promising materials, later retracted, where "the retraction, it's a much smaller haystack needle in that corpus than the headlines and the citations." Difficulty of *finding* the answer was not what the harness fixed, because the answer was already in the window. (05:29-06:05)
- The complementary positive: "if I start to run tasks that are longer term horizon, and the entire task and the relevant context doesn't fit, then having a good memory harness really starts to pay off." The same harness, the same model, opposite verdicts — the discriminating variable is fit, not task quality. (06:41-06:55)
- The out-of-window case that makes the harness the entire game, from the same study: "the right answer is in like step 124, but the moment when I ask the question, I'm asking it like at step 500. So it's completely outside of the context window, and the model needs to use the memory harness to retrieve the specific answer from the right step." (06:56-07:33)
- Practical reading: the boundary is a *cheap* test. Both halves of it came from one ablation on one machine, because the null result only requires running the task with the recall block turned off — the bottom rung of [the recall ladder](ablate-the-recall-policy-with-a-ladder-and-an-oracle.md).
- This is the memory-specific case of a pattern the wiki has now measured three times on different layers: doing nothing beat every context-compaction preset in Towards AI's bake-off, and agentic knowledge-base browsing tied a tuned retriever at 50% worse latency. In all three, an intuitively sensible addition cost real money for no measured gain, and only a do-nothing control revealed it.
- Caveats: no accuracy figures are given for either task, only the statement of equality; the models were local and quantized; and "fits in context" was assessed by construction of the corpus rather than by a reported token count.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Ablate the Recall Policy With a Ladder and an Oracle](ablate-the-recall-policy-with-a-ladder-and-an-oracle.md)
- [Bad Recall Costs More Than No Recall](bad-recall-costs-more-than-no-recall.md)
- [Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md)
- [Measure Agentic Knowledge-Base Browsing Before Adding It](measure-agentic-knowledge-base-browsing-before-adding-it.md)
- [Do not treat long context as durable model memory](do-not-treat-long-context-as-durable-model-memory.md)
- [Full History Recalls Details That Summaries Delete](full-history-recalls-details-that-summaries-delete.md)
- [Offload Long-Horizon Agent State Outside the Context Window](offload-long-horizon-agent-state-outside-the-context-window.md)

Sources:
- [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](../sources/20260812_R3-anFK1YM8.md), 05:29-07:33
