# Build Ephemeral Microworlds to Feel How Code Works

Summary: Agents can write code whose purpose is not to ship but to help *you* understand code — throwaway debuggers, simulations, and step-through UIs that let you inhabit a system and get an intuitive, peripheral-vision feel for it. This gives understanding that static docs and "just let the agent fix the bug" cannot.

Use when:
- A subsystem, algorithm, or migration feels hard to grasp from reading source or prose alone.
- You want intuition and "a feel for the machine," not just a verified fix.
- You want the learning benefit of doing something iteratively/by hand without the manual pain.

Details:
- Inspiration: Seymour Papert's idea of "Mathland" (kids learn French by living in France — where do they go to learn math?) and the Logo turtle; the point isn't the robot, it's that the kids are *changed* by programming it. Apply the same to understanding code. (12:06-12:45)
- Example 1 — a debugger microworld: Litt had Claude build an ephemeral UI to visualize a Prolog interpreter's internal implementation on a scrubbable, step-by-step timeline showing all state at each step (plus a commenting feature to leave notes to himself). He used it to fix narrow bugs *and* to get a feel for the machine — peripheral vision you don't get when an agent just fixes the bug for you. (12:45-13:53)
- Example 2 — a "do-it-yourself" game: migrating his personal website between frameworks, instead of trusting a one-shot script he had no feel for, he had Claude build a video-game-like tool (old site on the left, new site on the right, click Next through each step with the commands shown and file trees visibly moving) — the benefit of doing the port iteratively by hand without the pain. (13:54-14:50)
- Takeaway: "agents can write code to help us understand code" — building little micro worlds (the Mathland), simulations of just this one thing, not software to ship. Because "code is free," ephemeral UIs, dynamic simulations, debuggers, and playgrounds for understanding are now cheap to make — the Alan Kay vision of computers leveling up humans. (14:50-15:00, 17:37-18:50)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Understand Agent Work to Participate, Not Just to Verify](understand-agent-work-to-participate-not-just-to-verify.md)
- [Have Agents Write Literate Explainer Docs for Their Changes](have-agents-write-literate-explainer-docs-for-their-changes.md)
- [Dynamic artifacts make agent work reviewable and reusable](dynamic-artifacts-make-agent-work-reviewable-and-reusable.md)

Sources:
- [Understanding is the new bottleneck — Geoffrey Litt, Notion](../sources/20260710_WkBPX-oDMnA.md), 12:06-14:50, 17:37-18:50
