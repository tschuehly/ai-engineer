# Agent Enablement Falls Between Platform and Developer Experience, So Name an Owner

Summary: Agent adoption creates a new class of shared infrastructure — skill registries, evaluation systems for context, guardrails specific to coding agents, agent identities — that neither the platform team nor the developer-experience team owns by default: one runs infrastructure without doing development, the other does the reverse. Without a named owner driving it as a program, there are no paved roads and every team rebuilds the same thing.

Use when:
- Deciding which existing group inherits skills, context, and coding-agent guardrails at company scale.
- Several teams have each built their own agent setup and nobody can say who should consolidate them.
- A platform team is focused on infrastructure and cloud and has not noticed the new objects arriving.
- Writing the charter for an AI-enablement or agent-platform group.

Details:
- **The new inventory.** "The platform people might not be paying close attention because they're like infrastructure and cloud and working on like MCP gateway and stuff like that. But there's new things bubbling up there. They need to think about maybe skill registries or eval systems for your context and guardrails specifically for coding agents and identities and stuff. So, they need a little bit of a hand growing to that role." ([Debois](../sources/20260822_zCJtYuqwm7E.md), 10:29-10:56) Each of those four has a page or a cluster in this wiki already; what is new is the observation that they arrive together and land on a team that was not staffed for them.
- **The ownership gap, stated precisely.** "That central role, it's hard. You need an owner to drive that program, but is it the platform team? Is it developer experience team? They don't typically own any of those pieces of the infrastructure and the other people don't really do the development. So, there's somewhere a blend, but you need to make sure that there's an owner driving this centralized piece and not just within your team. Because you won't have paved roads." (10:56-11:26) The gap is structural rather than political: the work needs both the right to run shared infrastructure and enough development practice to know what a good skill or context package is, and the standard org chart splits those.
- **Why "not just within your team" is the load-bearing phrase.** A team can build its own harness and get real value from it; what a team cannot do is make its harness the one other teams find, trust, and extend. That is the same argument [Own Agent Adoption at the Leadership Layer Because the Fixes Are Shared](own-agent-adoption-at-the-leadership-layer-because-the-fixes-are-shared.md) makes one level down, at the IC-versus-leadership boundary. Debois is applying it a second time, at the team-versus-organization boundary, which suggests the rule generalizes: the owner of a shared surface has to sit one level above the people who benefit from it.
- **The mandate is the org layer's actual job.** Debois rejects both the generic transformation playbook — "hackathon, a lunch and learn, let's share the successes, have a shared Slack channel, have a champions program. That's all generic transformation. It could have been Agile… It could have been DevOps" — and the opposite, "let a thousand flowers bloom, it doesn't work." What he advocates instead is narrow: "you give the team leads and the platform that mandate to start doing that work. And it's not the solo developer piece." (14:22-15:09)
- **This is a direct qualification of the wiki's champions pattern.** [Drive Org-Wide Agentic Adoption Through Champions and AI-Ready Repos](drive-org-wide-agentic-adoption-through-champions-and-ai-ready-repos.md) is a well-evidenced rollout mechanism, and Debois's objection is not that it fails but that it is *content-free* — the same shape ran for Agile and DevOps, so its presence tells you nothing about whether the agent-specific infrastructure is being built. Both can be true: run the champions program to seed practice, and separately name someone accountable for the registry, the evals, and the guardrails, because a champion cohort has no standing budget and no operational ownership.
- **What the owner is accountable for, concretely.** Not just hosting the registry but "making it testable… modular, that other people can extend the context, for example, or the harness, that it's security scanned." (12:26-12:44) See [Ship a Catalog of Paved Roads, Not One Standard](ship-a-catalog-of-paved-roads-not-one-standard.md) for the shape of the output and the sprawl it is defending against.
- **Caveats.**
  - Debois does not resolve the question he raises. "There's somewhere a blend" is the answer, with no staffing model, no reporting line, and no example of an organization that named the owner and what happened next.
  - The four objects are listed, not specified. Whether "eval systems for your context" means a CI-integrated harness or a review process is left entirely open — the wiki's [Evaluate Context Changes with Lint, Task Scenarios, and Probabilistic Budgets](evaluate-context-changes-with-lint-task-scenarios-and-probabilistic-budgets.md), from the same speaker's earlier talk, is the closest thing to a definition.
  - No cost is given for the central program, which matters because the argument for it is entirely about avoided duplication and duplication cost is never quantified.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Build Paved Paths for Enterprise AI Engineering Tools](build-paved-paths-for-enterprise-ai-engineering-tools.md)
- [Own Agent Adoption at the Leadership Layer Because the Fixes Are Shared](own-agent-adoption-at-the-leadership-layer-because-the-fixes-are-shared.md)
- [Drive Org-Wide Agentic Adoption Through Champions and AI-Ready Repos](drive-org-wide-agentic-adoption-through-champions-and-ai-ready-repos.md)
- [Ship a Catalog of Paved Roads, Not One Standard](ship-a-catalog-of-paved-roads-not-one-standard.md)
- [Distributed Rule Authoring Is a Platform Problem, Not an Authoring Problem](distributed-rule-authoring-is-a-platform-problem.md)
- [Evaluate Context Changes with Lint, Task Scenarios, and Probabilistic Budgets](evaluate-context-changes-with-lint-task-scenarios-and-probabilistic-budgets.md)
- [First-Class Agent Users Need Identity, Scopes, and Audit Trails](first-class-agent-users-need-identity-scopes-and-audit-trails.md)
- [Institutionalize Knowledge Infrastructure for AI Adoption](institutionalize-knowledge-infrastructure-for-ai-adoption.md)

Sources:
- [Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl](../sources/20260822_zCJtYuqwm7E.md), 10:29-11:26, 12:26-12:44, 14:22-15:09
