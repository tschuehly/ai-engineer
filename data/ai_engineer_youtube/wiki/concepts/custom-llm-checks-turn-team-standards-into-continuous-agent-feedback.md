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

- **What breaks when "teams encode their own best practices" is scaled to hundreds of teams: nobody is left to retire the bad checks.** Uber's mechanism is to return per-rule telemetry to the rule's author — "we had to actually surface all of this observability… like the agent trajectory, addressal rate, sentiment analysis back to the teams. So that the teams could actually understand that 'Oh, I wrote this rule, but maybe not a lot of developers are liking it in my team, so let me go and update it.'" Without that view a custom-check library only grows, because the author never learns their check is disliked and no central reviewer is reading hundreds of team rule sets. The authoring itself was trivial by comparison; "the hard part was how to run these skills at scale with consistent quality and low cost." ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 09:16-10:12)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [AI review gates turn standards into executable feedback](ai-review-gates-turn-standards-into-executable-feedback.md)
- [Use reviewer agents and lints to turn review lessons into guardrails](use-reviewer-agents-and-lints-to-turn-review-lessons-into-guardrails.md)
- [Parallel Coding Agents Support Multitasking and Variation Search](parallel-coding-agents-support-multitasking-and-variation-search.md)
- [Distributed Rule Authoring Is a Platform Problem, Not an Authoring Problem](distributed-rule-authoring-is-a-platform-problem.md)

Sources:
- [Beyond the Prototype: Using AI to Write High-Quality Code - Josh Albrecht, Imbue](../sources/20250725_x_1EumTaXeE.md), 14:49-17:25
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 09:16-10:12
