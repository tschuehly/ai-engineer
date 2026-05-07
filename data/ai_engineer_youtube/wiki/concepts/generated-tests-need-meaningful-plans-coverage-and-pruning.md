# Generated Tests Need Meaningful Plans, Coverage, and Pruning

Summary: AI makes tests cheap to generate, but generated suites still need human-meaningful plans, coverage signals, sandboxed execution, and pruning. Keeping too many low-value generated tests can become future context noise for coding agents.

Use when:
- Asking a coding agent to add tests for generated or modified code.
- Deciding which AI-generated tests should be kept in a durable repository.

Details:
- Cheap test generation removes some effort objections, but Albrecht warns against indiscriminately keeping generated unit tests because obsolete or excessive tests can confuse future LLM changes (09:55-10:37).
- User-level integration test plans are a better steering artifact than isolated implementation checks: a human can specify behavior such as an add-to-cart flow, and the agent can write tests from that meaning-level plan (13:04-13:49).
- Merge confidence improves when changed code has enough coverage, tests pass, and the tests themselves are reviewed as reasonable rather than merely present (13:52-14:28).
- Tests should run in sandboxes and without secrets so generated test execution does not accidentally mutate production systems or depend on flaky external state (14:31-14:47).

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Use Multisensory Feedback Loops for Coding-Agent Validation](use-multisensory-feedback-loops-for-coding-agent-validation.md)
- [Autonomous browser verification finds painted-door failures](autonomous-browser-verification-finds-painted-door-failures.md)
- [Give coding agents the same engineering infrastructure humans need](give-coding-agents-the-same-engineering-infrastructure-humans-need.md)

Sources:
- [Beyond the Prototype: Using AI to Write High-Quality Code - Josh Albrecht, Imbue](../sources/20250725_x_1EumTaXeE.md), 09:55-14:47
