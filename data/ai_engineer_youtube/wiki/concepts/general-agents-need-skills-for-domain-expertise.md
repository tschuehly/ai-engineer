# General Agents Need Skills for Domain Expertise

Summary: A general code/runtime agent can be reused across domains, but useful real-world work still needs domain-specific procedural knowledge packaged separately from the core scaffold.

Use when:
- Deciding whether to build a new domain-specific agent or add skills to a general agent.
- Separating general agent runtime capability from specialized professional expertise.

Details:
- The talk argues that code is a universal interface to digital work: the same agent can call APIs, manage files, run Python analysis, and produce outputs through a thin Bash/filesystem scaffold. 01:38-02:09
- The limiting factor is not only intelligence or tools, but expertise: a tax, finance, legal, research, or internal-software workflow needs consistent domain execution instead of forcing the model to infer specialized rules from first principles. 02:11-02:56
- A domain capability can often be added by equipping the same general agent with the right MCP servers for connectivity and the right skill library for procedural expertise. 09:13-10:31
- Why the gap does not close with a better model: the general account is that digital work is "millions of these micro worlds" where "even if you're using the same software, every company configure it differently," each with "its unique local physics" — too heterogeneous and too dynamic for "any monolithic model to try to compress it into one static representation" ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 05:25-06:24). Skills are one way to hold that per-environment competence outside the weights; the argument says something has to.
- Skills read as one option on a design axis rather than the answer. Su lists the candidate reusable structures for accumulated experience as "parameters like adapters of your language models, or vectors, graphs, or skills, or even [world] models" ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 11:48-11:59) — so choosing skills is choosing an inspectable, editable, human-authored structure over a learned one, with the tradeoffs that implies.
- **Why domain expertise has nowhere else to go.** Touil derives the same conclusion by elimination across a workflow's four components: hooks only "trigger on events," MCP servers are consumed rather than authored, and sub agents exist "just to minimize the context window," so "at the end of the day you will find all of your know-how is actually at the skills level. And if you don't have the right structure of your skills, then you're not really having a deterministic workflow." ([Touil](../sources/20260828_M05vON8i0aI.md), 05:53-06:52) The consequence for a general agent is that its domain expertise is not merely *best* placed in skills; there is no other authorable surface for it. Nothing in the talk is measured.

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Use skills for workflow guidance and MCP for integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Use Bash as a composable code-mode tool for agents](use-bash-as-a-composable-code-mode-tool-for-agents.md)
- [Digital Work Is Millions of Microworlds With Local Physics](digital-work-is-millions-of-microworlds-with-local-physics.md)
- [Define Continual Learning as Adaptive Compression of Experience](define-continual-learning-as-adaptive-compression-of-experience.md)
- [Skills Are the Residual Where Organizational Know-How Lands](skills-are-the-residual-where-organizational-know-how-lands.md)

Sources:
- [Don't Build Agents, Build Skills Instead - Barry Zhang & Mahesh Murag, Anthropic](../sources/20251208_CEvIs9y1uog.md), 01:38-02:56, 09:13-10:31
- [Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 05:25-06:24, 11:48-11:59
- [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../sources/20260828_M05vON8i0aI.md), 05:53-06:52
