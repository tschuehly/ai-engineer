# Run Parallel Coding Sessions as Typed Swim Lanes

Summary: A practical operating model for running many concurrent coding agents is to organize them into "swim lanes" categorized by work type — CI, test refactors, features, bugs, triage — and supervise each lane differently rather than babysitting all of them equally. Stable, low-risk lanes get fire-and-forget instructions; risky or exploratory lanes get an active conversation. The count scales up and down, and the binding constraint becomes raw compute and operator attention, not tokens.

Use when:
- One person needs to keep 10-20 coding sessions productive at once without a heavy orchestration framework.
- Deciding how much supervision each parallel agent deserves instead of treating them uniformly.
- Explaining why "more agents" stops helping once it exceeds the operator's brain space.

Details:
- The lanes self-partition by task type: e.g. lanes 1-2 are stable test refactors told to "take your time, make the tests pass, just commit and push" with little babysitting; lanes 3-4 are features/issues (Docker, a messaging channel) that need an active back-and-forth conversation; lane 5 triages new P0s/P1s from GitHub or a Discord-channel agent ("what happened in the last 2 hours I need to pay attention to"). (09:25-10:49)
- The model is "factory manager over a production line": at peak Vincent Koc ran ~10-15 foreground lanes and Peter Steinberger ~15, with up to 60-70 agents between them once subagents are counted; the OpenClaw project peaked at ~800 commits/day. (06:13-07:03, 04:34-04:44)
- Minimal process — "in harness we trust": no elaborate plan mode or spec mode, just a conversation with the agent worked through to a result. The complexity he added (git worktrees) he regrets; see the worktree caveat. (10:51-11:57)
- The bottleneck shifts: "tokens are no longer the problem"; what runs out is raw compute and the operator's brain space to keep an eye on every session — which is why supervision has to be triaged per lane, not spread evenly. (10:29-11:04)
- Feeding the lanes is its own step: with ~60k PRs/issues, a semantic graph / vector embedding over the backlog dedupes near-identical requests (one PR had ~106 edges), and convergent pressure across many duplicates becomes the signal for what to work on next — a way to decide, not a roadmap. (14:24-15:19)
- Framed as management, not prompting: "how do you manage 10+ agents?" is answered with "how do you manage 10+ staff?" — the soft skills of delegation and supervision transfer, so it's about the process, not the model or the agent. (15:38-16:14)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Read an Agent's Reasoning to Catch It Bullshitting](read-an-agents-reasoning-to-catch-it-bullshitting.md)
- [Parallel Coding Agents Support Multitasking and Variation Search](parallel-coding-agents-support-multitasking-and-variation-search.md)
- [Isolate Parallel Coding Work With Project Worktrees](isolate-parallel-coding-work-with-project-worktrees.md)
- [Human Taste Limits Fully Dark Coding Factories](human-taste-limits-fully-dark-coding-factories.md)
- [Treat Human Attention as the Bottleneck for Agentic Work](treat-human-attention-as-the-agentic-bottleneck.md)
- [Agent Managers Orchestrate Editor, Browser, and Background Agents](agent-managers-orchestrate-editor-browser-and-background-agents.md)

Sources:
- [Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw](../sources/20260605_pmoDeA3RBZY.md), 04:34-16:14
