# Crystallize the UI for Repeated Use Cases and Generate It for Novel Ones

Summary: The argument against generating every interface is not cost or consistency but user learning — a surface someone visits repeatedly should stay the same so it can be learned once, which makes repetition, not capability, the criterion for when to freeze a UI and when to let the model produce one.

Use when:
- Deciding whether an internal or product capability ships as a chat interface, a built screen, or a generated one.
- A team is replacing working dashboards with chat because the model can now generate any view.
- Justifying investment in a durable internal tool when an agent could answer the same question ad hoc.

Details:
- The mistake is named directly: "there's still this mistake in the agent world which is made that's like, hey, does everything need to be a chatbot? I think the answer is no." ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 10:57-11:09)
- The capability is conceded before it is qualified — dynamic user interfaces "are amazing. Like yes, technically AI can just produce a new UI for any use case that you have… just to answer a question, it could produce like an HTML markdown file." The objection is not that generation fails. (11:19-11:33)
- The criterion is user learning over repeated visits: "there is something really nice about being able to visit the same consistent UX for the same use cases over time so that you can like learn how to use some tool." Generated-per-invocation output has no stable affordances to learn, so every visit costs a re-read. (11:33-11:43)
- The resolution is both, split by the shape of the use case: "having crystallized UIs and then also arbitrarily powerful flexible chat agents are both important components of being agent first." Recurring, named use cases get frozen surfaces; open-ended or first-time questions get the flexible agent. (11:43-11:51)
- This adds a fourth axis to the usual static/declarative/generative tradeoff of flexibility, consistency, latency, and token cost — see [Place Agent UI Generation on a Static–Declarative–Generative Spectrum](place-agent-ui-on-the-static-declarative-generative-spectrum.md). Learnability is an argument the others do not make, and it points the same direction as design-system consistency for a different reason: the user's accumulated knowledge of the surface, not the brand's.
- It also qualifies the stronger form of "ship APIs and let users generate the interface": that pattern is well suited to a use case run once by one person, and pays a re-learning cost each time the same interface is regenerated for the same recurring job. See [Ship Stable APIs and Let Users Vibe-Code the Interface](ship-stable-apis-and-let-users-vibe-code-the-interface.md).
- The speaker's own internal stack is the worked example: two crystallized interfaces (a market classification dashboard and an alerting surface) alongside about a dozen chat agents. (05:18-08:20)
- **Limit.** This is an assertion about user learning with no study, usage data, or A/B behind it, from a company reporting its own internal tooling choices. (10:57-11:51)
- **Who crystallizes it, once the platform is self-service.** Izmit's roadmap ends with the teams doing it themselves: go-to-market teams that were "always in the backlog of someone… or trying to get a SaaS budget" now "build the custom dashboards that are fully optimized for what their team needs" plus team skills, applications, automations, and alerts. That is this page's crystallization step relocated from the platform team to the users, and it changes the criterion from "is this use case repeated enough to justify our building a UI" to "is it repeated enough for the team that has it to build one" — a much lower bar, which is the point. The precondition is that the platform makes it safe: inherited access control and curation of which data sources an agent may reach. ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 10:27-11:01, 19:39-20:19)
- **The same axis applied to artifacts rather than interfaces.** Cloudflare freezes the recurring one — a weekly summary with a fixed structure of pacing, trends, standouts, and watches, pushed on a schedule — while generating the situational ones per invocation: forecast briefs, QBR decks, purchase decks, account plans, renewal prep. Repetition decides which side something falls on, exactly as this page argues for UI, and the reason is the same: a reader who sees the weekly summary fifty times should not have to re-learn its shape, while a deck for one customer call has no second reader to learn anything. ([Joyce](../sources/20260826_Qw_tC68KKes.md), 09:04-09:18, 12:36-14:28)

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Tools](../topics/tools.md)
- [Go To Market](../topics/go-to-market.md)

Related concepts:
- [Place Agent UI Generation on a Static–Declarative–Generative Spectrum](place-agent-ui-on-the-static-declarative-generative-spectrum.md)
- [Ship Stable APIs and Let Users Vibe-Code the Interface](ship-stable-apis-and-let-users-vibe-code-the-interface.md)
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Replace Buy-Versus-Build With Arbitrary Customizability](replace-buy-versus-build-with-arbitrary-customizability.md)
- [Stage the Internal Agent Roadmap From Answers to Automation to Team-Built Tooling](stage-the-internal-agent-roadmap-from-answers-to-automation-to-team-built-tooling.md)
- [Push the Narrative Because Dashboard Adoption Is Always Uneven](push-the-narrative-because-dashboard-adoption-is-always-uneven.md)
- [Layer Ask, Push, and Self-Serve Because Teams Interface Differently](layer-ask-push-and-self-serve-because-teams-interface-differently.md)

Sources:
- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md), 05:18-08:20, 10:57-11:51
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 10:27-11:01, 19:39-20:19
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 09:04-09:18, 12:36-14:28
