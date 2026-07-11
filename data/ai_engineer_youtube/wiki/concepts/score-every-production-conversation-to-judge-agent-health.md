# Score Every Production Conversation to Judge Agent Health

Summary: To recover the "feel" for a shipped agent, run a session-analyzer that LLM-scores *every* production conversation (not a sampled few) into a system-health dashboard, connecting the dots across sessions into high-level patterns — a zoom-out monitoring loop distinct from the fast per-incident fix loop.

Use when:
- You have lost visibility into whether a live agent is getting better or worse across thousands of sessions.
- You want an aggregate health signal and recurring failure patterns, not just point fixes.
- Choosing between per-incident monitoring and periodic system-level review.

Details:
- Motivation: the fast log-monitoring loop only sees a ~one-hour window with "no high-level understanding," so a second, zoomed-out system is needed to keep a hand on the pulse. (12:22-12:52, 08:46-09:04)
- The session analyzer scores every conversation (running many state agents and spending a lot of tokens) to detect patterns, connect the dots, surface logical problems, and produce a single system-health score — "visibility was impossible before the agent." (12:22-13:12)
- Scoring every session (not a sample) is the point: it lets you "watch across hundreds of conversations" and rank/score each one with a detailed per-session explanation of what needs attention. (13:12-15:51)
- The health dashboard surfaces: sessions analyzed, cost, average score, success rate, trends, sentiment analysis, tool-call analytics (and rejection reasons), score distribution, and — most importantly — AI insights that connect the dots into patterns, each with a description, why it matters, root cause, sessions affected, and a recommended fix. (13:32-15:02)
- Cadence and scope: its goal is high-level understanding, not fixing a specific bug, so run it roughly once or twice a week rather than continuously. (15:51-16:12, 09:04)
- Build-vs-buy: other tools provide similar systems, but Wandero built theirs in-house "because I know what I'm interested in, what I'm looking for." (16:12-16:33, 13:32-13:44)

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

Sources:
- [The Missing Layer After Launch - Raphael Kalandadze, Wandero AI](../sources/20260705_kZsf_Sfm7RU.md), 12:22-16:33
