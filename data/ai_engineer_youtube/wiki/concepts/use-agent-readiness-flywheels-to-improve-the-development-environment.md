# Use Agent Readiness Flywheels to Improve the Development Environment

Summary: Agent adoption improves when organizations use agents to harden the environment that future agents depend on. Better linters, tests, docs, instructions, and readiness measurement create a feedback loop where agents become more useful because the development environment becomes more explicit.

Use when:
- Planning a repository-readiness program for coding agents.
- Choosing between buying another coding tool and improving the shared validation and instruction surface used by every tool.

Details:
- Tool comparisons and benchmark deltas are less durable than organizational practices that make many coding agents succeed, such as validation criteria and developer-liked workflows (07:07-07:35).
- Agents cannot reliably invent organization-specific validation criteria without source material; teams need documentation for AI systems, explicit lint and test commands, and instruction files such as `AGENTS.md` that encode how software should be built and reviewed (08:26-10:08).
- Organizations can assess readiness across validation pillars such as linter quality, instruction coverage, tests, and measurable usage outcomes, then identify whether weaker users or teams are blocked by missing validation rather than by lack of effort (09:47-10:37).
- Coding agents can help improve readiness by finding weak lint rules, generating tests, and creating patterns that later agents notice and follow; imperfect tests can be useful starting points when they pass for intended behavior and fail for some wrong behavior (11:07-11:52).
- The development-experience flywheel is that better agents improve the environment, the improved environment makes later agents better, and the reclaimed time funds further environment work (11:54-12:18).
- Highly autonomous bug-to-fix-to-approval loops are technically feasible, but the limiting factor is whether the organization has strong validation criteria rather than whether the agent can produce code at all (13:49-14:35).

- **The flywheel has a negative first turn, and someone has to fund it.** Amazon's pilot teams report the environment work costing output before returning any: "in almost every team that was interviewed, they reported that their productivity actually went down as they intentionally adopted a new way of working… You have to do intentional engineering work before you're going to see that hockey stick curve." Their inventory matches this page's — agent context, error messages the model can read on failure, new tools and MCP servers, codebase restructuring — but Liguori adds the organizational precondition the flywheel framing omits: leaders have to accept the dip rather than ask "why are you not going faster?", because "you have to take those two months to invest in your code base." ([Liguori](../sources/20260828_pqlWNihgdjI.md), 09:39-10:32, 17:02-17:54)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Treat agent readiness as verification infrastructure](treat-agent-readiness-as-verification-infrastructure.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Agent rules should emerge from observed off-rail behavior](agent-rules-should-emerge-from-observed-off-rail-behavior.md)
- [Budget the Productivity Dip That Precedes the Agent Speedup](budget-the-productivity-dip-that-precedes-the-agent-speedup.md)

Sources:
- [Making Codebases Agent Ready - Eno Reyes, Factory AI](../sources/20251222_ShuJ_CN6zr4.md), 07:07-14:35
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 09:39-10:32, 17:02-17:54
