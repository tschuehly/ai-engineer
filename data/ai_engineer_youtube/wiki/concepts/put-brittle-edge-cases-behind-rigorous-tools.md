# Put brittle edge cases behind rigorous tools

Summary: A flexible agent loop can stay simple while specific brittle or high-risk behavior moves into structured tools. Tool boundaries are useful when a behavior needs versioning, evaluation, security controls, or tighter semantics than prompt guidance can provide.

Use when:
- Choosing whether an agent behavior belongs in a prompt, a skill, a DAG, or a tool.
- Hardening coding-agent or product-agent workflows that need reliable handling of edge cases.

Details:
- The source recommends a middle ground: keep the master loop and tool-call paradigm, but make selected tool calls rigorous when the use case needs more care. 25:10-25:29
- For edge cases, structured tools can be versioned and evaluated, while exploratory work can remain model-led or prompt-steered. 25:29-25:48
- Read, grep/glob, edit, and Bash illustrate different tool-boundary reasons: token limits, exact search, read-before-edit constraints, sandboxing, and command composition. 12:48-17:37
- Unified diffing is treated as a tool-level representation choice that reduces token load and makes edits faster and less error-prone than whole-file rewrites. 34:49-35:31

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Use Bash as a composable code-mode tool for agents](use-bash-as-a-composable-code-mode-tool-for-agents.md)
- [Layer agent permissions across model behavior, harness parsing, and sandboxing](layer-agent-permissions-across-model-behavior-harness-parsing-and-sandboxing.md)
- [Constrain sensitive file access with purpose-built tools](constrain-sensitive-file-access-with-purpose-built-tools.md)

Sources:
- [How Claude Code Works - Jared Zoneraich, PromptLayer](../sources/20251226_RFKCzGlAU6Q.md), 12:48-17:37
- [How Claude Code Works - Jared Zoneraich, PromptLayer](../sources/20251226_RFKCzGlAU6Q.md), 25:10-25:48
- [How Claude Code Works - Jared Zoneraich, PromptLayer](../sources/20251226_RFKCzGlAU6Q.md), 34:49-35:31
