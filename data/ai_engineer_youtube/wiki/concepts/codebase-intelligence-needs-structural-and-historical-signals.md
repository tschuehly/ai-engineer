# Codebase Intelligence Needs Structural and Historical Signals

Summary: Coding agents need representations of the codebase beyond raw text when work spans multiple files. Useful codebase intelligence includes structural relationships, language-server signals, commit history, lint feedback, and cross-file references.

Use when:
- Designing context retrieval or navigation tools for multi-file coding agents.
- Explaining why larger context windows alone do not solve repository understanding.

Details:
- Wu says broader bugs and feature requests require diagnosing behavior, working across files, and keeping changes consistent across several files.
- He highlights call hierarchies, language servers, git commit history, lint output, and cross-file references as signals that help an agent understand how files relate.
- Devin's internal codebase representation became useful to humans too through DeepWiki and codebase search, supporting a workflow where the user asks questions, explores with the agent, and then dispatches implementation.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Context engines select task-specific organizational context](context-engines-select-task-specific-organizational-context.md)
- [Model-shaped codebase architecture for coding agents](model-shaped-codebase-architecture-for-coding-agents.md)
- [Active repos per engineer exposes context architecture drag](active-repos-per-engineer-exposes-context-architecture-drag.md)

Sources:
- [Devin 2.0 and the Future of SWE - Scott Wu, Cognition](../sources/20250725_MI83buT_23o.md), 08:18-12:28
