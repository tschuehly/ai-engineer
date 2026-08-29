# Do not report agent autonomy without quality accountability

Summary: Autonomy duration is a weak agent-quality signal unless it is paired with evidence about the resulting work. Long unattended runs can still produce code slop, tech debt, or unsafe behavior.

Use when:
- Evaluating claims that an agent can work autonomously for many hours.
- Designing dashboards, demos, or benchmarks for coding-agent autonomy.

Details:
- The talk criticizes autonomy-duration claims that say a model can run for 30-60 hours without also saying whether the resulting code was good. (06:05-06:16)
- swyx summarizes the evaluation gap as "autonomy without accountability": autonomy is not enough when output quality, safety, and maintainability remain unreported. (06:16-06:23)
- Code slop is presented as more than messy code; a small number of engineers or agents can create disproportionate tech debt, and serious failures can expose private user data. (05:44-05:57)
- Practical autonomy reporting should therefore include code-quality evidence, tests, review findings, security checks, maintainability costs, and whether humans can still understand and own the change.
- **A clean worked example of the omission this page warns about.** Garvin's demo shows an agent independently provisioning a customer, building a multi-pool credit model, and generating a draft invoice from one sentence, and reports zero quality evidence: no attempt count, no correction, no comparison against the pricing page being replicated, no failure rate across the "multiple different versions of this" he says were run. The autonomy is real and demonstrated; the accuracy is asserted by looking at the screen. The architecture is still worth copying — but the sandbox boundary is doing the work that quality accountability would otherwise have to. ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 13:17-13:19, 15:41-15:51)

- **A target state defined by unattended hours, and the quality column it leaves blank.** Amazon's "frontier developer" is defined behaviourally — writes "maybe 1 to 2% of the code that they produce," gets the assistant "to run for up to hours at a time without their intervention," and runs "multiple agents in parallel churning through a backlog of tasks" — and the pilot outcomes are reported as commits and "deployment velocity to production." No defect rate, revert rate, incident count, or review-effort figure appears anywhere in the talk, so the autonomy claim and the throughput claim are both made without the accountability half. What the source does supply is a quality *bar* in the workflow rather than in the reporting: the agent should return only "when it actually runs and compiles and passes tests, when it's testable, when it actually has high coverage." That is a real gate, and it is still an input condition, not evidence about the code that shipped. ([Liguori](../sources/20260828_pqlWNihgdjI.md), 01:43-02:20, 06:36-07:06, 12:09-12:24)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Separate watched and unwatched agent time horizons](separate-watched-and-unwatched-agent-time-horizons.md)
- [Reliability thresholds determine whether coding agents save time](reliability-thresholds-determine-whether-coding-agents-save-time.md)
- [Keep critical code inside human understanding and review capacity](keep-critical-code-inside-human-understanding-and-review-capacity.md)
- [Let the Agent Reach a Test Environment, Not Production, When the Domain Carries Money](let-the-agent-reach-a-test-environment-not-production.md)
- [Being in the Loop Is the Ceiling on Agent Parallelism](being-in-the-loop-is-the-ceiling-on-agent-parallelism.md)

Sources:
- [No More Slop - swyx](../sources/20251222_IoiHI7p12Ao.md), 05:44-06:23
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 13:17-13:19, 15:41-15:51
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 01:43-02:20, 06:36-07:06, 12:09-12:24
