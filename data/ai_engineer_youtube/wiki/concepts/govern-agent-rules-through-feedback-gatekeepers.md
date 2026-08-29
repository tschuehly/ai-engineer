# Govern Agent Rules Through Feedback Gatekeepers

Summary: Shared agent instructions should have an explicit owner or group that receives feedback, maintains the rules, and keeps system prompts aligned with current engineering practice.

Use when:
- Establishing ownership for `AGENTS.md`, Cursor rules, system prompts, or other agent-control files.
- Deciding how to update shared prompt context after recurring model failures or stale framework guidance.

Details:
- The talk groups system prompts, Cursor rules, and agent Markdown as mainstream mechanisms for controlling model and agent behavior. (11:18-11:31)
- A Spring Boot example illustrates why rule files need maintenance: models may keep suggesting older framework patterns when the organization wants current Spring Boot 3 guidance. (11:36-11:46)
- Reock recommends a gatekeeper or group that receives feedback and understands how to maintain and continuously improve shared system prompts. (11:48-11:58)
- The reason for governance is organization-wide effect: shared prompts shape how assistants, models, and agents behave across the business. (11:58-12:04)
- The same section cautions that generation settings such as temperature should be chosen by use case, with more deterministic settings for repeatability and higher settings for divergent creative solutions. (12:07-13:25)

- **An alternative to a central gatekeeper for organizations where one cannot exist, plus the part that must stay central anyway.** At Uber's scale a gatekeeper is ruled out by construction: "with hundreds of teams across the company, we can't have centralized management of our code reviews, our customizations, and our rules, and even the knowledge that goes into those code reviews." What replaces it is telemetry returned to the author — addressal rate, reply sentiment, and agent trajectory per rule, so "the teams could actually understand that 'Oh, I wrote this rule, but maybe not a lot of developers are liking it in my team, so let me go and update it.'" Governance becomes a feedback path rather than an approval queue. The exception is checks that may not be skipped: "we can't rely on teams hoping to run the code review skill that happens," so security and compliance stay centrally mandated and run on everything. ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 02:04-02:25, 02:43-02:57, 09:16-09:43)
- **The gatekeeper role, named by function rather than by process.** Touil's answer to who arbitrates is an explicit list of standing roles — "your architects, your engineer leads, infra leads etc, and cyber leads actually sitting down owning part of those domains and making sure that the skills we need to get updated is actually according to the policies you want to adhere" — preceded by the concession that motivates it: "this is where technology stop solving the problem." ([Touil](../sources/20260828_M05vON8i0aI.md), 14:47-15:17) The three constituencies map onto the three ways a shared rule can be wrong: architecturally misplaced, operationally unrunnable, or unsafe to grant. Asserted with no deployment behind it, and it is also the shape of the transformation work the speaker's firm sells.

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [System prompt learning updates agent rules from eval explanations](system-prompt-learning-updates-agent-rules-from-eval-explanations.md)
- [Treat prompts as distributed harness surfaces](treat-prompts-as-distributed-harness-surfaces.md)
- [Distributed Rule Authoring Is a Platform Problem, Not an Authoring Problem](distributed-rule-authoring-is-a-platform-problem.md)
- [Skill Composability Is Decided Before Authoring, Not in the Registry](skill-composability-is-decided-before-authoring-not-in-the-registry.md)

Sources:
- [Leadership in AI Assisted Engineering - Justin Reock, DX (acq. Atlassian)](../sources/20251219_PmZDupFP3UM.md), 11:18-13:25
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 02:04-02:25, 02:43-02:57, 09:16-09:43
- [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../sources/20260828_M05vON8i0aI.md), 14:47-15:17
