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

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Connect Production Observability to Offline Eval Loops](connect-production-observability-to-offline-eval-loops.md)
- [Trace Agent Tool Use To Improve Prompts And Tools](trace-agent-tool-use-to-improve-prompts-and-tools.md)
- [Agent Traces Require Specialized Eval Infrastructure](agent-traces-require-specialized-eval-infrastructure.md)

Sources:
- [Human seeded Evals - Samuel Colvin, Pydantic](../sources/20250725_o_LRtAomJCs.md), 05:49-06:43, 10:19-11:49
- [Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs](../sources/20260708_HEFSExa0xl0.md), 15:08-16:02
