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

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Ralph loops process one ticket at a time with fresh context](ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md)
- [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [Hackable agent runtimes need tight safety boundaries](hackable-agent-runtimes-need-tight-safety-boundaries.md)

Sources:
- [Building Conversational Agents - Thor Schaeff and Philipp Schmid, Google DeepMind](../sources/20260430_cVzf49yg0D8.md), 14:33-17:09, 32:23-34:58, 42:31-42:46
