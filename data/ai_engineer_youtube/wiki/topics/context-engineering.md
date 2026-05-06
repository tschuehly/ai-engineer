# Context Engineering

## Overview

Context engineering treats prompts, skills, memory, retrieval, and documentation as an engineered substrate for agent work. Demand-driven context adds a practical enterprise workflow: rather than predicting every context need upfront, assign real work to agents, observe failures, and convert missing institutional knowledge into reusable context blocks.

## Key Concepts

- [Enterprise agent failures often expose missing institutional knowledge](../concepts/enterprise-agent-failures-expose-missing-institutional-knowledge.md) - agent failures can indicate missing or stale enterprise knowledge rather than weak model reasoning.
- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](../concepts/demand-driven-context-pulls-knowledge-from-failed-work.md) - real tasks reveal the exact context that needs to be documented.
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](../concepts/context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md) - reusable knowledge units make enterprise context easier for agents to retrieve and apply.
- [Evaluate retrieval and MCP layers by task value, not only response availability](../concepts/evaluate-retrieval-and-mcp-layers-by-task-value.md) - connector output should be judged by its contribution to task completion.

## Open Questions

- What minimum metadata should each context block include so retrieval systems can select it reliably for future tasks?
- How often should teams rescan or revalidate context blocks when source systems change?

## Sources

- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md)
