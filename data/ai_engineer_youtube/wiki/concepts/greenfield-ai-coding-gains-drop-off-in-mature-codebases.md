# Greenfield AI Coding Gains Drop Off in Mature Codebases

Summary: Enterprise AI coding rollouts can show early gains on proofs of concept, tests, and one-off scripts, then lose measurable impact when teams move into mature codebases where verification, review, merge latency, and system complexity dominate.

Use when:
- Evaluating whether AI coding productivity gains are coming from toy or greenfield work.
- Planning AI adoption for large codebases with existing architecture, dependencies, and review constraints.

Details:
- Bloomberg started broad AI coding adoption by releasing capabilities so teams could try tools and measure impact rather than guessing which products would help. (03:55-04:43)
- Surveys showed faster proofs of concept, tests, and one-time script generation, but measurements dropped quickly once work moved beyond greenfield scenarios. (04:49-05:15)
- Mature codebases make raw code generation risky because system complexity grows with the amount of live software assets, and teams still need care around what changes are applied. (05:30-06:10)
- AI rollout increased average open pull requests and time to merge because more code still had to be reviewed and merged by humans. (08:07-08:23)
- Qualification: the drop-off may be a feedback-loop problem more than an inherent property of mature code. Lajili (Poolside) argues the real greenfield/brownfield difference is that the agent's intuition is correct on greenfield but hits "dragons" (dead ends, unused code, unseen parts) on brownfield — and reports legacy success when the agent has a strong self-verification loop, so a bespoke "eyes" tool can recover much of the lost gain. ([Your agent is blindfolded](../sources/20260708_iRcX54EO5g8.md), 00:42-02:46)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [AI output speed can overwhelm review capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Measure AI engineering impact across utilization, impact, and cost](measure-ai-engineering-impact-across-utilization-impact-and-cost.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Reproduce the Bug Before Fixing to Earn Agent Trust](reproduce-the-bug-before-fixing-to-earn-agent-trust.md)

Sources:
- [What We Learned Deploying AI within Bloomberg's Engineering Organization - Lei Zhang, Bloomberg](../sources/20251216_Q81AzlA-VE8.md), 03:55-08:23
- [Your agent is blindfolded — Johan Lajili, Poolside AI](../sources/20260708_iRcX54EO5g8.md), 00:42-02:46
