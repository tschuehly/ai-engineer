# Let the Agent Reach a Test Environment, Not Production, When the Domain Carries Money

Summary: When the system an agent operates carries money or deep business logic, bound autonomy by *environment* rather than by confidence: let the agent run unattended all the way to a populated test instance, and require a human to carry the result into production. The stopping point is a property of the domain, so it does not move as models improve.

Use when:
- A coding agent is being pointed at billing, payments, entitlements, or any other system whose errors are financial rather than cosmetic.
- Deciding what "human in the loop" concretely means for an agent that is already reliable enough to finish the task.
- A vendor or platform team is deciding how far to let customers drive its product with an agent, and how to say so publicly.

Details:
- The rule as stated by the vendor of the product being driven: "the goal that we have from a product development standpoint is not to have a customer operate the entire system without a human in the loop. This is a type of system that is both business critical, has deep business logic behind it. And so instead, what we are recommending and building toward is to use your coding agent as a way to accelerate your work and get into a test mode and test environment." ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 07:19-07:47)
- The negative half is stated as flatly as the positive half, which is what makes it a boundary rather than a preference: "we're not expecting to ship into production. We're not pushing it into production." (07:41-07:47)
- **The boundary is the environment, not the confidence level.** This is the distinction that separates the pattern from the wiki's other autonomy rules. Those route by how uncertain the task is, how reliable the model has become, or what the user is competent to review; all three move over time. An environment boundary does not: the agent has full autonomy *inside* the sandbox — it provisioned the customer, chose the pricing structure, and generated usage without supervision — and zero authority to cross out of it. What the human reviews is a finished artifact, not the agent's process.
- The acceleration is real and is where the value sits. Metronome's normal path is "an onboarding wizard meant for a human that needs to set up their environment"; the demo skips it entirely — "we don't need this now because we had an agent set up this environment" — and the entire instruction was one natural-language sentence asking to replicate a named competitor's pricing model. (13:49-13:59, 15:41-15:51)
- The handoff is explicit rather than implied: initialize the accounts, let the agent build the demo instance, then do "the exact testing and tweaking from there exactly what you wanted before bringing that into production." (15:56-16:24)
- Worth noting who is making the argument. A usage-billing vendor has a commercial interest in appearing agent-ready, and this is the opposite claim. It is not disinterested — a vendor eats the reputational cost of a customer's mispriced invoice — but the bias runs toward caution here, not toward the demo.
- Caveat the source does not supply: nothing is measured. There is no report of what the agent got wrong, how many attempts the model took, or how the sandbox result was verified beyond looking at the resulting invoice. The pattern is an architecture decision presented as sound practice, not a result.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Seed the Agent-Built Sandbox With Usage, Not Just Objects](seed-the-agent-built-sandbox-with-usage-not-just-objects.md)
- [Choose Autonomy Level by Task Uncertainty and Control Needs](choose-autonomy-level-by-task-uncertainty-and-control-needs.md)
- [Start with augmentation when autonomous reliability is not ready](start-with-augmentation-when-autonomous-reliability-is-not-ready.md)
- [Stage Vibe Coding From Prototype to Structured Workflow](stage-vibe-coding-from-prototype-to-structured-workflow.md)
- [Prevent AI Billing Surprises With Caps, Notifications, and Rate Limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md)

Sources:
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 07:19-08:19, 13:49-13:59, 15:41-16:24
