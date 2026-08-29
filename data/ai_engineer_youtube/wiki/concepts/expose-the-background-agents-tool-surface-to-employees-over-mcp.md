# Expose the Background Agents' Tool Surface to Employees Over MCP

Summary: Publish the exact tool set your production background agents use as an internal MCP server that employees can connect their own agents and chat clients to. One surface, two consumers: every capability the platform team ships is automatically available to everyone building their own automations, with no separate distribution step.

Use when:
- An internal AI platform team is deciding whether self-serve access is a second product or a view onto the first.
- Employees are already building their own agents against whatever data they can reach, and the platform team wants that to converge on its tools.
- Weighing the cost of maintaining a "for humans" API alongside the automation-facing one.

Details:
- **The design, stated as identity rather than similarity.** "We've built this in a way where employees have access to the same tools and skills that are being used for the background agents that we're creating. We set up what we call our GT MCP, and this is basically just a window into the same exact tools that we've set up for these background agents." ([Vaziri](../sources/20260826_VjEP0xqTUI0.md), 14:11-14:27)
- **The payoff is distribution, and it is free.** "So that way the things that we build are just kind of automatically federated out to people who want to go and build their own agents. They want to go chat with the information that we're setting up, and build their own automations." A new tool ships once and appears in both the nightly fan-out and every employee's client. (14:27-14:40)
- **This is the self-serve tier of the three-mode delivery pattern, implemented as a protocol rather than as an application.** Cloudflare's equivalent gives each user a persistent agentic workspace ([Layer Ask, Push, and Self-Serve Because Teams Interface Differently](layer-ask-push-and-self-serve-because-teams-interface-differently.md)); this version ships no interface at all and lets people bring their own client. The tradeoff is discoverability against reach: a workspace can guide a non-technical user, while an MCP endpoint assumes the user already has an agent and knows what to ask for.
- **It is the operational form of the shared-substrate argument.** [Put Humans and Agents on the Same Substrate Instead of an AI Layer on Top](put-humans-and-agents-on-the-same-substrate-instead-of-an-ai-layer-on-top.md) argues that two substrates become two systems that drift apart. Sharing the *tool* surface, not just the data, is a stronger version: the human's agent and the background agent cannot diverge in what they can see or do, because there is only one definition.
- **It also makes the demand side legible.** Because employees connect their own agents to a server you operate, their usage is instrumented by construction — which is what turns the endpoint into a roadmap ([Read Employee-Built Automations as the Productionization Backlog](read-employee-built-automations-as-the-productionization-backlog.md)).
- **Scoping is the unaddressed half.** The durable-execution layer provides "config-scoped tool calls — different agents are going to have access to different sets of tools" (10:49-10:58), but nothing is said about how scope is decided when the caller is a person rather than a configured background agent. A background agent's tool set is chosen by the platform team for one workflow; an employee's is chosen by the employee. The wiki's answer elsewhere is to bind capability to the caller rather than to the agent ([Scope a Person-Cloned Agent by Caller, With Drafts as the Shared Capability](scope-a-person-cloned-agent-by-caller-with-drafts-as-the-shared-capability.md)), and this source does not describe doing that.
- **Limit.** No tool count, user count, access-control model, audit trail, rate limit, or write-capability policy is described, and "they're building a ton of them" is the only usage evidence. The security surface of exposing an automation platform's full tool set to every employee's chosen client is not discussed. (14:11-14:43)

Related topics:
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)
- [Go To Market](../topics/go-to-market.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Read Employee-Built Automations as the Productionization Backlog](read-employee-built-automations-as-the-productionization-backlog.md)
- [Put Humans and Agents on the Same Substrate Instead of an AI Layer on Top](put-humans-and-agents-on-the-same-substrate-instead-of-an-ai-layer-on-top.md)
- [Layer Ask, Push, and Self-Serve Because Teams Interface Differently](layer-ask-push-and-self-serve-because-teams-interface-differently.md)
- [Scope a Person-Cloned Agent by Caller, With Drafts as the Shared Capability](scope-a-person-cloned-agent-by-caller-with-drafts-as-the-shared-capability.md)
- [Filter MCP Tools by Scopes and Step-Up Authorization](filter-mcp-tools-by-scopes-and-step-up-authorization.md)
- [Design MCP Servers as Agent Products](design-mcp-servers-as-agent-products.md)
- [Use Skills for Workflow Guidance and MCP for Integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)
- [Solve One Team, Then Mirror the Build Sideways](solve-one-team-then-mirror-the-build-sideways.md)

Sources:
- [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](../sources/20260826_VjEP0xqTUI0.md), 10:49-10:58, 14:11-14:43
