# Use Social and Expert Graphs to Personalize Coding-Agent Context

Summary: Social and expert graphs can personalize context by modeling who works on which repositories, who reviews whose PRs, and where expertise lives. Those signals help route deeper retrieval and review context toward the people and code areas most relevant to the task.

Use when:
- Building coding-agent context systems that need to know owners, reviewers, or likely experts.
- Personalizing retrieval across many repositories without giving every agent every organizational artifact.

Details:
- Personalized retrieval can infer a person's focused repositories from PR contribution counts, then search those repositories more deeply while searching the rest of the codebase more broadly. (21:11-22:01)
- Historical PR comments can be distilled into memories so agents see recurring organizational practices when working on similar code. (19:10-19:41)
- The workshop demo builds a local social graph from GitHub repository data to show who reviews whose PRs and who gets reviewed. (43:31-44:36)
- The same graph-building exercise aims to identify experts and which parts of the code they work on, making social structure part of the context engine rather than just a visualization. (43:52-44:08)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Ralph loops process one ticket at a time with fresh context](ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md)
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Context engines select task-specific organizational context](context-engines-select-task-specific-organizational-context.md)

Sources:
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md), 19:10-19:41, 21:11-22:01, 43:31-44:36
