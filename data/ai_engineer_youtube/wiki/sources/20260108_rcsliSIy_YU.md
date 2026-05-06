# Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands

Source: [Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands](https://www.youtube.com/watch?v=rcsliSIy_YU)
Uploaded: 2026-01-08
Transcript: `raw/20260108_rcsliSIy_YU/rcsliSIy_YU.en-orig.vtt`

## Summary

Robert Brennan frames large refactors, dependency upgrades, CVE remediation, and framework migrations as too large for single-agent one-shots but well suited to orchestrated parallel agents when the work is decomposed into reviewable, verifiable batches. The talk emphasizes dependency-aware batching, shared migration context, intermediate human review, isolated cloud sandboxes, and verify-fix-review loops that let humans merge small PR-sized outputs while agents handle repeatable maintenance toil.

## Extracted Concepts

- [Decompose large refactors into dependency-aware agent batches](../concepts/decompose-large-refactors-into-dependency-aware-agent-batches.md) - this source describes using dependency graphs, directory structure, and PR-sized batches to make large refactors parallelizable and reviewable.
- [Run verify-fix-review loops for agentic refactors](../concepts/run-verify-fix-review-loops-for-agentic-refactors.md) - this source shows a loop where verifiers find problems, fixer agents produce small PRs, humans review and merge, and newly unblocked batches continue.

## Topic Links

- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

## Notes

- Large-scale software maintenance work such as dependency updates, CVE remediation, code modernization, and framework migrations is described as repeatable and automatable, but often too large for a single agent prompt or one-shot run. (08:51-11:41)
- Cloud-based sandboxes make concurrent agents safer and more scalable than local laptop runs because an agent can damage only its own isolated environment and does not require constant command approval. (06:41-07:23)
- The recommended orchestration flow starts with a branch carrying shared migration context, optionally adds scaffolding, then launches multiple agents that submit work back into that branch before final cleanup and merge. (16:37-17:25)
- Beginners should limit themselves to roughly three to five concurrent agents until they have a reliable human-input loop; mature orchestration can fan out much further when review is delegated to downstream teams or clear PR gates. (17:28-18:01)
- Dependency visualization can turn hundreds of files into human-sized batches; a batch should be small enough for one agent to handle and one human to understand. (19:11-20:08)
- The refactor workflow uses a verifier to identify problems, a fixer to address them, human review and merge for resulting PRs, then repeats as dependency-order progress unblocks later batches. (24:56-26:57)
- Effective decomposition looks for tasks a single agent can one-shot, tasks that fit in one commit or PR, work that can run in parallel, quick verification such as CI or manual app checks, and clear dependencies between tasks. (27:36-29:00)
