# Isolate Parallel Coding Work With Project Worktrees

Summary: Worktree-backed agent sessions let multiple feature, bugfix, and investigation threads proceed within the same project without interfering with each other.

Use when:
- Running several coding-agent tasks in parallel on one repository.
- Designing review workflows where completed agent work should be inspectable as separate branches or diffs.

Details:
- Codex app projects can contain multiple worktrees, allowing individual feature requests, bug fixes, or Q&A sessions to run at the same time. 07:51-08:09
- Native worktree support is presented as a way to reduce context switching and prevent independent tasks from interfering with one another. 08:09-08:24
- The source also links worktrees with native Git support, allowing users to push changes with the intended Git identity or workflow surface. 09:13-09:27
- Scaling caveat: at extreme parallelism the worktree-per-PR pattern can backfire. Vincent Koc reports that running a heavy test harness against ~70-80 active worktrees in a day "completely nuked" his machine, and that he had to build self-heal logic so Codex stays aware of worktrees and recovers (e.g. sparse-checkout repair) when a crash leaves them inconsistent — so he wishes he hadn't adopted worktrees at all. (Koc, 10:51-11:50)
- Simpler alternative that several OpenClaw maintainers prefer: clone the whole repo ~10 times and point a separate coding-agent session at each clone, trading disk for the operational fragility of many worktrees on one checkout. (Koc, 11:50-11:57)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)
- [Evaluate workspace isolation with positive and negative filesystem scorers](evaluate-workspace-isolation-with-positive-and-negative-filesystem-scorers.md)
- [Run Parallel Coding Sessions as Typed Swim Lanes](run-parallel-coding-sessions-as-typed-swim-lanes.md)

Sources:
- [OpenAI Codex Masterclass  - Vaibhav Srivastav & Katia Gil Guzman](../sources/20260429_MhHEGMFCEB0.md), 07:51-09:27
- [Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw](../sources/20260605_pmoDeA3RBZY.md), 10:51-11:57
