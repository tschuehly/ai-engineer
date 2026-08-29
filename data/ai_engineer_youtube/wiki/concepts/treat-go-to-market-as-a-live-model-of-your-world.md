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

Sources:
- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md), 02:56-05:16, 08:00-08:20, 10:08-10:12
