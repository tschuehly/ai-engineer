# Use Durable Execution for Production Agent Loops

Summary: Production agent loops should be treated as durable distributed workflows, not as single-process scripts. Persisting completed LLM calls, tool outputs, and workflow state lets agents resume after crashes, rate limits, or downstream outages without repeating expensive or side-effecting work.

Use when:
- Designing an agent that may run for many turns, call external APIs, or survive process restarts.
- Deciding whether a demo agent loop is ready for production infrastructure.

Details:
- Temporal is framed as a distributed-systems backing service for AI agents: developers write the happy-path logic while durability handles crashes, rate limits, downstream API failures, and retries, 07:46-10:18.
- Durable execution records completed LLM calls and returns, so a crash on a later turn can resume without re-burning the earlier token spend, 10:53-11:35.
- A plain Agents SDK loop running only as a Python process loses its in-flight state when the process is killed; placing the agent inside a workflow adds durability around the loop and its tools, 50:05-51:44.

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Treat multi-agent systems as distributed systems](treat-multi-agent-systems-as-distributed-systems.md)
- [Wrap agent calls with circuit breakers and compensation](wrap-agent-calls-with-circuit-breakers-and-compensation.md)
- [Agent traces require specialized eval infrastructure](agent-traces-require-specialized-eval-infrastructure.md)

Sources:
- [OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal](../sources/20260112_k8cnVCMYmNc.md), 07:46-11:35, 50:05-51:44
