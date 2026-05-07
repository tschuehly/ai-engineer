# No Vibes Allowed: Solving Hard Problems in Complex Codebases - Dex Horthy, HumanLayer

Source: [No Vibes Allowed: Solving Hard Problems in Complex Codebases - Dex Horthy, HumanLayer](https://www.youtube.com/watch?v=rmvDxxNubIg)
Uploaded: 2025-12-02
Transcript: `raw/20251202_rmvDxxNubIg/rmvDxxNubIg.en-orig.vtt`

## Summary

Dex Horthy argues that coding agents can work in complex brownfield codebases when teams deliberately manage the context window instead of treating a long chat as durable understanding. The talk frames frequent intentional compaction as a workflow for keeping agents in a high-quality context regime: research compresses codebase truth, planning compresses human intent, implementation starts from a narrow reviewed plan, and human review preserves mental alignment as generated-code throughput rises.

## Extracted Concepts

- [Frequent intentional compaction keeps coding agents in the smart zone](../concepts/frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md) - this source names and details the workflow of repeatedly compressing useful state into reviewed Markdown artifacts.
- [Review research and plans before they multiply into code](../concepts/review-research-and-plans-before-they-multiply-into-code.md) - this source explains why wrong research or plans have higher blast radius than a single bad line of generated code.
- [Use research-plan-implement loops for coding agents](../concepts/use-research-plan-implement-loops-for-coding-agents.md) - this source adds the context-compaction rationale behind the research, plan, and implementation phases.
- [Keep agent context small, fresh, and task-specific](../concepts/keep-agent-context-small-fresh-and-task-specific.md) - this source contributes the "smart zone" framing and warnings about bloated MCP/tool context.

## Topic Links

- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

## Notes

- The talk starts from the problem that greenfield demos can work while mature codebases produce churn, rework, and "slop" unless teams improve context management for current models. 00:53-02:00
- Intentional compaction means asking an agent to compress useful session state into a Markdown file, reviewing and tagging that artifact, then starting a new agent with the compacted state instead of carrying an entire noisy conversation forward. 03:47-04:06
- Horthy frames context quality by correctness, completeness, size, and trajectory; incorrect information is worse than missing information, and repeated correction/yelling can become a harmful trajectory inside the model's active context. 04:38-05:43
- Subagents are useful for context control, not role theater: a subagent can read broadly through a codebase and return a succinct finding so the parent reads only the relevant file or conclusion. 06:35-07:27
- The research-plan-implement workflow keeps context small by separating codebase understanding, explicit file-and-test planning, and implementation from a reviewed low-context plan. 07:31-08:25
- Static onboarding docs can grow too long or stale in large repositories; on-demand compressed context can instead build a task-specific, code-backed snapshot of the parts that matter. 12:14-14:10
- Code review preserves mental alignment about how and why the codebase changes; plans and agent transcripts can help reviewers follow the steps, prompts, build results, and manual testing behind a larger generated diff. 14:56-16:00
- The workflow is not a perfect prompt or a substitute for thinking: a bad research note can send the whole implementation in the wrong direction, so human attention should move to the highest-leverage research and plan checkpoints. 16:40-17:38
