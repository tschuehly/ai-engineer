# The Install Handoff Is Now a Prompt

Summary: The artifact you hand a prospective user to get your tool installed has changed from a walkthrough — or, famously at Stripe, taking their laptop — to a prompt they paste into an agent. This makes prior developer-experience investment convert directly into agent readiness, and it makes the prompt itself a distribution asset worth authoring and maintaining.

Use when:
- Deciding whether developer-experience work still pays off now that agents install things.
- Designing the first-run path for a library, SDK, or API product.
- Looking for the smallest distribution artifact to ship alongside a release.

Details:
- **The observed change.** "We went from wizards installing our software to agents installing them… [the Collison brothers of Stripe] would hand you their laptop, and they would install Stripe. These days, it's kind of like just a prompt. Being in Y Combinator, we just give people a prompt." The high-touch install that a famous company treated as a founder's job compresses into a paste. ([Burns](../sources/20260826_V_5bn4q-vAI.md), 03:34-04:11)
- **The claim it licenses.** "Our very good developer experience primitives are now hitting agent primitives." The DX work — clear defaults, one-command setup, legible errors, honest docs — was not superseded by the agent channel; it is what the agent consumes. This is the same convergence the wiki records as a curb cut, arrived at from the vendor's side rather than the advocate's. See [Treat Agent Experience as a Curb Cut](treat-agent-experience-as-a-curb-cut.md). (04:11-04:20)
- **Why the category mattered.** c15t was built against tools "built for marketers and lawyers" while "we were built for the developer. So, we had to make sure we had a very good developer experience." The DX investment predates the agent channel and was made for competitive reasons; the agent payoff was discovered afterward, which is what makes the sequence credible rather than retrofitted. (02:07-02:17)
- **The audience check that shows it is not one company's habit.** Asked how many in the room had told an agent to accomplish something, had it propose installing a library, and accepted, "pretty much most people" raised their hands. A second source at the same event reports the same show of hands ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 04:44-05:22), so unattended library selection by agents is the assumed default among practitioners at this point, not a projection. (03:03-03:32)
- **What it implies operationally.** If the handoff is a prompt, the prompt is a product surface: it is versioned, it goes stale, and it can be tested by running it. It is also the *shortest* path you control end to end — unlike a docs page, you write both the instruction and the environment it lands in. Pair it with the two surfaces that determine whether the prompt succeeds: the docs the agent will actually read ([Ship Bundled Docs and an AGENTS.md Inside the Published Package](ship-bundled-docs-and-an-agents-md-inside-the-published-package.md)) and an adoption path with no human gate in it ([Self-Serve Onboarding Is a Precondition for Agent Recommendation](self-serve-onboarding-is-a-precondition-for-agent-recommendation.md)).
- **The asymmetry to keep in view.** A handed-over prompt is a channel you control; an assistant recommending you unprompted is not. The first is distribution you can author, the second is distribution you can only earn — and only the second showed up as this library's largest inbound source ([Attribute LLM-Sourced Inbound With a How-Did-You-Hear Field](attribute-llm-sourced-inbound-with-a-how-did-you-hear-field.md)).
- **Limit.** This is an anecdote about founder practice at one accelerator plus a show of hands at a conference, with no data on prompt-handoff conversion versus any other install path. The durable part is the framing — the install artifact is now text an agent executes — not any claim about its effectiveness.
- **The same principle applied to a buyer who is not a developer, and it goes the other way.** Rosenthal's rule for enterprise deals is that no work crosses to the counterparty: "Never say, 'Hey, go do these five things and then come back to me'… don't send your buyer away to do something and wait for them to come back because you lose total control of the sales cycle." Where the agent channel removes the human from the install path, the enterprise motion inserts one — "maybe that means you have to set up hackathons and come in their office and do it with them in person." Same invariant, opposite implementation: a pasted prompt and a hands-on integration session are both refusals to hand the work over. See [Never Send the Buyer Away With Homework](never-send-the-buyer-away-with-homework.md). ([Rosenthal](../sources/20260826_wdTRsfw0KG0.md), 05:52-06:31)

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Go To Market](../topics/go-to-market.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Treat Agent Experience as a Curb Cut](treat-agent-experience-as-a-curb-cut.md)
- [Self-Serve Onboarding Is a Precondition for Agent Recommendation](self-serve-onboarding-is-a-precondition-for-agent-recommendation.md)
- [Attribute LLM-Sourced Inbound With a How-Did-You-Hear Field](attribute-llm-sourced-inbound-with-a-how-did-you-hear-field.md)
- [Agents Widen the Dev-Tool ICP Beyond Engineers](agents-widen-the-dev-tool-icp-beyond-engineers.md)
- [Optimize Onboarding Around One Aha Moment](optimize-onboarding-around-one-aha-moment.md)
- [Ship Bundled Docs and an AGENTS.md Inside the Published Package](ship-bundled-docs-and-an-agents-md-inside-the-published-package.md)
- [Agent Experience Means Autonomous Access, Understanding, and Operation](agent-experience-means-autonomous-access-understanding-and-operation.md)
- [Never Send the Buyer Away With Homework](never-send-the-buyer-away-with-homework.md)

Sources:
- [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](../sources/20260826_V_5bn4q-vAI.md), 02:07-04:20
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 04:44-05:22
- [Reverse-Engineering the AI Buyer — Aliisa Rosenthal, Acrew Capital](../sources/20260826_wdTRsfw0KG0.md), 05:52-06:31
