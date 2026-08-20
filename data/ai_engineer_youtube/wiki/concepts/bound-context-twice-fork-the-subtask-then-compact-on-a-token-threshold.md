# Bound Context Twice: Fork the Subtask, Then Compact on a Token Threshold

Summary: Forking each subtask into its own context and returning only its summary bounds what any one subtask adds to the main thread, but it does not bound the total, because the summaries accumulate. The pattern is two controls in the same loop body: fork on the way in, then read the running token count and trigger compaction past a threshold on the way out.

Use when:
- Writing the orchestration loop yourself and deciding where context growth is actually stopped.
- A long session stays healthy per-step but degrades over hours, with no single subtask to blame.
- Choosing between "use subagents" and "compact often" as if they were alternatives.

Details:
- The anti-pattern named is "let every subtask dump its full output into the primary thread, crowding out the context," paired with the broader one, "let the context grow unbounded." The prescription is stated as two actions, not one: "You want to isolate your subtask output, and you want to compact long sessions." ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 15:17-15:48)
- **The first control is the fork.** For a task like "scan all the logs for error," you fork "the agent into like a separate thread where whatever the agent does and thinks and adds tokens to does not come back and pollute the main context," then "take this summation, and then you add that summation without all the other stuff into the overriding context." What re-enters the parent is a summary of where the problems are, not the log-reading trajectory that found them. ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 15:55-16:42)
- **The second control is a measured branch, not a habit.** "You can check your token count, and you can determine how big the token count is. And if you can set some limit and if you have more than 150,000 tokens, then what you want to do is you can run a compact." The threshold is the example given, not a recommendation with evidence behind it; what transfers is that the compaction decision is a comparison against a number the loop can read, so it fires deterministically instead of when someone notices the session feels slow. ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 16:42-17:08)
- The rationale for both is stated in the same breath and is two-sided: "context means tokens, tokens mean money, and the more context you have, the more confused the LLM is going to be in giving you an answer" — cost and accuracy degrade together. The explicit corollary is that a large window is capacity, not a plan: "even though oh, a million token context window, I can put everything in there. No, no, don't put everything in there. Limit what's going to go in there because then you're going to get a much more accurate system." ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 13:07-13:41)
- **The compactor is a seam you can own.** Vendor compaction is treated as a black box — "Anthropic and Claude have these compaction algorithms that take this giant context and compact it in some way, shape, or form. Not quite sure how the implementation is of that" — and the alternative offered is a framework that "provides custom logic for compression of context" where "you can extend his base class and have your own compression of your data, whatever you think is important." That matches this wiki's stronger position that useful compaction preserves task-specific particulars such as exact files and line numbers ([Frequent intentional compaction keeps coding agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md)), which a generic summarizer will not know to keep. ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 17:04-18:07)
- **What the threshold check does not settle.** Compaction is not free at the moment it fires: it discards the prefix that [prompt caching](prompt-caching-sets-the-break-even-bar-for-compaction.md) was amortizing, so a threshold tuned only against the window size ignores the cost side of the trade. The talk gives no method for choosing the number, no behavior for the case where the compacted result is still over the limit, and no discussion of what happens to a subtask summary that itself turns out to be the wrong slice.
- The isolation half is argued by analogy to shared-memory concurrency — with multiple threads over shared memory "you get into issues with synchronization… Keep the little threads independent. Keep your agents independent" — which is a useful intuition and also an imperfect one, since the failure here is dilution and cost rather than a data race, and forked agents that never see each other's state can duplicate or contradict work rather than corrupt it. ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 05:23-05:52)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Use Subagents to Isolate Context-Heavy Subtasks](use-subagents-to-isolate-context-heavy-subtasks.md)
- [Frequent intentional compaction keeps coding agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md)
- [Prompt caching sets the break-even bar for compaction](prompt-caching-sets-the-break-even-bar-for-compaction.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [Withhold the Producer's Reasoning From the Critic](withhold-the-producers-reasoning-from-the-critic.md)

Sources:
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](../sources/20260808_Z-c11pV_uvU.md), 05:23-05:52, 13:07-13:41, 15:17-18:07
