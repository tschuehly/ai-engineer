# Ship Stable APIs and Let Users Vibe-Code the Interface

Summary: A platform team serving many use cases cannot build a bespoke UI for each one, and the usual fallback — one configurable generic UI — fits none of them. DoorDash's GenAI platform team stopped shipping annotation screens and shipped stable APIs instead, then had strategy-and-operations staff point Codex or Claude Code at those endpoints and generate whatever interface their use case needed. The decision is only safe under a specific precondition the team checked first: the variation across use cases was in the presentation, not in the data model.

Use when:
- A platform team's backlog is a queue of one-off internal UIs — annotation screens, review tools, labeling consoles — that no two teams want the same way.
- Deciding whether the next investment is a more configurable UI or a more stable API.
- Justifying why non-engineers should be given a coding agent and an API key rather than a feature request form.
- Estimating what actually blocks non-engineers from building their own tools, once they already have coding agents.

Details:
- **The problem is the interface count, not the interface quality.** "We talked to multiple different teams who have various ways of annotating their data sets, and it's almost hard for a platform team to build like a UI specific for each use case." The named use cases are genuinely unlike each other — grading restaurant menus, image annotation, manual testing — and each has an annotator, a strategy-and-operations person deciding what gets annotated, and a platform team owning the APIs. ([Paranjape](../sources/20260828_bMjlRrWjdT0.md), 08:39-09:18)
- **The precondition that makes the move safe, stated in one line.** "What stood out to us was the underlying patterns were similar. So if we are API first, we can actually enable our partners to simply vibe code these UIs for annotation." The diversity lived above the API line and the invariant lived below it: same traces, same scores, same datasets, same annotation records, different screens. A platform whose use cases differ in their *data model* cannot make this trade, because then the generated UI is not the only thing that has to be generated. (09:39-10:01)
- **What "API first" had to mean for this to work.** "All our scores, our data sets — these are all powered by very stable APIs that our team owns. So all your API access including SDK access is basically powered by this single plane." Two properties are doing the work. *Stable*, because a generated UI is written once against the endpoints as they were on the day the operator prompted for it and will not be re-generated when they drift. *Single plane*, because the SDK, the MCP surface, and the operator's generated app all read the same primitives, so an operator's tool is not a second-class view of the data. (06:12-06:35, 07:10-07:44)
- **What the platform team gave up, and named as the point.** "What helped us was to give this workflow in the hands of the operators so that they can actually build their own vibe-coded annotation UIs." The team stopped trying to anticipate the interface. The corresponding loss is that the platform team no longer sees or maintains the surface its users work in: no shared component library, no consistency across teams' tools, and no one to call when a generated app breaks. The talk does not discuss who owns those apps afterwards, whether any were rebuilt, or what happened to them when an API changed. (10:16-10:29)
- **The result the team claims, and its exact shape.** "We actually did see a lot of reduction in the spend at per annotation cost. As you all can imagine we do have thousands of rows that need to get annotated every week and it can get pretty expensive at DoorDash scale." The cost line being attacked is external per-unit annotator spend, not engineering time — which is what makes the argument different from ordinary internal-tooling ROI. No figure, baseline, or before/after is given; "thousands of rows… every week" is the only quantity in the talk. (13:58-14:33)
- **How this sits against the wiki's existing position on bespoke expert tooling.** Anterior's case for [purpose-built domain-expert review tools](domain-expert-review-tools-convert-judgment-into-deployable-knowledge.md) is that bespoke tooling is worth it when review outputs feed the platform directly. DoorDash agrees the tooling should be bespoke and moves the *builder*: the person who needs the screen writes it. The two positions diverge on how many distinct expert workflows you have. One clinical review surface justifies engineering investment; a dozen unlike annotation workflows does not, and that is the count that decides which of the two you are in.
- **What this is not.** The wiki's [agent-experience argument for APIs over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md) says ship APIs because the *consumer* is an agent. Here the consumer is a human non-engineer, and the API matters because it is what their coding agent can build against. The two arguments point at the same investment for opposite reasons, and this one has a dependency the other does not: the operator needs a coding agent, permission to use it, and somewhere to run the result.
- **The qualifier is repetition.** Generating the interface per user works best where the use case is run once by one person; where the same job recurs, Wang argues the regenerated surface charges a re-learning cost each time — "there is something really nice about being able to visit the same consistent UX for the same use cases over time so that you can like learn how to use some tool." His own stack splits accordingly: two crystallized internal interfaces for the recurring questions (what is our market, what changed with a customer) and about a dozen chat agents for everything else. ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 05:18-08:20, 10:57-11:51)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Move the Platform's Primary Surface as Its Users Gain Tools](move-the-platforms-primary-surface-as-its-users-gain-tools.md)
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Domain Expert Review Tools Convert Judgment Into Deployable Knowledge](domain-expert-review-tools-convert-judgment-into-deployable-knowledge.md)
- [Environment Isolation Is What Lets Non-Engineers Trigger Real Work](environment-isolation-is-what-lets-non-engineers-trigger-real-work.md)
- [Non-technical collaborators can steer agents with natural work artifacts](non-technical-collaborators-can-steer-agents-with-natural-work-artifacts.md)
- [Let Prototypes Opt Out of Codebase Standards](let-prototypes-opt-out-of-codebase-standards.md)
- [Make Internal Platforms Self-Service for Agent Users](make-internal-platforms-self-service-for-agent-users.md)
- [Crystallize the UI for Repeated Use Cases and Generate It for Novel Ones](crystallize-the-ui-for-repeated-use-cases-and-generate-it-for-novel-ones.md)

Sources:
- [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 06:12-06:35, 07:10-07:44, 08:39-10:29, 13:58-14:33
- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md), 05:18-08:20, 10:57-11:51
