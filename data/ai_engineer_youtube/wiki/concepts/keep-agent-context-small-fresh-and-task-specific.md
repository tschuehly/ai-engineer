# Keep agent context small, fresh, and task-specific

Summary: Agent context should be deliberately curated, externalized, trimmed, and isolated by task. More context can increase cost, degrade quality, and preserve stale or wrong assumptions that pull later work back toward failed paths.

Use when:
- A long coding-agent session starts producing confused or repetitive changes.
- Deciding whether to add files, MCP servers, history, or project notes to an agent run.

Details:
- Each additional context token adds recurring input cost because chat history is resent, and heavily filled context windows can degrade output quality rather than improve it. (04:33-05:32)
- The cost half of that claim is now provider-dependent and worth checking before acting on it. Where the prefix is cache-stable, resent history is charged at the cached rate — up to 50x cheaper on some APIs — so the recurring cost of an extra token can be close to zero, and Towards AI measured the setup sending the *most* tokens as the cheapest to run (97% of its tokens cached). The quality half of the claim is unaffected; the cost half applies to context that is *newly added or rewritten* each turn, not to a stable history that keeps hitting the cache. ([Context Engineering in 2026](../sources/20260817_WP3hjUXd918.md), 15:55-17:37, 52:10-53:07)
- Always-enabled MCP servers and broad file references can add background tool and code context that is unrelated to the current step. (05:32-05:52)
- Bad context can poison output when a session mixes unrelated tasks, includes outdated comments, or retains earlier wrong decisions after the human tries to steer back. (05:58-06:49)
- Durable information should live outside the active context window in scratchpads, memory files, and AGENTS.md-like project instructions, then be selectively pulled in for the current task. (07:16-08:05)
- When the session has drifted, start a new session, have the agent summarize the useful state for the next agent, manually verify the summary, and continue with only the corrected context. (10:37-11:15)
- Splitting work across agents or sessions can be useful primarily because it isolates task context and prevents irrelevant or wrong history from accumulating. (08:30-08:48)
- Vibe engineering needs explicit context surfaces such as rules, docs, commands, and memories because the model cannot hold an entire app context or infer project intent like a mind reader. (10:59-11:13)
- Frequent intentional compaction treats correctness, completeness, size, and trajectory as context-quality dimensions; repeated correction history and wrong research can poison the next tool choice even when the prompt still fits in the model window. 04:38-05:43
- For coding agents, broad static onboarding can become too large or stale, while on-demand compressed context can summarize only the current vertical slice from source-backed code. 12:14-14:10
- A symptom checklist for the failure this page prevents, usable as a production trigger rather than a diagnosis after the fact: the model "starts contradicting itself, or it has to redo the work because it forgot it did that task in the first place, or it starts to drift from your questions because it forgot them." Each maps to a different remedy — self-contradiction to conflict surfacing, repeated work to a decisions record, question drift to keeping the task statement pinned in the core context. The same talk cites "keeping the context clean" as one item in a reported organizational cost reduction (Coinbase, via a CEO tweet, alongside more local models, better routing, better caching, and per-task usage visibility) — second-hand and unquantified, but the only place in the wiki where context hygiene appears in a *company-level* spend story rather than a per-session one. ([Memory Harnesses for Long-Running Research Agents](../sources/20260812_R3-anFK1YM8.md), 00:46-01:04, 01:44-02:17)
- A self-improving injected-context bank needs the same hygiene: Lovable's "Stack Overflow" entries go stale "incredibly quickly" — every new model release or feature change — so they aggressively rebalance and discard knowledge, because deprecated entries cause context rot and actively hamper the agent rather than helping it. Freshness here is a maintenance task on the knowledge store, not just on a single session's window. (Lovable 10:27-11:02)
- **A large window is capacity, not a plan, and the two costs move together.** Coyle states the trade in one line — "context means tokens, tokens mean money, and the more context you have, the more confused the LLM is going to be in giving you an answer" — and applies it directly to the temptation a long window creates: "even though oh, a million token context window, I can put everything in there. No, no, don't put everything in there. Limit what's going to go in there because then you're going to get a much more accurate system." The accuracy claim is asserted rather than measured here, and this wiki's [do-nothing baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md) result is a real counterweight on the cost half; the argument for restraint holds on quality grounds in agentic work more than on token price. ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 13:07-13:41)
- **Smallness obtained by reference rather than by omission.** Figma's design-to-code server names the consumer's own component instead of reproducing it — the payload shrinks to "use button component" and fidelity goes *up*, because the referenced component carries accessibility and internationalization properties the generated copy silently dropped. Where the usual context-trimming move trades completeness for size, referencing something the reader already holds avoids the trade entirely, at the cost of needing an authored mapping between your vocabulary and theirs. ([Lumarie](../sources/20260828_ZIYYsAzaLlA.md), 07:36-08:37)

- **"Task-specific flow" as the reason, stated independently of cost.** Werry refuses the dump-everything move with two reasons that need separating: the organizational corpus does not fit "even [in a window] that's a million tokens in size," and — the reason that survives any window size — "it causes the agent to get distracted. When you're working on a task, you want task-specific flow… your agents will get distracted easily if you give them things that cause them to look this way in that way. And it'll just waste tokens and time." Teams that justify trimming on token cost alone will stop trimming when tokens get cheap; the distraction argument does not expire. ([Werry](../sources/20260827_qdAkxLoYNI8.md), 05:34-06:20)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Context development lifecycle treats context as an engineered artifact](context-development-lifecycle-treats-context-as-an-engineered-artifact.md)
- [Own agent context instead of accepting hidden harness mutation](own-agent-context-instead-of-accepting-hidden-harness-mutation.md)
- [MCP tool surfaces need default context budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Frequent intentional compaction keeps coding agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md)
- [Mine stuck-then-solved sessions for injectable fixes](mine-stuck-then-solved-sessions-for-injectable-fixes.md)
- [Prompt Caching Sets the Break-Even Bar for Compaction](prompt-caching-sets-the-break-even-bar-for-compaction.md)
- [Treat Memory as a Write–Manage–Read Control Loop, Not a Store](treat-memory-as-a-write-manage-read-control-loop.md)
- [Bound Context Twice: Fork the Subtask, Then Compact on a Token Threshold](bound-context-twice-fork-the-subtask-then-compact-on-a-token-threshold.md)
- [Return a Pointer to the Reader's Own Component Instead of a Faithful Copy](return-a-pointer-to-the-readers-own-component-instead-of-a-copy.md)

Sources:
- [Agentic Engineering: Working With AI, Not Just Using It - Brendan O'Leary](../sources/20260407_BEKc4P87XKo.md), 04:33-11:15
- [From Vibe Coding To Vibe Engineering - Kitze, Sizzy](../sources/20251214_JV-wY5pxXLo.md), 10:59-11:13
- [No Vibes Allowed: Solving Hard Problems in Complex Codebases - Dex Horthy, HumanLayer](../sources/20251202_rmvDxxNubIg.md), 04:38-05:43, 12:14-14:10
- [How Lovable self-improves every hour — Benjamin Verbeek, Lovable](../sources/20260602_KA5kPbdkK2E.md), 10:27-11:02
- [Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](../sources/20260817_WP3hjUXd918.md), 15:55-17:37, 52:10-53:07
- [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](../sources/20260812_R3-anFK1YM8.md), 00:46-01:04, 01:44-02:17
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](../sources/20260808_Z-c11pV_uvU.md), 13:07-13:41
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 07:36-08:37
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 05:34-06:20
