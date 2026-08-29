# Treat Go-to-Market as a Live Model of Your World That Agents Act On

Summary: The recurring go-to-market tasks — researching accounts, finding the right person at a company, building demos — are all queries against the same missing artifact, so the engineering deliverable is not a set of automations but a continuously refreshed joined model of internal and external data that agents can read and act on.

Use when:
- A revenue, marketing, or support team asks for AI help and the requests arrive as a list of unrelated automations.
- Deciding what to build first for an internal agent fleet that serves a non-engineering function.
- Scoping which data sources an operations agent needs before writing any prompt.

Details:
- The reframe is stated as a unification, not a metaphor: the laundry list of GTM work — "you got to research your customer… research your targets… find out information about targets… find the right people at particular companies… build POCs" — has a "grand unifying theme. Well, go-to-market is a data problem." ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 02:56-03:30)
- The artifact that follows from the reframe is named precisely: "you need basically a live model of your world that agents can act on." *Live* and *agents can act on* are both load-bearing — a static enrichment dump satisfies neither. (03:53-03:58)
- The model spans two source classes that most teams keep separate. Internal: "information that you know about your customers, about people that are at your company… data about how people use the product." External: "there's over 60 million companies in the world, and there's like billions of people, like over a billion that are on LinkedIn… and all this news." The instruction is to keep the full source inventory in view because those sources are what is "available to your agents." (04:01-04:42)
- The order of construction matters: the world model is the substrate, and the visible surfaces (a market dashboard, an alerting system, a fleet of chat agents) are all readers of it. In the described stack the same model backs the ICP dashboard, Request Lens, and a dozen Slack agents that "all have access to tons and tons of our internal data." (05:22-08:20)
- The claim is undated only in the sense that the speaker traces it back: he built GTM this way from Exa's mid-2023 launch because even GPT-4 "could actually just automate entire parts of go-to-market," so the pattern is not presented as newly enabled by frontier models. (04:53-05:16)
- **Limit.** This is one company's self-report with no measurement attached — the only outcome claim is "our go-to-market team is very lean, but very productive," with no numbers on either side, and no comparison to a team that did not build a world model. (10:08-10:12)
- **The same substrate argument from inside a 10,000-person sales organization, where the missing model is felt as tool sprawl.** Izmit's account of what reps actually do is the failure state of not having the joined model: "we have reps who are using 15 different tools, not because they love the UI of those tools, because every tool has a different data point, and then they end up stitching all of that together in spreadsheets," with 1,000 accounts each whose news, consumption, support tickets, and earnings must be tracked "30 times, 40 times a day." The human is the join. His answer is consolidation into one governed store so agents inherit access control, versus Exa's answer of programmatic access to systems that stay put — the same live-model goal reached from opposite directions, and the discriminator is whether you can move the data at all. ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 01:46-02:29, 19:26-19:55)
- **A second worked instance of the artifact, built by an engineering team rather than a founder, and it splits the model into a compute half and a serve half.** At Notion the warehouse ingests every GTM vendor feed and produces "a small set of modeled, versioned entities" — accounts, contacts, workspaces, eligibility, facts — while a key-value store publishes "a denormalized, key-addressable profile that agents can quickly query in milliseconds with no joins," with agent-generated research and rolling summaries keyed to the same IDs. The reframe is stated as a reclassification of the discipline: "a year ago, I would have told you that building a GTM system was a marketing ops problem. And today, I think it's one of the most interesting distributed systems problems that I've worked on." ([Liu](../sources/20260826_L4I7WgiEquo.md), 00:20-00:31, 09:04-10:07)
- **The fifth account, and the first that prices the model instead of describing it.** Berry's version of the same goal is "a perfect virtual copy of the market, the ideal customers, the accounts and contacts that you're going after," and his contribution is the mechanics underneath *live*: no vendor covers a field, so you waterfall providers and eval them; refreshing everything is unaffordable when the data is purchased, so field refresh becomes a per-field budget; and every vendor represents the same company differently, so entity resolution is a precondition. He also names why the copy will never settle — the account changes on its own, you change it by selling at it, and it emits hiring and firing signals, all at once. "A great data layer will tackle all of these things and allow me to move on to the more interesting work, but without this, it's really, really hard to execute automated GTM plays." ([Berry](../sources/20260826_UhCY231d0FQ.md), 02:19-06:19)
- **A fourth internal build, and a deliberate deflation of the novelty.** "If you're looking at this and you're like, 'that looks like a CDP,' yeah, you're right. We effectively went and built an internal customer data platform at Ramp" — CRM, product, enrichment and web data, buying signals both internally modeled ("we think that this customer has a high propensity to attach to procurement or treasury") and external ("funding announcements"), plus interaction data across emails, meetings, calls, and page views. What is claimed as new is not the architecture but that it is internal, agent-addressable, and holds embedded unstructured content beside the structured entities. The link to execution is causal rather than aesthetic: without one source of truth it is "effectively impossible to go and distribute some coordinated action across these different go-to-market teams and channels." ([Vaziri](../sources/20260826_VjEP0xqTUI0.md), 02:53-03:04, 05:44-07:24)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Agents](../topics/agents.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Classify the Whole Addressable Market Instead of Searching It Account by Account](classify-the-whole-addressable-market-instead-of-searching-it.md)
- [Alert on Account Change Events, Including the Ones That Are Absences](alert-on-account-change-events-including-absences.md)
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Personal Knowledge Bases Become Agent Context Substrates](personal-knowledge-bases-become-agent-context-substrates.md)
- [Context as a Service Is Vertical Search for Agents](context-as-a-service-is-vertical-search-for-agents.md)
- [Land the Data in One Governed Store So Agents Inherit Access Control](land-the-data-in-one-governed-store-so-agents-inherit-access-control.md)
- [Compute Truth in the Warehouse and Serve It as a Denormalized Profile](compute-truth-in-the-warehouse-and-serve-it-as-a-denormalized-profile.md)
- [Reduce Every Workflow to Know, Decide, Act, and Learn](reduce-every-workflow-to-know-decide-act-and-learn.md)
- [Waterfall Data Vendors and Run Evals to Decide Which to Trust](waterfall-data-vendors-and-run-evals-to-decide-which-to-trust.md)
- [Resolve Entities Across Vendors Before the Agent Reads the Record](resolve-entities-across-vendors-before-the-agent-reads-the-record.md)
- [Refresh Record Fields Selectively by Volatility and Price](refresh-record-fields-selectively-by-volatility-and-price.md)
- [Treat Tool-to-Tool Orchestration as a Data Engineering Problem](treat-tool-to-tool-orchestration-as-a-data-engineering-problem.md)
- [Ship Go-to-Market Changes on an Engineering Release Cadence](ship-go-to-market-changes-on-an-engineering-release-cadence.md)
- [Back the Served Context Layer With a Transactional Store for Referential Integrity](back-the-served-context-layer-with-a-transactional-store-for-referential-integrity.md)
- [Distribution Is the Bottleneck, Not the Idea](distribution-is-the-bottleneck-not-the-idea.md)
- [Build the Automated Motion First and Hire Into Its Bottlenecks](build-the-automated-motion-first-and-hire-into-its-bottlenecks.md)

Sources:
- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md), 02:56-05:16, 08:00-08:20, 10:08-10:12
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 01:46-02:29, 19:26-19:55
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 00:20-00:31, 03:43-05:27, 09:04-10:07
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 02:19-06:19
- [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](../sources/20260826_VjEP0xqTUI0.md), 02:53-03:04, 05:44-07:24
