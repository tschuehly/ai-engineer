# Use component inventories to preserve bug-hunting context

Summary: Bug-hunting agents reason better when they first build an explicit inventory of relevant components, relationships, and changed code. This mitigates context compaction and lost cross-file links during repository navigation.

Use when:
- An agent needs to find complex multi-step bugs across a larger codebase.
- A bug investigation spans classes, variables, diffs, and usage paths that may fall out of context.

Details:
- The talk says agents often lose logical links to code they already read, especially after context limits trigger summarization or compaction. That weakens their ability to detect complex bugs nested deeply in a codebase. (02:24-02:48, 04:26-04:44)
- Users should manage the agent's context by feeding changed-code diffs, keeping key files from being summarized out of the context window, and preserving cause-and-effect evidence. (04:44-05:05)
- A practical mitigation is to ask the agent for a step-by-step component inventory that indexes classes, variables, and usage across the codebase before bug finding. The talk reports that this made agents more able to find bugs in benchmarking. (05:05-05:24)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [Plan coding-agent work through feature inventories and dependency graphs](plan-coding-agent-work-through-feature-inventories-and-dependency-graphs.md)
- [Review research and plans before they multiply into code](review-research-and-plans-before-they-multiply-into-code.md)

Sources:
- [How to Improve your Vibe Coding - Ian Butler](../sources/20250803_g03m-WFEu1U.md), 02:24-02:48, 04:26-05:24
