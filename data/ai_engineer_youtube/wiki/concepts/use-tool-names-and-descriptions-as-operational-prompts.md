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
- **When the description channel is unavailable, the tool *result* becomes the prompt.** MCP's server-instructions field existed in the spec but "no clients implemented it," so Figma added "additional instructions into each tool call. Basically instructing the LLM how to use our server um even though server descriptions weren't necessarily written out yet." This is the same lever moved one layer later in the call: it costs tokens on every invocation rather than once at handshake, and it only reaches a model that has already decided to call the tool. ([Lumarie](../sources/20260828_ZIYYsAzaLlA.md), 09:48-10:14)
- **A description also has to override what the model already believes, and saying nothing lets the prior win.** Jarmak's trace is the clean demonstration: the model expected a particular parameter name "based off of its biases… from its training data," and "there's nothing in our description that would have led it to believe otherwise," so it called the tool with `read line` instead of `start line`. The tool was correct, the description was merely silent, and the run still cost a turn. Treat any place where your naming departs from the obvious convention as something the description must state explicitly rather than leave to inference. See [Count Burned Turns, Because Agent Self-Recovery Hides Tool Defects](count-burned-turns-because-agent-self-recovery-hides-tool-defects.md). ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 06:33-07:20)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use skills for workflow guidance and MCP for integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)
- [Visual agent workflows make tool use observable and adjustable](visual-agent-workflows-make-tool-use-observable-and-adjustable.md)
- [Human approval can hide tool-description and parameter risk](human-approval-can-hide-tool-description-and-parameter-risk.md)
- [Turn Tool Errors Into Agent Self-Healing Recovery](turn-tool-errors-into-agent-self-healing-recovery.md)
- [Tools Are the Only Primitive Every Client Implements](tools-are-the-only-primitive-every-client-implements.md)
- [Count Burned Turns, Because Agent Self-Recovery Hides Tool Defects](count-burned-turns-because-agent-self-recovery-hides-tool-defects.md)

Sources:
- [Human-in-the-Loop Automation with n8n - Liam McGarrigle](../sources/20260502_tDArkCqjA-c.md), 29:06-32:14
- [$1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs - Diego Carpentero](../sources/20260416_YZHPEkfy2kc.md), 10:53-12:04
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 09:48-10:14
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 06:33-07:20
