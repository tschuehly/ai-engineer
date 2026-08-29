# Measure AI Transformation by Outcomes Instead of Adoption

Summary: AI transformation measurement should connect tool investment and enablement to delivery, quality, developer experience, resilience, and economic outcomes. Adoption breadth and usage are intermediate signals, not proof that the operating model improved.

Use when:
- Designing executive dashboards for AI-assisted engineering transformation.
- Diagnosing why higher AI-tool usage did not translate into enterprise productivity.

Details:
- A rollout can add users and still produce no overall impact if people use tools suboptimally or do not change expectations, upskilling, habits, and workflow integration. (16:32-17:48)
- The talk says robust measurement should prioritize outcomes, not just adoption, because it helps monitor progress, find issues, and course-correct quickly. (18:31-18:43)
- Bottom-performing enterprises in the cited survey often lacked basic outcome measurement: the speakers say they were not measuring speed, and only 10% were measuring productivity. (18:43-18:52)
- The proposed measurement chain starts from inputs such as investment in coding tools, other AI tools, upskilling, and change management, then connects those to adoption, velocity, capacity, developer NPS, craft satisfaction, security, quality, resilience, and economic outcomes. (18:53-20:24)
- Mean time to resolve priority bugs is given as one proxy for software resilience in an AI engineering measurement system. (19:38-19:51)
- **Where the outcome is a physical event, the measurement problem largely dissolves — and that is unusual.** Shenoy's outcome metrics for operated services businesses are "did the roof get repaired? Did the books get closed?" — settled by the world rather than by a dashboard definition, which is why he can treat the same signal as an eval label and as a transformation metric at once. The transferable point is diagnostic: if you cannot name the physical or financial event that settles whether the agent's work succeeded, you are probably about to measure adoption instead. The costs are coarseness and delay, not ambiguity. ([Shenoy](../sources/20260828_B0fjR3yaZFU.md), 11:08-11:49)

- **A case where an adoption metric would have shown nothing at all.** In Amazon's 50-team pilot "90% of these teams used Kiro, among other internal tools that we have" — tool adoption was near-uniform — while deployment-velocity outcomes split in half, under 3x versus a median of 4.5x. Any dashboard counting licenses, seats, or active users would have reported a successful rollout across both halves. Liguori's substitute for an adoption metric is a *behavioural* target state, which is a leading indicator an outcome metric cannot give you: frontier developers "write maybe 1 to 2% of the code that they produce," get their assistant "to run for up to hours at a time without their intervention," and "run multiple agents in parallel churning through a backlog of tasks." Those are observable without a survey, though the talk gives no method for measuring the 1-2% figure. ([Liguori](../sources/20260828_pqlWNihgdjI.md), 01:43-02:20, 06:50-07:34)
- **A caution about how far down the adoption metric can be demoted, and a worked example of the gap this page warns about.** Izmit's usage numbers are extensive — over a million questions, ~40,000 a week, ~6,000 users, >70% weekly retention at beta exit — while the business outcomes his talk opens with (book coverage, win rates, deal-cycle length, incremental revenue) carry no figures at all and no before/after comparison. That is precisely the intermediate-signal problem stated here. But his 20%-trial diagnostic shows that adoption breadth still earns a place on the dashboard for a different reason than proving value: it is the metric that decides whether the next sprint belongs to the product team or to change management, which no outcome metric can disambiguate. ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 00:25-00:43, 02:33-03:09, 07:34-07:53)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Measure AI engineering impact across utilization, impact, and cost](measure-ai-engineering-impact-across-utilization-impact-and-cost.md)
- [Do not use token volume as a developer productivity metric](do-not-use-token-volume-as-a-developer-productivity-metric.md)
- [Move enterprise AI adoption beyond spot experiments](move-enterprise-ai-adoption-beyond-spot-experiments.md)
- [Operational Outcomes Are Eval Labels You Only See If You Own the Operation](operational-outcomes-are-eval-labels-you-only-see-if-you-own-the-operation.md)
- [Stage Productivity Pilots to Strip One Confound at a Time](stage-productivity-pilots-to-strip-one-confound-at-a-time.md)
- [Separate the Did-Not-Try Problem From the Did-Not-Return Problem](separate-the-did-not-try-problem-from-the-did-not-return-problem.md)

Sources:
- [Moving away from Agile: What's Next - Martin Harrysson & Natasha Maniar, McKinsey & Company](../sources/20251212_SZStlIhyTCY.md), 16:32-17:48, 18:31-20:24
- [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../sources/20260828_B0fjR3yaZFU.md), 11:08-11:49
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 01:43-02:20, 06:50-07:34
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 00:25-00:43, 02:33-03:09, 07:34-07:53
