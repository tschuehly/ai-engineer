# Build RL Environments as Software Artifacts

Summary: Reinforcement-learning environments for language models should be packaged as runnable software artifacts, not only as static datasets. The environment owns setup, state transitions, parsing, rewards, rollouts, and evaluation or training hooks.

Use when:
- Turning an interactive task into an evaluation or post-training setup.
- Deciding whether a static dataset is enough or a stateful environment is needed.

Details:
- Fiorucci frames RL environments as gyms where LLM agents can use tools, run code, solve multi-step tasks, and learn from interaction and feedback. (00:45-01:02)
- Verifiers packages environments as installable Python packages and provides base classes for single-turn, multi-turn, and tool-using environments, plus parsers, reward functions, model-serving abstraction, parallel trajectories, and trainer integrations. (10:19-11:46)
- In the simple reverse-text environment, `load_environment` prepares the dataset, a parser extracts the model answer, a reward function compares it to ground truth, and a weighted rubric defines the score used for evaluation or training. (11:52-14:20)
- For tic-tac-toe, the environment behaves like a game engine: it stores board state, parses the model's move, checks validity, applies opponent moves, checks win or draw state, and emits the next prompt until the trajectory ends. (19:00-20:52)
- CWM adds a large-scale code-agent training example: samplers execute terminal actions in an environment, trajectories are scored, trainers compute gradients, checkpoints are pushed to samplers, and queued models plus queued trajectories keep asynchronous RL throughput high. 08:43-10:31
- The talk notes that mid-trajectory checkpoint updates can make a trajectory somewhat off-policy, but the system accepts that risk to remove bottlenecks and process more interaction data. 10:34-11:31

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Treat multi-agent systems as distributed systems](treat-multi-agent-systems-as-distributed-systems.md)
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Post-train small models for narrow capabilities](post-train-small-models-for-narrow-capabilities.md)
- [Train code models on execution traces, not only syntax](train-code-models-on-execution-traces-not-only-syntax.md)

Sources:
- [Let LLMs Wander: Engineering RL Environments - Stefano Fiorucci](../sources/20260408_71V3fTaUp2Q.md), 00:45-20:52
- [Code World Model: Building World Models for Computation - Jacob Kahn, FAIR Meta](../sources/20251217_sYgE4ppDFOQ.md), 08:43-11:31
