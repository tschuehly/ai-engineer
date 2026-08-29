# Layer Ask, Push, and Self-Serve Because Teams Interface Differently

Summary: The same data substrate has to reach its users through three delivery modes at once — an operations team that answers questions on request, a pushed narrative nobody has to ask for, and a self-serve agentic surface people drive themselves — because the modes serve different people rather than succeeding each other, and skipping one leaves that population unserved.

Use when:
- Planning the rollout of an internal data or agent platform across a large non-engineering organization.
- Arguing against retiring a human-in-the-loop request queue once a self-serve surface ships.
- Diagnosing why a technically successful internal tool is not reaching part of its intended audience.

Details:
- The three pillars are scaling analysis (the operations team answers more, faster), scaling insight (the story is pushed out), and self-service (the go-to-market team pulls what it needs against expert skills). ([Joyce](../sources/20260826_Qw_tC68KKes.md), 04:56-06:45)
- **The layering is stated as a finding, and the reason is preference rather than capability:** "the layering of those three pillars... being able to answer questions where the team comes to you, some of the go-to-market team, that's how they like to interface with the operations team is to be able to ask questions. And then the pushing of information and then self-serviceability. Through that, you're able to interweave all the needs of the team." (16:30-16:55)
- Each mode carries a different failure if it is missing: without self-service, people cannot get situation-specific data at the moment of a customer call; without push, the population that never opens a dashboard is unreached and performance views diverge; without a scaled analytical team, "the opportunity cost of that team being overloaded" is that the go-to-market team's needs are simply not met. (14:39-15:33)
- **Ask and self-serve are not the same interaction with different staffing.** The request queue is where a human interprets an ambiguous question; the self-serve workspace is where a rep executes a known job. Treating the queue as legacy misreads it as an inefficient version of self-service rather than as the surface for the questions that are not yet enumerable — the residual the skill files explicitly do not cover, "the other 20%... more complex strategic questions." (07:45-07:53)
- The three modes share one substrate: the same role-specific skill files back the analyst's queries, the automated summary's data preparation, and the reps' self-serve workspace, which is what makes maintaining three surfaces affordable. (08:15-08:29)
- **The staging is not a maturity ladder.** This differs from the four-rung roadmap in [Stage the Internal Agent Roadmap From Answers to Automation to Team-Built Tooling](stage-the-internal-agent-roadmap-from-answers-to-automation-to-team-built-tooling.md), where each rung changes what the user does and supersedes the previous one's sufficiency; here the three modes run concurrently and permanently, because they are segmented by user preference rather than by system capability.
- **Limit.** No usage split across the three modes is reported, so the claim that all three are needed rests on the speaker's judgment rather than on evidence that any population would have gone unserved. The only outcome figure attached to the whole framework is an unmethodized "2x our efficiency." (16:56-17:08)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Product Strategy](../topics/product-strategy.md)
- [Business Intelligence](../topics/business-intelligence.md)

Related concepts:
- [Stage the Internal Agent Roadmap From Answers to Automation to Team-Built Tooling](stage-the-internal-agent-roadmap-from-answers-to-automation-to-team-built-tooling.md)
- [Push the Narrative Because Dashboard Adoption Is Always Uneven](push-the-narrative-because-dashboard-adoption-is-always-uneven.md)
- [Choose AI coworker form factors by interaction mode](choose-ai-coworker-form-factors-by-interaction-mode.md)
- [Separate the Did-Not-Try Problem From the Did-Not-Return Problem](separate-the-did-not-try-problem-from-the-did-not-return-problem.md)
- [Crystallize the UI for Repeated Use Cases and Generate It for Novel Ones](crystallize-the-ui-for-repeated-use-cases-and-generate-it-for-novel-ones.md)
- [Separate the Context Gap From the Expert Gap](separate-the-context-gap-from-the-expert-gap.md)
- [Choose Quality Over Coverage Because the First Five Answers Decide Adoption](choose-quality-over-coverage-because-the-first-five-answers-decide-adoption.md)
- [Ship Go-to-Market Changes on an Engineering Release Cadence](ship-go-to-market-changes-on-an-engineering-release-cadence.md)

Sources:
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 04:56-06:45, 14:39-15:33, 16:30-17:08
