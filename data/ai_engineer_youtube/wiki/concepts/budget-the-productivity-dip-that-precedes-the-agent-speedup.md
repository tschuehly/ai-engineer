# Budget the Productivity Dip That Precedes the Agent Speedup

Summary: Across Amazon's pilot interviews, "almost every team" reported that productivity *fell* while they intentionally changed how they worked, because brownfield codebases need engineering investment before agents succeed in them. The organizational failure is not the dip itself but a leadership layer that reads it as underperformance and demands the speedup first.

Use when:
- A team two months into an agent rollout is shipping less and someone is asking why.
- Planning the sequencing and the roadmap cost of an agent-adoption program in an existing codebase.
- Deciding what specifically to spend the pre-work window on.

Details:
- **The reported pattern.** "In almost every team that was interviewed, they reported that their productivity actually went down as they intentionally adopted a new way of working. That's counterintuitive, right? You have to do intentional engineering work before you're going to see that hockey stick curve in productivity improvement." ([Liguori](../sources/20260828_pqlWNihgdjI.md), 09:39-10:02)
- **Why brownfield is where it bites.** "We have to do real work in our code base first for agents to be successful there, especially in brownfield existing code bases" — and Amazon's 50-team pilot was deliberately all brownfield, "existing systems with existing code bases. Nothing green field," which is what makes the dip a general expectation rather than a story about one messy repo. (10:02-10:10, 06:04-06:19)
- **The inventory of what the window is spent on**, in the order she gives it: build the agent context up; "improve existing tools error messages so that the model knew what was going on when it failed"; build "new tools, new MCP servers for helping that model to actually get done what it needed to get done"; and restructure "their code base so that agents could actually navigate it more easily." Error messages are first and are the most transferable item — they are the channel through which an agent learns what went wrong, and most codebases have never been asked to make them legible to a non-human reader. (10:10-10:32)
- **The extreme case, offered with its own hedge.** "I've even seen drastic changes like changing the programming language of the code base… often I've seen teams struggle with Python, with JavaScript because they're untyped languages. It's hard to test. There's no compiler errors. So the model kind of guesses and gives it back to you. And so I've seen teams moving to TypeScript. Rust has become very popular inside of Amazon. The compiler gives great error messages." She immediately adds "you don't have to do that." The selection criterion is worth extracting even if the rewrite is not: what these teams are buying is a *machine-readable failure signal*, which is the same thing the error-message work buys, applied at the language level. (10:32-11:08)
- **The organizational half, which is the part that actually fails.** Liguori names it as a leadership behaviour and includes herself: "I've been guilty of this myself. My fellow leaders have been guilty of… saying, 'Well, you have the AI tools now and the models are so amazing now. Why are you not going faster?' And that's because you have to take those two months to invest in your code base, to figure out the best practices for your team, to make hard habit changes on your team." The external pressure is named too — "we're seeing all of these companies on X saying how they're shipping 20 PRs a day." A dip that nobody has agreed to fund gets abandoned halfway, which is worse than not starting: the team pays the investment cost and keeps the old workflow. (17:02-17:54)
- **What this predicts about mid-rollout metrics.** Any dashboard that samples during the window will show the change failing. If the pre-work is real, the metric you are watching is the one that has to fall first — so the commitment has to be made in advance, on a stated horizon ("those two months"), rather than re-litigated monthly against the number.
- **Distinguish from the correlational version.** That clean codebases amplify AI gains is a *cross-sectional* claim about which teams do better. This is the *temporal* claim about the transition between the two states, and it carries the cost that the cross-sectional version leaves out.
- Provenance: interview self-report from teams participating in an internal pilot, aggregated as "almost every team." No magnitude, duration, or recovery time is given for the dip; "those two months" is a leader's rule of thumb, not a measured window. No team is reported to have taken the dip and failed to recover, which is exactly the case that would price the risk.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Product Strategy](../topics/product-strategy.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Codebase Hygiene Amplifies AI Productivity Gains](codebase-hygiene-amplifies-ai-productivity-gains.md)
- [Agent-Legible Codebases Reduce Generated-Code Entropy](agent-legible-codebases-reduce-generated-code-entropy.md)
- [Treat Agent Readiness as Verification Infrastructure](treat-agent-readiness-as-verification-infrastructure.md)
- [Own Agent Adoption at the Leadership Layer Because the Fixes Are Shared](own-agent-adoption-at-the-leadership-layer-because-the-fixes-are-shared.md)
- [Run a Time-Boxed Roadmap Pause to Shift AI Work Habits](run-a-time-boxed-roadmap-pause-to-shift-ai-work-habits.md)
- [Stage Productivity Pilots to Strip One Confound at a Time](stage-productivity-pilots-to-strip-one-confound-at-a-time.md)

Sources:
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 06:04-06:19, 09:39-11:08, 17:02-17:54
