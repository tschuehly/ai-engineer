# Do Not Use Token Volume as a Developer Productivity Metric

Summary: Token count or AI spend is a weak proxy for useful engineering work and can create Goodharted behavior when tied to leaderboards, performance review, or adoption pressure.

Use when:
- Designing AI adoption dashboards or productivity metrics for engineering teams.
- Explaining why raw token spend should not be treated as evidence of impact.

Details:
- The source describes companies exposing AI token output or spend through leaderboards and lookup tools, after which engineers worried about being in the bottom cohort for usage. (01:17-03:14)
- Token metrics can be weaponized like any other performance data point: low impact plus low token use can be read as "not trying," while high impact plus high token use can be read as innovation even when the causal link is unclear. (02:03-02:39)
- The failure mode is concrete: engineers may ask agents to summarize documentation poorly or run autonomous agents to produce low-value work because those actions raise visible token counts. (03:00-03:27)
- The transcript compares token counting to lines-of-code and pull-request-count metrics, both of which encouraged optimization of output volume rather than valuable software outcomes. (04:18-04:41)
- A later source describes companies using token-burning leaderboards as visible career signals, which can reward adoption theater instead of validated engineering impact. (20:48-21:04)
- A Stanford ROI talk adds field-study evidence that token spend per engineer had only a loose correlation with productivity lift, with a directional "death valley" around mid-level token use where some teams did worse than lower-usage teams. (03:14-04:02)
- **"Percent of committed code from the model" is the same metric wearing better clothes.** Rizwan relays Uber's CTO reporting that after rolling out Claude, "95% of their engineers were using it, 70% of their committed code came from Claude, and their monthly spend per user was up to $2,000," with the entire 2026 budget consumed in four months. Adoption rate and generated-code share are the two figures a rollout naturally produces, and neither says anything about delivered value — the fourth number in the same sentence is the cost. The counter-evidence sits in this source too: on Cline's own head-to-head, the model that emitted more tokens produced the working build and the one that emitted fewer broke production, so volume did not even track code quality within a single task. Relayed second-hand from a slide. ([Rizwan](../sources/20260807_CoEIs6Xm8m8.md), 06:05-06:27, 09:45-10:05)
- **The one reading of token spend that survives this warning, and why.** Touil uses spend as a diagnostic on the *library* rather than a score on the engineer: without a skill for a recurring task, "someone is vibe coding back and forth and trying to figure out exactly how to steer the agent to implement it properly. That is burning more tokens from one side cost-wise, but also the productivity is spending more time rather than giving in one shot the right answer." ([Touil](../sources/20260828_M05vON8i0aI.md), 16:18-16:42) Three things keep this outside the Goodhart trap this page describes: the unit is a task class rather than a person, the direction is inverted (high spend for an ordinary outcome is the signal, so there is nothing to game upward), and the action it triggers is writing a skill rather than judging anyone. Attach it to a person or a leaderboard and it converts straight back into the metric this page warns against. Nothing in the talk is measured; the illustration is a self-authored simulation.

- **A worked metric ladder that stops one rung short.** Amazon's early frontier result was scored on commits — the Bedrock Mantle team "looked at commits" to claim "up to 20X improvement" — and the later 50-team pilot deliberately moved off it: "a productivity metric of deployment velocity to production. So, not just commits, how many commits are they producing, but how quickly are we getting changes out to customers?" That is a real improvement, since commits are an activity count and deployments are at least a delivery event. It is still an output proxy: nothing in the talk adjusts for defect rate, rework, revert rate, incident load, or the value of what shipped, and no quality outcome is reported anywhere. The general shape worth taking is that moving from activity to delivery is the easy half of this fix, and moving from delivery to outcome is the half most organizations skip. ([Liguori](../sources/20260828_pqlWNihgdjI.md), 03:20-03:23, 06:36-07:06)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Track user dissatisfaction alongside pairwise model preference](track-user-dissatisfaction-alongside-pairwise-model-preference.md)
- [Limit agent change size by feedback speed](limit-agent-change-size-by-feedback-speed.md)
- [Benchmark AI engineering practices by usage pattern](benchmark-ai-engineering-practices-by-usage-pattern.md)
- [Measure AI ROI with primary output and guardrails](measure-ai-roi-with-primary-output-and-guardrails.md)
- [A Subsidized Coding-Agent Subscription Is a Lock-In Ramp](a-subsidized-coding-agent-subscription-is-a-lock-in-ramp.md)
- [A Missing Skill Is Billed as Tokens, Not Recorded as a Gap](a-missing-skill-is-billed-as-tokens-not-recorded-as-a-gap.md)
- [Stage Productivity Pilots to Strip One Confound at a Time](stage-productivity-pilots-to-strip-one-confound-at-a-time.md)

Sources:
- [How AI is changing Software Engineering: A Conversation with Gergely Orosz, @pragmaticengineer](../sources/20260421_CS5Cmz5FssI.md), 01:17-04:41
- [From Vibe Coding To Vibe Engineering - Kitze, Sizzy](../sources/20251214_JV-wY5pxXLo.md), 20:48-21:04
- [Can you prove AI ROI in Software Eng? (Stanford 120k Devs Study) - Yegor Denisov-Blanch, Stanford](../sources/20251211_JvosMkuNxF8.md), 03:14-04:02
- [Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline](../sources/20260807_CoEIs6Xm8m8.md), 06:05-06:27, 09:45-10:05
- [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../sources/20260828_M05vON8i0aI.md), 16:18-16:42
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 03:20-03:23, 06:36-07:06
