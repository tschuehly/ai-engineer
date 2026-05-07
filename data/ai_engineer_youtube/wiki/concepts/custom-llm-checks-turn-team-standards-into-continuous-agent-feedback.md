# Custom LLM Checks Turn Team Standards Into Continuous Agent Feedback

Summary: LLM-based checks can turn branch goals, style rules, architecture expectations, specs, implementation gaps, and test-quality standards into continuous feedback for coding agents. Once an issue is stated clearly, repair agents can fix it more reliably.

Use when:
- Building custom review checks around a coding-agent workflow.
- Converting team standards or recurring review comments into reusable agent feedback.

Details:
- Albrecht proposes asking an LLM to check whether the current branch matches its goal, whether code follows style and architecture expectations, whether specs are missing or outdated, and whether tests are meaningful (14:49-15:26).
- Custom checks let teams encode their own best practices instead of relying only on generic linters or one-time prompt instructions (14:49-15:26).
- Well-stated issues are easier for agents to repair; simple strategies such as multiple attempts by different agents can work when sandboxing and parallelism make failed attempts cheap (15:29-16:22).
- Adjacent developer-experience tools such as post-deployment debugging, logging, tracing, profiling, automated QA agents, and visual-to-code systems fit the same pattern of using AI around the whole software lifecycle rather than only code generation (16:24-17:25).

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [AI review gates turn standards into executable feedback](ai-review-gates-turn-standards-into-executable-feedback.md)
- [Use reviewer agents and lints to turn review lessons into guardrails](use-reviewer-agents-and-lints-to-turn-review-lessons-into-guardrails.md)
- [Parallel Coding Agents Support Multitasking and Variation Search](parallel-coding-agents-support-multitasking-and-variation-search.md)

Sources:
- [Beyond the Prototype: Using AI to Write High-Quality Code - Josh Albrecht, Imbue](../sources/20250725_x_1EumTaXeE.md), 14:49-17:25
