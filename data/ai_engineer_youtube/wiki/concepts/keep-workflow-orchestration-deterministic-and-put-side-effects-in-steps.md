# Keep Workflow Orchestration Deterministic and Put Side Effects in Steps

Summary: Durable agent workflows should keep the orchestration layer deterministic and move side-effecting work into explicit steps. This lets the workflow rerun for recovery without duplicating LLM calls, tool calls, external API effects, or state pollution.

Use when:
- Wrapping a TypeScript or serverless agent loop in a durable workflow engine.
- Deciding whether logic belongs in orchestration code or in a step/activity boundary.

Details:
- Workflow DevKit compiles workflow-related code into a separate bundle and blocks imports that would create side effects, because the orchestration layer must be rerunnable deterministically, 12:24-12:45.
- LLM calls and agent tool calls should be marked as steps; in the demo, a durable agent class adds a step marker around the AI SDK agent's underlying LLM calls, 12:45-13:17.
- Step inputs and outputs can be cached after a successful run and failed steps can be retried, so production recovery does not require re-running every prior part of the agent loop, 16:10-16:26.
- Temporal's Python model draws the same line: workflow code must be deterministic, while IO and other non-deterministic work belong in activities whose inputs and outputs are recorded for replay, 04:47-05:36.
- **A production orchestrator that keeps the model inside a node rather than around it.** Clay's graph is five general-purpose node types — "nodes that run agents, nodes that make tool calls, nodes that handle our conditional logic, nodes that run code, and then nodes that run effectively this map reduce system to fan out the information and bring it back" — which puts conditionals and code outside the agent's discretion by construction. The agent is one step type in a deterministic shell, not the shell. Berry presents it as vendor-neutral: "whether you buy it or build it, I think this is like fundamentally the modern way to set this up." ([Berry](../sources/20260826_UhCY231d0FQ.md), 08:55-09:32)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use durable execution for production agent loops](use-durable-execution-for-production-agent-loops.md)
- [Model LLM calls and tools as durable activities](model-llm-calls-and-tools-as-durable-activities.md)
- [Treat multi-agent systems as distributed systems](treat-multi-agent-systems-as-distributed-systems.md)
- [Build Orchestration From a Few General-Purpose Node Types](build-orchestration-from-a-few-general-purpose-node-types.md)
- [Wait for the Background Sync Before Acting on a Record You Just Created](wait-for-the-background-sync-before-acting-on-a-record-you-just-created.md)

Sources:
- [Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel](../sources/20260106_kmV-qg4uoNI.md), 12:24-13:17, 16:10-16:26
- [From Stateless Nightmares to Durable Agents - Samuel Colvin, Pydantic](../sources/20251124_flf_IKnFYnE.md), 04:47-05:36
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 08:55-09:32
