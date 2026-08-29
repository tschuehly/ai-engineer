# Treat Memory as a Write–Manage–Read Control Loop, Not a Store

Summary: Agent memory is a control loop wrapped around the model — write, manage, read — rather than a database you attach to it. Naming the three phases separately is what makes memory debuggable and ablatable, because each phase has its own policy, its own cost, and its own failure mode.

Use when:
- Designing or reviewing an agent memory system and needing a decomposition to reason about rather than a product to pick.
- A memory system "works" but you cannot say which phase is responsible for a wrong answer.
- Choosing what to vary in a memory experiment, or what to instrument in production.

Details:
- The framing, stated as the mental model to keep: "you can think of memory as a write-manage-read loop… So, it's not just a database store. It's actually this control loop around the model." ([Memory Harnesses for Long-Running Research Agents](../sources/20260812_R3-anFK1YM8.md), 03:36-03:55)
- The concrete decomposition used in the experiment has three blocks, each with a distinct contract: a **core** that "is always shown to the agent"; a **recall** block where "I'm testing different modes"; and an **archival** block "keeping track of information across different sessions." Only the recall block was varied, which is what made the study an ablation rather than a comparison of products. (03:57-04:28)
- The choice of starting point follows from the framing: research agents were used "because they have zero durable memory, and I wanted all the memory to come from the harness." A subject with no built-in memory isolates the harness's contribution; a subject that already has memory confounds it. (03:57-04:08)
- Consequence for design questions. Once memory is a loop, the open questions are policies rather than schemas: "what are the type of memories that you want to store? How do you rank them? Like, how do you design your recall function?" plus the cross-session one — "what survives when you run this over and over and over and multiple sessions, multiple runs?" (10:02-10:35)
- The landscape sits on a structure axis, not a vendor axis: solutions run "from simple file system retrieval to training memory models… a wide spectrum of solutions from less structural to completely structured," and memory itself decomposes further into short-term, long-term, and "different cognitive techniques" — with evaluation results themselves usable as stored memory. (10:54-11:22)
- **The manage phase can be moved off the request path entirely.** Anthropic describes "dreaming": session transcripts plus the current memory state fed into "a periodic batch process" that extracts "new insights and new organized structures that essentially feed back and edit the memory as needed to make the next day's agent sessions automatically much more intelligent." This is the clearest example of why the three phases are worth separating — batching only makes sense for *manage*, and it buys three things a per-turn writer structurally cannot have: visibility across many sessions, freedom from latency pressure, and standing to decide an older memory is now wrong. Recorded with its unaddressed hazards (conflict resolution, rollback, cost, evaluation) as [rewrite agent memory in a periodic batch pass over session logs](rewrite-agent-memory-in-a-periodic-batch-pass-over-session-logs.md). ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 27:28-28:44)
- Provenance: single-author, unpublished work presented in a 13-minute talk, run on local quantized models; the framing is a mental model the speaker asks the audience to adopt, not a measured claim. The dreaming addition comes from a vendor talk where it appears on a coming-soon list with no evaluation attached.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Ablate the Recall Policy With a Ladder and an Oracle](ablate-the-recall-policy-with-a-ladder-and-an-oracle.md)
- [Rank a Decisions Ledger Instead of Retrieving Memories by Similarity](rank-a-decisions-ledger-instead-of-retrieving-memories-by-similarity.md)
- [Agent Harnesses Combine Model, Tools, Prompts, Filesystem, Skills, Hooks, and Memory](agent-harnesses-combine-model-tools-prompts-filesystem-skills-hooks-and-memory.md)
- [Do Not Outsource the Memory System](do-not-outsource-the-memory-system.md)
- [Give Enterprise Agents Tiered Database Memory With an Escape Hatch](give-enterprise-agents-tiered-database-memory-with-an-escape-hatch.md)
- [Budget Memory Between Update Cost and Serving Cost](budget-memory-between-update-cost-and-serving-cost.md)
- [Offload Long-Horizon Agent State Outside the Context Window](offload-long-horizon-agent-state-outside-the-context-window.md)
- [Rewrite Agent Memory in a Periodic Batch Pass Over Session Logs](rewrite-agent-memory-in-a-periodic-batch-pass-over-session-logs.md)
- [Institutional Memory Has No Benchmark the Way Graph Memory Does](institutional-memory-has-no-benchmark-the-way-graph-memory-does.md)

Sources:
- [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](../sources/20260812_R3-anFK1YM8.md), 03:36-04:28, 10:02-11:22
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 27:28-28:44
