# Platforms for Humans and Machines: Engineering for the Age of Agents - Juan Herreros Elorza

Source: [Platforms for Humans and Machines: Engineering for the Age of Agents - Juan Herreros Elorza](https://www.youtube.com/watch?v=cCRO3ChaYhM)
Uploaded: 2026-04-08
Transcript: `raw/20260408_cCRO3ChaYhM/cCRO3ChaYhM.en-orig.vtt`

## Summary

Juan Herreros Elorza argues that internal developer platforms become agent platforms when they expose self-service, API-based, local-first, documented, and observable workflows. The source frames AI as a forcing function for platform-engineering practices that were already useful for humans: remove person-dependent handoffs, let agents invoke platform capabilities and read results through machine-friendly surfaces, provide local validation loops, and guard AI-assisted platform contributions with policy plus agent-readable context.

## Extracted Concepts

- [Make internal platforms self-service for agent users](../concepts/make-internal-platforms-self-service-for-agent-users.md) - this source explains why person-dependent deployment and provisioning workflows block coding agents.
- [Expose observability as agent-readable feedback](../concepts/expose-observability-as-agent-readable-feedback.md) - this source connects logs, metrics, and traces to an agent's ability to verify and iterate.
- [Local-first platform workflows shorten agent feedback loops](../concepts/local-first-platform-workflows-shorten-agent-feedback-loops.md) - this source recommends failing early through local validation before remote pipelines.
- [Guard AI-assisted platform contributions with policy and context](../concepts/guard-ai-assisted-platform-contributions-with-policy-and-context.md) - this source warns that lower contribution barriers need hard guardrails and contribution instructions.

## Topic Links

- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- Platform pain that is tolerable for humans becomes a larger blocker for agents: a coding agent cannot realistically discover tribal deployment knowledge by asking teammates or waiting on another platform team. (02:54-06:24)
- Agent-ready platforms should make resource provisioning and operational actions self-service, with no mandatory dependency on a specific person. (07:06-08:24)
- Platform self-service should be API-based, with CLI or MCP wrappers around well-defined APIs when useful, because agents are stronger at invoking structured interfaces than navigating ad hoc human flows. (08:29-10:01)
- Because coding agents often work locally, platform teams should shift validation left so agents can detect failures before pushing to version control and waiting on remote workflows. (10:04-11:14)
- Agents need explicit success criteria plus access to machine-readable logs, metrics, and traces so they can close the iteration loop without relying on graphical dashboards. (11:14-12:20)
- Documentation should either live next to the code it explains or be discoverable centrally for broad platform knowledge; when possible, serve the precise relevant documentation over an API rather than forcing the agent to parse a full HTML page. (12:49-14:04)
- `AGENTS.md`, `CLAUDE.md`, compiler instruction files, and skills can encode build, test, deploy, verification, platform convention, and contribution guidance for agents. (14:09-15:11)
- AI lowers the barrier to contributing to internal platforms, but platform owners remain responsible for security, compliance, standards, and maintainability through policy guardrails plus agent-readable context. (15:19-17:05)
- Platform readiness for AI agents should be measured through before/after effects on delivery metrics, reliability, support requests, and developer experience rather than assumed from adoption. (17:12-19:19)
