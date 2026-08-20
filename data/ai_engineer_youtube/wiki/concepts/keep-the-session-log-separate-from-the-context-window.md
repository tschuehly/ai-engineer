# Keep the Session Log Separate From the Context Window

Summary: "With many traditional harness implementations, the context window and the session are one in the same" — so anything dropped from the window is gone from the run. Persisting the session as a durable log the window reads *from* converts context management from a destructive operation into a retrieval one: "the harness can actually just read in slices of that context from the session log into its current window."

Use when:
- Designing compaction, summarization, or context-reset behavior and deciding what "dropping" a message means.
- An agent loses information mid-run that it later needs, and re-deriving it is expensive or impossible.
- Choosing where observability, memory, and self-improvement data come from — one durable log can serve all three.

Details:
- **The failure being fixed, named precisely.** When the window *is* the session, eviction is deletion. A summarizer that compresses the first 80% of a run has destroyed the original; a mid-run discard loses the run. The alternative separates storage from working set: the log is the record, the window is a view onto it. ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 15:04-15:47)
- **What it enables that compaction alone does not.** Slicing is directional and repeatable — the harness can pull back a specific earlier region when the task turns out to need it, rather than deciding once, irreversibly, at compaction time what the future will need. This is why the property is *recoverability* rather than *compression*; a good summarizer still cannot answer a question it summarized away.
- **It is also what makes a run survive its own process.** If the agent loop dies, it resumes from the "durable session resource in a session log" rather than starting over. Durability of the record and recoverability of the context are the same property viewed from two failure modes. (12:25-12:52)
- **One artifact, three consumers.** Anthropic reports the session log answering two questions that are usually served by separate systems — "what's going on under the hood" and "how do I make my agent better over time" — with events "written play-by-play" feeding observability, memory, and self-improvement. That is an argument for building the log as the primary artifact rather than as a debugging side-channel: a trace emitted for dashboards is usually lossy in exactly the ways a memory system needs it not to be. (24:58-25:47)
- **What this costs.** The log grows without bound, and the talk says nothing about retention, size limits, or what a session log costs to store for a long-running agent. It is also, by construction, a complete record of everything the agent saw — including anything sensitive that passed through the context — which makes its access controls a security surface, not just an operational one. Neither is addressed in the source.
- **Where the developer's judgment goes.** Separating the two does not decide *which* slices to read back. Anthropic explicitly leaves context management with the developer as one of the two things a hosted platform will not do for you: "this is what separates a coding agent from a legal agent or go-to-market agent." The separation is a mechanism; the read policy is still domain work. (15:50-16:47)
- Provenance: an Anthropic vendor talk describing its own managed-agent architecture. No measurement accompanies the claim — no comparison of task success with and without slice-back, no cost figure, no retention policy. The failure mode it describes (window ≡ session) is real and widely instantiated; the benefit of the fix is asserted rather than demonstrated.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Offload Long-Horizon Agent State Outside the Context Window](offload-long-horizon-agent-state-outside-the-context-window.md)
- [Own agent context instead of accepting hidden harness mutation](own-agent-context-instead-of-accepting-hidden-harness-mutation.md)
- [Decouple the Agent Loop From the Tool Execution Environment](decouple-the-agent-loop-from-the-tool-execution-environment.md)
- [Model a Managed Agent as Agent, Environment, and Session](model-a-managed-agent-as-agent-environment-session.md)
- [Rewrite Agent Memory in a Periodic Batch Pass Over Session Logs](rewrite-agent-memory-in-a-periodic-batch-pass-over-session-logs.md)
- [Record Workflow History for Agent Debugging and Compliance](record-workflow-history-for-agent-debugging-and-compliance.md)

Sources:
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 12:25-12:52, 15:04-16:47, 24:58-25:47
