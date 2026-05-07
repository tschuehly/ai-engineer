# Choose agent observation and action spaces explicitly

Summary: Agent designers should choose the observation and action spaces deliberately instead of inheriting chat turns and tool calls by default. Character-level terminal streams, tool calls, browser controls, desktop frames, and persistent VM state each trade interpretability, responsiveness, capability, and evaluation complexity.

Use when:
- Comparing MCP/tool-call agents with terminal, browser, or computer-use agents.
- Designing benchmarks or environments that need to match the agent's production action surface.

Details:
- Hu frames robotics input modalities and sampling rates as explicit design choices, then points out that agents often discretize time implicitly through conversation turns and full tool-response waits. (04:06-05:20)
- The Terminus agent from Terminal-Bench is cited as an alternative action surface because it uses a terminal stream with character-level input and output, enabling actions such as control-C and window commands. (05:49-06:30)
- Agents can act through MCP/tool calls, character-level computer control, or frame-level mouse and keyboard interaction such as the Dreamer-style 20 FPS desktop approach; the question is which design choice enables or limits the target workflow. (06:33-07:25)
- Stateful VMs and persistent files change the observation space because an agent must account for active processes, current messages, world state, and objects it may need to interact with, not only the current prompt. (07:30-08:41)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Production-matched RL environments train coding agents on real tool surfaces](production-matched-rl-environments-train-coding-agents-on-real-tool-surfaces.md)
- [Browser agents sit in the prompt-injection lethal trifecta](browser-agents-sit-in-the-prompt-injection-lethal-trifecta.md)
- [Use Bash as a composable code-mode tool for agents](use-bash-as-a-composable-code-mode-tool-for-agents.md)

Sources:
- [Agents are Robots Too: What Self-Driving Taught Me About Building Agents - Jesse Hu, Abundant](../sources/20251124_qqXdLf3wy1E.md), 04:06-08:41
