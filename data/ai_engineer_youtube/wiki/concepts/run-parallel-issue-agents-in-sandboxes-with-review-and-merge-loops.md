# Run Parallel Issue Agents in Sandboxes With Review and Merge Loops

Summary: Parallel coding-agent work needs an explicit issue planner, isolated execution sandboxes, review of created commits, and a merge loop that handles integration failures. The parallelism works when dependency phases and branch ownership are clear enough that implementers can run independently.

Use when:
- Turning a backlog or PRD into parallel autonomous coding tasks.
- Designing orchestration around multiple coding agents and branches.

Details:
- The described flow starts with a planner that reads the backlog, chooses several issues, and accounts for blocking relationships or phases before parallel execution. (01:30:58-01:31:18)
- Each issue gets a sandbox and branch; an implementer receives the issue number, title, and branch, then creates commits if it can complete the work. (01:31:24-01:31:51)
- A review step inspects created commits before they are passed to a merger agent. (01:31:47-01:31:59)
- The merger agent takes the created branches and issues, merges them, and resolves integration problems such as type and test failures. (01:31:58-01:32:15)
- The speaker routes coding standards into the reviewer and allows the implementer to pull relevant context, with a stronger model used for review than implementation. (01:32:23-01:32:44)
- Large refactors add a dependency-graph variant of the same pattern: start from shared migration context, split the codebase into PR-sized batches, run agents in dependency order, and merge reviewed outputs as they unblock later batches. (16:37-29:00)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)
- [Use parent agents to compare and merge parallel subagent outputs](use-parent-agents-to-compare-and-merge-parallel-subagent-outputs.md)
- [Isolate parallel coding work with project worktrees](isolate-parallel-coding-work-with-project-worktrees.md)
- [Decompose large refactors into dependency-aware agent batches](decompose-large-refactors-into-dependency-aware-agent-batches.md)
- [Run verify-fix-review loops for agentic refactors](run-verify-fix-review-loops-for-agentic-refactors.md)

Sources:
- [Full Walkthrough: Workflow for AI Coding - Matt Pocock](../sources/20260424_-QFHIoCo-Ko.md), 01:30:58-01:32:44
- [Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands](../sources/20260108_rcsliSIy_YU.md), 16:37-29:00
