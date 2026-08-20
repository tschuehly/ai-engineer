# Rank a Decisions Ledger Instead of Retrieving Memories by Similarity

Summary: For long-horizon agents, recording what was *decided* on each turn and then ranking those decisions beat pulling memories by embedding similarity — and beat every other rung tested, including an oracle handed the right memory. The reusable claim is that the unit of memory should be a decision with a priority, not a chunk with an embedding.

Use when:
- Choosing what an agent writes to memory each turn, and in what form.
- A vector store over agent history is retrieving plausible-looking but useless context.
- Designing recall for a run long enough that early turns fall out of the window.

Details:
- The comparison, with the model and everything else held fixed. The ladder ran no-recall, vector RAG "just to see whatever the harness would pull in terms of similarity," a decisions ledger, and an oracle. "The rank only ledger performed the best." ([Memory Harnesses for Long-Running Research Agents](../sources/20260812_R3-anFK1YM8.md), 04:28-05:18, 08:17-08:32)
- What the ledger is: "a decisions ledger where I actually keep track of what decisions are being made for every turn, and then I can prioritize them." Two mechanisms, not one — a **write policy** (capture decisions per turn) and a **read policy** (rank them), and the winning condition is named for the ranking. (04:50-05:00)
- The task shape it wins on: an xbench question whose answer sits at step 124 while the question arrives at step 500, "completely outside of the context window." Similarity has little to work with when the useful item is one specific past step among hundreds; a ledger of decisions is already a much smaller, already-structured candidate set. (06:56-07:33)
- Robustness checks that the policy survived: arbitrary examples, the wrong step, and the most recent step were all fed in as ablations, "and I still found that the best performing condition was the one with the ranked policy for recall." The recency heuristic — a common default — was among the conditions it beat. (08:59-09:22)
- It also beat asking the model whether it needed memory at all; see [Do Not Gate Memory Use on the Agent's Own Judgment](do-not-gate-memory-use-on-the-agents-own-judgment.md). (08:17-08:32)
- Held across a second local model (DeepSeek V4 Flash) and a second benchmark (Spider V2), which is what raises this from a benchmark artifact to a candidate policy result. (09:24-09:36)
- **Independent convergence, from a different mechanism.** StarlightSearch reaches the same "similarity alone loses" conclusion by re-ranking memories on a *utility* score learned from whether each memory preceded a pass or a fail — see [Rank Agent Memory by Outcome Utility, Not Just Similarity](rank-agent-memory-by-outcome-utility-not-just-similarity.md). The two answers are complementary rather than competing: this one changes the *unit* stored (a decision, not a chunk) and ranks structurally with no outcome labels required, while the utility approach keeps the unit and learns the ranking from outcomes, at the cost of a cold start. A system could do both.
- Caveats: no accuracy figures are given for any condition, so the *ordering* is the finding; the ranking function itself is not described beyond "prioritize them," which is the load-bearing detail a reimplementation would need; and both base models were local and quantized.

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Rank Agent Memory by Outcome Utility, Not Just Similarity](rank-agent-memory-by-outcome-utility-not-just-similarity.md)
- [Do Not Gate Memory Use on the Agent's Own Judgment](do-not-gate-memory-use-on-the-agents-own-judgment.md)
- [Ablate the Recall Policy With a Ladder and an Oracle](ablate-the-recall-policy-with-a-ladder-and-an-oracle.md)
- [Treat Memory as a Write–Manage–Read Control Loop, Not a Store](treat-memory-as-a-write-manage-read-control-loop.md)
- [Bad Recall Costs More Than No Recall](bad-recall-costs-more-than-no-recall.md)
- [Offload Long-Horizon Agent State Outside the Context Window](offload-long-horizon-agent-state-outside-the-context-window.md)
- [Repo-Local Markdown Tasks Give Agents Durable Scoped Work Units](repo-local-markdown-tasks-give-agents-durable-scoped-work-units.md)

Sources:
- [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](../sources/20260812_R3-anFK1YM8.md), 04:28-05:18, 06:56-07:33, 08:17-09:36
