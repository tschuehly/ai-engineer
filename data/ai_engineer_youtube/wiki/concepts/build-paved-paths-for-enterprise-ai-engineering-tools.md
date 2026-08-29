# Build Paved Paths for Enterprise AI Engineering Tools

Summary: Enterprise AI engineering adoption needs a paved path that makes the right behavior easy: model gateways, tool discovery, standardized MCP deployment, runtime support, proof-of-concept freedom, production quality controls, training, communities, and leadership enablement.

Use when:
- Designing internal AI engineering platforms or MCP rollout processes.
- Preventing duplicate agent tools, uncontrolled MCP servers, and fragmented adoption across a large organization.

Details:
- Bloomberg observed that thousands of engineers and many teams independently building PR-review bots, incident-response agents, or MCP servers could quickly create chaos and duplication. (09:37-10:05)
- Its paved path included a gateway for model experimentation and visibility, an MCP discovery hub for finding existing servers, and a standard platform service for tool creation, deployment, runtime, and authentication concerns. (11:50-12:47)
- The platform intentionally made proof-of-concept work easy while requiring production quality control because stability and reliability are core business constraints. (12:48-13:24)
- Adoption used existing enablement mechanisms: AI coding became part of onboarding and training, champ/guild communities deduplicated work and shared learning, inner-source and visiting-engineer patterns helped cross-team delivery, and leadership workshops addressed lower manager and tech-lead adoption. (13:47-17:02)

- **How many paved paths, and what the registry has to guarantee.** Debois agrees with the duplication diagnosis and disagrees about the cardinality. Getting two teams to agree on how they work "requires a lot of communication and brokerage. So, you probably don't end up with one thing, but a catalog of three, four paved roads where they can pick off. And they can still do their own, but that's on their own budget." The reconciling variable is what is being shared: infrastructure everyone must traverse (a gateway, a discovery hub) can be singular, while a working practice cannot. He also specifies the owner's obligations, which is what separates a registry from a shared folder — entries must be testable, modular, extendable by others, and security scanned — and names the failure it prevents, which is a *choosing* failure rather than a duplication one: two similar skills with unclear maintenance leave the consumer unable to pick, so both go unused and a third gets written. See [Ship a Catalog of Paved Roads, Not One Standard](ship-a-catalog-of-paved-roads-not-one-standard.md). ([Debois](../sources/20260822_zCJtYuqwm7E.md), 11:26-13:26)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Build internal AI engineering platforms when off-the-shelf tools lack enterprise context](build-internal-ai-engineering-platforms-when-off-the-shelf-tools-lack-enterprise-context.md)
- [MCP gateways create an enterprise root of trust](mcp-gateways-create-an-enterprise-root-of-trust.md)
- [Gateway platform primitives let teams focus on MCP business logic](gateway-platform-primitives-let-teams-focus-on-mcp-business-logic.md)
- [Govern agent rules through feedback gatekeepers](govern-agent-rules-through-feedback-gatekeepers.md)
- [Ship a Catalog of Paved Roads, Not One Standard](ship-a-catalog-of-paved-roads-not-one-standard.md)
- [Agent Enablement Falls Between Platform and Developer Experience, So Name an Owner](agent-enablement-falls-between-platform-and-developer-experience-so-name-an-owner.md)

Sources:
- [What We Learned Deploying AI within Bloomberg's Engineering Organization - Lei Zhang, Bloomberg](../sources/20251216_Q81AzlA-VE8.md), 09:37-17:02
- [Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl](../sources/20260822_zCJtYuqwm7E.md), 11:26-13:26
