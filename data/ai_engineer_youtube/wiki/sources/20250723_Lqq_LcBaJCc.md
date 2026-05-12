# How agents will unlock the $500B promise of AI - Donald Hruska, Retool

Source: [How agents will unlock the $500B promise of AI - Donald Hruska, Retool](https://www.youtube.com/watch?v=Lqq_LcBaJCc)
Uploaded: 2025-07-23
Transcript: `raw/20250723_Lqq_LcBaJCc/Lqq_LcBaJCc.en-orig.vtt`

## Summary

Donald Hruska frames production business agents as a build-versus-buy engineering decision: the basic ReAct-style loop is easy to prototype, but enterprise use depends on controls such as SSO, RBAC, secure connectors, audit logs, observability, cost tracking, evals, and deployment options for regulated environments.

## Extracted Concepts

- [Build Core Agents and Buy Commodity Agent Workflows](../concepts/build-core-agents-and-buy-commodity-agent-workflows.md) - this source gives a decision rule for handbuilt agents versus managed platforms.
- [Production Agent Platforms Need Enterprise Controls](../concepts/production-agent-platforms-need-enterprise-controls.md) - this source lists the operational and governance controls needed beyond a simple agent loop.
- [Agent tool loops turn model-required actions into executable results](../concepts/agent-tool-loops-turn-model-required-actions-into-executable-results.md) - this source reinforces the basic reason-act-tool-result loop and its need for iteration bounds.

## Topic Links

- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

## Notes

- A basic agent can be implemented as an LLM wrapped in an execution loop that reads, decides, calls tools, and self-verifies, with a maximum iteration count to avoid runaway thinking and cost burn, 04:10-05:43.
- The source warns that the easy prototype is not the production problem: enterprise agents need SSO, role-based access control, secure external-service integrations, audit logs, compliance, secrets handling, and internationalization, 05:44-06:47.
- Production agents also need safeguards for hallucinated or unpredictable results, security exposure, token-cost overruns, and evals that make nondeterministic behavior as controlled as possible, 06:47-07:22.
- Hruska groups implementation choices into handbuilt agents, frameworks such as LangGraph, agent platforms such as Retool Agents, and vertical agents; the tradeoff is control, engineering lift, flexibility, and production readiness, 07:26-08:36.
- The build-versus-buy decision should reserve handbuilt work for core product or competitive-edge workflows, consider both paths for regulated data or hard SLAs, and prefer managed platforms for commodity workflows needed in days rather than quarters, 08:39-09:29.
- Managed-platform evaluation should cover connector breadth, permissioning, compliance, audit trails, observability, email or notification support, token cost, infrastructure cost, and engineering cost, 09:32-10:33.
- Retool's Q&A adds that regulated customers may require on-prem or air-gapped agent support rather than cloud-only deployment, 15:34-16:01.
