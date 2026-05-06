# Retrieval

## Overview

Retrieval gives agents access to institutional systems such as Confluence, Jira, SharePoint, GitHub, Slack, knowledge graphs, and file-backed knowledge bases. The useful retrieval layer is not the one with the most connectors, but the one that provides accurate, task-relevant context and exposes gaps when the source knowledge is missing or stale. Small models can improve this layer by embedding, reranking, extracting entities, filtering inputs, or building structured knowledge targets.

## Key Concepts

- [Context blocks turn monolithic enterprise knowledge into reusable agent context](../concepts/context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md) - decomposed context units give retrieval systems cleaner targets than broad documentation monoliths.
- [Evaluate retrieval and MCP layers by task value, not only response availability](../concepts/evaluate-retrieval-and-mcp-layers-by-task-value.md) - retrieval must be tested against whether it helps complete work.
- [Use small models as context-management tools before agent reasoning](../concepts/use-small-models-as-context-management-tools-before-agent-reasoning.md) - embeddings, rerankers, NER, and extraction models can structure or filter retrieval inputs before agent reasoning.

## Open Questions

- How should retrieval systems route between source-of-truth systems and curated context blocks when they disagree?
- Which retrieval steps benefit from hot-swappable small models rather than a single general embedding or reranking service?

## Sources

- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md)
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
