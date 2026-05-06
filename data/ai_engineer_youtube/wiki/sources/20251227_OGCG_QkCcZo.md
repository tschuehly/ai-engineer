# AGI: The Path Forward - Jason Warner & Eiso Kant, Poolside

Source: [AGI: The Path Forward - Jason Warner & Eiso Kant, Poolside](https://www.youtube.com/watch?v=OGCG_QkCcZo)
Uploaded: 2025-12-27
Transcript: `raw/20251227_OGCG_QkCcZo/OGCG_QkCcZo.en-orig.vtt`

## Summary

Poolside presents a vertically integrated path for long-horizon knowledge-work agents: train models from scratch, pair next-token prediction with reinforcement learning, serve them through coding and web interfaces, and constrain agent behavior carefully in high-consequence environments. The live demo shows an agent translating an Ada codebase to Rust, testing the generated program, adding command-history support with a Rust library, and using Bash scripts and live diffs as verification surfaces.

## Extracted Concepts

- [Pair next-token prediction with reinforcement learning for long-horizon work](../concepts/pair-next-token-prediction-with-reinforcement-learning-for-long-horizon-work.md) - Poolside frames RL as the missing ingredient for moving language models toward more capable autonomous knowledge work.
- [Ratchet agent permissions down in high-consequence code environments](../concepts/ratchet-agent-permissions-down-in-high-consequence-code-environments.md) - the demo stresses that defense and government codebases require tightly scoped data and action access.
- [Treat long-horizon agents as asynchronous workers with evolving interfaces](../concepts/treat-long-horizon-agents-as-asynchronous-workers-with-evolving-interfaces.md) - the speakers describe agents doing hour-long work today and potentially day-long work later, with interfaces expected to change around that capability.

## Topic Links

- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)
- [Workflows](../topics/workflows.md)

## Notes

- Poolside says it builds its own models from scratch and originally bet that next-token prediction needed reinforcement learning to make a larger leap in capability, with Malibu Agent presented as a second-generation model. (00:30-01:00)
- The live coding demo uses a VS Code assistant backed by Poolside Agent to inspect an Ada codebase and convert it to Rust, emphasizing a familiar IDE interface over slides. (01:27-02:56)
- The agent wrote roughly 1,152 lines of code, created files visible in a live diff view, generated test commands, and then returned a summary of its work. (03:27-05:09)
- In high-consequence government and defense environments, the speakers say agents cannot be given broad access to data sources; permissions need to be narrowed to what those organizations are comfortable allowing. (03:17-04:01)
- The demo validates the Rust program manually by running it, creating a table, inserting a record, querying it, and then asking the agent to add command-history support. (05:18-06:39)
- The agent identifies the `rustyline` package for command history, updates files, builds successfully with warnings, writes Bash scripts to test history and demo behavior, and the presenters rerun the program to check the up-arrow workflow. (06:52-07:59)
- Poolside describes the shown coding interface as one expression of the platform, alongside web and downloadable machine-local agents for organizations using the system. (08:20-08:35)
- The speakers describe more compute coming online for the next-generation model, including a claimed 40,000-plus GB300s, and connect scaling compute to stronger capabilities in software development and long-horizon knowledge work. (08:56-10:24)
- They describe current asynchronous agents doing hour-long tasks and expect future agents to do day-long tasks, while the interface continues to evolve around that change. (10:30-10:52)
