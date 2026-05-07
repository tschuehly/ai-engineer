# General Agents Need Skills for Domain Expertise

Summary: A general code/runtime agent can be reused across domains, but useful real-world work still needs domain-specific procedural knowledge packaged separately from the core scaffold.

Use when:
- Deciding whether to build a new domain-specific agent or add skills to a general agent.
- Separating general agent runtime capability from specialized professional expertise.

Details:
- The talk argues that code is a universal interface to digital work: the same agent can call APIs, manage files, run Python analysis, and produce outputs through a thin Bash/filesystem scaffold. 01:38-02:09
- The limiting factor is not only intelligence or tools, but expertise: a tax, finance, legal, research, or internal-software workflow needs consistent domain execution instead of forcing the model to infer specialized rules from first principles. 02:11-02:56
- A domain capability can often be added by equipping the same general agent with the right MCP servers for connectivity and the right skill library for procedural expertise. 09:13-10:31

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Use skills for workflow guidance and MCP for integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Use Bash as a composable code-mode tool for agents](use-bash-as-a-composable-code-mode-tool-for-agents.md)

Sources:
- [Don't Build Agents, Build Skills Instead - Barry Zhang & Mahesh Murag, Anthropic](../sources/20251208_CEvIs9y1uog.md), 01:38-02:56, 09:13-10:31
