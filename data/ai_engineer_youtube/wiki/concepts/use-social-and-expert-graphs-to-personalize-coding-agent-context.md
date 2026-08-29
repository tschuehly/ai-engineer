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

- **Two more outputs from the same graph, and the operational one is a staffing risk map.** The follow-up talk shows the review-relationship graph clustered into inferred team labels and then projected onto the codebase as a coverage map — "you can see kind of where the holes are, where you might be lacking expert coverage. And that's exactly what we use within the context engine itself." That is a second consumer for a structure built for retrieval: the same edges that route context also tell an engineering manager which areas have one reviewer and no backup. The other output is authority weighting for mined review guidance — "we use the sort of seniority or expertise as a signal to boost comments that are important" — which gives a flat mine of PR history the tiebreak it otherwise lacks. See [Weight Mined Review Guidance by the Author's Expertise](weight-mined-review-guidance-by-the-authors-expertise.md). ([Werry, Aug 2026](../sources/20260827_qdAkxLoYNI8.md), 13:24-13:40, 16:04-16:44)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Ralph loops process one ticket at a time with fresh context](ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md)
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Context engines select task-specific organizational context](context-engines-select-task-specific-organizational-context.md)
- [Weight Mined Review Guidance by the Author's Expertise](weight-mined-review-guidance-by-the-authors-expertise.md)

Sources:
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md), 19:10-19:41, 21:11-22:01, 43:31-44:36
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 13:24-13:40, 16:04-16:44
