# Seed the Agent-Built Sandbox With Usage, Not Just Objects

Summary: For systems whose behaviour only appears in derived artifacts — invoices, balances, aggregates, downstream schedules — checking that an agent created the right objects proves nothing. Direct the agent to also generate the flow that makes the derived artifact materialize, because that artifact is the only thing a human can actually inspect for correctness.

Use when:
- An agent has provisioned or configured a stateful system and you need to decide what "it worked" means before a human signs off.
- Writing the vendor-side skill or setup instructions that tell an agent what a complete environment looks like.
- A sandbox or test tenant reports success while the real misconfiguration is invisible until data has flowed through it.

Details:
- The observation, stated as a correction to the obvious check: "what it means to test your initial setup is not just that you can see a contract or something like that or see a customer provision but also you need to see usage." ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 07:53-08:04)
- The mechanism is that this obligation lives in the vendor's skills file, not in the user's prompt: "on the back end here our skills files are directing the agent to actually flow usage into the Metronome platform so that you can see what a live customer would look like." The user asked for a pricing model; the skill knew that a pricing model with no usage against it is untestable. (08:04-08:19)
- What the seeding buys is an inspectable artifact. The demo's real output is not the provisioned customer but the draft invoice, broken into build credits, plan mode credits, cloud credits, and AI gateway credits — the level of detail at which a human can recognize whether the model was replicated correctly. Object-level checks would have passed on a wrong invoice. (14:22-14:31, 15:34-15:41)
- The general shape: the further a system's correctness sits from its configuration, the more the check has to be run rather than read. Billing is an extreme case because a credit pool, a drawdown rule, and an overage threshold interact over a period, and "the credit itself" is called out as the object "relatively complicated to administer." (14:53-15:01)
- Say out loud that the data is synthetic, because a screenshot of a sandbox invoice looks identical to a real one. Garvin does: "you can see the usage that we plopped in. All obviously in a production environment, you would be seeing this against real usage that you have," with the purpose being "to just see what it would look like if you adopted the pricing model and then had real usage against it." (15:14-15:32)
- Limit worth carrying: seeded usage exercises the shape of the model, not its economics. Whether the credit pools are sized correctly for real traffic is a question this test cannot answer, which is where usage-data simulation against historical volumes takes over.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Let the Agent Reach a Test Environment, Not Production, When the Domain Carries Money](let-the-agent-reach-a-test-environment-not-production.md)
- [Simulate AI Pricing Against Usage Data Before Launch](simulate-ai-pricing-against-usage-data-before-launch.md)
- [Package Reusable Context as Skills, Libraries, and Registries](package-reusable-context-as-skills-libraries-and-registries.md)
- [Make Validation Fast, Local, Deterministic, and Actionable](make-validation-fast-local-deterministic-and-actionable.md)

Sources:
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 07:53-08:19, 14:22-15:41
