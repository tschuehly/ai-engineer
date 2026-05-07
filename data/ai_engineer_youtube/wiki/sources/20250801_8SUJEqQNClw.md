# Agents vs Workflows: Why Not Both? - Sam Bhagwat, Mastra.ai

Source: [Agents vs Workflows: Why Not Both? - Sam Bhagwat, Mastra.ai](https://www.youtube.com/watch?v=8SUJEqQNClw)
Uploaded: 2025-08-01
Transcript: `raw/20250801_8SUJEqQNClw/8SUJEqQNClw.en-orig.vtt`

## Summary

Sam Bhagwat argues that agents and workflows should be treated as composable primitives rather than competing top-level ideologies. Agents provide flexible turn-based exploration and tool use; workflows provide readable control flow, dependency tracking, traceability, suspend/resume behavior, and reliability around nondeterministic LLM calls.

## Extracted Concepts

- [Compose agents and workflows as interchangeable primitives](../concepts/compose-agents-and-workflows-as-interchangeable-primitives.md) - supports using agents as workflow steps, workflows as agent tools, and agents as callable tools.
- [Prefer readable workflow APIs over graph-theory surfaces](../concepts/prefer-readable-workflow-apis-over-graph-theory-surfaces.md) - supports keeping workflow control flow readable to ordinary team members.
- [Add structure where agent reliability fails](../concepts/add-structure-where-agent-reliability-fails.md) - supports decomposing unreliable LLM calls into more structured agent or workflow steps.

## Topic Links

- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Tools](../topics/tools.md)

## Notes

- The talk rejects an agents-versus-workflows framing and says useful systems often combine the primitives rather than choosing one dogmatic abstraction. (10:05-12:07)
- Agents are framed as turn-based interaction loops with humans, tool calls, and repeated model turns, while workflows are framed as dependency-aware rules engines or data pipelines. (08:03-09:22)
- Workflow frameworks should make control flow readable; requiring node/edge graph-theory thinking can hurt team comprehension even when the underlying workflow has graph-like semantics. (03:40-06:02)
- Workflows are especially valuable in AI engineering because nondeterminism makes traceability and post-hoc debugging more important than in ordinary deterministic code paths. (09:25-10:01)
- A practical debugging move is to identify the unreliable part of an agent application and add structure there, such as splitting one broad medical-documentation LLM call into separate symptom-specific calls. (10:30-11:15)
- Composition patterns include agents as workflow steps, workflows as agent tools, agents as tools, workflow steps that call workflows, supervisor agents that call other agents, dynamic tool injection, nested workflows, and workflow-mediated agent handoffs. (11:46-13:53)
