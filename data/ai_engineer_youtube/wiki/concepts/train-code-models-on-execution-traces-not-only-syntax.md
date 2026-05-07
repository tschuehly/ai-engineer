# Train code models on execution traces, not only syntax

Summary: Code models can learn richer program semantics when training data includes execution traces that expose state transitions, local variables, memory, and line-by-line behavior. This reframes code modeling as predicting future program observations from past observations and actions, not just predicting the next source token.

Use when:
- Designing data for code models that need to reason about program behavior.
- Comparing token-only source modeling with execution-aware model training.

Details:
- CWM starts from the question of whether code is only syntax in the editor or the execution behavior behind that syntax; token-based autoregressive models normally see tokenized source as input and predict more source as output. 01:36-02:06
- Execution tracing can represent each executed line with local variables, memory information, and corresponding source-line context, giving the model a structured view of program state transitions. 02:06-03:16
- The same state/action/state framing can describe both executing the next program line and an agent taking an action in an environment, which makes execution traces a bridge between code modeling and agentic reasoning. 03:39-04:38
- The talk extends this idea beyond toy functions to repository-level, distributed-system-level, and code-contest execution traces generated from GitHub PR data, tests, and CI. 03:18-06:03

Related topics:
- [Models](../topics/models.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Build RL environments as software artifacts](build-rl-environments-as-software-artifacts.md)
- [Use Bash as a composable code-mode tool for agents](use-bash-as-a-composable-code-mode-tool-for-agents.md)
- [Sandboxed code execution turns model reasoning into inspectable computation](sandboxed-code-execution-turns-model-reasoning-into-inspectable-computation.md)

Sources:
- [Code World Model: Building World Models for Computation - Jacob Kahn, FAIR Meta](../sources/20251217_sYgE4ppDFOQ.md), 01:36-06:03
