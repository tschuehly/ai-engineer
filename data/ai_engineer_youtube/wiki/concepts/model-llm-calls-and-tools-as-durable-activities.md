# Model LLM Calls and Tools as Durable Activities

Summary: External calls in an agent loop can be modeled as durable activities so retries, timeouts, persistence, and tool execution are handled by workflow infrastructure rather than bespoke control-flow code.

Use when:
- Wrapping LLM calls, MCP tools, or downstream API calls inside a production workflow.
- Choosing where retry policy and timeout behavior should live for agent tool use.

Details:
- Temporal activities are described as chunks of work, especially heavy work or external calls, that can receive special SDK behavior through activity decorators, 12:46-14:15.
- Workflows orchestrate activities into business logic; retry policies can specify exponential backoff, retry limits, and retry windows while the workflow invokes the activities normally, 14:15-15:43.
- The demo implements agent tools as activities and passes them into an OpenAI Agents SDK agent, so tool calls and the agent loop share the workflow's durability guarantees, 50:05-51:23.
- The talk notes that the LLM call itself should also be wrapped as an activity so rate limits and retries are handled durably, 53:22-54:21.

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Enforce deterministic guardrails around sensitive tool calls](enforce-deterministic-guardrails-around-sensitive-tool-calls.md)
- [Move mandatory brittle tool steps outside the agent loop](move-mandatory-brittle-tool-steps-outside-the-agent-loop.md)

Sources:
- [OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal](../sources/20260112_k8cnVCMYmNc.md), 12:46-15:43, 50:05-54:21
