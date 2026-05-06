# Treat Agent Readiness as Verification Infrastructure

Summary: A codebase is agent-ready when agents can rely on explicit, objective, scalable, low-noise validation signals. Model choice matters less when the environment cannot tell agents whether code style, behavior, integration, review expectations, and deployment safety are satisfied.

Use when:
- Diagnosing why coding agents work in demos but fail in production repositories.
- Deciding whether to invest in validation infrastructure, documentation, and repository conventions before broader agent rollout.

Details:
- Software development is a strong domain for agents because many tasks can be verified more cheaply than they can be solved; useful validation is objective, quick to check, scalable, low-noise, and able to provide continuous signals rather than only vague pass/fail feedback (01:23-03:20).
- Agent readiness includes ordinary engineering checks such as unit tests, end-to-end tests, QA tests, OpenAPI specs, linters, and newer browser or visual validation paths because those checks become constraints the agent can use during search (03:20-04:08).
- Human teams can tolerate partial test coverage, manual testing, and flaky builds because people compensate with tacit judgment; those same gaps reduce agent capability when agents participate in coding, review, documentation, and testing workflows (04:32-06:04).
- Spec and plan modes become more useful when the team specifies both what should be built and how it should be validated, then lets the agent generate candidates, verify mechanically, incorporate human intuition, and iterate (06:05-07:05).
- Scaled workflows such as parallel agents or large modernization decomposition require reliable single-task execution first; if a simple validated task does not work nearly all the time, parallelizing the workflow only multiplies failure (07:35-08:24).

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Agent software factories need runnable, contextual, and verifiable primitives](agent-software-factories-need-runnable-contextual-and-verifiable-primitives.md)
- [Agent-legible codebases reduce generated-code entropy](agent-legible-codebases-reduce-generated-code-entropy.md)

Sources:
- [Making Codebases Agent Ready - Eno Reyes, Factory AI](../sources/20251222_ShuJ_CN6zr4.md), 01:23-08:24
