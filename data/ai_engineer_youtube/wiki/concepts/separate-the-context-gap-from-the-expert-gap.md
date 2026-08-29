# Separate the Context Gap From the Expert Gap

Summary: Frontline work has two distinct deficits that agent tooling is often built to close at once — the context gap, which is the assembly cost of preparing for each interaction, and the expert gap, which is the difference between your best performer and someone still ramping — and they have different fixes, different owners, and different evidence of success.

Use when:
- Scoping an internal agent for a sales, support, or customer-success team and choosing what it should do first.
- Diagnosing why a tool that saves preparation time did not change outcome quality.
- Writing the success criteria for a floor-raising internal deployment.

Details:
- The context gap is a switching cost, and the work being described is legitimate: a rep goes from a prospect call to a current-customer call to an adoption conversation, and "they have to gather information for those specific calls, which is good. They really need to get that information to have those calls and understand how to approach the situation, but they have to do all that work in between." ([Joyce](../sources/20260826_Qw_tC68KKes.md), 02:55-03:37)
- **The expert gap is about judgment under a specific situation, not about knowledge in general:** the difference between how an expert "would approach a situation, how he would talk to a prospect, how he would work on adoption call, how he would handle a customer satisfaction issue" and how a new or ramping person would. The named target is "everyone working at the same operational level, so you have consistency in execution, consistency in messaging." (03:37-04:17)
- **The two gaps take different remedies in the same system.** The context gap is closed by retrieval and assembly — a self-serve workspace that pulls account data and generates the forecast brief, QBR deck, or renewal prep on demand. The expert gap is closed by curated skills carrying "expert-level information," which is a content problem requiring someone to decide what expert behavior is. Shipping only the first produces a faster path to the same uneven quality. (12:36-13:35)
- The evidence for each differs too. Closing the context gap shows up as time — the talk's framing of "2 hours to 5 minutes" for the analytical version of the same problem — while closing the expert gap shows up as variance across people, which nothing in this source measures. (05:03-05:26)
- **The expert gap is a floor problem, and it is the one that resists tooling.** Related sources converge on the same asymmetry: encoding a shadowed top rep's workflow is described as raising the floor for the team rather than the ceiling for the expert ([Shadow Your Best Human Before Encoding the Workflow](shadow-your-best-human-before-encoding-the-workflow.md)), and the general argument for prioritizing the floor over the ceiling is that trust is lost at the bottom of the distribution ([Raise the Floor Before Maxing the Benchmark](raise-the-floor-before-maxing-the-benchmark.md)).
- Both gaps are presented as the reason the go-to-market organization is inefficient rather than as separate initiatives: "with these two problems with manual work as well as salespeople not having enough information... it really creates an inefficiency in the go-to-market organization." (04:17-04:35)
- **Limit.** The two gaps are asserted from the speaker's experience, with no measurement of either — no preparation-time study, no ramp-time figure, no variance across reps before or after, and no definition of who counts as the expert whose level is being encoded.
- **The context gap stated as a state-management problem rather than an assembly problem.** Berry's account of one account — signals arriving, data going stale, actions taken by reps and agents, meetings and feedback landing — is what the rep is holding in their head between calls: "we are relying on sales reps in a lot of cases to manually sort through this." Cloudflare's framing is the switching cost of gathering information before each conversation; this one is the cost of maintaining continuity across a months-long cycle. Retrieval on demand closes the first and not the second, which is an argument for the persistent per-account agent rather than for a better search over the same sources. ([Berry](../sources/20260826_UhCY231d0FQ.md), 09:59-10:38)
- **The two gaps appearing as two separate builds inside one system.** Ramp's pre-meeting brief is a pure context-gap fix: usage, account vitals, open tickets, and the customer's own emailed agenda gathered into one place so an account manager in back-to-back meetings "can go in prepared." The expert-gap half is the platform-owned skill library — "meeting prep skills that we own at the system level" — which encodes what a good brief must contain regardless of who is reading it. Users then layer their own format instructions on top. The three-layer split (assembled context, system-owned judgment, personal presentation) is a usable decomposition of what a generated internal artifact is actually made of. ([Vaziri](../sources/20260826_VjEP0xqTUI0.md), 08:37-09:33, 12:11-13:00)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Agents](../topics/agents.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Shadow Your Best Human Before Encoding the Workflow](shadow-your-best-human-before-encoding-the-workflow.md)
- [Raise the Floor Before Maxing the Benchmark](raise-the-floor-before-maxing-the-benchmark.md)
- [Domain Expert Review Tools Convert Judgment Into Deployable Knowledge](domain-expert-review-tools-convert-judgment-into-deployable-knowledge.md)
- [Put the Business Question Set Inside the Skill File, Not Just the Schema](put-the-business-question-set-inside-the-skill-file-not-just-the-schema.md)
- [Layer Ask, Push, and Self-Serve Because Teams Interface Differently](layer-ask-push-and-self-serve-because-teams-interface-differently.md)
- [Environment Isolation Is What Lets Non-Engineers Trigger Real Work](environment-isolation-is-what-lets-non-engineers-trigger-real-work.md)
- [Run One Dormant, Long-Lived Agent Per Account](run-one-dormant-long-lived-agent-per-account.md)
- [The Human-Agent Handoff Is the Hard Part Once Agents Are the Decision Layer](the-human-agent-handoff-is-the-hard-part-once-agents-are-the-decision-layer.md)
- [Ship Go-to-Market Changes on an Engineering Release Cadence](ship-go-to-market-changes-on-an-engineering-release-cadence.md)
- [Let Users Author the Output Format as a Skill](let-users-author-the-output-format-as-a-skill.md)
- [Distribution Is the Bottleneck, Not the Idea](distribution-is-the-bottleneck-not-the-idea.md)

Sources:
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 02:55-04:35, 05:03-05:26, 12:36-13:35
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 09:59-10:38
- [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](../sources/20260826_VjEP0xqTUI0.md), 08:37-09:33, 12:11-13:00
