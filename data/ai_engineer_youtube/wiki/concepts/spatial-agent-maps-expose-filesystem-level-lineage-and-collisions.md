# Spatial Agent Maps Expose Filesystem-Level Lineage and Collisions

Summary: A spatial orchestration interface can show where each agent is working in the repository, which files changed, and whether parallel work streams are likely to collide. This makes multi-agent activity easier to audit than separate terminal logs or chat panes.

Use when:
- Designing UI for many coding agents working in the same codebase.
- Evaluating how to detect duplicate or conflicting parallel edits before review.

Details:
- AgentCraft represents coding-agent sessions as visible units that can be detected from local tools or spawned from the orchestration surface. 02:10-02:32
- Its map projects the filesystem into spatial regions: directories appear as map areas and files as rooms, letting the operator see which file an agent is working on. 03:36-04:21
- Because the orchestrator observes changes, it can show a changelist and preserve lineage over which agent changed what and when. 04:21-04:31
- The same activity data can feed heat maps for likely collisions, making it possible to visualize and potentially prevent overlapping edits before they become merge or review problems. 04:33-04:44

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)
- [Shared canvases expose multi-agent state and coordination](shared-canvases-expose-multi-agent-state-and-coordination.md)

Sources:
- [AgentCraft: Putting the Orc in Orchestration - Ido Salomon](../sources/20260425_kR64LOqBBCU.md), 02:10-04:44
