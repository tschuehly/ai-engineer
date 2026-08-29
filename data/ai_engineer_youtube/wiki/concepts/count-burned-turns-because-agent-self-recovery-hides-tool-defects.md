# Count Burned Turns, Because Agent Self-Recovery Hides Tool Defects

Summary: When an agent guesses a wrong parameter, reads your error message, and retries correctly, the task still passes — so the defect never appears in a success rate. It appears as a wasted turn, extra tokens, and added latency, which is exactly the axis buyers now evaluate tools on. Read traces for recovered failures, not only for failed runs.

Use when:
- Your agent-facing tool passes its evals and you want to know what it still costs.
- Deciding which trace events are worth alerting on when the run completed successfully.
- Writing or auditing tool descriptions and parameter names.

Details:
- **The trace.** On a read tool, "the model had these expectations based off of its biases… from its training data of what it expected for a particular command… And there's nothing in our description that would have led it to believe otherwise. So it tried to use like `read line` instead of `start line`." ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 06:33-07:01)
- **The recovery is the trap.** "It ended up failing, but then at least the error told it why it failed… So it was able to fix itself. But then it's burning right an entire turn just failing. And you could just go in and fix that aspect of like how it's interacting with the tool." A good error message converts a hard failure into a silent tax. Both halves are true and the second is the one teams skip. (07:01-07:20)
- **The metric that makes it visible.** Turns burned on recovered errors, per tool, per parameter. Adjacent framings on the wiki measure the same waste from other directions: [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md) warns that step count can penalize useful verification — so scope this metric to steps that ended in a tool error the agent then corrected, which are unambiguously waste.
- **Why it is a purchasing criterion and not just hygiene.** "It's the way that different organizations are going to be evaluating your tool… in terms of not just is it working well, but like how many tokens is the agent dealing with to work with your tool? And how fast is it?" A tool whose schema fights the model's priors loses on a scoreboard the buyer keeps, not on yours. (07:23-07:38)
- **The fix is usually the description or the name, not the code.** Nothing about the tool's behavior was wrong; the model's expectation came from its training distribution and the description did not contradict it. That makes the repair cheap — name the parameter what the model expects, or state the deviation explicitly in the description. See [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md) and [Match Agent Tooling to the Model's Training Distribution](match-agent-tooling-to-the-models-training-distribution.md), which supplies the general rule this trace is an instance of: the model arrives with habits, and the cheaper move is to satisfy them.
- **Where the signal comes from if you do not run a benchmark.** The agent itself can report it: a self-triggered complaint tool surfaces "unclear tool names, parameters/schemas that don't match expectations" as first-person diagnoses — see [Give Agents a Vent Tool to Report Platform Friction](give-agents-a-vent-tool-to-report-platform-friction.md), whose launch-day example was likewise a defect that logs called a success.
- **Generalization worth stating.** Any tool-side design that the model recovers from — a paginated result the agent must re-request, a required field it learns about from a validation error, a two-call sequence where one would do — has the same shape. The class is "errors the agent absorbs," and its cost is denominated in context window rather than in failures.

Related topics:
- [Tools](../topics/tools.md)
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Benchmark Your Own Tool by Running Agents With and Without It](benchmark-your-tool-by-running-agents-with-and-without-it.md)
- [Match Agent Tooling to the Model's Training Distribution](match-agent-tooling-to-the-models-training-distribution.md)
- [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [Trace agent tool arguments to debug real failures](trace-agent-tool-arguments-to-debug-real-failures.md)
- [Give Agents a Vent Tool to Report Platform Friction](give-agents-a-vent-tool-to-report-platform-friction.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Wrap Generic Tool Descriptions With Use-Case Guidance](wrap-generic-tool-descriptions-with-use-case-guidance.md)

Sources:
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 06:33-07:38
