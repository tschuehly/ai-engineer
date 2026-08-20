# Offload Long-Horizon Agent State Outside the Context Window

Summary: Long-horizon agents do not need to keep every state detail in the model context window. They can preserve coherence by writing state into code, documentation, plans, task lists, file-system memory, and scoped subagents that return compact results.

Use when:
- Designing agents that must run for long trajectories without relying on extremely large context windows.
- Deciding what state belongs in files, plans, task lists, memory stores, or specialist subagents.

Details:
- Replit's talk argues that long context models are not required for coherent long trajectories; even ambitious tasks can often fit inside roughly 200K tokens when context is managed deliberately. 15:13-15:49
- The codebase itself can maintain state through documentation written while new code is created. 15:52-16:08
- Plans, task lists, and memories can be persisted on the file system and reloaded when relevant rather than continuously included in the active prompt. 16:08-16:35
- Subagents provide separation of concerns: each starts from fresh context, receives only the subset needed for its task, runs to completion, and returns compact results to the main loop. 17:00-17:41
- Replit reported fewer context recompressions after moving work into subagent orchestration because less context pollution stayed in the main loop. 17:41-18:16
- Anthropic's Claude API talk describes memory as a client-side file-system-like tool that keeps codebase patterns and git workflow preferences outside the active context window, then lets Claude pull them back only when relevant. 05:12-05:55

- **The task shape that makes offloading non-optional, plus the failure symptoms it prevents.** Stefania Druga's long-horizon test case is an xbench question where "the right answer is in like step 124, but the moment when I ask the question, I'm asking it like at step 500" — the answer is not merely far away, it is "completely outside of the context window," so no context discipline recovers it and the harness is the only route. The symptoms she uses to characterize the failure this avoids are concrete enough to check for in production: "the model starts contradicting itself, or it has to redo the work because it forgot it did that task in the first place, or it starts to drift from your questions because it forgot them." Her framing of what the offloaded store must be is a **write–manage–read control loop** rather than a place to put things — "it's not just a database store" — because *what* is written and *how* it is ranked on read is what decides whether the offload helps; a decisions ledger ranked by priority beat vector similarity over the same history. ([Memory Harnesses for Long-Running Research Agents](../sources/20260812_R3-anFK1YM8.md), 00:46-01:04, 03:36-03:55, 06:56-07:33, 08:17-08:32)

- **The cheapest offload target is the run's own transcript.** Anthropic observes that "with many traditional harness implementations, the context window and the session are one in the same," which makes eviction destructive; persisting the session separately means "the harness can actually just read in slices of that context from the session log into its current window." That is offloading with no summarization policy and no schema — the store is the verbatim record, and the only design question is the read policy. It is a weaker mechanism than a curated ledger and a strictly cheaper one, which makes it a reasonable floor to have in place before building anything selective ([Keep the Session Log Separate From the Context Window](keep-the-session-log-separate-from-the-context-window.md)). ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 15:04-15:47)

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Use subagents to isolate context-heavy subtasks](use-subagents-to-isolate-context-heavy-subtasks.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [Do not treat long context as durable model memory](do-not-treat-long-context-as-durable-model-memory.md)
- [Context Window Editing Clears Stale Tool Results](context-window-editing-clears-stale-tool-results.md)
- [Treat Memory as a Write–Manage–Read Control Loop, Not a Store](treat-memory-as-a-write-manage-read-control-loop.md)
- [Rank a Decisions Ledger Instead of Retrieving Memories by Similarity](rank-a-decisions-ledger-instead-of-retrieving-memories-by-similarity.md)
- [Keep the Session Log Separate From the Context Window](keep-the-session-log-separate-from-the-context-window.md)

Sources:
- [The 3 Pillars of Autonomy - Michele Catasta, Replit](../sources/20251222_MLhAA9yguwM.md), 15:13-18:16
- [Katelyn Lesse - Evolving Claude APIs for Agents, Anthropic](../sources/20251204_aqW68Is_Kj4.md), 05:12-05:55
- [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](../sources/20260812_R3-anFK1YM8.md), 00:46-01:04, 03:36-03:55, 06:56-08:32
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 15:04-15:47
