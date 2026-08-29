# Self-Serve Onboarding Is a Precondition for Agent Recommendation

Summary: An agent recommending a tool has to hand the user everything that follows from the recommendation. If adoption requires demos and sales emails, the agent's recommendation becomes an unpleasant errand it will not assign, so gated onboarding does not merely slow the funnel — it removes you from the agent's answer set.

Use when:
- A product's evaluation path runs through a demo request or a sales-qualified lead form.
- Deciding what to expose for free or self-serve when agents are a distribution channel.
- Prioritizing distribution work: registry listings, install paths, credential flows.

Details:
- **The stated mechanism.** "Reduce as much friction as possible for an agent or developer to go from finding out about your tool to embedding it in their workflow. Because if an agent realizes your tool requires like three different demos and emailing sales reps and stuff, they're never going to say, 'Hey user, like here's what you should do, but FYI, you're going to have to do all this other stuff.' It's like not going to happen." ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 12:28-12:53)
- **Why this is stronger than conversion-rate friction.** In a human funnel, gating filters who continues. Here the gate acts one step earlier, at the recommendation itself: the agent evaluates whether the suggestion is actionable before it makes it. A tool that cannot be adopted inside the session is one the agent has reason to substitute — in the same talk, with "have your developers make a wiki page." The cost is not a lower conversion rate on a known lead; it is never entering the consideration set.
- **Be reachable where an agent looks.** "Go to market. So, go to agent market. Make sure you're in the marketplace, in the MCP registries, everywhere that you would expect an agent to be able to easily find you." Registry presence and frictionless install are two halves of one requirement — discoverable and adoptable. See [Distribute MCP Apps Through Stores and Dynamic Discovery](distribute-mcp-apps-through-stores-and-dynamic-discovery.md). (12:12-12:28)
- **The parts of onboarding an agent cannot do.** The concrete blockers named are human-gated sequences: booking demos, emailing a sales rep. The wiki's adjacent pages name the rest — a human onboarding wizard rendered redundant by an agent with an API and a skills file, and the missing web convention for how an agent signs up and logs in. See [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md) and [Design an Agent-First Signup and Login Flow](design-an-agent-first-signup-and-login-flow.md).
- **The tension this creates with enterprise sales.** Demo-gated evaluation exists to qualify and to price; removing it has real revenue consequences. The resolution this page suggests is not abolishing the sales motion but ensuring a complete self-serve path exists *alongside* it, because the agent channel routes around anything else. The talk does not address this tradeoff, so treat the resolution as inference rather than as sourced advice.
- **Cover the pain, not just the category.** The same passage pairs friction reduction with content coverage: "make sure that you are covering those pains… that's how a user is going to be most in their time of need… you want to make sure that there's enough content out there on the internet for the agent to be aware of that and make those connections for you." Discoverability and adoptability fail independently, so both need their own measurement — see [Measure Agent Recommendations on Pain Prompts, Not Comparison Prompts](measure-agent-recommendations-on-pain-prompts-not-comparison-prompts.md). (12:53-13:10)
- **What the frictionless end state actually looks like, plus the outcome.** This page argues negatively, from what disqualifies you. Burns shows the positive form: the install handoff compressed into a pasted prompt — "we went from wizards installing our software to agents installing them… these days, it's kind of like just a prompt. Being in Y Combinator, we just give people a prompt" — and, at the same conference, assistant recommendation registering as the library's number one inbound source on its onboarding form. It is one data point, but it is a data point on the side of the funnel this page predicts. See [The Install Handoff Is Now a Prompt](the-install-handoff-is-now-a-prompt.md) and [Attribute LLM-Sourced Inbound With a How-Did-You-Hear Field](attribute-llm-sourced-inbound-with-a-how-did-you-hear-field.md). ([Burns](../sources/20260826_V_5bn4q-vAI.md), 02:17-04:11)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Product Strategy](../topics/product-strategy.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Measure Agent Recommendations on Pain Prompts, Not Comparison Prompts](measure-agent-recommendations-on-pain-prompts-not-comparison-prompts.md)
- [Distribute MCP Apps Through Stores and Dynamic Discovery](distribute-mcp-apps-through-stores-and-dynamic-discovery.md)
- [Design an Agent-First Signup and Login Flow](design-an-agent-first-signup-and-login-flow.md)
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Optimize Onboarding Around One Aha Moment](optimize-onboarding-around-one-aha-moment.md)
- [Separate Agent as Product, Agent as Buyer, and Agent as User](separate-agent-as-product-buyer-and-user.md)
- [Treat Agent Experience as a Curb Cut](treat-agent-experience-as-a-curb-cut.md)
- [The Install Handoff Is Now a Prompt](the-install-handoff-is-now-a-prompt.md)
- [Attribute LLM-Sourced Inbound With a How-Did-You-Hear Field](attribute-llm-sourced-inbound-with-a-how-did-you-hear-field.md)

Sources:
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 12:12-13:10
- [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](../sources/20260826_V_5bn4q-vAI.md), 02:17-04:11
