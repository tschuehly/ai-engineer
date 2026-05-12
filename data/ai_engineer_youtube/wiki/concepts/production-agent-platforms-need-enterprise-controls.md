# Production Agent Platforms Need Enterprise Controls

Summary: Moving an agent from prototype to enterprise production requires platform controls around identity, permissions, connectors, audit, compliance, observability, cost, deployment, and evals.

Use when:
- Auditing an agent platform or internal harness for enterprise readiness.
- Turning a short ReAct-style prototype into a production business workflow.

Details:
- Hruska argues that the agent itself is the easy part; the production burden is the same class of enterprise concerns that makes quickly generated web apps hard to ship safely, 04:10-06:01.
- The checklist includes SSO, role-based access control, secure external-service integration, audit logs, compliance such as SOC 2, secrets handling, and internationalization, 06:01-06:47.
- Agent-specific risks include hallucinated or unpredictable results, access to sensitive systems, accidental token burn, and the need for evals to constrain nondeterministic behavior, 06:47-07:22.
- Managed platform evaluation should ask whether connector breadth, permissioning, compliance, audit trails, observability, email or notification surfaces, token cost, infrastructure cost, and engineering cost are built in or still owned by the team, 09:32-10:33.
- Regulated deployments may require on-prem or air-gapped support rather than cloud-only agents, 15:34-16:01.

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Build Core Agents and Buy Commodity Agent Workflows](build-core-agents-and-buy-commodity-agent-workflows.md)
- [First-Class Agent Users Need Identity, Scopes, and Audit Trails](first-class-agent-users-need-identity-scopes-and-audit-trails.md)
- [Replace Anecdotal Agent Tuning With Eval and Observability Loops](replace-anecdotal-agent-tuning-with-eval-and-observability-loops.md)

Sources:
- [How agents will unlock the $500B promise of AI - Donald Hruska, Retool](../sources/20250723_Lqq_LcBaJCc.md), 04:10-07:22, 09:32-10:33, 15:34-16:01
