# Govern MCP Tool Calls With Tool-Level Policy and End-to-End Traces

Summary: Enterprise MCP governance needs policy and observability around each tool call, not only session-level OAuth. Production systems should record who or what called each tool, parameters, returned data, policy decisions, and the full path from request validation through generated response.

Use when:
- Designing audit, compliance, or incident-response controls for MCP servers.
- Deciding which MCP policy checks belong at session, tool, resource, and response boundaries.

Details:
- Agent-to-agent graphs need end-to-end authorization visibility as authority moves across agents and servers, not only policy at the first MCP connection. 16:58-17:13
- OAuth scopes help but remain session-scoped; enterprise RBAC should also scope permissions at the individual tool and resource level. 22:42-23:00
- Data masking should remove fields such as email, phone, national identifiers, or other PII before agents see them when the immediate task does not require that data. 23:03-23:17
- Interaction logs should record which agent called which tool, with which parameters, and what data was returned; autonomous systems may need this level of detail for compliance regimes such as the EU AI Act. 23:22-23:39
- Full-request observability should trace client request validation, execution, data retrieval, and generated response; without end-to-end traceability, teams cannot govern agent behavior after the fact. 23:43-24:07

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [MCP gateways create an enterprise root of trust](mcp-gateways-create-an-enterprise-root-of-trust.md)
- [Gateway platform primitives let teams focus on MCP business logic](gateway-platform-primitives-let-teams-focus-on-mcp-business-logic.md)
- [LLM guardrails need checkpoints at every untrusted boundary](llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md)
- [Agent traces require specialized eval infrastructure](agent-traces-require-specialized-eval-infrastructure.md)

Sources:
- [How to Secure Agents using OAuth - Jared Hanson (Keycard, Passport.js)](../sources/20250730_blmAkayzE8M.md), 16:58-17:13
- [Your Insecure MCP Server Won't Survive Production - Tun Shwe, Lenses](../sources/20260408_BurJvbqFr4c.md), 22:42-24:07
