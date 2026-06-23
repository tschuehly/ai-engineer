# Read an Agent's Reasoning to Catch It Bullshitting

Summary: When supervising many parallel coding agents, the high-leverage skill is not prompting but detecting when an agent has gone off the rails — and the tell is the *quality of its reasoning narration*, not its actions. An agent that is waffling, not making sense, or doesn't seem to know what it's doing is "bullshitting" you the same way an underperforming employee would; the right move is to cut that session rather than keep wrestling with it.

Use when:
- Watching reasoning/thinking streams across several concurrent agent sessions and deciding which to trust.
- Deciding whether to let a session continue, nuke it, or hand it off.
- Building intuition for agent supervision instead of relying on the model's self-reported "done."

Details:
- The signal is *how* the agent explains itself, not *what* it's doing: a lane "sounds off" because the narration is waffling, incoherent, or shows the agent doesn't know what it's doing — analogous to the Matrix "I can see the woman in the red dress" scene where you learn to read the stream. (12:05-12:50)
- This mirrors managing people: if a report "started downright bullshitting," you'd stop and ask what's going on — the same instinct applied to a reasoning trace. (12:50-13:00)
- Disposition on a bad session: nuke it and leave that section of code to another maintainer, or come back to it four or five days later — don't pour more attention into a session that has lost the plot. (13:00-13:10)
- The intuition is earned, not free: it was built from the "sheer volume of token maxing" over the prior year of running agents at scale — supervision skill compounds with exposure. (13:10-13:17)
- It is the explicit complement to per-lane supervision: typed swim lanes decide *how much* to watch each session; reading the reasoning decides *when a watched session has failed* and should be cut. (whole talk)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Run Parallel Coding Sessions as Typed Swim Lanes](run-parallel-coding-sessions-as-typed-swim-lanes.md)
- [Turn Tool Errors Into Agent Self-Healing Recovery](turn-tool-errors-into-agent-self-healing-recovery.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Human Ownership Keeps Agent Pull Requests From Bypassing Review](human-ownership-keeps-agent-pull-requests-from-bypassing-review.md)

Sources:
- [Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw](../sources/20260605_pmoDeA3RBZY.md), 12:05-13:17
