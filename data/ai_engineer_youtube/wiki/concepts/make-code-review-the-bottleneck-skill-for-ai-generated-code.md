# Make Code Review the Bottleneck Skill for AI-Generated Code

Summary: As agents generate more implementation, code review becomes the scarce production skill. Teams need reviewers who can explain whether a change is good or bad, and review tools that present change intent and system impact rather than only file-sorted diffs.

Use when:
- Designing review workflows for agent-generated pull requests.
- Hiring or training engineers for AI-assisted software teams.

Details:
- Code review is framed as the most important skill for AI-assisted engineering because agents will write more code and humans must decide what is acceptable. (11:20-11:44)
- The source argues that interviews should test the ability to read someone else's code and explain why it is good or bad, not only solve isolated coding puzzles. (11:23-11:38)
- Current review tools are criticized for presenting lexicographically sorted changed files, which does not match how reviewers reason about the intent and effects of a software change. (11:44-12:05)
- Reviewers should distinguish code that is merely different from code that is worse; style guides, linters, and rules files should absorb preference disputes so human attention can focus on quality. (13:23-14:06)
- LLM claims about what the model did should be verified against actual tool behavior and code evidence, because fluent explanations may not reflect the real process. (12:24-13:17)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [AI output speed can overwhelm review capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Review coding-agent work at task, plan, and code checkpoints](review-coding-agent-work-at-task-plan-and-code-checkpoints.md)
- [Context quality determines AI code review trust](context-quality-determines-ai-code-review-trust.md)
- [Do not report agent autonomy without quality accountability](do-not-report-agent-autonomy-without-quality-accountability.md)

Sources:
- [Vibes won't cut it - Chris Kelly, Augment Code](../sources/20250803_Dc3qOA9WOnE.md), 11:20-14:06
