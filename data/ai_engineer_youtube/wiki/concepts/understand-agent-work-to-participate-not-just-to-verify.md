# Understand Agent Work to Participate, Not Just to Verify

Summary: The reason a human still needs to understand agent-written code is not only to verify correctness — agents are getting good at that and the human's correctness role is shrinking — but to *participate*: each review loop changes you, and that accumulated understanding is what lets you have the next idea. Treat understanding as a compounding asset across loops, not a one-time gate on a single diff.

Use when:
- Deciding how much to stay in the loop as agents write more of the code.
- Arguing against "the agents are smart enough now, get out of the loop and just run it."
- Explaining why review speed alone (moving at the speed of correctness) is the wrong target.

Details:
- The common framing is "understand to verify": agents do dumb things and the human keeps them in line by asking "is this correct?" (matches the spec, doesn't take down production, is well architected) — but those are thumbs-up/thumbs-down decisions agents can increasingly make themselves given the right verification loop, so the human's role in correctness checking is decreasing, which Litt says he's fine with when he has a clear intent and the agent executes it. (02:42-03:52)
- The deeper reason is "understanding to participate": it's not one loop — reviewing what happened changes you, and that understanding is the foundation you carry to the next loop and the next; rich conceptual structures you can fluently recombine (without going out to ask an agent or human how it works) are what let you take creative leaps, "the human part of the work." (04:08-05:20)
- The failure mode is **cognitive debt** (Margaret-Mary Storey's term, an analogy to technical debt; also blogged by Simon Willison): you get away with it while vibe coding until you realize you have no idea what's going on and "basically can't participate anymore." (05:26-05:56)
- The team/collective version: shared understanding (including shared *names* for parts of a system) is what lets people communicate and jam creatively, so Notion is exploring multiplayer chat threads with multiple humans and agents in one visible space (like moving from one-on-ones to Slack channels) and commentable collaborative documents so a team can discuss an agent's plan in place; they run coding agents (Claude, Cursor) inside Notion for these shared-space benefits. (15:03-16:55)
- Optimistic frame (Alan Kay's "A Personal Computer for Children of All Ages," ~50 years old): computers were meant to level up humans, and because "code is free" now we can build ephemeral UIs and simulations to understand better than ever — putting ourselves *more* deeply in loops rather than out of them. (17:37-18:50)
- **A direct response from another speaker, accepting the diagnosis and rejecting its scope.** Gazit cites this talk by name and qualifies it: "that's very true at a me level. But my personal understanding was never sufficient for shipping code inside a team. Our understanding at an us level can't only happen at the end of the process, when the process happens so much faster." The move is from an individual comprehension problem to a group one, and it changes what the remedy has to be — a way for one person to follow an agent's work does not produce shared understanding across a team, which is why his answer is a multiplayer session and a co-edited document rather than a better review view. He also prices the failure: "a small misalignment can snowball into a ton of wasted work, and that work costs tokens, and tokens cost real money now." ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 01:34-01:43, 03:51-04:30)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Have Agents Write Literate Explainer Docs for Their Changes](have-agents-write-literate-explainer-docs-for-their-changes.md)
- [Gate Agent Code on a Comprehension Quiz You Must Pass](gate-agent-code-on-a-comprehension-quiz-you-must-pass.md)
- [Build Ephemeral Microworlds to Feel How Code Works](build-ephemeral-microworlds-to-feel-how-code-works.md)
- [Keep critical code inside human understanding and review capacity](keep-critical-code-inside-human-understanding-and-review-capacity.md)
- [Coding Agents Shift Engineering Work Toward Planning and Review](coding-agents-shift-engineering-work-toward-planning-and-review.md)
- [Tell the Agent Only What Is Not Recoverable From the Code](tell-the-agent-only-what-is-not-recoverable-from-the-code.md)

Sources:
- [Understanding is the new bottleneck — Geoffrey Litt, Notion](../sources/20260710_WkBPX-oDMnA.md), 02:42-05:56, 15:03-18:50
- [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../sources/20260808_iQ5xldZ9StU.md), 01:34-01:43, 03:51-04:30
