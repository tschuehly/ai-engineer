# AI Output Speed Can Overwhelm Review Capacity

Summary: Coding agents can increase code production faster than teams increase responsible review capacity. The resulting pressure turns "one more prompt" into large pull requests, rubber-stamped reviews, and loss of time for architectural judgment.

Use when:
- Reviewing whether generated-code throughput is outpacing human review.
- Designing coding-agent workflows, PR limits, or team review policies.

Details:
- The speakers describe the adoption shift from AI tools creating useful extra time to AI use becoming the baseline expectation, which turns speed into pressure to ship more code. (03:35-04:23)
- Fast output can trick engineers into feeling more efficient while reducing the time available to stop, decide whether the implementation approach is right, and keep the agent from reading or changing irrelevant files. (04:52-05:27)
- Code production and code review used to be more balanced; with agents, each engineer gains much more producing power than reviewing power, and more humans outside engineering can now create code while responsibility still stays with the engineering team. (05:32-06:43)
- Large generated pull requests are a trap: the moment a 5,000-line diff needs the most thinking is also the moment reviewers are most likely to feel overwhelmed and tap out. (06:45-07:10)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Limit agent change size by feedback speed](limit-agent-change-size-by-feedback-speed.md)
- [Coding agents shift engineering work toward planning and review](coding-agents-shift-engineering-work-toward-planning-and-review.md)
- [Do not use token volume as a developer productivity metric](do-not-use-token-volume-as-a-developer-productivity-metric.md)

Sources:
- [The Friction is Your Judgment - Armin Ronacher & Cristina Poncela Cubeiro, Earendil](../sources/20260418__Zcw_sVF6hU.md), 03:35-07:10
