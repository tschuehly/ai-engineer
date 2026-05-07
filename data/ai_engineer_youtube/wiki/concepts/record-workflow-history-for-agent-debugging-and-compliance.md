# Record Workflow History for Agent Debugging and Compliance

Summary: Production agent workflows should preserve an inspectable execution history. A durable workflow history gives teams evidence for debugging, test/dev replay, observability, and compliance instead of leaving agent behavior as an opaque sequence of transient model and tool calls.

Use when:
- Designing traceability for long-running agents that call tools, wait for humans, or branch through multiple steps.
- Deciding what operational evidence to retain for agent audits, debugging, or regulated workflows.

Details:
- Somal says complex agent systems are difficult to debug and test because visibility into what is happening across LLMs, tools, state, and interactions is hard to get. (02:57-03:15)
- Temporal stores workflow history so developers can inspect how an agent navigated a complex set of interactions. (10:42-10:57)
- The same history can be exported for compliance needs or to debug behavior in test/dev environments. (11:44-12:05)
- Signals and queries for user/system interaction are stored in workflow history, creating a clear record of how the agent executes. (11:26-11:41)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use Durable Execution for Production Agent Loops](use-durable-execution-for-production-agent-loops.md)
- [Agent traces require specialized eval infrastructure](agent-traces-require-specialized-eval-infrastructure.md)
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)

Sources:
- [Scaling AI Agents Without Breaking Reliability - Preeti Somal, Temporal](../sources/20250728_1izYWsokr9s.md), 02:57-03:15, 10:42-12:05
