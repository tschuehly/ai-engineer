# Make Validation Fast, Local, Deterministic, and Actionable

Summary: Agent capability rises when checks are objective, deterministic, fast enough to run during development, and written with clear failure messages. Slow CI-only checks, vague errors, and superficial tests make agents loop blindly or ship work that only appears validated.

Use when:
- Designing tests, linters, CI, or local commands for coding-agent workflows.
- Diagnosing why agents keep making low-quality fixes after running the available checks.

Details:
- Objective deterministic validation increases agent capability because it gives the model concrete feedback to repair against (05:07-05:17).
- Validation quality matters more than merely having a check: the error should explain the problem and what the agent should do next, not just return a vague failure such as an unexplained 500 (05:20-05:49).
- Asking an agent to add tests to an untestable codebase can produce shallow tests that only prove a button was pushed; teams may need to refactor for testability before agent-written tests become useful (05:50-06:40).
- Checks should be runnable at development time, not only in slow CI. Agents may patiently rerun a 15- or 20-minute pipeline many times, but that repeated loop destroys developer productivity compared with a 30-second local check (16:37-17:18).
- Agent readiness depends on validation being objective, quick, scalable, low-noise, and continuous enough for agents to search against; partial manual testing and flaky builds that humans tolerate become capability limits for coding agents (01:23-06:04).
- Validation should encode more than formatting: opinionated linters, tests that catch low-quality generated changes, OpenAPI specs, browser or visual checks, and review documentation all give agents constraints they cannot reliably invent from context alone (03:20-04:41, 08:26-10:08).

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent software factories need runnable, contextual, and verifiable primitives](agent-software-factories-need-runnable-contextual-and-verifiable-primitives.md)
- [Treat agent readiness as verification infrastructure](treat-agent-readiness-as-verification-infrastructure.md)
- [Use agent readiness flywheels to improve the development environment](use-agent-readiness-flywheels-to-improve-the-development-environment.md)
- [Limit agent change size by feedback speed](limit-agent-change-size-by-feedback-speed.md)
- [Use deep modules to make agent work testable](use-deep-modules-to-make-agent-work-testable.md)

Sources:
- [Developer Experience in the Age of AI Coding Agents - Max Kanat-Alexander, Capital One](../sources/20251223_rT2Del5pwg4.md), 05:07-06:40, 16:37-17:18
- [Making Codebases Agent Ready - Eno Reyes, Factory AI](../sources/20251222_ShuJ_CN6zr4.md), 01:23-10:08
