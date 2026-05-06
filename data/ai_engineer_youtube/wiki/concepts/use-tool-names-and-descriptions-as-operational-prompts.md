# Use Tool Names and Descriptions as Operational Prompts

Summary: Tool names and descriptions are part of the agent prompt surface, so they should be explicit, task-oriented, and updated when tool-calling behavior fails.

Use when:
- An agent has tools available but calls the wrong one or fails to call one.
- Encoding tool-specific instructions without bloating the global system prompt.

Details:
- The n8n workshop warns that users often under-specify tool prompting; the node name becomes the tool name, and the node description becomes the tool description passed to the LLM. 29:06-29:59
- Tool descriptions can hold full prompts for tool-specific behavior, making reusable nodes more modular than putting every instruction in the agent's system prompt. 30:00-30:47
- If a tool is not being called or expected behavior is missing, the recommended debugging loop is to adjust the relevant prompt or description and retest. 31:48-32:14
- Tool descriptions are also an attack surface: Carpentero describes an MCP exploit where the model reads hidden instructions in a full tool description that the human approval summary does not show. 10:53-12:04

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use skills for workflow guidance and MCP for integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)
- [Visual agent workflows make tool use observable and adjustable](visual-agent-workflows-make-tool-use-observable-and-adjustable.md)
- [Human approval can hide tool-description and parameter risk](human-approval-can-hide-tool-description-and-parameter-risk.md)

Sources:
- [Human-in-the-Loop Automation with n8n - Liam McGarrigle](../sources/20260502_tDArkCqjA-c.md), 29:06-32:14
- [$1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs - Diego Carpentero](../sources/20260416_YZHPEkfy2kc.md), 10:53-12:04
