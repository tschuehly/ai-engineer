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
- Deep agentic coding turns writing into reading and can make every engineer primarily a code reviewer, while agent-generated PR volume makes review itself a scaling bottleneck (09:44-10:45).
- Review load should be assigned to specific people, distributed by a system, and governed by SLOs or other enforcement mechanisms; broadcasting review requests to a team channel often overloads the one most responsive reviewer (11:56-12:42).
- Review systems need clear turn-taking because PR comments, responses, and follow-up pushes can otherwise depend on out-of-band Slack messages to tell reviewers when action is needed (12:42-13:14).
- The best reviewers should teach review quality through apprenticeship; when senior reviewers spend all their time in meetings, junior engineers do not learn the judgment needed to maintain quality under higher agentic throughput (14:10-14:49).
- The Qodo talk adds a volume-based failure mode: if AI produces more tasks, more PRs, and similar bugs per line, total bug and review load can grow even without proving AI-generated code is worse per line. (08:11-09:09)
- Volkov (ThursdAI) names this "human review is the new bottleneck" and grounds it in production data. Faros AI's April 2026 survey of 22,000 engineers ("the acceleration whiplash") reports an 861% increase in code deletion per PR alongside a 31% increase in PRs merged with no review at all — human or agentic — and a 242% increase in incidents per PR, while a second study finds bugs per developer up 6x vs 2025; "output does not mean stability." (ZpK5PWX2YRM 09:10-10:59)
- Anthropic's recursive-self-improvement essay makes the mechanism explicit via Amdahl's law: as engineers 10x–1000x their output, human code review becomes the blocking stage; neither Anthropic nor OpenAI removes the human, so the fix is to move review up a layer (encode caught bug-classes as docs/linters/reviewers), not to skip it. (ZpK5PWX2YRM 11:44-11:46)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Limit agent change size by feedback speed](limit-agent-change-size-by-feedback-speed.md)
- [Coding agents shift engineering work toward planning and review](coding-agents-shift-engineering-work-toward-planning-and-review.md)
- [Do not use token volume as a developer productivity metric](do-not-use-token-volume-as-a-developer-productivity-metric.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Route each change to the proof it needs](route-each-change-to-the-proof-it-needs.md)

Sources:
- [The Friction is Your Judgment - Armin Ronacher & Cristina Poncela Cubeiro, Earendil](../sources/20260418__Zcw_sVF6hU.md), 03:35-07:10
- [Developer Experience in the Age of AI Coding Agents - Max Kanat-Alexander, Capital One](../sources/20251223_rT2Del5pwg4.md), 09:44-14:49
- [The State of AI Code Quality: Hype vs Reality — Itamar Friedman, Qodo](../sources/20251211_rgjF5o2Qjsc.md), 08:11-09:09
- [Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI](../sources/20260710_ZpK5PWX2YRM.md), 09:10-11:46
