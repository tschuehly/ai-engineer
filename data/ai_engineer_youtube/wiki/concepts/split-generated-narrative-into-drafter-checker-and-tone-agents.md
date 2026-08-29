# Split a Generated Narrative Into Drafter, Fact-Checker, and Tone Agents

Summary: A recurring generated narrative — a weekly business summary, a status digest, an executive brief — is more reliable when three agents own three separate objectives: one drafts from the data, a second checks the draft against the data, and a third rewrites for framing, with the third agent's job explicitly not correctness but balance.

Use when:
- Automating a recurring written artifact that a human currently assembles from a dashboard or a query.
- Deciding whether a single reviewer agent is enough, or whether editorial framing needs its own pass.
- Designing a pipeline whose output is prose that leadership will act on.

Details:
- The three roles are stated as a sequence over a data-fetch step: "we first get the data, and then we do a first pass draft on the data calling our MCPs, and then this we have a second reviewer agent who checks the veracity of the data, and then we have a third agent, which is a tone agent, who using a multi-shot prompt is able to just craft the message and highlight the risks and opportunities equally." ([Joyce](../sources/20260826_Qw_tC68KKes.md), 11:03-11:32)
- **The tone agent exists because a factually correct summary can still be a biased one.** Its target is that risks and opportunities "land with equal weight," which is a framing property no veracity check measures: a draft can pass fact-checking while burying the bad news, and no amount of grounding in the numbers fixes that. Separating the framing objective from the correctness objective is what makes it auditable.
- The tone agent is the only stage described as prompted by example: "using a multi-shot prompt." Editorial voice is the part of the pipeline where the specification is a set of exemplars rather than a rule, which is consistent with it being a style target rather than a truth target. (11:26-11:29)
- **Per-call observability is treated as part of the architecture, not as an add-on.** "With every run, we have observability into each of the LLM calls, so we can see what is passed and what is the response that is going on there" — with three agents in sequence, an inspectable trace per call is what makes it possible to attribute a bad summary to the drafter, the checker, or the rewrite. (11:32-11:41)
- The drafter reads through MCP servers rather than being handed a payload, so the fact-checker is verifying a draft against sources the drafter chose — which is a stronger check than re-reading a fixed context, and a weaker one than an independent re-derivation. (11:11-11:18)
- The pipeline's inputs are pre-shaped rather than raw, which bounds what the drafter can get wrong in the first place; see [Pre-Shape Analytics Data by Time, Slice, and Metric Before the Agent Reads It](pre-shape-analytics-data-by-time-slice-and-metric-before-the-agent-reads-it.md). (10:04-11:03)
- The same three-stage shape is what the team plans to reuse for the harder write path into the CRM: "I see that being set up in a way that I set up with that automated analysis where you have workflows to just make sure that everything is getting done right." (18:04-18:11)
- **Limit.** No accuracy figure is reported for the reviewer agent, no disagreement rate between drafter and checker, and no example of a catch. The evidence for the pipeline is the two-to-three-month manual read of every run, not a measurement of the checker's yield.

Related topics:
- [Workflows](../topics/workflows.md)
- [Business Intelligence](../topics/business-intelligence.md)
- [Go To Market](../topics/go-to-market.md)

Related concepts:
- [Use Reviewer and Approver Roles To Make Agent Workflows Reliable](use-reviewer-and-approver-roles-to-make-agent-workflows-reliable.md)
- [Withhold the Producer's Reasoning From the Critic](withhold-the-producers-reasoning-from-the-critic.md)
- [Stage Complex AI Applications Into Inspectable Deterministic and Agentic Steps](stage-complex-ai-applications-into-inspectable-deterministic-and-agentic-steps.md)
- [Read Every Run for Months Before Trusting an Unevaluatable Narrative](read-every-run-for-months-before-trusting-an-unevaluatable-narrative.md)
- [Pre-Shape Analytics Data by Time, Slice, and Metric Before the Agent Reads It](pre-shape-analytics-data-by-time-slice-and-metric-before-the-agent-reads-it.md)
- [Push the Narrative Because Dashboard Adoption Is Always Uneven](push-the-narrative-because-dashboard-adoption-is-always-uneven.md)
- [Self-verifying agent loops hide review rather than remove it](self-verifying-agent-loops-hide-review-rather-than-remove-it.md)
- [Run a Jury of Analysts and a Consensus Judge for No-Ground-Truth Questions](run-a-jury-of-analysts-and-a-consensus-judge-for-no-ground-truth-questions.md)

Sources:
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 10:04-12:03, 18:04-18:11
