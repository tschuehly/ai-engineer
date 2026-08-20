# Model Async Agent Work as Spawn, Send, Wait, Shut Down

Summary: Anything the agent starts and then keeps running alongside itself — a subagent, a long-lived shell — can be exposed through one handle abstraction with four operations: spawn an instance, send it input, wait on it, and shut it down. Codex uses the same primitive for subagents and background terminals rather than building two mechanisms.

Use when:
- Adding subagents, background processes, dev servers, or long-running jobs to a harness.
- Finding that the agent can start work it cannot then steer or stop.
- Deciding how many distinct concurrency concepts a model has to learn to use your tools.

Details:
- The subagent shape: "we give the agent a spawn agent tool, which then allows the agent to create new… agent instances, and then use a send input tool to either send new content to… those newly created agents, wait for an agent, or shut it back down." ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 07:18-07:49)
- The reuse is the point: "we use that same concept actually for background terminals as well. So, the Codex agent has a tool to spin up a new… background terminal and then continuously interact with it by sending new data through standard in… or wait for a specific amount of time for that agent to finish a task." A terminal and a subagent are different things, but the agent's relationship to both is identical. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 07:50-08:08)
- The category the talk puts these in is defined by the caller's obligation: async actions are "things that are happening while the agent has to continue to do work." That is what forces a handle — a blocking call would not need one. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 07:04-07:18)
- The four operations map onto the properties that make delegation controllable rather than merely possible: **send** makes the delegate steerable after launch instead of fire-and-forget, **wait** with a timeout gives the parent an explicit rejoin point instead of polling, and **shut down** gives it a way to stop paying for work it no longer needs.
- **What this adds to the wiki's subagent thread.** [Use Subagents to Isolate Context-Heavy Subtasks](use-subagents-to-isolate-context-heavy-subtasks.md) and [Customize Subagents by Task, Model, Tools, and Permissions](customize-subagents-by-task-model-tools-and-permissions.md) cover why to delegate and how to configure the delegate; this is the interface question underneath both — what the parent can do to a running child. It also gives the mid-run steering that a one-shot "run this subagent and return its output" call cannot express.
- The uniformity has a consequence worth stating: capability differences between kinds of async work then have to be expressed as *properties of the spawned instance* rather than as different tools. The [read-only review subagent](escalate-risky-actions-to-a-read-only-review-subagent.md) is spawned the same way but cannot spawn others, which is a per-instance restriction on the same primitive.
- **Provenance.** Tool names and behaviors as described in one vendor talk, with no schemas shown, no concurrency limits mentioned, and no account of what happens to orphaned handles when the parent turn ends. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 07:04-08:08)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Use Subagents to Isolate Context-Heavy Subtasks](use-subagents-to-isolate-context-heavy-subtasks.md)
- [Customize Subagents by Task, Model, Tools, and Permissions](customize-subagents-by-task-model-tools-and-permissions.md)
- [Escalate Risky Actions to a Read-Only Review Subagent](escalate-risky-actions-to-a-read-only-review-subagent.md)
- [Drive Computer Use Through a Persistent Scripting Session](drive-computer-use-through-a-persistent-scripting-session.md)
- [End a Long-Horizon Loop With a Model-Called Goal Tool](end-a-long-horizon-loop-with-a-model-called-goal-tool.md)

Sources:
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 07:04-08:08
