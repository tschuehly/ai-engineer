# Human Approval Can Hide Tool-Description and Parameter Risk

Summary: Human approval gates only work when the reviewer can see the actual action, instructions, and parameters being approved. A simplified tool summary can hide full tool-description instructions or side-channel parameters that the model reads and executes.

Use when:
- Designing approval UX for MCP, function calling, workflow tools, or agent actions.
- Auditing whether an approval prompt exposes enough detail to support a real human decision.

Details:
- The MCP attack described in the talk exploits an asymmetry between the human-visible tool summary and the full tool description read by the model. 10:53-11:19
- A user may approve a benign one-line operation, while hidden instructions in the full description cause the model to exfiltrate credentials through a hidden parameter. 11:19-11:44
- The talk calls this an "iceberg effect": what the human reviewer sees may not be what they are actually approving. 15:28-15:39
- Approval systems should therefore render the effective operation, sensitive arguments, hidden metadata, and tool-description risk, rather than presenting only a friendly function name or short summary. This is an inference from the source's MCP exploit and approval-surface critique.

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [Filter MCP tools by scopes and step-up authorization](filter-mcp-tools-by-scopes-and-step-up-authorization.md)

Sources:
- [$1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs - Diego Carpentero](../sources/20260416_YZHPEkfy2kc.md), 10:53-12:04, 15:28-15:39
