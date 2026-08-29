# Measure a Context Layer on Compounding, Not on the First Task

Summary: A/B-ing one short task with and without a context layer measures the wrong thing. The cost of missing context is not the extra searching on step one — it is that the agent discovers the *wrong* things, carries them into a plan, and loops back later on bad assumptions. The metric that matters is rework across a multi-step run, and it is the metric almost nobody reports, including the vendors making the argument.

Use when:
- Building the business case for a context engine, code index, or retrieval layer and reaching for a token-cost comparison.
- Reviewing a vendor demo that shows a cheaper single task.
- Designing an eval harness for context infrastructure rather than for model quality.
- Deciding whether an unimpressive first-task delta is a reason not to adopt.

Details:
- The argument, stated by the vendor against his own headline number: the agent without context "has to look around, has to discover things. And this compounds — not only does it have to do more work to discover things, it doesn't discover the right things. So when you get further down in your execution, it may be operating on the wrong plan or the wrong assumptions. And then you have to go back and you have to loop over and over again. So the real value of a context engine is not like the upfront cost on these short tasks. It's the compounding effect." ([Werry](../sources/20260827_qdAkxLoYNI8.md), 11:52-12:27)
- The numbers actually shown, which are the first-task metric he just discounted: generating the same optimization plan in Claude Code cost "sub-dollar" and "about a minute" with the context engine, against "about 2 minutes" and more cost without. (11:13-11:52)
- Read those numbers with the speaker's own caveat, delivered mid-sentence: "Ignore the wall clock time because I've had this open for about an hour." The timing figures come off the same panel he tells the audience not to trust for wall clock. (11:24-11:30)
- What the comparison does not control: one task, one repository, one run per arm, no token counts, no statement of what was in each context, and no rubric establishing that the two plans were equally correct — the no-engine plan is graded "great… but maybe could do a little bit better" by the person selling the engine. (09:55-11:13)
- So the transferable content is the metric definition, not the result. A compounding measurement needs a task long enough to have a mid-course correction in it, and an outcome variable that counts corrections: re-planning events, discarded work, turns spent recovering from a wrong assumption, or tasks abandoned. First-task token cost is a proxy that can move in the wrong direction — a context layer that injects more tokens up front should *lose* on step one and win on step five.
- The harness the same talk offers is the right shape even though the evidence is not: a "context engine simulator" that "will build up a context behind the scenes on a per-task basis and then use that context to drive the task. It'll do it with context and without context so that you can see what the differences might be." A paired-run harness on your own tasks is the artifact to demand from any context vendor. (16:44-17:26)
- Pair it with a do-nothing control and, where feasible, an oracle arm. The control is what tells you the whole category is a loss when it is; the oracle bounds what any amount of context could deliver. See [Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md) and [An Oracle Ceiling Separates Retrieval Failure From Use Failure](an-oracle-ceiling-separates-retrieval-failure-from-use-failure.md).
- The independently-measured counterexample that keeps this page honest: a context intervention is not free by construction. When a task's corpus already fits in the window, a memory harness produced "the same performance with memory and without memory, and it only added more cost." Compounding is a hypothesis about long-horizon tasks, not a guarantee about all tasks. See [A Memory Harness Adds Only Cost When the Task Fits in Context](a-memory-harness-adds-only-cost-when-the-task-fits-in-context.md).
- The closing customer quote — "50% fewer tokens, faster triage, better answers" — arrives with no methodology, baseline, or workload and should be treated as marketing rather than evidence. (17:35-17:45)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Context Engineering](../topics/context-engineering.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md)
- [An Oracle Ceiling Separates Retrieval Failure From Use Failure](an-oracle-ceiling-separates-retrieval-failure-from-use-failure.md)
- [A Memory Harness Adds Only Cost When the Task Fits in Context](a-memory-harness-adds-only-cost-when-the-task-fits-in-context.md)
- [Evaluate retrieval and MCP layers by task value, not only response availability](evaluate-retrieval-and-mcp-layers-by-task-value.md)
- [Satisfaction of Search Stops Agents at the First Plausible Hit](satisfaction-of-search-stops-agents-at-the-first-plausible-hit.md)
- [An Agent Is an Expert Who Onboards Again on Every Task](an-agent-is-an-expert-who-onboards-again-on-every-task.md)

Sources:
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 09:55-12:27, 16:44-17:45
