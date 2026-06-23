# Mine Agent Conversation History to Generate Missing Skills

Summary: Coding-agent sessions leave a durable, locally stored record (JSONL conversation logs). A scheduled retrospective pass over that history can find where the human and agent spent excessive thinking tokens or went back and forth to remove ambiguity, then convert that "delta" into new skills, MCP servers, or workflow rules so the same friction does not recur.

Use when:
- A developer's agent sessions repeat the same struggles week over week.
- You want the harness to improve itself from real usage rather than from speculative upfront rules.
- Deciding which new skills, tools, or MCP servers would have the highest leverage.

Details:
- Claude Code conversations are saved locally as JSONL files; treating those sessions as "gold" (not trashing the accumulated context) enables a scheduled pass — daily or weekly — where an agent reviews your own conversations with it. (13:22-14:08)
- The pass looks for patterns of struggle: places where you spent a significant amount of thinking tokens, or where you and the agent went back and forth to eliminate ambiguity before a task succeeded, then asks what skills/MCP servers are missing and what the delta would be if you had them, so the loop tightens next week. (14:08-15:31)
- Claude Code includes a built-in skill that can not only author skills but evaluate and improve them, turning a natural-language prompt into a bespoke skill — so the analysis output can be acted on directly. (14:42-15:01)
- A single retrospective pass with a capable model (Opus 4.6) can reveal many skills that would make next week's work faster and more reliable, which is the payoff for keeping session context instead of discarding it. (15:01-15:31)
- Caveat: raw JSONL is "not really meant for AI consumption" — it gets long and full of junk. Pointing the model straight at it works, but a more robust path uses hooks that fire at session-end or PR-merge to extract the key bits (especially where you struggled) into a separate store (Obsidian, a flat weekly markdown file, or an archive) before the periodic analysis runs. (20:07-21:30)
- This is a different cadence from per-run loop feedback: it is a periodic batch retrospective across many stored sessions, aimed at discovering missing capabilities rather than fixing the current run.
- A continuous, agent-driven variant runs the same idea per skill rather than as a backlog-wide pass: at OpenClaw, skills live as `.skills` (open-sourced on GitHub, analogous to dotfiles), and a "Go Codex" skill goes through the agent's own Codex session logs, reads them, and edits that skill to make it better, after which the improved skill is redeployed into the open core or personal environment — so the agent maintains its own skills from real usage instead of a human authoring each revision (tooling named, auto-caption approximate: a skills "gem" like Geppetto, `vercel.skills.sh`). (Koc, 13:20-14:21)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Use Compounding Engineering Loops](use-compounding-engineering-loops.md)
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)
- [Skills turn procedural feedback into transferable agent memory](skills-turn-procedural-feedback-into-transferable-agent-memory.md)
- [Use agent hooks to automate session rituals](use-agent-hooks-to-automate-session-rituals.md)
- [Treat Human Attention as the Bottleneck for Agentic Work](treat-human-attention-as-the-agentic-bottleneck.md)
- [Run Parallel Coding Sessions as Typed Swim Lanes](run-parallel-coding-sessions-as-typed-swim-lanes.md)

Sources:
- [Your Attention Is the Bottleneck, Not Your Agents — Zack Proser, WorkOS](../sources/20260611_so9l_MwS2yg.md), 13:22-15:31, 20:07-21:30
- [Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw](../sources/20260605_pmoDeA3RBZY.md), 13:20-14:21
