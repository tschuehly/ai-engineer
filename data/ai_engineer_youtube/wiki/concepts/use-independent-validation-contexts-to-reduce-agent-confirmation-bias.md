# Use independent validation contexts to reduce agent confirmation bias

Summary: Validation done inside the same agent context that produced the work can miss defects because the agent is biased toward its own prior decisions. Independent review contexts, such as subagents with smaller context windows, can find issues the main loop overlooks.

Use when:
- A coding agent says its own work is complete but defects still slip through.
- You are designing validation for autonomous or semi-autonomous coding loops.

Details:
- The speaker agrees with an audience observation that same-context validation can become self-affirming, while validation in subagents starts with less context and can find more issues. 55:19-56:24
- Test passing is necessary but not sufficient; the loop should also verify that the intended work was actually done and decide how to report or hand off failures. 51:02-51:43
- The speaker recommends being deliberate about risk and permissions for autonomous agents, especially where the agent has broad access to tools or data. 54:42-55:13
- **A fresh context is necessary but not sufficient, because you choose what goes into it.** Coyle's version specifies the payload: a critic gets "the claim and the evidence… but we're not giving it the thought processes that went in to creating this claim." The failure he is guarding against is convergence — "when you get a bunch of agents together collaborating and talking to each other, there's a tendency to have group think" — so a subagent with a smaller window that is nonetheless handed the producer's reasoning trace has an independent *context* and a borrowed *conclusion*. The generalization is per-agent slicing: "every agent gets its own slice." See [Withhold the Producer's Reasoning From the Critic](withhold-the-producers-reasoning-from-the-critic.md). ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 13:44-15:12)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Ralph loops process one ticket at a time with fresh context](ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md)
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Withhold the Producer's Reasoning From the Critic](withhold-the-producers-reasoning-from-the-critic.md)

Sources:
- [Ralph Loops: Build Dumb AI Loops That Ship - Chris Parsons, Cherrypick](../sources/20260504_2TLXsxkz0zI.md), 51:02-51:43, 54:42-56:24
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](../sources/20260808_Z-c11pV_uvU.md), 13:44-15:12
