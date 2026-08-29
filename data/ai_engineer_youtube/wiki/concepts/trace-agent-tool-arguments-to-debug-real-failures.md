# Trace Agent Tool Arguments to Debug Real Failures

Summary: Agent traces should expose the exact tool calls, arguments, model exchanges, latency, and cost behind a run so failures can be diagnosed from observed behavior rather than guessed from the final answer.

Use when:
- Debugging why a tool-using agent produced a wrong or failed result.
- Deciding what observability data an agent framework or application should capture.

Details:
- Colvin instruments Pydantic AI examples with Logfire so the team can inspect each agent run, model call, tool call, tool response, and validation retry. 05:49-06:43
- In the memory-tool demo, the first run failed because the model called `retrieve_memory` with "your name", which did not match the simplistic substring lookup over the stored memory; the trace made the bad argument visible. 10:19-11:15
- The follow-up run succeeded when the model used "name" as the retrieval argument, which matched the stored sentence and returned the expected memory. 11:23-11:36
- The trace also showed per-call timing and pricing at both aggregate and span levels, connecting behavioral debugging with cost and latency analysis. 11:39-11:49
- Witan Labs reinforces the diagnostic value of reading traces: infrastructure bugs "many times end up looking like reasoning failures," and it "may seem like the model is doing something wrong" when really the model is doing the right thing given a broken environment. ([Witan Labs](../sources/20260708_HEFSExa0xl0.md), 15:08-15:27)
- Three recurring bug-not-reasoning patterns to look for in the trace: a plain bug in the code; a wrong example in the skill/prompt that the model "is following very faithfully"; or a failing tool that the model "keeps retrying" around so it "seems like the model is being dumb" when it is just working around the issue — so "always check your traces and your plumbing, because sometimes agent confusion is just bugs and you should fix that." ([Witan Labs](../sources/20260708_HEFSExa0xl0.md), 15:27-16:02, 18:38-18:47)
- **Arguments can also be designed into the schema for the log, not only read out of it.** Figma added optional query arguments to tools such as `get design context` purely so the agent would report the user's language and framework — a field with no behavioural effect whose only consumer is the server's own analytics. That makes the tool signature a telemetry surface, which is a different act from this page's: here the argument is evidence the model produced for its own reasons, there it is evidence the server asked for. The two coexist in one trace, but only the second changes the interface, and it charges the context budget on every handshake to do so. ([Lumarie](../sources/20260828_ZIYYsAzaLlA.md), 12:45-13:09)
- **Read the argument traces of runs that succeeded, not only of runs that failed.** The Pydantic example above is diagnosed because the run failed. Jarmak's case is the one that never reaches a bug queue: the model called a read tool with `read line` instead of `start line`, "and there's nothing in our description that would have led it to believe otherwise," then recovered from the error message and completed the task. The wrong argument is visible in the trace and invisible in every outcome metric, so the query worth running over a trace corpus is "which tool calls errored and were then retried with a corrected argument," grouped by tool and parameter. See [Count Burned Turns, Because Agent Self-Recovery Hides Tool Defects](count-burned-turns-because-agent-self-recovery-hides-tool-defects.md). ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 06:33-07:20)

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Connect Production Observability to Offline Eval Loops](connect-production-observability-to-offline-eval-loops.md)
- [Trace Agent Tool Use To Improve Prompts And Tools](trace-agent-tool-use-to-improve-prompts-and-tools.md)
- [Agent Traces Require Specialized Eval Infrastructure](agent-traces-require-specialized-eval-infrastructure.md)
- [Optional Self-Reported Tool Arguments Are Segmentation Signal, Not Ground Truth](optional-self-reported-tool-arguments-are-segmentation-signal.md)
- [Count Burned Turns, Because Agent Self-Recovery Hides Tool Defects](count-burned-turns-because-agent-self-recovery-hides-tool-defects.md)

Sources:
- [Human seeded Evals - Samuel Colvin, Pydantic](../sources/20250725_o_LRtAomJCs.md), 05:49-06:43, 10:19-11:49
- [Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs](../sources/20260708_HEFSExa0xl0.md), 15:08-16:02
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 12:45-13:09
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 06:33-07:20
