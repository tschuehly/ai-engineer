# Enforce Deterministic Guardrails Around Sensitive Tool Calls

Summary: Sensitive or mission-critical tool calls should be wrapped with deterministic checks that run before the underlying tool executes. The agent can still choose actions, but hard policy boundaries should not depend on model compliance.

Use when:
- A tool can write files, access tenants, handle secrets, or affect production state.
- Prompt and tool-description guidance is insufficient as an enforcement mechanism.

Details:
- Multi-tenant systems can leak data when an agent does not understand folder, database, schema, or tenant boundaries, especially when third-party tools lack local architecture awareness. 03:52-04:32
- The talk recommends deterministic logic for sensitive task aspects because agents are nondeterministic and may ignore prompt or tool-description guidance. 22:53-23:55
- The demo wrapped the visual screenshot tool with path validation, checking that requested output paths stayed under the configured screenshot root before invoking the Playwright tool. 24:05-27:40
- Guardrail failures should return an agent-facing explanation that tells the model how to retry correctly, rather than crashing the whole agent process. 27:44-28:25

Related topics:
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [LLM Guardrails Need Checkpoints at Every Untrusted Boundary](llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md)
- [Secure MCP Servers by Shrinking the Agent-Visible Surface](secure-mcp-servers-by-shrinking-the-agent-visible-surface.md)
- [Govern MCP Tool Calls With Tool-Level Policy and End-to-End Traces](govern-mcp-tool-calls-with-tool-level-policy-and-end-to-end-traces.md)

Sources:
- [Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz](../sources/20260408_U00AOI1eJUE.md), 03:52-28:25
