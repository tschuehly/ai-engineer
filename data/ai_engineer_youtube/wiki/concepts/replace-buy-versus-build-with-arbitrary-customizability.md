# Replace Buy-Versus-Build With Arbitrary Customizability

Summary: Buy-versus-build asks the wrong question once agents do the customizing; the decision axis is whether the resulting system can be changed programmatically on your behalf, which a purchased system with a good API or MCP server satisfies and a purchased system without one does not.

Use when:
- A team is arguing between adopting a SaaS system of record and building an internal replacement.
- Evaluating vendors for an agent-heavy workflow and weighing feature lists against integration surfaces.
- Justifying keeping an incumbent tool that the team has outgrown at the UI layer.

Details:
- The dichotomy is refused, not resolved: on "should you shop for Salesforce or should you build your own CRM," the answer is "I actually think this is like a false dichotomy… we don't live in a world where the choice is between purchasing SaaS and building things yourself." ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 11:56-12:14)
- The replacement criterion is one property: "you should just be using something that is arbitrarily customizable." Building satisfies it trivially "cuz you can write code and make it better at any given point"; buying satisfies it conditionally, "if you can make that SaaS work on your behalf and be arbitrarily customizable, then that works too." (12:18-12:38)
- The consequence for planning is that the roadmap obligation disappears: "you don't need to build this GUI and like have a proactive roadmap as to like what features would make really great sense inside of some system. Like if you can arbitrarily customize the system, even if it's a system you've purchased, then you're pretty good." A customizable bought system removes the reason most teams build — waiting on someone else's roadmap. (12:39-12:52)
- The worked example separates the two things a purchase buys. Salesforce is kept because "it's a really good database. It's made a lot of amazing choices around what sales should look like, choices that we don't want to make ourselves" — a data model plus embedded domain decisions — "and then it exposes MCP. So all of our agents have access to Salesforce MCP. Works really well. Our team uses it every day." Domain opinions are the thing worth buying; the interface is the thing worth customizing. (12:52-13:11)
- The summary line is a ranking, not a preference: "infinite customizability is really the highest order bit." (13:11-13:16)
- This makes an agent-accessible programmatic surface a procurement requirement rather than an integration nicety, which is the buying-side counterpart of [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md) — a vendor without one fails the criterion regardless of its feature set.
- **Limits.** No cost, migration, or maintenance comparison is given, and the failure mode of the position is not discussed: an MCP server is a narrower surface than source code, and "arbitrarily customizable" via a vendor API is bounded by what that API exposes. One company, one example, no counterexample where the bought system's customizability ran out. (11:56-13:16)
- **The competing answer, from a company that could move its data.** Where this page keeps purchased systems in place and requires them to expose a programmatic surface, Snowflake's internal team pulls the contents out: "we bring all the first-party, the third-party data, all the Salesforce data, everything, the call transcripts, all together," so that agents inherit role-based access control from one store. Salesforce is the same system in both accounts and is treated oppositely — kept and called through MCP in one, drained into the warehouse in the other. The tradeoff is where the per-integration cost lands: customizability pays it at every system boundary and keeps each system's own permission model, consolidation pays it once at ingestion and inherits a single one. Note that the consolidating team sells the store, which is not a neutral position. ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 19:26-19:55)
- **A different resolution of the same dichotomy, cut by layer rather than by customizability.** Notion's GTM team rents orchestration, email, CRM, and enrichment outright — "vendors do that really well" — and builds only the context layer, for two reasons: "a generic tool can't capture all of our esoteric data models or workflows, and we do not want that context layer to be something we can't debug." Read against Wang's criterion, this is a caution about where programmatic customizability stops being enough: an MCP interface lets agents change a bought system's contents, and it does not make the system's representation of your domain yours or its behaviour inspectable. ([Liu](../sources/20260826_L4I7WgiEquo.md), 08:37-09:00, 17:52-18:17)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Tools](../topics/tools.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Build Core Agents and Buy Commodity Agent Workflows](build-core-agents-and-buy-commodity-agent-workflows.md)
- [Decide the Agent Buy Boundary With Six Production Questions](decide-the-agent-buy-boundary-with-six-production-questions.md)
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Crystallize the UI for Repeated Use Cases and Generate It for Novel Ones](crystallize-the-ui-for-repeated-use-cases-and-generate-it-for-novel-ones.md)
- [Verify AI Call Summaries Before CRM Sync](verify-ai-call-summaries-before-crm-sync.md)
- [Land the Data in One Governed Store So Agents Inherit Access Control](land-the-data-in-one-governed-store-so-agents-inherit-access-control.md)
- [Own the Context Layer and Rent Every Other Layer](own-the-context-layer-and-rent-every-other-layer.md)

Sources:
- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md), 11:56-13:16
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 19:26-19:55
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 08:37-09:00, 17:52-18:17
