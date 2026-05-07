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

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Track user dissatisfaction alongside pairwise model preference](track-user-dissatisfaction-alongside-pairwise-model-preference.md)
- [Limit agent change size by feedback speed](limit-agent-change-size-by-feedback-speed.md)

Sources:
- [How AI is changing Software Engineering: A Conversation with Gergely Orosz, @pragmaticengineer](../sources/20260421_CS5Cmz5FssI.md), 01:17-04:41
- [From Vibe Coding To Vibe Engineering - Kitze, Sizzy](../sources/20251214_JV-wY5pxXLo.md), 20:48-21:04
