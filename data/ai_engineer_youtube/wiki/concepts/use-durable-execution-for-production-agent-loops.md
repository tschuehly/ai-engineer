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
- Somal makes the production framing explicit: agentic AI applications are complex distributed systems that coordinate unreliable LLMs, tool calls, long-lived state, human approvals, parallelism, tracing, and visibility, so reliability belongs in the workflow substrate rather than in ad hoc agent-loop code, 01:14-03:15.
- **A non-engineering workload on the same substrate, where the deciding property is batch isolation.** At Notion "every signal becomes a workflow on Temporal," and a single run touches enrichment, web search, and draft generation — "each of these is a network call that could fail or rate limit" — so the framework handles "the retries, dedupes, and going back to exactly where failures left off." The requirement stated as decisive is per-item isolation: "one malformed transcript can't take down the whole batch," which is what mass-processing customer events demands beyond crash recovery for a single long-running agent. ([Liu](../sources/20260826_L4I7WgiEquo.md), 13:04-13:52)
- **A failure class that makes durability structural rather than nice to have.** In a stack of pre-integrated SaaS tools, the tools sync to each other outside your orchestrator, so "if you create contacts in your CRM, you actually need to wait for that contact to sync to the sequencer before you can then take action on it," which "creates some difficult problems where you actually need to introduce things like [waits] and loops to check if information is ready." A workflow that can suspend, poll, and resume handles this natively; a stateless script has to choose between a fixed sleep and a retry that misdiagnoses a success as a failure. Berry also names constant partial failure as the steady state of the distributed setup — "I also have failures that are happening all the time." ([Berry](../sources/20260826_UhCY231d0FQ.md), 08:08-08:55)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Treat multi-agent systems as distributed systems](treat-multi-agent-systems-as-distributed-systems.md)
- [Wrap agent calls with circuit breakers and compensation](wrap-agent-calls-with-circuit-breakers-and-compensation.md)
- [Agent traces require specialized eval infrastructure](agent-traces-require-specialized-eval-infrastructure.md)
- [Keep workflow orchestration deterministic and put side effects in steps](keep-workflow-orchestration-deterministic-and-put-side-effects-in-steps.md)
- [Emit Owner-Assigned Tasks From Signals, With a Marketing Default When None Fire](emit-owner-assigned-tasks-from-signals-with-a-marketing-default-when-none-fire.md)
- [Own the Context Layer and Rent Every Other Layer](own-the-context-layer-and-rent-every-other-layer.md)
- [Wait for the Background Sync Before Acting on a Record You Just Created](wait-for-the-background-sync-before-acting-on-a-record-you-just-created.md)
- [Treat Tool-to-Tool Orchestration as a Data Engineering Problem](treat-tool-to-tool-orchestration-as-a-data-engineering-problem.md)
- [Build Orchestration From a Few General-Purpose Node Types](build-orchestration-from-a-few-general-purpose-node-types.md)
- [Run One Dormant, Long-Lived Agent Per Account](run-one-dormant-long-lived-agent-per-account.md)

Sources:
- [OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal](../sources/20260112_k8cnVCMYmNc.md), 07:46-11:35, 50:05-51:44
- [Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel](../sources/20260106_kmV-qg4uoNI.md), 12:24-17:23
- [From Stateless Nightmares to Durable Agents - Samuel Colvin, Pydantic](../sources/20251124_flf_IKnFYnE.md), 04:03-04:44, 08:34-10:42
- [Scaling AI Agents Without Breaking Reliability - Preeti Somal, Temporal](../sources/20250728_1izYWsokr9s.md), 01:14-03:15
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 13:04-13:52
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 08:08-08:55
