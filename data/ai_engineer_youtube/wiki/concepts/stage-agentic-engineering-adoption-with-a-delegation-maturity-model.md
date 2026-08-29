# Stage Agentic-Engineering Adoption With a Delegation Maturity Model

Summary: Measure and drive an engineering org's agentic transformation with a Stage 0–5 ladder that ranks each engineer by their delegation and orchestration *relationship* with AI agents, not by whether they use AI at all — because high IDE-level usage can produce no faster shipping.

Use when:
- Diagnosing why broad AI-tool adoption has not translated into faster delivery.
- Defining a concrete target and measurement axis for an agentic-engineering rollout across many teams.

Details:
- The gap that motivates the model: within months ~90% of Block's engineers used Goose and Claude Code, and metrics plus token bills proved it, yet "features certainly weren't making it to our customers any faster" because usage was stuck at IDE-level autocomplete and chat. Framed as three enablement phases — experimentation, adoption, impact — where 90% usage clears experimentation but not impact. (00:57-01:51)
- The target state is defined by *how work is produced*, not tool presence: engineers "leverage AI agents as their primary means of producing engineering outcomes" — decomposing problems, delegating, and reviewing/verifying — as their default way of operating. (02:28-03:03)
- The ladder measures how engineers "think and delegate and orchestrate" (reorganized with help from Steve Yegge's "Gas Town" article): **Stage 0** no AI in the workflow; **Stage 1** AI autocomplete only, never agent mode; **Stage 2** chatting with agents but producing no PRs; **Stage 3** delegating tasks to agents and reviewing the output; **Stage 4** running multiple agents in parallel; **Stage 5** ("final boss") delegating complete tasks where the agent produces shippable results without the human needing to guide it. (03:03-04:10)
- Placement is the planning tool: the bulk of 3,500 engineers sat at Stage 1–2, and the stated goal was to move them to Stage 5 — the ladder both locates the org and names the next rung to climb. (04:10-04:18)
- The model is a *relationship/capability* axis, complementary to outcome dashboards: it explains why usage and token-bill metrics can look "all in on AI" while shipping velocity is flat, so it should be paired with outcome measurement rather than replacing it.
- **The same ladder outside engineering, where the top rungs are not reachable yet.** Shenoy's autonomy ladder for services work — copilot, synchronous agent, asynchronous agent, long-running agent, AI coworker — matches this model's shape but reports the async rung as unbuilt outside code, because the forking substrate and the tolerance for out-of-order completion are both software-practice inheritances. Block's Stage 4 ("running multiple agents in parallel") is therefore not a generic maturity level: it is the stage that engineers can reach cheaply and that a property manager or an architect currently cannot, which is worth stating before this ladder is offered to a non-engineering function. ([Shenoy](../sources/20260828_B0fjR3yaZFU.md), 05:23-10:13)

- **Staging at the organizational level, with the cost of skipping it named.** Amazon ran three studies in sequence rather than a company-wide launch, and Liguori lists going "too broad in the organization too fast" as a distinct failure mode: "if we had expected all teams in massive organizations to be frontier teams immediately, we would not have had the learnings that we had from the Pathfinder, from the sprint experiment, from the pilot teams." What early breadth destroys is specifically local knowledge — "you have a lot of teams who don't know what they're doing. You haven't had time to find the best practices for your own organizations, the context that your organization needs" — which is a different loss from a team being handed more autonomy than it can handle. The stated next step is scale, not depth: "how do we scale this out… to the next 2,000 teams instead of 50 teams." ([Liguori](../sources/20260828_pqlWNihgdjI.md), 17:54-18:46)

- **A second ladder from the vendor side, and where it says teams are stuck.** Werry recounts a borrowed eight-stage curve running autocomplete (Copilot, GPT-3.5 era) → IDE agents (Cursor) → organizational wikis → MCP servers and skills → … → software factories, and places the field at "the sort of stage four to five level," adding that at that stage teams "understand that context is the bottleneck and they're trying to build solutions to solve it." The two ladders are measuring different axes and are worth keeping distinct: this page ranks an engineer's *delegation relationship* with agents, Werry's ranks the *infrastructure* the organization has built. A team can be high on one and low on the other, which is a more useful diagnosis than either alone. Attribution caveat: the slide is credited to a name that does not resolve from the audio, and no data supports the stage placement. ([Werry](../sources/20260827_qdAkxLoYNI8.md), 02:25-03:37)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Drive Org-Wide Agentic Adoption Through Champions and AI-Ready Repos](drive-org-wide-agentic-adoption-through-champions-and-ai-ready-repos.md)
- [Measure Feature Adoption Not Shipping Velocity](measure-feature-adoption-not-shipping-velocity.md)
- [Measure AI Transformation by Outcomes Instead of Adoption](measure-ai-transformation-by-outcomes-instead-of-adoption.md)
- [Universal AI Adoption Changes Engineering Coordination](universal-ai-adoption-changes-engineering-coordination.md)
- [Async Agents Need a Forking Substrate and a User Who Tolerates Out-of-Order Completion](async-agents-need-a-forking-substrate-and-a-tolerant-user.md)
- [Stage Productivity Pilots to Strip One Confound at a Time](stage-productivity-pilots-to-strip-one-confound-at-a-time.md)

Sources:
- [Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation](../sources/20260628_whue9_YquGA.md), 00:57-04:18
- [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../sources/20260828_B0fjR3yaZFU.md), 05:23-10:13
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 17:54-18:46
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 02:25-03:37
