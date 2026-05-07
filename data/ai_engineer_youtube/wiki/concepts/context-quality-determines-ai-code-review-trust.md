# Context Quality Determines AI Code Review Trust

Summary: AI code generation and review become more trustworthy when they receive the right software-development context, not just the current code diff. Useful context can include code, standards, best practices, version history, PR history, organizational logs, and documentation.

Use when:
- Investigating why developers distrust generated code or AI review comments.
- Designing context engines or MCP tools for code generation, review, testing, and quality gates.

Details:
- The talk reports that developers who distrust AI-generated code often point to weak or missing LLM context, and context was the top requested improvement for generation and review tools. (14:19-15:10)
- Better context is framed as improving quality across generation and review, with context calls often going to a context MCP or similar source rather than a generic tool. (14:19-15:31)
- Review context should include standards and best practices as well as repository code; the source reports that a portion of review-context usage comes from standards-related files. (15:31-15:50)
- The broader context substrate can include code, versioning, PR history, organizational logs, and other software-development records rather than only the latest branch. (16:19-16:39)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Context engines select task-specific organizational context](context-engines-select-task-specific-organizational-context.md)
- [Encode non-functional requirements as agent-visible context](encode-non-functional-requirements-as-agent-visible-context.md)
- [Fresh Markdown context mitigates model rot in codegen](fresh-markdown-context-mitigates-model-rot-in-codegen.md)

Sources:
- [The State of AI Code Quality: Hype vs Reality — Itamar Friedman, Qodo](../sources/20251211_rgjF5o2Qjsc.md), 14:19-16:39
