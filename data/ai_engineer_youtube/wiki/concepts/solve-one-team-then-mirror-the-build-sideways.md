# Solve One Team, Then Mirror the Build Sideways

Summary: Build a complete vertical for one team before generalizing, then extend horizontally by mirroring the pattern — and be explicit about what actually transfers. The pipeline plumbing (embeddings over emails and transcripts, durable execution, user custom instructions) carries over unchanged; the data sources and the skills do not, and they are the whole of the porting work.

Use when:
- Choosing between building a general internal agent platform and shipping one team's workflow end to end.
- Estimating what it costs to bring a second team onto a system that already works for the first.
- A platform proposal is stalling because it is being designed for every consumer at once.

Details:
- **The sequencing is stated as a policy.** "The way we tend to approach these problems is solve for one team first, then scale horizontally." The justification is workflow overlap: "you have a very overlapping set of problems… Everybody wants to do automated outbound. Everybody wants to prepare for meetings. Whereas certain teams may have problems or things that they do that are isolated to them, like QBR generation." Overlapping workflows are where mirroring pays; isolated ones stay verticals. ([Vaziri](../sources/20260826_VjEP0xqTUI0.md), 08:07-08:34)
- **What transfers, named concretely.** Moving the pre-meeting-brief build from account managers to account executives, the reusable parts are "email, call transcript embeddings, custom instructions, generalizable" — the ingestion and retrieval plumbing plus the user-authored format layer. (13:29-13:47)
- **What does not transfer, also named.** "If we're building this for AEs, we're handling pre-sales opportunities, we need to focus more on third-party data instead of a bunch of product data that we have already, and that needs to be incorporated into our customer data platform. The skills need to reference a different set of information that we have on the people that we're trying to sell to." Pre-sales has no product usage to read, so the data sources swap and every skill written against them has to be rewritten. Horizontal extension "is mainly an exercise of creating specific skills, data integrations, and just data ingestion itself." (13:47-14:09)
- **The vertical is what teaches you the shape.** From the Q&A: "by doing these things and solving these problems, you get a really good understanding of how this works, how it could extend to other teams." The two-person origin — GPT-3.5 writing personalized copy into outbound sequences three years earlier — is offered as the model for a small team, not as a stage to skip. (18:56-19:21)
- **The anti-pattern is explicit.** "The reality is that you can't spend a year going and building some really complicated system architecture that is perfect. So you have to piece together the vertical solutions and then stick them together." Note that this is the closing advice of a talk whose middle fifteen minutes describe a platform — the platform is presented as the residue of the verticals, not their precondition. (19:26-19:36)
- **The corollary for the layer above.** These verticals are claimed to be the substrate for multi-channel distribution: "these vertical builds that we're creating are the foundation of multi-team, multi-channel distribution," because an intent can only be fanned out into channels that already have a working generator behind them. (15:45-15:53)
- **Limit.** No cost is given for either the first vertical or any subsequent mirror, so the claim that horizontal extension is cheaper is untested; and the talk describes exactly one vertical in detail, with the account-executive port described prospectively.

Related topics:
- [Workflows](../topics/workflows.md)
- [Go To Market](../topics/go-to-market.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Distribution Is the Bottleneck, Not the Idea](distribution-is-the-bottleneck-not-the-idea.md)
- [Start Customer-Facing Agents With Narrow, Valuable Outcomes](start-customer-facing-agents-with-narrow-valuable-outcomes.md)
- [Shadow Your Best Human Before Encoding the Workflow](shadow-your-best-human-before-encoding-the-workflow.md)
- [Let Users Author the Output Format as a Skill](let-users-author-the-output-format-as-a-skill.md)
- [Expose the Background Agents' Tool Surface to Employees Over MCP](expose-the-background-agents-tool-surface-to-employees-over-mcp.md)
- [Gate Each Rollout Phase on a Different Question](gate-each-rollout-phase-on-a-different-question.md)
- [Layer Ask, Push, and Self-Serve Because Teams Interface Differently](layer-ask-push-and-self-serve-because-teams-interface-differently.md)

Sources:
- [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](../sources/20260826_VjEP0xqTUI0.md), 08:07-08:34, 13:29-14:09, 15:45-15:53, 18:56-19:36
