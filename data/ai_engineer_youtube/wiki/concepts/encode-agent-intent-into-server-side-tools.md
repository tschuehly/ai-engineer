# Encode Agent Intent Into Server-Side Tools

Summary: A production tool surface can improve reliability by encoding the agent's intended workflow into a server-side tool instead of forcing the model to compose many low-level API calls.

Use when:
- A model repeatedly fails a workflow because it must sequence several service API calls correctly.
- Extra server-side work would reduce agent round trips, context use, latency, or tool-call failure.

Details:
- GitHub found preventable tool failures by studying remote-server usage and encoding more agent intent into the MCP tool surface. (06:43-07:11)
- A robust tool may execute several API calls server-side; doing so can reduce model round trips, save context, save time, and improve agent success. (07:11-07:30)
- Tool descriptions should be evaluated as a set, not only micro-optimized one by one, because a description that causes a tool to be called all the time is as harmful as one that hides the tool when needed. (07:32-08:08)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)

Sources:
- [Scaling GitHub for your Agents — Sam Morrow, GitHub](../sources/20260427_0n3MKk7r60w.md), 06:43-08:08
