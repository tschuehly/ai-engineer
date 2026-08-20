# Plain In-Context Learning Topped a Continual-Learning Benchmark

Summary: On the first release of a benchmark built specifically to require learning across instances, vanilla in-context learning — append the experience to the context and manage nothing — beat the more elaborate context-management systems on reward, and stayed ahead on both the reward-versus-cost and gain-versus-cost Pareto frontiers. It is the third independent measurement in this wiki where doing less to the context beat doing more.

Use when:
- Choosing between "just keep the history" and a memory or context-management system for a stateful agent.
- Justifying a memory architecture and being asked what it beats.
- Reading a claim that a context-management technique improves learning across sessions.

Details:
- The result, on all three axes: "the in-context learning systems, this is vanilla in context learning where you just put the experience in the context and you don't do any of the fancy context management that some of these other systems do. It tops the leaderboard and it's not just on reward. It's actually also when we look at the Pareto frontiers, this kind of holds across reward versus cost and gain versus cost." ([Evaluating Continual Learning](../sources/20260812_iqloyWCGYQQ.md), 13:52-14:28)
- Winning on **gain** as well as reward is the part that is hard to explain away. Gain is stateful reward minus the same system rerun with memory wiped between instances ([Measure Learning as Gain Over a Memory-Wiped Rerun](measure-learning-as-gain-over-a-memory-wiped-rerun.md)), so this is not the strong-base-model confound — plain context accumulation *learned more*, not merely scored higher.
- The tasks were built to make this hard: six domains, sequences with shared latent structure, deliberate concept drift, and a headroom requirement that rules out anything the base model could already do. The speaker's framing: "these more expensive context management systems perform a lot poorly compared to just vanilla in context learning on these sets of tasks where you have to do real learning." (13:01-13:52, 14:42-14:52)
- **The speaker's own caveat, volunteered rather than extracted, and the one to carry forward.** "You could argue that these were medium horizon tasks and they didn't push the frontiers of the in-context learning systems enough and I would say that's fair and that's one of the things on our road map to push those even further." Horizon is exactly the variable that should flip this result, so the finding is best read as bounded to task lengths where the accumulated history still fits comfortably. (14:28-14:42)
- He does not read it as settled either: "I don't necessarily think this is what the end state of continual learning might look like." (14:28-14:33)
- **Third independent convergence in this wiki, from three different teams on three different layers.** Towards AI's bake-off found full untouched history beat every compaction preset and their own shipped defaults on recall, cost, and latency at once ([Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md)). Sakana's memory ablation found a harness produced "the same performance with memory and without memory, and it only added more cost" whenever the corpus fit in the window ([A Memory Harness Adds Only Cost When the Task Fits in Context](a-memory-harness-adds-only-cost-when-the-task-fits-in-context.md)). This adds the learning axis: even where the task demands improvement over a sequence, the elaborate machinery did not buy it. The three do not share a mechanism, a benchmark, or a team.
- What the convergence does *not* license: all three studies sit at or below the window's capacity. The complementary half is measured too — when the answer sits at step 124 and the question arrives at step 500, "completely outside of the context window," the harness is the entire mechanism. The honest summary is that context management has to earn its keep against a growing-context baseline, and it only reliably does so once the content provably does not fit.
- Practical decision rule this supports: make "append everything and pay the tokens" the default, and require any context-management or memory layer to beat it on a gain-versus-cost plot on your own task sequences before shipping it.
- Caveats: **no numbers are reported** — no scores, no margins, no cost figures, no error bars, no instance counts. **The competing systems are never named**, so the result cannot be attributed to any particular product or paper. Parametric approaches were only partially represented in this release and are listed as future work.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Measure Learning as Gain Over a Memory-Wiped Rerun](measure-learning-as-gain-over-a-memory-wiped-rerun.md)
- [Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md)
- [A Memory Harness Adds Only Cost When the Task Fits in Context](a-memory-harness-adds-only-cost-when-the-task-fits-in-context.md)
- [Full History Recalls Details That Summaries Delete](full-history-recalls-details-that-summaries-delete.md)
- [Do not treat long context as durable model memory](do-not-treat-long-context-as-durable-model-memory.md)
- [Offload Long-Horizon Agent State Outside the Context Window](offload-long-horizon-agent-state-outside-the-context-window.md)
- [Explicit Context Attachments Can Outperform Opaque Agent Memory](explicit-context-attachments-can-outperform-opaque-agent-memory.md)
- [A Learning Benchmark Needs Headroom, Shared Structure, and a Signal](a-learning-benchmark-needs-headroom-shared-structure-and-a-signal.md)
- [Bad Recall Costs More Than No Recall](bad-recall-costs-more-than-no-recall.md)

Sources:
- [Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley](../sources/20260812_iqloyWCGYQQ.md), 13:01-14:52
