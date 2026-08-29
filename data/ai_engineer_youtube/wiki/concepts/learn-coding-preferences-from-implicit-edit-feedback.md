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

- **The coarse org-scale version of the same implicit signal, used as a quality metric rather than as preference learning.** Uber grades each automated review comment by whether the developer subsequently changed the code — "when a uReview comment is made, does the developer go and actually address the comment?" — reporting an addressal rate of about 67% with nearly three-quarters of high-severity issues addressed. The reason to prefer this over asking is coverage: of about 25,000 comments a week, "we get 10% of them actually get some feedback." Anything requiring a person to respond is measured on a self-selected tenth of the output, while whether the code changed is computable for all of it. The limit is that addressal is not correctness — a developer can comply with a wrong comment — and the talk validates it against no labelled sample. ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 05:47-06:07, 10:12-10:47)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)
- [System prompt learning updates agent rules from eval explanations](system-prompt-learning-updates-agent-rules-from-eval-explanations.md)
- [Operational Outcomes Are Eval Labels You Only See If You Own the Operation](operational-outcomes-are-eval-labels-you-only-see-if-you-own-the-operation.md)
- [Measure a Review Bot by Whether the Comment Changed the Code](measure-a-review-bot-by-whether-the-comment-changed-the-code.md)

Sources:
- [Developing Taste in Coding Agents: Applied Meta Neuro-Symbolic RL - Ahmad Awais, CommandCode](../sources/20251124_kWOQS3XPZ10.md), 00:54-01:09, 05:50-06:10, 13:17-13:25, 14:58-16:14
- [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../sources/20260828_B0fjR3yaZFU.md), 11:49-12:14
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 05:47-06:07, 10:12-10:47
