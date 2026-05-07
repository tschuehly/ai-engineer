# Learn coding preferences from implicit edit feedback

Summary: Coding agents can learn durable preferences by observing how developers revise AI-generated code, then applying those preferences in later runs without requiring manual rule maintenance for every convention.

Use when:
- A reviewer repeatedly makes the same style, architecture, or library-choice corrections to agent output.
- A team wants feedback from normal coding and review behavior to update future agent context.

Details:
- Awais describes wanting the agent to learn from how he edits its code and continuously adapt to his preference set. (00:54-01:09)
- CommandCode's taste file is described as generated from prior behavior, not hand-written by the developer, and the system is presented as learning from both explicit and implicit feedback. (05:50-06:10, 14:58-15:10)
- The `meow` to `commander` example shows preference learning as temporal and contextual: the agent should notice that the developer's CLI convention changed and update the relevant rule without a manual rewrite. (15:37-16:06)
- The workflow reduces the choice between "write code" and "teach the agent to write code" by extracting preferences from the act of writing and reviewing code. (13:17-13:25, 16:06-16:14)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)
- [System prompt learning updates agent rules from eval explanations](system-prompt-learning-updates-agent-rules-from-eval-explanations.md)

Sources:
- [Developing Taste in Coding Agents: Applied Meta Neuro-Symbolic RL - Ahmad Awais, CommandCode](../sources/20251124_kWOQS3XPZ10.md), 00:54-01:09, 05:50-06:10, 13:17-13:25, 14:58-16:14
