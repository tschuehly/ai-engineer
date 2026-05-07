# Use Durable Execution for Production Agent Loops

Summary: Production agent loops should be treated as durable distributed workflows, not as single-process scripts. Persisting completed LLM calls, tool outputs, and workflow state lets agents resume after crashes, rate limits, or downstream outages without repeating expensive or side-effecting work.

Use when:
- Designing an agent that may run for many turns, call external APIs, or survive process restarts.
- Deciding whether a demo agent loop is ready for production infrastructure.

Details:
- Temporal is framed as a distributed-systems backing service for AI agents: developers write the happy-path logic while durability handles crashes, rate limits, downstream API failures, and retries, 07:46-10:18.
- Durable execution records completed LLM calls and returns, so a crash on a later turn can resume without re-burning the earlier token spend, 10:53-11:35.
- A plain Agents SDK loop running only as a Python process loses its in-flight state when the process is killed; placing the agent inside a workflow adds durability around the loop and its tools, 50:05-51:44.
- Workflow DevKit applies the same production shape to TypeScript AI SDK agents: move the agent call into a workflow, mark LLM and tool calls as steps, and let successful step inputs and outputs be cached for recovery, 12:24-17:23.
- PydanticAI's Temporal integration shows the same pattern in Python: wrap ordinary agents in Temporal-backed agents, keep the agent-facing code largely intact, and let workflow replay recover completed calls after a Kubernetes-style process kill, 04:03-04:44, 08:34-10:42.

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Treat multi-agent systems as distributed systems](treat-multi-agent-systems-as-distributed-systems.md)
- [Wrap agent calls with circuit breakers and compensation](wrap-agent-calls-with-circuit-breakers-and-compensation.md)
- [Agent traces require specialized eval infrastructure](agent-traces-require-specialized-eval-infrastructure.md)
- [Keep workflow orchestration deterministic and put side effects in steps](keep-workflow-orchestration-deterministic-and-put-side-effects-in-steps.md)

Sources:
- [OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal](../sources/20260112_k8cnVCMYmNc.md), 07:46-11:35, 50:05-51:44
- [Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel](../sources/20260106_kmV-qg4uoNI.md), 12:24-17:23
- [From Stateless Nightmares to Durable Agents - Samuel Colvin, Pydantic](../sources/20251124_flf_IKnFYnE.md), 04:03-04:44, 08:34-10:42
