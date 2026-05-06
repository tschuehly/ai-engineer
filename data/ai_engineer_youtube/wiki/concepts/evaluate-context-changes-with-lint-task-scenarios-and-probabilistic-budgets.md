# Evaluate Context Changes with Lint, Task Scenarios, and Probabilistic Budgets

Summary: Context updates should be evaluated at multiple levels, from format linting to task scenarios. Because LLM outputs vary, context CI should use repeated runs and acceptable error budgets instead of expecting exact deterministic results every time.

Use when:
- Testing edits to `AGENTS.md`, `agent.md`, skills, prompt libraries, or team conventions.
- Deciding whether an AI eval should be a deterministic check, an LLM judge, a tool-backed execution test, or a repeated-run threshold.

Details:
- A small edit to a context file can change generated code, so teams should test context impact rather than relying on "looks good" review (06:12-06:59).
- Lint-like checks can validate context package structure, such as required descriptions and length limits for skills (07:03-07:35).
- Clarity checks can ask whether an agent understands a context block and whether it is explicit or complete enough for the intended task (07:38-08:26).
- Scenario checks can compare generated code against team-specific rules, such as requiring a custom API route prefix that no model would infer without context (08:43-10:14).
- Tool-backed judges can execute generated behavior in a sandbox, turning a context eval into an end-to-end check instead of only inspecting files (10:44-11:34).
- Nondeterministic evals should be run multiple times and judged against an error budget, because a single pass/fail run may not be stable enough for CI/CD (12:28-13:48).

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Validate eval harnesses before trusting skill scores](validate-eval-harnesses-before-trusting-skill-scores.md)
- [Evaluate agent skills with task scenarios and comparative conditions](evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md)

Sources:
- [Context Is the New Code - Patrick Debois, Tessl](../sources/20260503_bSG9wUYaHWU.md), 06:12-13:48
