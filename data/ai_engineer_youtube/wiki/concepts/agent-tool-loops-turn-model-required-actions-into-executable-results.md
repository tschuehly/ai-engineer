# Agent tool loops turn model-required actions into executable results

Summary: A basic agent loop calls the model with tool definitions, inspects whether the model requires action, executes recognized tool calls, returns tool results, and repeats until the model produces final text.

Use when:
- Implementing a minimal tool-using coding agent or conversational assistant.
- Debugging why a model selected a tool that the runtime cannot execute.

Details:
- The workshop describes agents as a model, tools, context, and a loop: the model decides between text and tool calls, tools provide access to the environment, context constrains behavior, and the loop runs until tool calls stop. 14:33-15:04
- The Interactions API tool path uses a `requires_action` state to tell the client that it must execute a generated function call before the model can continue. 16:42-17:09
- The demo maps tool schemas to executable Python functions for reading files, writing files, and running commands, then checks whether each requested function exists before executing it. 32:23-33:54
- Tool results are returned as function-result events using the same interaction schema, then the run method recurses until the model returns final text instead of another tool call. 33:54-34:23
- The source highlights a safety boundary through the coding-agent demo: writing, reading, and running `date` are acceptable tool actions, while a joking "delete all files" prompt is explicitly rejected rather than executed. 34:39-34:58, 42:31-42:46
- Hruska describes the same ReAct-style production skeleton as an execution loop where the model reads, decides, calls tools, receives tool results, and stops when it reaches a final answer; the loop should have a maximum iteration count so it cannot think forever and burn token budget. 04:10-05:43
- **The loop's control variable is the stop reason, and it is multi-valued.** Coyle presents the same skeleton as a `while True` and makes the branch explicit — the named anti-pattern is "just to let the agent go and do something and get the response back and use it," because the response text does not say why control came back. Tool use is one reason; running out of output tokens is another, and it "is based on partial when the LLM had to stop" while still reading like a finished answer. See [Read the Stop Reason Before You Read the Answer](read-the-stop-reason-before-you-read-the-answer.md). ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 08:03-08:17, 10:50-11:12)
- **Why the loop, specifically, is what changed.** Coyle argues loop-centric agent framing is not novel so much as newly complete: Böhm and Jacopini's 1966 result says Turing completeness needs only sequential statements, if-then conditionals, and a loop, and "up to now we've had sort of sequences. You have prompts, you have maybe if-then, but now we have a loop. And now this is what's giving us the power." That reframes the max-iteration bound above as the same discipline any unbounded loop needs, rather than an LLM-specific safeguard. ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 06:32-07:48)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Ralph loops process one ticket at a time with fresh context](ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md)
- [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [Hackable agent runtimes need tight safety boundaries](hackable-agent-runtimes-need-tight-safety-boundaries.md)
- [Read the Stop Reason Before You Read the Answer](read-the-stop-reason-before-you-read-the-answer.md)

Sources:
- [Building Conversational Agents - Thor Schaeff and Philipp Schmid, Google DeepMind](../sources/20260430_cVzf49yg0D8.md), 14:33-17:09, 32:23-34:58, 42:31-42:46
- [How agents will unlock the $500B promise of AI - Donald Hruska, Retool](../sources/20250723_Lqq_LcBaJCc.md), 04:10-05:43
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](../sources/20260808_Z-c11pV_uvU.md), 06:32-07:48, 08:03-08:17, 10:50-11:12
