# Secure MCP Servers by Shrinking the Agent-Visible Surface

Summary: Production MCP security starts with interface design: expose fewer, more specific tools with constrained inputs and minimal outputs. A server that gives agents broad tools, ambiguous descriptions, free-form payloads, or oversized responses increases both prompt-injection risk and data-exfiltration blast radius.

Use when:
- Designing an MCP server or function-calling API for agent use.
- Reviewing whether an agent-facing tool catalog exposes too much authority or context.

Details:
- Agents enumerate tool names and descriptions when they connect, so every extra tool description adds context cost and a possible tool-poisoning surface. 02:24-03:03
- Agent retries can resend the full conversation history, including previous tool results; oversized or sensitive responses can therefore leak repeatedly across retries. 03:03-03:29
- Coarse-grained outcome tools should replace fine-grained API operations when the agent only needs a business result, because one tool can have one permission check, audit log entry, and authorization point. 05:16-05:47
- Tool input schemas should prefer constrained primitives and enums, avoid free-form nested payloads, and validate stricter structures before they reach shells, query engines, or downstream APIs. 05:51-06:23
- Tool descriptions are a defensive layer: clear, complete, unambiguous documentation leaves less room for neighboring poisoned tool descriptions to steer the model. 06:26-06:58
- Tool responses should return only the fields needed for the immediate task; PII, credentials, internal IDs, and system details in context are one prompt injection away from exfiltration. 07:00-07:26
- Non-destructive capabilities should use MCP read-only annotations or resources where possible, and permissions should be scoped at the tool and resource level instead of broadly at the session level. 07:29-07:54

Related topics:
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [MCP tool surfaces need default context budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Discover large API tool surfaces progressively](discover-large-api-tool-surfaces-progressively.md)
- [Human approval can hide tool-description and parameter risk](human-approval-can-hide-tool-description-and-parameter-risk.md)
- [LLM guardrails need checkpoints at every untrusted boundary](llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md)

Sources:
- [Your Insecure MCP Server Won't Survive Production - Tun Shwe, Lenses](../sources/20260408_BurJvbqFr4c.md), 02:24-07:54
