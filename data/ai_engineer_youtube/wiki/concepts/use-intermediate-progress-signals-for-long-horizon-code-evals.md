# Use intermediate progress signals for long-horizon code evals

Summary: Long-horizon codebase tasks need more than final pass/fail correctness because a single terminal score gives too little feedback for multi-hour work. Intermediate progress measures can show whether an agent is moving in the right direction before full completion.

Use when:
- Evaluating codebase translation, large refactors, or other hours-long agent tasks.
- Designing feedback loops for agents whose final correctness signal is sparse or expensive.

Details:
- The source describes translating a complex C compression library into Rust, using a million compression inputs to check correctness of the generated implementation. (12:53-13:42)
- The task originally took about 12 hours in the described work, and even faster future models would still put the task near the frontier of current code-agent capability. (13:42-13:54)
- End-to-end correctness gives only one bit of feedback, which is too sparse for very long-horizon tasks. (13:54-14:05)
- Intermediate signals such as fraction of code translated and fraction of code refactored can reveal progress and help scale systems better. (14:05-14:25)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Separate watched and unwatched agent time horizons](separate-watched-and-unwatched-agent-time-horizons.md)
- [Decompose large refactors into dependency-aware agent batches](decompose-large-refactors-into-dependency-aware-agent-batches.md)

Sources:
- [Coding Evals: From Code Snippets to Codebases - Naman Jain, Cursor](../sources/20251215_tHN44yJoeS8.md), 12:53-14:25
