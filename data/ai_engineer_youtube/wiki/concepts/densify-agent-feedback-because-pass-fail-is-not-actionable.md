# Densify Agent Feedback Because Pass/Fail Is Not Actionable

Summary: A benchmark that returns one bit tells an agent that it failed but nothing about what to change, so the highest-leverage improvement to a feedback loop is usually densifying the signal — and the trace of the run already contains that dense signal, unused.

Use when:
- An agent has an eval or benchmark score but no path from a failure to a fix.
- Designing rewards or scorers for a long, multi-step task.
- Deciding whether to invest in richer scoring versus more tasks.

Details:
- The failure stated plainly: "like terminal bench, the output is just a number, right? Like, did you pass or did you not pass? That's like kind of helpful, but if I give you like a super random task, like you just did a bunch of stuff, and then I just said like you failed or you passed — if you failed, like you wouldn't really have a good signal to figure out what you should do next." ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 15:21-15:44)
- The prescription and where the dense signal comes from: "densifying feedback is a really good way to improve agents, and like traces are the substrate that hold that feedback. And then agents are very good at reading those traces and then figuring out like what to do next." Nothing new needs to be measured; the record already contains the intermediate steps that the terminal score collapsed. ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 15:44-15:58)
- This makes densification a *read-path* problem rather than a scorer-design problem: the loop that pays is do something → read the results → read the traces → do an update, which he describes as "pretty useful" and which is the same loop behind auto-research agents that read their own traces, propose experiments, and try fixes. ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 14:51-15:21)
- Consistent with the wiki's existing narrower result on long-horizon code work: end-to-end correctness gives one bit, which is too sparse for multi-hour tasks, and intermediate progress measures (fraction translated, fraction refactored) reveal direction before completion ([Use intermediate progress signals for long-horizon code evals](use-intermediate-progress-signals-for-long-horizon-code-evals.md)). This generalizes that observation past code and names the trace as the free source of density.
- Tension worth holding: the wiki also argues for simple, debuggable scores and for narrow binary judge metrics ([Prefer simple debuggable eval scores](prefer-simple-debuggable-eval-scores.md), [Split LLM judges into narrow binary metrics](split-llm-judges-into-narrow-binary-metrics.md)). These are not in conflict once you separate the two roles: a score that a human ranks systems by should stay simple and binary, while the feedback an agent acts on should be dense. Densification means adding a diagnostic channel alongside the score, not replacing the score with a fuzzy one.
- The complementary discipline: decomposing an eval into rubrics targets the specific failing behavior, which is another route to density that keeps each component interpretable ([Decompose evals into rubrics to target the failing behavior](decompose-evals-into-rubrics-to-target-the-failing-behavior.md)).

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Use intermediate progress signals for long-horizon code evals](use-intermediate-progress-signals-for-long-horizon-code-evals.md)
- [Decompose evals into rubrics to target the failing behavior](decompose-evals-into-rubrics-to-target-the-failing-behavior.md)
- [Prefer simple debuggable eval scores](prefer-simple-debuggable-eval-scores.md)
- [Close the eval-to-action loop so signal survives the dashboard](close-the-eval-to-action-loop-so-signal-survives-the-dashboard.md)
- [Observability and Continual Learning Are the Same Problem](observability-and-continual-learning-are-the-same-problem.md)
- [An Agent's Eval Suite Describes Its Behavior](an-agents-eval-suite-describes-its-behavior.md)

Sources:
- [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../sources/20260812_CvRngaQZQ3Y.md), 14:51-15:58
