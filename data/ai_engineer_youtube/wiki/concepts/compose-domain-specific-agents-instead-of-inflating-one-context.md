# Compose domain-specific agents instead of inflating one agent's context

Summary: Adding more skills and MCP servers to a single general-purpose agent is an *inheritance* pattern that inflates one context window and hits diminishing returns; the composition alternative is many small, isolated, full domain-specific agents — each with its own system prompt, precise tools, message history, and agentic loop — coordinated by a top-level agent that delegates to them in plain English.

Use when:
- Deciding whether to keep piling skills/MCP onto one agent or split work into specialist agents.
- Designing a multi-agent architecture where each specialist owns one domain (Gmail, Figma, Salesforce, GDPR).
- Explaining why an agent gets worse as you install more skills and MCP tools.

Details:
- The default "inheritance" model stacks model → system prompt → tools → skills → MCP → messages, which is "almost all context"; installing more MCPs and skills gives one agent more properties but degrades it — 5 skills works, 100 or 1000 hits diminishing returns, and "using very many [skills] actually makes your agent substantially worse." ([Domain-Specific Agents](../sources/20260629_spNAUEgq_A8.md), 09:59-13:30)
- Composition instead builds a tiny agent per domain whose *system prompt is the domain expertise* (a Figma agent that knows Figma's APIs, clicks, and mouse moves), carrying only the precise tools it needs and a small domain-only message history — "a full agent with its own message history, its own agentic loop," not just a server with tools. ([Domain-Specific Agents](../sources/20260629_spNAUEgq_A8.md), 13:32-14:38)
- The coordination protocol between the top agent and its specialists is natural language: they "just talk to each other the way a human does" (coordinator asks the Gmail agent for trip emails, results funnel up, then it delegates to the travel agent). ([Domain-Specific Agents](../sources/20260629_spNAUEgq_A8.md), 14:38-15:25)
- Biomimicry/Apollo analogy: teams of experts each "really really good" at a few tools got to the moon; "we didn't land a man on the moon by giving one guy a ton of tools," and MCP has become mainly a *tool*-distribution mechanism, but tools alone (and skills-as-documentation) are not the fundamental fix. ([Domain-Specific Agents](../sources/20260629_spNAUEgq_A8.md), 08:33-09:56, 15:27-16:20)
- Specialists can be nested recursively (coordinator → Salesforce → Google Workspace + asset-gen → legal → GDPR → OSHA), which lets a large domain context (e.g. ~45MB of GDPR rules) live in its own sub-agent instead of bloating the parent, keeping every context window small. ([Domain-Specific Agents](../sources/20260629_spNAUEgq_A8.md), 27:56-30:07)
- Framing bet: rest of 2026 sees a rapid uptick in domain-specific-agent frameworks (Vercel's Eve is cited as the first to publicly use the term), and 2027 is called "the year of multi-agent orchestration." ([Domain-Specific Agents](../sources/20260629_spNAUEgq_A8.md), 21:00-22:32)

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Domain-specific agents unlock small models and tight permissions](domain-specific-agents-unlock-small-models-and-tight-permissions.md)
- [Use subagents to isolate context-heavy subtasks](use-subagents-to-isolate-context-heavy-subtasks.md)
- [Split broad automation surfaces into specialized subagents and subworkflows](split-large-automation-surfaces-into-specialized-subagents-and-subworkflows.md)
- [Treat multi-agent systems as distributed systems](treat-multi-agent-systems-as-distributed-systems.md)
- [Use skills for workflow guidance and MCP for integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)

Sources:
- [The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents](../sources/20260629_spNAUEgq_A8.md), 09:59-16:20, 27:56-30:07
