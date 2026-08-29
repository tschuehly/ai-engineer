# Separate Agent as Product, Agent as Buyer, and Agent as User

Summary: "Building for agents" collapses three different projects with three different obligations — metering what your agent consumes, being discoverable and purchasable by someone else's agent, and repricing when an agent replaces your human users. Teams routinely complete one and believe they have answered all three.

Use when:
- A roadmap item says "support agents" and nobody has said which agents, whose, or doing what.
- Deciding whether the agent work in front of you is a metering problem, a distribution problem, or a pricing-model problem.
- Auditing an agent strategy that has shipped an MCP server or a CLI and stopped there.

Details:
- The prompt for the split: product teams "are obviously thinking about building for agents, but I think one of the things that's important to do is to decode what exactly does that mean," answered by "thinking about the different roles that they play." ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 09:33-09:53)
- **Agent as your product** — you ship the agent, so its consumption is your cost of goods. "If the agent can be the product and run up a token bill it's important for you to be able to meter on that," which is why agent products converge on usage-based pricing rather than choosing it stylistically. (09:53-10:07)
- **Agent as a buyer** — someone else's agent procures from you unattended. In the demo this is literal: the Stripe Projects CLI is "literally procuring their initial Stripe instance as well as additional backend services," so the obligation is to "make your services discoverable to agents that may be building an application or working in the open web." Vercel and Hugging Face are named as providers onboarding into that environment for exactly this reason. (10:07-10:26, 17:14-17:31)
- The buyer role has two markets that are easy to conflate: B2C is agentic commerce, B2B is an agent provisioning infrastructure for the application it is building. The discoverability work rhymes; the trust, authorization, and contracting work does not. (10:26-10:33)
- **Agent as your user** — an agent operates the product a human used to operate. Garvin calls this the reason his own category is growing, and it is the role that breaks the pricing metric rather than adding a surface: see [Per-Seat Pricing Loses Its Referent When One Agent Does the Work of Many Logins](per-seat-pricing-loses-its-referent-when-agents-do-the-work.md). (10:36-11:23)
- The practical value of the taxonomy is that each role has a different owner and a different failure. Metering is a billing-infrastructure problem, discoverability is a distribution and interface problem, and repricing is a go-to-market problem — and the third can be true of a company that has never built an agent at all.
- The roles compose rather than exclude. Metronome is simultaneously being bought by an agent (Stripe Projects provisions it), operated by an agent (the coding agent configures the pricing model), and used to meter someone else's agent product. Asking which role applies is a question per surface, not per company.
- Limit: this is a framework offered by a vendor whose product sits under all three roles, presented without any data on how commonly each role is confused for another. Its value is as a disambiguation checklist, not as a claim about the market's composition.
- **Agent-as-buyer arrives as someone else's protocol, not as your API design.** In commerce, being purchasable by another company's agent means conforming to ACP, UCP, and Meta's feed schemas — three specifications you do not control — and the enforcement is exclusion rather than a support ticket: "you want to make sure that the feeds are actually conforming, or else they will not support it." The obligation in this bucket is therefore set by the channel and re-set whenever the channel's spec moves, which makes it an ongoing conformance cost rather than an integration project. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 09:19-09:30, 17:55-18:12)

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Agents](../topics/agents.md)
- [AI Monetization](../topics/ai-monetization.md)

Related concepts:
- [Per-Seat Pricing Loses Its Referent When One Agent Does the Work of Many Logins](per-seat-pricing-loses-its-referent-when-agents-do-the-work.md)
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Agentic Commerce Moves From Static Stores to Intent Infrastructure](agentic-commerce-moves-from-static-stores-to-intent-infrastructure.md)
- [Choose Direct or Indirect AI Monetization](choose-direct-or-indirect-ai-monetization.md)
- [Delegate Agentic Commerce Transactions With Explicit Payment Authority](delegate-agentic-commerce-transactions-with-explicit-payment-authority.md)
- [Eval an Agent Surface for Protocol Compliance, Not Just Behavior](eval-agent-surfaces-for-protocol-compliance-not-just-behavior.md)

Sources:
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 09:33-11:23, 16:42-16:54, 17:14-17:31
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 09:19-09:30, 17:55-18:12
