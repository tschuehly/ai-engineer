# Budget a Third of Sprint Capacity for Re-Architecture

Summary: When the platform layer under an agent is changing every few months, re-architecture is not technical debt to be avoided but a standing line item. One team that shipped an internal assistant to 6,000 users runs 60-70% of sprint capacity on features and quality and 30-40% on rebuilding onto new primitives, and reports that 80% of its current architecture does not match the plan it launched against.

Use when:
- A team is evaluating frameworks and platforms instead of shipping.
- Planning capacity for an agent product whose underlying platform is releasing new primitives.
- Justifying a rewrite of a component that was correct when it was written.
- Deciding how much architecture to commit to before there are any users.

Details:
- The anti-pattern he names in enterprises: "they are still trying to purchase that perfect architecture. They're trying to test different frameworks. They're trying to see how the technology is maturing. But the thing that they don't do is they don't build, and then they don't launch, and they don't learn." ([Izmit](../sources/20260826_DrTdD-ttjCY.md), 11:45-12:11)
- **The launch configuration is the argument.** "When we first launched the agent, it was a nine-page long agent instructions. It was a couple of Cortex Analyst tools, semantic views. It was a Cortex Search service for our unstructured data. And we were managing the agent instructions versions out of a Google Doc. That's how we launched it. To 6,000 people." A version-controlled prompt pipeline was not a launch prerequisite; the quality of the answers was ([Choose Quality Over Coverage](choose-quality-over-coverage-because-the-first-five-answers-decide-adoption.md)). (12:11-12:34)
- **Everything after arrived in a forced order, each item triggered by a limit rather than a plan.** Google Doc versioning broke, so CI/CD. Then eval infrastructure "with all the unit test, routing test." Business processes and workflows stopped fitting in the agent instructions, so a skill library. MCP servers arrived, which needed their own orchestration instructions, which hit the agent-instruction size limit, which forced progressive disclosure. Then user memory, task scheduling, and a Slack interface beyond the chat screen. Each step is a response to a symptom the previous configuration produced. (12:35-13:16)
- The plan-versus-outcome comparison: against the original PRD and architecture diagram, "80% of it doesn't match" the architecture now running. (13:17-13:25)
- **The capacity split is the transferable artifact.** "If you look at our sprints, maybe 60-70% of the work we are doing is adding new features, improving quality, and all kinds of things. But 30-40% of the work is that we are constantly re-architecting with the new technology." Naming it as a share of committed capacity converts a recurring interruption into a plannable cost, and makes visible when it is being borrowed from feature work.
- The posture that follows: "you shouldn't be too much tied to your architecture. You should be okay to pivot very easily so that you can double down on these new capabilities… don't over-invest in the current architecture. Just make sure that you keep your flexibility." With a pace argument attached: "the longer you wait, the more you lose towards your competition, because if your competition is doing these kind of things 3-4 months ahead of you, that means they're also getting more customers." (13:41-14:06, 17:33-17:57)
- Scope note: this reasoning holds where the *platform* underneath is moving — new agent primitives, protocol support, memory, scheduling. It is not a general license to skip architecture; the components this team added are mostly ones that a stable-platform team would have had from the start, and the cost of getting them late is paid in the interim, unmeasured.
- Limits: "80%" and the 30-40% share are recollections, not a measured breakdown of committed work, and no incident, outage, or rework cost from launching without CI/CD or evals is reported — the account is written entirely from the winning side. The team is also customer zero for the platform it re-architects onto, so it learns about new primitives earlier and cheaper than an outside adopter would. ([Provenance and Limits](../sources/20260826_DrTdD-ttjCY.md))

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)
- [Context Engineering](../topics/context-engineering.md)
- [Agents](../topics/agents.md)

Related concepts:
- [The Wow Factor Collapses Into a Baseline Within Months](the-wow-factor-collapses-into-a-baseline-within-months.md)
- [Agent Skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Skills Are the Residual Where Organizational Know-How Lands](skills-are-the-residual-where-organizational-know-how-lands.md)
- [Choose Quality Over Coverage Because the First Five Answers Decide Adoption](choose-quality-over-coverage-because-the-first-five-answers-decide-adoption.md)
- [Plugin architectures let agent systems absorb experiments](plugin-architectures-let-agent-systems-absorb-experiments.md)
- [Operate Agent Products as the Missing Post-Launch Layer](operate-agent-products-as-the-missing-post-launch-layer.md)

Sources:
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 11:45-14:06, 17:33-17:57
