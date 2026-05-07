# Coding-agent taste captures the invisible architecture of choices

Summary: Coding-agent taste is the learned set of situational coding choices that makes generated code match a developer, team, project, or domain style beyond mere correctness.

Use when:
- A coding agent produces code that passes tests but feels wrong for the repository or reviewer.
- A team wants agents to reproduce maintainability, file-layout, tooling, naming, and interaction conventions that are hard to enumerate exhaustively.

Details:
- Awais frames good code as more than correct output: programmers care about an "invisible architecture of choices" built over years that makes code readable, maintainable, and humane. (12:21-12:44)
- In the CLI demo, the preference layer chooses TypeScript, pnpm, tsup, Commander, Vitest, command-directory structure, lowercase `-v`, and `0.0.1` starting versions because those match the developer's prior choices rather than the immediate prompt alone. (02:08-05:30)
- The concept challenges static rule files as a complete solution: `CLAUDE.md`, `AGENTS.md`, and similar files can expose rules, but taste covers contextual judgment that a developer may not be able to write down before doing the work. (10:12-10:50, 15:21-15:31)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [AI agents still need human taste for interaction quality](ai-agents-still-need-human-taste-for-interaction-quality.md)
- [Treat prompts as distributed harness surfaces](treat-prompts-as-distributed-harness-surfaces.md)
- [Maintain ubiquitous language for AI coding](maintain-ubiquitous-language-for-ai-coding.md)

Sources:
- [Developing Taste in Coding Agents: Applied Meta Neuro-Symbolic RL - Ahmad Awais, CommandCode](../sources/20251124_kWOQS3XPZ10.md), 02:08-05:30, 10:12-10:50, 12:21-12:44, 15:21-15:31
