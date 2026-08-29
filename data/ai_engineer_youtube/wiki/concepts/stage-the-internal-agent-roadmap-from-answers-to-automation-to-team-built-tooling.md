# Stage the Internal Agent Roadmap From Answers to Automation to Team-Built Tooling

Summary: The durable roadmap for an internal data assistant has four rungs, each of which changes what the user is doing rather than how well the previous rung works: talk to your data, then automate my workflows, then let teams build their own tooling, then personalize per person and per customer. Each rung requires a different substrate, and stopping at the first one is what makes a successful product stale.

Use when:
- Planning the next two quarters for an internal assistant that already answers questions well.
- Deciding whether the next investment is more data sources or a different capability class.
- Explaining to leadership why "we already have talk-to-your-data" is not a finished product.
- Judging when a platform is ready to be handed to non-engineering teams as a build surface.

Details:
- **Rung one, talk to your data.** The problem it retires is dashboard sprawl and analyst queues: "how do we get you out of those hundreds of dashboards situation, dependency to the analyst, and then first we'll democratize the data for you so that you can talk to your data." Substrate: a semantic layer over consolidated data — in this system 15 semantic views, 85 tables, 3,000 columns. ([Izmit](../sources/20260826_DrTdD-ttjCY.md), 09:38-09:53, 05:14-05:31)
- **Rung two, automate my workflows.** Unlocked by integrations rather than by better answers: "the next wave comes with all the MCP connections, all the integrations that you are building. Now it becomes automate my workflows. We literally have now sellers who use our agent to monitor their inbox, they monitor their Slack channels, keep track of all the customer questions coming about product questions, use the agent to draft responses, save that in Gmail, review them afterwards, send those things out. Or they automate their outreach workflows." The role change is explicit: "I became an orchestrator." Note that the write path is drafts-plus-review, not autonomous send. (09:54-10:26)
- **Rung three, teams build their own tooling.** The change is who holds the build capability, and the constraint it removes is organizational rather than technical: "historically a lot of these go-to-market teams, they have been always in the backlog of someone, backlog of an IT team, or trying to get a SaaS budget to learn and get a vendor on board to actually enable something. And now all of a sudden they're able to build team skills. They're able to build the custom dashboards that are fully optimized for what their team needs. Are able to deploy applications, automations, alerts." Substrate: skills, a no-code deployment surface, and inherited access control ([Land the Data in One Governed Store So Agents Inherit Access Control](land-the-data-in-one-governed-store-so-agents-inherit-access-control.md)). (10:27-11:01)
- **Rung four, hyper-personalization.** "Everyone is able to now get everything personalized for them, not only for themselves, but also for their customers with living context of customers, contacts." This is the least developed rung in the source — no mechanism, no example. (11:02-11:14)
- The ladder exists to answer a specific decay, not to be comprehensive: each rung is a new *kind* of thing the user can do, which is what resets the reference point that habituation keeps lowering ([The Wow Factor Collapses Into a Baseline Within Months](the-wow-factor-collapses-into-a-baseline-within-months.md)). "If you just do the first stage, and if you just wait there, you will get disrupted in a month or two." (11:14-11:35)
- **Read as a dependency chain rather than a maturity model, it explains its own ordering.** Rung two needs write-capable integrations, which need the trust earned at rung one. Rung three needs both a skill mechanism and governance that makes user-built artifacts safe to run, which is what rungs one and two put in place. The rungs are not interchangeable phases of ambition; each consumes the previous one's output.
- Limits: this is one company's observed sequence, presented as what "we usually see with the sales teams," with no adoption or value data attached to any rung and no report of what fraction of users reached rungs two or three. The team-built-tooling rung in particular assumes a governed platform where non-engineers can deploy safely; nothing is said about review, ownership, or sprawl of team-built skills. ([Provenance and Limits](../sources/20260826_DrTdD-ttjCY.md))
- **A second internal deployment whose three modes run concurrently rather than as rungs.** Cloudflare layers a request queue, a pushed weekly narrative, and a self-serve agentic workspace at the same time, segmented by user preference — "the layering of those three pillars... being able to answer questions where the team comes to you... and then the pushing of information and then self-serviceability." And its next step is not personalization but the write path: "harder problems around quoting and approvals and updating the CRM itself." Read together, the two accounts suggest the ladder describes capability depth while the layering describes delivery breadth, and a roadmap needs both axes. ([Joyce](../sources/20260826_Qw_tC68KKes.md), 16:30-17:08, 17:51-18:11)

Related topics:
- [Business Intelligence](../topics/business-intelligence.md)
- [Go To Market](../topics/go-to-market.md)
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)

Related concepts:
- [The Wow Factor Collapses Into a Baseline Within Months](the-wow-factor-collapses-into-a-baseline-within-months.md)
- [Land the Data in One Governed Store So Agents Inherit Access Control](land-the-data-in-one-governed-store-so-agents-inherit-access-control.md)
- [Make internal platforms self-service for agent users](make-internal-platforms-self-service-for-agent-users.md)
- [Use skills for workflow guidance and MCP for integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)
- [Treat Go-to-Market as a Live Model of Your World That Agents Act On](treat-go-to-market-as-a-live-model-of-your-world.md)
- [Crystallize the UI for Repeated Use Cases and Generate It for Novel Ones](crystallize-the-ui-for-repeated-use-cases-and-generate-it-for-novel-ones.md)
- [Layer Ask, Push, and Self-Serve Because Teams Interface Differently](layer-ask-push-and-self-serve-because-teams-interface-differently.md)
- [Read-Side Agents Scale First Because the Write Side Needs Approvals](read-side-agents-scale-first-because-the-write-side-needs-approvals.md)

Sources:
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 05:14-05:31, 09:38-11:35
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 16:30-17:08, 17:51-18:11
