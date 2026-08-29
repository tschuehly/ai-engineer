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
- **Determinism settles what the check decides, not whether it answers.** A wrapper that calls out to a policy service, a classifier, or a filter is still a dependency: "guardrails are just like another service that can go down that can be unreliable," so the design has to state whether the sensitive tool call proceeds when the check is unavailable — "do you fail open or do you fail close" — with Manuja's default rule being that "the default choice should be the worst case that you can live with." For the sensitive-tool-call case that usually resolves to fail-closed, but the point is that leaving it unstated picks an answer anyway. ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 10:12-11:00)


- **The narrowest deterministic guardrail in the wiki, and why its narrowness is the feature.** Anthropic's CI team puts a proxy beside every agent session that "is not reading the prompt. It doesn't know why the agent wants to do something and it doesn't really care. It will see a delete happening, it'll see a budget being crossed and it'll simply return a 403." It "counts, compares, it can allow a delete or deny" and nothing more, and the payoff is stated as an injection property: "a clever prompt injection cannot really talk it out of the rule itself." An enforcement point that reads the prompt inherits the prompt's attack surface; a counter does not. The fail-open-or-closed question above applies to it directly and the source does not answer it, which matters more here than usual because this proxy sits in the path of *every* outbound call the agent makes. ([Malhotra](../sources/20260822_rbjWzZK2LU0.md), 16:05-16:59)

Related topics:
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [LLM Guardrails Need Checkpoints at Every Untrusted Boundary](llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md)
- [Secure MCP Servers by Shrinking the Agent-Visible Surface](secure-mcp-servers-by-shrinking-the-agent-visible-surface.md)
- [Govern MCP Tool Calls With Tool-Level Policy and End-to-End Traces](govern-mcp-tool-calls-with-tool-level-policy-and-end-to-end-traces.md)
- [Treat Guardrails as a Failable Dependency With Its Own Time Budget](treat-guardrails-as-a-failable-dependency-with-a-time-budget.md)
- [Keep Policy in Text for Intent and in Infrastructure for Bounds](keep-policy-in-text-for-intent-and-in-infrastructure-for-bounds.md)

Sources:
- [Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz](../sources/20260408_U00AOI1eJUE.md), 03:52-28:25
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 10:12-11:00
- [Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](../sources/20260822_rbjWzZK2LU0.md), 16:05-16:59
