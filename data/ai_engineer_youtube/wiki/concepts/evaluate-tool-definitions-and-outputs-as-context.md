# Evaluate tool definitions and outputs as context

Summary: Tool definitions and tool outputs are part of the model's context, not only backend API plumbing. Agent evals should inspect whether tool schemas, descriptions, output formats, and token footprint help the model solve the task.

Use when:
- Designing MCP, function-calling, GraphQL, or internal API tools for agents.
- Debugging an agent that has the right system prompt but fails after tool calls or produces weak analysis over tool outputs.

Details:
- Goyal frames modern prompts as system prompts plus iterative LLM calls, tool calls, and tool responses; most context in agent traces can come from tool-related messages rather than the system prompt, 04:27-05:08, 16:21-17:24.
- Tool definitions should be written for what the LLM needs to see, not merely as a direct reflection of existing product APIs, 05:15-05:32.
- Tool output format can matter to the model even when it would not matter to ordinary code consumers. The talk cites an internal case where changing output from JSON to YAML made a significant difference because YAML was more token-efficient and easier for the LLM to analyze, 05:45-06:32.
- The Q&A warns against exposing a GraphQL API as a large set of tool calls without engineering the tool surface for model success, 17:03-17:30.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [MCP tool surfaces need default context budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Encode agent intent into server-side tools](encode-agent-intent-into-server-side-tools.md)

Sources:
- [Five hard earned lessons about Evals - Ankur Goyal, Braintrust](../sources/20250823_a4BV0gGmXgA.md), 04:27-06:32, 16:21-17:30
