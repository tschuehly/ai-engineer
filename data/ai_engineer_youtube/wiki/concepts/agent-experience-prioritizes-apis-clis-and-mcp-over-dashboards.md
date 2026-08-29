# Agent experience prioritizes APIs, CLIs, and MCP over dashboards

Summary: As agents and bots become primary product users, products need machine-friendly control surfaces such as APIs, CLIs, and MCP servers, not only human dashboards.

Use when:
- Designing product interfaces for agentic users or deciding whether a dashboard is enough.
- Prioritizing API, CLI, MCP, or embedded UI work for a service that agents need to operate.

Details:
- Swyx cites a conference keynote claim that a large share of Vercel's users are now bots or agents, then infers that dashboards matter less than APIs, CLIs, and MCP surfaces for those users. (12:48-13:06)
- He links this to "agent experience": products may need to ship UI or capabilities into someone else's app, and the primary user may be an agent rather than a human clicking through a custom dashboard. (13:06-13:28)
- In his own workflow, Figma was useful less as a dashboard destination than as an artifact handed into an agentic workflow that produced implementation output. (13:29-13:38)
- Ubl gives the direct Vercel observation behind this pattern: more than 60% of Vercel page views over the prior seven days were AI agents, and platform usage is shifting from dashboard clicking toward APIs and CLIs. (13:00-13:26)
- He says feature proposals should answer how the feature is automated and how an agent uses it, treating CLI design as a first-class product question rather than an afterthought to UI. (13:27-13:38)
- Kanat-Alexander frames CLIs and APIs as accuracy infrastructure for agents: browser or computer-use automation can work, but text-native action surfaces better match how agents operate and reduce unnecessary orchestration risk (04:36-05:07).
- Agent-facing CLIs and APIs should run during development when they are part of the coding loop; CI-only feedback with long latency weakens iterative agent workflows (16:37-17:18).
- Friedman frames the CLI as a workflow surface for coding agents: developers can run agents in the background, collect logs, pipe outputs, and chain specialized generation, coverage, and review agents across SDLC tasks. (14:32-17:25)
- Burazin adds that APIs and readable docs are the baseline for agent experience, but the practical test is whether an agent can complete the task without a human clicking buttons, typing into terminals, reading logs, or debugging missing setup. 03:07-06:29, 14:30-15:02
- The pattern now shows up in infrastructure categories far from web hosting. Keegan McCallum, launching a real-time generative-video inference platform, treats the agent surface as a launch requirement rather than a later port: "in 2026, [we] don't just need platforms, we need software factories and ways for agents [to] interact with these. And so we've actually built one that will let folks hook into a CLI or an MCP server and build these kinds of applications," shipped next to the human-facing React component and Python runtime (Xln-On3syJk 06:53-07:58).
- **The same investment, justified by a human consumer rather than an agent one.** DoorDash's eval platform ships APIs not because agents are its users but because its human users now hold coding agents: "everybody has access to coding agents, and we actually doubled down on that API first approach. So because we had these APIs we were actually able to enable our stat ops teams to use something like a Codex or a Claude Code and vibe code their own annotation UIs." The dashboards-versus-APIs framing gets a third option — the API plus a generated interface per user — which only holds where the use cases differ in presentation and agree on the data model. ([AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 09:18-10:01)
- **The sharpest version of the claim: a human onboarding surface becomes dead weight.** Metronome's setup path is "an onboarding wizard meant for a human that needs to set up their environment," and the demo's line about it is "we don't need this now because we had an agent set up this environment." This is stronger than dashboards mattering less — a wizard is a sequenced, validating, state-carrying flow, and it is precisely the kind of surface an agent with an API and a skills file renders redundant. Stripe's supporting datum is unquantified: "the use of Stripe's CLI has exponentially increased over the course of the past five six months." ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 01:40-01:46, 13:49-13:59)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Agent Experience Means Autonomous Access, Understanding, and Operation](agent-experience-means-autonomous-access-understanding-and-operation.md)
- [Use skills for workflow guidance and MCP for integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)
- [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [Separate agent harnesses from generated-code execution](separate-agent-harnesses-from-generated-code-execution.md)
- [Standardize development environments around common model priors](standardize-development-environments-around-common-model-priors.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Ship Stable APIs and Let Users Vibe-Code the Interface](ship-stable-apis-and-let-users-vibe-code-the-interface.md)
- [Separate Agent as Product, Agent as Buyer, and Agent as User](separate-agent-as-product-buyer-and-user.md)

Sources:
- [Agents for Everything Else - swyx](../sources/20260501_zepu8Kk6FBQ.md), 12:48-13:38
- [The New Application Layer - Malte Ubl, CTO Vercel](../sources/20260420_XKup1pj-34M.md), 13:00-13:38
- [Developer Experience in the Age of AI Coding Agents - Max Kanat-Alexander, Capital One](../sources/20251223_rT2Del5pwg4.md), 04:36-05:07, 16:37-17:18
- [Vibe Coding with Confidence - Itamar Friedman, Qodo](../sources/20250806_n991Yxo1aOI.md), 14:32-17:25
- [AX is the only Experience that Matters - Ivan Burazin, Daytona](../sources/20250724_e9sLVMN76qU.md), 03:07-06:29, 14:30-15:02
- [Generative Video at the Speed of Light — Keegan McCallum, uRun](../sources/20260818_Xln-On3syJk.md), 06:53-07:58
- [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 09:18-10:01
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 01:40-01:46, 13:49-13:59
