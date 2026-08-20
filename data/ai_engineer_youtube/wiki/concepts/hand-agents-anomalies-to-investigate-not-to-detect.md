# Hand Agents Anomalies to Investigate, Not to Detect

Summary: Detection and investigation are different jobs and agents are only good at one of them. Find the anomaly with something deterministic and cheap — a keyword frequency spike, a rate change — then hand that concrete object to an agent to explain. Asking an agent to go find what is unusual inverts the split.

Use when:
- Designing an "AI monitors your AI" loop and deciding what the model is actually for.
- An agent asked to "find anything unusual in these traces" returns plausible, unreproducible findings.
- Building the first automated layer on top of a trace store with a small budget.
- Reviewing a vendor claim that an agent surfaces issues autonomously.

Details:
- The rule, stated directly: "agents are very, very bad at anomaly detection. So don't ask your agent to find anomalies. Uh ask it to investigate anomalies you've already found." ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 18:38-18:46)
- The mechanism for the detection half: "pull out as many deterministic things as you can like keyword frequency." (18:48-18:52)
- The detector is allowed to be wrong, and that is the design. "If you see a spike in like a keyword it doesn't necessarily mean that there's an issue, but it does mean that… it's like something more tangible tractable that you can have an agent actually investigate." The detector's job is not to be right; it is to produce a bounded, checkable object with a timestamp and a population attached. (18:52-19:05)
- Why the split works: an anomaly is defined against a baseline over a full population, which is a statistical operation over data no context window holds. An investigation is a bounded question about a specific slice, which is exactly the shape a model handles well. This is the same constraint that forces trace mining to be agentic rather than context-loaded ([Mine Trace Corpora With Agents Because They Do Not Fit in Context](mine-trace-corpora-with-agents-because-they-do-not-fit-in-context.md)) — but it cuts the other way for detection, because sampling a corpus destroys the very rate information a detector needs.
- The failure mode being avoided is not hallucination but unfalsifiability: an agent asked to find anomalies will always find some, with no baseline to check them against and no way to tell whether the same "anomaly" was present last week.
- Deterministic detection composes directly with the two triage numbers, since a keyword-frequency series carries onset and share for free ([Triage Agent Issues by Onset and Share of Users](triage-agent-issues-by-onset-and-share-of-users.md)). A model-generated finding carries neither.
- The natural detector layer is a code-mode sweep over the whole corpus rather than a hand-written metric list ([Run Trace Classifiers as Code Mode in a Sandbox](run-trace-classifiers-as-code-mode-in-a-sandbox.md)) — the model still writes the detector; it just does not *be* the detector.
- Read against the wiki's agentic trace-mining page, the two are compatible and the boundary is the question type: an agent should be sent to answer "where did users get upset" or "does the agent degrade after the second compaction," which have no code-level answer ([Ask Traces the Behavioral Questions Code Cannot Answer](ask-traces-the-behavioral-questions-code-cannot-answer.md)), and should not be sent to answer "what changed."
- Caveat, and it is a real one: the claim is asserted with no evidence at all. No model is named, no task is described, no baseline is measured, and no alternative is compared. It is cheap to adopt and cheap to test against your own corpus, but nothing here establishes it.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Run Trace Classifiers as Code Mode in a Sandbox](run-trace-classifiers-as-code-mode-in-a-sandbox.md)
- [Ask Traces the Behavioral Questions Code Cannot Answer](ask-traces-the-behavioral-questions-code-cannot-answer.md)
- [Triage Agent Issues by Onset and Share of Users](triage-agent-issues-by-onset-and-share-of-users.md)
- [Mine Trace Corpora With Agents Because They Do Not Fit in Context](mine-trace-corpora-with-agents-because-they-do-not-fit-in-context.md)
- [Observability to PR Agents Turn Incidents Into Reviewable Fixes](observability-to-pr-agents-turn-incidents-into-reviewable-fixes.md)

Sources:
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 18:38-19:05
