# Context Engineering

## Overview

Context engineering treats prompts, skills, memory, retrieval, and documentation as an engineered substrate for agent work. Demand-driven context adds a practical enterprise workflow: rather than predicting every context need upfront, assign real work to agents, observe failures, and convert missing institutional knowledge into reusable context blocks. Small-model preprocessing can further manage context by filtering, classifying, extracting, or reranking data before it reaches the agent. Skills are a packaging mechanism for this context: a small description can trigger deeper workflow instructions, reference files, or scripts only when the task needs them.

## Key Concepts

- [Enterprise agent failures often expose missing institutional knowledge](../concepts/enterprise-agent-failures-expose-missing-institutional-knowledge.md) - agent failures can indicate missing or stale enterprise knowledge rather than weak model reasoning.
- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](../concepts/demand-driven-context-pulls-knowledge-from-failed-work.md) - real tasks reveal the exact context that needs to be documented.
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](../concepts/context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md) - reusable knowledge units make enterprise context easier for agents to retrieve and apply.
- [Evaluate retrieval and MCP layers by task value, not only response availability](../concepts/evaluate-retrieval-and-mcp-layers-by-task-value.md) - connector output should be judged by its contribution to task completion.
- [Use small models as context-management tools before agent reasoning](../concepts/use-small-models-as-context-management-tools-before-agent-reasoning.md) - preprocessing, filtering, and extraction can reduce context rot before context reaches the agent.
- [Agent skills package progressive-disclosure context for repeatable workflows](../concepts/agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md) - skill metadata can keep initial context small while making deeper instructions discoverable.

## Open Questions

- What minimum metadata should each context block include so retrieval systems can select it reliably for future tasks?
- How often should teams rescan or revalidate context blocks when source systems change?
- Which context-management tasks should be implemented with deterministic code, retrieval, or small-model inference?
- How should teams decide what belongs in `SKILL.md` versus referenced files or tool descriptions?

## Sources

- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md)
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
- [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](../sources/20260504_GmAQKINjv1E.md)
