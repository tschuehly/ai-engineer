# Run Trace Classifiers as Code Mode in a Sandbox

Summary: Code mode — having the model write code instead of emitting structured calls — transplants from tool use to trace analysis. The model writes a classifier, the classifier runs in a sandbox, and the sandbox runs it across the whole production trace corpus. The model touches the question, not the data.

Use when:
- You need an answer about every trace, not a sample, and per-trace LLM scoring is unaffordable.
- A trace question is precise enough to be code ("did the agent call `refund` before confirming the amount?").
- Deciding what to build on top of a trace store beyond search and dashboards.
- Choosing between an agentic trace-mining pass and a deterministic sweep — often the answer is both, in that order.

Details:
- The transplant, stated as a recommendation: "you've heard about code mode in the context of MCPs… I highly recommend just uh trying to apply this to traces. Like you can just write uh these classifiers and you can write them and you can run them in a sandbox and you can run them at production scale." ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 18:14-18:32)
- It is offered as a build-it-yourself pattern, not a product requirement: "we have a feature that makes this easier, but like you can do this." (18:32-18:36)
- Why the economics change. The wiki's cost model for LLM trace mining is multiplicative — input token price × trace count × average trace size ([Mine Trace Corpora With Agents Because They Do Not Fit in Context](mine-trace-corpora-with-agents-because-they-do-not-fit-in-context.md)). A classifier moves the model call from once-per-trace to once-per-question, and the per-trace cost becomes compute rather than tokens. That is the difference between sampling and full coverage.
- Why the context limit stops applying. The same page's harder constraint is capacity: a single long agent session already exceeds the reading model's context window. A classifier never loads the trace into a context window at all; it streams over it.
- What it buys beyond cost: a classifier is a *named, versioned, re-runnable* predicate. Re-running yesterday's classifier over last month's traces yields a comparable time series, which is what makes onset and growth computable ([Triage Agent Issues by Onset and Share of Users](triage-agent-issues-by-onset-and-share-of-users.md)) and what a clustering pass cannot give you ([Clusters Are Not Issues](clusters-are-not-issues.md)).
- The sandbox is load-bearing for the same reasons it is in tool-calling code mode: model-written code that sweeps a production corpus is untrusted code with broad read access. The wiki's existing treatment of sandboxed model-written code applies unchanged ([Run agent-written API code inside programmable sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md), [Sandboxed code execution turns model reasoning into inspectable computation](sandboxed-code-execution-turns-model-reasoning-into-inspectable-computation.md)).
- The division of labor with agentic mining is complementary rather than competitive. Deterministic classifiers answer questions you can already state; agent readers answer the behavioral questions code cannot settle, such as whether users got upset or whether the agent degrades after each compaction ([Ask Traces the Behavioral Questions Code Cannot Answer](ask-traces-the-behavioral-questions-code-cannot-answer.md)). The cheap sweep is also the natural way to surface something for an agent to investigate ([Hand Agents Anomalies to Investigate, Not to Detect](hand-agents-anomalies-to-investigate-not-to-detect.md)).
- Caveat: no numbers accompany the recommendation — no cost comparison, no coverage figure, no example classifier. The mechanism is sound and cheap to try, but this source demonstrates none of it, and the classifier's own accuracy becomes a new thing to validate.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Mine Trace Corpora With Agents Because They Do Not Fit in Context](mine-trace-corpora-with-agents-because-they-do-not-fit-in-context.md)
- [Expose large APIs through typed code mode](expose-large-apis-through-typed-code-mode.md)
- [Use Bash as a composable code-mode tool for agents](use-bash-as-a-composable-code-mode-tool-for-agents.md)
- [Apply Online Scoring to Production Traces With Cost-Aware Sampling](apply-online-scoring-to-production-traces-with-cost-aware-sampling.md)
- [Clusters Are Not Issues](clusters-are-not-issues.md)
- [Hand Agents Anomalies to Investigate, Not to Detect](hand-agents-anomalies-to-investigate-not-to-detect.md)

Sources:
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 18:14-18:36
