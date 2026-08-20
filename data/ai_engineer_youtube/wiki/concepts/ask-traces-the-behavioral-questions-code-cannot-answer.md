# Ask Traces the Behavioral Questions Code Cannot Answer

Summary: Trace mining pays off when you bring specific questions to it, and the highest-value questions are exactly the ones no amount of code reading can settle — where users got upset, whether the agent degrades after each compaction, and what a different model would have done at the same step.

Use when:
- You have tracing on and want a starting question list rather than a dashboard.
- A design debate is stuck on what the agent "probably" does under some condition.
- Deciding whether a claimed context-management or model change is worth shipping.

Details:
- Setup first: centralize traces into a tracing project, "either like per agent or like centralized across all of our agents," then "send agents to read traces from other agents." ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 04:40-05:09)
- **Sentiment and outcome mining.** "Find a bunch of like good and bad interactions where like users got upset or like users are like really happy." This is the question that turns raw volume into a triage queue. ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 05:09-05:16)
- **Degradation across compactions.** "Agents now run for millions of tokens. Does the agent get really dumb after the first compaction? After the second compaction? Does it never get dumb? Like how do we actually answer these questions? We need to do it by actually looking at the traces." This is the sharpest instance of the general rule: the answer is deployment-specific, it changes with every model and prompt revision, and it is unreadable from the harness source. ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 05:16-05:32)
- **Counterfactual model swaps.** "I ran GPT 5.5 for this and I heard like GLM is really good. What happens if I run GLM 5.2 for this task and how do I compare them?" The trace is the substrate that makes the comparison concrete because "the trace level captures the actual behavior that users see," which is what makes it useful "for seeing behavior at fine grain scales." ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 05:32-05:57)
- Why these questions have no code-level answer: agents are assembled from prompts, tools, skills, hooks, middlewares, and other agents orchestrated in swarms, so a human cannot predict how a prompt change propagates at scale, and the same change lands differently in the medical and legal domains. ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 03:31-04:19)
- Practical note on the compaction question: the wiki carries opposing published findings on whether compaction helps or hurts — a quality argument for frequent intentional compaction in reviewed coding sessions, and a benchmark where untouched full history beat every compaction preset on recall, cost, and latency at once ([Frequent intentional compaction keeps coding agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md), [Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md)). That disagreement is precisely why the question belongs in your own trace corpus rather than in a citation.
- **The boundary condition, from a talk at the same event: this list is what to ask an agent, not what to ask it to find.** Ben Hylak's rule is that "agents are very, very bad at anomaly detection. So don't ask your agent to find anomalies. Uh ask it to investigate anomalies you've already found" — surface something deterministic first, "like keyword frequency," and hand the agent that object ([Hand Agents Anomalies to Investigate, Not to Detect](hand-agents-anomalies-to-investigate-not-to-detect.md)). The two pages are compatible and the split is by question type: every question on this list is a *bounded interpretive* question about a named slice, which is the shape agents handle. "What is unusual in here" is a statistical question over a full population with a baseline, which is not. Note that Hylak asserts this with no evidence — no model, task, or baseline named. ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 18:38-19:05)
- Turning an answer into an artifact is a separate step the wiki documents in detail: cluster the failures, validate the clusters with a human, then promote each validated cluster into the golden dataset so it becomes a regression test ([Promote Validated Live-Trace Failure Clusters Into the Golden Dataset](promote-validated-live-trace-failure-clusters-into-the-golden-dataset.md)).

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Observability and Continual Learning Are the Same Problem](observability-and-continual-learning-are-the-same-problem.md)
- [Mine Trace Corpora With Agents Because They Do Not Fit in Context](mine-trace-corpora-with-agents-because-they-do-not-fit-in-context.md)
- [Frequent intentional compaction keeps coding agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md)
- [Promote Validated Live-Trace Failure Clusters Into the Golden Dataset](promote-validated-live-trace-failure-clusters-into-the-golden-dataset.md)
- [Trace agent tool arguments to debug real failures](trace-agent-tool-arguments-to-debug-real-failures.md)
- [Turn Recorded Agent Traces Into Free Replay Test Cases](turn-recorded-agent-traces-into-free-replay-test-cases.md)
- [Hand Agents Anomalies to Investigate, Not to Detect](hand-agents-anomalies-to-investigate-not-to-detect.md)
- [Run Trace Classifiers as Code Mode in a Sandbox](run-trace-classifiers-as-code-mode-in-a-sandbox.md)

Sources:
- [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../sources/20260812_CvRngaQZQ3Y.md), 03:31-05:57
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 18:38-19:05
