# Context Is the New Code - Patrick Debois, Tessl

Source: [Context Is the New Code - Patrick Debois, Tessl](https://www.youtube.com/watch?v=bSG9wUYaHWU)
Uploaded: 2026-05-03
Transcript: `raw/20260503_bSG9wUYaHWU/bSG9wUYaHWU.en-orig.vtt`

## Summary

Patrick Debois frames agent context as an engineering artifact that deserves a lifecycle similar to code: generate, evaluate, distribute, observe, and then improve it from feedback. The talk covers reusable prompts and skills, context evals and linting, probabilistic error budgets for nondeterministic evals, package and registry models for distributing context, and operational feedback loops from agent logs, PR reviews, production failures, and context-filter security controls.

## Extracted Concepts

- [Context development lifecycle treats context as an engineered artifact](../concepts/context-development-lifecycle-treats-context-as-an-engineered-artifact.md) - this source defines a generate, evaluate, distribute, observe, and adapt loop for context.
- [Evaluate context changes with lint, task scenarios, and probabilistic budgets](../concepts/evaluate-context-changes-with-lint-task-scenarios-and-probabilistic-budgets.md) - this source explains how context tests differ from deterministic code tests.
- [Package reusable context as skills, libraries, and registries](../concepts/package-reusable-context-as-skills-libraries-and-registries.md) - this source describes distributing reusable context across projects and teams.
- [Use agent logs and review feedback as context observability signals](../concepts/use-agent-logs-and-review-feedback-as-context-observability-signals.md) - this source treats missing-context signals in logs, PRs, and production as inputs to context improvement.
- [Filter untrusted context before it reaches the agent](../concepts/filter-untrusted-context-before-it-reaches-the-agent.md) - this source warns that sandboxing execution does not stop malicious or unsafe context from being loaded.

## Topic Links

- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- Context can replace code for workflows whose branching surface would be expensive to hard-code: a skill can tell an agent to inspect the user's package manager and ecosystem before guiding setup steps, turning reusable workflow logic into context (01:21-02:35).
- The proposed context development lifecycle is generate, test/evaluate, distribute, observe, adapt, and regenerate; the loop is modeled after software delivery practices rather than one-off prompting (03:04-03:45).
- Generated context includes prompts, reusable instruction files such as `agent.md`, current library documentation, repository or ticket context pulled through tools, and spec-driven prompts broken into plans (03:50-06:03).
- Context changes need evaluation because a small edit to agent instructions can change downstream code behavior, and different coding agents may react differently to the same context (06:12-10:14).
- Context evals can include lint-like checks for format, clarity checks that ask whether the agent can understand the context, LLM-as-judge checks of generated code, and tool-backed judges that execute generated behavior in a sandbox (07:03-11:34).
- Because LLM evals are nondeterministic, context CI should use repeated runs and error budgets rather than a single exact pass/fail result (12:28-13:48).
- Reusable context can be packaged like a library, discovered through registries, and installed per project, but this introduces quality, dependency, versioning, and security concerns similar to software packages (14:00-17:40).
- Observability should use agent logs, PR feedback, and production failures to find missing or ineffective context, then convert repeated failures into shared context improvements (17:54-20:29).
- Sandboxes constrain tool execution, but they do not prevent unsafe `agent.md` or `skill.md` content from being loaded into the agent; context filters are needed to screen prompt injection or unsafe patterns before context enters the model (20:55-22:12).
