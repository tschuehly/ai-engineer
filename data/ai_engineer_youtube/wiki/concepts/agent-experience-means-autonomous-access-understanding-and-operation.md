# Agent Experience Means Autonomous Access, Understanding, and Operation

Summary: Agent experience is the ease with which agents can access, understand, and operate in a digital environment to complete a user-defined goal, with autonomy as the important extra constraint.

Use when:
- Designing products, devtools, or runtime environments whose primary users may be agents.
- Auditing whether a tool still depends on humans to click buttons, read logs, debug setup, or bridge missing machine interfaces.

Details:
- Burazin frames agent experience as the successor to user, customer, and developer experience, focused on whether agents can access, understand, and operate within digital environments to achieve the user's goal. 02:04-02:45
- He argues that the missing test is autonomy: if an agent always falls back to a human to log in, click buttons, debug errors, or type into terminals, the tool has not really solved agent experience. 05:35-06:29, 14:00-14:27
- The baseline agent-facing surface includes authentication handoff, clean Markdown documentation such as `.md` doc views and `llms.txt`, and API-first access to key product functionality. 03:07-05:23
- He cautions that API-first and readable docs are necessary but not sufficient; the stronger question is whether the agent can complete the task end to end without a human acting as an operational adapter. 05:23-06:29, 14:30-15:02
- Lajili (Poolside) frames this as the engineer's new job — the "AIX engineer": "focus less on the product and more on trying to make the AI work on the product" by building tools, improving the codebase so it is easier to work on, and improving knowledge bases, in whatever form fits (CLI, skill, or MCP). ([Your agent is blindfolded](../sources/20260708_iRcX54EO5g8.md), 05:51-07:02)
- His oxygen-mask investment argument: "put the mask on the AI first" — make it self-served *before* you build features, because "even if it slows you down right now, it's an investment that pays off as soon as you start multiplying agents and running things over time"; velocity without this "self-serve" scaffolding just compounds errors. ([Your agent is blindfolded](../sources/20260708_iRcX54EO5g8.md), 06:38-07:29)
- **The three layers, filled in by a billing vendor.** Access is the CLI, through which Stripe Projects "provisions a Stripe account for you as well as backend services… think like Vercel, Postgres, and in this case, a Metronome billing agent." Understanding is "an extensible set of skills files that can provide context to the agent that's implementing Metronome and working with our API," portable and installable on the customer's side. Operation is the verbose-error channel that lets the agent self-correct mid-run. The instructive part is that all three are shipped by the vendor rather than assembled by the user, and the understanding layer carries domain hazards — "a lot of different ways to hit foot guns" — that no amount of API polish removes. ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 00:59-01:22, 06:13-07:12)
- **The same test turned inward, at internal data rather than at a product.** Wang applies the access requirement to a company's own systems: every internal GTM surface — a market-classification dashboard, an alerting system, a dozen Slack agents — presupposes "really good APIs on top of any internal and external data," without which "we'd be out of luck." Agent experience is usually argued as an obligation to external agents visiting your product; here it is the precondition for your own staff's agents reaching your own data, and the interface is deliberately unspecified: "MCP, CLI, whatever… you just need some interface that's programmatic." ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 10:25-10:56)
- **A stricter test than autonomous completion: would the agent recommend it?** Jarmak's version adds a step past access, understanding, and operation — the agent also decides whether to hand the tool to its user, and it declines when adoption is human-gated: "if an agent realizes your tool requires like three different demos and emailing sales reps and stuff, they're never going to say, 'Hey user, like here's what you should do, but FYI, you're going to have to do all this other stuff.'" A product can pass every autonomy check inside the session and still fail here, because the failure is in what happens after the session. See [Self-Serve Onboarding Is a Precondition for Agent Recommendation](self-serve-onboarding-is-a-precondition-for-agent-recommendation.md). ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 12:28-12:53)
- **The understanding layer can ship inside the dependency, at zero adoption cost.** Every access-and-understanding surface on this page — CLI, skills files, docs site, MCP server — needs the consumer to install, configure, or visit something. Burns's version needs nothing: bundle the Markdown docs into the published package with an `AGENTS.md` beside them, and the understanding layer arrives with `npm install`, pinned to the installed version. It is worth separating from the rest of this page precisely because it is the one agent-experience investment with no counterpart action required on the other side. See [Ship Bundled Docs and an AGENTS.md Inside the Published Package](ship-bundled-docs-and-an-agents-md-inside-the-published-package.md). ([Burns](../sources/20260826_V_5bn4q-vAI.md), 10:04-11:53)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Treat agents as embodied action systems](treat-agents-as-embodied-action-systems.md)
- [Give Your Agent Eyes With a Product-Specific Observation Tool](give-your-agent-eyes-with-a-product-specific-observation-tool.md)
- [Harness Engineering Shifts Scarcity From Code Production to Control Surfaces](harness-engineering-shifts-scarcity-from-code-production-to-control-surfaces.md)
- [Separate Agent as Product, Agent as Buyer, and Agent as User](separate-agent-as-product-buyer-and-user.md)
- [Treat Go-to-Market as a Live Model of Your World That Agents Act On](treat-go-to-market-as-a-live-model-of-your-world.md)
- [Self-Serve Onboarding Is a Precondition for Agent Recommendation](self-serve-onboarding-is-a-precondition-for-agent-recommendation.md)
- [Treat Agent Experience as a Curb Cut](treat-agent-experience-as-a-curb-cut.md)
- [Ship Bundled Docs and an AGENTS.md Inside the Published Package](ship-bundled-docs-and-an-agents-md-inside-the-published-package.md)
- [The Install Handoff Is Now a Prompt](the-install-handoff-is-now-a-prompt.md)

Sources:
- [AX is the only Experience that Matters - Ivan Burazin, Daytona](../sources/20250724_e9sLVMN76qU.md), 02:04-06:29, 14:00-15:02
- [Your agent is blindfolded — Johan Lajili, Poolside AI](../sources/20260708_iRcX54EO5g8.md), 05:51-07:29
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 00:59-01:22, 06:13-07:12
- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md), 10:25-10:56
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 12:28-12:53
- [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](../sources/20260826_V_5bn4q-vAI.md), 10:04-11:53
