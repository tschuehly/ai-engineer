# Model a Managed Agent as Agent, Environment, and Session

Summary: Three primitives are enough to describe a hosted agent runtime: an **agent** (model, prompts, tools, skills), an **environment** (a container definition, instantiated fresh per session), and a **session** (agent + environment, persisted as a durable cloud resource). The payoff of naming them separately is that each has a different lifetime — a definition you version, an image you build, a run you resume — and a runtime that conflates any two of them loses a capability.

Use when:
- Designing the object model or API for an agent platform and needing the minimal set of nouns.
- Deciding what is versioned, what is templated, and what is instantiated per run.
- Reasoning about what "resuming an agent" can even mean in a given architecture.

Details:
- **The three primitives as stated.** An *agent* is "the model, the prompts, the tools and the skills." An *environment* is the container, and crucially it is a definition rather than an instance: multiple sessions can run against one environment definition, "each with its own isolated container instance." A *session* is an agent plus an environment, and is "a durable resource persisted in the cloud of every single interaction." ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 12:56-13:44)
- **The definition/instance split in the environment is the load-bearing part.** Because the environment is a template, isolation between concurrent sessions is a property of the model rather than something the operator has to arrange, and the environment can carry policy that applies to every instance — the demo's "SRE sandbox" ships with "the networking limited and allowed hosts only being the MCP server," so egress policy is attached to the definition and inherited by every run. (18:30-19:20)
- **The four session states.** *Idle* — created but not running. *Running*. *Rescheduling* — an error occurred and the session is being retried. *Terminated* — an unrecoverable state. Rescheduling is the one worth noticing: making retry a first-class state rather than a loop inside the harness is what lets the platform own recovery, and it is the state that [decoupling the loop from the tool environment](decouple-the-agent-loop-from-the-tool-execution-environment.md) makes reachable, since a new sandbox can be attached to the same session. (13:51-14:43)
- **What each primitive buys you when it is separate.** Agent separate from environment: swap the model without rebuilding the container, which is the mechanic behind treating the harness as a model-evolution boundary. Environment definition separate from instance: policy and dependencies are declared once. Session separate from both: a run outlives the process executing it, so resumption is possible at all.
- **The scope this claim actually has.** These are the primitives of a *managed* runtime — a platform whose job is to run other people's agents. A single-tenant agent that runs in one process may reasonably collapse all three, and the cost of doing so is exactly the list above: no concurrent isolation, no policy inheritance, no resume. That is the tradeoff to evaluate rather than a rule to follow.
- Provenance: an Anthropic vendor talk describing the object model of Claude managed agents. It is a design account of one product, not a survey and not a validated abstraction — no alternative decomposition is discussed, and no failure of a different object model is reported. Treat it as a well-specified reference point rather than the settled vocabulary.
- **Two variables this decomposition holds fixed that another platform makes free.** Warp's cloud platform varies the *harness* — users bring Claude Code, Codex, or their own — which means the "agent" primitive here splits further into a definition the platform holds and an executor the user chooses, and the session's state has to be storable and rehydratable across that boundary ([Support Many Harnesses by Owning Conversation State and Artifacts](support-many-harnesses-by-owning-conversation-state-and-artifacts.md)). It also varies *who operates the environment*: after starting with managed sandboxes, the team added self-hosting because "for teams doing serious work… something that is hosted or managed is usually not sufficient" ([Ship Managed and Self-Hosted Sandboxes Because Serious Teams Bring Their Own Infrastructure](ship-managed-and-self-hosted-sandboxes-because-serious-teams-bring-their-own-infrastructure.md)). Both are worth noting against the environment-definition claim above, because policy inherited by every instance is a guarantee the platform can only make on infrastructure it runs. ([Abdalla](../sources/20260822_L173Z8DpaJg.md), 04:12-06:24)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Decouple the Agent Loop From the Tool Execution Environment](decouple-the-agent-loop-from-the-tool-execution-environment.md)
- [Keep the Session Log Separate From the Context Window](keep-the-session-log-separate-from-the-context-window.md)
- [Decide the Agent Buy Boundary With Six Production Questions](decide-the-agent-buy-boundary-with-six-production-questions.md)
- [Use stable agent harnesses as model-evolution boundaries](use-stable-agent-harnesses-as-model-evolution-boundaries.md)
- [Agent Harnesses Combine Model, Tools, Prompts, Filesystem, Skills, Hooks, and Memory](agent-harnesses-combine-model-tools-prompts-filesystem-skills-hooks-and-memory.md)
- [Support Many Harnesses by Owning Conversation State and Artifacts](support-many-harnesses-by-owning-conversation-state-and-artifacts.md)
- [Ship Managed and Self-Hosted Sandboxes Because Serious Teams Bring Their Own Infrastructure](ship-managed-and-self-hosted-sandboxes-because-serious-teams-bring-their-own-infrastructure.md)

Sources:
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 12:56-14:43, 18:30-19:20
- [The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp](../sources/20260822_L173Z8DpaJg.md), 04:12-06:24
