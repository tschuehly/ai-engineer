# Keep agent-generated code clean enough for continued agent work

Summary: Agent-generated code does not need every possible abstraction or optimization, but it must stay clean enough that humans and later agents can continue from it without hitting avoidable roadblocks.

Use when:
- Reviewing whether an agent-generated change is acceptable.
- Deciding whether to optimize, refactor, accept repetition, or move on.

Details:
- The talk argues that LLMs are comfortable with repetitive code, and that humans often over-abstract repeated code too early. (05:16-05:27)
- Loose vibe coding is more appropriate for one-off scripts, simple features, personal tools, and code unlikely to be touched again. (12:41-13:01)
- The reusable skill is judging which generated code is good enough for the job and which niche optimization is not worth doing. (18:49-19:31)
- The quality bar is not "accept everything": repeatedly accepting slop eventually creates a codebase where even skilled engineers and future agents get stuck. (19:33-19:50)
- "Clean enough" includes enough structure for agents to continue working, not just enough polish for a human reviewer to tolerate once. (19:33-19:42)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Treat slop as a quality failure, not an AI provenance label](treat-slop-as-a-quality-failure-not-an-ai-provenance-label.md)
- [Limit agent change size by feedback speed](limit-agent-change-size-by-feedback-speed.md)
- [Use deep modules to make agent work testable](use-deep-modules-to-make-agent-work-testable.md)

Sources:
- [From Vibe Coding To Vibe Engineering - Kitze, Sizzy](../sources/20251214_JV-wY5pxXLo.md), 05:16-19:50
