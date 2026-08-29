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
- **Where the readiness backlog comes from, and how it gets ordered.** Blum ranks this investment first — "investing in verification is probably the highest value thing we can do in our code base" — and frames each item as a left shift: "anytime that we can left shift anything in our workflow from a human needing to do it to an agent being able to verify it." What this page lacks is a source for the ordering, and he supplies one: the org's agent skeptics are "seeing the way you are lacking validation, where your tools fail," so "their feedback is basically the road map of how to improve your agent[s] interacting with the code base." Readiness work then has a prioritized backlog written by the people currently absorbing the failures rather than by whoever owns the rollout. ([Blum](../sources/20260828_5Bn0xro2ol8.md), 05:00-05:20, 11:57-12:33)

- **The ROI argument that finally pays for it, and the one item that is genuinely new.** Liguori's fifth habit is the familiar list — "linters… unit tests, integration tests, performance tests, security tests" — with an unusually honest framing: "these are all things we all know we should have been doing all along. This is good engineering hygiene and practices. But now the ROI is, I think, finally high enough for actually us to actually invest in it." The item that is not just older advice with a new justification is the shift away from live-service integration testing: "we've been investing a lot in mock services that run entirely locally with deterministic responses because it lets the agent do everything locally," on the laptop, "without having to spin up a bunch of other services and connect to cloud services." The stated payoff is loop count — "the more that your agent can get fast feedback means the more loops that it can do" — which is why readiness work is what buys the hours-long unattended run. ([Liguori](../sources/20260828_pqlWNihgdjI.md), 13:53-15:19)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Agent software factories need runnable, contextual, and verifiable primitives](agent-software-factories-need-runnable-contextual-and-verifiable-primitives.md)
- [Agent-legible codebases reduce generated-code entropy](agent-legible-codebases-reduce-generated-code-entropy.md)
- [The Best Engineers Adopt Agents Last, and Their Objections Are the Roadmap](the-best-engineers-adopt-agents-last-and-their-objections-are-the-roadmap.md)
- [Being in the Loop Is the Ceiling on Agent Parallelism](being-in-the-loop-is-the-ceiling-on-agent-parallelism.md)

Sources:
- [Making Codebases Agent Ready - Eno Reyes, Factory AI](../sources/20251222_ShuJ_CN6zr4.md), 01:23-08:24
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 05:00-05:20, 11:57-12:33
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 13:53-15:19
