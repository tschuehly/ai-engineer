# Move the Platform's Primary Surface as Its Users Gain Tools

Summary: An internal platform's primary surface is not a permanent architectural choice — it is a function of what its current users can build for themselves. DoorDash's GenAI platform went UI first, then API first, then workflow first, and each move was triggered by a different bottleneck: non-engineers could not call an API, then engineers were blocked waiting on the central team, then coding agents made non-engineers capable of consuming the API directly. The surfaces accumulated rather than replaced each other.

Use when:
- Deciding what an internal platform ships first when its users are a mix of engineers and non-engineers.
- Re-examining a UI-heavy platform roadmap now that its non-engineer users have coding agents.
- Explaining why a platform decision that was right two years ago is now the constraint.
- Sequencing platform investment against who is currently blocked, rather than against an architectural ideal.

Details:
- **Stage one, UI first, because the domain experts were not engineers.** "We needed to empower the people who are the domain experts, and in our case that was strategy and operations folks, it was product managers, it was even labeling partners, and not only engineers. So we kind of started with like, okay, we have to be UI first" — a decision explicitly backed by co-founder Andy Fang. The bottleneck named at this stage is that the people who hold the domain knowledge have no way to contribute at all. ([Chitlur Haridas](../sources/20260828_bMjlRrWjdT0.md), 02:50-03:14)
- **Stage two, API first, because the platform team became the queue.** "Then we kind of evolved to also being API first so that engineers can also build and not be blocked on the central platform and they can build their own systems." The bottleneck moved from *capability* to *throughput*: a UI-only platform routes every unanticipated need back through the team that owns the UI. (03:14-03:30)
- **Stage three, workflow first, because the users changed capability.** "Then of course with the coding agents, now we have become workflow first, where we kind of empower S&O and PMs to also being able to navigate the platform and run operations as well." Nothing about the platform's users' job description changed; their tooling did, and that converted a population that needed screens into a population that could consume APIs. This is the transition worth watching for, because it is caused by something outside the platform. (03:30-03:45)
- **The stages accumulate; they do not replace.** "We started with the UIs, we are now API and workflow first." The self-serve judge-calibration console is a first-party UI built *after* the API-first move, for exactly the workflow that was too intricate to leave to a generated app. So "API first" is a claim about which layer is guaranteed and owned, not a claim that the team stopped building screens. (11:35-11:47, 13:36-13:58)
- **The other half of the stage-three move is reuse rather than new build.** "We're trying to reuse a lot of the existing infrastructure that already existed at DoorDash, and that's helped us get a long way." The eval platform is described as the fourth pillar next to an LLM gateway, an agent gateway, and open-weights model hosting — a layer added to an existing platform rather than a greenfield product, which is part of why the surface could keep moving without a rewrite. (01:20-02:11, 13:44-13:58)
- **Limits, and the reason to treat this as a frame rather than a finding.** This is one team's retrospective on its own sequencing, with no counterfactual: there is no evidence that starting API-first would have been worse, and the "workflow first" stage is described in a single sentence with no artifact behind it beyond the calibration UI and the vibe-coded annotation apps. The transferable content is the diagnostic question — which class of user is currently blocked, and by what — not the specific three-stage path.
- **The failure mode when surfaces accumulate without edges between them.** This page's surfaces accumulated *and* remained reachable; Krieger describes the version where they do not. Code, co-work, and chat "don't interoperate well and they can't delegate to each other," and "the average person off the street could not explain to you why those are all different" — with the tell being a copy-paste handoff the product asks the user to perform: "can you please create a paragraph that I can paste into Claude Code? That is some 2020 kind of workflow that really shouldn't exist anymore." He names the same constraint as the top limit on a specific product: what holds Claude Design back is "better interaction with our other surfaces." Adding a surface is only additive if the delegation edges are added with it. ([Krieger](../sources/20260827_qqrk7CtkuIw.md), 14:10-14:41, 16:33-17:16)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Product Strategy](../topics/product-strategy.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Ship Stable APIs and Let Users Vibe-Code the Interface](ship-stable-apis-and-let-users-vibe-code-the-interface.md)
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Make Internal Platforms Self-Service for Agent Users](make-internal-platforms-self-service-for-agent-users.md)
- [Scale AI Fluency With Self-Service Platforms](scale-ai-fluency-with-self-service-platforms.md)
- [Gateway Platform Primitives Let Teams Focus on MCP Business Logic](gateway-platform-primitives-let-teams-focus-on-mcp-business-logic.md)
- [Build Internal AI Engineering Platforms When Off-the-Shelf Tools Lack Enterprise Context](build-internal-ai-engineering-platforms-when-off-the-shelf-tools-lack-enterprise-context.md)
- [Product Surface Fragmentation Makes the User the Integration Layer](product-surface-fragmentation-makes-the-user-the-integration-layer.md)

Sources:
- [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 01:20-03:45, 11:35-11:47, 13:36-13:58
- [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 14:10-17:16
