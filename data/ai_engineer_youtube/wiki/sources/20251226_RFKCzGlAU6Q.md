# How Claude Code Works - Jared Zoneraich, PromptLayer

Source: [How Claude Code Works - Jared Zoneraich, PromptLayer](https://www.youtube.com/watch?v=RFKCzGlAU6Q)
Uploaded: 2025-12-26
Transcript: `raw/20251226_RFKCzGlAU6Q/RFKCzGlAU6Q.en-orig.vtt`

## Summary

Jared Zoneraich argues that modern coding agents work because strong models can operate inside a simple master loop with a compact set of tools, filesystem context, sandboxing, and prompt-steered state such as todos. The source is useful for agent harness design because it contrasts flexible model-led exploration with deterministic DAGs, explains where structured tools remain useful for edge cases, and proposes backtests, point-in-time tests, end-to-end checks, and trajectory metrics for evaluating agent behavior.

## Extracted Concepts

- [Run coding agents through a simple master loop](../concepts/run-coding-agents-through-a-simple-master-loop.md) - this source describes Claude Code-style agents as one while loop that executes tool calls and returns results until the model stops calling tools.
- [Use prompt-enforced todos as lightweight agent state](../concepts/use-prompt-enforced-todos-as-lightweight-agent-state.md) - this source frames todos as structured but not deterministically enforced state injected into the system prompt.
- [Put brittle edge cases behind rigorous tools](../concepts/put-brittle-edge-cases-behind-rigorous-tools.md) - this source recommends keeping the master loop flexible while moving high-risk or specific edge cases into versioned, testable tools.
- [Evaluate agent trajectories with backtests and smell metrics](../concepts/evaluate-agent-trajectories-with-backtests-and-smell-metrics.md) - this source highlights the eval difficulty of flexible agent loops and suggests historical backtests plus metrics such as tool-call count, retries, and runtime.

## Topic Links

- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- Claude Code, Codex, Cursor, and Amp are described as using a simple master loop: while there are tool calls, run the tool, return results to the model, and continue until final user-facing output. 11:29-12:09
- The talk treats model flexibility as an architectural asset: the more the system lets the model explore and recover from mistakes, the more it can benefit from stronger future models. 12:17-12:41
- Tooling remains compact but purposeful: read handles token limits on large files, grep/glob can outperform vector retrieval for exact codebase search, Bash is powerful but needs sandboxing, and edit tools can force read-before-write behavior. 12:48-17:37
- Todo lists are useful because they are structured enough to orient the model but prompt-enforced rather than hard-coded workflow state. 17:55-19:24
- The source cautions that DAGs make some guarantees easier but can create hundreds of brittle prompt/classification nodes; a master loop is more maintainable when the task can rely on model exploration. 22:15-23:24
- For sensitive or highly specific behavior, the suggested middle ground is to keep the agent paradigm but implement rigorous tool calls that can be versioned and evaluated. 25:10-25:48
- Skills are framed as an extendable system prompt that can load task-specific context, but the speaker notes that automatic skill selection can fail and may require explicit invocation or better model training. 33:32-37:19
- Unified diffing is recommended for agent edits because it reduces token load, shortens outputs, speeds review, and reduces rewrite-style mistakes. 34:49-35:31
- Flexible master-loop agents are harder to evaluate than fixed workflows; the talk suggests end-to-end task checks, point-in-time tool-selection snapshots, backtests over historical data, and agent-smell metrics such as tool calls, retries, and run time. 49:06-50:34
