# Code World Model: Building World Models for Computation - Jacob Kahn, FAIR Meta

Source: [Code World Model: Building World Models for Computation - Jacob Kahn, FAIR Meta](https://www.youtube.com/watch?v=sYgE4ppDFOQ)
Uploaded: 2025-12-17
Transcript: `raw/20251217_sYgE4ppDFOQ/sYgE4ppDFOQ.en-orig.vtt`

## Summary

Jacob Kahn presents Code World Model as a research direction for training code models on program execution dynamics, not only code syntax. The talk frames code as a constrained world-modeling substrate where models can learn state/action/state transitions from execution traces, use Bash-oriented environments for agentic coding tasks, and eventually simulate program behavior for neural debugging or expensive execution reasoning.

## Extracted Concepts

- [Train code models on execution traces, not only syntax](../concepts/train-code-models-on-execution-traces-not-only-syntax.md) - this source introduces CWM's core claim that execution traces provide a richer representation of code semantics than tokenized source alone.
- [Use neural debugging to fill code by simulated execution](../concepts/use-neural-debugging-to-fill-code-by-simulated-execution.md) - this source describes a model that traces local variables and program state to complete ambiguous code structure.
- [Use Bash as a composable code-mode tool for agents](../concepts/use-bash-as-a-composable-code-mode-tool-for-agents.md) - this source adds CWM's deliberately small, Bash-oriented tool surface for coding-agent training.
- [Build RL environments as software artifacts](../concepts/build-rl-environments-as-software-artifacts.md) - this source adds an asynchronous RL setup with terminal execution, trajectory scoring, queued samplers, and model checkpoint updates.

## Topic Links

- [Models](../topics/models.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

## Notes

- CWM treats world modeling as predicting future observations from past observations and actions, with code chosen because it is constrained and rule-bound. 00:41-01:17
- The talk challenges a pure syntax view of code modeling: token-based autoregressive models see source tokens in and source tokens out, while execution traces expose local variables, memory, line-by-line state, and state transitions. 01:36-03:16
- The state/action/state framing is applied both to program execution and to agentic model decisions: a program state plus the next executed line yields a new state, while an agent action in an environment yields feedback. 03:39-04:38
- CWM is described as a 32B dense transformer trained end to end with pretraining, domain mid-training, long-context mid-training, instruction/reasoning tuning, and joint RL plus agentic reasoning. 06:13-06:51
- The model is trained in a Bash-oriented environment with fewer tools than many coding agents, so it learns terminal commands, file mutation, and code execution in a setting close to an engineer's shell workflow. 06:55-08:05
- The post-training system uses asynchronous samplers, terminal environments, trajectory scoring, trainers, queues, and eager checkpoint exchange to keep throughput high while staying relatively on-policy. 08:43-10:31
- CWM can trace a function line by line and show local variable values, motivating a neural-debugger interface where developers express partial program shape in code and the model fills gaps by simulating execution. 12:01-13:57
- The talk speculates that execution simulation can approximate expensive program reasoning tasks, such as predicting halting behavior or debugging large distributed systems without running every path. 14:01-15:39
