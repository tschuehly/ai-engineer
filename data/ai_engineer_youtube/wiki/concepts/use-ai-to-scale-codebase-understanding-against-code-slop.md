# Use AI to scale codebase understanding against code slop

Summary: AI can fight code slop by increasing human and agent understanding of the codebase, not only by generating more code. Code maps, computer-use workflows, subagents, and modular boundaries help route scarce human attention to the hardest decisions.

Use when:
- Designing anti-slop workflows for large codebases.
- Deciding whether an AI tool should generate code, inspect code, map context, or operate existing development tools.

Details:
- The talk frames anti-slop work as asymmetric: falling token costs make generation cheap, while the taste needed to fight low-quality output is much larger than the effort needed to produce it. (04:28-05:08)
- swyx suggests using AI to fight slop, including prompting models explicitly not to produce slop and using AI news curation as an example of telling users when there is nothing worth reading. (05:11-05:41)
- For code, the source points to human attention on the hardest problems while commoditized work becomes more asynchronous. (06:31-06:44)
- AI-generated code maps are presented as a way to scale codebase understanding, which can help fight code slop by making the system easier to inspect before and after generated changes. (06:46-07:04)
- The talk also names computer use for complex apps, subagents for context rot, and modularity with clear human-designed boundaries as anti-slop patterns. (07:04-08:01)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent-legible codebases reduce generated-code entropy](agent-legible-codebases-reduce-generated-code-entropy.md)
- [Use deep modules to make agent work testable](use-deep-modules-to-make-agent-work-testable.md)
- [Use human judgment gates for high-risk agent code changes](use-human-judgment-gates-for-high-risk-agent-code-changes.md)
- [Fresh Markdown context mitigates model rot in codegen](fresh-markdown-context-mitigates-model-rot-in-codegen.md)

Sources:
- [No More Slop - swyx](../sources/20251222_IoiHI7p12Ao.md), 04:28-08:01
