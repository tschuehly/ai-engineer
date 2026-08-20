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

- This page states the unpriced cost of the doc-as-state pattern. Matt Dailey (Ref) proposes making a durable shared document the state of the work — "separate the agent as the action and the doc as the state" — so that agents restart from it and the team reads it to reconstruct context, but names no owner, no versioning against the code, and no retirement policy for those documents. A living state document is exactly the artifact that rots most expensively, because unlike a completed PRD it is *meant* to be read as current. If you adopt the pattern, its lifecycle is the design work you inherit. See [Make the Doc the State and the Agent the Action](make-the-doc-the-state-and-the-agent-the-action.md). ([Dailey](../sources/20260809_Kz4QJmNrVXU.md), 13:25-14:30)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Fresh Markdown context mitigates model rot in codegen](fresh-markdown-context-mitigates-model-rot-in-codegen.md)
- [Do not cache context-engine answers as durable truth](do-not-cache-context-engine-answers-as-durable-truth.md)
- [Filter untrusted context before it reaches the agent](filter-untrusted-context-before-it-reaches-the-agent.md)
- [Make the Doc the State and the Agent the Action](make-the-doc-the-state-and-the-agent-the-action.md)

Sources:
- [Full Walkthrough: Workflow for AI Coding - Matt Pocock](../sources/20260424_-QFHIoCo-Ko.md), 01:24:19-01:26:08
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../sources/20260809_Kz4QJmNrVXU.md), 13:25-14:30

