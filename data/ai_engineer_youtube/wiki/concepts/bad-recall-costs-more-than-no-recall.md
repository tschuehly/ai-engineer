# Bad Recall Costs More Than No Recall

Summary: "Bad memory is expensive because it spends more tokens and it can send the agent the wrong way." Recall quality and recall cost are not a tradeoff — the winning policy in a controlled ablation was simultaneously more accurate *and* cheaper, because wrong memory pays twice: once for the tokens it occupies and again for the work the agent does down the path it suggested.

Use when:
- A memory or retrieval layer is being justified or cut on cost grounds.
- Deciding whether to accept a noisier retriever to save tokens.
- Explaining why an agent's token bill grew after memory was added but accuracy did not.

Details:
- The measured direction: "it's not just that it gives you better recall, it actually costs less." The ranked decisions ledger won on both axes against vector similarity, recency, and no-recall-at-all conditions. ([Memory Harnesses for Long-Running Research Agents](../sources/20260812_R3-anFK1YM8.md), 09:36-09:41)
- The heuristic as stated, with both mechanisms named: "bad memory is expensive because it spends more token and it can send the agent the wrong way. But having like a good structural policy for recall can save you a lot of tokens and budget." The second mechanism is the one that gets missed — misdirection is a *trajectory* cost, not a prompt-size cost, and it does not show up in a per-call token count. (09:42-10:02)
- The corollary for cost accounting: budgeting memory by prompt tokens undercounts bad recall, because the expensive part is the extra turns spent on a wrong path. A recall policy's cost should be measured over the whole run, not over the retrieval call.
- Why this cuts against the intuitive framing. Adding memory looks like buying accuracy with tokens, so the natural saving is to retrieve less or retrieve conditionally. Both moves are wrong under this result: retrieving *better* is what reduces spend, and gating on the model's own judgment lost outright — see [Do Not Gate Memory Use on the Agent's Own Judgment](do-not-gate-memory-use-on-the-agents-own-judgment.md).
- The one case where the tradeoff framing holds is when the task already fits in the window, where the harness added cost and no capability at all — a different situation from bad recall, and one you can detect offline. See [A Memory Harness Adds Only Cost When the Task Fits in Context](a-memory-harness-adds-only-cost-when-the-task-fits-in-context.md). (06:14-06:39)
- Read alongside the serving-side account of memory cost: a running profile's cost is length × traffic on the write/serve side, while this page is about the read side, where the cost of a retrieved item scales with how wrong it is rather than how long it is. See [Budget Memory Between Update Cost and Serving Cost](budget-memory-between-update-cost-and-serving-cost.md).
- Caveats: no cost figures, token counts, or dollar amounts appear in the talk — the cost claim is directional. The measurement was on local models run serially, where token cost is wall-clock rather than an API bill, so the *relative* ordering is what transfers, not any monetary number.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Inference](../topics/inference.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Rank a Decisions Ledger Instead of Retrieving Memories by Similarity](rank-a-decisions-ledger-instead-of-retrieving-memories-by-similarity.md)
- [A Memory Harness Adds Only Cost When the Task Fits in Context](a-memory-harness-adds-only-cost-when-the-task-fits-in-context.md)
- [Do Not Gate Memory Use on the Agent's Own Judgment](do-not-gate-memory-use-on-the-agents-own-judgment.md)
- [Budget Memory Between Update Cost and Serving Cost](budget-memory-between-update-cost-and-serving-cost.md)
- [Cut Coding-Agent Cost by Fixing the Input, Not the Model or Output](cut-coding-agent-cost-by-fixing-the-input-not-the-model-or-output.md)
- [Measure Agent Interface Efficiency With Tokens per Successful Outcome](measure-agent-interface-efficiency-with-tokens-per-successful-outcome.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)

Sources:
- [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](../sources/20260812_R3-anFK1YM8.md), 06:14-06:39, 09:36-10:02
