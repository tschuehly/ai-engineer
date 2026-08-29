# An Agent Is an Expert Who Onboards Again on Every Task

Summary: The right mental model for a coding agent is not a junior engineer and not a search engine: it is an expert software engineer on their first day, repeated. Capability is high, organizational knowledge is zero, and the reset happens per task rather than once per hire — which means the onboarding cost never amortizes and the fix is onboarding material, not a smarter model.

Use when:
- Deciding what to write down for agents, and in what form.
- Explaining to a team why agent output is competent but wrong about *this* codebase.
- Estimating the value of a context layer: the multiplier is task volume, not headcount.
- Pushing back on "the next model will fix it" as a reason not to invest in organizational context.

Details:
- The framing: "agents are like new employees. They reset their knowledge every time you start a new task… you can think of an agent like an expert software engineer who's a new employee onboarding for the first time. Every time they have to rediscover your codebase, how your organization builds tests and how they deploy software with each and every task." ([Werry](../sources/20260827_qdAkxLoYNI8.md), 01:52-02:18)
- The half that changes the economics is "every task," not "new employee." A human onboards once and the cost is amortized over years of work; an agent pays it per invocation, so the same per-task cost multiplied by agent-task volume is what a context layer is actually buying down.
- The half that changes the *diagnosis* is "expert." The deficit is organizational, not intellectual, so it does not shrink as models improve — a better model rediscovers your deployment conventions faster, but still rediscovers them. This is the same separation the wiki records elsewhere between raw intelligence and situated expertise. See [Separate Intelligence From Expertise When Diagnosing an Agent](separate-intelligence-from-expertise-when-diagnosing-agents.md).
- What the agent inherits and what it does not. Werry's setup is that "for years you were the context layer," trawling data sources, discussions, and the codebase, while the organization accumulated "battle scars" from incidents and architecture decisions. Agents "suffer from all of these challenges except for one thing" — they also reset. The scar tissue is exactly the part that was never written down. (00:58-01:52)
- The artifact this implies is onboarding material — how we build, how we test, how we deploy, what we decided and why — which is a different corpus from API docs and a different corpus from code. It is also the corpus most likely not to exist, because employees only need it once.
- Practical consequence for prioritization: rank what to write down by (frequency the agent hits it) × (cost when it guesses wrong), which is not the same ranking a human onboarding guide would use. A human asks a colleague when stuck; the agent guesses plausibly and continues.
- The complement, which this page should not be read without: waiting to write everything down first is the failure mode on the other side. Give agents real work, watch where they fail or ask, and convert *that* into context. See [Demand-Driven Context Pulls Knowledge From Failed Work](demand-driven-context-pulls-knowledge-from-failed-work.md).
- Limit: the framing is an analogy offered without measurement. The source gives no figure for per-task rediscovery cost, and the one cost comparison it does report is a single unreplicated pair of runs.

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Demand-driven context pulls knowledge from failed work](demand-driven-context-pulls-knowledge-from-failed-work.md)
- [Enterprise agent failures expose missing institutional knowledge](enterprise-agent-failures-expose-missing-institutional-knowledge.md)
- [Separate Intelligence From Expertise When Diagnosing an Agent](separate-intelligence-from-expertise-when-diagnosing-agents.md)
- [Institutionalize knowledge infrastructure for AI adoption](institutionalize-knowledge-infrastructure-for-ai-adoption.md)
- [Context engines select task-specific organizational context](context-engines-select-task-specific-organizational-context.md)
- [Measure a Context Layer on Compounding, Not on the First Task](measure-a-context-layer-on-compounding-not-the-first-task.md)

Sources:
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 00:58-02:18
