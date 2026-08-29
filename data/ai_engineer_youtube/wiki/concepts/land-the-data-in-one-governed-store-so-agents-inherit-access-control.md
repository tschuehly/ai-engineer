# Land the Data in One Governed Store So Agents Inherit Access Control

Summary: If first-party, third-party, CRM, and unstructured data all land in one governed store, authorization becomes a property agents inherit rather than something each agent implements. That is a data-consolidation decision made for the sake of the agent layer, and it is what makes no-code agent deployment safe enough to hand to business teams.

Use when:
- Deciding whether to federate queries across systems or consolidate the data first.
- Non-engineering teams are being given the ability to deploy their own agents.
- Working out where row- and column-level permissions live in an agent architecture.
- Weighing a platform that supplies retrieval, chat UI, and guardrails against assembling them.

Details:
- The choice is described as strategic and deliberate: "we made a strategic choice for our internal thing where we said, look, it is important that we bring all our data together. And we do that in Snowflake. We bring all the first-party, the third-party data, all the Salesforce data, everything, the call transcripts, all together." ([Izmit](../sources/20260826_DrTdD-ttjCY.md), 19:26-19:39)
- **The payoff named first is authorization, not query performance.** "And then these agents can basically inherit a lot of the role-based access controls." Access decisions are made once in the store and apply to every agent built over it, rather than being re-derived per agent, per tool, or per connector — which is the version that fails as the number of agent authors grows. (19:39-19:43)
- The deployment consequence follows from it: "I literally can deploy these agents without writing a single line of code," with the chat UI available out of the box, on a no-code agent platform intended for business users. Handing a build surface to non-engineers is only defensible when the permission model is not something they have to get right ([Stage the Internal Agent Roadmap From Answers to Automation to Team-Built Tooling](stage-the-internal-agent-roadmap-from-answers-to-automation-to-team-built-tooling.md)). (19:43-19:55)
- Platform-level guardrails cover the other half — which data an agent may reach: "it comes with the guardrails and things where you don't really need to worry about them going very crazy on what data sources to do things. So we are able to do a lot of curation. We are able to do a lot of security guardrails in there as well." (20:04-20:19)
- **The cost of this design is the consolidation itself, and it is the part that is invisible in the talk.** Sixty percent of the system's data arrived after launch, over six to seven months, which is a fair estimate of how long the pipeline work actually takes even at a company whose business is the store. Nothing here removes that work; it relocates it upstream of the agent so that the agent layer stays thin. (05:06-05:11)
- Contrast with the alternative shape the wiki already carries: an agent-first stack built over programmatic access to systems that stay where they are ([Replace Buy-Versus-Build With Arbitrary Customizability](replace-buy-versus-build-with-arbitrary-customizability.md)) keeps each system's own permission model and pays per integration; consolidation pays once at ingestion and then inherits. The discriminator is whether you can move the data at all — this team could, because their employer sells the store.
- Limits: this is the vendor describing its own platform, and every affordance praised (inherited RBAC, no-code deployment, out-of-the-box chat UI, curation and guardrails) is a product feature of the speaker's employer. No mechanism is given for how permissions propagate through semantic views, skills, or MCP connections, and no failure, leak, or over-permission incident is discussed. Whether the agent's retrieval layer respects the same controls as direct SQL is not addressed. ([Provenance and Limits](../sources/20260826_DrTdD-ttjCY.md))
- **A neighbouring design that consolidates computation but splits serving, and says nothing about inherited authorization.** Notion lands every GTM vendor feed in one warehouse to compute modeled, versioned entities, then publishes a denormalized profile to a key-value store for agent reads in milliseconds. Consolidation there is justified by data quality, latency, and joinability rather than by access control — no role-based inheritance is claimed — which makes the pair worth reading together: one governed store buys authorization, a compute/serve split buys read latency, and neither buys the other automatically. ([Liu](../sources/20260826_L4I7WgiEquo.md), 04:36-04:59, 09:04-10:07)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Security](../topics/security.md)
- [Business Intelligence](../topics/business-intelligence.md)

Related concepts:
- [Stage the Internal Agent Roadmap From Answers to Automation to Team-Built Tooling](stage-the-internal-agent-roadmap-from-answers-to-automation-to-team-built-tooling.md)
- [Production agent platforms need enterprise controls](production-agent-platforms-need-enterprise-controls.md)
- [Make internal platforms self-service for agent users](make-internal-platforms-self-service-for-agent-users.md)
- [Replace Buy-Versus-Build With Arbitrary Customizability](replace-buy-versus-build-with-arbitrary-customizability.md)
- [Draw the Cut Line Between Verified Data and Free-Form Agent Analysis](draw-the-cut-line-between-verified-data-and-free-form-agent-analysis.md)
- [Scope a Person-Cloned Agent by Caller, With Drafts as the Shared Capability](scope-a-person-cloned-agent-by-caller-with-drafts-as-the-shared-capability.md)
- [Compute Truth in the Warehouse and Serve It as a Denormalized Profile](compute-truth-in-the-warehouse-and-serve-it-as-a-denormalized-profile.md)

Sources:
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 05:06-05:11, 19:04-20:19
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 04:36-04:59, 09:04-10:07
