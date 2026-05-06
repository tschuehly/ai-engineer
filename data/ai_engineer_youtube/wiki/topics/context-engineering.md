# Context Engineering

## Overview

Context engineering treats prompts, skills, memory, retrieval, and documentation as an engineered substrate for agent work. It needs a lifecycle similar to software delivery: generate context, evaluate it, distribute it, observe its use, and adapt it from feedback. Demand-driven context adds a practical enterprise workflow: rather than predicting every context need upfront, assign real work to agents, observe failures, and convert missing institutional knowledge into reusable context blocks. A context engine is the selection and reasoning layer for this substrate: it should combine task relevance, user and team signals, source relationships, permissions, and conflict handling rather than relying on generic RAG, many MCP servers, or larger context windows alone. Small-model preprocessing can further manage context by filtering, classifying, extracting, or reranking data before it reaches the agent. Skills and context packages distribute reusable workflow guidance, but package-like reuse also creates versioning, dependency, quality, and security concerns.

## Key Concepts

- [Enterprise agent failures often expose missing institutional knowledge](../concepts/enterprise-agent-failures-expose-missing-institutional-knowledge.md) - agent failures can indicate missing or stale enterprise knowledge rather than weak model reasoning.
- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](../concepts/demand-driven-context-pulls-knowledge-from-failed-work.md) - real tasks reveal the exact context that needs to be documented.
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](../concepts/context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md) - reusable knowledge units make enterprise context easier for agents to retrieve and apply.
- [Evaluate retrieval and MCP layers by task value, not only response availability](../concepts/evaluate-retrieval-and-mcp-layers-by-task-value.md) - connector output should be judged by its contribution to task completion.
- [Use small models as context-management tools before agent reasoning](../concepts/use-small-models-as-context-management-tools-before-agent-reasoning.md) - preprocessing, filtering, and extraction can reduce context rot before context reaches the agent.
- [Agent skills package progressive-disclosure context for repeatable workflows](../concepts/agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md) - skill metadata can keep initial context small while making deeper instructions discoverable.
- [Context engines select task-specific organizational context](../concepts/context-engines-select-task-specific-organizational-context.md) - context engines should personalize and narrow organizational context for the current task.
- [Surface unresolved context conflicts to agents and users](../concepts/surface-unresolved-context-conflicts-to-agents-and-users.md) - unresolved contradictions should become explicit handoff points rather than hidden guesses.
- [Do not cache context-engine answers as durable truth](../concepts/do-not-cache-context-engine-answers-as-durable-truth.md) - generated answers can become stale or self-reinforcing if reused as canonical context.
- [Use social and expert graphs to personalize coding-agent context](../concepts/use-social-and-expert-graphs-to-personalize-coding-agent-context.md) - reviewer and contribution graphs can help route context to likely owners and experts.
- [Context development lifecycle treats context as an engineered artifact](../concepts/context-development-lifecycle-treats-context-as-an-engineered-artifact.md) - context should move through generate, evaluate, distribute, observe, and adapt loops.
- [Evaluate context changes with lint, task scenarios, and probabilistic budgets](../concepts/evaluate-context-changes-with-lint-task-scenarios-and-probabilistic-budgets.md) - prompt and skill changes need validation because small context edits can change generated behavior.
- [Package reusable context as skills, libraries, and registries](../concepts/package-reusable-context-as-skills-libraries-and-registries.md) - shared context needs package, registry, dependency, and security practices.
- [Use agent logs and review feedback as context observability signals](../concepts/use-agent-logs-and-review-feedback-as-context-observability-signals.md) - logs, reviews, and production failures should feed durable context improvements.
- [Filter untrusted context before it reaches the agent](../concepts/filter-untrusted-context-before-it-reaches-the-agent.md) - repository and marketplace context needs screening before model ingestion.

## Open Questions

- What minimum metadata should each context block include so retrieval systems can select it reliably for future tasks?
- How often should teams rescan or revalidate context blocks when source systems change?
- Which context-management tasks should be implemented with deterministic code, retrieval, or small-model inference?
- How should teams decide what belongs in `SKILL.md` versus referenced files or tool descriptions?
- Which parts of a context engine can be cached safely as source-backed structure, and which generated answers must be recomputed from current sources?
- What metadata should context packages expose so teams can evaluate provenance, version compatibility, dependencies, and security risk before installation?

## Sources

- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md)
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
- [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](../sources/20260504_GmAQKINjv1E.md)
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md)
- [Context Is the New Code - Patrick Debois, Tessl](../sources/20260503_bSG9wUYaHWU.md)
