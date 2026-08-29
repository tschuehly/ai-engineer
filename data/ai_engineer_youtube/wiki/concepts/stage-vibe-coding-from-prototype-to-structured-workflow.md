# Stage Vibe Coding From Prototype to Structured Workflow

Summary: Vibe coding is useful when its autonomy level matches the stakes. Fast exploratory prompting can produce learning artifacts and prototypes, while durable team work needs templates, shared instructions, custom tools, configured checks, and approval boundaries.

Use when:
- Deciding whether an AI coding session is a throwaway exploration or production-directed work.
- Designing a team workflow that keeps the speed of vibe coding without accepting unmanaged generated code.

Details:
- The Copilot session describes "YOLO vibes" as useful for learning, proofs of concept, mockups, and helping nontechnical collaborators express an idea, but not as a sufficient path for shipping a maintainable product. (01:28-04:18)
- Structured vibe coding adds starter templates, familiar stacks, shared instructions, internal design systems, domain-specific tools, and guardrails so repeated agent sessions converge on the team's intended shape. (32:12-33:54)
- More mature use adds specifications or plans, MCP-connected systems such as databases and project tracking, configured test tasks, and periodic human review when the agent starts drifting. (01:15:00-01:18:44)

- Khandelwal turns the same distinction into an enforcement rule rather than a judgment call: agent-written experiment code is slop by design, so give it a declared exemption. "There is going to be slop when you're going to write experiments… It's not going to be shipped… It's a prototype. So, treat it like one. Get it to opt out of all the rigorous other standards you've got across your code base." A named lane keeps the standards credible everywhere else and gives the team's slop-detection and issue-filing agents a reason not to generate work items against code nobody intends to fix — but the source specifies no marking convention and no rule preventing promotion. See [Let Prototypes Opt Out of Codebase Standards](let-prototypes-opt-out-of-codebase-standards.md). ([Khandelwal](../sources/20260811_aeTb5BdmTTc.md), 12:57-13:15)
- **Internal operational tooling is a durable third category, not a stage-one prototype on its way somewhere.** DoorDash's annotation UIs are vibe-coded by non-engineers, used for real work that thousands of rows a week pass through, and never enter a codebase or a review process — "a vibe coded UI, looks pretty clean, does the job." The stakes calculus this page uses still applies but resolves unusually: the app is production for its single user and disposable to everyone else, so the standards that matter are the API contract underneath rather than the code above it. The talk never says who maintains these apps when an endpoint changes. ([AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 09:18-10:29)
- **The stage boundary can be drawn by the vendor of the dependency, not only by the builder.** Metronome ships the prototype lane as product surface: a sandbox tenant, skills files that teach the agent the API's foot guns, and an explicit public position that customers should not "operate the entire system without a human in the loop." A staging discipline enforced by the thing you are integrating with survives a builder's enthusiasm in a way a self-imposed one does not — and it also tells you which of your dependencies have thought about this at all. ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 06:13-06:35, 07:19-07:53)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Let Prototypes Opt Out of Codebase Standards](let-prototypes-opt-out-of-codebase-standards.md)
- [Vibe engineering is supervised agentic coding with judgment](vibe-engineering-is-supervised-agentic-coding-with-judgment.md)
- [Vibe coding hangover is a maintainability failure](vibe-coding-hangover-is-a-maintainability-failure.md)
- [Shift review and testing left for confident vibe coding](shift-review-and-testing-left-for-confident-vibe-coding.md)
- [Ship Stable APIs and Let Users Vibe-Code the Interface](ship-stable-apis-and-let-users-vibe-code-the-interface.md)
- [Let the Agent Reach a Test Environment, Not Production, When the Domain Carries Money](let-the-agent-reach-a-test-environment-not-production.md)

Sources:
- [Real World Development with GitHub Copilot and VS Code — Harald Kirschner, Christopher Harrison](../sources/20250803_eOxOzcw70f0.md), 01:28-04:18, 32:12-33:54, 01:15:00-01:18:44
- [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../sources/20260811_aeTb5BdmTTc.md), 12:57-13:15
- [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 09:18-10:29
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 06:13-06:35, 07:19-07:53
