# Interleave reasoning and tool calls for long-horizon agents

Summary: Long-horizon agents should be trained and evaluated for repeated think-act-observe loops, not only one reasoning block followed by one set of tool calls and a final answer.

Use when:
- Building agents that must continue after tool errors, incomplete observations, or changing environment state.
- Comparing model support for multi-tool workplace or coding tasks that unfold over many turns.

Details:
- The transcript contrasts a simple tool-use pattern, where the model thinks once, calls tools, reads responses, and finalizes, with real environments that are noisy and dynamic.
- MiniMax describes "interleaved thinking" as repeatedly reasoning after tool responses, deciding whether the information is enough, and taking additional actions when results are suboptimal.
- The pattern can span many tool-call turns inside one user interaction, which makes it closer to a long-running agent loop than to a single function-call completion.
- This behavior is especially relevant when tools can fail, return unexpected results, or require the model to switch tools and plans after observing the environment.

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Models](../topics/models.md)

Related concepts:
- [Run coding agents through a simple master loop](run-coding-agents-through-a-simple-master-loop.md)
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Pair next-token prediction with reinforcement learning for long-horizon work](pair-next-token-prediction-with-reinforcement-learning-for-long-horizon-work.md)

Sources:
- [Minimax M2: Building the #1 Open Model - Olive Song, MiniMax](../sources/20251213_lY1iFbDPRlw.md), 05:42-08:16
