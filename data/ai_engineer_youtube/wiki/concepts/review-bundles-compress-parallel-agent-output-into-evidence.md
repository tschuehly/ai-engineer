# Review Bundles Compress Parallel Agent Output Into Evidence

Summary: Review bundles turn many autonomous agent PRs into compact review artifacts that explain tasks, changes, rationale, and visual evidence. They help keep review from becoming the new bottleneck after agents generate work in parallel.

Use when:
- Reviewing many agent-generated PRs or implementation attempts.
- Designing handoff artifacts for autonomous feature, UI, or maintenance work.

Details:
- After channels or autonomous agent runs create many PRs, the human still needs a way to decide what is worth accepting. 06:45-07:10
- AgentCraft review bundles show what changed in each output, why agents made those changes, and which tasks were attempted. 07:03-07:16
- Visual evidence such as screenshots and videos lets the reviewer inspect UI-facing results without replaying the whole session manually. 07:16-07:25
- Salomon frames this as shifting more effort from planning into review: running multiple attempts can be reasonable only when selection is supported by clear evidence. 07:30-07:43

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)
- [Use parent agents to compare and merge parallel subagent outputs](use-parent-agents-to-compare-and-merge-parallel-subagent-outputs.md)
- [Let agents propose quest queues for parallel work](let-agents-propose-quest-queues-for-parallel-work.md)

Sources:
- [AgentCraft: Putting the Orc in Orchestration - Ido Salomon](../sources/20260425_kR64LOqBBCU.md), 06:45-07:43
