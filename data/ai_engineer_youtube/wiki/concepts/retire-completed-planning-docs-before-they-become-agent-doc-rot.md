# Retire Completed Planning Docs Before They Become Agent Doc Rot

Summary: Planning artifacts can become harmful retrieval context after implementation because the code, file structure, names, and requirements keep changing. Completed PRDs should be closed, removed from default agent context, or clearly marked as no longer current so agents do not treat stale plans as source truth.

Use when:
- Deciding whether generated PRDs, Markdown plans, or issue drafts should remain in a repository.
- Debugging agents that follow outdated planning documents instead of current code and tests.

Details:
- The source warns that an old PRD can mislead a later agent when the real implementation has diverged from the original plan. (01:24:19-01:24:46)
- Drift can include renamed concepts, changed file structure, changed requirements, and user-tested learnings that invalidate the original plan. (01:24:28-01:24:40)
- The speaker's preferred GitHub Issues workflow closes completed planning artifacts so they remain fetchable if needed but no longer appear as live work context. (01:24:50-01:25:05)
- Database migrations are treated as a different case because they are deterministic records of what changed, not speculative planning context. (01:25:41-01:26:08)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Fresh Markdown context mitigates model rot in codegen](fresh-markdown-context-mitigates-model-rot-in-codegen.md)
- [Do not cache context-engine answers as durable truth](do-not-cache-context-engine-answers-as-durable-truth.md)
- [Filter untrusted context before it reaches the agent](filter-untrusted-context-before-it-reaches-the-agent.md)

Sources:
- [Full Walkthrough: Workflow for AI Coding - Matt Pocock](../sources/20260424_-QFHIoCo-Ko.md), 01:24:19-01:26:08

