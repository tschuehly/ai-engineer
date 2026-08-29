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

- **The four properties do not move together, and verification routes trade among them.** Proof checking is the extreme of *deterministic* and does well on *local* — Lean runs in the browser, the kernel runs on your machine — but it is weakest on *actionable*: a failed proof reports a goal that would not close, not an input that breaks. The solver route is the counterexample-producing sibling, since a solver "is a calculator… you feed in a formula and it returns an output. In this case, satisfiable or unsatisfiable," which is what Verus builds on with Z3. Worth carrying: the route you pick changes the quality of the feedback, not only the strength of the guarantee. ([Pant](../sources/20260828_lRa9sPaMyy4.md), 03:16-03:53, 07:07-07:39, 09:17-09:35)

- **All four properties in one investment, with actionability treated as an engineering task in its own right.** Amazon's teams built "mock services that run entirely locally with deterministic responses because it lets the agent do everything locally" — fast, local, and deterministic in a single move — and separately worked on the actionable half, listing "improve existing tools error messages so that the model knew what was going on when it failed" as part of the brownfield pre-work rather than as an incidental fix. The same criterion drives the most drastic change she reports, moving off untyped languages because "there's no compiler errors. So the model kind of guesses," toward Rust and TypeScript, where "the compiler gives great error messages." The stated payoff for all of it is loops: "the more that your agent can get fast feedback means the more loops that it can do." ([Liguori](../sources/20260828_pqlWNihgdjI.md), 10:10-11:08, 14:36-15:19)

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
- [Pick a Verification Route by Which Translation You Can Afford](pick-a-verification-route-by-which-translation-you-can-afford.md)
- [Being in the Loop Is the Ceiling on Agent Parallelism](being-in-the-loop-is-the-ceiling-on-agent-parallelism.md)

Sources:
- [Developer Experience in the Age of AI Coding Agents - Max Kanat-Alexander, Capital One](../sources/20251223_rT2Del5pwg4.md), 05:07-06:40, 16:37-17:18
- [Making Codebases Agent Ready - Eno Reyes, Factory AI](../sources/20251222_ShuJ_CN6zr4.md), 01:23-10:08
- [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](../sources/20260828_lRa9sPaMyy4.md), 03:16-03:53, 07:07-07:39, 09:17-09:35
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 10:10-11:08, 14:36-15:19
