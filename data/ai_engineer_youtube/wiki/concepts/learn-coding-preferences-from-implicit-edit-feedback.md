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
- **The same signal outside the editor, and why it is the strongest thing in a feedback pipeline.** Shenoy separates explicit feedback (thumbs up and down, an optional note) from the correction itself: "maybe there's some data that the AI generated and there's a real diff between the data that the AI generated and what was ultimately submitted. That's rich information that almost no one else has." A rating says the output was wrong; the diff says what right looked like, and it costs the user nothing because they had to submit the corrected version anyway. The generalization matters — any AI-drafted artifact that a human commits through a business system yields the same signal, not only code. ([Shenoy](../sources/20260828_B0fjR3yaZFU.md), 11:49-12:14)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)
- [System prompt learning updates agent rules from eval explanations](system-prompt-learning-updates-agent-rules-from-eval-explanations.md)
- [Operational Outcomes Are Eval Labels You Only See If You Own the Operation](operational-outcomes-are-eval-labels-you-only-see-if-you-own-the-operation.md)

Sources:
- [Developing Taste in Coding Agents: Applied Meta Neuro-Symbolic RL - Ahmad Awais, CommandCode](../sources/20251124_kWOQS3XPZ10.md), 00:54-01:09, 05:50-06:10, 13:17-13:25, 14:58-16:14
- [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../sources/20260828_B0fjR3yaZFU.md), 11:49-12:14
