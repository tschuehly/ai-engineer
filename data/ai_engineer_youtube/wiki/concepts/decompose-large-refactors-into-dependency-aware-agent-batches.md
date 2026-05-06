# Decompose Large Refactors Into Dependency-Aware Agent Batches

Summary: Large refactors become tractable for parallel coding agents when the codebase is decomposed into dependency-aware, PR-sized batches. The batch should be small enough for one agent to complete and one human to review, while the dependency graph controls which batches can safely run or merge next.

Use when:
- Planning framework migrations, dependency upgrades, CVE remediation, or modernization work that touches many files.
- Deciding whether to split a refactor across parallel agents or keep it as a single serial task.

Details:
- The OpenHands workflow treats large refactors as sprawling interconnected changes that can touch hundreds of files, not as ordinary single-agent tasks. (18:28-18:56)
- Dependency graphs expose file import relationships and can be collapsed into a simpler graph where nodes are batches and edges are inherited dependencies between those batches. (19:11-20:43)
- Batching can use graph algorithms when structural guarantees matter, but existing directory structure can be sufficient when it keeps semantically related files together. (19:52-20:08)
- A good batch fits in a single commit or pull request, can be one-shot by a single agent, can be verified quickly, and has clear ordering relative to other batches. (27:36-29:00)
- Shared migration context should be placed on an initial branch before spawning agents so each worker understands the target transition, such as a Redux-to-Zustand or Spark 2-to-Spark 3 migration. (16:37-17:25)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Run parallel issue agents in sandboxes with review and merge loops](run-parallel-issue-agents-in-sandboxes-with-review-and-merge-loops.md)
- [Spatial agent maps expose filesystem-level lineage and collisions](spatial-agent-maps-expose-filesystem-level-lineage-and-collisions.md)
- [Limit agent change size by feedback speed](limit-agent-change-size-by-feedback-speed.md)

Sources:
- [Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands](../sources/20260108_rcsliSIy_YU.md), 16:37-29:00
