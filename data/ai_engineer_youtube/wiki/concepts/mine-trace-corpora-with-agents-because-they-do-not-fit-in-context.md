# Mine Trace Corpora With Agents Because They Do Not Fit in Context

Summary: Two independent constraints stop you from just feeding traces to a model — the cost is multiplicative (input token price × number of traces × average trace size) and a single long agent session already exceeds the reading agent's context window — so the trace has to be treated as an external object that a mining agent queries into rather than as a payload you load.

Use when:
- Planning to "have an LLM read our traces" and sizing what that costs.
- A single coding-agent or deep-agent session is too large to hand to another model.
- Designing the read path of a trace store, not just its write path.

Details:
- The cost model is arithmetic you can do before you build anything: "think of it as like an input token cost. You can like literally multiply the input token cost times the number of traces times like how big each trace is on average." The regime where this bites is millions of traces at millions of tokens per trace. ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 06:35-07:03)
- The capacity constraint is the harder one and is not fixed by a bigger budget: "if I have a super long interaction with a coding agent like Claude Code or Codex or like deep agents, I can't even read that trace with another agent because that context like doesn't fit in memory." ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 07:03-07:17)
- The response inverts the data flow: "we need to develop systems so I can sort of treat that context as like an external object and then I can sort of query into it… we need to build agents to efficiently mine data from other agents and it's no longer as simple as just feeding the data into context." ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 07:17-07:36)
- Consequence for tooling: the mining product LangChain built around this reads the corpus, finds issues, "agentically searches over it," and prepares datasets — a search agent over trace storage, not a summarization pass. ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 10:39-11:08)
- The problem gets worse monotonically. "The data that we see today is going to be the smallest that humans have ever seen in their entire lives," as agent runtimes stretch from year scales to 6-month, 3-month, and daily cadences. A read path that only works at today's corpus size is a read path with an expiry date. ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 05:59-06:35)
- This is the read-side counterpart to the storage-side constraint: agent traces are text-heavy, semi-structured, large, and high-velocity, which already breaks naive relational storage ([Agent traces require specialized eval infrastructure](agent-traces-require-specialized-eval-infrastructure.md)). Both sides have to hold, and neither implies the other.
- **A fourth lever attacks the same arithmetic from a different angle: move the model call from once-per-trace to once-per-question.** Ben Hylak's version is to transplant code mode from MCP tool calling onto traces — "you can just write uh these classifiers and you can run them in a sandbox and you can run them at production scale" — so the corpus is swept by deterministic code the model wrote, and neither the token term nor the context-window constraint applies at all ([Run Trace Classifiers as Code Mode in a Sandbox](run-trace-classifiers-as-code-mode-in-a-sandbox.md)). This does not replace agentic mining; it partitions the work. Questions you can already state become cheap full-coverage sweeps, and the agent reader is reserved for the behavioral questions no classifier can express. ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 18:14-18:36)
- Cost control the wiki records elsewhere applies here too and is complementary rather than alternative: sample rather than score everything ([Apply online scoring to production traces with cost-aware sampling](apply-online-scoring-to-production-traces-with-cost-aware-sampling.md)), and use a cheaper model for the bulk judging pass ([Read the Frontier Model's Traces to Harness-Engineer Its Cheap Replacement](read-frontier-traces-to-harness-engineer-a-cheap-replacement.md)). Sampling reduces the trace count; a cheaper judge reduces the price term; agentic querying reduces the per-trace token term.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Agent traces require specialized eval infrastructure](agent-traces-require-specialized-eval-infrastructure.md)
- [Apply online scoring to production traces with cost-aware sampling](apply-online-scoring-to-production-traces-with-cost-aware-sampling.md)
- [Observability and Continual Learning Are the Same Problem](observability-and-continual-learning-are-the-same-problem.md)
- [Ask Traces the Behavioral Questions Code Cannot Answer](ask-traces-the-behavioral-questions-code-cannot-answer.md)
- [Use subagents to isolate context-heavy subtasks](use-subagents-to-isolate-context-heavy-subtasks.md)
- [Run Trace Classifiers as Code Mode in a Sandbox](run-trace-classifiers-as-code-mode-in-a-sandbox.md)

Sources:
- [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../sources/20260812_CvRngaQZQ3Y.md), 05:59-07:36, 10:39-11:08
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 18:14-18:36
