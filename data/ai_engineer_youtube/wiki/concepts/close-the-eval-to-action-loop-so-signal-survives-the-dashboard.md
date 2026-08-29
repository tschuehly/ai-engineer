# Close the Eval-to-Action Loop So Signal Survives the Dashboard

Summary: Observability traces and eval pass/fail verdicts are captured but never reflected back into what the agent does, so the outcome signal "dies in the dashboard" and the agent starts every run from a blank slate. A runtime-experience layer should consume traces, absorb eval outcomes, and convert both into retrieval guidance for future runs — improving the agent while it executes, without retraining, fine-tuning, or manual prompt rewrites.

Use when:
- Your eval suite and observability stack capture everything but the agent keeps repeating the same mistake.
- You want an agent to improve from production outcomes without a fine-tune or a manual prompt-rewrite/redeploy cycle.
- Deciding whether lessons should be baked in at compile time or applied at runtime.

Details:
- The gap is a **missing layer between evals and action**: observability records every tool call, LLM completion, and exception, and the eval suite judges pass/fail, but that verdict is not reflected in the agent's context, skills, or actions — the agent has no access to why yesterday's runs passed or failed, so "the eval signal dies in the dashboard," 02:16-03:09.
- The manual alternative is an engineer reading dashboards and then rewriting the prompt, redeploying, upgrading to a more expensive model, restructuring the harness, or fine-tuning — slow, anecdotal, and unscalable across many agents, 03:17-03:36.
- The proposed fix ("Agent RX" / "agent runtime experience") is a runtime layer that consumes traces, absorbs eval outcomes, and converts both into **retrieval guidance** so the agent improves *while executing the task* — no retraining, fine-tuning, or manual prompt engineering, 03:09-05:14.
- Contrast with **compile-time** approaches "like DSPy" that bake all lessons into the prompt up front; here the lessons are applied and re-ranked at runtime instead, 05:01-05:14.
- Once enough outcome-labeled memories accumulate for a task (~10 memories / ~5 reviews), **bake the stabilized reasoning into a skill** the agent always calls, without changing the existing prompt — e.g. a product SQL agent whose system prompt still names a column that is no longer useful, which no system updates today, 06:44-08:02, 14:34-15:10.
- The retrieval side of this loop uses outcome-weighted ranking; see the companion concept for the mechanism that turns each run's pass/fail into a per-memory utility score.
- **A loop that closes through people rather than through runtime memory.** DoorDash's answer to signal dying in a dashboard is a human circuit: sample traces down, annotate them, promote a golden dataset, recalibrate the judge against it, and have the owning team "elevate that judge prompt as their LLM as a judge" before monitoring and repeating. The action taken is a promoted judge and a grown golden set rather than retrieval guidance injected at run time — slower, and it changes what the system is measured against rather than what it does. Worth reading as the complementary case: this page moves the lesson into the agent's execution path, that one moves it into the specification. ([AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 05:19-06:12, 11:14-11:24)
- **The business-system version of the same failure, named as "the naive version."** At Notion the alternative to a closed loop is stated concretely: "a data analyst coming in and trying to understand if the output of this could be better," replaced by "wiring our engagement history back into the decision layer so that the system decides whether or not to continue a thread, advance to the next step, or pivot." The enabling mechanism is attribution — "every action is a decision log and every outcome threads back to the decision that caused it" — and it is kept separate from step-level tracing, which serves workflow quality rather than decision quality. ([Liu](../sources/20260826_L4I7WgiEquo.md), 14:46-15:37)
- **The same death, one layer up: the insight dies in the dashboard before any agent is involved.** Cloudflare's argument for pushing a generated narrative is that KPI adoption is uneven — some people "are never going to look at" a dashboard — so a correct metric on an unopened page changes nothing. The fix is structurally identical to this page's: convert the artifact into something that reaches the consumer's workflow rather than waiting to be queried. The same source also shows the failure applied to its own quality signal: two to three months of reading every run produced no recorded defect taxonomy or regression suite, so that signal died in a person instead of a dashboard. ([Joyce](../sources/20260826_Qw_tC68KKes.md), 09:42-10:04, 11:41-11:55)

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Rank Agent Memory by Outcome Utility, Not Just Similarity](rank-agent-memory-by-outcome-utility-not-just-similarity.md)
- [Replace Anecdotal Agent Tuning With Eval and Observability Loops](replace-anecdotal-agent-tuning-with-eval-and-observability-loops.md)
- [Skills Turn Procedural Feedback Into Transferable Agent Memory](skills-turn-procedural-feedback-into-transferable-agent-memory.md)
- [Automate the Agent-Building Loop With an Agentic AI Engineer](automate-the-agent-building-loop-with-an-agentic-ai-engineer.md)
- [Show the Prompt Diff So a Non-Engineer Can Promote an Optimized Judge](show-the-prompt-diff-so-a-non-engineer-can-promote-an-optimized-judge.md)
- [Thread Every Outcome Back to the Decision That Caused It](thread-every-outcome-back-to-the-decision-that-caused-it.md)
- [Push the Narrative Because Dashboard Adoption Is Always Uneven](push-the-narrative-because-dashboard-adoption-is-always-uneven.md)
- [Read Every Run for Months Before Trusting an Unevaluatable Narrative](read-every-run-for-months-before-trusting-an-unevaluatable-narrative.md)

Sources:
- [User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch](../sources/20260628_Jx4ZFEAq6bY.md), 02:16-15:10
- [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 05:19-06:12, 11:14-11:24
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 14:46-15:37
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 09:42-10:04, 11:41-11:55
