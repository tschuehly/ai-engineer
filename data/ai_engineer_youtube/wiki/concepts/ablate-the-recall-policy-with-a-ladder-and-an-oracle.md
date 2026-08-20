# Ablate the Recall Policy With a Ladder and an Oracle

Summary: To find out whether your memory system is earning its keep, hold the model and the task fixed and vary only the recall policy across a ladder — no recall at all, similarity retrieval, your structured policy, and an oracle handed the correct memory as ground truth. The bottom rung tells you whether memory helps at all; the top rung tells you how much of the remaining gap is even a retrieval problem.

Use when:
- Deciding whether to keep, replace, or delete a memory or retrieval layer in an agent.
- Designing an eval for a memory system rather than for a model.
- A memory system is being compared against a competitor's instead of against doing nothing.

Details:
- The controlled setup: "the model is fixed across all the different tasks. So the only things that I'm changing is like these different variables in the recall block." Everything else — core context, archival store, task, benchmark — is held constant. ([Memory Harnesses for Long-Running Research Agents](../sources/20260812_R3-anFK1YM8.md), 05:18-05:27)
- The four rungs as run (04:28-05:18):
  - **No recall at all** — "the baseline is like not to use memory at all." This is the do-nothing control, and on one of the two tasks it won.
  - **Vector RAG** — "just to see whatever the harness would pull in terms of similarity."
  - **A ranked decisions ledger** — "keep track of what decisions are being made for every turn, and then I can prioritize them."
  - **An oracle** — "basically this is the ground truth… telling the harness for every loop what the correct memory that needs to be retrieved is."
- A fifth condition was added and is worth copying because it tests a shipped default rather than a research idea: **gating** the harness by asking the model "do you need to use memory or do you not need to use memory." It lost to always-on ranked recall. (08:17-08:32)
- **The oracle rung is the part most harnesses omit, and it is the cheapest to add.** It bounds the recall problem: whatever the oracle fails to solve is not a retrieval defect, so effort spent on better retrieval cannot recover it. See [An Oracle Ceiling Separates Retrieval Failure From Use Failure](an-oracle-ceiling-separates-retrieval-failure-from-use-failure.md). (08:35-08:59)
- Adversarial ablations on the same axis, all cheap variants of the oracle: feed arbitrary examples, feed the wrong step, feed the most recent step. "And I still found that the best performing condition was the one with the ranked policy for recall." Giving the *wrong* memory deliberately is what separates a policy that works from one that happens to be surfacing something plausible. (08:59-09:22)
- Generalization was checked along two axes, not one: a second local model (DeepSeek V4 Flash alongside the model captioned "Qwen 27B") and a second benchmark (Spider V2 alongside xbench). A recall policy that only wins on one model and one benchmark has not been shown to be a policy result. (09:24-09:36)
- Scale, and the limits of it: 68 questions with "multiple cells and lots of different seeds" (08:05-08:17). **No effect sizes are reported anywhere in the talk** — every result is stated as an ordering ("performed the best," "more frequently than without," "costs less"), with no variance or significance test given. Treat the rank order of conditions as the finding and treat any magnitude as unmeasured.
- Provenance: single-author, unpublished work by a Sakana AI research scientist, run on local quantized models on one machine.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [An Oracle Ceiling Separates Retrieval Failure From Use Failure](an-oracle-ceiling-separates-retrieval-failure-from-use-failure.md)
- [A Memory Harness Adds Only Cost When the Task Fits in Context](a-memory-harness-adds-only-cost-when-the-task-fits-in-context.md)
- [Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md)
- [Measure Agentic Knowledge-Base Browsing Before Adding It](measure-agentic-knowledge-base-browsing-before-adding-it.md)
- [Invest in the Harness to Run Weaker and Local Models](invest-in-the-harness-to-run-weaker-and-local-models.md)
- [Treat Memory as a Write–Manage–Read Control Loop, Not a Store](treat-memory-as-a-write-manage-read-control-loop.md)
- [Rank a Decisions Ledger Instead of Retrieving Memories by Similarity](rank-a-decisions-ledger-instead-of-retrieving-memories-by-similarity.md)
- [Hold the Browser Environment Constant Across Runs](hold-the-browser-environment-constant-across-runs.md)

Sources:
- [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](../sources/20260812_R3-anFK1YM8.md), 04:28-05:27, 08:05-09:36
