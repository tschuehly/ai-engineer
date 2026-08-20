# Do Not Gate Memory Use on the Agent's Own Judgment

Summary: Asking the model "do you need memory for this?" before running recall performed worse than simply always running a good ranked recall policy. The model's self-assessment of whether it needs memory is a weak signal, so a gate built on it buys a token saving and pays for it in accuracy.

Use when:
- Designing a memory or retrieval layer and considering a cheap LLM gate to skip it on "easy" turns.
- A memory system is being tuned for cost and the first proposed saving is conditional invocation.
- Reviewing an architecture where the model decides when to call its own memory tools.

Details:
- The measured comparison: the ranked decisions ledger "performed better than like just gating the harness by saying do you need to use memory or do you not need to use memory." Gating was run as a full condition on the same ladder, with the model and task fixed. ([Memory Harnesses for Long-Running Research Agents](../sources/20260812_R3-anFK1YM8.md), 08:17-08:32)
- Why the result is not surprising once stated next to the oracle finding from the same study: a model handed the *correct* memory can still "choose to ignore it or be confused" (08:35-08:59). If model judgment about supplied memory is unreliable, model judgment about *needed* memory has no reason to be better. The two findings are the same weakness observed on the read side and the request side.
- The economic argument for gating does not survive either, because the study found good recall to be *cheaper* rather than more expensive — a gate that skips recall is not buying much even when it is right. See [Bad Recall Costs More Than No Recall](bad-recall-costs-more-than-no-recall.md). (09:36-10:02)
- What this does *not* say. It is not an argument against ever skipping memory — the same study found that when the whole task fits in context, the harness adds only cost, and that determination was made by the *engineer* from the task shape, not by the model at run time. See [A Memory Harness Adds Only Cost When the Task Fits in Context](a-memory-harness-adds-only-cost-when-the-task-fits-in-context.md). Gate on a property of the workload you can establish offline; do not gate on the model's introspection.
- Tension worth noting against a shipped consumer design: Claude's memory v1 was exactly a model-invoked design — no profile, two search tools, retrieval "on demand when it decides it needs to" — and both flagships now pair on-demand search with an always-on profile. The always-on half is what this result argues for; the on-demand half is not measured against a ranked alternative anywhere in the wiki. See [Pair a Running Profile With On-Demand Conversation Search](pair-a-running-profile-with-on-demand-conversation-search.md).
- Caveats: no figures are given for the gate condition or the margin it lost by; the gate's prompt is not described; and the base models were local and quantized, which may make self-assessment weaker than on a frontier model.

Related topics:
- [Agents](../topics/agents.md)
- [Retrieval](../topics/retrieval.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [An Oracle Ceiling Separates Retrieval Failure From Use Failure](an-oracle-ceiling-separates-retrieval-failure-from-use-failure.md)
- [Rank a Decisions Ledger Instead of Retrieving Memories by Similarity](rank-a-decisions-ledger-instead-of-retrieving-memories-by-similarity.md)
- [A Memory Harness Adds Only Cost When the Task Fits in Context](a-memory-harness-adds-only-cost-when-the-task-fits-in-context.md)
- [Pair a Running Profile With On-Demand Conversation Search](pair-a-running-profile-with-on-demand-conversation-search.md)
- [Ablate the Recall Policy With a Ladder and an Oracle](ablate-the-recall-policy-with-a-ladder-and-an-oracle.md)

Sources:
- [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](../sources/20260812_R3-anFK1YM8.md), 08:17-08:59, 09:36-10:02
