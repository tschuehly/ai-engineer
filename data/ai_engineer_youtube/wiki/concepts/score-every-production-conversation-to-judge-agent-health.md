# Score Every Production Conversation to Judge Agent Health

Summary: To recover the "feel" for a shipped agent, run a session-analyzer that LLM-scores *every* production conversation (not a sampled few) into a system-health dashboard, connecting the dots across sessions into high-level patterns — a zoom-out monitoring loop distinct from the fast per-incident fix loop.

Use when:
- You have lost visibility into whether a live agent is getting better or worse across thousands of sessions.
- Evals are currently a pre-launch checklist and you need a signal that keeps working after the gate is passed.
- You want an aggregate health signal and recurring failure patterns, not just point fixes.
- Choosing between per-incident monitoring and periodic system-level review.

Details:
- Motivation: the fast log-monitoring loop only sees a ~one-hour window with "no high-level understanding," so a second, zoomed-out system is needed to keep a hand on the pulse. (12:22-12:52, 08:46-09:04)
- The session analyzer scores every conversation (running many state agents and spending a lot of tokens) to detect patterns, connect the dots, surface logical problems, and produce a single system-health score — "visibility was impossible before the agent." (12:22-13:12)
- Scoring every session (not a sample) is the point: it lets you "watch across hundreds of conversations" and rank/score each one with a detailed per-session explanation of what needs attention. (13:12-15:51)
- The health dashboard surfaces: sessions analyzed, cost, average score, success rate, trends, sentiment analysis, tool-call analytics (and rejection reasons), score distribution, and — most importantly — AI insights that connect the dots into patterns, each with a description, why it matters, root cause, sessions affected, and a recommended fix. (13:32-15:02)
- Cadence and scope: its goal is high-level understanding, not fixing a specific bug, so run it roughly once or twice a week rather than continuously. (15:51-16:12, 09:04)
- Build-vs-buy: other tools provide similar systems, but Wandero built theirs in-house "because I know what I'm interested in, what I'm looking for." (16:12-16:33, 13:32-13:44)
- **Hinge Health runs the same pattern as a safety layer, and makes the "live traffic, not a golden set" distinction explicit.** "Most teams treat evals as a pre-launch checklist. You run your tests, you ship, you move on. That's necessary, of course, but that's hardly enough. What actually holds up in production is judges that continuously keep scoring real conversations as they happen. Not a saved golden data set. Live traffic." ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 09:35-10:14)
- **Three signal sources, each catching something the others miss.** Automated judges — "30, 40, name it, as much as you can scale" — on always-refreshing dimensions (clinical accuracy, safety, escalation, relevance, drift, refusal) catch regressions and "even sensitive drops in quality." Member feedback, thumbs up/down "on each and every single message," is "the truth signal… the only one that comes straight from the person that you're serving it to," and catches tone problems judges miss. Sampled traces are "random samples spread across capabilities with high-stake cases checked every single time, 100% sampling on those" — so sampling rate is set by stakes, not by budget alone. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 10:16-11:25)
- **A new production failure is a new judge, so judge count is a scaling axis.** Some failures resist prompt fixes: "you ship the fix, it comes back under new conditions. New prompts, new tools, the model shifts. You ship the fix again. Each round buys you less and less. The rate never hits zero." Hence "monitoring is not a last resort. It is the first resort, which is always on," and "a new failure that you see in production simply means you now have a new judge" — the architecture has to keep absorbing judges as the user base grows. The framing: "monitoring is how you know that the architecture is still holding," compressed as "don't gate what you can monitor." ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 11:49-12:37, 20:38-20:40)
- **The ceiling is human, not compute.** "People are going to catch what no single metric is going to catch," and "the bottleneck is not the compute, the models, the capability. It's actually having enough people to read the signal and act on it." Scoring everything is cheap; interpreting it is the scarce resource that has to be staffed before the judges are added. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 11:25-11:48)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Operate Agent Products as the Missing Post-Launch Layer](operate-agent-products-as-the-missing-post-launch-layer.md)
- [Staff Agent Operations With a Team of Agents](staff-agent-operations-with-a-team-of-agents.md)
- [Apply Online Scoring to Production Traces With Cost-Aware Sampling](apply-online-scoring-to-production-traces-with-cost-aware-sampling.md)
- [Analyze operational health over time slices before invoking repair agents](analyze-operational-health-over-time-slices-before-invoking-repair-agents.md)
- [Choose Eval Scope Across Span, Multispan, Trajectory, and Session](choose-eval-scope-across-span-multispan-trajectory-and-session.md)
- [Check Whether the Judge Is Right Before Changing the Agent](check-the-judge-before-changing-the-agent.md)

Sources:
- [The Missing Layer After Launch - Raphael Kalandadze, Wandero AI](../sources/20260705_kZsf_Sfm7RU.md), 12:22-16:33
- [Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health](../sources/20260819_YXEqC05WEI0.md), 09:35-12:37, 20:38-20:40
