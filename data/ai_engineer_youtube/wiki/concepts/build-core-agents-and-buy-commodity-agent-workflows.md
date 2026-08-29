# Build Core Agents and Buy Commodity Agent Workflows

Summary: Agent implementation strategy should follow business criticality: build when the agent is core product or competitive edge, and buy or platform-host when the workflow is commodity and speed matters more than maximal control.

Use when:
- Deciding whether to hand-roll an agent, adopt an agent framework, use a managed platform, or buy a vertical agent.
- Reviewing whether scarce engineering time should go into business logic or platform plumbing such as auth, connectors, hosting, and observability.

Details:
- Hruska groups agent implementation choices into handbuilt agents, framework-built agents such as LangGraph, managed agent platforms such as Retool Agents, and vertical agents; the tradeoff is control, engineering lift, flexibility, hosting, and production readiness, 07:26-08:36.
- Core product capabilities or workflows that create competitive advantage usually justify handbuilt agents because the team needs ownership and maximum control, 08:39-09:04.
- Commodity workflows that need to ship in days rather than quarters are stronger candidates for managed platforms, especially when the alternative is engineers debugging platform concerns instead of the business process, 09:13-09:29.
- Regulated or sensitive data and hard SLAs do not automatically decide the choice; they require a risk assessment of both build and buy paths, 09:04-09:29.
- Hruska expects businesses to keep a few purpose-built agents for strategic use cases and a long tail of business agents on managed platforms, analogous to handbuilt core software plus bought internal-tooling platforms, 10:41-11:16.
- **A different cut of the same decision: not what it is, but whether you can change it.** Wang rejects the framing outright for internal systems — "we don't live in a world where the choice is between purchasing SaaS and building things yourself… you should just be using something that is arbitrarily customizable" — and keeps Salesforce because it supplies domain decisions worth inheriting ("it's made a lot of amazing choices around what sales should look like, choices that we don't want to make ourselves") *and* an MCP server through which agents can bend it. Criticality tells you where to spend; customizability tells you whether buying forecloses the spend later. ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 11:56-13:16)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Raise Agent Agency Only When Efficacy Holds](raise-agent-agency-only-when-efficacy-holds.md)
- [Agent Experience Means Autonomous Access, Understanding, and Operation](agent-experience-means-autonomous-access-understanding-and-operation.md)
- [Keep Fixed Business Logic Outside the Model](keep-fixed-business-logic-outside-the-model.md)
- [Replace Buy-Versus-Build With Arbitrary Customizability](replace-buy-versus-build-with-arbitrary-customizability.md)

Sources:
- [How agents will unlock the $500B promise of AI - Donald Hruska, Retool](../sources/20250723_Lqq_LcBaJCc.md), 07:26-11:16
- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md), 11:56-13:16
