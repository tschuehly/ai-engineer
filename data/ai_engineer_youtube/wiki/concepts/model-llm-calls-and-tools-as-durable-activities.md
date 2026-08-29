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
- Colvin argues that Temporal-backed agent support is not very useful unless tool calls are activities too, because agent loops depend on tool use; his demo records both LLM IO and tool calls so failed or killed runs can retry only the unfinished activity, 05:40-06:03, 19:25-20:18.
- Somal's agent architecture maps tools to activities and uses workflow signals and queries for interaction, while keeping the LLM provider interchangeable and letting the workflow layer handle failures, 10:57-11:41.
- **A worked activity list from a go-to-market pipeline.** One Temporal run for a single signal touches "enrichment, web search, draft generation and more," each modeled as a step that can fail or be rate-limited, which lets the team "focus on writing the sequential logic for our GTM use cases" while retries, dedupes, and resume-at-failure are handled by the engine. Dedupe is worth noting alongside retries: when the same customer event can arrive more than once, at-most-once side effects matter as much as recovery. ([Liu](../sources/20260826_L4I7WgiEquo.md), 13:16-13:52)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Enforce deterministic guardrails around sensitive tool calls](enforce-deterministic-guardrails-around-sensitive-tool-calls.md)
- [Move mandatory brittle tool steps outside the agent loop](move-mandatory-brittle-tool-steps-outside-the-agent-loop.md)
- [Emit Owner-Assigned Tasks From Signals, With a Marketing Default When None Fire](emit-owner-assigned-tasks-from-signals-with-a-marketing-default-when-none-fire.md)

Sources:
- [OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal](../sources/20260112_k8cnVCMYmNc.md), 12:46-15:43, 50:05-54:21
- [From Stateless Nightmares to Durable Agents - Samuel Colvin, Pydantic](../sources/20251124_flf_IKnFYnE.md), 05:40-06:03, 19:25-20:18
- [Scaling AI Agents Without Breaking Reliability - Preeti Somal, Temporal](../sources/20250728_1izYWsokr9s.md), 10:57-11:41
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 13:16-13:52
