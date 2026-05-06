# Design Coding-Agent Editors as Review Surfaces

Summary: When agents produce most code changes, the editor becomes less a typing surface and more a review, navigation, and comprehension surface. Interfaces should expose enough agent activity and diff structure for humans to understand and safely accept or revise the change.

Use when:
- Designing editor or terminal UX for coding agents.
- Reviewing whether an agent product helps humans understand generated changes.
- Improving review throughput for agent-produced code.

Details:
- Amp's terminal UI streams diffs and shows CLI commands while avoiding every token of model explanation, balancing observability with overload. (01:27-01:49)
- Editor integrations can collect diagnostics from tools such as Emacs, Neovim, and JetBrains so the coding agent sees task-relevant feedback from the developer's environment. (01:53-02:05)
- The source frames the editor as a reader once agents drive most edits through an agent panel, with human attention moving to review. (11:21-11:54)
- Amp's review interface supports arbitrary commit ranges, quick file-level diffs, editable diffs, code navigation, and a guided tour of which files to inspect first; this addresses the practical problem that large generated changes can be hard to enter. (12:00-12:35)
- This strengthens the broader review-interface pattern: agent products should compress changed work into navigable evidence, not merely dump logs or final patches on reviewers.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)
- [Review bundles compress parallel agent output into evidence](review-bundles-compress-parallel-agent-output-into-evidence.md)
- [AI output speed can overwhelm review capacity](ai-output-speed-can-overwhelm-review-capacity.md)

Sources:
- [Amp Code: Next Generation AI Coding - Beyang Liu, Amp Code](../sources/20251222_gvIAkmZUEZY.md), 01:27-02:05, 11:21-12:35
