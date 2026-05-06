# Retrieval

## Overview

Retrieval gives agents access to institutional systems such as Confluence, Jira, SharePoint, GitHub, Slack, knowledge graphs, and file-backed knowledge bases. The useful retrieval layer is not the one with the most connectors, but the one that provides accurate, task-relevant context and exposes gaps when the source knowledge is missing, stale, contradictory, or unavailable to the current user. Personal Markdown knowledge bases can play the same role at individual scale when saved links, notes, tasks, and project records are indexed, tagged, connected, and resurfaced when relevant. Context engines add a reasoning layer over retrieval by personalizing results to the task, team, permissions, and source relationships. Small models can improve this layer by embedding, reranking, extracting entities, filtering inputs, or building structured knowledge targets.

## Key Concepts

- [Context blocks turn monolithic enterprise knowledge into reusable agent context](../concepts/context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md) - decomposed context units give retrieval systems cleaner targets than broad documentation monoliths.
- [Evaluate retrieval and MCP layers by task value, not only response availability](../concepts/evaluate-retrieval-and-mcp-layers-by-task-value.md) - retrieval must be tested against whether it helps complete work.
- [Use small models as context-management tools before agent reasoning](../concepts/use-small-models-as-context-management-tools-before-agent-reasoning.md) - embeddings, rerankers, NER, and extraction models can structure or filter retrieval inputs before agent reasoning.
- [Context engines select task-specific organizational context](../concepts/context-engines-select-task-specific-organizational-context.md) - retrieval needs task and user relevance, not just available chunks.
- [Surface unresolved context conflicts to agents and users](../concepts/surface-unresolved-context-conflicts-to-agents-and-users.md) - contradictory retrieved sources should be resolved or exposed.
- [Do not cache context-engine answers as durable truth](../concepts/do-not-cache-context-engine-answers-as-durable-truth.md) - answer reuse can preserve stale code, docs, or model mistakes.
- [Use social and expert graphs to personalize coding-agent context](../concepts/use-social-and-expert-graphs-to-personalize-coding-agent-context.md) - contribution and review signals can bias retrieval toward relevant repositories and experts.
- [Personal knowledge bases become agent context substrates](../concepts/personal-knowledge-bases-become-agent-context-substrates.md) - personal retrieval becomes more useful when ingestion adds context and links to existing notes.

## Open Questions

- How should retrieval systems route between source-of-truth systems and curated context blocks when they disagree?
- Which retrieval steps benefit from hot-swappable small models rather than a single general embedding or reranking service?
- How should Graph RAG or graph summarization systems preserve permission boundaries when summaries cross source scopes?
- How should personal retrieval distinguish durable notes from stale bookmarks and noisy saved material?

## Sources

- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md)
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md)
- [I Gave an AI Agent the Keys to My Life (Here's What Happened) - Radek Sienkiewicz (@velvetshark-com)](../sources/20260502_sJ2jc7leKBk.md)
